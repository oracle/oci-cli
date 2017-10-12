# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .work_pool_task import WorkPoolTask

from retrying import retry
from .. import retry_utils


# A task which can retrieve an object from Object Storage
class GetObjectTask(WorkPoolTask):
    MEBIBYTE = 1024 * 1024
    OBJECT_GET_CHUNK_SIZE = MEBIBYTE

    def __init__(self, object_storage_client, callbacks_container, **kwargs):
        super(GetObjectTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.kwargs = kwargs

    def do_work_hook(self):
        get_object_response = self._make_retrying_get_call()

        with open(self.kwargs['full_file_path'], "wb") as file:
            for chunk in get_object_response.data.raw.stream(self.OBJECT_GET_CHUNK_SIZE, decode_content=False):
                file.write(chunk)

    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000, wait_jitter_max=2000,
           retry_on_exception=retry_utils.retry_on_timeouts_connection_internal_server_and_throttles)
    def _make_retrying_get_call(self):
        return self.object_storage_client.get_object(
            self.kwargs['namespace'],
            self.kwargs['bucket_name'],
            self.kwargs['object_name'],
            if_match=self.kwargs.get('if_match'),
            if_none_match=self.kwargs.get('if_none_match'),
            range=self.kwargs.get('range'),
            opc_client_request_id=self.kwargs.get('request_id')
        )
