#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the Service Gateway service's change compartment API in the CLI.
# Please set the following two env variables two variables before running the script:
#
#   * SRC_COMPARTMENT_ID: OCID of the source compartment where we'll create service gateway
#   * DEST_COMPARTMENT_ID: OCID of the destination compartment where the service gateway needs to be moved 
#
# The script will demonstrate:
#
#     * Change Service Gateway Compartment
#
# Following operations are performed for change compartment example :
# 1. Create VCN
# 2. Create Service Gateway
# 3. Change Service Gateway Compartment
# 4. Get Service Gateway to see the new compartment for the service gateway
# 5. Delete Service Gateway
# 6. Delete VCN

set -e 

function cleanup {
    # Delete service gateway
    if [[ -z "$SERVICE_GATEWAY_ID" ]]; then
        echo "Service Gateway not existing. Nothing to clean"
    else
        echo "Deleting Service Gateway"
        oci network service-gateway delete --service-gateway-id $SERVICE_GATEWAY_ID --force --wait-for-state TERMINATED
        echo "Deleted Service Gateway"
    fi

    # Delete VCN

    if [[ -z "$VCN_ID" ]]; then
        echo "VCN not existing. Nothing to clean"
    else
        echo "Deleting VCN"
        oci network vcn delete --vcn-id $VCN_ID --force --wait-for-state TERMINATED
        echo "Deleted VCN"
    fi
}
trap cleanup EXIT

if [[ -z "$SRC_COMPARTMENT_ID" ]]; then
    echo "SRC_COMPARTMENT_ID must be defined in your environment"
    exit 1
fi

if [[ -z "$DEST_COMPARTMENT_ID" ]]; then
    echo "SRC_COMPARTMENT_ID must be defined in your environment"
    exit 1
fi

# First we will create a VCN and a subnet. Since these resources have a lifecycle state, we can create them and use
# the --wait-for-state option so that our command will only return/complete when the resouce enters the desired
# state (in this case AVAILABLE)
echo "Create VCN"
VCN_ID=$(oci network vcn create -c $SRC_COMPARTMENT_ID --display-name createServiceGatewayExampleVcn --cidr-block 10.0.0.0/16 --wait-for-state AVAILABLE --query 'data.id' --raw-output 2>/dev/null)
echo "VCN OCID: ${VCN_ID}"

echo "Create Service Gateway"
# First we create a service gateway. A service gateway has a lifecycle state so we can use the --wait-for-state
# option so that our command will only return/complete when the nat gateway reaches the desired state.
# Note : for the purpose of this test, services field is passed empty. Please pass the right services' values to reach required Oracle Services
SERVICE_GATEWAY_ID=$(oci network service-gateway create -c $SRC_COMPARTMENT_ID --vcn-id $VCN_ID --services "[]" --display-name exampleServiceGateway --wait-for-state AVAILABLE --query data.id --raw-output 2>/dev/null)
echo "Service Gateway OCID: $SERVICE_GATEWAY_ID"
echo ""

# Change service gateway's compartment (service gateway id and target compartment id are mandatory arguments):
echo "Change service gateway compartment"
oci network service-gateway change-compartment --service-gateway-id $SERVICE_GATEWAY_ID -c $DEST_COMPARTMENT_ID 
echo ""

# Get service gateway call to see the new compartment id for service gateway
echo "Get service gateway after change service gateway call"
oci network service-gateway get --service-gateway-id $SERVICE_GATEWAY_ID 

cleanup

echo "Script Finished"
