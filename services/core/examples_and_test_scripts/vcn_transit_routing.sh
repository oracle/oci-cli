#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

#
# Requirements for running this script:
#   - OCI CLI v2.4.33 or later (you can check this by running oci --version)

#
# Sample to demonstrate setting up VCN Transit Routing
# <p>
# The sample relies on the correct IAM policies already being in place for a given compartment ID.
# <p/>
#
#                                              TOPOLOGY
#                 spokeVcn                                                   hubVcn
#               11.0.0.0/16                                               10.0.0.0/16
#      +----------------------------+                              +-------------------- +
#      |                            |                              |                     |
#      |                            |                           +---------------+        |
#      |                            |                           |  |            |        |
#      |  +-----------+             |                           v  |            |        |
#      |  |           +----+        +-----+                  +-----+----+       |        |
#      |  |  SUBNET   | RT |------->| LPG +------------------+ LPG | RT |       |        |
#      |  |           +----+        +-----+                  +-----+--+-+       |        |
#      |  +-----------+             |                              |  |         |        |
#      |                            |                              |  |    +----+---+    |
#      |                            |                              |  |    |   RT   |    |
#      |                            |                              +--|----+--------+----+
#      +----------------------------+                                 |    | DrgAtt |
#                                                                     |    +----+---+
#                                                                     |         |
#                                                                     |    +----+---+
#                                                                     +--->|   DRG  |
#                                                                          +----+---+
#                                                                               |
#                                                                               |
#                                                                               +
#                                                                to OnPrem Network 172.16.0.0/16
#
#  Vcn Transit Routing allows your OnPrem network to access your connected VCN as well as any
#  Peered VCN(s). VCN Transit Routing is achieved through the use of LocalPeeringGateway in conjunction
#  with a dynamically routing gateway (or DRG).
#
#  The order of operations and waiting for the appropriate state is important. This sample
#  demonstrates the creation of resources on a single thread to more clearly demonstrate the
#  setup for VCN Transit Routing.
#
#  It is also worth noting that the Hub VCN utilizes a dynamic routing gateway. DRGs are a
#  finite resource and may require contacting customer support if limits have been exceeded
#  for a given tenancy.
#

set -e

COMPARTMENT_ID=""  # Your compartment OCID
HUB_VCN_CIDR="10.0.0.0/16"
SPOKE_VCN_CIDR="11.0.0.0/16"
ON_PREM_NETWORK_CIDR="172.16.0.0/16"
SPOKE_VCN_SUBNET_CIDR="11.0.1.0/24"

# dynamically select image so it is for the correct region
AVAILABILITY_DOMAIN=$(oci iam availability-domain list -c $COMPARTMENT_ID --query 'data[0].name' --raw-output)

# Hub Vcn
echo 'Creating Hub VCN...'
HUB_VCN_ID=$(oci network vcn create -c $COMPARTMENT_ID --display-name hub-vcn --cidr-block 10.0.0.0/16 --wait-for-state AVAILABLE --query 'data.id' --raw-output 2>/dev/null)
echo "VCN OCID: ${HUB_VCN_ID}"

echo 'Creating Hub LPG route table...'
HUB_LPG_RT_ID=$(oci network route-table create -c $COMPARTMENT_ID --display-name hub-lpg-rt --route-rules '[]' --vcn-id $HUB_VCN_ID --wait-for-state AVAILABLE --query data.id --raw-output )
echo "Hub LPG Route table ID: $HUB_LPG_RT_ID"

echo 'Creating LPG in Hub VCN...'
HUB_LPG_ID=$(oci network local-peering-gateway create --compartment-id $COMPARTMENT_ID --display-name hub-lpg --vcn-id $HUB_VCN_ID --route-table-id $HUB_LPG_RT_ID --wait-for-state AVAILABLE --query data.id --raw-output)
echo "Hub LPG ID: $HUB_LPG_ID"

echo 'Creating DRG...'
HUB_DRG_ID=$(oci network drg create --compartment-id $COMPARTMENT_ID --display-name hub-drg --wait-for-state AVAILABLE --query data.id --raw-output)
echo "HUB DRG ID: $HUB_DRG_ID"

echo 'Creating Hub DRG Attachment route table...'
HUB_DRG_RT_ID=$(oci network route-table create -c $COMPARTMENT_ID --display-name hub-drg-att-rt --route-rules '[]' --vcn-id $HUB_VCN_ID --wait-for-state AVAILABLE --query data.id --raw-output )
echo "Hub DRG Route table ID: $HUB_LPG_RT_ID"

echo 'Creating DRG Attachment in Hub VCN...'
HUB_DRG_ATT_ID=$(oci network drg-attachment create --display-name hub-drg-att --drg-id $HUB_DRG_ID --vcn-id $HUB_VCN_ID --route-table-id $HUB_DRG_RT_ID --wait-for-state ATTACHED --query data.id --raw-output)
echo "Hub Drg Attachment ID: $HUB_DRG_ATT_ID"

echo 'Updating DRG route table with rules targeting spoke VCN...'
oci network route-table update --rt-id $HUB_DRG_RT_ID --force --route-rules '[{"cidrBlock":"'$SPOKE_VCN_CIDR'", "networkEntityId":"'$HUB_LPG_ID'"}]'

echo 'Updating LPG route table with rules targeting On-Prem network...'
oci network route-table update --rt-id $HUB_LPG_RT_ID --force --route-rules '[{"cidrBlock":"'$ON_PREM_NETWORK_CIDR'", "networkEntityId":"'$HUB_DRG_ID'"}]'


# Spoke VCN
echo 'Creating Spoke VCN...'
SPOKE_VCN_ID=$(oci network vcn create -c $COMPARTMENT_ID --display-name spoke-vcn --cidr-block $SPOKE_VCN_CIDR --wait-for-state AVAILABLE --query 'data.id' --raw-output 2>/dev/null)
echo "Spoke VCN ID: ${SPOKE_VCN_ID}"

echo 'Creating LPG in Spoke VCN...'
SPOKE_LPG_ID=$(oci network local-peering-gateway create --compartment-id $COMPARTMENT_ID --display-name spoke-lpg --vcn-id $SPOKE_VCN_ID --wait-for-state AVAILABLE --query data.id --raw-output)
echo "Spoke LPG ID: $SPOKE_LPG_ID"

echo 'Creating Route Table for subnet in Spoke VCN...'
SPOKE_SUBNET_RT=$(oci network route-table create --compartment-id $COMPARTMENT_ID --display-name spoke-subnet-rt --vcn-id $SPOKE_VCN_ID --route-rules '[{"cidrBlock":"'$HUB_VCN_CIDR'", "networkEntityId":"'$SPOKE_LPG_ID'"}, {"cidrBlock":"'$ON_PREM_NETWORK_CIDR'", "networkEntityId":"'$SPOKE_LPG_ID'"}]' --wait-for-state AVAILABLE --query data.id --raw-output)
echo "Spoke Subnet Route Table ID: $SPOKE_SUBNET_RT"

echo 'Creating subnet in Spoke VCN...'
SPOKE_SUBNET_ID=$(oci network subnet create -c $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN --display-name spoke-subnet --vcn-id $SPOKE_VCN_ID --cidr-block $SPOKE_VCN_SUBNET_CIDR --route-table-id $SPOKE_SUBNET_RT --wait-for-state AVAILABLE --query 'data.id' --raw-output 2>/dev/null)
echo "Spoke Subnet ID: $SPOKE_SUBNET_ID"


echo "Establishing Peering between Hub and Spoke VCN..."
oci network local-peering-gateway connect --local-peering-gateway-id $HUB_LPG_ID --peer-id $SPOKE_LPG_ID

echo 'VCN Transit Routing Setup Completed'


echo "Starting Cleanup"

# Clear Route Rules first
oci network route-table update --rt-id $HUB_DRG_RT_ID --route-rules '[]' --force

oci network route-table update --rt-id $HUB_LPG_RT_ID --route-rules '[]' --force

oci network drg-attachment delete --drg-attachment-id $HUB_DRG_ATT_ID --wait-for-state DETACHED --force

oci network drg delete --drg-id $HUB_DRG_ID --wait-for-state TERMINATED --force

oci network local-peering-gateway delete --local-peering-gateway-id $HUB_LPG_ID --wait-for-state TERMINATED --force

oci network route-table delete --rt-id $HUB_DRG_RT_ID --wait-for-state TERMINATED --force

oci network route-table delete --rt-id $HUB_LPG_RT_ID --wait-for-state TERMINATED --force

oci network vcn delete --vcn-id $HUB_VCN_ID --wait-for-state TERMINATED --force

oci network route-table update --rt-id $SPOKE_SUBNET_RT --route-rules '[]' --force

oci network subnet delete --subnet-id $SPOKE_SUBNET_ID --wait-for-state TERMINATED --force

oci network route-table delete --rt-id $SPOKE_SUBNET_RT --wait-for-state TERMINATED --force

oci network local-peering-gateway delete --local-peering-gateway-id $SPOKE_LPG_ID --wait-for-state TERMINATED --force

oci network vcn delete --vcn-id $SPOKE_VCN_ID --wait-for-state TERMINATED --force

echo 'Success!'
