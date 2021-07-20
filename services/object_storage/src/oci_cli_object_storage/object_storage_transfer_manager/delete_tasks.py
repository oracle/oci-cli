# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .work_pool_task import WorkPoolTask


# A task which deletes objects from Object Storage
class DeleteObjectTask(WorkPoolTask):
    def __init__(self, object_storage_client, callbacks_container, **kwargs):
        super(DeleteObjectTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.kwargs = kwargs

    def do_work_hook(self):
        self._make_retrying_delete_object_call(self.object_storage_client, **self.kwargs)

    def _make_retrying_delete_object_call(self, client, **kwargs):
        client.delete_object(
            kwargs['namespace'],
            kwargs['bucket_name'],
            kwargs['object_name'],
            if_match=kwargs.get('if_match'),
            opc_client_request_id=kwargs.get('request_id'),
            version_id=kwargs.get('version_id')
        )


# A task which deletes PARs from object storage
class DeletePreAuthenticatedRequestTask(WorkPoolTask):
    def __init__(self, object_storage_client, callbacks_container, **kwargs):
        super(DeletePreAuthenticatedRequestTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.kwargs = kwargs

    def do_work_hook(self):
        self._make_retrying_delete_par_call(self.object_storage_client, **self.kwargs)

    def _make_retrying_delete_par_call(self, client, **kwargs):
        client.delete_preauthenticated_request(
            kwargs['namespace'],
            kwargs['bucket_name'],
            kwargs['par_id'],
            opc_client_request_id=kwargs.get('request_id')
        )


# A task which deletes Replication Policies from object storage
class DeleteReplicationPolicyTask(WorkPoolTask):
    def __init__(self, object_storage_client, callbacks_container, **kwargs):
        super(DeleteReplicationPolicyTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.kwargs = kwargs

    def do_work_hook(self):
        self._make_retrying_delete_rep_policy_call(self.object_storage_client, **self.kwargs)

    def _make_retrying_delete_rep_policy_call(self, client, **kwargs):
        client.delete_replication_policy(
            kwargs['namespace'],
            kwargs['bucket_name'],
            kwargs['replication_id'],
            opc_client_request_id=kwargs.get('request_id')
        )


# A task which deletes Uploads which are yet to be committed
class DeleteUploadTask(WorkPoolTask):
    def __init__(self, object_storage_client, callbacks_container, **kwargs):
        super(DeleteUploadTask, self).__init__(callbacks_container=callbacks_container)

        self.object_storage_client = object_storage_client
        self.kwargs = kwargs

    def do_work_hook(self):
        self._make_retrying_delete_upload_call(self.object_storage_client, **self.kwargs)

    def _make_retrying_delete_upload_call(self, client, **kwargs):
        client.abort_multipart_upload(
            kwargs['namespace'],
            kwargs['bucket_name'],
            kwargs['object_name'],
            kwargs['upload_id'],
            opc_client_request_id=kwargs.get('request_id')
        )
