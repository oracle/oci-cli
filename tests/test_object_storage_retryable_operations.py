try:
    import unittest.mock as mock
except ImportError:
    import mock

import oci
import oci_cli
import pytest
import six

from requests.exceptions import Timeout
from requests.exceptions import ConnectionError


def test_get_object_retry_timeout_exhaust_retries():
    mock_client = create_mock_get_object_client([Timeout(), Timeout(), Timeout()])

    with pytest.raises(Timeout):
        oci_cli.object_storage_cli.retrying_get_object(mock_client, None, "namespace", "bucket_name", "object", None, None, None, six.StringIO(), None, None, None)

    assert mock_client.get_object.call_count == 3


def test_get_object_retry_connection_error_exhaust_retries():
    mock_client = create_mock_get_object_client([ConnectionError(), ConnectionError(), ConnectionError()])

    with pytest.raises(ConnectionError):
        oci_cli.object_storage_cli.retrying_get_object(mock_client, None, "namespace", "bucket_name", "object", None, None, None, six.StringIO(), None, None, None)

    assert mock_client.get_object.call_count == 3


def test_get_object_retry_internal_server_error_exhaust_retries():
    mock_client = create_mock_get_object_client([
        oci.exceptions.ServiceError(500, "blah", {}, "blah"),
        oci.exceptions.ServiceError(501, "blah", {}, "blah"),
        oci.exceptions.ServiceError(502, "blah", {}, "blah")
    ])

    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_get_object(mock_client, None, "namespace", "bucket_name", "object", None, None, None, six.StringIO(), None, None, None)

    assert mock_client.get_object.call_count == 3
    assert exception.value.status == 502


def test_get_object_retry_unknown_service_error_exhaust_retries():
    mock_client = create_mock_get_object_client([
        oci.exceptions.ServiceError(-1, "blah", {}, "blah"),
        oci.exceptions.ServiceError(-1, "blah", {}, "blah"),
        oci.exceptions.ServiceError(-1, "blah", {}, "blah")
    ])

    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_get_object(mock_client, None, "namespace", "bucket_name", "object", None, None, None, six.StringIO(), None, None, None)

    assert mock_client.get_object.call_count == 3
    assert exception.value.status == -1


def test_get_object_retry_throttles_exhaust_retries():
    mock_client = create_mock_get_object_client([
        oci.exceptions.ServiceError(429, "blah", {}, "blah"),
        oci.exceptions.ServiceError(429, "blah", {}, "blah"),
        oci.exceptions.ServiceError(429, "blah", {}, "blah")
    ])

    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_get_object(mock_client, None, "namespace", "bucket_name", "object", None, None, None, six.StringIO(), None, None, None)

    assert mock_client.get_object.call_count == 3
    assert exception.value.status == 429


def test_get_object_does_not_retry_on_client_error():
    mock_client = create_mock_get_object_client([oci.exceptions.ServiceError(400, "blah", {}, "blah")])

    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_get_object(mock_client, None, "namespace", "bucket_name", "object", None, None, None, six.StringIO(), None, None, None)

    assert mock_client.get_object.call_count == 1
    assert exception.value.status == 400


def test_get_object_does_not_retry_on_random_exception():
    mock_client = create_mock_get_object_client([Exception()])

    with pytest.raises(Exception):
        oci_cli.object_storage_cli.retrying_get_object(mock_client, None, "namespace", "bucket_name", "object", None, None, None, six.StringIO(), None, None, None)

    assert mock_client.get_object.call_count == 1


def test_get_object_succeeds_after_retries():
    mock_data = mock.Mock()
    mock_stream = mock.Mock()
    mock_stream.return_value = []
    mock_data.raw = mock.PropertyMock(return_value=mock_stream)

    mock_client = create_mock_get_object_client([
        oci.exceptions.ServiceError(429, "blah", {}, "blah"),
        oci.response.Response(200, {}, mock_data, None)
    ])

    oci_cli.object_storage_cli.retrying_get_object(mock_client, None, "namespace", "bucket_name", "object", None, None, None, six.StringIO(), None, None, None)

    # 2 calls (1 failure and we succeed on the retry)
    assert mock_client.get_object.call_count == 2


def test_list_objects_retry_timeout_exhaust_retries():
    side_effect = [Timeout(), Timeout(), Timeout()]

    mock_client = create_mock_list_objects_client(side_effect)
    with pytest.raises(Timeout):
        oci_cli.object_storage_cli.retrying_list_objects_single_page(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name')
    assert mock_client.list_objects.call_count == 3

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(Timeout):
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', False)
    assert mock_client.list_objects.call_count == 3

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(Timeout):
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', True)
    assert mock_client.list_objects.call_count == 3


def test_list_objects_retry_connection_error_exhaust_retries():
    side_effect = [ConnectionError(), ConnectionError(), ConnectionError()]

    mock_client = create_mock_list_objects_client(side_effect)
    with pytest.raises(ConnectionError):
        oci_cli.object_storage_cli.retrying_list_objects_single_page(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name')
    assert mock_client.list_objects.call_count == 3

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(ConnectionError):
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', False)
    assert mock_client.list_objects.call_count == 3

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(ConnectionError):
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', True)
    assert mock_client.list_objects.call_count == 3


def test_list_objects_retry_internal_server_error_exhaust_retries():
    side_effect = [
        oci.exceptions.ServiceError(500, "blah", {}, "blah"),
        oci.exceptions.ServiceError(501, "blah", {}, "blah"),
        oci.exceptions.ServiceError(502, "blah", {}, "blah")
    ]

    mock_client = create_mock_list_objects_client(side_effect)
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_list_objects_single_page(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name')
    assert mock_client.list_objects.call_count == 3
    assert exception.value.status == 502

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', False)
    assert mock_client.list_objects.call_count == 3
    assert exception.value.status == 502

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', True)
    assert mock_client.list_objects.call_count == 3
    assert exception.value.status == 502


def test_list_objects_retry_unknown_service_error_exhaust_retries():
    side_effect = [
        oci.exceptions.ServiceError(-1, "blah", {}, "blah"),
        oci.exceptions.ServiceError(-1, "blah", {}, "blah"),
        oci.exceptions.ServiceError(-1, "blah", {}, "blah")
    ]

    mock_client = create_mock_list_objects_client(side_effect)
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_list_objects_single_page(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name')
    assert mock_client.list_objects.call_count == 3
    assert exception.value.status == -1

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', False)
    assert mock_client.list_objects.call_count == 3
    assert exception.value.status == -1

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', True)
    assert mock_client.list_objects.call_count == 3
    assert exception.value.status == -1


def test_list_objects_retry_throttles_exhaust_retries():
    side_effect = [
        oci.exceptions.ServiceError(429, "blah", {}, "blah"),
        oci.exceptions.ServiceError(429, "blah", {}, "blah"),
        oci.exceptions.ServiceError(429, "blah", {}, "blah")
    ]

    mock_client = create_mock_list_objects_client(side_effect)
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_list_objects_single_page(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name')
    assert mock_client.list_objects.call_count == 3
    assert exception.value.status == 429

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', False)
    assert mock_client.list_objects.call_count == 3
    assert exception.value.status == 429

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', True)
    assert mock_client.list_objects.call_count == 3
    assert exception.value.status == 429


def test_list_objects_does_not_retry_on_client_error():
    side_effect = [oci.exceptions.ServiceError(400, "blah", {}, "blah")]

    mock_client = create_mock_list_objects_client(side_effect)
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_list_objects_single_page(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name')
    assert mock_client.list_objects.call_count == 1
    assert exception.value.status == 400

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', False)
    assert mock_client.list_objects.call_count == 1
    assert exception.value.status == 400

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', True)
    assert mock_client.list_objects.call_count == 1
    assert exception.value.status == 400


def test_list_objects_does_not_retry_on_random_exception():
    side_effect = [Exception()]

    mock_client = create_mock_list_objects_client(side_effect)
    with pytest.raises(Exception):
        oci_cli.object_storage_cli.retrying_list_objects_single_page(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name')
    assert mock_client.list_objects.call_count == 1

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(Exception):
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', False)
    assert mock_client.list_objects.call_count == 1

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(Exception):
        oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', True)
    assert mock_client.list_objects.call_count == 1


def test_list_objects_succeeds_after_retries():
    dummy_data = oci.object_storage.models.ListObjects()
    dummy_data.objects = []
    dummy_data.next_start_with = None
    dummy_response = oci.response.Response(200, {}, dummy_data, None)
    side_effect = [oci.exceptions.ServiceError(429, "blah", {}, "blah"), dummy_response]

    mock_client = create_mock_list_objects_client(side_effect)
    oci_cli.object_storage_cli.retrying_list_objects_single_page(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name')
    assert mock_client.list_objects.call_count == 2

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', False)
    assert mock_client.list_objects.call_count == 2

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    oci_cli.object_storage_cli.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', True)
    assert mock_client.list_objects.call_count == 2


def create_mock_get_object_client(side_effect):
    mock_client = mock.Mock()
    mock_client.get_object = mock.Mock()
    mock_client.get_object.side_effect = side_effect

    return mock_client


def create_mock_list_objects_client(side_effect):
    mock_client = mock.Mock()
    mock_client.list_objects = mock.Mock()
    mock_client.list_objects.side_effect = side_effect

    return mock_client
