#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides an example of how to copy an object in object storage.
#
# Requirements for running this script:
#   - OCI CLI v2.4.33 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI
set -e

# These variables should be provided in your environment.
# COMPARTMENT_ID=""
# SOURCE_BUCKET=""
# SOURCE_OBJECT=""
# DEST_BUCKET=""
# DEST_OBJECT=""

echo "Fetching namespace."
NAMESPACE=$(oci os ns get | jq -r .data)
echo "Using namespace '$NAMESPACE'."

WORK_REQUEST_ID=$(oci os object copy --bucket-name $SOURCE_BUCKET --source-object-name $SOURCE_OBJECT --destination-region us-phoenix-1 --destination-namespace $NAMESPACE --destination-bucket $DEST_BUCKET --destination-object-name $DEST_OBJECT | jq -r '."opc-work-request-id"')
echo "Work request ID is $WORK_REQUEST_ID."

while true; do

    WORK_REQUEST_STATE=$(oci os work-request get --work-request-id $WORK_REQUEST_ID | jq -r .data.status)
    if [ "$WORK_REQUEST_STATE" == "COMPLETED" ]; then
        echo "Copy has completed."
        break
    elif [ "$WORK_REQUEST_STATE" == "FAILED" ]; then
        echo "Copy has failed."
        break
    elif [ "$WORK_REQUEST_STATE" == "CANCELED" ]; then
        echo "Copy has been canceled."
        break
    else
        echo "Copy is still in $WORK_REQUEST_STATE state."
        sleep 5
    fi

done