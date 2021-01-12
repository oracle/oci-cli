#!/bin/sh
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

set -e

{
    result=$(oci audit config update --compartment-id ${COMPARTMENT_ID} --retention-period-days 100)
} || {
    echo "Could not update audit config"
    echo ${result}
    exit 1
}

{
    result=$(oci audit config get --compartment-id ${COMPARTMENT_ID})
    retention_period=$(echo ${result} | jq '[.data][0]."retention-period-days"')
} || {
    echo "Could not get audit config retention-period-days."
    echo ${result}
    exit 1
}

if [ "${retention_period}" != "100" ];then
    echo "retention-period-days should be 100."
    exit 1
fi

echo "$(basename "$0") complete"
