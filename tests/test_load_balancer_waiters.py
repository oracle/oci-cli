# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import oci_cli
from . import util

LB_PROVISIONING_TIME_SEC = 300  # 5 minutes

DEFAULT_WAIT_TIME = 120  # 1 minute


@util.slow
def test_load_balancer_operations_with_waiters(runner, config_file, config_profile, vcn_and_subnets, key_pair_files):
    subnet_ocid_1 = vcn_and_subnets[1]
    subnet_ocid_2 = vcn_and_subnets[2]

    lb_name = util.random_name('cli_lb')
    params = [
        'load-balancer', 'create',
        '-c', util.COMPARTMENT_ID,
        '--display-name', lb_name,
        '--shape-name', '100Mbps',
        '--subnet-ids', '["{}","{}"]'.format(subnet_ocid_1, subnet_ocid_2),
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result, json_response_expected=False)
    load_balancer = util.get_json_from_mixed_string(result.output)
    assert load_balancer['data']['lifecycle-state'] == 'ACTIVE'
    assert 'loadbalancer' in load_balancer['data']['id']
    assert load_balancer['data']['display-name'] == lb_name
    assert load_balancer['data']['shape-name'] == '100Mbps'
    assert len(load_balancer['data']['subnet-ids']) == 2
    assert subnet_ocid_1 in load_balancer['data']['subnet-ids']
    assert subnet_ocid_2 in load_balancer['data']['subnet-ids']

    _do_backend_and_backend_set(runner, load_balancer['data']['id'], config_file, config_profile)
    _do_certificate(runner, load_balancer['data']['id'], config_file, config_profile, key_pair_files)

    params = [
        'load-balancer', 'delete',
        '--load-balancer-id', load_balancer['data']['id'],
        '--force',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer['data']['id'])


def _do_backend_and_backend_set(runner, load_balancer_id, config_file, config_profile):
    backend_set_name = util.random_name('cli_lb_backend_set')

    params = [
        'backend-set', 'create',
        '--name', backend_set_name,
        '--policy', 'ROUND_ROBIN',
        '--load-balancer-id', load_balancer_id,
        '--health-checker-protocol', 'HTTP',
        '--health-checker-return-code', '200',
        '--health-checker-url-path', '/healthcheck',
        '--health-checker-interval-in-ms', '60000',  # 1 minute
        '--session-persistence-cookie-name', '*',
        '--session-persistence-disable-fallback', 'false',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    ip_address = '10.0.0.10'
    port = '80'
    params = [
        'backend', 'create',
        '--ip-address', ip_address,
        '--port', port,
        '--load-balancer-id', load_balancer_id,
        '--backend-set-name', backend_set_name,
        '--weight', '3',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    backend_name = "{}:{}".format(ip_address, port)
    params = [
        'backend', 'update',
        '--load-balancer-id', load_balancer_id,
        '--backend-set-name', backend_set_name,
        '--backend-name', backend_name,
        '--weight', '2',
        '--offline', 'true',
        '--backup', 'false',
        '--drain', 'false',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    params = [
        'backend', 'delete',
        '--load-balancer-id', load_balancer_id,
        '--backend-set-name', backend_set_name,
        '--backend-name', backend_name,
        '--force',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    _do_listener(runner, load_balancer_id, backend_set_name, config_file, config_profile)

    params = [
        'backend-set', 'delete',
        '--load-balancer-id', load_balancer_id,
        '--backend-set-name', backend_set_name,
        '--force',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)


def _do_certificate(runner, load_balancer_id, config_file, config_profile, key_pair_files):
    private_key_filename = key_pair_files[1]
    certificate_filename = key_pair_files[2]

    cert_name = util.random_name('cli_lb_certificate')

    params = [
        'certificate', 'create',
        '--certificate-name', cert_name,
        '--load-balancer-id', load_balancer_id,
        '--ca-certificate-file', certificate_filename,
        '--private-key-file', private_key_filename,
        '--public-certificate-file', certificate_filename,
        '--passphrase', 'secret!',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    params = [
        'certificate', 'delete',
        '--load-balancer-id', load_balancer_id,
        '--certificate-name', cert_name,
        '--force',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)


def _do_listener(runner, load_balancer_id, backend_set_name, config_file, config_profile):
    listener_name = util.random_name('cli_listener')
    params = [
        'listener', 'create',
        '--default-backend-set-name', backend_set_name,
        '--load-balancer-id', load_balancer_id,
        '--name', listener_name,
        '--port', '8080',
        '--protocol', 'HTTP',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    params = [
        'listener', 'update',
        '--listener-name', listener_name,
        '--default-backend-set-name', backend_set_name,
        '--load-balancer-id', load_balancer_id,
        '--port', '8080',
        '--protocol', 'HTTP',
        '--force',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)

    params = [
        'listener', 'delete',
        '--load-balancer-id', load_balancer_id,
        '--listener-name', listener_name,
        '--force',
        '--wait-for-state', 'SUCCEEDED'
    ]
    result = invoke(runner, config_file, config_profile, params)
    _validate_work_request_result(result, load_balancer_id)


def _validate_work_request_result(result, load_balancer_id):
    util.validate_response(result, json_response_expected=False)
    assert 'Action completed. Waiting until the work request has entered state: SUCCEEDED' in result.output

    work_request = util.get_json_from_mixed_string(result.output)
    assert work_request['data']['load-balancer-id'] == load_balancer_id
    assert work_request['data']['lifecycle-state'] == 'SUCCEEDED'


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile, 'lb'] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile, 'lb'] + params, ** args)

    return result
