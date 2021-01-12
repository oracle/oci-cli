#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides an example of how to use tags in the CLI in terms of:
#
#   - Managing tag namespaces and tags by performing create, read (get/list) and update operations on them
#   - Applying tags to resources
#
# Requirements for running this script:
#   - OCI CLI v2.4.40 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI

# Define the color of echo text
RED='\033[0;31m'
ORANGE='\033[0;33m'
GREEN='\033[0;32m'

if [[ -z "$TENANCY_ID" ]];then
    echo "TENANCY_ID must be defined in the environment. "
    exit 1
fi

if [[ -z "$COMPARTMENT_ID" ]];then
    echo "COMPARTMENT_ID must be defined in the environment. "
    exit 1
fi

TOPIC_NAME="my_first_test_topic"
# Creating Topic
CREATED_TOPIC=$(oci ons topic create -c $COMPARTMENT_ID --name $TOPIC_NAME --description "A description of the topic")
TOPIC_ID=$(jq -r '.data."topic-id"' <<< "$CREATED_TOPIC")
echo "Topic OCID: ${TOPIC_ID}"

# Wait for the topic to become ACTIVE before creating subscriptions
max_sleep_time=10
sleep_time=0
while true; do
    sleep_time=$((sleep_time+2))

    GET_TOPIC=$(oci ons topic get --topic-id $TOPIC_ID)
    TOPIC_STATUS=$(jq -r '.data."lifecycle-state"' <<< "$GET_TOPIC")

    if [[ $TOPIC_STATUS != *"ACTIVE"* ]]; then
      continue
    fi

    if [ "$sleep_time" -gt "$max_sleep_time" ]
    then
      echo -e "$RED Topic (id: $TOPIC_ID) doesn't become active after waiting for 10 seconds. EXIT. $NC"
      exit 1
    fi
done

# Update topic description
oci ons topic update --topic-id $TOPIC_ID --description "new description"

# List all topics
oci ons topic list --compartment-id $COMPARTMENT_ID

# Create HTTPS subscription
CREATED_SUBSCRIPTION=$(oci ons subscription create --topic-id $TOPIC_ID --compartment-id $COMPARTMENT_ID --protocol "HTTPS" --subscription-endpoint "https://example.com")
SUBSCRIPTION_ID=$(jq -r '.data.id' <<< "$CREATED_SUBSCRIPTION")

# Re-send subscription confirmation
RESEND_SUBSCRIPTION_CONFIRMATION_RESPONSE=$(oci ons subscription resend-confirmation --id $SUBSCRIPTION_ID)
