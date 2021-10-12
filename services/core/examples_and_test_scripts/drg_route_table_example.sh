#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script demonstrates how to add, update, delete, and list static route rules in Dynamic Routing Gateway route tables
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

echo "Creating a new DRG Route Table"
DRG_ROUTE_TABLE=$(oci network drg-route-table create --display-name "Drg Route Table" --drg-id $DRG_ID --wait-for-state AVAILABLE --query data --raw-output)
DRG_ROUTE_TABLE_ID=$(jq -r '.id' <<< "$DRG_ROUTE_TABLE")
IMPORT_ROUTE_DISTRIBUTION_ID=$(jq -r '."import-drg-route-distribution-id"' <<< "$DRG_ROUTE_TABLE")
echo "Drg Route Table ID: $DRG_ROUTE_TABLE_ID"

echo "Assign the newly created DRG route table to drg attachment 1 (with VCN1)."
oci network drg-attachment update --drg-attachment-id $DRG_ATT_1_ID --drg-route-table-id $DRG_ROUTE_TABLE_ID

echo "Add static route rules pointing to attachment 2."
# Create a temporary JSON file containing route rules we want to add
JSON_RULES_TO_ADD=$(mktemp)
cat > ${JSON_RULES_TO_ADD} << EOF
[
  {
    "destination": "192.168.250.0/24",
    "destinationType": "CIDR_BLOCK",
    "nextHopDrgAttachmentId": "$DRG_ATT_2_ID"
  },
  {
    "destination": "192.150.250.0/24",
    "destinationType": "CIDR_BLOCK",
    "nextHopDrgAttachmentId": "$DRG_ATT_2_ID"
  }
]
EOF
oci network drg-route-rule add --drg-route-table-id $DRG_ROUTE_TABLE_ID --route-rules file://$JSON_RULES_TO_ADD

echo "List static route rules in the route table."
STATIC_RULES=$(oci network drg-route-rule list --drg-route-table-id $DRG_ROUTE_TABLE_ID --route-type "STATIC" --query data --raw-output)
RULE_1_ID=$(jq -r '.[0].id' <<< "$STATIC_RULES")
RULE_2_ID=$(jq -r '.[1].id' <<< "$STATIC_RULES")
echo $STATIC_RULES

echo "Update static route rules."
# Create a temporary JSON file containing route rules we want to update
JSON_RULES_TO_UPDATE=$(mktemp)
cat > ${JSON_RULES_TO_UPDATE} << EOF
[
   {
     "id": "$RULE_1_ID",
     "destination": "120.168.250.0/24",
     "destinationType": "CIDR_BLOCK",
     "nextHopDrgAttachmentId": "$DRG_ATT_2_ID"
   },
   {
     "id": "$RULE_2_ID",
     "destination": "115.150.250.0/24",
     "destinationType": "CIDR_BLOCK",
     "nextHopDrgAttachmentId": "$DRG_ATT_2_ID"
   }
]
EOF
oci network drg-route-rule update --drg-route-table-id $DRG_ROUTE_TABLE_ID --route-rules file://$JSON_RULES_TO_UPDATE

echo "List static route rules in the route table."
STATIC_RULES=$(oci network drg-route-rule list --drg-route-table-id $DRG_ROUTE_TABLE_ID --route-type "STATIC" --query data --raw-output)
echo $STATIC_RULES

echo "Remove both static route rules."
# Create a temporary JSON file containing route rules we want to remove
JSON_RULES_TO_DELETE=$(mktemp)
cat > ${JSON_RULES_TO_DELETE} << EOF
[
 "$RULE_1_ID",
 "$RULE_2_ID"
]
EOF
oci network drg-route-rule remove --drg-route-table-id $DRG_ROUTE_TABLE_ID --route-rule-ids file://$JSON_RULES_TO_DELETE

echo "List static route rules in the route table."
STATIC_RULES=$(oci network drg-route-rule list --drg-route-table-id $DRG_ROUTE_TABLE_ID --route-type "STATIC" --query data --raw-output)
echo $STATIC_RULES

echo "Remove import route distribution."
oci network drg-route-table remove-import-route-distribution --drg-route-table-id $DRG_ROUTE_TABLE_ID

echo "Add import route distribution back."
DRG_ROUTE_DISTRIBUTION_ID=$(oci network drg-route-distribution create --display-name "Drg Route Distribution Sample" --drg-id $DRG_ID --distribution-type "IMPORT" --query data.id --raw-output)
oci network drg-route-table update --drg-route-table-id $DRG_ROUTE_TABLE_ID --import-route-distribution-id $DRG_ROUTE_DISTRIBUTION_ID

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