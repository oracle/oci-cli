#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# This script provides an example of how to get information about work requests.
#
# Requirements for running this script:
#   - OCI CLI v2.5.6 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI

# Please provide values for the following env variables:
# COMPARTMENT_ID
# RESOURCE_ID
# WORK_REQUEST_ID

set -e

if [[ -z "$COMPARTMENT_ID" ]];then
echo "COMPARTMENT_ID must be defined in the environment. "
exit 1
fi

if [[ -z "$RESOURCE_ID" ]];then
echo "RESOURCE_ID must be defined in the environment. "
exit 1
fi

if [[ -z "$WORK_REQUEST_ID" ]];then
echo "WORK_REQUEST_ID must be defined in the environment. "
exit 1
fi


echo "Listing work requests by compartment ID."
LIST_BY_COMPARTMENT=$(oci work-requests work-request list --compartment-id $COMPARTMENT_ID | jq -r .data)
echo "Output: '$LIST_BY_COMPARTMENT'"

echo "Listing work requests by compartment ID and resource ID."
LIST_BY_RESOURCE=$(oci work-requests work-request list --compartment-id $COMPARTMENT_ID --resource-id $RESOURCE_ID | jq -r .data)
echo "Output: '$LIST_BY_RESOURCE'"

echo "Getting information about a work request."
GET_WORK_REQUEST=$(oci work-requests work-request get --work-request-id $WORK_REQUEST_ID | jq -r .data)
echo "Output: '$GET_WORK_REQUEST'"

echo "Getting logs for a work request."
LIST_WORK_REQUEST_LOGS=$(oci work-requests work-request-log-entry list --work-request-id $WORK_REQUEST_ID --all | jq -r .data)
echo "Output: '$LIST_WORK_REQUEST_LOGS'"

echo "Getting error messages for a work request."
LIST_WORK_REQUEST_ERRORS=$(oci work-requests work-request-error list --work-request-id $WORK_REQUEST_ID --all | jq -r .data)
echo "Output: '$LIST_WORK_REQUEST_ERRORS'"