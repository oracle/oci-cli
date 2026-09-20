# either license.

import io
import mock

from services.object_storage.src.oci_cli_object_storage.object_storage_transfer_manager.get_object_tasks import (
    GetObjectMultipartTask,
    _make_retrying_get_call
)
from services.object_storage.src.oci_cli_object_storage.object_storage_transfer_manager.work_pool_task import (
    WorkPoolTaskCallbacksContainer
)


def test_make_retrying_get_call_passes_version_id():
    client = mock.Mock()

    _make_retrying_get_call(
        client,
        namespace='namespace',
        bucket_name='bucket',
        object_name='object',
        request_id='request-id',
        range='bytes=0-10',
        version_id='version-id'
    )

    client.get_object.assert_called_once_with(
        'namespace',
        'bucket',
        'object',
        if_match=None,
        if_none_match=None,
        range='bytes=0-10',
        opc_client_request_id='request-id',
        version_id='version-id',
        opc_sse_customer_algorithm=None,
        opc_sse_customer_key=None,
        opc_sse_customer_key_sha256=None
    )


def test_multipart_head_object_call_passes_version_id():
    client = mock.Mock()
    request_pool = mock.Mock()
    task = GetObjectMultipartTask(
        client,
        WorkPoolTaskCallbacksContainer(),
        request_pool,
        io.BytesIO(),
        namespace='namespace',
        bucket_name='bucket',
        object_name='object',
        request_id='request-id',
        multipart_download_threshold=128,
        version_id='version-id'
    )

    task._make_retrying_head_object_call()

    client.head_object.assert_called_once_with(
        namespace_name='namespace',
        bucket_name='bucket',
        object_name='object',
        if_match=None,
        if_none_match=None,
        opc_client_request_id='request-id',
        version_id='version-id',
        opc_sse_customer_algorithm=None,
        opc_sse_customer_key=None,
        opc_sse_customer_key_sha256=None
    )
