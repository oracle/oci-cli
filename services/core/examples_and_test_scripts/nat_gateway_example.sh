#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the Nat Gateway service in the CLI.
# The two variables at the beginning of the script must be specified accordingly:
#
#   * COMPARTMENT_ID: The OCID of the compartment where we'll create our file system and related resources
#
# The script will demonstrate:
#
#     * Creating a new nat gateway
#     * Getting a nat gateway
#     * Updating a nat gateway
#     * Deleting a nat gateway
#
#
# Requirements for running this script:
#   - OCI CLI v2.4.34 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying of CLI output. This may be a useful utility in general and may help cater to scenarios
#     which can't be wholly addressed by the --query option in the CLI

set -e

COMPARTMENT_ID=""

# First we will create a VCN and a subnet. Since these resources have a lifecycle state, we can create them and use
# the --wait-for-state option so that our command will only return/complete when the resouce enters the desired
# state (in this case AVAILABLE)
VCN_ID=$(oci network vcn create -c $COMPARTMENT_ID --display-name createNatgwExampleVcn --cidr-block 10.0.0.0/16 --wait-for-state AVAILABLE --query 'data.id' --raw-output 2>/dev/null)
echo "VCN OCID: ${VCN_ID}"

echo
# First we create a nat gateway. A nat gateway has a lifecycle state so we can use the --wait-for-state
# option so that our command will only return/complete when the nat gateway reaches the desired state.
NAT_GATEWAY_ID=$(oci network nat-gateway create -c $COMPARTMENT_ID --vcn-id $VCN_ID --display-name exampleNatGateway --wait-for-state AVAILABLE --query data.id --raw-output)
echo "Nat Gateway OCID: $NAT_GATEWAY_ID"
echo ""

# Update routing for the subnet by creating a route table with a route rule that directs internet-bound traffic to the Nat Gateway
# Create route table and wait for it to become available 
ROUTE_RULE='[{"cidrBlock":"0.0.0.0/0","networkEntityId":"'${NAT_GATEWAY_ID}'"}]'
echo "Create route table and add Nat Gateway rule"
echo "========================="
ROUTE_TABLE_ID=$(oci network route-table create -c $COMPARTMENT_ID --route-rules $ROUTE_RULE --vcn-id $VCN_ID --wait-for-state AVAILABLE --query data.id --raw-output)
echo "Route Table OCID: $ROUTE_TABLE_ID"
echo ""

# We can show the route table directed to the nat gateway
echo "Get route table"
echo "========================="
oci network route-table get --rt-id $ROUTE_TABLE_ID
echo ""

# We can list all nat gateways in a compartment. This is a paginated call and we can use the --all option to get
# all results rather than having to manually deal with page tokens
echo "Listing all nat gateways"
echo "========================="
oci network nat-gateway list -c $COMPARTMENT_ID --all
echo ""

# We can get a specific nat gateway
echo "Get nat gateway"
echo "========================="
oci network nat-gateway get --nat-gateway-id $NAT_GATEWAY_ID
echo ""

# We can update a nat gateway to block traffic through it
echo "Update nat gateway"
echo "========================="
oci network nat-gateway update --nat-gateway-id $NAT_GATEWAY_ID --block-traffic true
echo ""

# Now clean up resources. Since these resources have lifecycle states, we can use --wait-for-state so that the command
# In order to delete nat gateway, There must not be a route table that lists the NAT gateway as a target.
# only completes/returns when the resource has entered the DELETED (or equivalent) state
oci network route-table delete --rt-id $ROUTE_TABLE_ID --force --wait-for-state TERMINATED
echo "Deleted Route Table"

oci network nat-gateway delete --nat-gateway-id $NAT_GATEWAY_ID --force --wait-for-state TERMINATED
echo "Deleted Nat Gateway"

oci network vcn delete --vcn-id $VCN_ID --force --wait-for-state TERMINATED
echo "Deleted VCN"
echo ""

echo "Script Finished"
