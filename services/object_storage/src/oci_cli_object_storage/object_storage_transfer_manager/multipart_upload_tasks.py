# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .pooled_multipart_object_assembler import PooledMultipartObjectAssembler
from .work_pool_task import WorkPoolTask
from oci_cli import cli_util


# A task which prepares a multipart upload by:
#
#   - Creating a new multipart upload
#   - Breaking the file to upload into parts
#   - Sending the upload tasks to the main request pool
#   - Committing the multipart upload when done
class MultipartUploadProcessorTask(WorkPoolTask):
    def __init__(self, object_storage_client, namespace_name, bucket_name, object_name, file_path, callbacks_container, object_storage_request_pool, part_size, verify_checksum, **multipart_kwargs):
        super(MultipartUploadProcessorTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.namespace_name = namespace_name
        self.bucket_name = bucket_name
        self.object_name = object_name
        self.file_path = file_path
        self.multipart_kwargs = multipart_kwargs.copy()
        self.part_size = part_size
        self.object_storage_request_pool = object_storage_request_pool
        self.verify_checksum = verify_checksum

        if 'multipart_part_completion_callback' in self.multipart_kwargs:
            self.multipart_part_completion_callback = self.multipart_kwargs['multipart_part_completion_callback']
            self.multipart_kwargs.pop('multipart_part_completion_callback')
        else:
            self.multipart_part_completion_callback = None

    def do_work_hook(self):
        if 'content_md5' in self.multipart_kwargs:
            self.multipart_kwargs.pop('content_md5')

        self.multipart_kwargs['part_size'] = self.part_size
        ma = PooledMultipartObjectAssembler(self.object_storage_client, self.namespace_name, self.bucket_name, self.object_name, self.object_storage_request_pool, **self.multipart_kwargs)

        ma.new_upload()
        ma.add_parts_from_file(self.file_path)
        if self.multipart_part_completion_callback:
            ma.upload(progress_callback=self.multipart_part_completion_callback)
        else:
            ma.upload()
        response = ma.commit()

        multipart_hash = cli_util.verify_checksum(self.file_path, no_multipart=False, ma=ma) if self.verify_checksum else None
        return response, multipart_hash
