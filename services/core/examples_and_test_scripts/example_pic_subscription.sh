#!/usr/bin/env bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides an example of how use the consumer listings CLI in terms of:
#   - Retrieving a listing
#   - Retrieving a resource versions available for the listing
#   - Creating a subscription for the listing and version
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

# TODO: Fill in your compartment-id
compartment_id=${COMPARTMENT_ID}

echo 'Fetching listing id'
listing_id=$(oci compute pic listing list --limit 1 --sort-order ASC 2>/dev/null  | grep -v WARNING  | jq -r '.data[0]."listing-id"')

echo "Fetching version for the listing: $listing_id"
resource_version=$(oci compute pic version list --listing-id $listing_id --limit 1 | jq -r '.data[0]."listing-resource-version"')

echo "Fetching agreements for listing:$listing_id and version:$resource_version"
agreements=$(oci compute pic agreements get --listing-id "$listing_id" --resource-version "$resource_version")
signature=$(printf "%s" $agreements | jq -r '.data."signature"')
time_ret=$(printf "%s" $agreements  | jq -r '.data."time-retrieved"' | sed -e 's/000+00:00/Z/')
eula_link=$(printf "%s" $agreements | jq -r '.data."eula-link"')
oracle_tou_link=$(printf "%s" $agreements | jq -r '.data."oracle-terms-of-use-link"')

echo 'Creating subscription'
oci compute pic subscription create --compartment-id "$compartment_id" --listing-id "$listing_id" --resource-version "$resource_version" \
   --signature "$signature" --oracle-tou-link "$oracle_tou_link" --time-retrieved "$time_ret" --eula-link "$eula_link"
