# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci_cli
import pytest
from tests import util
from tests import test_config_container

CASSETTE_LIBRARY_DIR = 'services/core/tests/cassettes'


@pytest.fixture(scope='module')
def cross_connect_group(runner, config_file, config_profile):
    # Set-up of cross-connect group
    ccg_id = None
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_fastconnect_fixture_crossconnectgroup.yml'):
        # Create cross connect group
        ccg_name = util.random_name('cli_test_network_ccg')
        params = [
            'network', 'cross-connect-group', 'create',
            '--display-name', ccg_name,
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        ccg_id = json.loads(result.output)['data']['id']

        # Get cross connect group
        params = [
            'network', 'cross-connect-group', 'get',
            '--cross-connect-group-id', ccg_id
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # List cross connect group
        params = [
            'network', 'cross-connect-group', 'list',
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # Update cross connect group
        ccg_name = util.random_name('cli_test_network_crossconnect_grp')
        params = [
            'network', 'cross-connect-group', 'update',
            '--cross-connect-group-id', ccg_id,
            '--display-name', ccg_name
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        yield ccg_id

    # Teardown of cross-connect group
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_fastconnect_fixture_crossconnectgroup_delete.yml'):
        if ccg_id:
            # Delete cross connect group
            params = [
                'network', 'cross-connect-group', 'delete',
                '--cross-connect-group-id', ccg_id,
                '--wait-for-state', 'TERMINATED',
                '--force'
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result, json_response_expected=False)


@pytest.fixture(scope='module')
def cross_connect(runner, config_file, config_profile, cross_connect_group):
    # Set-up of cross-connect resource
    cc_id = None
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_fastconnect_fixture_crossconnect.yml'):
        # Find cross-connect locations
        params = [
            'network', 'cross-connect-location', 'list',
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        fc_location_name = json.loads(result.output)['data'][0]['name']

        # Get cross-connect port speeds
        params = [
            'network', 'cross-connect-port-speed-shape', 'list',
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        fc_port_speed = json.loads(result.output)['data'][0]['name']

        # Create cross-connect
        cc_name = util.random_name('cli_test_network_cc')
        params = [
            'network', 'cross-connect', 'create',
            '--display-name', cc_name,
            '--location-name', fc_location_name,
            '--port-speed-shape-name', fc_port_speed,
            '--cross-connect-group-id', cross_connect_group,
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        cc_id = json.loads(result.output)['data']['id']

        # Get cross-connect status by cross-connect OCID
        params = [
            'network', 'cross-connect-status', 'get',
            '--cross-connect-id', cc_id
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # Get cross-connect by cross-connect OCID
        params = [
            'network', 'cross-connect', 'get',
            '--cross-connect-id', cc_id
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # List cross-connects in a given compartment
        params = [
            'network', 'cross-connect', 'list',
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # Update cross-connect group.
        # Make sure the cross-connect is activated; Virtual circuit can ONLY be created in a cross-connect group
        # which has cross-connect in it.
        cc_name = util.random_name('cli_test_network_crossconnect')
        params = [
            'network', 'cross-connect', 'update',
            '--cross-connect-id', cc_id,
            '--display-name', cc_name,
            '--is-active', 'true',
            '--wait-for-state', 'PROVISIONED'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result, json_response_expected=False)
        assert util.get_json_from_mixed_string(result.output)['data']['lifecycle-state'] == 'PROVISIONED'

        yield cc_id

    # Teardown of cross-connect resource.
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_fastconnect_fixture_crossconnect_delete.yml'):
        if cc_id:
            # Delete cross-connect
            params = [
                'network', 'cross-connect', 'delete',
                '--cross-connect-id', cc_id,
                '--wait-for-state', 'TERMINATED',
                '--force'
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result, json_response_expected=False)


# Virtual circuit creation depends on cross-connect and cross-connect group creation. The fixtures passed as arguments
# below allow for this dependency injection.
@util.slow
def test_virtual_circuit_crud_operations(runner, config_file, config_profile, cross_connect_group, cross_connect):
    # Set up of virtual circuit
    vc_id = None
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_fastconnect_fixture_virtualcircuit.yml'):
        # Create Dynamic Routing Gateway
        drg_name = util.random_name('cli_test_network_drg')
        params = [
            'network', 'drg', 'create',
            '--display-name', drg_name,
            '--compartment-id', util.COMPARTMENT_ID,
            '--wait-for-state', 'AVAILABLE'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result, json_response_expected=False)
        assert util.get_json_from_mixed_string(result.output)['data']['lifecycle-state'] == 'AVAILABLE'
        drg_id = util.get_json_from_mixed_string(result.output)['data']['id']

        # Get fast connect service provider OCID
        params = [
            'network', 'fast-connect-provider-service', 'list',
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        fcps_id = json.loads(result.output)['data'][0]['id']

        # Get virtual circuit bandwidth shapes for a particular fast connect service provider
        params = [
            'network', 'fast-connect-provider-service', 'virtual-circuit-bandwidth-shape', 'list',
            '--provider-service-id', fcps_id
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        vc_bandwidth = json.loads(result.output)['data'][0]['name']

        # Create virtual circuit
        vc_name = util.random_name('cli_test_network_vc')
        bgpMd5AuthKey = 'null'
        customerBgpPeeringIp = '10.0.0.17/31'
        oracleBgpPeeringIp = '10.0.0.16/31'
        vlan = 131
        cc_mappings = '[{{"bgpMd5AuthKey":{},"crossConnectOrCrossConnectGroupId":"{}",' \
                      '"customerBgpPeeringIp":"{}","oracleBgpPeeringIp":"{}","vlan":{}}}]'\
                      .format(bgpMd5AuthKey, cross_connect_group, customerBgpPeeringIp, oracleBgpPeeringIp, vlan)
        params = [
            'network', 'virtual-circuit', 'create',
            '--display-name', vc_name,
            '--type', 'PRIVATE',
            '--bandwidth-shape-name', vc_bandwidth,
            '--cross-connect-mappings', cc_mappings,
            '--customer-bgp-asn', '12345',
            '--gateway-id', drg_id,
            '--wait-for-state', 'PROVISIONED',
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result, json_response_expected=False)
        assert util.get_json_from_mixed_string(result.output)['data']['lifecycle-state'] == 'PROVISIONED'
        vc_id = util.get_json_from_mixed_string(result.output)['data']['id']

        # Get virtual-circuit by virtual-circuit OCID
        params = [
            'network', 'virtual-circuit', 'get',
            '--virtual-circuit-id', vc_id
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # List virtual-circuits in a given compartment
        params = [
            'network', 'virtual-circuit', 'list',
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # Update virtual-circuit
        vc_name = util.random_name('cli_test_network_virtualcircuit')
        params = [
            'network', 'virtual-circuit', 'update',
            '--virtual-circuit-id', vc_id,
            '--display-name', vc_name
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

    # Teardown of virtual-circuit
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_fastconnect_fixture_virtualcircuit_delete.yml'):
        if vc_id:
            # Delete virtual-circuit
            params = [
                'network', 'virtual-circuit', 'delete',
                '--virtual-circuit-id', vc_id,
                '--wait-for-state', 'TERMINATED',
                '--force'
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result, json_response_expected=False)

            # Delete the dynamic gateway
            params = [
                'network', 'drg', 'delete',
                '--drg-id', drg_id,
                '--wait-for-state', 'TERMINATED',
                '--force'
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result, json_response_expected=False)


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile] + params, ** args)

    return result
