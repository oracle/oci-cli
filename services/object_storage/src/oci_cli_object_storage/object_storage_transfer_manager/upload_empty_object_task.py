# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates. All rights reserved.

from oci.object_storage import UploadManager

from oci_cli import cli_util
from .work_pool_task import WorkPoolTask
from oci.retry import DEFAULT_RETRY_STRATEGY


# A task which uploads a single empty object to Object Storage
class SingleEmptyObjectUploadTask(WorkPoolTask):
    def __init__(self, object_storage_client, namespace_name, bucket_name, object_name, input_stream, callbacks_container, verify_checksum, **kwargs):
        super(SingleEmptyObjectUploadTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.namespace_name = namespace_name
        self.bucket_name = bucket_name
        self.object_name = object_name
        self.input_stream = input_stream
        self.kwargs = kwargs.copy()  # Copy because we're going to potentially do some destructive stuff to the dict below
        self.verify_checksum = verify_checksum

        # These are not valid for single uploads, so remove them if present
        self.kwargs.pop('allow_parallel_uploads', None)
        self.kwargs.pop('parallel_process_count', None)
        self.kwargs.pop('part_size', None)

    def do_work_hook(self):
        multipart_hash = cli_util.verify_checksum(self.file_path, no_multipart=True,
                                                  ma=None) if self.verify_checksum else None
        return self._make_retrying_upload_stream_call(), multipart_hash

    def _make_retrying_upload_stream_call(self):
        self.kwargs["retry_strategy"] = DEFAULT_RETRY_STRATEGY
        upload_manager = UploadManager(self.object_storage_client, allow_multipart_uploads=False)
        return upload_manager.upload_stream(self.namespace_name, self.bucket_name, self.object_name, self.input_stream, **self.kwargs)
