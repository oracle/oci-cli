#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script demonstrates how to attach two Virtual Cloud Networks (VCN) to a single Dynamic Routing Gateway (DRG) to provide
# inter-VCN network connectivity, and remove and add back export route distribution to a DRG Attachment
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
DRG_ROUTE_TABLE_ID=$(oci network drg-route-table create --display-name "Drg Route Table" --drg-id $DRG_ID --wait-for-state AVAILABLE --query data.id --raw-output)
echo "Drg Route Table ID: $DRG_ROUTE_TABLE_ID"

echo "Assign the newly created DRG route table to drg attachment 1 (with VCN1)."
oci network drg-attachment update --drg-attachment-id $DRG_ATT_1_ID --drg-route-table-id $DRG_ROUTE_TABLE_ID

echo "Add a static route rule pointing to attachment 2."
# Create a temporary JSON file containing route rule we want to add
JSON_RULES_FILE=$(mktemp)
cat > ${JSON_RULES_FILE} << EOF
[
  {
    "destination": "192.168.250.0/24",
    "destinationType": "CIDR_BLOCK",
    "nextHopDrgAttachmentId": "$DRG_ATT_2_ID"
  }
]
EOF
oci network drg-route-rule add --drg-route-table-id $DRG_ROUTE_TABLE_ID --route-rules file://$JSON_RULES_FILE

echo "Creating Cpe."
CPE_ID=$(oci network cpe create --compartment-id $COMPARTMENT_ID --display-name "cpe_sample" --ip-address "192.168.0.2" --query data.id --raw-output)
echo "CPE ID:" $CPE_ID

echo "Creating IpSec connection."
IPSEC_ID=$(oci network ip-sec-connection create --compartment-id $COMPARTMENT_ID --cpe-id $CPE_ID --drg-id $DRG_ID \
--static-routes "[\"192.168.1.0/24\"]" --display-name "ipsec_sample" --wait-for-state AVAILABLE --query data.id --raw-output)
echo "IPSEC ID:" $IPSEC_ID

echo "Get the attachment for Ipsec tunnel."
ATTACHMENTS=$(oci network drg-attachment list --compartment-id $COMPARTMENT_ID --drg-id $DRG_ID --attachment-type "IPSEC_TUNNEL" --query data --raw-output)
IPSEC_ATTACHMENT=${ATTACHMENTS}

echo "Remove export route distribution."
IPSEC_ATTACHMENT_ID=$(jq -r '.[0].id' <<< "$IPSEC_ATTACHMENT")
EXPORT_ROUTE_DISTRIBUTION_ID=$(jq -r '.[0]."export-drg-route-distribution-id"' <<< "$IPSEC_ATTACHMENT")
oci network drg-attachment remove-export-route-distribution --drg-attachment-id $IPSEC_ATTACHMENT_ID

echo "Add the export route distribution back."
oci network drg-attachment update --drg-attachment-id $IPSEC_ATTACHMENT_ID --export-drg-route-distribution-id $EXPORT_ROUTE_DISTRIBUTION_ID

# Clean up resources.
echo "Deleting Ipsec"
oci network ip-sec-connection delete --ipsc-id $IPSEC_ID --wait-for-state TERMINATED --force

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

echo "Deleting Cpe"
oci network cpe delete --cpe-id $CPE_ID --force

echo "Script Finished"