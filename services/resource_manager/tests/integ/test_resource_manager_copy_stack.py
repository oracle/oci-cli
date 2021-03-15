# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import os
import oci_cli
import pytest
from tests import test_config_container
import oci  # noqa: F401

CASSETTE_LIBRARY_DIR = 'services/resource_manager/tests/cassettes'
ZIP_SOURCE_STACK_ID = 'ocid1.ormstack.oc1.phx.aaaaaaaashhh6un2cidqtpkbwnzwdtibob34sasifjr4gg4qazdvsn5x7xdq'
GIT_CONFIG_SOURCE_STACK_ID = 'ocid1.ormstack.oc1.phx.aaaaaaaadannhlhdld26kygynq2n2udjxphai2kt4gyrox6nn64e232c4j7q'
RESOURCE_DISCOVERY_STACK_ID = 'ocid1.ormstack.oc1.phx.aaaaaaaa622fvlsuqbagptyvqwvea5fzsw57267aoeezbc7expxwyqehui3q'
OBJECT_STORAGE_CONFIG_SOURCE_STACK_ID = 'ocid1.ormstack.oc1.phx.aaaaaaaaa6i7p5wy3wdpkecklycbo76jvez6pzkriin7mxg7oxgqyrk3sngq'
CHANGE_COMPARTMENT_OCID = "ocid1.compartment.oc1..aaaaaaaaqrsxf2pnsnfswitk6t3tkph6mjdwu6ldipmwxj4ijddca7w2obca"
GITHUB_ACCESS_TOKEN = "b72337dd1fc9a6f1d1bc19869842f9707fe42db6"
DESTINATION_REGION = 'ap-tokyo-1'


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('resource_manager_copy_stack.yml'):
        yield


#################################################
# IN-REGION TESTS
#################################################
def test_in_region_copy_stack_zip(runner, config_file, config_profile):
    get_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'get',
        '--stack-id', ZIP_SOURCE_STACK_ID
    ])
    assert get_result is not None
    parsed_output = json.loads(get_result.output)
    assert len(parsed_output['data']) > 0
    source_stack = parsed_output['data']

    copy_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'copy',
        '--stack-id', ZIP_SOURCE_STACK_ID
    ])
    assert copy_result is not None
    parsed_copy_output = json.loads(copy_result.output)
    assert len(parsed_copy_output['data']) > 0
    copied_stack = parsed_copy_output['data']

    compare_stack_metadata(source_stack, copied_stack)
    compare_zip_config_metadata(source_stack, copied_stack)

    compare_stack_TF_config(runner, config_file, config_profile, source_stack["id"], copied_stack["id"])


def test_in_region_copy_stack_git_config_source(runner, config_file, config_profile):
    get_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'get',
        '--stack-id', GIT_CONFIG_SOURCE_STACK_ID
    ])
    assert get_result is not None
    parsed_output = json.loads(get_result.output)
    assert len(parsed_output['data']) > 0
    source_stack = parsed_output['data']

    copy_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'copy',
        '--stack-id', GIT_CONFIG_SOURCE_STACK_ID
    ])
    assert copy_result is not None
    parsed_copy_output = json.loads(copy_result.output)
    assert len(parsed_copy_output['data']) > 0
    copied_stack = parsed_copy_output['data']

    compare_stack_metadata(source_stack, copied_stack)
    compare_git_config_source_metadata(source_stack, copied_stack)


def test_in_region_copy_stack_resource_discovery(runner, config_file, config_profile):
    get_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'get',
        '--stack-id', RESOURCE_DISCOVERY_STACK_ID
    ])
    assert get_result is not None
    parsed_output = json.loads(get_result.output)
    assert len(parsed_output['data']) > 0
    source_stack = parsed_output['data']

    copy_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'copy',
        '--stack-id', RESOURCE_DISCOVERY_STACK_ID
    ])
    assert copy_result is not None
    parsed_copy_output = json.loads(copy_result.output)
    assert len(parsed_copy_output['data']) > 0
    copied_stack = parsed_copy_output['data']

    compare_stack_metadata(source_stack, copied_stack)
    compare_zip_config_metadata(source_stack, copied_stack, is_source_from_resource_discovery=True)

    compare_stack_TF_config(runner, config_file, config_profile, source_stack["id"], copied_stack["id"])


#################################################
# CROSS-REGION TESTS
#################################################
def test_cross_region_copy_stack_zip(runner, config_file, config_profile):
    get_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'get',
        '--stack-id', ZIP_SOURCE_STACK_ID
    ])
    assert get_result is not None
    parsed_output = json.loads(get_result.output)
    assert len(parsed_output['data']) > 0
    source_stack = parsed_output['data']

    copy_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'copy',
        '--stack-id', ZIP_SOURCE_STACK_ID, '--destination-region', DESTINATION_REGION
    ])
    assert copy_result is not None
    parsed_copy_output = json.loads(copy_result.output)
    assert len(parsed_copy_output['data']) > 0
    copied_stack = parsed_copy_output['data']

    compare_stack_metadata(source_stack, copied_stack)
    compare_zip_config_metadata(source_stack, copied_stack)


def test_cross_region_copy_stack_git_config_source(runner, config_file, config_profile):
    get_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'get',
        '--stack-id', GIT_CONFIG_SOURCE_STACK_ID
    ])
    assert get_result is not None
    parsed_output = json.loads(get_result.output)
    assert len(parsed_output['data']) > 0
    source_stack = parsed_output['data']

    copy_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'copy',
        '--stack-id', GIT_CONFIG_SOURCE_STACK_ID, '--destination-region', DESTINATION_REGION,
        '--access-token', GITHUB_ACCESS_TOKEN
    ])
    assert copy_result is not None

    parsed_copy_stack_output = copy_result.output
    index = parsed_copy_stack_output.rfind("{\n  \"data\": {")
    parsed_copy_output = json.loads(parsed_copy_stack_output[index:])
    print(parsed_copy_output)

    assert len(parsed_copy_output['data']) > 0
    copied_stack = parsed_copy_output['data']

    compare_stack_metadata(source_stack, copied_stack)
    compare_git_config_source_metadata(source_stack, copied_stack, in_region=False)


def test_cross_region_copy_stack_resource_discovery(runner, config_file, config_profile):
    get_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'get',
        '--stack-id', RESOURCE_DISCOVERY_STACK_ID
    ])
    assert get_result is not None
    parsed_output = json.loads(get_result.output)
    assert len(parsed_output['data']) > 0
    source_stack = parsed_output['data']

    copy_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'copy',
        '--stack-id', RESOURCE_DISCOVERY_STACK_ID, '--destination-region', DESTINATION_REGION
    ])
    assert copy_result is not None
    parsed_copy_output = json.loads(copy_result.output)
    assert len(parsed_copy_output['data']) > 0
    copied_stack = parsed_copy_output['data']

    compare_stack_metadata(source_stack, copied_stack)
    compare_zip_config_metadata(source_stack, copied_stack, is_source_from_resource_discovery=True)


#################################################
# METADATA TESTS
#################################################
def test_change_compartment_in_region(runner, config_file, config_profile):
    get_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'get',
        '--stack-id', ZIP_SOURCE_STACK_ID
    ])
    assert get_result is not None
    parsed_output = json.loads(get_result.output)
    assert len(parsed_output['data']) > 0
    source_stack = parsed_output['data']

    copy_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'copy',
        '--destination-compartment-id', CHANGE_COMPARTMENT_OCID,
        '--stack-id', ZIP_SOURCE_STACK_ID
    ])
    assert copy_result is not None
    parsed_copy_output = json.loads(copy_result.output)
    assert len(parsed_copy_output['data']) > 0
    copied_stack = parsed_copy_output['data']

    assert copied_stack["compartment-id"] == CHANGE_COMPARTMENT_OCID

    compare_stack_metadata(source_stack, copied_stack, change_compartment=True)
    compare_zip_config_metadata(source_stack, copied_stack)


def test_change_compartment_cross_region(runner, config_file, config_profile):
    get_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'get',
        '--stack-id', ZIP_SOURCE_STACK_ID
    ])
    assert get_result is not None
    parsed_output = json.loads(get_result.output)
    assert len(parsed_output['data']) > 0
    source_stack = parsed_output['data']

    copy_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'copy',
        '--stack-id', ZIP_SOURCE_STACK_ID, '--destination-region', DESTINATION_REGION,
        '--destination-compartment-id', CHANGE_COMPARTMENT_OCID,
    ])
    assert copy_result is not None
    parsed_copy_output = json.loads(copy_result.output)
    assert len(parsed_copy_output['data']) > 0
    copied_stack = parsed_copy_output['data']

    assert copied_stack["compartment-id"] == CHANGE_COMPARTMENT_OCID

    compare_stack_metadata(source_stack, copied_stack, change_compartment=True)
    compare_zip_config_metadata(source_stack, copied_stack)


def test_destination_region_equals_source_region(runner, config_file, config_profile):
    get_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'get',
        '--stack-id', GIT_CONFIG_SOURCE_STACK_ID
    ])
    assert get_result is not None
    parsed_output = json.loads(get_result.output)
    assert len(parsed_output['data']) > 0
    source_stack = parsed_output['data']

    copy_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'copy',
        '--stack-id', GIT_CONFIG_SOURCE_STACK_ID, '--destination-region', "us-phoenix-1",
        '--access-token', GITHUB_ACCESS_TOKEN
    ])
    assert copy_result is not None
    assert copy_result.output.count("data", 0, len(copy_result.output)) == 1
    parsed_copy_output = json.loads(copy_result.output)
    assert len(parsed_copy_output['data']) > 0
    copied_stack = parsed_copy_output['data']

    compare_stack_metadata(source_stack, copied_stack)
    compare_git_config_source_metadata(source_stack, copied_stack)


def test_copy_stack_invalid_config_source_type(runner, config_file, config_profile):
    copy_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'copy',
        '--stack-id', OBJECT_STORAGE_CONFIG_SOURCE_STACK_ID,
        '--freeform-tags', '{"new_key": "new_value"}',
        '--variables', '{"availability_domain_name": "CgGK:PHX-AD-2"}'
    ])
    assert copy_result is not None
    assert "Only zip-upload config, git-configuration-source and create-from-compartment stacks are supported for copy stack" in copy_result.output


def test_copy_stack_change_tags(runner, config_file, config_profile):

    get_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'get',
        '--stack-id', ZIP_SOURCE_STACK_ID
    ])
    assert get_result is not None
    parsed_output = json.loads(get_result.output)
    assert len(parsed_output['data']) > 0
    source_stack = parsed_output['data']

    copy_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'copy',
        '--stack-id', ZIP_SOURCE_STACK_ID,
        '--freeform-tags', '{"new_key": "new_value"}',
        '--variables', '{"availability_domain_name": "CgGK:PHX-AD-2"}'
    ])
    assert copy_result is not None
    parsed_copy_output = json.loads(copy_result.output)
    assert len(parsed_copy_output['data']) > 0
    copied_stack = parsed_copy_output['data']

    print(copied_stack["variables"])

    compare_stack_metadata(source_stack, copied_stack, change_tags_and_variables=True)
    compare_zip_config_metadata(source_stack, copied_stack)


def test_copy_stack_invalid_stack_id(runner, config_file, config_profile):
    result = None
    try:
        result = invoke(runner, config_file, config_profile, [
            'resource-manager', 'stack', 'copy',
        ])
    except Exception:
        assert 'Error: Missing option(s)' in result.output
        assert 'stack-id' in result.output

    result = None
    try:
        result = invoke(runner, config_file, config_profile, [
            'resource-manager', 'stack', 'copy',
            '--stack-id', "sdfsjfdsfklsdjfklsdjflksdjflksdjflksjdfksjd"
        ])
    except Exception:
        assert 'Error: Missing option(s)' in result.output
        assert 'stack-id' in result.output


def test_copy_stack_invalid_destination_region(runner, config_file, config_profile):
    result = None
    try:
        result = invoke(runner, config_file, config_profile, [
            'resource-manager', 'stack', 'copy',
            '--stack-id', ZIP_SOURCE_STACK_ID, '--destination-region', "fake-region"
        ])
    except Exception:
        assert 'Unrecognized region' in result.output

    result = None
    try:
        result = invoke(runner, config_file, config_profile, [
            'resource-manager', 'stack', 'copy',
            '--stack-id', ZIP_SOURCE_STACK_ID, '--destination-region', "ap-chiyoda-1"
        ])
    except Exception:
        assert 'Invalid region. Destination region must be in the same realm' in result.output


def test_copy_stack_cross_region_git_config_source_invalid_access_token(runner, config_file, config_profile):
    result = None
    try:
        result = invoke(runner, config_file, config_profile, [
            'resource-manager', 'stack', 'copy',
            '--stack-id', GIT_CONFIG_SOURCE_STACK_ID,
            '--destination-region', DESTINATION_REGION
        ])
    except Exception:
        assert 'Error: Missing option(s)' in result.output
        assert '--access-token' in result.output

    result = None
    try:
        result = invoke(runner, config_file, config_profile, [
            'resource-manager', 'stack', 'copy',
            '--stack-id', GIT_CONFIG_SOURCE_STACK_ID,
            '--destination-region', DESTINATION_REGION, '--access-token', "nnjknkjhjhkj"
        ])
    except Exception:
        assert 'Error: Missing option(s)' in result.output
        assert '--access-token' in result.output


def test_copy_stack_invalid_compartment_id(runner, config_file, config_profile):

    get_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'get',
        '--stack-id', GIT_CONFIG_SOURCE_STACK_ID
    ])
    assert get_result is not None
    parsed_output = json.loads(get_result.output)
    assert len(parsed_output['data']) > 0
    source_stack = parsed_output['data']

    copy_result = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'copy',
        '--destination-compartment-id', 'dsfdfsdf',
        '--stack-id', ZIP_SOURCE_STACK_ID
    ])
    assert copy_result is not None
    parsed_copy_output = copy_result.output

    assert "Failed to copy stack: " in parsed_copy_output
    assert "Deleting copied configuration source provider: " not in parsed_copy_output


#################################################
# HELPER METHODS
#################################################
def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, **args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile',
                                                           config_profile] + params, **args)
    else:
        result = runner.invoke(oci_cli.cli,
                               root_params + ['--config-file', config_file, '--profile', config_profile] + params,
                               **args)

    return result


def compare_stack_TF_config(runner, config_file, config_profile, source_stack_id, copied_stack_id):
    filename_source_tf_config = "source_stack_tf_config"
    source_tf_config_response = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'get-stack-tf-config',
        '--stack-id', source_stack_id, "--file", filename_source_tf_config
    ])

    file = open(filename_source_tf_config, 'rb')

    try:
        source_tf_config_binary = file.read()
    finally:
        file.close()

    filename_copied_tf_config = "copied_stack_tf_config"
    copied_tf_config_response = invoke(runner, config_file, config_profile, [
        'resource-manager', 'stack', 'get-stack-tf-config',
        '--stack-id', copied_stack_id, "--file", filename_copied_tf_config
    ])

    file2 = open(filename_copied_tf_config, 'rb')

    try:
        copied_tf_config_binary = file2.read()
    finally:
        file2.close()

    assert copied_tf_config_binary is not None
    assert source_tf_config_binary is not None
    assert copied_tf_config_binary == source_tf_config_binary

    os.remove(filename_source_tf_config)
    os.remove(filename_copied_tf_config)


def compare_stack_metadata(source_stack, copied_stack, change_compartment=False, change_tags_and_variables=False):

    assert source_stack["display-name"] in copied_stack["display-name"]
    assert copied_stack["description"] == source_stack["description"]
    assert copied_stack["id"] != source_stack["id"]
    assert copied_stack["terraform-version"] == source_stack["terraform-version"]

    if change_compartment:
        assert copied_stack["compartment-id"] != source_stack["compartment-id"]
    else:
        assert copied_stack["compartment-id"] == source_stack["compartment-id"]

    if change_tags_and_variables:
        assert copied_stack["freeform-tags"] != source_stack["freeform-tags"]
        assert all(copied_stack["freeform-tags"].get(key, None) == val for key, val in source_stack["freeform-tags"].items())
        # assert copied_stack["defined-tags"] != source_stack["defined-tags"]
        assert copied_stack["variables"] != source_stack["variables"]

        for key in copied_stack["variables"]:
            if key == "availability_domain_name":
                assert copied_stack["variables"][key] != source_stack["variables"][key]
            else:
                assert copied_stack["variables"][key] == source_stack["variables"][key]

    else:
        assert copied_stack["freeform-tags"] == source_stack["freeform-tags"]
        assert copied_stack["defined-tags"] == source_stack["defined-tags"]
        assert copied_stack["variables"] == source_stack["variables"]


def compare_zip_config_metadata(source_stack, copied_stack, is_source_from_resource_discovery=False):
    assert copied_stack["config-source"]["working-directory"] == source_stack["config-source"]["working-directory"]

    if is_source_from_resource_discovery:
        assert copied_stack["config-source"]["config-source-type"] != source_stack["config-source"]["config-source-type"]
        assert copied_stack["config-source"]["config-source-type"] == oci.resource_manager.models.ConfigSource.CONFIG_SOURCE_TYPE_ZIP_UPLOAD
        assert source_stack["config-source"]["config-source-type"] == oci.resource_manager.models.ConfigSource.CONFIG_SOURCE_TYPE_COMPARTMENT_CONFIG_SOURCE
    else:
        assert copied_stack["config-source"]["config-source-type"] == source_stack["config-source"]["config-source-type"]


def compare_git_config_source_metadata(source_stack, copied_stack, in_region=True):
    assert copied_stack["config-source"]["working-directory"] == source_stack["config-source"]["working-directory"]
    assert copied_stack["config-source"]["config-source-type"] == source_stack["config-source"]["config-source-type"]
    assert copied_stack["config-source"]["branch-name"] == source_stack["config-source"]["branch-name"]
    assert copied_stack["config-source"]["repository-url"] == source_stack["config-source"]["repository-url"]

    if in_region:
        assert copied_stack["config-source"]["configuration-source-provider-id"] == source_stack["config-source"]["configuration-source-provider-id"]
    else:
        assert copied_stack["config-source"]["configuration-source-provider-id"] != source_stack["config-source"]["configuration-source-provider-id"]
