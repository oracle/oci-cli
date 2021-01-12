#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the Monitoring Alarm apis in the Python CLI. This script
# will demonstrate:
#
#   * Creating, updating, retrieving, listing and deleting alarms.
#   * Retrieving alarm state history.
#   * Listing status of alarms.
#
# The following variables must be populated at the top of this script:
#
#   * Display name for the alarm
#   * Namespace for the alarm
#   * Query of the alarm
#   * Severity of the alarm
#   * Start time of the suppression, e.g. 2018-12-10T05:00:00.600Z
#   * End time of the suppression, e.g. 2018-12-11T05:00:00.600Z
#
# Requirements for running this script:
#   - OCI CLI v2.4.40 or later (you can check this by running oci --version)
#   - Define environment variable COMPARTMENT_ID and NOTIFICATION_DESTINATION

set -e

DISPLAY_NAME="Alarm for Python CLI sample";
NAMESPACE="oci_computeagent";
QUERY_TEXT="CpuUtilization[1m].max() > 75";
SEVERITY="CRITICAL";
SUPPRESS_FROM=$(date -u +'%Y-%m-%dT%H:%M:%S.000Z');
if [ "$OSTYPE" == "linux-gnu" ]; then
    # Linux
    SUPPRESS_UNTIL=$(date -u -d '+1 Day' +'%Y-%m-%dT%H:%M:%S.000Z');
elif [[ "$OSTYPE" =~ darwin.* ]]; then
    # Mac OSX
    SUPPRESS_UNTIL=$(date -u -v+1d +'%Y-%m-%dT%H:%M:%S.000Z');
fi

BORDER="=========================================="

function print_header() {
    echo $BORDER
    echo $1
    echo $BORDER
}

if [[ "$COMPARTMENT_ID" == "" || "$NOTIFICATION_DESTINATION" == "" ]]; then
    echo "COMPARTMENT_ID and NOTIFICATION_DESTINATION must be defined in your environment"
    exit 1
fi

echo "Create a new alarm"
ALARM_ID=$(oci monitoring alarm create --display-name "$DISPLAY_NAME" \
                                      --compartment-id $COMPARTMENT_ID \
                                      --metric-compartment-id $COMPARTMENT_ID \
                                      --namespace $NAMESPACE \
                                      --query-text "$QUERY_TEXT" \
                                      --severity $SEVERITY \
                                      --destinations "[\"$NOTIFICATION_DESTINATION\"]" \
                                      --is-enabled "true" \
                                      --query "data.id" \
                                      --raw-output)

echo "Update the new alarm by adding a suppression"
JSON_FILE=$(mktemp)
cat > ${JSON_FILE} << EOF
    { "description": "Suppress the alarm", "timeSuppressFrom": "$SUPPRESS_FROM", "timeSuppressUntil": "$SUPPRESS_UNTIL" }
EOF

oci monitoring alarm update --alarm-id $ALARM_ID \
                           --suppression file://${JSON_FILE}

echo "Remove suppression for the alarm"
oci monitoring suppression remove --alarm-id $ALARM_ID

echo "Retrieve the alarm"
oci monitoring alarm get --alarm-id $ALARM_ID

echo "Retrieve history for the alarm"
oci monitoring alarm-history-collection get-alarm-history --alarm-id $ALARM_ID

echo "List alarms in the compartment filtered by display name of the new alarm"
oci monitoring alarm list --compartment-id $COMPARTMENT_ID --display-name "$DISPLAY_NAME"

echo "List status of alarms in the compartment filtered by display name of the new alarm"
oci monitoring alarm-status list-alarms-status --compartment-id $COMPARTMENT_ID --display-name "$DISPLAY_NAME"

echo "List status of alarms in the compartment filtered by display name of the new alarm"
oci monitoring alarm-status list-alarms-status --compartment-id $COMPARTMENT_ID --display-name "$DISPLAY_NAME"

echo "Delete the alarm"
oci monitoring alarm delete --alarm-id $ALARM_ID

echo "Done"