# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# Copy auth token received in email and set CONFIRMATION_TOKEN
# One example of auth token from email: token=MDAwMHJpeWF3RFVzREhRMGlsOE9NUFNFY0R3cUd4clc0V0xLQjRNR3grMGI3bzRMT2xiT0Y0PQ==&
# Copy and set CONFIRMATION_TOKEN="MDAwMHJpeWF3RFVzREhRMGlsOE9NUFNFY0R3cUd4clc0V0xLQjRNR3grMGI3bzRMT2xiT0Y0PQ=="
if [[ -z "$CONFIRMATION_TOKEN" ]];then
    echo "CONFIRMATION_TOKEN must be defined in the environment. It can be copied from the email"
    exit 1
fi

if [[ -z "$SUBSCRIPTION_ID" ]];then
    echo "SUBSCRIPTION_ID must be defined in the environment."
    exit 1
fi

if [[ -z "$TOPIC_ID" ]];then
    echo "TOPIC_ID must be defined in the environment."
    exit 1
fi

if [[ -z "$COMPARTMENT_ID" ]];then
    echo "COMPARTMENT_ID must be defined in the environment. "
    exit 1
fi

# Confirm subscription
CONFIRMATION_RESPONSE=$(oci ons subscription confirm --id $SUBSCRIPTION_ID --token $CONFIRMATION_TOKEN --protocol "HTTPS")

# Get unsubscribe token
UNSUBSCRIBE_TOKEN=$(jq -r '.data."unsubscribe-url"' <<< $CONFIRMATION_RESPONSE | sed -e 's/.*token=\(.*\)&.*/\1/')

# Get the subscription
oci ons subscription get --subscription-id $SUBSCRIPTION_ID

# List all subscriptions
oci ons subscription list --compartment-id $COMPARTMENT_ID

# Update the subscription
oci ons subscription update --subscription-id $SUBSCRIPTION_ID --delivery-policy '{"backoffRetryPolicy": {"maxRetryDuration": 60000,"policyType": "EXPONENTIAL"}}'

# Publish message to the topic
oci ons message publish --topic-id $TOPIC_ID --body "hello world"

# Un-subscribe the subscription
oci ons subscription unsubscribe --id $SUBSCRIPTION_ID --token $UNSUBSCRIBE_TOKEN --protocol "HTTPS"

# Delete the topic
oci ons topic delete --topic-id $TOPIC_ID