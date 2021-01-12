#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

set -e

if [[ -z "$COMPARTMENT_ID" ]];then
    echo "COMPARTMENT_ID must be defined in the environment. "
    exit 1
fi

USER_NAME="TestUser"
USER_DESCRIPTION="User created by raw request"
TARGET_URI='https://identity.us-phoenix-1.oraclecloud.com/20160918/users/'
HTTP_METHOD='POST'
PROFILE='ADMIN'
REQUEST_BODY="{\"compartmentId\": \"$COMPARTMENT_ID\", \"name\": \"$USER_NAME\", \"description\": \"$USER_DESCRIPTION\"}"


echo "oci raw-request --profile ${PROFILE} --target-uri ${TARGET_URI} --http-method ${HTTP_METHOD} --request-body "${REQUEST_BODY}" | jq -r '.data.id'"
USER_OCID=$(oci raw-request --profile ${PROFILE} --target-uri ${TARGET_URI} --http-method ${HTTP_METHOD} --request-body "${REQUEST_BODY}" | jq -r '.data.id')

echo "Created user OCID: $USER_OCID"