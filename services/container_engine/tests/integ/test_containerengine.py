# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os
import json
import yaml
import oci_cli
import pytest
import shutil

from tests import util
from tests import test_config_container

CLUSTER_CREATE_PROVISIONING_TIME_SEC = 1200
CLUSTER_UPDATE_TIME_SEC = 1200
PROVISIONING_TIME_SEC = 300
DELETION_TIME_SEC = 1200
DEFAULT_KUBECONFIG_LOCATION = '~/.kube/config'
USER_KUBECONFIG_DIR = './config/'
USER_KUBECONFIG_LOCATION = USER_KUBECONFIG_DIR + 'kubeconfig'
CASSETTE_LIBRARY_DIR = 'services/container_engine/tests/cassettes'
# When we run this test under tox with multi-threading, some of these tests were failing
# as there was contention to read/write to DEFAULT_KUBECONFIG_LOCATION.
# Thus it is useful to explictly specify a separate config for each test.
# The default assumption is that the test will be run in a multi-threaded environment
# and the original intent to not use --file will be altered.
is_multi_threaded_test = True


@pytest.fixture(scope='module')
def oce_cluster(runner, config_file, config_profile):
    # Set-up of cross-connect group
    cluster_id = None
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_oce_fixture_cluster.yml'):
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

        regional_subnet_name = util.random_name('cli_test_compute_subnet')
        subnet_names.append(regional_subnet_name)
        params = [
            'network', 'subnet', 'create',
            '--compartment-id', util.COMPARTMENT_ID,
            '--display-name', regional_subnet_name,
            '--vcn-id', vcn_ocid,
            '--cidr-block', "10.0.6.0/24",
        ]

        # Create a public regional subnet for the cluster endpoint
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        regional_subnet_ocid = util.find_id_in_response(result.output)
        subnet_ocids.append(regional_subnet_ocid)
        util.wait_until(['network', 'subnet', 'get', '--subnet-id', regional_subnet_ocid], 'AVAILABLE',
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
        kub_upgrade_version = json.loads(result.output)['data']['kubernetes-versions'][1]

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
            '--service-lb-subnet-ids', cluster_lb_subnets,
            '--endpoint-subnet-id', regional_subnet_ocid
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
        if os.path.exists('kubeconfig'):
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
            '--name', cluster_name,
            '--kubernetes-version', kub_upgrade_version
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # Update cluster returns work request. Get work request response to check the command succeeded
        response = json.loads(result.output)
        work_request_id = response['opc-work-request-id']
        get_work_request_result = util.wait_until(['ce', 'work-request', 'get', '--work-request-id', work_request_id],
                                                  'SUCCEEDED', state_property_name='status',
                                                  max_wait_seconds=CLUSTER_UPDATE_TIME_SEC)
        util.validate_response(get_work_request_result)

        # Get the list of work request logs
        params = [
            'ce', 'work-request-log-entry', 'list',
            '--work-request-id', work_request_id,
            '--compartment-id', util.COMPARTMENT_ID
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # Update a cluster endpoint
        params = [
            'ce', 'cluster', 'update-endpoint-config',
            '--cluster-id', cluster_id,
            '--is-public-ip-enabled', 'true',
            '--nsg-ids', '[]'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # Update endpoint config returns a work request. Get work request response to check the command succeeded
        response = json.loads(result.output)
        work_request_id = response['opc-work-request-id']
        get_work_request_result = util.wait_until(['ce', 'work-request', 'get', '--work-request-id', work_request_id],
                                                  'SUCCEEDED', state_property_name='status',
                                                  max_wait_seconds=CLUSTER_UPDATE_TIME_SEC)
        util.validate_response(get_work_request_result)

        yield cluster_id, subnet_ocids[0], subnet_ocids[1], subnet_ocids[2]

    # Tear down sequence
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_oce_fixture_cluster_delete.yml'):
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

    if os.path.isdir(os.path.expandvars(os.path.expanduser(USER_KUBECONFIG_DIR))):
        shutil.rmtree(USER_KUBECONFIG_DIR)


@util.slow
@pytest.mark.skip('Skipped to allow DEXREQ-2587')
def test_oce_node_pool(runner, config_file, config_profile, oce_cluster):
    # Set-up of cross-connect group
    node_pool_id = None
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_oce_fixture_node_pool.yml'):
        # Find the node-pool options
        params = [
            'ce', 'node-pool-options', 'get',
            '--node-pool-option-id', 'all'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        # Pick the first version in the response to be used for the test cluster
        kub_version = json.loads(result.output)['data']['kubernetes-versions'][0]
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
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_oce_fixture_node_pool_delete.yml'):
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


# INPUT:
# Overwrite flag (--overwrite) is NOT set
# Filename option (--file) NOT explcitly provided by the user
# Default kubeconfig file (~/.kube/config) does NOT exist
# OUTPUT:
# New kubeconfig file created at default location with command returned contents.
def test_create_kubeconfig_1(runner, config_file, config_profile, oce_cluster, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_oce_create_kubeconfig_test1.yml'):
        config_file_path = os.path.expandvars(os.path.expanduser(DEFAULT_KUBECONFIG_LOCATION))
        if is_multi_threaded_test:
            config_file_path += "_" + request.function.__name__
        # There should be no default kubeconfig file for this test.
        if os.path.isfile(config_file_path):
            os.remove(config_file_path)

        cluster_id, _, _, _ = oce_cluster
        params = [
            'ce', 'cluster', 'create-kubeconfig',
            '--cluster-id', cluster_id
        ]
        if is_multi_threaded_test:
            params.append('--file')
            params.append(config_file_path)
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result, json_response_expected=False)

        # Check that a file got created at default kubeconfig location
        assert(os.path.isfile(config_file_path))
        # Check if it is a valid yaml. yaml load will raise an exception in case of invalid yaml
        with open(config_file_path, 'r') as f:
            kubeconfig = yaml.safe_load(f)
        # Check there is only ONE cluster, user and context in the downloaded kubeconfig for this test.
        assert(len(kubeconfig['clusters']) == 1)
        assert (len(kubeconfig['contexts']) == 1)
        assert (len(kubeconfig['users']) == 1)


# TEST 2A
# INPUT:
# Overwrite flag (--overwrite) is NOT set
# Filename option (--file) NOT explicitly provided by the user
# Default kubeconfig file (~/.kube/config) does exist
# Default file is PRE-POPULATED with kubeconfig contents.
# New contents from the command and old contents in kubeconfig have DIFFERENT clusters
# OUTPUT:
# Merge new contents with old contents to the default kubeconfig file. Since the contents are DIFFERENT, merged
# kubeconfig has one more cluster, user and context than before.
# TEST 2B
# INPUT:
# Overwrite flag (--overwrite) is NOT set
# Filename option (--file) NOT explicitly provided by the user
# Default kubeconfig file (~/.kube/config) does exist
# Default kubeconfig file is PRE-POPULATED kubeconfig contents.
# New contents from the command and old contents in kubeconfig have SAME clusters
# OUTPUT:
# Merge new contents with old contents to the default kubeconfig file. Since the contents are same, merged kubeconfig
# still has same number of clusters, users and context. However, the user now has new token for the cluster.
@pytest.mark.skip
def test_create_kubeconfig_2(runner, config_file, config_profile, oce_cluster, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_oce_create_kubeconfig_test2.yml'):

        # TEST 2A
        # There should be a pre-populated default kubeconfig file for this test.
        config_file_path = os.path.expandvars(os.path.expanduser(DEFAULT_KUBECONFIG_LOCATION))
        if is_multi_threaded_test:
            config_file_path += "_" + request.function.__name__
        # Remove any previous ./kube/config file if it exists
        if os.path.isfile(config_file_path):
            os.remove(config_file_path)
        # Create the directory path for the file based on default path ~/.kube/config
        if os.path.dirname(config_file_path) and not os.path.exists(os.path.dirname(config_file_path)):
            os.makedirs(os.path.dirname(config_file_path))
        # Write a sample kubeconfig to kubeconfig file at default location
        with open((config_file_path), 'w') as f:
            f.write(sample_kubeconfig)
        sample_kubeconfig_yaml = yaml.safe_load(sample_kubeconfig)
        cluster_id, _, _, _ = oce_cluster
        params = [
            'ce', 'cluster', 'create-kubeconfig',
            '--cluster-id', cluster_id
        ]
        if is_multi_threaded_test:
            params.append('--file')
            params.append(config_file_path)
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result, json_response_expected=False)

        # Check if it is a valid yaml. yaml load will raise an exception in case of invalid yaml
        with open(config_file_path, 'r') as f:
            kubeconfig = yaml.safe_load(f)
        # Check there is ONE more cluster, user and context added in the merged kubeconnfig file.
        assert(len(kubeconfig['clusters']) == len(sample_kubeconfig_yaml['clusters']) + 1)
        assert(len(kubeconfig['contexts']) == len(sample_kubeconfig_yaml['contexts']) + 1)
        assert(len(kubeconfig['users']) == len(sample_kubeconfig_yaml['users']) + 1)

        # TEST 2B
        # For this test, execute the command again
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result, json_response_expected=False)

        # Check if it is a valid yaml. yaml load will raise an exception in case of invalid yaml
        with open(config_file_path, 'r') as f:
            kubeconfig2 = yaml.safe_load(f)
        # Check the number of clusters, users and contexts remained the same after the merge
        assert(len(kubeconfig['clusters']) == len(kubeconfig2['clusters']))
        assert(len(kubeconfig['contexts']) == len(kubeconfig2['contexts']))
        assert(len(kubeconfig['users']) == len(kubeconfig2['users']))


# INPUT:
# Overwrite flag (--overwrite) is NOT set
# Filename option (--file) IS explicitly provided by the user
# Kubeconfig file does NOT exist at user provided file path.
# OUTPUT:
# New kubeconfig file created at user provided file location with command returned contents.
def test_create_kubeconfig_3(runner, config_file, config_profile, oce_cluster, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_oce_create_kubeconfig_test3.yml'):
        config_file_path = os.path.expandvars(os.path.expanduser(USER_KUBECONFIG_LOCATION + "_" + request.function.__name__))

        # There should be no file at user provided location for this test.
        if os.path.isfile(config_file_path):
            os.remove(config_file_path)

        cluster_id, _, _, _ = oce_cluster
        params = [
            'ce', 'cluster', 'create-kubeconfig',
            '--cluster-id', cluster_id,
            '--file', config_file_path
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result, json_response_expected=False)

        # Check that a file got created at user provided kubeconfig location
        assert(os.path.isfile(config_file_path))
        # Check if it is a valid yaml. yaml load will raise an exception in case of invalid yaml
        with open(config_file_path, 'r') as f:
            kubeconfig = yaml.safe_load(f)
        # Check there is only ONE cluster, user and context in the downloaded kubeconfig for this test.
        assert(len(kubeconfig['clusters']) == 1)
        assert (len(kubeconfig['contexts']) == 1)
        assert (len(kubeconfig['users']) == 1)


# INPUT:
# Overwrite flag (--overwrite) is NOT set
# Filename option (--file) IS provided by the user
# Kubeconfig file does exist at user provided file path.
# Kubeconfig file contents are EMPTY.
# OUTPUT:
# Existing kubeconfig file at user provided file location populated with command returned contents.
def test_create_kubeconfig_4(runner, config_file, config_profile, oce_cluster, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_oce_create_kubeconfig_test4.yml'):
        # There should be an EMPTY kubeconfig file at user provided location for this test.
        config_file_path = os.path.expandvars(os.path.expanduser(USER_KUBECONFIG_LOCATION + "_" + request.function.__name__))
        # Remove any previous file from user provided location USER_KUBECONFIG_LOCATION
        if os.path.isfile(config_file_path):
            os.remove(config_file_path)
        # Create the directory path for the file based on user provided file location USER_KUBECONFIG_LOCATION
        if os.path.dirname(config_file_path) and not os.path.exists(os.path.dirname(config_file_path)):
            os.makedirs(os.path.dirname(config_file_path))
        # Create an empty file at the user provided location
        open(config_file_path, 'w').close()

        cluster_id, _, _, _ = oce_cluster
        params = [
            'ce', 'cluster', 'create-kubeconfig',
            '--cluster-id', cluster_id,
            '--file', config_file_path
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result, json_response_expected=False)

        # Check if it is a valid yaml. yaml load will raise an exception in case of invalid yaml
        with open(config_file_path, 'r') as f:
            kubeconfig = yaml.safe_load(f)
        # Check there is only ONE cluster, user and context in the downloaded kubeconfig for this test.
        assert(len(kubeconfig['clusters']) == 1)
        assert (len(kubeconfig['contexts']) == 1)
        assert (len(kubeconfig['users']) == 1)


# INPUT:
# Overwrite flag (--overwrite) is SET.
# Filename option (--file) IS NOT provided by the user
# Default kubeconfig (~/.kube/config) file DOES exist at default file path.
# Default kubeconfig file has pre-populated kubeconfig contents.
# OUTPUT:
# Default kubeconfig file at user provided file location should be overwritten with command returned contents.
def test_create_kubeconfig_5(runner, config_file, config_profile, oce_cluster, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_oce_create_kubeconfig_test5.yml'):
        # There should be a pre-populated kubeconfig file at default location for this test.
        config_file_path = os.path.expandvars(os.path.expanduser(DEFAULT_KUBECONFIG_LOCATION))
        if is_multi_threaded_test:
            config_file_path += "_" + request.function.__name__
        # Remove any previous ./kube/config file if it exists
        if os.path.isfile(config_file_path):
            os.remove(config_file_path)
        # Create the directory path for the file based on default path ~/.kube/config
        if os.path.dirname(config_file_path) and not os.path.exists(os.path.dirname(config_file_path)):
            os.makedirs(os.path.dirname(config_file_path))
        # Write a sample kubeconfig to kubeconfig file at default location
        with open((config_file_path), 'w') as f:
            f.write(sample_kubeconfig)
        sample_kubeconfig_yaml = yaml.safe_load(sample_kubeconfig)
        cluster_id, _, _, _ = oce_cluster
        params = [
            'ce', 'cluster', 'create-kubeconfig',
            '--cluster-id', cluster_id,
            '--overwrite'
        ]
        if is_multi_threaded_test:
            params.append('--file')
            params.append(config_file_path)
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result, json_response_expected=False)

        # Check if it is a valid yaml. yaml load will raise an exception in case of invalid yaml
        with open(config_file_path, 'r') as f:
            kubeconfig = yaml.safe_load(f)
        # Check there is only ONE cluster, user and context in the downloaded kubeconfig for this test.
        assert(len(kubeconfig['clusters']) == 1)
        assert (len(kubeconfig['contexts']) == 1)
        assert (len(kubeconfig['users']) == 1)
        # Check that the cluster key has changed indicating we did overwrite old cluster content with new cluster content
        assert(kubeconfig['clusters'] != sample_kubeconfig_yaml['clusters'])


# INPUT:
# Overwrite flag (--overwrite) is SET.
# Filename option (--file) IS provided by the user
# File DOES NOT exist at user provided file path.
# OUTPUT:
# New kubeconfig file created at user provided file location populated with command returned contents.
def test_create_kubeconfig_6(runner, config_file, config_profile, oce_cluster, request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('test_oce_create_kubeconfig_test6.yml'):
        config_file_path = os.path.expandvars(os.path.expanduser(USER_KUBECONFIG_LOCATION + "_" + request.function.__name__))
        # There should be no file at user provided location for this test.
        if os.path.isfile(config_file_path):
            os.remove(config_file_path)

        cluster_id, _, _, _ = oce_cluster
        params = [
            'ce', 'cluster', 'create-kubeconfig',
            '--cluster-id', cluster_id,
            '--file', config_file_path,
            '--overwrite'
        ]
        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result, json_response_expected=False)

        # Check that a file got created at default kubeconfig location
        assert(os.path.isfile(config_file_path))
        # Check if it is a valid yaml. yaml load will raise an exception in case of invalid yaml
        with open(config_file_path, 'r') as f:
            kubeconfig = yaml.safe_load(f)
        # Check there is only ONE cluster, user and context in the downloaded kubeconfig for this test.
        assert(len(kubeconfig['clusters']) == 1)
        assert (len(kubeconfig['contexts']) == 1)
        assert (len(kubeconfig['users']) == 1)


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


# Sample kubeconfig consisting configuration of 2 clusters.
sample_kubeconfig = """apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURqRENDQW5TZ0F3SUJBZ0lVYmJ4VHF2eVR2U3RWMFVKRTAwYjJsT3Q5bktFd0RRWUpLb1pJaHZjTkFRRUwKQlFBd1hqRUxNQWtHQTFVRUJoTUNWVk14RGpBTUJnTlZCQWdUQlZSbGVHRnpNUTh3RFFZRFZRUUhFd1pCZFhOMAphVzR4RHpBTkJnTlZCQW9UQms5eVlXTnNaVEVNTUFvR0ExVUVDeE1EVDBSWU1ROHdEUVlEVlFRREV3WkxPRk1nClEwRXdIaGNOTVRneE1ERXdNVGMxTkRBd1doY05Nak14TURBNU1UYzFOREF3V2pCZU1Rc3dDUVlEVlFRR0V3SlYKVXpFT01Bd0dBMVVFQ0JNRlZHVjRZWE14RHpBTkJnTlZCQWNUQmtGMWMzUnBiakVQTUEwR0ExVUVDaE1HVDNKaApZMnhsTVF3d0NnWURWUVFMRXdOUFJGZ3hEekFOQmdOVkJBTVRCa3M0VXlCRFFUQ0NBU0l3RFFZSktvWklodmNOCkFRRUJCUUFEZ2dFUEFEQ0NBUW9DZ2dFQkFLK0J6SVVzOEI4ZjJXSzZHNTBxWG5WTjJGSDFXS3pZNHVjakZ6Q0sKdC9HN2RJajBJcHNvdC9jUk01citjdTVzNmZLNHN0SDVHWW9GRUhkVGhQanBuV1dGbWhIbjdMWlVvZ29EY05lMQpBYTJ3WkJuWTduTWFHZzhZc1YwMjBucGQ4aG5IRkthMG05ZmxNVVhjK2kwdVNRdk1CUmwwYVROZFcxVkNsdUl2CmViSUR3d0xzaWFzNmRPRU00UWVVYVU4M0VLQy85bDdGendFUXRhUVlSUDIxVWFoUXRFWnRBVXAyZDl0MGJCRDcKcllLNnlWOStvMXR2V084Ym1sMjJLR3dtMC90WmwrbnJ3MDV4VW9lZFBsbjVWZlRYTHFuU2NHazdsYS9NQzN2dAo2TVFpU3Q3UzQvVzFIMWFPVWxwdGVLQUNKazV1a0lqR3dRM0dTT2JmaFlyUDh5RUNBd0VBQWFOQ01FQXdEZ1lEClZSMFBBUUgvQkFRREFnRUdNQThHQTFVZEV3RUIvd1FGTUFNQkFmOHdIUVlEVlIwT0JCWUVGQmppTzFYSEhWMHkKV0VFUGFQVElOS2x5K3pSK01BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQUdYSE0zVWtjMmJ3dHlqNTlnYlN6cApmakNhUEZ3aFAvSE1YalcrbC9EbnFlUUY3UHF2dktiRk0xS0tNMlIzbGczSGt1MFlhTzQ1bVc5dWVEaC9yaDZpCjRxZFVMeGVITURGSUxBZ2hrTE5KdEJaNjMzb2w0MWtoMWx2dzhYWG9iRHpkeGRGSDBDU28yUExyWXJ0UVVCaVkKbzRtOGRNM0NpZE52cExmR3RkMUNQRWpiVmdGU0gyb0hxM2wyREpzQTFMdEg4VGJpcUZIbjRIZHpzeS9XZndHawp5ZXRNMmhPMGdPTi84Yit5U0JHN2dTR2FZUk8zK1FTTDNYWmxYaEJlZ1o3aXpuS1NMRTJmd0xnWG1zM2tOK0srClJ3dlRmOFBrR2dhQm5wVEkxSERqYU9HaERocjI4b3pjTHhsMTljc0hXS20weUM3WnBDK3lHZWRjOG1ESnptZFcKLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=
    server: https://cstczjxgm4t.us-phoenix-1.clusters.oci.oraclecloud.com:6443
  name: cluster-cstczjxgm4t
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURqRENDQW5TZ0F3SUJBZ0lVSzYzS1VlbzVTK3d6alZsUVRSS3V3eG9IZHlJd0RRWUpLb1pJaHZjTkFRRUwKQlFBd1hqRUxNQWtHQTFVRUJoTUNWVk14RGpBTUJnTlZCQWdUQlZSbGVHRnpNUTh3RFFZRFZRUUhFd1pCZFhOMAphVzR4RHpBTkJnTlZCQW9UQms5eVlXTnNaVEVNTUFvR0ExVUVDeE1EVDBSWU1ROHdEUVlEVlFRREV3WkxPRk1nClEwRXdIaGNOTVRrd01URXdNRE16T0RBd1doY05NalF3TVRBNU1ETXpPREF3V2pCZU1Rc3dDUVlEVlFRR0V3SlYKVXpFT01Bd0dBMVVFQ0JNRlZHVjRZWE14RHpBTkJnTlZCQWNUQmtGMWMzUnBiakVQTUEwR0ExVUVDaE1HVDNKaApZMnhsTVF3d0NnWURWUVFMRXdOUFJGZ3hEekFOQmdOVkJBTVRCa3M0VXlCRFFUQ0NBU0l3RFFZSktvWklodmNOCkFRRUJCUUFEZ2dFUEFEQ0NBUW9DZ2dFQkFPbjBIOGFlVEY3aTRPU0pkSUw2Nk1lbWhMOFVaS084SzZRU2tiUXAKcFlQTWROclNSRDlYQkhvd0tpQm04ZXpoRmJuU21BNFZDTURTVDlnNHNqcktPK01vSVBLWE1VOWxpekhYSTdQZgpZaFhVaVN5RWVuT3Fxa2grR24wZU9QbGlYTi96OHgyYjRRdEswMURMMHpMazE3ZFFCekI3ZStOZS9udlIrZ05nClFZOXRwOGlkY1Y3TityL2Z1OTM2MFhCblhpaXRQbmppMzNLbWtLOUJsWnp2dW9SQkg5NTkwRk03VndCSEI4Y0gKOUhWMDdzT2xEK25KaEN3QytpVHJIRDF2eUt1QTQxb3dDUkV6K3d0MFp2clpQNVdOYW4zNFpVRi9pdXNLTDlpMApPVFZZTDgvL0VNQ2N3cktxTmhqNjJmSjNuY2ZXTTNDTERSZG9sTStRTlhxRWZNVUNBd0VBQWFOQ01FQXdEZ1lEClZSMFBBUUgvQkFRREFnRUdNQThHQTFVZEV3RUIvd1FGTUFNQkFmOHdIUVlEVlIwT0JCWUVGRGtNOU04a2k4NGwKVm9oUVh2Z1NNWkR1eVF1dE1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQWR6WTNmbVovVGRWcDVaNzFhWjFRdwp0TWYreXpzVkRzNXNmZ0R2QU9KTk45L1F3SjZCclBFbENVb0VJd0FqRUNqYVpzL0ErOTN6TkpyLy9pYW1RY2NHClZqdjlnTVdrOUw3MUptTG1HRm9aYWdRRTU5WGxYekNnQWZnNU9Pc09KWEJhanR4ejhBcmhlWnNOcHVsRXVrWlEKNjlIZjNzQ3NNOHJsTE5Da1k5THpHNFA3WXhaOFdLNURTOFI1VUtKSTZxdlVmQm9BYm1WUzN4ZVVyYXR3UG90MAo3alRMNjhDNUJldDZSMFpJZmNIenU2SXpWeWluUlNsVE9KTjh0K1U2dDBTejl5Uzhab2hrdE12cFBxZ2pFR3l3CkRpYVdTU0x6d1VITFVDa3ZZcFZqNFloZ3EwQ3YvaUF3a3FGRmNKdlBQaGtYRmZWMXp1eFlwY3NlWUExcVdDdjIKLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=
    server: https://cytom3dgzqt.us-phoenix-1.clusters.oci.oraclecloud.com:6443
  name: cluster-cytom3dgzqt
contexts:
- context:
    cluster: cluster-cstczjxgm4t
    user: user-cstczjxgm4t
  name: context-cstczjxgm4t
- context:
    cluster: cluster-cytom3dgzqt
    user: user-cytom3dgzqt
  name: context-cytom3dgzqt
current-context: context-cstczjxgm4t
kind: Config
preferences: {}
users:
- name: user-cstczjxgm4t
  user:
    token: eyJoZWFkZXIiOnsiQXV0aG9yaXphdGlvbiI6WyJTaWduYXR1cmUgYWxnb3JpdGhtPVwicnNhLXNoYTI1NlwiLGhlYWRlcnM9XCJkYXRlIChyZXF1ZXN0LXRhcmdldCkgaG9zdCBjb250ZW50LWxlbmd0aCBjb250ZW50LXR5cGUgeC1jb250ZW50LXNoYTI1NlwiLGtleUlkPVwib2NpZDEudGVuYW5jeS5vYzEuLmFhYWFhYWFhM3ZpM2Z0M3lpM3NxNG5oaXFsNG52YnpqejZnaXBibjcyaDd3ZXJsNm5qczZ4c3E0d2dkcS9vY2lkMS51c2VyLm9jMS4uYWFhYWFhYWE1M2ZpaGcyYnVzdXV5YnF3amZyY2VpYXJ0anVjbXBzbWs3ZnRuenlueGplbnk2cWRzcGpxL2E2OjYzOjAwOmI3OjA4OmJkOjcyOjM4OjZhOjZjOjhmOjEzOjk1OjgwOmVjOjBjXCIsc2lnbmF0dXJlPVwiRk5Ec0FlK21MY2lRclQrdDcxM0lCNDRVUklxL1B0VzBGRGw4TjI4dml2SEhRV1pNdTR5RUdMZFBCVzRYRzBFMzRFbzBhRytNUnpVZUZqb3Myd2MxbWVkaHF6bThVWC8rN2c1Z0dFTGRkamU1RUNWM1JJeUZrYzBiYUZXYVFoUFNibzVkNnBCQ3poTTcrNTEvZEJWTDdzMnQ3Sk1FemJxaFVVVGxhN0lzV3ZualJuUXFpZUVzVW5LRnIybE41S2JjUDBaeXU3OG8rQ1l1djUrRzBjME0zNFBqWDI5azZVUVY0T1E1NlAxTGpLRUxtZWplWkNkWGpTQzFPQ0xwWWRHL244cXhHemtJa1JlTkh5R0h2UEFpYzcxaFJteEEvQWZjV3B0UGp5a1ljdWRlM0VRQUVPWVNaSkFHQnpWdXhJclVrTnozOU5uOHI5YXdkVTlvZ29MWmV3PT1cIix2ZXJzaW9uPVwiMVwiIl0sIkNvbnRlbnQtTGVuZ3RoIjpbIjIiXSwiQ29udGVudC1UeXBlIjpbImFwcGxpY2F0aW9uL2pzb24iXSwiRGF0ZSI6WyJUaHUsIDEwIEphbiAyMDE5IDAzOjI1OjQ2IEdNVCJdLCJYLUNvbnRlbnQtU2hhMjU2IjpbIlJCTnZvMVd6WjRvUlJxMFc5K2hrbnBUN1Q4SWY1MzZERU1CZzloeXEvNG89Il19LCJib2R5Ijp7InRva2VuVmVyc2lvbiI6IjEuMC4wIiwiZXhwaXJhdGlvbiI6MjU5MjAwMDAwMDAwMDAwMH0sImhvc3QiOiJjb250YWluZXJlbmdpbmUudXMtcGhvZW5peC0xLm9yYWNsZWNsb3VkLmNvbSIsInJlcXVlc3RfdXJpIjoiLzIwMTgwMjIyL2NsdXN0ZXJzL29jaWQxLmNsdXN0ZXIub2MxLnBoeC5hYWFhYWFhYWFmdGRjbWxjaGE0Z2tubGVtcnJ3a3psY21leXRreXp3bW0zZHN5M2ZtY3N0Y3pqeGdtNHQva3ViZWNvbmZpZy9jb250ZW50In0=
- name: user-cytom3dgzqt
  user:
    token: eyJoZWFkZXIiOnsiQXV0aG9yaXphdGlvbiI6WyJTaWduYXR1cmUgYWxnb3JpdGhtPVwicnNhLXNoYTI1NlwiLGhlYWRlcnM9XCJkYXRlIChyZXF1ZXN0LXRhcmdldCkgaG9zdCBjb250ZW50LWxlbmd0aCBjb250ZW50LXR5cGUgeC1jb250ZW50LXNoYTI1NlwiLGtleUlkPVwib2NpZDEudGVuYW5jeS5vYzEuLmFhYWFhYWFhM3ZpM2Z0M3lpM3NxNG5oaXFsNG52YnpqejZnaXBibjcyaDd3ZXJsNm5qczZ4c3E0d2dkcS9vY2lkMS51c2VyLm9jMS4uYWFhYWFhYWE1M2ZpaGcyYnVzdXV5YnF3amZyY2VpYXJ0anVjbXBzbWs3ZnRuenlueGplbnk2cWRzcGpxL2E2OjYzOjAwOmI3OjA4OmJkOjcyOjM4OjZhOjZjOjhmOjEzOjk1OjgwOmVjOjBjXCIsc2lnbmF0dXJlPVwiYVhDSGkxOTkzN1lMK09QQjJQZVZCRWpiSTh2YkJrWFNEMEpscStvN3JJREs4WWE2NTduVElQNkxOZ0dHdHNkOHlvRENiQUx6SEdUSWhiL1lId3RXN3VvR01QaTE4eTV2UEl1cHBNcUhIT3pHVDU1dktIY09QR0lsTkg5cHpOZnBHeW1RRVVtUFNmdVFDRDVKOGFHTlR5ai93aU5XR2FTSHVQMmJ3QTdCdEp3SE1KMnpwZEl3ejg4d3RBV1NyTk5nV1NMM3h6Nk42S3cyaVFWblhXV1VsTFBLSTdYNDJDQUh2ZG02c1puRTdOMmJ5NnNhdlZTTjBBcS8zb2tldEZVTTN3WVNyYkdJRy9jRzdjdVY0L0YxVnAvcllCMnFyWEFQb243WXZvb05XOFBCZVBQVDFMekF6WTZPRVFnbHdQcG12Rm5CcXgwRk5kcTlZK0pwWFo0dGJRPT1cIix2ZXJzaW9uPVwiMVwiIl0sIkNvbnRlbnQtTGVuZ3RoIjpbIjIiXSwiQ29udGVudC1UeXBlIjpbImFwcGxpY2F0aW9uL2pzb24iXSwiRGF0ZSI6WyJUaHUsIDEwIEphbiAyMDE5IDA0OjU2OjUxIEdNVCJdLCJYLUNvbnRlbnQtU2hhMjU2IjpbIlJCTnZvMVd6WjRvUlJxMFc5K2hrbnBUN1Q4SWY1MzZERU1CZzloeXEvNG89Il19LCJib2R5Ijp7InRva2VuVmVyc2lvbiI6IjEuMC4wIiwiZXhwaXJhdGlvbiI6MjU5MjAwMDAwMDAwMDAwMH0sImhvc3QiOiJjb250YWluZXJlbmdpbmUudXMtcGhvZW5peC0xLm9yYWNsZWNsb3VkLmNvbSIsInJlcXVlc3RfdXJpIjoiLzIwMTgwMjIyL2NsdXN0ZXJzL29jaWQxLmNsdXN0ZXIub2MxLnBoeC5hYWFhYWFhYWFmdGRheWpzZzR5d215dGJnZTNkZW16d216cXRhemxlZ3pyZ2N5cnhnY3l0b20zZGd6cXQva3ViZWNvbmZpZy9jb250ZW50In0="""
