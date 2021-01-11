#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the Nat Gateway service in the CLI.
# The two variables at the beginning of the script must be specified accordingly:
#
#   * SRC_COMPARTMENT_ID: The OCID of the compartment where the NAT gateway and related resources will be created<
#   * DEST_COMPARTMENT_ID: The OCID of the compartment where the NAT gateway will be moved to
#
# The script will demonstrate:
#
#     * Creating a new nat gateway
#     * Changing the nat gateway's compartment
#
#
# Requirements for running this script:
#   - OCI CLI v2.5.10+preview.1 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying of CLI output. This may be a useful utility in general and may help cater to scenarios
#     which can't be wholly addressed by the --query option in the CLI

set -e

if [[ -z "$SRC_COMPARTMENT_ID" ]]; then
    echo "SRC_COMPARTMENT_ID must be defined in your environment"
    exit 1
fi

if [[ -z "$DEST_COMPARTMENT_ID" ]]; then
    echo "DEST_COMPARTMENT_ID must be defined in your environment"
    exit 1
fi

# First we will create a VCN. Since this resource has a lifecycle state, we can create it and use
# the --wait-for-state option so that our command will only return/complete when the resouce enters the desired
# state (in this case AVAILABLE)
VCN_ID=$(oci network vcn create -c $SRC_COMPARTMENT_ID --display-name createNatgwExampleVcn --cidr-block 10.0.0.0/16 --wait-for-state AVAILABLE --query 'data.id' --raw-output 2>/dev/null)
echo "VCN OCID: ${VCN_ID}"
echo ""

# Create a nat gateway. A nat gateway has a lifecycle state so we can use the --wait-for-state
# option so that our command will only return/complete when the nat gateway reaches the desired state.
echo "Creating NAT Gateway"
echo "========================="
NAT_GATEWAY_ID=$(oci network nat-gateway create -c $SRC_COMPARTMENT_ID --vcn-id $VCN_ID --display-name exampleNatGateway --wait-for-state AVAILABLE --query data.id --raw-output)
echo "Created NAT Gateway: "
oci network nat-gateway get --nat-gateway-id $NAT_GATEWAY_ID
echo ""

# We can update a nat gateway to block traffic through it
echo "Changing NAT gateway's compartment"
echo "========================="
oci network nat-gateway change-compartment --nat-gateway-id $NAT_GATEWAY_ID -c $DEST_COMPARTMENT_ID
echo "NAT Gateway's compartment has changed: "
oci network nat-gateway get --nat-gateway-id $NAT_GATEWAY_ID

# Now clean up resources. Since these resources have lifecycle states, we can use --wait-for-state so that the command
# In order to delete nat gateway, There must not be a route table that lists the NAT gateway as a target.
# only completes/returns when the resource has entered the DELETED (or equivalent) state

oci network nat-gateway delete --nat-gateway-id $NAT_GATEWAY_ID --force --wait-for-state TERMINATED
echo "Deleted Nat Gateway"

oci network vcn delete --vcn-id $VCN_ID --force --wait-for-state TERMINATED
echo "Deleted VCN"
echo ""

echo "Script Finished"