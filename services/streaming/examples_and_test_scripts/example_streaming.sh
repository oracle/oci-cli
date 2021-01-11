#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

set -e -x

#########################################################
# This script provides examples of basic streaming usage.
# Dependencies:
# - jq, allows for simpler handling of json responses
#
# The streaming CLI is organized into two parts:
# - admin CLI; which supports management-level control-plane operations, like stream creation and deletion.
# - stream CLI; which supports stream-level data-plane operations, like publishing to and consuming from streams.
# Commands under the stream CLI require an explicit setting of the --endpoint argument, which can be retrieved
# from the Get Stream call on in the admin CLI.
#
# Included examples:
# - Admin CLI
#   - Create a stream
#   - Get a stream
#   - List streams
# - Stream CLI
#   - Publish to a stream
#   - Consume from a stream partition, using a cursor
#   - Delete a stream
#########################################################

# Provide the required information to get started; most required information is taken from the oci configuration file.
# Use the compartment ocid here for where you'd like to put your created streams.
if [[ -z "$COMPARTMENT_ID" ]];then
    echo "COMPARTMENT_ID must be defined in the environment. "
    exit 1
fi


#########################################################
# Create a stream
# Stream creation is asynchronous; it can take up to 15 seconds for the stream to become ACTIVE.
# Note that we're waiting for the state to become active before the command succeeds.
STREAM_FILE=$(mktemp)
echo "Creating a stream, and storing metadata in $STREAM_FILE"
oci streaming admin stream create \
    --compartment-id ${COMPARTMENT_ID} \
    --name demo-stream \
    --partitions 1 \
    --retention-in-hours 24 \
    --wait-for-state ACTIVE | grep -v "Action completed" | tee ${STREAM_FILE}

STREAM_ID=$(cat ${STREAM_FILE} | jq -r ".data.id")


#########################################################
# Get a stream
echo "Getting stream $STREAM_ID"
oci streaming admin stream get \
    --stream-id ${STREAM_ID}


#########################################################
# List streams
# You can also view all the streams in a compartment.
# It is often useful to filter by lifecycle-state or name.
echo "Listing all active streams in compartment $COMPARTMENT_ID"
oci streaming admin stream list \
    --compartment-id ${COMPARTMENT_ID} \
    --lifecycle-state ACTIVE \
    --all


#########################################################
# Publish to a stream
# Stream operations require setting a message endpoint explicitly, which is included in each streams' metadata.
MESSAGE_ENDPOINT=$(cat ${STREAM_FILE} | jq -r '.data["messages-endpoint"]')

# A single request can contain many messages; messages are base64 encoded key/value pairs.
# The messages argument is a json array of messages; its easiest to pass the argument from a file.
# An example json structure can be obtained via an oci command:
# `oci streaming stream message put --generate-param-json-input messages`

KEY1=$(echo -n "key1" | base64)
MESSAGE1=$(echo "hello world! " | base64)

KEY2=$(echo -n "key2" | base64)
MESSAGE2=$(echo "from Oracle Streaming Service!" | base64)

JSON_FILE=$(mktemp)
cat > ${JSON_FILE} << EOF
[
    { "key": "${KEY1}", "value": "${MESSAGE1}" },
    { "key": "${KEY2}", "value": "${MESSAGE2}" }
]
EOF

echo "Publishing 2 messages to stream $STREAM_ID"
oci streaming stream message put \
    --endpoint ${MESSAGE_ENDPOINT} \
    --stream-id ${STREAM_ID} \
    --messages file://${JSON_FILE}


#########################################################
# Consuming from a stream
# Cursors describe a location in the stream, and are used to traverse the stream.
echo "Creating a partition-0 cursor at the trim horizon."
CURSOR=$(oci streaming stream cursor create-cursor \
    --endpoint ${MESSAGE_ENDPOINT} \
    --stream-id ${STREAM_ID} \
    --partition 0 \
    --type TRIM_HORIZON | jq -r '.data.value')

# Get messages
RESPONSE_FILE=$(mktemp)
oci streaming stream message get \
    --endpoint ${MESSAGE_ENDPOINT} \
    --stream-id ${STREAM_ID} \
    --cursor ${CURSOR} \
    --limit 100 | tee ${RESPONSE_FILE}

# Each response returns a new cursor, which can be used to get subsequent messages from the stream.
CURSOR=$(cat ${RESPONSE_FILE} | jq -r '.["opc-next-cursor"]')

# Remember that keys and values are base64 encoded binary values.
echo "Decoding the messages"
cat ${RESPONSE_FILE} | jq -r ".data[] | .value" | base64 -d


#########################################################
# Deleting the stream
echo "Deleting the stream $STREAM_ID"
oci streaming admin stream delete \
    --stream-id ${STREAM_ID} \
    --force \
    --wait-for-state DELETED
