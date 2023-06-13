# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .work_pool import WorkPool
from .work_pool_task import WorkPoolTask
from .work_pool_task import WorkPoolTaskCallbacksContainer, WorkPoolTaskErrorCallback
from oci._vendor.urllib3.exceptions import (
    ReadTimeoutError,
    ProtocolError
)

import heapq
import oci
import os
import six
import threading
import random
import time


MEBIBYTE = 1024 * 1024
OBJECT_GET_CHUNK_SIZE = MEBIBYTE
DEFAULT_RETRY_COUNT = 5


def _make_retrying_get_call(object_storage_client, **kwargs):
    return object_storage_client.get_object(
        kwargs['namespace'],
        kwargs['bucket_name'],
        kwargs['object_name'],
        if_match=kwargs.get('if_match'),
        if_none_match=kwargs.get('if_none_match'),
        range=kwargs.get('range'),
        opc_client_request_id=kwargs.get('request_id'),
        opc_sse_customer_algorithm=kwargs.get('opc_sse_customer_algorithm'),
        opc_sse_customer_key=kwargs.get('opc_sse_customer_key'),
        opc_sse_customer_key_sha256=kwargs.get('opc_sse_customer_key_sha256')
    )


# Retry the given function with exponential backoff until either retry count is zero or exception is not retryable
def _retry_with_backoff(fn, *fn_args, **kwargs):
    retries = DEFAULT_RETRY_COUNT
    backoff_multiplier_in_secs = 1
    if 'retries' in kwargs:
        retries = kwargs["retries"]
    if 'backoff_multiplier_in_secs' in kwargs:
        backoff_multiplier_in_secs = kwargs["backoff_multiplier_in_secs"]
    retry_count = 0

    while True:
        try:
            return fn(*fn_args)
        except Exception as e:
            # Raise if retries are exhausted or exception is not retryable
            if (retry_count == retries) or (not _is_retryable(e)):
                raise
            sleep = (backoff_multiplier_in_secs * 2 ** retry_count + random.uniform(0, 1))
            time.sleep(sleep)
            retry_count += 1


# Check if the exception is retryable, currently this is either ConnectionError or ReadTimeoutError
# or ProtocolError (which can be due either ConnectionResetError or ReadIncompleteError)
def _is_retryable(exception):
    if isinstance(exception, (ConnectionError, ReadTimeoutError, ProtocolError)):
        return True
    return False


# A task which can retrieve an object from Object Storage and write it to a file
class GetObjectTask(WorkPoolTask):
    def __init__(self, object_storage_client, callbacks_container, **kwargs):
        super(GetObjectTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.kwargs = kwargs

    def do_work_hook(self):
        get_object_response = _make_retrying_get_call(self.object_storage_client, **self.kwargs)
        try:
            with open(self.kwargs['full_file_path'], "wb") as file:
                for chunk in get_object_response.data.raw.stream(OBJECT_GET_CHUNK_SIZE, decode_content=False):
                    file.write(chunk)
        except IOError as e:
            # IsADirectoryError, PermissionError
            if e.errno == 21 or (e.errno == 13 and os.path.isdir(self.kwargs['full_file_path'])):
                pass
            else:
                raise


# A task which coordinates getting an object in multiple parts (using ranged GetObject calls), combining them and then sending them
# to their output destination. It does this by:
#
#   - Figuring out what the ranges are
#   - Sending those to be procesed by the appropriate worker pool
#   - Spawning an extra thread to coordinate writing data in the right order and as it becomes ready to the destination. We have an
#     extra thread for this so that we can write as we go rather than waiting until the end (this is also handier for piping/streaming scenarios
#     since the other end is probably not expecting to get everything all at once)
class GetObjectMultipartTask(WorkPoolTask):
    DEFAULT_MULTIPART_DOWNLOAD_SIZE = 10 * MEBIBYTE

    def __init__(self, object_storage_client, callbacks_container, object_storage_request_pool, destination_file_handle, **kwargs):
        super(GetObjectMultipartTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.object_storage_request_pool = object_storage_request_pool
        self.range_tuples = []

        self.kwargs = kwargs.copy()
        self.multipart_download_threshold = self.kwargs['multipart_download_threshold']
        self.kwargs.pop('multipart_download_threshold')

        if 'chunk_written_callback' in self.kwargs:
            self.chunk_written_callback = self.kwargs['chunk_written_callback']
            self.kwargs.pop('chunk_written_callback')
        else:
            self.chunk_written_callback = None

        if 'part_completed_callback' in self.kwargs:
            self.part_completed_callback = self.kwargs['part_completed_callback']
            self.kwargs.pop('part_completed_callback')
        else:
            self.part_completed_callback = None

        if 'part_size' in self.kwargs:
            self.part_size = self.kwargs['part_size']
            self.kwargs.pop('part_size')
        else:
            self.part_size = self.DEFAULT_MULTIPART_DOWNLOAD_SIZE

        if isinstance(destination_file_handle, six.string_types):
            # If it's a string, treat it like a file path. Also, since we open the file of our own volition, close it after we're
            # done. To constrast, if someone provided us something we assume is a file (or file-like) then don't auto-close because
            # they may want to do something with it after we've done our work
            self.destination_file_handle = open(destination_file_handle, 'wb')
            self.auto_close_destination_file = True
        else:
            self.destination_file_handle = destination_file_handle
            self.auto_close_destination_file = False

        self.add_pending_write_lock = threading.Lock()
        self.all_done_lock = threading.Lock()
        self.pending_writes = PendingWrites(self.all_done_lock)
        self.io_writer_pool = WorkPool(pool_size=1, max_workers=1)  # Only one thing writes to the destination

    def do_work_hook(self):
        if 'total_size' in self.kwargs:
            content_length = self.kwargs['total_size']
        else:
            head_object_result = self._make_retrying_head_object_call()
            if not head_object_result:
                raise RuntimeError('Cannot download object as it does not exist')
            content_length = int(head_object_result.headers['Content-Length'])
            if self.part_completed_callback:
                self.part_completed_callback(1, total_bytes=content_length)

        if content_length <= self.multipart_download_threshold:
            # If the content is not larget than the threshold then just grab the object and put it where it needs to go
            get_object_response = _make_retrying_get_call(self.object_storage_client, **self.kwargs)
            for chunk in get_object_response.data.raw.stream(OBJECT_GET_CHUNK_SIZE, decode_content=False):
                self.destination_file_handle.write(chunk)
        else:
            # According to https://tools.ietf.org/rfc/rfc7233 section 2.1, we want things like:
            #
            #   bytes=0-499 (first 500 bytes, inclusive)
            #   bytes=500-999 (second 500 bytes, inclusive)
            start_byte = 0
            end_byte = self.part_size - 1
            tuple_counter = 0

            while end_byte < content_length:
                if start_byte != end_byte:
                    self.range_tuples.append(
                        (
                            tuple_counter,
                            {'range': 'bytes={}-{}'.format(start_byte, end_byte)}
                        )
                    )

                tuple_counter += 1

                # Next window of bytes
                start_byte = start_byte + self.part_size
                end_byte = end_byte + self.part_size

                if start_byte >= content_length:
                    break

                # Don't overshoot the end part of the window
                if end_byte >= content_length:
                    end_byte = content_length - 1

            self.pending_writes.total_parts = len(self.range_tuples)

            errors = list()

            for rt in self.range_tuples:
                failure_callback_kwargs = {'errors': errors}
                failure_callback = WorkPoolTaskErrorCallback(self._enqueue_errors, **failure_callback_kwargs)

                release_lock_on_error_kwargs = {}
                release_lock_on_failure_callback = WorkPoolTaskErrorCallback(self.pending_writes.release_lock_on_error, **release_lock_on_error_kwargs)

                callbacks_container = WorkPoolTaskCallbacksContainer(error_callbacks=[failure_callback, release_lock_on_failure_callback])

                copy_kwargs = self.kwargs.copy()
                copy_kwargs['range'] = rt[1]['range']
                copy_kwargs['part_completed_callback'] = self.part_completed_callback
                copy_kwargs['chunk_written_callback'] = self.chunk_written_callback
                get_object_range_task = GetObjectRangeTask(
                    self.object_storage_client,
                    callbacks_container,
                    self.destination_file_handle,
                    rt[0],
                    self.io_writer_pool,
                    self.add_pending_write_lock,
                    self.pending_writes,
                    **copy_kwargs
                )

                # Because we delegate work to another pool, errors could happen anytime so check before and after we submit work (noting that submitting work is a blocking
                # operation if the pool does not have any slots available)
                self._handle_errors(errors)
                self.object_storage_request_pool.submit(get_object_range_task)
                self._handle_errors(errors)

            # This blocks until something makes the PendingWrites object releases the lock
            self.all_done_lock.acquire()

            # Make sure that the IO pool has no pending tasks (it probably shouldn't because we've released the lock by this point)
            self.io_writer_pool.wait_for_completion()

            self._handle_errors(errors)

        if self.auto_close_destination_file:
            self.destination_file_handle.close()

    def _enqueue_errors(self, **kwargs):
        kwargs['errors'].append(str(kwargs['callback_exception']))

    def _handle_errors(self, errors):
        if not errors:
            return

        raise RuntimeError('Error downloading parts: {}'.format('\n'.join(errors)))

    def _make_retrying_head_object_call(self):
        try:
            return self.object_storage_client.head_object(
                namespace_name=self.kwargs['namespace'],
                bucket_name=self.kwargs['bucket_name'],
                object_name=self.kwargs['object_name'],
                if_match=self.kwargs.get('if_match'),
                if_none_match=self.kwargs.get('if_none_match'),
                opc_client_request_id=self.kwargs.get('request_id'),
                opc_sse_customer_algorithm=self.kwargs.get('opc_sse_customer_algorithm'),
                opc_sse_customer_key=self.kwargs.get('opc_sse_customer_key'),
                opc_sse_customer_key_sha256=self.kwargs.get('opc_sse_customer_key_sha256')

            )
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                return None
            else:
                raise


# A task which can retrieve a range of bytes for an object from object storage. Intended for internal use by GetObjectMultipartTask and not as a general task.
class GetObjectRangeTask(WorkPoolTask):
    def __init__(self, object_storage_client, callbacks_container, destination_file_handle, tuple_counter, io_writer_pool, add_pending_write_lock, pending_writes, **kwargs):
        super(GetObjectRangeTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.kwargs = kwargs
        self.tuple_counter = tuple_counter
        self.io_writer_pool = io_writer_pool
        self.pending_writes = pending_writes
        self.add_pending_write_lock = add_pending_write_lock
        self.retry_count = 0 if isinstance(self.object_storage_client.retry_strategy, oci.retry.NoneRetryStrategy) else DEFAULT_RETRY_COUNT
        self.destination_file_handle = destination_file_handle
        self.downloaded_data = six.BytesIO()

        if 'chunk_written_callback' in self.kwargs:
            self.chunk_written_callback = self.kwargs['chunk_written_callback']
            self.kwargs.pop('chunk_written_callback')
        else:
            self.chunk_written_callback = None

        if 'part_completed_callback' in self.kwargs:
            self.part_completed_callback = self.kwargs['part_completed_callback']
            self.kwargs.pop('part_completed_callback')
        else:
            self.part_completed_callback = None

    def do_work_hook(self):
        # Get object request -> stream data with retries (connection breaks during data streaming will raise urllib
        # exceptions which are being caught in _retry_with_backoff)
        self.downloaded_data = _retry_with_backoff(self._get_object, retries=self.retry_count)

        # PendingWrites uses heapq, which is not thread safe, so we need to lock it
        with self.add_pending_write_lock:
            parts_to_write = self.pending_writes.process_pending_write(self.tuple_counter, self.downloaded_data)
            self.io_writer_pool.submit(
                GetObjectRangeIOWriterTask(
                    WorkPoolTaskCallbacksContainer(error_callbacks=self.get_error_callbacks()),  # Pass along any error callbacks so that we can signal the parent task that something bad has happened
                    parts_to_write=parts_to_write,
                    destination_file_handle=self.destination_file_handle,
                    pending_writes=self.pending_writes,
                    chunk_written_callback=self.chunk_written_callback,
                    part_completed_callback=self.part_completed_callback
                )
            )

    def _get_object(self):
        downloaded_data = six.BytesIO()
        get_object_response = _make_retrying_get_call(self.object_storage_client, **self.kwargs)
        total_size = 0
        for chunk in get_object_response.data.raw.stream(None, decode_content=False):
            downloaded_data.write(chunk)
            total_size += len(chunk)
            if self.chunk_written_callback:
                self.chunk_written_callback(len(chunk))
        if self.part_completed_callback:
            self.part_completed_callback(total_size)
        return downloaded_data


class GetObjectRangeIOWriterTask(WorkPoolTask):
    READ_WRITE_CHUNK_SIZE = 10 * MEBIBYTE

    def __init__(self, callbacks_container, **kwargs):
        super(GetObjectRangeIOWriterTask, self).__init__(callbacks_container=callbacks_container)
        self.parts_to_write = kwargs['parts_to_write']
        self.destination_file_handle = kwargs['destination_file_handle']
        self.pending_writes = kwargs['pending_writes']
        self.chunk_written_callback = kwargs.get('chunk_written_callback')
        self.part_completed_callback = kwargs.get('part_completed_callback')

    def do_work_hook(self):
        total_size = 0
        for part in self.parts_to_write:
            part[1].seek(0)
            self.destination_file_handle.write(part[1].read())
            if self.part_completed_callback:
                self.part_completed_callback(part[1].tell() / 2)
            part[1].close()
            self.pending_writes.increment_written_parts()

        if self.part_completed_callback:
            self.part_completed_callback(total_size)

        # After we have written this set of parts, check if we have written all the parts. This also signals back to the overarching
        # GetObjectMultipartTask that all the work has been done
        self.pending_writes.check_if_all_parts_written()


# Stores the writes we have left to do. Has a lock which it acquires on initialization and releases
# once all parts have been written to their destination
class PendingWrites(object):
    def __init__(self, all_done_lock):
        self.pending = []
        self.next_part = 0  # Always start at zero
        self._written_parts = 0
        self._total_parts = 0
        self.all_done_lock = all_done_lock
        self.written_parts_lock = threading.Lock()

        self.all_done_lock.acquire()

    @property
    def total_parts(self):
        return self._total_parts

    @total_parts.setter
    def total_parts(self, value):
        self._total_parts = value

    def increment_written_parts(self):
        with self.written_parts_lock:
            self._written_parts += 1

    def process_pending_write(self, tuple_counter, data):
        heapq.heappush(self.pending, (tuple_counter, data))

        able_to_write = []
        while self.pending and self.pending[0][0] == self.next_part:
            able_to_write.append(heapq.heappop(self.pending))
            self.next_part += 1

        return able_to_write

    def check_if_all_parts_written(self):
        if not self.pending and self._written_parts == self._total_parts:
            self.all_done_lock.release()

    def release_lock_on_error(self, **kwargs):
        self.all_done_lock.release()
