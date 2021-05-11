#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

set -e

if [ "$COMPARTMENT_ID" == "" ]; then
    echo "COMPARTMENT_ID must be defined in the environment"
    exit 1
fi

if [ "$ANNOUNCEMENT_ID" == "" ]; then
    echo "ANNOUNCEMENT_ID must be defined in the environment"
    exit 1
fi

if [ "$USER_ID" == "" ]; then
    echo "USER_ID must be defined in the environment"
    exit 1
fi

oci announce announcements get --announcement-id $ANNOUNCEMENT_ID

# List Announcements
# Default page size of 100
oci announce announcements list --compartment-id $COMPARTMENT_ID
# Filter by action recommended announcement type
oci announce announcements list --compartment-id $COMPARTMENT_ID --announcement-type ACTION_RECOMMENDED
# Filter by active lifecycle state
oci announce announcements list --compartment-id $COMPARTMENT_ID --lifecycle-state ACTIVE
# Filter by active banners
oci announce announcements list --compartment-id $COMPARTMENT_ID --is-banner true
# Sort by reference ticket number
oci announce announcements list --compartment-id $COMPARTMENT_ID --sort-by referenceTicketNumber
# Sort by default order, time created, in descending order
oci announce announcements list --compartment-id $COMPARTMENT_ID --sort-order DESC

set +e
# Filter time one to be at least the current time
oci announce announcements list --compartment-id $COMPARTMENT_ID --time-one-earliest-time 2021-05-05T23:11:01.000Z
# Filter time one to be at most the current time
oci announce announcements list --compartment-id $COMPARTMENT_ID --time-one-latest-time 2021-05-05T23:11:06.000Z
set -e 

oci announce user-status get --announcement-id $ANNOUNCEMENT_ID
# Update user's announcement acknowledgement time to now
oci announce user-status update --announcement-id $ANNOUNCEMENT_ID --user-status-announcement-id $ANNOUNCEMENT_ID --user-id $USER_ID --time-acknowledged 2021-05-05T23:11:17.000Z
oci announce user-status get --announcement-id $ANNOUNCEMENT_ID
# Cleanup status
oci announce user-status update --announcement-id $ANNOUNCEMENT_ID --user-status-announcement-id $ANNOUNCEMENT_ID --user-id $USER_ID --time-acknowledged 2021-05-05T23:11:17.000Z
