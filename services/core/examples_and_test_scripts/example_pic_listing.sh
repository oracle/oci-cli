#!/usr/bin/env bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides an example of how use the consumer listings CLI in terms of:
#   - Retrieving a listing
#   - Retrieving at most 8 resource versions available for the listing
#
# It displays a short summary of the listing and resource versions of a listing.
#
# For more help with specific consumer listing commands with, see:
#   oci compute pic -h
#
# Requirements for running this script:
#   - OCI CLI v2.4.33 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI

set -e 

echo "Fetching data from pic catalog listing"

# Fetch a listing and get all the relevant fields
pic_list=$(oci compute pic listing list --limit 1 --sort-order ASC 2>/dev/null | grep -v WARNING)
listing_id=$(printf "%s" $pic_list       | jq -r '.data[0]."listing-id"')
display_name=$(printf "%s" $pic_list     | jq -r '.data[0]."display-name"')
publisher_name=$(printf "%s" $pic_list   | jq -r '.data[0]."publisher-name"')
summary=$(printf "%s" $pic_list          | jq -r '.data[0]."summary"')

# Get the last 8 resource versions sorted by publish date
echo "Fetching data from pic catalog listing version"
resource_version_list=$(oci compute pic version list  --listing-id $listing_id --sort-order ASC --limit 8)
resource_versions=$(printf "%s" $resource_version_list | jq '.data[] | ."listing-resource-version"' | paste -s -d, -)

echo ""
echo "Listing Id     : $listing_id"
echo "Display Name   : $display_name"
echo "Publisher Name : $publisher_name"
echo "Summary        : $summary"
echo "Versions       : [$resource_versions]"
