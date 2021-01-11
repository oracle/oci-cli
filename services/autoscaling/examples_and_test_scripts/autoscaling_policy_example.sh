#!/usr/bin/env bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.
# This script provides an example of how use the autoscaling policy CLI in terms of:
#   - Creating scheduled autoscaling policy
#   - Updating scheduled autoscaling policy
#   - Deleting scheduled autoscaling policy
#
# For more help with specific autoscaling commands, see:
#   oci autoscaling -h
#
# Environment variables need to be set:
#   - AUTOSCALING_CONFIGURATION_ID - Your Autoscaling Configuration OCID




set -e


if [ -d ./services/autoscaling/examples_and_test_scripts/autoscaling_example ];then
    autoscaling_example_data="services/autoscaling/examples_and_test_scripts/autoscaling_example"
elif [ -d ./autoscaling_example ];then
    autoscaling_example="./autoscaling_example"
else
    echo "Could not find autoscaling_example data files"
    exit 1
fi

# An Autoscaling policy's capacity needs to be uploaded as a JSON object. Example is provided below:
# {
#  "initial": 2,
#  "max": 3,
#  "min": 1
# }
#
# A valid example Autoscaling policy's capacity exists in autoscaling_example/capacity.json
#
# An Autoscaling policy's execution schedule needs to be uploaded as a JSON object. Example is provided below:
# {
#  "type": "cron",
#  "timezone": "UTC",
#  "expression": "* * * * *"
# }
#
# A valid example Autoscaling policy's execution schedule exists in autoscaling_example/execution_schedule.json

echo "Creating autoscaling policy."
AUTOSCALING_POLICY_ID=$(oci autoscaling policy create --auto-scaling-configuration-id $AUTOSCALING_CONFIGURATION_ID --capacity file://${autoscaling_example_data}/capacity.json --policy-type scheduled --execution-schedule file://${autoscaling_example_data}/execution_schedule.json | jq -r '."id"')
echo "Autoscaling policy created successfully."
echo AUTOSCALING_POLICY_ID


echo "waiting.."
sleep 90

echo "Updating autoscaling policy."
oci autoscaling policy update --auto-scaling-configuration-id $AUTOSCALING_CONFIGURATION_ID --auto-scaling-policy-id $AUTOSCALING_POLICY_ID --policy-type scheduled --execution-schedule file://${autoscaling_example_data}/execution_schedule.json
echo "Autoscaling policy created successfully."

echo "Deleting autoscaling policy."
oci autoscaling policy delete --auto-scaling-configuration-id $AUTOSCALING_CONFIGURATION_ID --auto-scaling-policy-id $AUTOSCALING_POLICY_ID
echo "Autoscaling policy deleted successfully."
