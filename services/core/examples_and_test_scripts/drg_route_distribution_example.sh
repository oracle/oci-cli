#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script demonstrate how to add, update, delete, and list statements in a DRG Route Distribution for managing
# dynamic route rules in DRG Route Tables
#
# The three variables at the beginning of the script must be specified accordingly:
#
#   * The OCID of the compartment where resources will be created
#   * VCN 1 CIDR
#   * VCN 2 CIDR
#
# Requirements for running this script:
#   - OCI CLI v2.23.0 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying of CLI output. This may be a useful utility in general and may help cater to scenarios
#     which can't be wholly addressed by the --query option in the CLI

set -e

COMPARTMENT_ID="" # Your compartment OCID
VCN_CIDR_1="" # Your VCN 1 CIDR
VCN_CIDR_2="" # Your VCN 2 CIDR

if [[ -z "$COMPARTMENT_ID" ]]; then
    echo "COMPARTMENT_ID must be defined in your environment"
    exit 1
fi

if [[ -z "$VCN_CIDR_1" ]]; then
    echo "VCN_CIDR_1 must be defined in your environment"
    exit 1
fi

if [[ -z "$VCN_CIDR_2" ]]; then
    echo "VCN_CIDR_2 must be defined in your environment"
    exit 1
fi

echo "Creating DRG..."
DRG_ID=$(oci network drg create --compartment-id $COMPARTMENT_ID --display-name "Drg Sample" --wait-for-state AVAILABLE --query data.id --raw-output)
echo "DRG ID: $DRG_ID"

echo "Creating VCN 1"
VCN_1_ID=$(oci network vcn create -c $COMPARTMENT_ID --display-name "VCN 1" --cidr-block 10.0.0.0/16 --wait-for-state AVAILABLE --query 'data.id' --raw-output 2>/dev/null)
echo "VCN 1 ID: ${VCN_1_ID}"

echo "Creating DRG Attachment 1"
DRG_ATT_1_ID=$(oci network drg-attachment create --display-name "Drg Attachment 1" --drg-id $DRG_ID --vcn-id $VCN_1_ID --wait-for-state ATTACHED --query data.id --raw-output)
echo "Drg Attachment 1 ID: $DRG_ATT_1_ID"

echo "Creating VCN 2"
VCN_2_ID=$(oci network vcn create -c $COMPARTMENT_ID --display-name "VCN 2" --cidr-block 10.0.0.0/16 --wait-for-state AVAILABLE --query 'data.id' --raw-output 2>/dev/null)
echo "VCN 2 ID: ${VCN_2_ID}"

echo "Creating DRG Attachment 2"
DRG_ATT_2_ID=$(oci network drg-attachment create --display-name "Drg Attachment 2" --drg-id $DRG_ID --vcn-id $VCN_2_ID --wait-for-state ATTACHED --query data.id --raw-output)
echo "Drg Attachment 2 ID: $DRG_ATT_2_ID"

echo "Creating DRG Route Distribution."
DRG_ROUTE_DISTRIBUTION_ID=$(oci network drg-route-distribution create --display-name "Drg Route Distribution Sample" --drg-id $DRG_ID --distribution-type "IMPORT" --query data.id --raw-output)

echo "Add a statement to the route distribution to import from DRG Attachment 2"
# Create a temporary JSON file containing statement we want to add
STATEMENTS_TO_ADD=$(mktemp)
cat > ${STATEMENTS_TO_ADD} << EOF
[
  {
    "action": "ACCEPT",
    "matchCriteria": [
      {
          "drgAttachmentId": "$DRG_ATT_2_ID",
          "matchType": "DRG_ATTACHMENT_ID"
      }
    ],
    "priority": 1
  }
]
EOF
ROUTE_DISTRIBUTION_STATEMENTS=$(oci network drg-route-distribution-statement add --route-distribution-id $DRG_ROUTE_DISTRIBUTION_ID --statements file://$STATEMENTS_TO_ADD --query data --raw-output)
ROUTE_DISTRIBUTION_STATEMENT_ID=$(jq -r '.[0].id' <<< "$ROUTE_DISTRIBUTION_STATEMENTS")

echo "Add a statement to the route distribution to import from attachments of all types by specifying match all matchCriteria"
# Create a temporary JSON file containing statement we want to add
STATEMENTS_TO_ADD=$(mktemp)
cat > ${STATEMENTS_TO_ADD} << EOF
[
  {
    "action": "ACCEPT",
    "matchCriteria": [
      null
    ],
    "priority": 10
  }
]
EOF
ROUTE_DISTRIBUTION_STATEMENTS=$(oci network drg-route-distribution-statement add --route-distribution-id $DRG_ROUTE_DISTRIBUTION_ID --statements file://$STATEMENTS_TO_ADD --query data --raw-output)

echo "Create a new route table pointing to the route distribution."
DRG_ROUTE_TABLE=$(oci network drg-route-table create --display-name "Drg Route Table" --drg-id $DRG_ID --wait-for-state AVAILABLE --import-route-distribution-id $DRG_ROUTE_DISTRIBUTION_ID --query data --raw-output)
DRG_ROUTE_TABLE_ID=$(jq -r '.id' <<< "$DRG_ROUTE_TABLE")
IMPORT_ROUTE_DISTRIBUTION_ID=$(jq -r '."import-drg-route-distribution-id"' <<< "$DRG_ROUTE_TABLE")
echo "Drg Route Table ID: $DRG_ROUTE_TABLE_ID"

echo "Assign the newly created DRG route table to drg attachment 1 (with VCN1)."
oci network drg-attachment update --drg-attachment-id $DRG_ATT_1_ID --drg-route-table-id $DRG_ROUTE_TABLE_ID

echo "List route distribution statements in the route distribution."
STATEMENTS=$(oci network drg-route-distribution-statement list --route-distribution-id $DRG_ROUTE_DISTRIBUTION_ID --query data --raw-output)
echo $STATEMENTS

echo "List dynamic route rules in the route table."
DYNAMIC_RULES=$(oci network drg-route-rule list --drg-route-table-id $DRG_ROUTE_TABLE_ID --route-type "DYNAMIC" --query data --raw-output)
echo $DYNAMIC_RULES

echo "Update route distribution statement."
# Create a temporary JSON file containing statement we want to update
STATEMENTS_TO_UPDATE=$(mktemp)
cat > ${STATEMENTS_TO_UPDATE} << EOF
[
  {
    "id": "$ROUTE_DISTRIBUTION_STATEMENT_ID",
    "matchCriteria": [
      {
          "attachmentType": "IPSEC_TUNNEL",
          "matchType": "DRG_ATTACHMENT_TYPE"
      }
    ],
    "priority": 2
  }
]
EOF
oci network drg-route-distribution-statement update --route-distribution-id $DRG_ROUTE_DISTRIBUTION_ID --statements file://$STATEMENTS_TO_UPDATE

echo "List route distribution statements in the route distribution."
STATEMENTS=$(oci network drg-route-distribution-statement list --route-distribution-id $DRG_ROUTE_DISTRIBUTION_ID --query data --raw-output)
echo $STATEMENTS

echo "List dynamic route rules in the route table."
DYNAMIC_RULES=$(oci network drg-route-rule list --drg-route-table-id $DRG_ROUTE_TABLE_ID --route-type "DYNAMIC" --query data --raw-output)
echo $DYNAMIC_RULES

echo "Remove route distribution statement."
# Create a temporary JSON file containing statement we want to remove
STATEMENTS_TO_DELETE=$(mktemp)
cat > ${STATEMENTS_TO_DELETE} << EOF
[
 "$ROUTE_DISTRIBUTION_STATEMENT_ID"
]
EOF
oci network drg-route-distribution-statement remove --route-distribution-id $DRG_ROUTE_DISTRIBUTION_ID --statement-ids file://$STATEMENTS_TO_DELETE

echo "List route distribution statements in the route distribution."
STATEMENTS=$(oci network drg-route-distribution-statement list --route-distribution-id $DRG_ROUTE_DISTRIBUTION_ID --query data --raw-output)
echo $STATEMENTS

echo "List dynamic route rules in the route table."
DYNAMIC_RULES=$(oci network drg-route-rule list --drg-route-table-id $DRG_ROUTE_TABLE_ID --route-type "DYNAMIC" --query data --raw-output)
echo $DYNAMIC_RULES

# Clean up resources.
echo "Deleting Drg attachment 1"
oci network drg-attachment delete --drg-attachment-id $DRG_ATT_1_ID --wait-for-state DETACHED --force

echo "Deleting Drg attachment 2"
oci network drg-attachment delete --drg-attachment-id $DRG_ATT_2_ID --wait-for-state DETACHED --force

echo "Deleting Vcn 1"
oci network vcn delete --vcn-id $VCN_1_ID --force --wait-for-state TERMINATED --force

echo "Deleting Vcn 2"
oci network vcn delete --vcn-id $VCN_2_ID --force --wait-for-state TERMINATED --force

echo "Deleting Drg"
oci network drg delete --drg-id $DRG_ID --wait-for-state TERMINATED --force

echo "Script Finished"