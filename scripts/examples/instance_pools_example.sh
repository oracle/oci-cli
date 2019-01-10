#!/usr/bin/env bash
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.
# This script provides an example of how use the instance pools CLI in terms of:
#   - Creating an instance config to be used for pool
#   - Creating an instance pool
#   - Listing instance pools
#   - Stopping instance pool
#   - Terminating instance pool
#
# For more help with specific instance pool commands with, see:
#   oci compute-management instance-pool -h
#
# Requirements for running this script:
#   - OCI CLI v2.4.33 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI

set -e 

COMPARTMENT_ID=""  # Your compartment OCID
AD="" # the AD where the pool will be spun up (the pool in this example only spans a single AD)
SUBNET_ID="" # the subnet ocid in the AD above
IMAGE_ID="" # the image ID to use for instances

INSTANCE_DETAILS_FILE_LOCATION="./instance_pools_example/instance_details_template.json"
PLACEMENT_CONFIG_FILE_LOCATION="./instance_pools_example/placement_details_template.json"

INSTANCE_DETAILS=$(sed s/__COMPARTMENT_ID__/$COMPARTMENT_ID/g $INSTANCE_DETAILS_FILE_LOCATION | sed s/__IMAGE_ID__/$IMAGE_ID/g)
echo "instance details"
echo $INSTANCE_DETAILS

PLACEMENT_CONFIG=$(sed s/__AD__/$AD/g $PLACEMENT_CONFIG_FILE_LOCATION | sed s/__SUBNET_ID__/$SUBNET_ID/g)
echo "placement config"
echo $PLACEMENT_CONFIG

INSTANCE_CONFIG_ID=""
INSTANCE_POOL_ID=""

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
oci compute-management instance-pool list-instances --instance-pool-id $INSTANCE_POOL_ID

echo "Setting the instance pool $INSTANCE_POOL_ID size to 2 "
oci compute-management instance-pool update --instance-pool-id $INSTANCE_POOL_ID --size 2

# adding some sleep here just so you can see the instances spinning up
sleep 2m

echo "Terminating instance pool $INSTANCE_POOL_ID"
oci compute-management instance-pool terminate --instance-pool-id $INSTANCE_POOL_ID --force --wait-for-state TERMINATED

echo "Deleting instance config $INSTANCE_CONFIG_ID"
oci compute-management instance-configuration delete --instance-configuration-id INSTANCE_CONFIG_ID --force
