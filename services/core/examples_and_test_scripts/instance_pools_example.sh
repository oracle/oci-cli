#!/usr/bin/env bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides an example of how use the instance pools CLI in terms of:
#   - Creating an instance config to be used for pool
#   - Creating an instance pool
#   - Listing instance pool instances
#   - Attaching a load balancer to the pool
#   - Updating instance pool size
#   - Getting the LB attachment info
#   - Terminating instance pool
#
# For more help with specific instance pool commands with, see:
#   oci compute-management instance-pool -h
#
# Requirements for running this script:
#   - OCI CLI v2.4.33 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI
# Environment variables need to be set:
#   - COMPARTMENT_ID - Your compartment OCID
#   - AD - the AD where the pool will be spun up (the pool in this example only spans a single AD)
#   - SUBNET_ID - the subnet ocid in the AD above
#   - IMAGE_ID - the image ID to use for instances
#   - LOAD_BALANCER_ID - The load balancer ID to use for the pool.
#   - BACKEND_SET_NAME - The backendset name in the load balancer that is being attached.
#   - ANOTHER_COMPARTMENT_ID - Another compartment OCID to move the pool into

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

if [[ -z "$LOAD_BALANCER_ID" ]]; then
    echo "LOAD_BALANCER_ID must be defined in your environment"
    exit 1
fi

if [[ -z "$BACKEND_SET_NAME" ]]; then
    echo "BACKEND_SET_NAME must be defined in your environment"
    exit 1
fi

if [[ -z "$ANOTHER_COMPARTMENT_ID" ]]; then
    echo "ANOTHER_COMPARTMENT_ID must be defined in your environment"
    exit 1
fi

if [ -d ./services/core/examples_and_test_scripts/instance_pools_example ];then
    instance_configs_example_data="./services/core/examples_and_test_scripts/instance_pools_example"
elif [ -d ./instance_pools_example ];then
    instance_configs_example_data="./instance_pools_example"
else
    echo "Could not find instance_pools_example data files"
    exit 1
fi


INSTANCE_DETAILS_FILE_LOCATION="${instance_configs_example_data}/instance_details_template.json"
PLACEMENT_CONFIG_FILE_LOCATION="${instance_configs_example_data}/placement_details_template.json"

INSTANCE_DETAILS=$(sed s/__COMPARTMENT_ID__/$COMPARTMENT_ID/g $INSTANCE_DETAILS_FILE_LOCATION | sed s/__IMAGE_ID__/$IMAGE_ID/g)
echo "instance details"
echo $INSTANCE_DETAILS

PLACEMENT_CONFIG=$(sed s/__AD__/$AD/g $PLACEMENT_CONFIG_FILE_LOCATION | sed s/__SUBNET_ID__/$SUBNET_ID/g)
echo "placement config"
echo $PLACEMENT_CONFIG

INSTANCE_CONFIG_ID=""
INSTANCE_POOL_ID=""
LB_ATTACHMENT_ID=""

echo "Creating instance config in compartment $COMPARTMENT_ID with launch details from $INSTANCE_DETAILS_FILE_LOCATION"
INSTANCE_CONFIG_ID=$(oci compute-management instance-configuration create --instance-details "$INSTANCE_DETAILS" --compartment-id $COMPARTMENT_ID --query 'data.id' --raw-output)
echo "Created instance config with id $INSTANCE_CONFIG_ID"

# this demonstrates how to get the details of a created instance config
echo "Getting instance config details for id $INSTANCE_CONFIG_ID"
oci compute-management instance-configuration get --instance-configuration-id $INSTANCE_CONFIG_ID

echo "Creating an instance pool based on instance config $INSTANCE_CONFIG_ID"
INSTANCE_POOL_ID=$(oci compute-management instance-pool create --compartment-id $COMPARTMENT_ID --instance-configuration-id $INSTANCE_CONFIG_ID --placement-configurations "$PLACEMENT_CONFIG" --size 1 --wait-for-state RUNNING --query 'data.id' --raw-output)
echo "Created instance pool with id $INSTANCE_POOL_ID"

echo "Listing instance pool instances for pool $INSTANCE_POOL_ID"
oci compute-management instance-pool list-instances --compartment-id $COMPARTMENT_ID --instance-pool-id $INSTANCE_POOL_ID

echo "Attaching load balancer to instance pool $INSTANCE_POOL_ID"
oci compute-management instance-pool attach-lb --instance-pool-id "$INSTANCE_POOL_ID" --load-balancer-id $LOAD_BALANCER_ID --backend-set-name $BACKEND_SET_NAME --port 80 --vnic-selection PrimaryVnic
echo "Attach in progress."

echo "Setting the instance pool $INSTANCE_POOL_ID size to 2 "
oci compute-management instance-pool update --instance-pool-id $INSTANCE_POOL_ID --size 2

# adding some sleep here just so you can see the instances spinning up
sleep 2m

echo "Getting the lb attachment id from pool info"
LB_ATTACHMENT_ID=$(oci compute-management instance-pool get --instance-pool-id $INSTANCE_POOL_ID --query 'data."load-balancers"[0].id' --raw-output)

echo 'Getting the lb attachment info'
oci compute-management instance-pool lb-attachment get --instance-pool-id $INSTANCE_POOL_ID --lb-attachment-id $LB_ATTACHMENT_ID

echo "Moving the instance pool resource into compartment $ANOTHER_COMPARTMENT_ID"
oci compute-management instance-pool change-compartment --instance-pool-id $INSTANCE_POOL_ID --compartment-id $ANOTHER_COMPARTMENT_ID

echo "Terminating instance pool $INSTANCE_POOL_ID"
oci compute-management instance-pool terminate --instance-pool-id $INSTANCE_POOL_ID --force --wait-for-state TERMINATED

echo "Deleting instance config $INSTANCE_CONFIG_ID"
oci compute-management instance-configuration delete --instance-configuration-id $INSTANCE_CONFIG_ID --force
