# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import requests

from oci.object_storage import UploadManager

from .work_pool import WorkPool
from .delete_tasks import DeleteObjectTask
from .get_object_tasks import GetObjectTask, GetObjectMultipartTask
from .head_object_tasks import HeadObjectTask
from .multipart_upload_tasks import MultipartUploadProcessorTask
from .upload_tasks import SimpleSingleUploadTask


class TransferManager():
    REQUESTS_POOL_SIZE_FACTOR = 4

    def __init__(self, object_storage_client, transfer_manager_config):
        self._client = object_storage_client
        self._config = transfer_manager_config
        self._object_storage_request_pool = WorkPool(pool_size=self._config.max_object_storage_requests, max_workers=self._config.max_object_storage_requests)

        # This is an intermediary pool where multipart uploads will go to be processed. "Processed" in this context means setting up a multipart upload (e.g. manifest,
        # what the file chunks are) and then put those requests in the main request pool to be done, and then committing the upload at the end.
        self._multipart_upload_processor_pool = WorkPool(pool_size=self._config.max_multipart_files_to_process, max_workers=self._config.max_multipart_files_to_process)

        # This is a pool which is intended to process multipart upload/download requests to Object Storage only. We have a separate pool to prevent too much contention between
        # very big uploads/downloads and other tasks (as a single multipart could consume all the processes in the pool, which may be undesirable depending on other
        # work which has been queued)
        self._object_storage_multipart_request_pool = WorkPool(pool_size=self._config.max_object_storage_multipart_requests, max_workers=self._config.max_object_storage_multipart_requests)

        # Increase the pool_maxsize since we'll have multiple threads/processes doing work and calling service operations.
        # See: https://laike9m.com/blog/requests-secret-pool_connections-and-pool_maxsize,89/
        requests_pool_size = self.REQUESTS_POOL_SIZE_FACTOR * self._config.max_object_storage_requests
        adapter = requests.adapters.HTTPAdapter(pool_maxsize=requests_pool_size)
        self._client.base_client.session.mount('https://', adapter)

    def upload_object(self, callbacks_container, namespace_name, bucket_name, object_name, file_path, file_size, **kwargs):
        if not self._config.use_multipart_uploads:
            upload_task = SimpleSingleUploadTask(self._client, namespace_name, bucket_name, object_name, file_path, callbacks_container)
            return self._object_storage_request_pool.submit(upload_task)

        part_size = self._config.multipart_part_size
        if 'part_size' in kwargs:
            part_size = kwargs['part_size']
            kwargs.pop('part_size')

        if not UploadManager._use_multipart(file_size, part_size=part_size):
            if 'multipart_part_completion_callback' in kwargs:
                kwargs.pop('multipart_part_completion_callback')

            upload_task = SimpleSingleUploadTask(self._client, namespace_name, bucket_name, object_name, file_path, callbacks_container, **kwargs)
            return self._object_storage_request_pool.submit(upload_task)
        else:
            multipart_upload_processor_task = MultipartUploadProcessorTask(
                self._client, namespace_name, bucket_name, object_name, file_path, callbacks_container,
                self._object_storage_multipart_request_pool, part_size,
                **kwargs
            )
            return self._multipart_upload_processor_pool.submit(multipart_upload_processor_task)

    def get_object(self, callbacks_container, **kwargs):
        get_object_task = GetObjectTask(self._client, callbacks_container, **kwargs)
        return self._object_storage_request_pool.submit(get_object_task)

    def get_object_multipart(self, callbacks_container, destination_file_handle, **kwargs):
        get_object_multipart_task = GetObjectMultipartTask(self._client, callbacks_container, self._object_storage_multipart_request_pool, destination_file_handle, **kwargs)
        return self._object_storage_request_pool.submit(get_object_multipart_task)

    def delete_object(self, callbacks_container, **kwargs):
        delete_task = DeleteObjectTask(self._client, callbacks_container, **kwargs)
        return self._object_storage_request_pool.submit(delete_task)

    def head_object(self, callbacks_container, **kwargs):
        head_object_task = HeadObjectTask(self._client, callbacks_container, **kwargs)
        return self._object_storage_request_pool.submit(head_object_task)

    def wait_for_completion(self):
        self._object_storage_request_pool.wait_for_completion()
        self._multipart_upload_processor_pool.wait_for_completion()
        self._object_storage_multipart_request_pool.wait_for_completion()
