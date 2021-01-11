#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides an example of how to create an instance with the CLI and scale it up or down to a different shape
#
# Requirements for running this script:
#   - OCI CLI v2.4.14 or later (you can check this by running oci --version)

COMPARTMENT_ID=""  # Your compartment OCID
SSH_AUTHORIZED_KEYS_FILE=~/.ssh/id_rsa.pub  # Your SSH public key to configure for access to the instances

ORIGINAL_INSTANCE_SHAPE='VM.Standard1.1'
SCALED_INSTANCE_SHAPE='VM.Standard1.4'
ORIGINAL_INSTANCE_DISPLAY_NAME='ScaleVMTest_OriginalInstance'
SCALED_INSTANCE_DISPLAY_NAME='ScaleVMTest_ScaledInstance'

# dynamically select image so it is for the correct region
ORACLE_LINUX_IMAGE_ID=$(oci compute image list -c $COMPARTMENT_ID --operating-system 'Oracle Linux' --operating-system-version '7.4' --shape $ORIGINAL_INSTANCE_SHAPE --query 'data[0].id' --raw-output)
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
    --display-name $ORIGINAL_INSTANCE_DISPLAY_NAME \
    --availability-domain $AVAILABILITY_DOMAIN \
    --compartment-id $COMPARTMENT_ID \
    --shape $ORIGINAL_INSTANCE_SHAPE \
    --ssh-authorized-keys-file $SSH_AUTHORIZED_KEYS_FILE \
    --subnet-id $SUBNET_ID \
    --assign-public-ip true \
    --wait-for-state RUNNING \
    --query 'data.id' \
    --raw-output`

# find the boot volume ID for the boot volume attached to the instance
BOOT_VOLUME_ID=`oci compute boot-volume-attachment list \
    --availability-domain $AVAILABILITY_DOMAIN \
    --compartment-id $COMPARTMENT_ID \
    --query 'data[?"instance-id" == \`'$INSTANCE_ID'\`] | [0]."boot-volume-id"' \
    --raw-output`

echo "Boot Volume ID: $BOOT_VOLUME_ID"

# terminate instance but preserve boot volume
# use --force to suppress confirmation prompt for deleting resource
oci compute instance terminate \
    --instance-id $INSTANCE_ID \
    --preserve-boot-volume true \
    --wait-for-state TERMINATED \
    --force

# launch a new instance using the original boot volume
SCALED_INSTANCE_ID=`oci compute instance launch \
    --display-name $SCALED_INSTANCE_DISPLAY_NAME \
    --availability-domain $AVAILABILITY_DOMAIN \
    --compartment-id $COMPARTMENT_ID \
    --shape $SCALED_INSTANCE_SHAPE \
    --ssh-authorized-keys-file $SSH_AUTHORIZED_KEYS_FILE \
    --source-boot-volume-id $BOOT_VOLUME_ID \
    --subnet-id $SUBNET_ID \
    --assign-public-ip true \
    --wait-for-state RUNNING \
    --query 'data.id' \
    --raw-output`

echo "Scaled instance ID: $SCALED_INSTANCE_ID"

# terminate the instance
oci compute instance terminate --instance-id $SCALED_INSTANCE_ID --wait-for-state TERMINATED --force

# delete the subnets
oci network subnet delete --subnet-id $SUBNET_ID --wait-for-state TERMINATED --force

# delete the VCN
oci network vcn delete --vcn-id $VCN_ID --wait-for-state TERMINATED --force

echo 'Success!'