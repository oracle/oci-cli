# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .work_pool_task import WorkPoolTask

from retrying import retry
from .. import retry_utils


# A task which deletes objects from Object Storage
class DeleteObjectTask(WorkPoolTask):
    def __init__(self, object_storage_client, callbacks_container, **kwargs):
        super(DeleteObjectTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.kwargs = kwargs

    def do_work_hook(self):
        self._make_retrying_delete_object_call(self.object_storage_client, **self.kwargs)

    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000, wait_jitter_max=2000,
           retry_on_exception=retry_utils.retry_on_timeouts_connection_internal_server_and_throttles)
    def _make_retrying_delete_object_call(self, client, **kwargs):
        client.delete_object(
            kwargs['namespace'],
            kwargs['bucket_name'],
            kwargs['object_name'],
            if_match=kwargs.get('if_match'),
            opc_client_request_id=kwargs.get('request_id')
        )
