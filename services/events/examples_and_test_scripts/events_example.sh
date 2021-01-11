#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

set -e

# This script provides a basic example of how to use the Events Service apis in the Python CLI.
#
# This script # will demonstrate:
#   * Creating a new Rule
#   * Getting and listing Rule(s)
#   * Updating and Deleting an existing Rule
#
# Assumptions:
#   * Post will post to PHOENIX endpoint
#
# Requirements for running this script:
#   - OCI CLI v2.4.40 or later (you can check this by running oci --version)

EVENTS_ENDPOINT="https://events.us-phoenix-1.oraclecloud.com"

print_header() {
    echo
    echo "##########################################"
    echo "# $*"
    echo "##########################################"
    echo
}

main() {
    if [[ -z "$COMPARTMENT_ID" ]] || [[ -z "$STREAM_ID" ]];then
        echo "COMPARTMENT_ID and STREAM_ID must be defined in the environment. "
        exit 1
    fi

    ACTION_FILE=$(mktemp)

    echo "{
        \"actions\": [
            {
                \"actionType\": \"OSS\",
                \"description\": \"My Oss Action\",
                \"streamId\": \"${STREAM_ID}\",
                \"isEnabled\": true
            }
        ]
    }" > ${ACTION_FILE}

    CREATE_RULE_OUTPUT_FILE=$(mktemp)

    print_header "Creating Rule and storing Rule information in ${CREATE_RULE_OUTPUT_FILE}"
    oci events rule create \
        --compartment-id "${COMPARTMENT_ID}" \
        --display-name "CLI-Demo-Rule" \
        --condition {} \
        --actions file://${ACTION_FILE} \
        --is-enabled true \
        --wait-for-state ACTIVE \
        --endpoint "${EVENTS_ENDPOINT}" | tee ${CREATE_RULE_OUTPUT_FILE}

    RULE_ID=$(cat ${CREATE_RULE_OUTPUT_FILE} | jq -r ".data.id")

    print_header "Reading the Rule that was just created"
    oci events rule get \
        --rule-id "${RULE_ID}" \
        --endpoint "${EVENTS_ENDPOINT}"

    print_header "Updating the condition parameter of the Rule that we had created"
    oci events rule update \
        --rule-id "${RULE_ID}" \
        --condition {\"eventType\":\"com.oraclecloud.objectstorage.bucket.create\"} \
        --endpoint "${EVENTS_ENDPOINT}"

    print_header "Listing all the Rule(s) in the compartment"
    oci events rule list \
        --compartment-id "${COMPARTMENT_ID}" \
        --endpoint "${EVENTS_ENDPOINT}"

    print_header "Deleting the Rule that we had created"
    oci events rule delete \
        --rule-id "${RULE_ID}" \
        --endpoint "${EVENTS_ENDPOINT}"

}

main "$@"