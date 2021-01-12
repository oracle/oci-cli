#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the Network Security Group feature in the CLI.
# These variables must be defined by the user:
#   * COMPARTMENT_ID: The OCID of the compartment that contains our resources, and is where we'll create the network security group 
#   * VCN_ID: The OCID of a VCN where we'll create the NSG
#   * VNIC_ID: The OCID of a VNIC which will belong to the NSG
#   * SUBNET_ID: The OCID of the VCN's subnet that will contain the VNIC
#   * IMAGE_ID: The OCID of the disk image needed to boot the new instance
#   * AVAILABILITY_DOMAIN: The AD in which to place the newly created VNIC 
#
# This script will demonstrate:
#   * Creating and getting information about a new Network Security Group (NSG)
#   * Adding and removing security rules to the NSG
#   * Listing and adding VNICs that belong to an NSG
#
# This script uses jq (https://stedolan.github.io/jq/) for JSON querying of CLI output.

COMPARTMENT_ID=""
VCN_ID=""
VNIC_ID=""
SUBNET_ID=""
IMAGE_ID=""
AVAILABILITY_DOMAIN=""
NSG_DISPLAY_NAME="Example network security group"



# Create a temporary JSON file containing security rules we wish to implement
# NOTE: Unspecified port ranges default to 'ALL'
JSON_RULES_FILE=$(mktemp)
cat > ${JSON_RULES_FILE} << EOF
[
   { 
      "description": "Incoming SSH connections from private network",
      "source": "10.0.0.0/24",
      "sourceType": "CIDR_BLOCK",
      "direction": "INGRESS",
      "isStateless": false,
      "protocol": "6",
      "tcpOptions": {
        "destinationPortRange": {
          "max": 22,
          "min": 22
        }
      }
    },
   { 
      "description": "Incoming internet connections",
      "source": "0.0.0.0/0",
      "sourceType": "CIDR_BLOCK",
      "direction": "INGRESS",
      "isStateless": false,
      "protocol": "6",
      "tcpOptions": {
        "destinationPortRange": {
          "max": 443,
          "min": 443
        }
      }
    },
    { 
      "description": "Outbound port 8080 connections to middle-tier NSG",
      "destination": "ocid.of.middle-tier.network.security.group",
      "destinationType": "NETWORK_SECURITY_GROUP",
      "direction": "EGRESS",
      "isStateless": false,
      "protocol": "6",
      "tcpOptions": {
        "destinationPortRange": {
          "max": 8080,
          "min": 8080
        }
      }
    }
]
EOF

# Create a new network security group
echo "Creating network security group"
echo "========================="
oci network nsg create --compartment-id $COMPARTMENT_ID --vcn-id $VCN_ID --display-name $DISPLAY_NAME

# List all network security groups (you may optionally filter by VCN OCID or exact display name); store id of the first returned NSG. 
echo "Listing network security groups"
echo "========================="
CREATED_NSG=`oci network nsg list --compartment-id $COMPARTMENT_ID | jq -r .data[0].id`
NSG_ID_1=`jq -r .data[0].id <<< $CREATED_NSG`

# Create a second network security for use in later configs
echo "Creating a second network security group"
echo "========================="
SECOND_NSG=`oci network nsg create --compartment-id $COMPARTMENT_ID --vcn-id $VCN_ID --display-name "Second NSG"`
NSG_ID_2=`jq -r .data.id <<< $SECOND__NSG`

# Add a VNIC to the NSG
echo "Adding $VNIC to the network security group"
echo "========================="
oci network vnic update --vnic-id $VNIC_ID --nsg-ids "[$NSG_ID]"

# List all VNICs in a given network security group
echo "Listing VNICs that belong to the network security group"
echo "========================="
oci network nsg vnics list --nsg-id $NSG_ID

# Update the display name for a network security group
echo "Changing display name for network security group $NSG_ID"
echo "========================="
oci network nsg update --nsg-id $NSG_ID --display-name "Updated example network security group"

# Add a rule to a network security group (using an intermediary file for JSON input)
echo "Adding security rules to network security group $NSG_ID"
echo "========================="
oci network nsg rules add --nsg-id $NSG_ID --security-rules file://$JSON_RULES_FILE

# List all rules in a given network security group
echo "Listing security rules for $NSG_ID"
echo "========================="
RULES_LIST=`oci network nsg rules list --nsg-id $NSG_ID`
RULE_1_ID=`jq -r .data[0].id <<< $RULES_LIST`
RULE_2_ID=`jq -r .data[1].id <<< $RULES_LIST`
RULE_3_ID=`jq -r .data[2].id <<< $RULES_LIST`

# Update the definition of a rule
echo "Modifying an existing security rule"
echo "========================="
JSON_UPDATE_RULE_FILE=$(mktemp)
cat > ${JSON_UPDATE_RULE_FILE} << EOF
[
    {
    "id": "$RULE_3_ID",
    "description": "Outbound port 8000 connections to middle-tier NSG",
    "destination": "ocid.of.middle-tier.network.security.group",
    "destinationType": "NETWORK_SECURITY_GROUP",
    "direction": "EGRESS",
    "isStateless": false,
    "protocol": "6",
    "tcpOptions": {
      "destinationPortRange": {
        "max": 8000,
        "min": 8000
      }
    }
  }
]
EOF
oci network nsg rules update --nsg-id $NSG_ID --security-rules file://$JSON_RULE_FILE

# Delete first two security rules using their Oracle-assigned IDs
echo "Removing rules $RULE_1_ID and $RULE_2_ID from $NSG_ID"
echo "========================="
oci network nsg rules remove --nsg-id $NSG_ID --security-rule-ids "[$RULE_ID, $RULE_2_ID]"

# Get details about a network security group
echo "Showing network security group details"
echo "========================="
oci network nsg get --nsg-id $NSG_ID

# Launch a new compute instance whose primary VNIC will be in the network security group
echo "Launch a new instance with primary VNIC in the network security group"
echo "========================="
NEW_INSTANCE=`oci compute instance launch --compartment-id $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN --subnet-id $SUBNET_ID --shape "VM.Standard1.2" --image $IMAGE_ID --nsg-ids "[$NSG_ID, $NSG_ID_2]"`
NEW_INSTANCE_ID=`jq -r .data.id <<< $NEW_INSTANCE`
NEW_INSTANCE_VNIC=`oci compute instance list-vnics --instance-id $NEW_INSTANCE_ID`
NEW_INSTANCE_VNIC_ID=`jq -r .data[0].id`

# Create a new secondary VNIC that will be in the network security group
echo "Creating a new VNIC in the network security group for an existing instance"
echo "========================="
SECONDARY_VNIC=`oci compute instance vnic attach-vnic --instance $INSTANCE_ID --subnet-id $SUBNET_ID --nsg-ids "[$NSG_ID]"`
SECONDARY_VNIC_ID=`jq -r .data.id <<< $SECONDARY_VNIC`

# List all VNICs in an NSG
echo "Listing all VNICs in the network security group $NSG_ID"
echo "========================="
oci network nsg vnics list --nsg-id $NSG_ID

# Remove the VNIC from all NSGs
echo "Removing $VNIC_ID, $NEW_INSTANCE_VNIC_ID, and $SECONDARY_VNIC_ID from the network security group"
echo "========================="
oci network vnic update --vnic-id $VNIC_ID --nsg-ids "[]"
oci network vnic update --vnic-id $NEW_INSTANCE_VNIC_ID --nsg-ids "[]"
oci network vnic update --vnic-id $SECONDARY_VNIC_ID --nsg-ids "[]"

# Clean up the example instance
echo "Terminating compute instance $INSTANCE_ID"
echo "========================="
oci network compute instance terminate --instance-id $INSTANCE_ID

# Delete the network security group, which must not contain any VNICs
echo "Deleting Network Security Group $NSG_ID"
echo "========================="
oci network nsg delete --nsg-id $NSG_ID
