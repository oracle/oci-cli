#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the WAAS Service in the Python SDK. This script accepts two
# will demonstrate:
#
#   * Creating, retrieving, listing and deleting policies 
#
# The following three variables must be populated at the top of this script:
#
#   * The compartment ID where policies will be created
#   * The domain that will be served by the WAF
#   * The origin that will receive traffic from the WAF
#
# Requirements for running this script:
#   - OCI CLI v2.4.19 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying of CLI output. This may be a useful utility in general and may help cater to scenarios
#     which can't be wholly addressed by the --query option in the CLI

set -e

COMPARTMENT_ID=${COMPARTMENT_ID:-""}
DOMAIN=${DOMAIN:-""}
ORIGIN=${ORIGIN:-""}

BORDER="=========================================="

function print_header() {
    echo $BORDER
    echo $1
    echo $BORDER
}

print_header "WAAS Policy Operations"

# Set up a policy. The operation creates a work request in the background. We grab the work request OCID so we can poll on it.
ORIGINS=$(printf '{"primary":{"uri":"%s","httpPort":80}}' $ORIGIN)
WORK_REQUEST_ID=$(oci waas waas-policy create -c $COMPARTMENT_ID --domain "$DOMAIN" --origins $ORIGINS --query '"opc-work-request-id"' --raw-output 2>/dev/null)
echo "Created WAAS policy, waiting on work request: $WORK_REQUEST_ID"

# Get the work request using its OCID and look it up as it will contain the OCID for the new policy.
POLICY_ID=$(oci waas work-request get --work-request-id $WORK_REQUEST_ID --query 'data.resources[0].identifier' --raw-output)
echo "Found WAAS policy from work request: $POLICY_ID"

echo "Waiting for WAAS policy to become active..."
oci waas waas-policy get --waas-policy-id $POLICY_ID

echo "Listing all WAAS policies"
oci waas waas-policy list -c $COMPARTMENT_ID --all

echo "Deleting WAAS policy: $POLICY_ID"
WORK_REQUEST_ID=$(oci waas waas-policy delete --waas-policy-id $POLICY_ID --force --query '"opc-work-request-id"' --raw-output 2>/dev/null)

oci waas work-request get --work-request-id $WORK_REQUEST_ID

echo "Success!"
