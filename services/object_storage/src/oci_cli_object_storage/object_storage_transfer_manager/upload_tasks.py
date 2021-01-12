# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci.object_storage import UploadManager
from .work_pool_task import WorkPoolTask
from retrying import retry
from oci_cli import retry_utils
from oci_cli import cli_util


# A simple task which uploads a single file to Object Storage
class SimpleSingleUploadTask(WorkPoolTask):
    def __init__(self, object_storage_client, namespace_name, bucket_name, object_name, file_path, callbacks_container, verify_checksum, **kwargs):
        super(SimpleSingleUploadTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.namespace_name = namespace_name
        self.bucket_name = bucket_name
        self.object_name = object_name
        self.file_path = file_path
        self.kwargs = kwargs.copy()  # Copy because we're going to potentially do some destructive stuff to the dict below
        self.verify_checksum = verify_checksum

        # These are not valid for single uploads, so remove them if present
        self.kwargs.pop('allow_parallel_uploads', None)
        self.kwargs.pop('parallel_process_count', None)
        self.kwargs.pop('part_size', None)

    def do_work_hook(self):
        multipart_hash = cli_util.verify_checksum(self.file_path, no_multipart=True, ma=None) if self.verify_checksum else None
        return self._make_retrying_upload_file_call(), multipart_hash

    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000, wait_jitter_max=2000,
           retry_on_exception=retry_utils.retry_on_timeouts_connection_internal_server_and_throttles)
    def _make_retrying_upload_file_call(self):
        upload_manager = UploadManager(self.object_storage_client, allow_multipart_uploads=False)
        return upload_manager.upload_file(self.namespace_name, self.bucket_name, self.object_name, self.file_path, **self.kwargs)
