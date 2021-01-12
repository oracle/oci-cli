#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides basic examples of how to use copy volume backup in the CLI.
#
#   * Copy a volume backup from a source region to a destination region, wait for the copy to succeed
#
# Environment variables that need to be set:
#
#   * VOLUME_BACKUP_ID: The OCID of the volume backup to copy
#   * DESTINATION_REGION: The name of the destination region
#   * DISPLAY_NAME (optional) : The display name of the copied backup. If not specified, defaults to the same as the
# source backup
#   * KMS_KEY_ID (optional) : A KMS key in the destination region to encrypt the volume backup with.
# If not set, the backup's encryption key will be encrypted with a platform master key.
#
# Requirements for running this script:
#   - OCI CLI v2.5.7+preview.1 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI
#   - Please make sure the user used by the CLI has the appropriate permissions for these operations

set -e

if [[ -z "$VOLUME_BACKUP_ID" ]];then
echo "VOLUME_BACKUP_ID must be defined in the environment."
exit 1
fi

if [[ -z "$DESTINATION_REGION" ]];then
echo "DESTINATION_REGION must be defined in the environment."
exit 1
fi

if [[ -z "$DISPLAY_NAME" ]];then
echo "no DISPLAY_NAME defined in the environment. Defaulting to using the source backup display name."
fi

if [[ -z "$KMS_KEY_ID" ]];then
echo "no KMS_KEY_ID defined in the environment. Defaulting to not using KMS encryption in the destination region."
fi


echo "Copying volume backup id $VOLUME_BACKUP_ID to region $DESTINATION_REGION"

# Copy the source volume backup to the specified destination region. Display-name and kms-key-id are optional.
FLAGS=(--volume-backup-id ${VOLUME_BACKUP_ID} --destination-region ${DESTINATION_REGION} )
if [[ -n "$DISPLAY_NAME" ]];then
	FLAGS+=(--display-name "\"${DISPLAY_NAME}\"")
fi

if [[ -n "$KMS_KEY_ID" ]];then
	FLAGS+=(--kms-key-id $KMS_KEY_ID)
fi

COPIED_BACKUP=$(./oci bv backup copy "${FLAGS[@]}")
echo "Copy backup response : $COPIED_BACKUP"

# Once the copy operation returns, we can poll on the copied backup in the destination region to wait for the backup's
# state to reach AVAILABLE.

COPIED_BACKUP_ID=$(jq -r '.data.id' <<< "$COPIED_BACKUP")
BACKUP_STATE=$(jq -r '.data["lifecycle-state"]' <<< "$COPIED_BACKUP")

echo "Waiting for the copied backup to reach AVAILABLE state."

while [ "$BACKUP_STATE" != "AVAILABLE" ]
do
	COPIED_BACKUP=$(./oci bv backup get --region $DESTINATION_REGION --volume-backup-id $COPIED_BACKUP_ID)
	BACKUP_STATE=$(jq -r '.data["lifecycle-state"]' <<< "$COPIED_BACKUP")
	echo "Copied backup with OCID: ${COPIED_BACKUP_ID} is in state ${BACKUP_STATE}..."
	sleep 10
done

echo "Copied backup with OCI $COPIED_BACKUP_ID reached AVAILABLE state."
