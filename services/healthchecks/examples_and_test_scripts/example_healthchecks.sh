#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the DNS service in the CLI. The two variables at the beginning of the script must be specified accordingly:
#
#   * COMPARTMENT_ID: The OCID of the compartment you want to use HealthChecks with
#
# Requirements for running this script:
#   - OCI CLI v2.4.44 or later (you can check this by running oci --version)
#   - jq for JSON parsing

# Please fill the following env variables
# COMPARTMENT_ID
# NEW_COMPARTMENT_ID

set -e

if [[ -z "$COMPARTMENT_ID" ]];then
    echo "COMPARTMENT_ID must be defined in the environment. "
    exit 1
fi

if [[ -z "$NEW_COMPARTMENT_ID" ]];then
    echo "NEW_COMPARTMENT_ID must be defined in the environment. "
    exit 1
fi

BORDER="=========================================="

function print_header() {
    echo $BORDER
    echo $1
    echo $BORDER
}

# List all vantage points:
print_header "Listing all vantage points"
oci health-checks vantage-point list

# List HTTP monitors within our compartment:
print_header "Listing existing HTTP monitors"
oci health-checks http-monitor list --compartment-id $COMPARTMENT_ID

# Create a new HTTP monitor letting service pick vantage points:
print_header "Creating example HTTP monitor in $COMPARTMENT_ID"

EXAMPLE_HTTP=`oci health-checks http-monitor create --compartment-id $COMPARTMENT_ID \
--display-name "Example HTTP test" \
--targets '["www.example.com"]' \
--protocol HTTP \
--interval-in-seconds 60`
echo $EXAMPLE_HTTP
#Pull out the {data: {id}}
EXAMPLE_HTTP_ID=`echo $EXAMPLE_HTTP | jq '.data.id' -r`

print_header "Created HTTP monitor id $EXAMPLE_HTTP_ID, full JSON return:"
echo $EXAMPLE_HTTP

# Create a new HTTP monitor setting vantage points:
# This is just to show how to set the vantage points complex type:
#
# EXAMPLE_HTTP_VPS=`oci health-checks http-monitor create --compartment-id $COMPARTMENT_ID \
# --display-name "Example HTTP test" \
# --targets '["www.example.com"]' \
# --protocol HTTP \
# --vantage-point-names '["goo-chs", "azr-ord"]' \
# --interval-in-seconds 60`

# Update the monitor:
print_header "Disabling the HTTP monitor $EXAMPLE_HTTP_ID"
oci health-checks http-monitor update --monitor-id $EXAMPLE_HTTP_ID \
--is-enabled false

# Retrieve results list:
# NOTE: This can take 60+ seconds to have results.
print_header "List results for example HTTP monitor $EXAMPLE_HTTP_ID"
oci health-checks http-probe-result list --probe-configuration-id $EXAMPLE_HTTP_ID

# Change compartment:
echo "changing compartment of http-monitor"
oci health-checks http-monitor change-compartment --monitor-id $EXAMPLE_HTTP_ID --compartment-id ${NEW_COMPARTMENT_ID}

# Delete the example monitor
print_header "Deleting example HTTP monitor $EXAMPLE_HTTP_ID"
oci health-checks http-monitor delete --monitor-id $EXAMPLE_HTTP_ID --force


########
# Ping monitor examples. Just like HTTP, but ping.
########

#List ping monitors within our compartment:
print_header "Listing existing ping monitors"
oci health-checks ping-monitor list --compartment-id $COMPARTMENT_ID

# Create a new ping monitor letting service pick vantage points:
print_header "Creating example ping monitor in $COMPARTMENT_ID"

EXAMPLE_PING=`oci health-checks ping-monitor create --compartment-id $COMPARTMENT_ID \
--display-name "Example ping test" \
--targets '["www.example.com"]' \
--protocol ICMP \
--interval-in-seconds 60`

#Pull out the {data: {id}}
EXAMPLE_PING_ID=`echo $EXAMPLE_PING | jq '.data.id' -r`

print_header "Created ping monitor id $EXAMPLE_PING_ID, full JSON return:"
echo $EXAMPLE_PING

# Update the monitor:
print_header "Disabling the ping monitor $EXAMPLE_PING_ID"
oci health-checks ping-monitor update --monitor-id $EXAMPLE_PING_ID \
--is-enabled false

# Retrieve results list:
# NOTE: This can take 60+ seconds to have results.
print_header "List results for example ping monitor $EXAMPLE_PING_ID"
oci health-checks ping-probe-result list --probe-configuration-id $EXAMPLE_PING_ID

# Change compartment:
echo "changing compartment of ping-monitor"
oci health-checks ping-monitor change-compartment --monitor-id $EXAMPLE_PING_ID --compartment-id ${NEW_COMPARTMENT_ID}

# Delete the example monitor
print_header "Deleting example ping monitor $EXAMPLE_PING_ID"
oci health-checks ping-monitor delete --monitor-id $EXAMPLE_PING_ID --force