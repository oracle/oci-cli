#!/bin/bash
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides examples of how to create the following resources in Database Service
#    1 - Autonomous Database Cross Region Autonomous Data Guard Standby
#    2 - Autonomous Database
#    3 - Clone Autonomous Database
#    4 - Clone Autonomous Database from Backup
#    5 - Clone Autonomous Database from Timestamp
#    6 - Refreshable Clone for Autonomous Database

# Please fill the following env variables
#
# COMPARTMENT_ID
# ADMIN_PASSWORD
#
# Please fill the following env variables for ADB Create Cross Region Autonomous Data Guard Standby
#
# SOURCEID
#

# 1 - Create Cross Region Autonomous Data Guard Standby
echo 'Create Cross Region Autonomous Data Guard Standby...'
CREATE_STANDBY=$(oci db autonomous-database create-adb-cross-region-data-guard-details -c $COMPARTMENT_ID --source-id $source-id --wait-for-state AVAILABLE)

STANDBY_ADB_ID=$(jq -r '.data.id' <<< "$CREATE_STANDBY")

echo 'Created standby with OCID:'
echo $STANDBY_ADB_ID

# Getting the peer ids from the standby

GET_ADB=$(oci db autonomous-database get --autonomous-database-id $STANDBY_ADB_ID)

PEER_IDS=$(jq -r '.data["peer-db-ids"]' <<< "GET_ADB")

echo 'Peer ADB OCID:'
echo $PEER_IDS

# 2 - Create Autonomous Database
echo 'Create Autonomous Database...'

# Below are sample values - please update if needed
CPU_CORE_COUNT=1
DATA_STORAGE_SIZE_IN_TBS=1
LICENSE_TYPE="LICENSE_INCLUDED"

CREATE_DATABASE=$(oci db autonomous-database create -c $COMPARTMENT_ID --admin-password $ADMIN_PASSWORD --db-name 'exampleAdb' --cpu-core-count $CPU_CORE_COUNT --data-storage-size-in-tbs $DATA_STORAGE_SIZE_IN_TBS --license-model $LICENSE_TYPE --wait-for-state AVAILABLE)
DATABASE_ID=$(jq -r '.data.id' <<< "$CREATE_DATABASE")

echo 'Autonomous Database OCID:'
echo $DATABASE_ID

# 3 - Clone Autonomous Database
echo 'Clone Autonomous Database...'

# Below are sample values - please update if needed
CLONE_TYPE="FULL"
CPU_CORE_COUNT=1
DATA_STORAGE_SIZE_IN_TBS=1
LICENSE_TYPE="LICENSE_INCLUDED"

CLONE_DATABASE=$(oci db autonomous-database create-from-clone --source-id $DATABASE_ID --clone-type=$CLONE_TYPE -c $COMPARTMENT_ID --admin-password $ADMIN_PASSWORD --db-name 'clonedAdb' --cpu-core-count $CPU_CORE_COUNT --data-storage-size-in-tbs $DATA_STORAGE_SIZE_IN_TBS --license-model $LICENSE_TYPE --wait-for-state AVAILABLE)
CLONE_ID=$(jq -r '.data.id' <<< "$CLONE_DATABASE")

echo 'Autonomous Database Clone OCID:'
echo $CLONE_ID

# 4 - Clone Autonomous Database from backup
echo 'Clone Autonomous Database from backup...'

# Creating a backup for an ADB to clone from
BACKUP=$(oci db autonomous-database-backup create --autonomous-database-id DATABASE_ID --wait-for-state ACTIVE)
BACKUP_ID=$(jq -r '.data.id' <<< "$BACKUP")

echo 'Autonomous Database Backup OCID:'
echo $BACKUP_ID

# Cloning from the backup

# Below are sample values - please update if needed
CLONE_TYPE="FULL"
CPU_CORE_COUNT=1
DATA_STORAGE_SIZE_IN_TBS=1
LICENSE_TYPE="LICENSE_INCLUDED"

CLONE_FROM_BACKUP_DATABASE=$(oci db autonomous-database create-from-backup-id --autonomous-database-backup-id $BACKUP_ID --clone-type=$CLONE_TYPE -c $COMPARTMENT_ID --admin-password $ADMIN_PASSWORD --db-name 'backupAdb' --cpu-core-count $CPU_CORE_COUNT --data-storage-size-in-tbs $DATA_STORAGE_SIZE_IN_TBS --license-model $LICENSE_TYPE --wait-for-state AVAILABLE)
CLONE_FROM_BACKUP_ID=$(jq -r '.data.id' <<< "$CLONE_FROM_BACKUP_DATABASE")

echo 'Autonomous Database Clone from Backup OCID:'
echo $CLONE_FROM_BACKUP_ID

# 5 - Clone Autonomous Database clone from timestamp
echo 'Clone Autonomous Database Clone from timestamp...'

# Below are sample values - please update if needed
CLONE_TYPE="FULL"
CPU_CORE_COUNT=1
DATA_STORAGE_SIZE_IN_TBS=1
LICENSE_TYPE="LICENSE_INCLUDED"
TIMESTAMP="2017-09-15T20:30:00.123456Z"

CLONE_FROM_TIMESTAMP_DATABASE=$(oci db autonomous-database create-from-backup-timestamp --timestamp $TIMESTAMP --clone-type=$CLONE_TYPE -c $COMPARTMENT_ID --admin-password $ADMIN_PASSWORD --db-name 'timestampAdb' --cpu-core-count $CPU_CORE_COUNT --data-storage-size-in-tbs $DATA_STORAGE_SIZE_IN_TBS --license-model $LICENSE_TYPE --wait-for-state AVAILABLE)
CLONE_FROM_TIMESTAMP_ID=$(jq -r '.data.id' <<< "$CLONE_FROM_TIMESTAMP_DATABASE")

echo 'Autonomous Database Clone from Timestamp OCID:'
echo $CLONE_FROM_TIMESTAMP_ID

# 6 - Refreshable Clone for Autonomous Database
echo 'Refreshable Clone for Autonomous Database...'
CPU_CORE_COUNT=1
DATA_STORAGE_SIZE_IN_TBS=1
LICENSE_TYPE="LICENSE_INCLUDED"

REFRESHABLE_CLONE=$(oci db autonomous-database create-refreshable-clone --source-id $DATABASE_ID --refreshable-mode 'MANUAL' -c $COMPARTMENT_ID --db-name 'refreshableAdb' --cpu-core-count $CPU_CORE_COUNT --data-storage-size-in-tbs $DATA_STORAGE_SIZE_IN_TBS --license-model $LICENSE_TYPE --wait-for-state AVAILABLE)
REFRESHABLE_CLONE_ID=$(jq -r '.data.id' <<< "$REFRESHABLE_CLONE")

echo 'Refreshable Clone for Autonomous Database OCID:'
echo $REFRESHABLE_CLONE_ID

