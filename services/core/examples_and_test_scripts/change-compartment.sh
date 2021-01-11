#!/bin/sh
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

#
# This script shows how to change the compartment in which an instance lives.
# This will also wait until the operation has succeeded.
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
    echo "Usage: change-instance-compartment instanceid compartmentid"
    exit
fi

echo "About to move instance $INSTANCE_ID into compartment $COMPARTMENT_ID"

# Start the move. This step will fail immediately in cases such as authorization
# failure, invalid compartment or instance ID, etc. But once the move starts,
# it may take some time for it to complete.

# This can also be checked by polling the work request service. This might
# be necessary if finer-grained info is needed, or if you want to wait for
# both success and failure. See the "change-compartment-using-work-request-id.sh".

oci compute instance change-compartment --instance-id $INSTANCE_ID --compartment-id $COMPARTMENT_ID --wait-for-state SUCCEEDED

# Final check is to ensure the instance is now in the new compartment.

NEW_COMPARTMENT=$(oci compute instance get --instance-id $INSTANCE_ID | jq -r '.data."compartment-id"')

if [ "$NEW_COMPARTMENT" = "$COMPARTMENT_ID" ]
then
    echo "SUCCESS: Instance is now in the new compartment."
else
    echo "FAIL: Instance is not in the new compartment."
    echo "Expected compartment ID: $COMPARTMENT_ID"
    echo "Actual compartment ID: $NEW_COMPARTMENT"
    exit 2
fi

