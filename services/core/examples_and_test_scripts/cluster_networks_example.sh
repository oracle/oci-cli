#!/usr/bin/env bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides an example of how use the instance pools CLI in terms of:
#   - Creating an instance config with HPC shape
#   - Creating a Cluster Network based on that configuration
#   - Wait for the Cluster Network to go to Running state.
#   - List instance of the Cluster Network
#   - Terminating Cluster Network
#   - Delete instance configuration
#
# For more help with specific cluster network commands with, see:
#   oci compute-management cluster-network -h
#
# Requirements for running this script:
#   - OCI CLI
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI
# Environment variables need to be set:
#   - COMPARTMENT_ID - Your compartment OCID
#   - AD - the AD where the pool will be spun up (the pool in this example only spans a single AD)
#   - SUBNET_ID - the subnet ocid in the AD above
#   - IMAGE_ID - the image ID to use for instances

set -e

if [[ -z "$COMPARTMENT_ID" ]]; then
    echo "COMPARTMENT_ID must be defined in your environment"
    exit 1
fi

if [[ -z "$AD" ]]; then
    echo "AD must be defined in your environment"
    exit 1
fi

if [[ -z "$SUBNET_ID" ]]; then
    echo "SUBNET_ID must be defined in your environment"
    exit 1
fi

if [[ -z "$IMAGE_ID" ]]; then
    echo "IMAGE_ID must be defined in your environment"
    exit 1
fi

if [ -d ./services/core/examples_and_test_scripts/cluster_network_example_files ];then
    cluster_networks_example_data="./services/core/examples_and_test_scripts/cluster_network_example_files"
elif [ -d ./cluster_network_example_files ];then
    cluster_networks_example_data="./cluster_network_example_files"
else
    echo "Could not find cluster_networks_example data files"
    exit 1
fi


INSTANCE_DETAILS_FILE_LOCATION="${cluster_networks_example_data}/instance_config_details_template.json"
PLACEMENT_CONFIG_FILE_LOCATION="${cluster_networks_example_data}/placement_details_template.json"
INSTANCE_POOLS_FILE_LOCATION="${cluster_networks_example_data}/instance_pools_input_template.json"

INSTANCE_DETAILS=$(sed s/__COMPARTMENT_ID__/$COMPARTMENT_ID/g $INSTANCE_DETAILS_FILE_LOCATION | sed s/__IMAGE_ID__/$IMAGE_ID/g)
echo "instance details"
echo $INSTANCE_DETAILS

PLACEMENT_CONFIG=$(sed s/__AD__/$AD/g $PLACEMENT_CONFIG_FILE_LOCATION | sed s/__SUBNET_ID__/$SUBNET_ID/g)
echo "placement config"
echo $PLACEMENT_CONFIG

INSTANCE_CONFIG_ID=""
CLUSTER_NETWORK_ID=""

echo "Creating instance config in compartment $COMPARTMENT_ID with launch details from $INSTANCE_DETAILS_FILE_LOCATION"
INSTANCE_CONFIG_ID=$(oci compute-management instance-configuration create --instance-details "$INSTANCE_DETAILS" --compartment-id $COMPARTMENT_ID --query 'data.id' --raw-output)
echo "Created instance config with id $INSTANCE_CONFIG_ID"

# we need the instance config ID in the create payload pool definition.
INSTANCE_POOL_DEF=$(sed s/__INSTANCE_CONFIG_ID__/$INSTANCE_CONFIG_ID/g $INSTANCE_POOLS_FILE_LOCATION)
echo "instance pool definition"
echo $INSTANCE_POOL_DEF

echo "Creating a cluster network based on instance config $INSTANCE_CONFIG_ID"
CLUSTER_NETWORK_ID=$(oci compute-management cluster-network create --compartment-id $COMPARTMENT_ID --instance-pools "$INSTANCE_POOL_DEF" --placement-configuration "$PLACEMENT_CONFIG" --wait-for-state RUNNING --query 'data.id' --raw-output)
echo "Created cluster network with id $CLUSTER_NETWORK_ID"

echo "Listing instances for cluster network $CLUSTER_NETWORK_ID"
oci compute-management cluster-network list-instances --compartment-id $COMPARTMENT_ID --cluster-network-id $CLUSTER_NETWORK_ID

echo "Terminating cluster network $CLUSTER_NETWORK_ID"
oci compute-management cluster-network terminate --cluster-network-id $CLUSTER_NETWORK_ID --force --wait-for-state TERMINATED

echo "Deleting instance config $INSTANCE_CONFIG_ID"
oci compute-management instance-configuration delete --instance-configuration-id $INSTANCE_CONFIG_ID --force
