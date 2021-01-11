#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script demonstrates the modifications that can be performed on a subnet
#
# Requirements for running this script:
#   - OCI CLI v2.4.36 or later (you can check this by running oci --version)

set -e

COMPARTMENT_ID=""  # Your compartment OCID

# dynamically select image so it is for the correct region
AVAILABILITY_DOMAIN=$(oci iam availability-domain list -c $COMPARTMENT_ID --query 'data[0].name' --raw-output)

echo 'Creating VCN...'

VCN_ID=$(oci network vcn create -c $COMPARTMENT_ID --display-name update-subnet-example-vcn --cidr-block 10.0.0.0/16 --wait-for-state AVAILABLE --query 'data.id' --raw-output 2>/dev/null)
echo "VCN OCID: ${VCN_ID}"

echo 'Creating Subnet...'

SUBNET_ID=$(oci network subnet create -c $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN --display-name update-subnet-example-subnet --vcn-id $VCN_ID --cidr-block 10.0.0.0/24 --wait-for-state AVAILABLE --query 'data.id' --raw-output 2>/dev/null)
echo "Subnet OCID: $SUBNET_ID"

echo 'Creating new route table'
RT_ID=$(oci network route-table create -c $COMPARTMENT_ID --route-rules '[]' --vcn-id $VCN_ID --wait-for-state AVAILABLE --query data.id --raw-output )

echo "Route table ID: $RT_ID"

echo 'Creating new DHCP options'
DHCP_OPTS_ID=$(oci network dhcp-options create -c $COMPARTMENT_ID --vcn-id $VCN_ID --options '[{"type":"DomainNameServer", "serverType":"CustomDnsServer", "customDnsServers": ["8.8.8.8"]}]' --wait-for-state AVAILABLE --query data.id --raw-output 2>/dev/null)

echo "DHCP options ID: $DHCP_OPTS_ID"

echo 'Creating new security list'
SECURITY_LIST_ID=$(oci network security-list create -c $COMPARTMENT_ID --vcn-id $VCN_ID --egress-security-rules '[]' --ingress-security-rules '[]' --wait-for-state AVAILABLE --query data.id --raw-output 2>/dev/null)

echo "Security list ID: $SECURITY_LIST_ID"

echo 'Updating subnet'
oci network subnet update --subnet-id $SUBNET_ID --route-table-id $RT_ID --dhcp-options-id $DHCP_OPTS_ID --security-list-ids '["'$SECURITY_LIST_ID'"]'

# delete the subnets
oci network subnet delete --subnet-id $SUBNET_ID --wait-for-state TERMINATED --force

# delete the RT
oci network route-table delete --rt-id $RT_ID --wait-for-state TERMINATED --force

# delete the DHCP options
oci network dhcp-options delete --dhcp-id $DHCP_OPTS_ID --wait-for-state TERMINATED --force

# delete the security list
oci network security-list delete --security-list-id $SECURITY_LIST_ID --wait-for-state TERMINATED --force

# delete the VCN
oci network vcn delete --vcn-id $VCN_ID --wait-for-state TERMINATED --force

echo 'Success!'

