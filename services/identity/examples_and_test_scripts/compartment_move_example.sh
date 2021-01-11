#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides an example of how to move a compartment to another compartment
# This script will create two compartments under tenancy and move one under another
# Alternatively, you can perform move with your existing compartments
#
#   WARNING: Compartments currently does not support hard delete. Once you created the compartments with the script, you cannot hard delete them.
#   WARNING: Compartments supported operations can be found https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/Compartment/.
#
# Please provide values for the following env variable:
#   - TENANCY_ID

# script to exit on first error
set -e

if [[ -z "$TENANCY_ID" ]];then
    echo "TENANCY_ID must be defined in the environment. "
    exit 1
fi

# Create compartment cp_source_CLI
echo "Creating Compartment cp_source_CLI"
CP_SOURCE=$(oci iam compartment create --compartment-id $TENANCY_ID --name cp_source_CLI --description "cp_source_CLI")
CP_SOURCE_ID=$(jq -r '.data.id' <<< "$CP_SOURCE")
echo "cp_source_CLI OCID: ${CP_SOURCE_ID}"

# Create compartment cp_target_CLI
echo "Creating Compartment cp_target_CLI"
CP_TARGET=$(oci iam compartment create --compartment-id $TENANCY_ID --name cp_target_CLI --description "cp_target_CLI")
CP_TARGET_ID=$(jq -r '.data.id' <<< "$CP_TARGET")
echo "cp_target_CLI OCID: ${CP_TARGET_ID}"

echo "moving cp_source_CLI under cp_target_CLI"
oci iam compartment move --compartment-id $CP_SOURCE_ID --target-compartment-id $CP_TARGET_ID

echo "compartment moved successfully"
