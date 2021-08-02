# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest.mock as mock

import oci
import services.object_storage.src.oci_cli_object_storage as oci_cli_object_storage
import pytest

from tests import util


@util.skip_while_rerecording
def test_list_objects_does_not_retry_on_client_error():
    side_effect = [oci.exceptions.ServiceError(400, "blah", {}, "blah")]

    mock_client = create_mock_list_objects_client(side_effect)
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli_object_storage.objectstorage_cli_extended.retrying_list_call_single_page(mock_client.list_objects, None, "namespace", "bucket_name", "prefix", None, None, 100, None, fields='name')
    assert mock_client.list_objects.call_count == 1
    assert exception.value.status == 400

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli_object_storage.objectstorage_cli_extended.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', False)
    assert mock_client.list_objects.call_count == 1
    assert exception.value.status == 400

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(oci.exceptions.ServiceError) as exception:
        oci_cli_object_storage.objectstorage_cli_extended.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', True)
    assert mock_client.list_objects.call_count == 1
    assert exception.value.status == 400


@util.skip_while_rerecording
def test_list_objects_does_not_retry_on_random_exception():
    side_effect = [Exception()]

    mock_client = create_mock_list_objects_client(side_effect)
    with pytest.raises(Exception):
        oci_cli_object_storage.objectstorage_cli_extended.retrying_list_call_single_page(mock_client.list_objects, None, "namespace", "bucket_name", "prefix", None, None, 100, None, fields='name')
    assert mock_client.list_objects.call_count == 1

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(Exception):
        oci_cli_object_storage.objectstorage_cli_extended.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', False)
    assert mock_client.list_objects.call_count == 1

    mock_client.list_objects.reset_mock()
    mock_client.list_objects.side_effect = side_effect
    with pytest.raises(Exception):
        oci_cli_object_storage.objectstorage_cli_extended.retrying_list_objects(mock_client, None, "namespace", "bucket_name", "prefix", None, None, 100, None, 'name', True)
    assert mock_client.list_objects.call_count == 1


def create_mock_list_objects_client(side_effect):
    mock_client = mock.Mock()
    mock_client.list_objects = mock.Mock()
    mock_client.list_objects.side_effect = side_effect

    return mock_client
