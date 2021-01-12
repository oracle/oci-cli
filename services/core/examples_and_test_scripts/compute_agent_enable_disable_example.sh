#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides an example of how to create an instance with the CLI and scale it up or down to a different shape
#
# Requirements for running this script:
#   - OCI CLI v2.4.40 or later (you can check this by running oci --version)
# The following environment variables must be populated before running the script: 
#       export COMPARTMENT_ID=	# <Your compartment id>
#       export SSH_AUTHORIZED_KEYS_FILE= # Your SSH public key to configure for access to the instances

set -e

ORIGINAL_INSTANCE_SHAPE='VM.Standard2.1'
INSTANCE_DISPLAY_NAME='AgentVmInstance'

INSTANCE_AGENT_CONFIG_ENABLE_MONITORING_MANAGEMENT='{"isMonitoringDisabled":false,"isManagementDisabled":false}'
INSTANCE_AGENT_CONFIG_DISABLE_MONITORING_MANAGEMENT='{"isMonitoringDisabled":true,"isManagementDisabled":true}'

# dynamically select image so it is for the correct region
ORACLE_LINUX_IMAGE_ID=$(oci compute image list -c $COMPARTMENT_ID --operating-system 'Oracle Linux' --operating-system-version '7.6' --shape $ORIGINAL_INSTANCE_SHAPE --query 'data[0].id' --raw-output)
AVAILABILITY_DOMAIN=$(oci iam availability-domain list -c $COMPARTMENT_ID --query 'data[0].name' --raw-output)

echo 'Creating VCN...'

VCN_ID=$(oci network vcn create -c $COMPARTMENT_ID --display-name scaleVMExampleVcn --cidr-block 10.0.0.0/16 --wait-for-state AVAILABLE --query 'data.id' --raw-output 2>/dev/null)
echo "VCN OCID: ${VCN_ID}"

echo 'Creating Subnet...'

SUBNET_ID=$(oci network subnet create -c $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN --display-name scaleVMSubnet --vcn-id $VCN_ID --cidr-block 10.0.0.0/24 --wait-for-state AVAILABLE --query 'data.id' --raw-output 2>/dev/null)
echo "Subnet OCID: $SUBNET_ID"

echo 'Launching instance...'
INSTANCE_ID=`oci compute instance launch \
    --image-id $ORACLE_LINUX_IMAGE_ID \
    --display-name $INSTANCE_DISPLAY_NAME \
    --availability-domain $AVAILABILITY_DOMAIN \
    --compartment-id $COMPARTMENT_ID \
    --shape $ORIGINAL_INSTANCE_SHAPE \
    --ssh-authorized-keys-file $SSH_AUTHORIZED_KEYS_FILE \
    --subnet-id $SUBNET_ID \
    --agent-config $INSTANCE_AGENT_CONFIG_ENABLE_MONITORING_MANAGEMENT \
    --assign-public-ip true \
    --wait-for-state RUNNING \
    --query 'data.id' \
    --raw-output`

echo "Instance id: $INSTANCE_ID"

INSTANCE_AGENT_CONFIG=`oci compute instance get --instance-id $INSTANCE_ID --query 'data."agent-config"'`

echo "Instance agent configuration after launch: $INSTANCE_AGENT_CONFIG"

oci compute instance update --agent-config $INSTANCE_AGENT_CONFIG_DISABLE_MONITORING_MANAGEMENT --instance-id $INSTANCE_ID --force

INSTANCE_AGENT_CONFIG=`oci compute instance get --instance-id $INSTANCE_ID --query 'data."agent-config"'`

echo "Instance agent configuration after update: $INSTANCE_AGENT_CONFIG"

# use --force to suppress confirmation prompt for deleting resource
oci compute instance terminate \
    --instance-id $INSTANCE_ID \
    --wait-for-state TERMINATED \
    --force
echo "Completed instance termination: $INSTANCE_ID"

# delete the subnets
oci network subnet delete --subnet-id $SUBNET_ID --wait-for-state TERMINATED --force
echo "Completed subnet termination: $SUBNET_ID"

# delete the VCN
oci network vcn delete --vcn-id $VCN_ID --wait-for-state TERMINATED --force
echo "Completed VCN termination: $VCN_ID"

echo 'Success!'
