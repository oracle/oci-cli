# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci import exceptions
from .work_pool_task import WorkPoolTask


# A task which can HEAD an object from Object Storage
class HeadObjectTask(WorkPoolTask):
    def __init__(self, object_storage_client, callbacks_container, **kwargs):
        super(HeadObjectTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.kwargs = kwargs

    def do_work_hook(self):
        return self._make_retrying_head_object_call()

    def _make_retrying_head_object_call(self):
        try:
            return self.object_storage_client.head_object(**self.kwargs)
        except exceptions.ServiceError as e:
            if e.status == 404:
                return None
            else:
                raise
