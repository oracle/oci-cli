#!/usr/bin/env bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides an example of how use the autoscaling CLI in terms of:
#   - Creating an instance config to be used for pool
#   - Creating an instance pool
#   - Creating an AutoScalingConfiguration for that pool
#   - Listing autoscaling configurations
#   - Deleting autoscaling configuration
#   - Terminating instance pool
#   - Deleting instance configuration
#
# For more help with specific autoscaling commands, see:
#   oci autoscaling configuration -h
#
# For more help with specific instance pools commands, see:
#   oci compute-management instance-pool -h
#
# Requirements for running this script:
#   - OCI CLI v2.4.41 or later (you can check this by running oci --version)
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

if [ -d ./services/autoscaling/examples_and_test_scripts/instance_pools_example ];then
    instance_pools_example_data="./services/autoscaling/examples_and_test_scripts/instance_pools_example"
elif [ -d ./instance_pools_example ];then
    instance_pools_example_data="./instance_pools_example"
else
    echo "Could not find instance_pools_example data files"
    exit 1
fi
if [ -d ./services/autoscaling/examples_and_test_scripts/autoscaling_example ];then
    autoscaling_example_data="./services/autoscaling/examples_and_test_scripts/autoscaling_example"
elif [ -d ./instance_pools_example ];then
    autoscaling_example_data="./autoscaling_example"
else
    echo "Could not find autoscaling_example data files"
    exit 1
fi
INSTANCE_DETAILS_FILE_LOCATION="${instance_pools_example_data}/instance_details_template.json"
PLACEMENT_CONFIG_FILE_LOCATION="${instance_pools_example_data}/placement_details_template.json"
RESOURCE_DETAILS_FILE_LOCATION="${autoscaling_example_data}/resource.json"

INSTANCE_DETAILS=$(sed s/__COMPARTMENT_ID__/$COMPARTMENT_ID/g $INSTANCE_DETAILS_FILE_LOCATION | sed s/__IMAGE_ID__/$IMAGE_ID/g)
echo "instance details"
echo $INSTANCE_DETAILS

PLACEMENT_CONFIG=$(sed s/__AD__/$AD/g $PLACEMENT_CONFIG_FILE_LOCATION | sed s/__SUBNET_ID__/$SUBNET_ID/g)
echo "placement config"
echo $PLACEMENT_CONFIG

INSTANCE_CONFIG_ID=""
INSTANCE_POOL_ID=""

echo "Creating instance config in compartment $COMPARTMENT_ID with launch details from $INSTANCE_DETAILS_FILE_LOCATION"
oci compute-management instance-configuration create --instance-details "$INSTANCE_DETAILS" --compartment-id $COMPARTMENT_ID --query 'data.id' --raw-output
INSTANCE_CONFIG_ID=$(oci compute-management instance-configuration create --instance-details "$INSTANCE_DETAILS" --compartment-id $COMPARTMENT_ID --query 'data.id' --raw-output)
echo "Created instance config with id $INSTANCE_CONFIG_ID"

# this demonstrates how to get the details of a created instance config
echo "Getting instance config details for id $INSTANCE_CONFIG_ID"
oci compute-management instance-configuration get --instance-configuration-id $INSTANCE_CONFIG_ID

echo "Creating an instance pool based on instance config $INSTANCE_CONFIG_ID"
INSTANCE_POOL_ID=$(oci compute-management instance-pool create --compartment-id $COMPARTMENT_ID --instance-configuration-id $INSTANCE_CONFIG_ID --placement-configurations "$PLACEMENT_CONFIG" --size 1 --wait-for-state RUNNING --query 'data.id' --raw-output)
echo "Created instance pool with id $INSTANCE_POOL_ID"

RESOURCE_INPUT=$(sed s/__INSTANCE_POOL_ID__/$INSTANCE_POOL_ID/g $RESOURCE_DETAILS_FILE_LOCATION)

echo "Creating an autoscaling configuration for the previously created pool with id $INSTANCE_POOL_ID"
ASC_CONFIG_ID=$(oci autoscaling configuration create --compartment-id $COMPARTMENT_ID --policies file://${autoscaling_example_data}/policies.json --resource "$RESOURCE_INPUT" --query 'data.id' --raw-output)

echo "Pausing for 2 minutes to let the pool scal to initial size defined in the autoscaling configuration"
sleep 2m

echo "Deleting the auto scaling configuration $ASC_CONFIG_ID"
oci autoscaling configuration delete --auto-scaling-configuration-id $ASC_CONFIG_ID --force

echo "Terminating instance pool $INSTANCE_POOL_ID"
oci compute-management instance-pool terminate --instance-pool-id $INSTANCE_POOL_ID --force --wait-for-state TERMINATED

echo "Deleting instance config $INSTANCE_CONFIG_ID"
oci compute-management instance-configuration delete --instance-configuration-id INSTANCE_CONFIG_ID --force

echo "SUCCESS"