#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides example of how to launch DB System using backup ID
# The following variables must be populated at the top of this script:
#   * Bare metal dbsystem ocid that you want to launch a new database from backup
#   * A new Database name
#   * Admin password of the backed up database
#   * Backup ocid of the database is required for database to be launched
#   * TDE wallet password
#   Please fill the following env variables
#DB_SYSTEM_ID=""
#DB_NAME=""
#BACKUP_ID=""
#ADMIN_PASSWORD=""
#BACKUP_TDE_PASSWORD=""
##############################################################################AutonomousDataWarehouse##############################################################################
set -e
if [[ -z "$DB_SYSTEM_ID" ]];then
    echo "DB_SYSTEM_ID must be defined in the environment. OCID of the dbsystem which the database needs to be restored to is required."
    exit 1
fi

if [[ -z "$DB_NAME" ]];then
    echo 'DB_NAME can be defined in the environment. A new database name for the database that is to be restored can be provided.'
fi

if [[ -z "$BACKUP_ID" ]];then
    echo 'BACKUP_ID must be defined in the environment. OCID of the backup is required.'
    exit 1
fi

if [[ -z "$ADMIN_PASSWORD" ]];then
    echo 'ADMIN_PASSWORD must be defined in the environment. Admin password of the database is required.'
    exit 1
fi

if [[ -z "$BACKUP_TDE_PASSWORD" ]];then
    echo 'BACKUP_TDE_PASSWORD must be defined in the environment. TDE wallet password of the database is required.'
    exit 1
fi

echo 'Starting rename database during restore examples.'

echo 'Create database from backup id'
LAUNCH_DATABASE=$(oci db database create-from-backup --db-system-id $DB_SYSTEM_ID --backup-id $BACKUP_ID --admin-password $ADMIN_PASSWORD --db-name $DB_NAME \
				--backup-tde-password $ADMIN_PASSWORD)

DATABASE_ID=$(jq -r '.data.id' <<< "$LAUNCH_DATABASE")

echo "Created database on baremetal dbsystem with OCID:"
echo $DATABASE_ID

echo 'Get Database'
oci db database get --database-id $DATABASE_ID

echo 'Terminate database'
oci db system terminate --database-id $DATABASE_ID
echo 'Terminated database'

echo 'End of rename database during restore examples'