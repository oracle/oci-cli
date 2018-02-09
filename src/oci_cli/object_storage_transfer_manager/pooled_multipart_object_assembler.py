# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from oci.object_storage.transfer.internal.multipart_object_assembler import MultipartObjectAssembler


# A version of MultipartObjectAssember which accepts an explicit pool to use to do parallel requests
class PooledMultipartObjectAssembler(MultipartObjectAssembler, object):
    def __init__(self, object_storage_client, namespace_name, bucket_name, object_name, object_storage_request_pool, **kwargs):
        super(PooledMultipartObjectAssembler, self).__init__(object_storage_client, namespace_name, bucket_name, object_name, **kwargs)
        self.object_storage_request_pool = object_storage_request_pool

    def upload(self, **kwargs):
        if self.manifest["uploadId"] is None:
            raise RuntimeError('Cannot call upload before initializing an upload using new_upload.')

        self.object_storage_request_pool.map(lambda part_tuple: self._upload_part(part_num=part_tuple[0] + 1, part=part_tuple[1], **kwargs), enumerate(self.manifest["parts"]))
