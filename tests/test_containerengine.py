# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import os
import json
import yaml
import oci_cli
import pytest

from . import util
from . import test_config_container

CLUSTER_CREATE_PROVISIONING_TIME_SEC = 1200
PROVISIONING_TIME_SEC = 300
DELETION_TIME_SEC = 300


@pytest.fixture(scope='module')
def oce_cluster(runner, config_file, config_profile):
    # Set-up of cross-connect group
    cluster_id = None
    with test_config_container.create_vcr().use_cassette('test_oce_fixture_cluster.yml'):
        # Create a VCN for Kubernetes cluster
        vcn_name = util.random_name('cli_test_oce_vcn')
        vcn_cidr_block = "10.0.0.0/16"
        pod_cidr_block = "10.96.0.0/16"
        kub_svcs_cidr_block = "10.240.0.0/16"
        params = [
            'network', 'vcn', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--display-name', vcn_name,
            '--cidr-block', vcn_cidr_block
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        vcn_ocid = util.find_id_in_response(result.output)
        util.wait_until(['network', 'vcn', 'get', '--vcn-id', vcn_ocid], 'AVAILABLE',
                        max_wait_seconds=PROVISIONING_TIME_SEC)

        # Create 5 subnets: 1st 3 subnets for Kubernetes worker nodes and last 2 subnets for load balancers
        subnet_cidrs = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24", "10.0.4.0/24", "10.0.5.0/24"]
        subnet_names = list()
        subnet_ocids = list()

        for idx, subnet_cidr_block in enumerate(subnet_cidrs):
            subnet_names.append(util.random_name('cli_test_compute_subnet'))
            params = [
                'network', 'subnet', 'create',
                '--compartment-id', util.COMPARTMENT_ID,
                '--availability-domain', util.availability_domain(),
                '--display-name', subnet_names[idx],
                '--vcn-id', vcn_ocid,
                '--cidr-block', subnet_cidr_block,
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)
            subnet_ocids.append(util.find_id_in_response(result.output))
            util.wait_until(['network', 'subnet', 'get', '--subnet-id', subnet_ocids[idx]], 'AVAILABLE',
                            max_wait_seconds=PROVISIONING_TIME_SEC)

        # Find Supported Kubernetes versions
        params = [
            'ce', 'cluster-options', 'get',
            '--cluster-option-id', 'all'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        # Pick the first version in the response to be used for the test cluster
        kub_version = json.loads(result.output)['data']['kubernetes-versions'][0]

        # Create a cluster
        cluster_lb_subnets = '["' + subnet_ocids[3] + '", "' + subnet_ocids[4] + '"]'
        cluster_name = util.random_name('cli_oce_cluster_name')
        params = [
            'ce', 'cluster', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--name', cluster_name,
            '--vcn-id', vcn_ocid,
            '--kubernetes-version', kub_version,
            '--dashboard-enabled', 'true',
            '--tiller-enabled', 'true',
            '--pods-cidr', pod_cidr_block,
            '--services-cidr', kub_svcs_cidr_block,
            '--service-lb-subnet-ids', cluster_lb_subnets
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # Create cluster returns work request. Get work request response to obtain cluster OCID.
        response = json.loads(result.output)
        work_request_id = response['opc-work-request-id']
        get_work_request_result = util.wait_until(['ce', 'work-request', 'get', '--work-request-id', work_request_id],
                                                  'SUCCEEDED', state_property_name='status',
                                                  max_wait_seconds=CLUSTER_CREATE_PROVISIONING_TIME_SEC)
        util.validate_response(get_work_request_result)
        cluster_id = json.loads(get_work_request_result.output)['data']['resources'][0]['identifier']

        # Get a cluster using cluster ID
        get_params = [
            'ce', 'cluster', 'get',
            '--cluster-id', cluster_id
        ]
        result = invoke(runner, config_file, config_profile, get_params)
        util.validate_response(result)

        # Check the kubeconfig file generation
        params = [
            'ce', 'cluster', 'create-kubeconfig',
            '--cluster-id', cluster_id,
            '--file', 'kubeconfig'
        ]
        invoke(runner, config_file, config_profile, params)
        # Validate the kubernetes config is in valid YAML format
        with open('kubeconfig', 'r') as config:
            config_data = config.read()
            yaml.safe_load(config_data)

        os.remove('kubeconfig')

        # Get the list of clusters in the compartment
        params = [
            'ce', 'cluster', 'list',
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # Update the cluster using cluster ID
        cluster_name = util.random_name('cli_test_oce_cluster')
        params = [
            'ce', 'cluster', 'update',
            '--cluster-id', cluster_id,
            '--name', cluster_name
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # Update cluster returns work request. Get work request response to check the command succeeded
        response = json.loads(result.output)
        work_request_id = response['opc-work-request-id']
        get_work_request_result = util.wait_until(['ce', 'work-request', 'get', '--work-request-id', work_request_id],
                                                  'SUCCEEDED', state_property_name='status',
                                                  max_wait_seconds=PROVISIONING_TIME_SEC)
        util.validate_response(get_work_request_result)

        # Get the list of work request logs
        params = [
            'ce', 'work-request-log-entry', 'list',
            '--work-request-id', work_request_id,
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        yield cluster_id, subnet_ocids[0], subnet_ocids[1], subnet_ocids[2]

    # Tear down sequence
    with test_config_container.create_vcr().use_cassette('test_oce_fixture_cluster_delete.yml'):
        # Delete the cluster
        params = [
            'ce', 'cluster', 'delete',
            '--cluster-id', cluster_id,
            '--force'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        # Get the cluster and check that it moves to DELETED state
        invoke(runner, config_file, config_profile, get_params)
        util.wait_until(get_params, 'DELETED', max_wait_seconds=DELETION_TIME_SEC)

        # Delete the subnets
        for subnet_id in subnet_ocids:
            params = [
                'network', 'subnet', 'delete',
                '--subnet-id', subnet_id,
                '--wait-for-state', 'TERMINATED',
                '--force'
            ]
            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result, json_response_expected=False)

        # Delete the VCN
        params = [
            'network', 'vcn', 'delete',
            '--vcn-id', vcn_ocid,
            '--wait-for-state', 'TERMINATED',
            '--force'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result, json_response_expected=False)


@util.slow
def test_oce_node_pool(runner, config_file, config_profile, oce_cluster):
    # Set-up of cross-connect group
    node_pool_id = None
    with test_config_container.create_vcr().use_cassette('test_oce_fixture_node_pool.yml'):
        # Find the node-pool options
        params = [
            'ce', 'node-pool-options', 'get',
            '--node-pool-option-id', 'all'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        # Pick the first version in the response to be used for the test cluster
        kub_version = json.loads(result.output)['data']['kubernetes-versions'][0]  # v1.8.11
        node_shape = "VM.Standard1.1"
        node_image = "Oracle-Linux-7.4"
        # Get the return values from the cluster generator
        cluster_id, subnet_id1, subnet_id2, subnet_id3 = oce_cluster
        node_pool_subnet_ids = '["' + subnet_id1 + '", "' + subnet_id2 + '", "' + subnet_id3 + '"]'

        # Create a node pool
        np_name = util.random_name('cli_test_oce_np')
        params = [
            'ce', 'node-pool', 'create',
            '--name', np_name,
            '--cluster-id', cluster_id,
            '--compartment-id', util.COMPARTMENT_ID,
            '--kubernetes-version', kub_version,
            '--node-image-name', node_image,
            '--node-shape', node_shape,
            '--subnet-ids', node_pool_subnet_ids
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        # Create node-pool returns work request. Get work request response to obtain the node-pool OCID.
        response = json.loads(result.output)
        work_request_id = response['opc-work-request-id']
        get_work_request_result = util.wait_until(['ce', 'work-request', 'get', '--work-request-id', work_request_id],
                                                  'SUCCEEDED', state_property_name='status',
                                                  max_wait_seconds=PROVISIONING_TIME_SEC)
        util.validate_response(get_work_request_result)
        node_pool_id = json.loads(get_work_request_result.output)['data']['resources'][0]['identifier']

        # Get a node pool from node pool id
        params = [
            'ce', 'node-pool', 'get',
            '--node-pool-id', node_pool_id
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # List the node pool
        params = [
            'ce', 'node-pool', 'list',
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # Update the node pool
        np_name = util.random_name('cli_test_oce_node_pool')
        params = [
            'ce', 'node-pool', 'update',
            '--node-pool-id', node_pool_id,
            '--name', np_name
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        # Update node pool returns work request. Get work request response to check the command succeeded
        response = json.loads(result.output)
        work_request_id = response['opc-work-request-id']
        get_work_request_result = util.wait_until(['ce', 'work-request', 'get', '--work-request-id', work_request_id],
                                                  'SUCCEEDED', state_property_name='status',
                                                  max_wait_seconds=PROVISIONING_TIME_SEC)
        util.validate_response(get_work_request_result)

    # Tear down the node pool resource
    with test_config_container.create_vcr().use_cassette('test_oce_fixture_node_pool_delete.yml'):
        # Delete the node pool
        params = [
            'ce', 'node-pool', 'delete',
            '--node-pool-id', node_pool_id,
            '--force'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        # Delete node pool returns work request. Get work request response to check the command succeeded
        response = json.loads(result.output)
        work_request_id = response['opc-work-request-id']
        get_work_request_result = util.wait_until(['ce', 'work-request', 'get', '--work-request-id', work_request_id],
                                                  'SUCCEEDED', state_property_name='status',
                                                  max_wait_seconds=DELETION_TIME_SEC)
        util.validate_response(get_work_request_result)


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True,
           strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile',
                                                           config_profile] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile',
                                                           config_profile] + params, ** args)

    return result
