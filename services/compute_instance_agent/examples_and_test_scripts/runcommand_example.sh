#!/usr/bin/env bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides an example of how use the instance pools CLI in terms of:
#   - Creating a command
#   - List all commands in a compartment
#   - Get command information from commandId
#   - List all command executions
#   - Get command execution information from commandId
#
# For more help with specific help, see:
#   oci instance-agent command -h
#   oci instance-agent command-execution -h
#
# Requirements for running this script:
#   - OCI CLI
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI
# Environment variables need to be set:
#   - COMPARTMENT_ID - Your compartment OCID
#   - INSTANCE_ID - the instance ID where the command will run

set -e

if [[ -z "$COMPARTMENT_ID" ]]; then
    echo "COMPARTMENT_ID must be defined in your environment"
    exit 1
fi

if [[ -z "$INSTANCE_ID" ]]; then
    echo "INSTANCE_ID must be defined in your environment"
    exit 1
fi

CREATE_COMMAND_TARGET_FILE_LOCATION="create_command_target.json"
CREATE_COMMAND_TARGET_JSON=$(sed s/__INSTANCE_ID__/$INSTANCE_ID/g $CREATE_COMMAND_TARGET_FILE_LOCATION)

CREATE_COMMAND_CONTENT_FILE_LOCATION="create_command_content.json"
CREATE_COMMAND_CONTENT_JSON=$(cat $CREATE_COMMAND_CONTENT_FILE_LOCATION)

echo "Starting command creation"
CREATED_COMMAND_ID=$(oci instance-agent command create --compartment-id $COMPARTMENT_ID \
                                                --timeout-in-seconds 3600 \
                                                --target "$CREATE_COMMAND_TARGET_JSON" \
                                                --display-name "example-command-$RANDOM" \
                                                --content "$CREATE_COMMAND_CONTENT_JSON" \
                                                --query 'data.id' --raw-output)
echo "Created commandId: $CREATED_COMMAND_ID"
echo "Getting command info for commandId:$CREATED_COMMAND_ID"
oci instance-agent command get --command-id $CREATED_COMMAND_ID

echo "Getting command execution info for commandId:$CREATED_COMMAND_ID and instanceId:$INSTANCE_ID"
oci instance-agent command-execution get --command-id $CREATED_COMMAND_ID --instance-id $INSTANCE_ID

echo "Listing all commands in compartmentId:$COMPARTMENT_ID"
oci instance-agent command list --compartment-id $COMPARTMENT_ID

echo "Listing all command execution info for instanceId:$INSTANCE_ID"
oci instance-agent command-execution list --compartment-id $COMPARTMENT_ID --instance-id $INSTANCE_ID

echo "Pausing for 3 minutes to let the given script run to completion"
sleep 180

echo "Getting command execution info again for commandId:$CREATED_COMMAND_ID and instanceId:$INSTANCE_ID"
oci instance-agent command-execution get --command-id $CREATED_COMMAND_ID --instance-id $INSTANCE_ID

