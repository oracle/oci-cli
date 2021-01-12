# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# get wr
# list wr
# get wr log
# get wr error (check feasibility)


import pytest
import data_safe_util

from tests import util
from tests import test_config_container


# These exist in CLITestCompartment in adscorp_tenant01
PRIVATE_IP = '10.0.0.10'
VCN_ID = "ocid1.vcn.oc1.iad.amaaaaaagn3s2faaakpo23ve66izav4irns2ws56y6bygoutsxjglrmmcvxa"
SUBNET_ID = "ocid1.subnet.oc1.iad.aaaaaaaafhqe56mpqjvxa7obixry6zglgugapmqi2i3wwblaqrc7x6moy6oq"
PE_DISPLAY_NAME = 'CLITest_PE'
PE_UPDATED_DISPLAY_NAME = 'CLITest_PE_Updated'
PE_DESCRIPTION = 'PE for CLI Testing'
SUCCEEDED_STATE = 'SUCCEEDED'
FAILED_STATE = 'FAILED'
COMPARTMENT_ID = 'ocid1.compartment.oc1..aaaaaaaaoqv2smvc4kii7uudwyuqgh6mkocmbe5nvtn2yd2krfwwmh3c5mza'
CHANGE_COMPARTMENT_ID = 'ocid1.compartment.oc1..aaaaaaaanlj6vtiefseqgwsabbuvebxo7nojc25i46uahifmdpqaddsj7rmq'


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=data_safe_util.CASSETTE_LIBRARY_DIR).use_cassette('pe_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.mark.skip("DEXREQ-1712")
def test_crud(runner, config_file, config_profile):
    pe_id = _create_pe(config_file, config_profile, runner)

    _get_pe(config_file, config_profile, pe_id, runner)

    _update_pe(config_file, config_profile, pe_id, runner)

    _list_pe(config_file, config_profile, runner)

    _delete_pe(config_file, config_profile, pe_id, runner)


def test_crud_sync(runner, config_file, config_profile):
    pe_id = _create_pe(config_file, config_profile, runner, is_async=False)

    _get_pe(config_file, config_profile, pe_id, runner)

    _update_pe(config_file, config_profile, pe_id, runner, is_async=False)

    _list_pe(config_file, config_profile, runner)

    _delete_pe(config_file, config_profile, pe_id, runner, is_async=False)


@pytest.mark.skip("DEXREQ-1712")
def test_create_error(runner, config_file, config_profile):
    _create_pe(config_file, config_profile, runner, completion_state=FAILED_STATE, private_ip="1.1.1.1.1", display_name="CLITest_Failed_PE")


@pytest.mark.skip(reason='DS-5401: CLI: PE "change-compartment" returns 404')
def test_change_compartment(runner, config_file, config_profile):
    pe_id = _create_pe(config_file, config_profile, runner)

    change_comp_params = [
        'data-safe', 'private-endpoint', 'change-compartment',
        '--private-endpoint-id', pe_id,
        '--compartment-id', CHANGE_COMPARTMENT_ID
    ]

    expected_data = {
        "id": pe_id,
        "compartment-id": CHANGE_COMPARTMENT_ID
    }

    data_safe_util.run_test(runner, config_file, config_profile, change_comp_params, expected_data=expected_data)

    _delete_pe(config_file, config_profile, pe_id, runner)


def _delete_pe(config_file, config_profile, pe_id, runner, is_async=True):
    # DELETE TEST #
    delete_params = [
        'data-safe', 'private-endpoint', 'delete',
        '--private-endpoint-id', pe_id,
        '--force'
    ]

    if is_async:
        # We just validate if work request id is returned and not the value as it is dynamic
        response = data_safe_util.run_test(runner, config_file, config_profile, delete_params,
                                           expected_data=data_safe_util.WORKFLOW_REQUEST_EXPECTED_DATA, check_values=False)
        delete_wr_id = response["opc-work-request-id"]
        util.wait_until(['data-safe', 'work-request', 'get', '--work-request-id', delete_wr_id],
                        SUCCEEDED_STATE, max_wait_seconds=600, state_property_name='status')
    else:
        delete_params.append('--wait-for-state')
        delete_params.append(SUCCEEDED_STATE)
        data_safe_util.run_test(runner, config_file, config_profile, delete_params, decode_response=False)


def _list_pe(config_file, config_profile, runner):
    # LIST TEST #
    list_params = [
        'data-safe', 'private-endpoint', 'list',
        '--compartment-id', COMPARTMENT_ID,
        '--all'
    ]
    data_safe_util.run_test(runner, config_file, config_profile, list_params, check_length=True)

    # Test list work-request
    list_wr_params = [
        'data-safe', 'work-request', 'list',
        '--compartment-id', COMPARTMENT_ID,
        '--all'
    ]
    data_safe_util.run_test(runner, config_file, config_profile, list_wr_params, check_length=True)


def _update_pe(config_file, config_profile, pe_id, runner, is_async=True):
    # UPDATE TEST #
    update_params = [
        'data-safe', 'private-endpoint', 'update',
        '--private-endpoint-id', pe_id,
        '--display-name', PE_UPDATED_DISPLAY_NAME,
        '--description', PE_DESCRIPTION,
        '--force'
    ]

    if is_async:
        # We just validate if work request id is returned and not the value as it is dynamic
        response = data_safe_util.run_test(runner, config_file, config_profile, update_params,
                                           expected_data=data_safe_util.WORKFLOW_REQUEST_EXPECTED_DATA, check_values=False)
        update_wr_id = response["opc-work-request-id"]
        util.wait_until(['data-safe', 'work-request', 'get', '--work-request-id', update_wr_id],
                        'SUCCEEDED', max_wait_seconds=600, state_property_name='status')
    else:
        update_params.append('--wait-for-state')
        update_params.append(SUCCEEDED_STATE)
        data_safe_util.run_test(runner, config_file, config_profile, update_params, decode_response=False)

    get_params = [
        'data-safe', 'private-endpoint', 'get',
        '--private-endpoint-id', pe_id
    ]

    expected_data = {
        "lifecycle-state": "ACTIVE",
        "display-name": PE_UPDATED_DISPLAY_NAME,
        "id": pe_id,
        "subnet-id": SUBNET_ID,
        "vcn-id": VCN_ID,
        "compartment-id": COMPARTMENT_ID,
        "description": PE_DESCRIPTION
    }

    data_safe_util.run_test(runner, config_file, config_profile, get_params, expected_data=expected_data)


def _get_pe(config_file, config_profile, pe_id, runner, private_ip=PRIVATE_IP):
    # get pe
    get_params = [
        'data-safe', 'private-endpoint', 'get',
        '--private-endpoint-id', pe_id
    ]

    expected_data = {
        "lifecycle-state": "ACTIVE",
        "display-name": PE_DISPLAY_NAME,
        "id": pe_id,
        "subnet-id": SUBNET_ID,
        "vcn-id": VCN_ID,
        "compartment-id": COMPARTMENT_ID,
        "private-endpoint-ip": private_ip
    }

    response = data_safe_util.run_test(runner, config_file, config_profile, get_params, expected_data=expected_data)
    return response


def _create_pe(config_file, config_profile, runner, completion_state=SUCCEEDED_STATE, private_ip=PRIVATE_IP, display_name=PE_DISPLAY_NAME, is_async=True):
    # CREATE TEST #
    create_params = [
        'data-safe', 'private-endpoint', 'create',
        '--compartment-id', COMPARTMENT_ID,
        '--display-name', display_name,
        '--subnet-id', SUBNET_ID,
        '--vcn-id', VCN_ID,
        '--private-endpoint-ip', private_ip
    ]

    if is_async:
        # We just validate if work request id is returned and not the value as it is dynamic
        response = data_safe_util.run_test(runner, config_file, config_profile, create_params,
                                           expected_data=data_safe_util.WORKFLOW_REQUEST_EXPECTED_DATA, check_values=False)
        create_wr_id = response["opc-work-request-id"]
        util.wait_until(['data-safe', 'work-request', 'get', '--work-request-id', create_wr_id],
                        completion_state, max_wait_seconds=600, state_property_name='status')

        # Test list-work-request-logs
        list_wr_log_params = [
            'data-safe', 'work-request-log-entry', 'list',
            '--work-request-id', create_wr_id,
            '--all'
        ]
        data_safe_util.run_test(runner, config_file, config_profile, list_wr_log_params, check_length=True)

        if completion_state == FAILED_STATE:
            # Test list-work-error
            list_wr_log_params = [
                'data-safe', 'work-request-error', 'list',
                '--work-request-id', create_wr_id,
                '--all'
            ]
            data_safe_util.run_test(runner, config_file, config_profile, list_wr_log_params, check_length=True)
    else:
        create_params.append('--wait-for-state')
        create_params.append(SUCCEEDED_STATE)
        data_safe_util.run_test(runner, config_file, config_profile, create_params, decode_response=False)

    pe_id = ''
    if completion_state == SUCCEEDED_STATE:
        list_params = [
            'data-safe', 'private-endpoint', 'list',
            '--compartment-id', COMPARTMENT_ID,
            '--display-name', display_name,
            '--all'
        ]

        response = data_safe_util.run_test(runner, config_file, config_profile, list_params, check_length=True)
        pe_id = response["data"][0]["id"]

    return pe_id
