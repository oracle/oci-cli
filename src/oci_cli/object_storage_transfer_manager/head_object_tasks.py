# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from oci import exceptions
from retrying import retry
from .work_pool_task import WorkPoolTask
from .. import retry_utils


# A task which can HEAD an object from Object Storage
class HeadObjectTask(WorkPoolTask):
    def __init__(self, object_storage_client, callbacks_container, **kwargs):
        super(HeadObjectTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.kwargs = kwargs

    def do_work_hook(self):
        return self._make_retrying_head_object_call()

    @retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000, wait_exponential_max=10000, wait_jitter_max=2000,
           retry_on_exception=retry_utils.retry_on_timeouts_connection_internal_server_and_throttles)
    def _make_retrying_head_object_call(self):
        try:
            return self.object_storage_client.head_object(**self.kwargs)
        except exceptions.ServiceError as e:
            if e.status == 404:
                return None
            else:
                raise
