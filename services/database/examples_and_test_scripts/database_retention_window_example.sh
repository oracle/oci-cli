#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

set -e
############################################################################ Backup Retention Window ##############################################################################
# This field of the backup config can be set/updated in 3 places - 1) launch dbsystem, 2) create dbhome and 3) update dataabse
# launch DbSystem
# Please fill the following env variables
# AVAILABILITY_DOMAIN
# SUBNET_ID
# COMPARTMENT_ID
# SSH_KEYS_FILE


if [[ -z "$AVAILABILITY_DOMAIN" ]];then
    echo "AVAILABILITY_DOMAIN must be defined in the environment. "
    exit 1
fi

if [[ -z "$SUBNET_ID" ]];then
    echo "SUBNET_ID must be defined in the environment. "
    exit 1
fi

if [[ -z "$COMPARTMENT_ID" ]];then
    echo "COMPARTMENT_ID must be defined in the environment. "
    exit 1
fi

if [[ -z "$SSH_KEYS_FILE" ]];then
    echo "SSH_KEYS_FILE must be defined in the environment. "
    exit 1
fi

# Below are sample values. Please update if needed.
DBSYSTEM_SHAPE="BM.DenseIO2.52"
HOST_NAME="cli-example-db-host"
CPU="2"
DB_EDITION="ENTERPRISE_EDITION_EXTREME_PERFORMANCE"
DISPLAY_NAME="displayName"
ADMIN_PASSWORD="DBaaS12345_#"
DB_NAME="cli-db-name"
DB_VERSION="12.2.0.1"

RETENTION_WINDOW=7
echo 'Launching DbSystem with Backup Retention Window as '
echo $RETENTION_WINDOW


LAUNCH_DBSYSTEM=$(oci db system launch --compartment-id $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN --subnet-id $SUBNET_ID \
                    --shape $DBSYSTEM_SHAPE --hostname $HOST_NAME --cpu-core-count $CPU --database-edition $DB_EDITION \
                    --display-name $DISPLAY_NAME --admin-password $ADMIN_PASSWORD --db-name $DB_NAME --db-version $DB_VERSION \
                     --ssh-authorized-keys-file $SSH_KEYS_FILE --wait-for-state AVAILABLE --recovery-window-in-days $RETENTION_WINDOW --auto-backup-enabled)

DBSYSTEM_ID=$(jq -r '.data.id' <<< "$LAUNCH_DBSYSTEM")

# get database
echo "Get Database"
LIST_DATABASE=$(oci db database list --db-system-id $DBSYSTEM_ID --compartment-id $COMPARTMENT_ID)
DATABASE_ID=$(jq -r '.data[0].id' <<< "$LIST_DATABASE")
echo $DATABASE_ID

# create database
RETENTION_WINDOW2=14
echo 'Creating Database with Backup Retention Window as '
echo $RETENTION_WINDOW2

CREATE_DBHOME=$(oci db database create --db-system-id $DBSYSTEM_ID --wait-for-state AVAILABLE --admin-password $ADMIN_PASSWORD --db-name DB_NAME2 \
--db-version DB_VERSION --recovery-window-in-days $RETENTION_WINDOW2 --auto-backup-enabled)

DB_HOME=$(jq -r '.data.id' <<< "$CREATE_DBHOME")
echo "Created DbHome with ID"
echo $DB_HOME

# update Database
RETENTION_WINDOW3=10
echo 'Updating Database Backup Retention Window to '
echo $RETENTION_WINDOW3

oci db database update --database-id $DATABASE_ID --wait-for-state AVAILABLE --recovery-window-in-days $RETENTION_WINDOW3

oci db system terminate --db-system-id $DBSYSTEM_ID
