#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides a basic example of how to use the DNS service in the CLI. The three variables at the beginning of the script must be specified accordingly:
#
#   * COMPARTMENT_ID: The first argument is the OCID of the compartment where we'll create a DNS zone
#   * DNS_ZONE_NAME: The second is the name of the DNS zone to create (e.g. my-example-zone.com)
#   * TARGET_COMPARTMENT_ID: The OCID of the compartment into which the DNS zone should be moved
#
# Requirements for running this script:
#   - OCI CLI v2.4.16 or later (you can check this by running oci --version)

set -e

if [ "${COMPARTMENT_ID}" == "" ]; then
  echo $0: "COMPARTMENT_ID must be defined in the environment"
  exit 1
fi

if [ "${DNS_ZONE_NAME}" == "" ]; then
  echo $0: "DNS_ZONE_NAME must be defined in the environment"
  exit 1
fi

if [ "${TARGET_COMPARTMENT_ID}" == "" ]; then
  echo $0: "TARGET_COMPARTMENT_ID must be defined in the environment"
  exit 1
fi

if [ -d ./services/dns/examples_and_test_scripts/dns_example ];then
    dns_example_data="./services/dns/examples_and_test_scripts/dns_example"
elif [ -d ./dns_example ];then
    dns_example_data="./dns_example"
else
    echo "Could not find dns_example_data data files"
    exit 1
fi


C_CLI=${COMPARTMENT_ID}
BORDER="=========================================="

function print_header() {
    echo $BORDER
    echo $1
    echo $BORDER
}

echo "Creating DNS zone: $DNS_ZONE_NAME"
oci dns zone create -c $COMPARTMENT_ID --zone-type PRIMARY --name $DNS_ZONE_NAME

ZONE_ID=$(oci dns zone get --zone-name-or-id $DNS_ZONE_NAME --raw-output --query 'data.id')
echo "ZONE ID: $ZONE_ID"

# list all zones
print_header "List all zones"
oci dns zone list -c $C_CLI

# We can also provide filter conditions and sort order to the list_zones operation. Here we filter based
# on an exact name match and filter by the time the zone was created descending
print_header "List all zones with sort and filter"
oci dns zone list -c $C_CLI --name $DNS_ZONE_NAME --sort-by timeCreated --sort-order DESC

# We can update records in the zone. This will overwrite any existing records so if there are items
# we wish to keep (e.g. the NS records in the zone) we need to read those out first and make
# sure they are included in the update.
#
# Downloading the existing collection, editing it, and calling update is not easy from the command line so
# we strongly recommend using the 'patch' functionality shown below to add / update / delete records. If
# you really want to use update, you can see an example in tests/test_dns.py::test_update_zone_records

# In addition to updates, we can use the patch operation to add and remove records from the zone without
# having to send through the complete list of records each time. In this example, we'll add 2 TXT records and
# remove one
print_header "Original Zone Records"
oci dns record zone get -c $C_CLI --zone-name-or-id $DNS_ZONE_NAME

RECORD_OPERATIONS_TEMPLATE=$(cat ${dns_example_data}/add_add_record_operations_template.json)
RECORD_OPERATIONS=$(sed s/__DNS_ZONE_NAME__/$DNS_ZONE_NAME/g <<< $RECORD_OPERATIONS_TEMPLATE)
echo $RECORD_OPERATIONS > "${dns_example_data}/add_add_record_operations.json"

echo "Patching zone records..."
oci dns record zone patch --zone-name-or-id $DNS_ZONE_NAME --items file://${dns_example_data}/add_add_record_operations.json > /dev/null 2>&1

print_header "List patched zone records filtered to only TXT records (newly added ones)"
oci dns record zone get -c $C_CLI --zone-name-or-id $DNS_ZONE_NAME --rtype TXT

# the example input template files have __DNS_ZONE_NAME__ in them which needs to be replaced with the real DNS_ZONE_NAME
RECORD_OPERATIONS_TEMPLATE=$(cat ${dns_example_data}/remove_record_operation_template.json)
RECORD_OPERATIONS=$(sed s/__DNS_ZONE_NAME__/$DNS_ZONE_NAME/g <<< $RECORD_OPERATIONS_TEMPLATE)
echo $RECORD_OPERATIONS > "${dns_example_data}/remove_record_operation.json"

echo "Patching zone records to remove one with rdata 'Some test data'..."
oci dns record zone patch --zone-name-or-id $DNS_ZONE_NAME --items file://${dns_example_data}/remove_record_operation.json > /dev/null 2>&1

print_header "List patched zone records filtered to only TXT records (now there is only one)"
oci dns record zone get -c $C_CLI --zone-name-or-id $DNS_ZONE_NAME --rtype TXT

# As part of patch operations, we can also specify preconditions (REQUIRE - data must be present, and
# PROHIBIT - data must not be present) which must be met for the operation to succeed
# This first example checks that there is no A record for subdomain testdomain1.$DNS_ZONE_NAME, and then adds one
RECORD_OPERATIONS_TEMPLATE=$(cat ${dns_example_data}/prohibit_if_present_then_add_record_template.json)
RECORD_OPERATIONS=$(sed s/__DNS_ZONE_NAME__/$DNS_ZONE_NAME/g <<< $RECORD_OPERATIONS_TEMPLATE)
echo $RECORD_OPERATIONS > "${dns_example_data}/prohibit_if_present_then_add_record.json"

echo 'Patching zone records with PROHIBIT precondition...'
oci dns record zone patch --zone-name-or-id $DNS_ZONE_NAME --items file://${dns_example_data}/prohibit_if_present_then_add_record.json

print_header "List patched zone records filtered to only A records (now there is one)"
oci dns record zone get -c $C_CLI --zone-name-or-id $DNS_ZONE_NAME --rtype A

# we expect this next command to return an error so dont quit the script
set +e

# Run the same patch operation again, and this time we expect it to fail because the record in the PROHIBIT precondition *does* exist
echo 'Repeating same patch with PROHIBIT precondition, which now fails because the record exists...'
oci dns record zone patch --zone-name-or-id $DNS_ZONE_NAME --items file://${dns_example_data}/prohibit_if_present_then_add_record.json
set -e

echo "Changing the compartment DNS zone: $DNS_ZONE_NAME"
# oci dns zone change-compartment --zone-id $ZONE_ID --compartment-id $TARGET_COMPARTMENT_ID

echo "Deleting DNS zone: $DNS_ZONE_NAME"
oci dns zone delete --zone-name-or-id $DNS_ZONE_NAME --force

# clean up temporary files
rm ${dns_example_data}/add_add_record_operations.json
rm ${dns_example_data}/remove_record_operation.json
rm ${dns_example_data}/prohibit_if_present_then_add_record.json

echo "SUCCESS"