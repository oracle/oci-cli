#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides basic examples of how to use volume backup policies in the CLI.
#
#   * Creating, updating, assigning and deleting scheduled backup policies
#
# Environment variables that need to be set:
#
#   * COMPARTMENT_ID: The OCID of the compartment where the policy will be created
#   * VOLUME_ID: The OCID of that will be used in this sample
#
# Requirements for running this script:
#   - OCI CLI v2.5.2+preview.1 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI
#   - Please make sure the user used by the CLI has the appropriate permissions for these operations

set -e

if [[ -z "$COMPARTMENT_ID" ]];then
echo "COMPARTMENT_ID must be defined in the environment. "
exit 1
fi

if [[ -z "$VOLUME_ID" ]];then
echo "VOLUME_ID must be defined in the environment. "
exit 1
fi

# Create a policy with one schedule for a daily incremental backup every day at 2am UTC and a retention of one week
CREATED_POLICY=$(oci bv volume-backup-policy create --display-name created_policy \
                                                    --compartment-id $COMPARTMENT_ID \
                                                    --schedules "[{ \
                                                                    \"backupType\": \"INCREMENTAL\", \
                                                                    \"offsetSeconds\": 7200, \
                                                                    \"period\": \"ONE_DAY\", \
                                                                    \"retentionSeconds\": 604800, \
                                                                    \"timeZone\": \"UTC\" \
                                                                   }]")
CREATED_POLICY_ID=$(jq -r '.data.id' <<< "$CREATED_POLICY")
echo "Created a volume backup policy. Policy OCID: ${CREATED_POLICY_ID}"

# Assign the created policy to a volume
CREATED_ASSIGNMENT=$(oci bv volume-backup-policy-assignment create --asset-id $VOLUME_ID --policy-id $CREATED_POLICY_ID)
ASSIGNMENT_ID=$(jq -r '.data.id' <<< "$CREATED_ASSIGNMENT")
echo "Assigned the volume backup policy to a volume. Assignment OCID: ${ASSIGNMENT_ID}"

# Update the policy's display name
UPDATED_POLICY=$(oci bv volume-backup-policy update --policy-id $CREATED_POLICY_ID --display-name updated_policy)
UPDATED_POLICY_ID=$(jq -r '.data.id' <<< "$UPDATED_POLICY")
echo "Updated the volume backup policy. Policy OCID: ${UPDATED_POLICY_ID}"

# Un-assign the policy
oci bv volume-backup-policy-assignment delete --policy-assignment-id $ASSIGNMENT_ID
echo "Deleted the policy assignment"

# Delete the policy
oci bv volume-backup-policy delete --policy-id $UPDATED_POLICY_ID
echo "Deleted the volume backup policy"

echo "Success!"