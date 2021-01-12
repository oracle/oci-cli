#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides an example of how to create, delete compartments and track the delete compartment work requests.
#
# Requirements for running this script:
#   - OCI CLI v2.4.34 or later (you can check this by running oci --version)
#   - jq (https://stedolan.github.io/jq/) for JSON querying and manipulation of CLI output. This may be a useful utility in general
#     and may help cater to scenarios which can't be wholly addressed by the --query option in the CLI

set -e

TENANCY_ID=""  # Your tenancy ID

# Create compartment CompartmentExample1
echo "Creating Compartment CompartmentExample1"
CREATED_COMPARTMENT=$(oci iam compartment create --compartment-id $TENANCY_ID --name CompartmentExample1 --description "CompartmentExample1")
COMPARTMENT_ID=$(jq -r '.data.id' <<< "$CREATED_COMPARTMENT")
echo "CompartmentExample1 OCID: ${COMPARTMENT_ID}"

# If we create/update and then try to use compartments straight away, sometimes we can get a 404. To try and avoid this, the script
# adds a short delay between the compartment management operations
sleep 10

# Delete compartment CompartmentExample1
# The delete task status is tracked by the workrequest id returned.
# The deleted compartment is kept for audit retention period.
echo "Deleting Compartment CompartmentExample1"
DELETED_COMPARTMENT=$(oci iam compartment delete --compartment-id $COMPARTMENT_ID --force)
WORKREQUEST_ID=$(jq -r '."opc-work-request-id"' <<< "$DELETED_COMPARTMENT")
echo "WORKREQUEST OCID: ${WORKREQUEST_ID}"

# If we delete compartment and then try to get work request straight away, sometimes we can get a 404. To try and avoid this, the script
# adds a short delay between the compartment management operations
sleep 10

# List all work requests
echo "List work requests under the CompartmentExample1"
LIST_WORKREQUESTS=$(oci iam work-request list --compartment-id $COMPARTMENT_ID)
echo "List WorkRequest output: $LIST_WORKREQUESTS"

# Get the work request details.
echo "Get the delete work request for CompartmentExample1"
GET_WORKREQUEST=$(oci iam work-request get --work-request-id $WORKREQUEST_ID)
echo "GET WorkRequest output: $GET_WORKREQUEST"

echo "DONE"