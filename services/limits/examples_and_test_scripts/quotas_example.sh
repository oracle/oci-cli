#!/usr/bin/env bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides an example of how to use quotas in the CLI in terms of:
#
#   - Managing quotas by performing create, read (get/list), update, delete operations on them
#
# Requirements for running this script:
#   - OCI CLI v2.5.19 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI
# Environment variables need to be set:
#   - COMPARTMENT_ID - The OCID of the compartment where the quota will be created. This must be your tenancy root compartment.
#   - NAME - A name for this quota.
#   - STATEMENT - A quota policy statement containing the quota-family (and if needed, quota-name) which should be whitelisted in the tenancy beforehand.
# Environment variables that may optionally be set:
#   - DESCRIPTION - A description for quota.
#   - NEW_DESCRIPTION - A description for modified quota.

set -e

if [[ "$COMPARTMENT_ID" == "" ]]; then
    echo "COMPARTMENT_ID must be defined in your environment"
    exit 1
fi

if [[ "$NAME" == "" ]]; then
    echo "NAME must be defined in your environment"
    exit 1
fi

if [[ "$STATEMENT" == "" ]]; then
    echo "STATEMENT must be defined in your environment"
    exit 1
fi

if [[ "$DESCRIPTION" == "" ]]; then
    DESCRIPTION="Sample quota"
fi

if [[ "$NEW_DESCRIPTION" == "" ]]; then
    NEW_DESCRIPTION="Modified sample quota"
fi

echo "Creating quota in compartment $COMPARTMENT_ID with statement '$STATEMENT'"
CREATED_QUOTA=$(oci limits quota create --compartment-id $COMPARTMENT_ID --name $NAME --description "$DESCRIPTION" --statements "[\"$STATEMENT\"]")

QUOTA_ID=$(jq -r '.data.id' <<< $CREATED_QUOTA)
echo "Getting quota $QUOTA_ID"
oci limits quota get --quota-id $QUOTA_ID

echo "Listing quotas in compartment $COMPARTMENT_ID"
oci limits quota list --compartment-id $COMPARTMENT_ID --limit 10

echo "Updating quota $QUOTA_ID to have description '$NEW_DESCRIPTION'"
oci limits quota update --quota-id $QUOTA_ID --description "$NEW_DESCRIPTION"

echo "Deleting quota $QUOTA_ID"
oci limits quota delete --quota-id $QUOTA_ID
