#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# -----------------------------------------
#
# This script provides an example of how use the Virtual Network API to
# create a Service Gateway
#
# Requirements for running this script:
# -----------------------------------------
# 1.  OCI CLI v2.5.9 or later (you can check this by running oci --version)
# 2. The following Environment variables must be set:
#   COMPARTMENT_ID - The compartment ID to use
#   VCN_ID - The VCN on which the ServiceGateway will be created
#   ROUTE_TABLE_ID - The Route Table assigned to the ServiceGateway

DISPLAY_NAME='pythonCliExampleServiceGateway'

function cleanup {
    if [[ -z "$SERVICE_GATEWAY_ID" ]]; then
        echo "Service Gateway not existing. Nothing to clean"
    else
        echo "Deleting Service Gateway..."
        oci network service-gateway delete --service-gateway-id $SERVICE_GATEWAY_ID --force --wait-for-state TERMINATED
    fi
}
trap cleanup EXIT

if [[ -z "$COMPARTMENT_ID" ]]; then
    echo "COMPARTMENT_ID must be defined in your environment"
    exit 1
fi

if [[ -z "$VCN_ID" ]]; then
    echo "VCN_ID must be defined in your environment"
    exit 1
fi

if [[ -z "$ROUTE_TABLE_ID" ]]; then
    echo "ROUTE_TABLE_ID must be defined in your environment"
    exit 1
fi

echo "Create Service Gateway..."
# A service gateway has a lifecycle state so we can use the --wait-for-state option
# so that our command will only return/complete when the nat gateway reaches the desired state.
# Note : for the purpose of this example, services field is passed empty. Pass service values to reach required Oracle Services.
SERVICE_GATEWAY_ID=$(oci network service-gateway create -c $COMPARTMENT_ID \
    --vcn-id $VCN_ID \
    --services "[]" \
    --display-name $DISPLAY_NAME \
    --wait-for-state AVAILABLE \
    --query data.id \
    --route-table-id $ROUTE_TABLE_ID)

echo "List Service Gateways..."
oci network service-gateway list --compartment-id $COMPARTMENT_ID

echo "Update Service Gateway..."
oci network service-gateway update --service-gateway-id $SERVICE_GATEWAY_ID --display-name "$DISPLAY_NAME-UPDATED"

echo "Get Service Gateway..."
oci network service-gateway get --service-gateway-id $SERVICE_GATEWAY_ID

cleanup

echo "Script Finished"
