# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci
import oci_cli
import pytest
import time
from tests import util
from tests import test_config_container

CASSETTE_LIBRARY_DIR = 'services/file_storage/tests/cassettes'


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('filestorage_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture(scope='module')
def vcn_and_subnet(runner, config_file, config_profile, network_client):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('filestorage_vcn_and_subnet_fixture.yml'):
        # create VCN
        vcn_name = util.random_name('cli_db_test_vcn')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        create_vcn_details = oci.core.models.CreateVcnDetails()
        create_vcn_details.cidr_block = cidr_block
        create_vcn_details.display_name = vcn_name
        create_vcn_details.compartment_id = util.COMPARTMENT_ID
        create_vcn_details.dns_label = vcn_dns_label

        result = network_client.create_vcn(create_vcn_details)
        vcn_ocid = result.data.id
        assert result.status == 200

        oci.wait_until(network_client, network_client.get_vcn(vcn_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        # create subnet in first AD
        subnet_name = util.random_name('python_sdk_test_subnet')
        cidr_block = "10.0.1.0/24"
        subnet_dns_label = util.random_name('subnet', insert_underscore=False) + '1'

        create_subnet_details = oci.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = util.COMPARTMENT_ID
        create_subnet_details.availability_domain = util.availability_domain()
        create_subnet_details.display_name = subnet_name
        create_subnet_details.vcn_id = vcn_ocid
        create_subnet_details.cidr_block = cidr_block
        create_subnet_details.dns_label = subnet_dns_label

        result = network_client.create_subnet(create_subnet_details)
        subnet_ocid = result.data.id
        assert result.status == 200

        oci.wait_until(network_client, network_client.get_subnet(subnet_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

    yield vcn_ocid, subnet_ocid

    # this code does not run inside the vcr_fixture because it is outside any test function
    # thus we are explicitly creating a separate cassette for it here
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('filestorage_vcn_and_subnet_fixture_cleanup.yml'):
        # Sometimes we can't delete the subnet straight after the mount target because some VNIC is still
        # hanging around. If we get a conflict, try a few times before bailing out
        attempts = 0
        while attempts < 5:
            try:
                network_client.delete_subnet(subnet_ocid)
                test_config_container.do_wait(
                    network_client,
                    network_client.get_subnet(subnet_ocid),
                    'lifecycle_state',
                    'TERMINATED',
                    max_wait_seconds=600,
                    succeed_on_not_found=True
                )
                break
            except oci.exceptions.ServiceError as e:
                attempts += 1
                if e.status == 409 and attempts < 5:
                    time.sleep(5)
                else:
                    raise

        network_client.delete_vcn(vcn_ocid)


@pytest.fixture(scope='module')
def file_system(filestorage_client, runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('filestorage_file_system_fixture.yml'):
        params = [
            'file-system', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--availability-domain', util.availability_domain()
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        file_system_id = json.loads(result.output)['data']['id']

        util.wait_until(['fs', 'file-system', 'get', '--file-system-id', file_system_id], 'ACTIVE', max_wait_seconds=300)

    yield file_system_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('filestorage_file_system_fixture_cleanup.yml'):
        params = [
            'file-system', 'delete',
            '--file-system-id', file_system_id,
            '--force'
        ]

        invoke(runner, config_file, config_profile, params)
        util.wait_until(['fs', 'file-system', 'get', '--file-system-id', file_system_id], 'DELETED', max_wait_seconds=300)


@pytest.fixture(scope='module')
def mount_target(filestorage_client, vcn_and_subnet, runner, config_file, config_profile):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('filestorage_mount_target_fixture.yml'):
        vcn_id = vcn_and_subnet[0]
        subnet_id = vcn_and_subnet[1]

        mount_target_name = util.random_name('cli_test_mt')

        params = [
            'mount-target', 'create',
            '--availability-domain', util.availability_domain(),
            '-c', util.COMPARTMENT_ID,
            '--subnet-id', subnet_id
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        mount_target = json.loads(result.output)['data']
        mount_target_id = mount_target['id']

        test_config_container.do_wait(
            filestorage_client,
            filestorage_client.get_mount_target(mount_target_id),
            'lifecycle_state',
            'ACTIVE'
        )

        # exercise CLI get mount target
        params = [
            'mount-target', 'get',
            '--mount-target-id', mount_target_id
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

    yield mount_target

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('filestorage_mount_target_fixture_cleanup.yml'):
        params = [
            'mount-target', 'delete',
            '--mount-target-id', mount_target_id,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        util.wait_until(['fs', 'mount-target', 'get', '--mount-target-id', mount_target_id], 'DELETED', max_wait_seconds=300)


def test_list_file_systems(file_system, runner, config_file, config_profile):
    params = [
        'file-system', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--availability-domain', util.availability_domain()
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


def test_list_and_update_mount_targets(mount_target, runner, config_file, config_profile):
    params = [
        'mount-target', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--availability-domain', util.availability_domain()
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    new_display_name = util.random_name('up_cli_test_mt')
    params = [
        'mount-target', 'update',
        '--mount-target-id', mount_target['id'],
        '--display-name', new_display_name
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    assert json.loads(result.output)['data']['display-name'] == new_display_name


def test_crud_export_set(mount_target, runner, config_file, config_profile):
    params = [
        'export-set', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--availability-domain', util.availability_domain()
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    found_export_set = False
    export_sets = json.loads(result.output)['data']
    for es in export_sets:
        if es['id'] == mount_target['export-set-id']:
            found_export_set = True
            break

    assert found_export_set

    updated_export_set_name = util.random_name('up_cli_test_es')
    params = [
        'export-set', 'update',
        '--export-set-id', mount_target['export-set-id'],
        '--display-name', updated_export_set_name
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    assert json.loads(result.output)['data']['display-name'] == updated_export_set_name

    params = [
        'export-set', 'get',
        '--export-set-id', mount_target['export-set-id']
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


def test_crud_export(file_system, mount_target, runner, config_file, config_profile):
    params = [
        'export', 'create',
        '--export-set-id', mount_target['export-set-id'],
        '--file-system-id', file_system,
        '--path', '/files'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    export = json.loads(result.output)['data']

    params = [
        'export', 'list',
        '-c', util.COMPARTMENT_ID,
        '--file-system-id', file_system
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # there should be one export for this fs
    exports = json.loads(result.output)['data']
    assert len(exports) == 1

    util.wait_until(['fs', 'export', 'get', '--export-id', export['id']], 'ACTIVE', max_wait_seconds=300)

    params = [
        'export', 'delete',
        '--export-id', export['id'],
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


def test_crud_snapshot(file_system, runner, config_file, config_profile):
    params = [
        'snapshot', 'list',
        '--file-system-id', file_system
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    assert len(result.output) == 0

    params = [
        'snapshot', 'create',
        '--file-system-id', file_system,
        '--name', util.random_name('cli_snapshot')
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    snapshot_id = json.loads(result.output)['data']['id']
    params = [
        'snapshot', 'get',
        '--snapshot-id', snapshot_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    util.wait_until(['fs', 'snapshot', 'get', '--snapshot-id', snapshot_id], 'ACTIVE', max_wait_seconds=300)

    params = [
        'snapshot', 'delete',
        '--snapshot-id', snapshot_id,
        '--force'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile, 'fs'] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile, 'fs'] + params, ** args)

    return result
