#!/bin/bash -e
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the Monitoring Metrics apis in the Python CLI.
#
# This script # will demonstrate:
#   * Posting metrics for the given namespace & metric name
#   * Summarizing metrics for the given namespace and metric name
#   * Listing namespace & metric names previously posted.
#
# Assumptions:
#   * Post will post to PHOENIX endpoint
#
# Requirements for running this script:
#   - OCI CLI v2.4.40 or later (you can check this by running oci --version)

set -e

INGESTION_ENDPOINT="https://telemetry-ingestion.us-phoenix-1.oraclecloud.com"

usage() {
    echo "$*"
    echo "Usage: $0 <compartmentId> <namespace> <metric_name>"
    exit 1
}

echo::exec() {
    echo ">>> $*"
    "$@"
}

print_header() {
    echo 
    echo "##########################################"
    echo "# $*"
}

request::create() {
    local request_file="$1"; shift;

    \rm -f ${request_file} 2> /dev/null
    echo "$@" > ${request_file}

    echo "--------- Request"
    cat -n ${request_file}
}

utc::now() {
    date -u +"%Y-%m-%dT%H:%M:%S.000Z"
}

main() {
    if [[ -z ${COMPARTMENT} ]] || [[ -z ${NAMESPACE} ]] || [[ -z ${METRIC_NAME} ]];then
        [[ $# -lt 3 ]] && usage "Error: Insufficient params."
        local compartment="$1"; shift
        local namespace="$1"; shift
        local metric_name="$1"; shift
    else
        compartment=${COMPARTMENT}
        namespace=${NAMESPACE}
        metric_name=${METRIC_NAME}
    fi

    print_header "post metrics"
    file=/tmp/post_metrics.txt
    request::create ${file} '{
      "metricData": [
        {
          "namespace": "'${namespace}'",
          "compartmentId": "'${compartment}'",
          "name": "'${metric_name}'",
          "dimensions": {
              "resourceId": "ocid1.instance.oc1..something"
          },
          "metadata": { "unit": "megabytes" },
          "datapoints": [
            { "value": 15.25, "count": 8, "timestamp": "'"$( utc::now )"'" },
            { "value": 12.34, "count": 5, "timestamp": "'"$( utc::now )"'" }
          ]
        }
      ]
    }'

    echo::exec oci monitoring metric-data post \
        --from-json file://${file} \
        --endpoint "${INGESTION_ENDPOINT}"

    print_header "list metrics - no namespace or metric name given"
    echo::exec oci monitoring metric list \
        --compartment-id "${compartment}"

    print_header "list metrics - with namespace but not metric name given"
    echo::exec oci monitoring metric list \
        --compartment-id "${compartment}" \
        --namespace "${namespace}"

    print_header "list metrics - with namespace and metric name given"
    echo::exec oci monitoring metric list \
        --compartment-id "${compartment}" \
        --namespace "${namespace}" \
        --name "${metric_name}"

    print_header "summarize metrics"
    echo::exec oci monitoring metric-data summarize-metrics-data \
        --compartment-id "${compartment}" \
        --namespace "${namespace}" \
        --query-text "${metric_name}[1m].sum()"
}

main "$@"
