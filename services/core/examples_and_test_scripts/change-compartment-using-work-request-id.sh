#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

#
# This script shows how to change the compartment in which an instance lives.
# It differs from "change-compartment.sh" in that this script will get the
# work request ID and use it to wait for completion and determine the status.
#
# Uses BASH to ensure mathematical operation is supported
#
# Requirements for running this script:
#   - OCI CLI v2.5.7 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation
#     of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed
#     by the --query option in the CLI
#
#  Usage: change-compartment-using-work-request-id.sh instanceid compartmentid

set -e

INSTANCE_ID=$1
COMPARTMENT_ID=$2

if [ -z "$COMPARTMENT_ID" ] || [ -z "$INSTANCE_ID" ]
then
    echo "Usage: change-compartment-using-work-request-id.sh instanceid compartmentid"
    exit
fi

echo "About to move instance $INSTANCE_ID into compartment $COMPARTMENT_ID"

# Start the move. This step will fail immediately in cases such as authorization
# failure, invalid compartment or instance ID, etc. But once the move starts,
# it may take some time for it to complete. In that case, we get back a
# request ID we can use with the work request service to query status.

REQUEST_ID=$(oci compute instance change-compartment --instance-id $INSTANCE_ID --compartment-id $COMPARTMENT_ID | jq -r '."opc-work-request-id"')

# Wait for it to be complete. We can do this by checking the percent-complete status.
COUNTER=0

PERCENT_COMPLETE="0"

# It is also possible to check the status instead of relying on the
# percent complete, though the check would have to check
# for multiple states (e.g. SUCCEEDED, FAILED).
while (( $PERCENT_COMPLETE < 100 ));
do
    # Wait a bit to avoid hitting API throttles
    sleep 5
    COUNTER=`expr $COUNTER + 1`
    if [ "$COUNTER" -eq "12" ]
    then
        echo "Timed out waiting for state change."
        exit 1
    fi
    
    # Check the status.
    RAW_OUTPUT=`oci work-requests work-request get --work-request-id $REQUEST_ID`

    # There's a lot of interesting information in the output, but for
    # this example, we just care if it is finished and its status.
    PERCENT_COMPLETE=`echo $RAW_OUTPUT | jq -r '.data."percent-complete"'`
    STATUS=`echo $RAW_OUTPUT |  jq -r '.data.status'`
    echo "Try $COUNTER: percent complete is $PERCENT_COMPLETE and status is $STATUS"
done

shopt -s nocasematch

# We can simply check the STATUS to determine what happened.
if [[ "$STATUS" = "SUCCEEDED" ]]
then
    echo "SUCCESS: Instance is now in the new compartment."
else
    echo "FAIL: Instance move failed, status is $STATUS"
    exit 2
fi

