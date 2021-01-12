#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the File Storage service in the CLI.
# The three variables at the beginning of the script must be specified accordingly:
#
#   * COMPARTMENT_ID: The OCID of the compartment where we'll create our file system and related resources
#   * AVAILABILITY_DOMAIN: The availability domain, e.g. Uocm:PHX-AD-1, where we'll create our file system and related resources
#   * DEFINED_TAGS: The defined tag namespace/key
#
# The script will demonstrate:
#
#     * Creating a new file system
#     * Creating a mount target via which the file system can be accessed. The mount target and file system must
#       be in the same availability domain in order to export the file system from the mount target
#     * Creating an export so that we can mount the file system (see
#       https://docs.cloud.oracle.com/Content/File/Tasks/mountingfilesystems.htm for more information)
#     * Creating a snapshot of the file system
#
# In order to demonstrate functionality for mount targets and export sets, this script will also create a VCN
# and subnet. These will be deleted at the end of the script.
#
# Requirements for running this script:
#   - OCI CLI v2.4.17 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying of CLI output. This may be a useful utility in general and may help cater to scenarios
#     which can't be wholly addressed by the --query option in the CLI

set -e

COMPARTMENT_ID=""
AVAILABILITY_DOMAIN=""
DEFINED_TAGS='{"": {"": "value"}}'
FREEFORM_TAGS='{"foo": "value"}'

# First we will create a VCN and a subnet. Since these resources have a lifecycle state, we can create them and use
# the --wait-for-state option so that our command will only return/complete when the resouce enters the desired
# state (in this case AVAILABLE)
CREATED_VCN=$(oci network vcn create -c $COMPARTMENT_ID --display-name createFsExampleVcn --cidr-block 10.0.0.0/16 --dns-label createFsExample --wait-for-state AVAILABLE 2>/dev/null)
VCN_ID=$(jq -r '.data.id' <<< "$CREATED_VCN")
echo "VCN OCID: ${VCN_ID}"

CREATED_SUBNET=$(oci network subnet create -c $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN --display-name createFsSubnet --vcn-id $VCN_ID --dns-label subnetFs --cidr-block 10.0.0.0/24 --wait-for-state AVAILABLE 2>/dev/null)
SUBNET_ID=$(jq -r '.data.id' <<< "$CREATED_SUBNET")
echo "Subnet OCID: $SUBNET_ID"
echo ""

# First we create a file system. A file system has a lifecycle state so we can use the --wait-for-state
# option so that our command will only return/complete when the file system reaches the desired state.
CREATED_FILE_SYSTEM=$(oci fs file-system create -c $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN --display-name exampleFileSystem --freeform-tags "$FREEFORM_TAGS" --defined-tags "$DEFINED_TAGS" --wait-for-state ACTIVE)
FILE_SYSTEM_ID=$(jq -r '.data.id' <<< "$CREATED_FILE_SYSTEM")
echo "File System OCID: $FILE_SYSTEM_ID"
echo ""

# We can list file systems. This is a paginated call and we can use the --all option to get
# all results rather than having to manually deal with page tokens
echo "Listing all file systems"
echo "========================="
oci fs file-system list -c $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN --all
echo ""

# We can retrieve the file system
echo "Retrieve file system"
echo "========================="
oci fs file-system get --file-system-id $FILE_SYSTEM_ID
echo ""

# Here we create a mount target. A couple of things to note:
#
#   - If we don't specify a --hostname for the mount target then it can only be accessed via its private IP address
#   - If we don't specify an --ip-address then one will be assigned from the free private IPs in the subnet
#   - A mount target has a lifecycle state, so we can use --wait-for-state so that the command will only return/complete when the
#     mount target reaches the desired state
CREATED_MOUNT_TARGET=$(oci fs mount-target create -c $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN --subnet-id $SUBNET_ID --display-name exampleMountTarget --freeform-tags "$FREEFORM_TAGS" --defined-tags "$DEFINED_TAGS" --wait-for-state ACTIVE)
MOUNT_TARGET_ID=$(jq -r '.data.id' <<< "$CREATED_MOUNT_TARGET")
echo "Mount Target OCID: $FILE_SYSTEM_ID"
echo ""

# We can list file systems. This is a paginated call and we can use the --all option to get
# all results rather than having to manually deal with page tokens
echo "Listing all mount targets"
echo "========================="
oci fs mount-target list -c $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN --all
echo ""

# We can retrieve the mount target
echo "Retrieve mount target"
echo "========================="
oci fs mount-target get --mount-target-id $MOUNT_TARGET_ID
echo ""

# If we want to find the IP address via which a mount target can be accessed then we need to pull the private
# IP OCIDs (this is an array) from the mount target and then retrieve the information about the private IP by its
# OCID
PRIVATE_IP_ID=$(oci fs mount-target get --mount-target-id $MOUNT_TARGET_ID | jq -r '.data."private-ip-ids"[0]')
echo "Private IP OCID: $PRIVATE_IP_ID"
PRIVATE_IP=$(oci network private-ip get --private-ip-id $PRIVATE_IP_ID | jq -r '.data."ip-address"')
echo "Private IP Address: $PRIVATE_IP"
echo ""

# A mount target contains an export set, which we can use to link the mount target to the file system. We do this
# by creating an export that links the export set and the file system. Once we have an export, we can access the
# file system via the mount target and the file system can be mounted on, say, a compute instance.
#
# For more information on mounting file systems see:
# https://docs.cloud.oracle.com/Content/File/Tasks/mountingfilesystems.htm
EXPORT_SET_ID=$(jq -r '.data."export-set-id"' <<< "$CREATED_MOUNT_TARGET")
CREATED_EXPORT=$(oci fs export create --file-system-id $FILE_SYSTEM_ID --export-set-id $EXPORT_SET_ID --wait-for-state ACTIVE --path /files)
EXPORT_ID=$(jq -r '.data.id' <<< "$CREATED_EXPORT")
echo "Export OCID: $EXPORT_ID"
echo ""

# We can list exports. This operation also takes optional filters so we can narrow this list down by file system
# or export set (mount target).
echo "Listing Exports By File System"
echo "==============================="
oci fs export list -c $COMPARTMENT_ID --file-system-id $FILE_SYSTEM_ID --all
echo ""

echo "Listing Exports By Export Set"
echo "==============================="
oci fs export list -c $COMPARTMENT_ID --export-set-id $EXPORT_SET_ID --all
echo ""

# We can also view information on the export set itself
echo "Export Set Info"
echo "================="
oci fs export-set get --export-set-id $EXPORT_SET_ID
echo ""

# We can create a point-in-time snapshot of a file system. Snapshots also have a lifecycle state, so we can wait on it
# to become available
#
# Note that snapshot names are immutable and must be unique amongst all non-DELETED snapshots for a file system.
CREATED_SNAPSHOT=$(oci fs snapshot create --file-system-id $FILE_SYSTEM_ID --name exampleSnapshot --freeform-tags "$FREEFORM_TAGS" --defined-tags "$DEFINED_TAGS" --wait-for-state ACTIVE)
SNAPSHOT_ID=$(jq -r '.data.id' <<< "$CREATED_SNAPSHOT")
echo "Snapshot OCID: $SNAPSHOT_ID"
echo ""

# We can list all snapshots in a file system
echo "Listing Snapshots By File System"
echo "================================="
oci fs snapshot list --file-system-id $FILE_SYSTEM_ID --all
echo ""

# Now clean up resources. Since these resources have lifecycle states, we can use --wait-for-state so that the command
# only completes/returns when the resource has entered the DELETED (or equivalent) state
oci fs snapshot delete --snapshot-id $SNAPSHOT_ID --force --wait-for-state DELETED
echo "Deleted Snapshot"

oci fs export delete --export-id $EXPORT_ID --force --wait-for-state DELETED
echo "Deleted Export"

oci fs mount-target delete --mount-target-id $MOUNT_TARGET_ID --force --wait-for-state DELETED
echo "Deleted Mount Target"

oci fs file-system delete --file-system-id $FILE_SYSTEM_ID --force --wait-for-state DELETED
echo "Deleted File System"

# Sometimes we can't delete the subnet straight after a mount target has been deleted as network resources
# still need to clear. To account for this in our script, put in a sleep
echo "Sleep for 60 seconds after mount target deletion before trying to delete the subnet"
sleep 60

oci network subnet delete --subnet-id $SUBNET_ID --force --wait-for-state TERMINATED
echo "Deleted Subnet"

oci network vcn delete --vcn-id $VCN_ID --force --wait-for-state TERMINATED
echo "Deleted VCN"
echo ""

echo "Script Finished"
