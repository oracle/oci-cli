#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides an example of how to use compartments in the CLI in terms of:
#
#   - Managing compartments by performing create, read (get/list) operations on them.
#
#   WARNING: Compartments currently does not supporting the hard delete. Once you created the compartments with the script, you cannot hard delete them.
#   WARNING: Compartments supported operations can be found https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/Compartment/.
#
# Requirements for running this script:
#   - OCI CLI v2.4.35 or later (you can check this by running oci --version).
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI.

TENANCY_ID=""  # Your tenancy ID

# script to exit on first error
set -e

##########################################################
# Setup the compartments like the following tree
# Here is the compartment Tree in this Test
# Tenancy
#     |
#     --- CP-1
#     |
#     |
#     --- CP-2
#     |    |
#     |    --- CP-21
#     |         |
#     |         --- CP-211
#     |
#     --- CP-3
#         |
#         --- CP-31
##########################################################

echo "WARNING: Compartments currently does not supporting the hard delete.Once you created the compartments with the script, you cannot hard delete them"
echo "WARNING: Compartments supported operations can be found https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/Compartment/"

# Create first level of compartments (CP1, CP2, CP3)
echo "Creating Compartment CP1"
CREATED_COMPARTMENT=$(oci iam compartment create --compartment-id $TENANCY_ID --name CP-1 --description "CP1")
COMPARTMENT_CP1_ID=$(jq -r '.data.id' <<< "$CREATED_COMPARTMENT")
echo "Compartment-CP1 OCID: ${COMPARTMENT_CP1_ID}"

echo "Creating Compartment CP2"
CREATED_COMPARTMENT=$(oci iam compartment create --compartment-id $TENANCY_ID --name CP-2 --description "CP2")
COMPARTMENT_CP2_ID=$(jq -r '.data.id' <<< "$CREATED_COMPARTMENT")
echo "Compartment-CP2 OCID: ${COMPARTMENT_CP2_ID}"

echo "Creating Compartment CP3"
CREATED_COMPARTMENT=$(oci iam compartment create --compartment-id $TENANCY_ID --name CP-3 --description "CP3")
COMPARTMENT_CP3_ID=$(jq -r '.data.id' <<< "$CREATED_COMPARTMENT")
echo "Compartment-CP3 OCID: ${COMPARTMENT_CP3_ID}"

# List first level compartments under tenancy
echo "List Compartments under Tenancy"
LIST_COMPARTMENTS=$(oci iam compartment list --compartment-id $TENANCY_ID)

echo "List Compartments under Tenancy with accessibleLevel == accessible"
LIST_COMPARTMENTS=$(oci iam compartment list --compartment-id $TENANCY_ID --access-level accessible)


# If we create/update and then try to use compartments straight away, sometimes we can get a 404. To try and avoid this, the script
# adds a short delay between the compartment management operations.
# Also sleep is not needed but kept as a safety measure for worst case for data plane sync with control plan changes.
sleep 10

# Create second level of compartments (CP21, CP31)
echo "Creating Compartment CP21 under CP2"
CREATED_COMPARTMENT=$(oci iam compartment create --compartment-id $COMPARTMENT_CP2_ID --name CP-21 --description "CP21")
COMPARTMENT_CP21_ID=$(jq -r '.data.id' <<< "$CREATED_COMPARTMENT")
echo "Compartment-CP21 OCID: ${COMPARTMENT_CP21_ID}"

echo "Creating Compartment CP31 under CP3"
CREATED_COMPARTMENT=$(oci iam compartment create --compartment-id $COMPARTMENT_CP3_ID --name CP-31 --description "CP31")
COMPARTMENT_CP31_ID=$(jq -r '.data.id' <<< "$CREATED_COMPARTMENT")
echo "Compartment-CP31 OCID: ${COMPARTMENT_CP31_ID}"


# If we create/update and then try to use compartments straight away, sometimes we can get a 404. To try and avoid this, the script
# adds a short delay between the compartment management operations.
# Also sleep is not needed but kept as a safety measure for worst case for data plane sync with control plan changes.
sleep 10

# Create third level of compartments (CP211)
echo "Creating Compartment CP211 under CP21"
CREATED_COMPARTMENT=$(oci iam compartment create --compartment-id $COMPARTMENT_CP21_ID --name CP-211 --description "CP211")
COMPARTMENT_CP211_ID=$(jq -r '.data.id' <<< "$CREATED_COMPARTMENT")
echo "Compartment-CP21 OCID: ${COMPARTMENT_CP211_ID}"


# List all level compartments under tenancy
echo "List Compartments under Tenancy with compartment-id-in-subtree == true"
LIST_COMPARTMENTS=$(oci iam compartment list --compartment-id $TENANCY_ID --compartment-id-in-subtree true)

# List all level compartments under tenancy with accessLevel == Accessible
echo "List Compartments under Tenancy with compartment-id-in-subtree == true and accessLevel == accessible"
LIST_COMPARTMENTS=$(oci iam compartment list --compartment-id $TENANCY_ID --access-level accessible --compartment-id-in-subtree true)

# List first level compartments under CP2
echo "List Compartments under CP2"
LIST_COMPARTMENTS=$(oci iam compartment list --compartment-id $COMPARTMENT_CP2_ID)

# List first level compartments under CP21
echo "List Compartments under CP21"
LIST_COMPARTMENTS=$(oci iam compartment list --compartment-id $COMPARTMENT_CP21_ID)

# List first level compartments under CP3
echo "List Compartments under CP3"
LIST_COMPARTMENTS=$(oci iam compartment list --compartment-id $COMPARTMENT_CP3_ID)

echo "DONE"
