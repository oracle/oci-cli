#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides examples of how to create the following resources in Database Service
#    1 - CRUD operations on Backup Destination (Create, Get, Update and Delete)
#    2 - Create DbHome with Backup Destination
#    3 - Update Database with Backup Destination

# Please fill the following env variables
# COMPARTMENT_ID, VM_CLUSTER_ID, DATABASE_ID

set -e

if [[ -z "$COMPARTMENT_ID" ]];then
    echo "COMPARTMENT_ID must be defined in the environment. "
    exit 1
fi

if [[ -z "$VM_CLUSTER_ID" ]];then
    echo "VM_CLUSTER_ID must be defined in the environment. "
    exit 1
fi

if [[ -z "$DATABASE_ID" ]];then
    echo "DATABASE_ID must be defined in the environment. "
    exit 1
fi

# Below are sample values. Please update if needed.
DISPLAY_NAME="displayName"
NFSPATH="path"
UPDATEDPATH="updatedpath"
DBNAME="dbname123"
PASSWORD="DBaaS12345_#"
VERSION="18.0.0.0"

##############################################################################BackupDestination##############################################################################

echo 'Starting Backup Destination Examples'

echo 'Create Backup Destination...'
CREATE_BACKUP_DESTINATION=$(oci db backup-destination create-nfs-details --compartment-id $COMPARTMENT_ID --display-name $DISPLAY_NAME --local-mount-point-path $NFSPATH)

BACKUP_DESTINATION_ID=$(jq -r '.data.id' <<< "$CREATE_BACKUP_DESTINATION")

echo "Created BackupDestination with OCID:"
echo $CREATE_BACKUP_DESTINATION

echo "Get BackupDestination"
oci db backup-destination get --backup-destination-id $BACKUP_DESTINATION_ID

echo "Update Backup Destination"
oci db backup-destination update --backup-destination-id $BACKUP_DESTINATION_ID --local-mount-point-path $UPDATEDPATH
echo "Updated path"

echo "Create Db home with Backup Destination"
oci db database create --db-name $DBNAME --admin-password $PASSWORD --db-version $VERSION --vm-cluster-id $VM_CLUSTER_ID --backup-destination '[{"id":"BackupDestinationOCID","type":"TYPE"}]'

echo "Update Database with Backup Destination"
oci db database update --backup-destination '[{"id":"BackupDestinationOCID","type":"TYPE"}]' --database-id $DATABASE_ID

echo "Delete Backup Destination"
oci db backup-destination delete --backup-destination-id $BACKUP_DESTINATION_ID