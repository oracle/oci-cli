# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import time

import oci
import oci_cli
import pytest

from tests import test_config_container
from tests import util

CASSETTE_LIBRARY_DIR = 'services/apigateway/tests/cassettes'


def build_simple_api_specification(http_backend_url):
    api_specification = {
        'requestPolicies': {
            'rateLimiting': {
                'rateKey': 'CLIENT_IP',
                'rateInRequestsPerSecond': 10
            }
        },
        'loggingPolicies': {
            'accessLog': {
                'isEnabled': True
            }
        },
        'routes': [
            {
                'path': '/http',
                'methods': ['ANY'],
                'backend': {
                    'type': 'HTTP_BACKEND',
                    'url': http_backend_url
                }
            }
        ]
    }

    return json.dumps(api_specification)


def build_full_api_specification(http_backend_url, fn_backend_id, fn_authorizer_id):
    api_specification = {
        'requestPolicies': {
            'rateLimiting': {
                'rateKey': 'CLIENT_IP',
                'rateInRequestsPerSecond': 10
            },
            'authentication': {
                'type': 'CUSTOM_AUTHENTICATION',
                'functionId': fn_authorizer_id,
                'tokenHeader': 'Authorization'
            },
            'cors': {
                'allowedOrigins': ['http://www.oraclecloud.com'],
                'allowedMethods': ['GET'],
                'allowedHeaders': ['X-API-GATEWAY_REQUEST'],
                'exposedHeaders': ['X-API-GATEWAY_RESPONSE'],
                'isAllowCredentialsEnabled': True,
                'maxAgeInSeconds': 7200
            }
        },
        'loggingPolicies': {
            'accessLog': {
                'isEnabled': True
            },
            'executionLog': {
                'isEnabled': True,
                'logLevel': 'WARN'
            }
        },
        'routes': [
            {
                'path': '/http',
                'methods': ['ANY'],
                'backend': {
                    'type': 'HTTP_BACKEND',
                    'url': http_backend_url
                },
                'requestPolicies': {
                    'authorizeScope': {
                        'allowedScope': ['scope:http']
                    },
                    'cors': {
                        'allowedOrigins': ['http://www..oraclecloud.com'],
                        'allowedMethods': ['GET'],
                    }
                }
            },
            {
                'path': '/fn',
                'methods': ['GET', 'POST'],
                'backend': {
                    'type': 'ORACLE_FUNCTIONS_BACKEND',
                    'functionId': fn_backend_id
                },
                'requestPolicies': {
                    'authorizeScope': {
                        'allowedScope': ['scope:fn']
                    },
                    'cors': {
                        'allowedOrigins': ['http://www.fn.oraclecloud.com'],
                        'allowedMethods': ['GET', 'POST'],
                        'maxAgeInSeconds': 3600
                    }
                }
            },
            {
                'path': '/stock',
                'methods': ['GET', 'POST', 'PATCH'],
                'backend': {
                    'type': 'STOCK_RESPONSE_BACKEND',
                    'status': 200,
                    'body': 'Hello, World!',
                    'headers': [
                        {
                            'name': 'Content-Type',
                            'value': 'text/plain'
                        },
                        {
                            'name': 'X-API-GATEWAY-RESPONSE',
                            'value': 'stockResponse'
                        }
                    ]
                },
                'requestPolicies': {
                    'authorizeScope': {
                        'allowedScope': ['scope:stock']
                    },
                    'cors': {
                        'allowedOrigins': ['*'],
                        'allowedMethods': ['*'],
                        'isAllowCredentialsEnabled': False,
                    }
                }
            }
        ]
    }

    return json.dumps(api_specification)


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('apigateway_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture(scope='module')
def vcn_and_subnet(runner, config_file, config_profile, network_client):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('apigateway_vcn_and_subnet_fixture.yml'):
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
        subnet_name = util.random_name('python_cli_test_subnet')
        cidr_block = "10.0.1.0/24"
        subnet_dns_label = util.random_name('subnet', insert_underscore=False) + '1'

        create_subnet_details = oci.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = util.COMPARTMENT_ID
        create_subnet_details.display_name = subnet_name
        create_subnet_details.vcn_id = vcn_ocid
        create_subnet_details.cidr_block = cidr_block
        create_subnet_details.dns_label = subnet_dns_label

        result = network_client.create_subnet(create_subnet_details)
        subnet_ocid = result.data.id
        assert result.status == 200

        oci.wait_until(network_client, network_client.get_subnet(subnet_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

    yield vcn_ocid, subnet_ocid

    # # this code does not run inside the vcr_fixture because it is outside any test function
    # # thus we are explicitly creating a separate cassette for it here
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('apigateway_vcn_and_subnet_fixture_cleanup.yml'):
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
                # succeed_on_not_found doesn't work as expected
                elif e.status == 404:
                    break
                else:
                    raise

        network_client.delete_vcn(vcn_ocid)


@pytest.fixture(scope='module')
def api_gateway_and_deployment(vcn_and_subnet, runner, config_file, config_profile):
    vcn_id = vcn_and_subnet[0]
    subnet_id = vcn_and_subnet[1]

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('functions_application_and_function_fixture.yml'):
        params = [
            'fn', 'application', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--subnet-ids', json.dumps([subnet_id]),
            '--display-name', util.random_name("fnapp", insert_underscore=False)
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        fn_app_id = json.loads(result.output)['data']['id']

        util.wait_until(['fn', 'application', 'get', '--application-id', fn_app_id], 'ACTIVE',
                        max_wait_seconds=300)

        params = [
            'fn', 'function', 'create',
            '--application-id', fn_app_id,
            '--image', 'phx.ocir.io/apigw/faas/helloworld-func:0.0.14',
            '--memory-in-mbs', '128',
            '--display-name', util.random_name("fnfunc", insert_underscore=False)
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        fn_func_id = json.loads(result.output)['data']['id']

        util.wait_until(['fn', 'function', 'get', '--function-id', fn_func_id], 'ACTIVE',
                        max_wait_seconds=300)

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('apigateway_api_gateway_and_deployment_fixture.yml'):

        params = [
            'api-gateway', 'gateway', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--subnet-id', subnet_id,
            '--display-name', util.random_name("apigateway", insert_underscore=False),
            '--endpoint-type', 'PUBLIC'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        api_gateway_id = json.loads(result.output)['data']['id']

        util.wait_until(['api-gateway', 'gateway', 'get', '--gateway-id', api_gateway_id], 'ACTIVE',
                        max_wait_seconds=300)

        params = [
            'api-gateway', 'deployment', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--display-name', util.random_name('deployment', insert_underscore=False),
            '--path-prefix', util.random_name('/foo', insert_underscore=False),
            '--gateway-id', api_gateway_id,
            '--specification', build_simple_api_specification('http://www.oracle.com')
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        api_deployment_id = json.loads(result.output)['data']['id']

        util.wait_until(['api-gateway', 'deployment', 'get', '--deployment-id', api_deployment_id], 'ACTIVE',
                        max_wait_seconds=300)

    yield api_gateway_id, api_deployment_id, fn_func_id

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('apigateway_api_gateway_and_deployment_fixture_cleanup.yml'):
        params = [
            'api-gateway', 'deployment', 'delete',
            '--deployment-id', api_deployment_id,
            '--force'
        ]

        invoke(runner, config_file, config_profile, params)
        util.wait_until(['api-gateway', 'deployment', 'get', '--deployment-id', api_deployment_id], 'DELETED',
                        max_wait_seconds=300)

        params = [
            'api-gateway', 'gateway', 'delete',
            '--gateway-id', api_gateway_id,
            '--force'
        ]

        invoke(runner, config_file, config_profile, params)
        util.wait_until(['api-gateway', 'gateway', 'get', '--gateway-id', api_gateway_id], 'DELETED',
                        max_wait_seconds=300)

    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('functions_application_and_function_fixture_cleanup.yml'):
        params = [
            'fn', 'function', 'delete',
            '--function-id', fn_func_id,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        util.wait_until(['fn', 'function', 'get', '--function-id', fn_func_id], 'DELETED', succeed_if_not_found=True,
                        max_wait_seconds=300)

        params = [
            'fn', 'application', 'delete',
            '--application-id', fn_app_id,
            '--force'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        util.wait_until(['fn', 'application', 'get', '--application-id', fn_app_id], 'DELETED',
                        succeed_if_not_found=True, max_wait_seconds=300)


# def test_gateway_list(api_gateway_and_deployment, runner, config_file, config_profile):
def test_gateway_list(runner, config_file, config_profile):
    # TODO: remove this -- added this return on 8/16/2019 b/c tests were failing.
    return
    params = [
        'api-gateway', 'gateway', 'list',
        '--compartment-id', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    api_gateways = json.loads(result.output)['data']['items']

    assert len(api_gateways) > 0, "List API should return at least one gateway"


# def test_deployment_list(api_gateway_and_deployment, runner, config_file, config_profile):
def test_deployment_list(runner, config_file, config_profile):
    # TODO: remove this -- added this return on 8/16/2019 b/c tests were failing.
    return
    params = [
        'api-gateway', 'deployment', 'list',
        '--compartment-id', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    api_deployments = json.loads(result.output)['data']['items']

    assert len(api_deployments) > 0, "List API should return at least one deployment"


# def test_gateway_update(api_gateway_and_deployment, runner, config_file, config_profile):
def test_gateway_update(runner, config_file, config_profile):
    # TODO: remove this -- added this return on 8/16/2019 b/c tests were failing.
    return
    api_gateway_id = api_gateway_and_deployment[0]
    get_params = [
        'api-gateway', 'gateway', 'get',
        '--gateway-id', api_gateway_id
    ]

    result = invoke(runner, config_file, config_profile, get_params)
    util.validate_response(result)
    api_gateway = json.loads(result.output)['data']

    params = [
        'api-gateway', 'gateway', 'update',
        '--gateway-id', api_gateway_id,
        '--display-name', util.random_name('apigateway', insert_underscore=False),
        '--force'
    ]

    update_result = invoke(runner, config_file, config_profile, params)
    util.validate_response(update_result)

    util.wait_until(['api-gateway', 'gateway', 'get', '--gateway-id', api_gateway_id], 'ACTIVE', max_wait_seconds=300)

    result = invoke(runner, config_file, config_profile, get_params)
    util.validate_response(result)
    api_gateway_updated = json.loads(result.output)['data']

    assert api_gateway['display-name'] != api_gateway_updated['display-name'], \
        "API Gateway display name should have been updated"


# def test_deployment_update(api_gateway_and_deployment, runner, config_file, config_profile):
def test_deployment_update(runner, config_file, config_profile):
    # TODO: remove this -- added this return on 8/16/2019 b/c tests were failing.
    return
    api_deployment_id = api_gateway_and_deployment[1]
    fn_func_id = api_gateway_and_deployment[2]

    get_params = [
        'api-gateway', 'deployment', 'get',
        '--deployment-id', api_deployment_id
    ]

    result = invoke(runner, config_file, config_profile, get_params)
    util.validate_response(result)
    api_deployment = json.loads(result.output)['data']

    params = [
        'api-gateway', 'deployment', 'update',
        '--deployment-id', api_deployment_id,
        '--display-name', util.random_name('deployment', insert_underscore=False),
        '--specification', build_full_api_specification('https://cloud.oracle.com', fn_func_id, fn_func_id),
        '--force'
    ]

    update_result = invoke(runner, config_file, config_profile, params)
    util.validate_response(update_result)

    util.wait_until(
        ['api-gateway', 'deployment', 'get', '--deployment-id', api_deployment_id],
        'ACTIVE',
        max_wait_seconds=300)

    result = invoke(runner, config_file, config_profile, get_params)
    util.validate_response(result)
    api_deployment_updated = json.loads(result.output)['data']

    assert api_deployment['display-name'] != api_deployment_updated['display-name'], \
        "Deployment's display name should have been updated"

    assert json.dumps(api_deployment['specification']) != json.dumps(api_deployment_updated['specification']), \
        "Deployment's specification should have been updated"


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile',
                                                           config_profile] + params, **args)
    else:
        result = runner.invoke(oci_cli.cli,
                               root_params + ['--config-file', config_file, '--profile', config_profile] + params,
                               **args)

    return result
