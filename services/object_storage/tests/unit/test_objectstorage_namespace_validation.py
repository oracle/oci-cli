# Copyright (c) 2016, 2026, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.

import click
import mock
import oci
import pytest
from oci.base_client import BaseClient

import oci_cli.final_command_processor as final_command_processor
from tests import util
from services.object_storage.src.oci_cli_object_storage.generated import objectstorage_cli
from services.object_storage.src.oci_cli_object_storage.objectstorage_cli_extended import (
    NAMESPACE_VALIDATION_ERROR,
    validate_namespace_name
)


@pytest.mark.parametrize('namespace', [
    'mynamespace',
    'dex-us-phx-cli-1',
    'my_namespace',
    'my.namespace',
    'my/namespace',
    'public_ostore_project/oci_plan_001_filesystem'
])
def test_validate_namespace_name_allows_host_safe_values(namespace):
    assert validate_namespace_name(namespace) == namespace


@pytest.mark.parametrize('namespace', [
    'bad@namespace',
    'bad?namespace',
    'bad#namespace',
    'bad:namespace',
    'bad namespace',
    ' mynamespace',
    'mynamespace ',
    '',
    ' '
])
def test_validate_namespace_name_rejects_url_unsafe_values(namespace):
    with pytest.raises(click.BadParameter) as exc:
        validate_namespace_name(namespace)

    assert NAMESPACE_VALIDATION_ERROR in str(exc.value)


def test_object_storage_namespace_callback_rejects_url_unsafe_values():
    final_command_processor.process()

    list_command = objectstorage_cli.object_group.commands['list']
    namespace_param = next(param for param in list_command.params if param.name == 'namespace')

    with pytest.raises(click.BadParameter) as exc:
        namespace_param.callback(None, namespace_param, 'bad#namespace')

    assert NAMESPACE_VALIDATION_ERROR in str(exc.value)


def test_object_storage_namespace_callback_wrapping_is_idempotent():
    final_command_processor.process()

    list_command = objectstorage_cli.object_group.commands['list']
    namespace_param = next(param for param in list_command.params if param.name == 'namespace')
    callback = namespace_param.callback

    final_command_processor.process()

    assert namespace_param.callback is callback


def test_object_storage_namespace_option_callback_accepts_slash():
    final_command_processor.process()
    namespace_param = next(
        param for param in objectstorage_cli.object_group.commands['list'].params
        if param.name == 'namespace'
    )

    assert namespace_param.callback(None, namespace_param, 'my/namespace') == 'my/namespace'


def test_nested_namespace_is_encoded_in_custom_endpoint_request_path():
    namespace = 'public_ostore_project/oci_plan_001_filesystem'
    response = oci.Response(200, {}, {}, None)

    with mock.patch.object(BaseClient, 'request', return_value=response) as request:
        result = util.invoke_command([
            '--endpoint', 'http://10.80.198.244/oci',
            'os', 'bucket', 'create',
            '--namespace-name', namespace,
            '--name', 'b',
            '--compartment-id', 'c'
        ])

    assert result.exit_code == 0
    request_seen_by_sdk = request.call_args[0][0]
    assert request_seen_by_sdk.url == (
        'http://10.80.198.244/oci/n/public_ostore_project%2Foci_plan_001_filesystem/b'
    )


def test_nested_namespace_does_not_bypass_default_endpoint_validation():
    # Realm-specific Object Storage endpoints place the namespace in the hostname.
    # Enable that path explicitly because the SDK default differs between branches.
    with mock.patch.object(BaseClient, 'should_allow_template_per_realm', return_value=True), mock.patch.object(BaseClient, 'request') as request:
        result = util.invoke_command([
            'os', 'bucket', 'create',
            '--namespace-name', 'public_ostore_project/oci_plan_001_filesystem',
            '--name', 'b',
            '--compartment-id', 'c'
        ])

    assert result.exit_code != 0
    assert 'Invalid endpoint host: endpoint must not contain path, query, or fragment.' in result.output
    request.assert_not_called()
