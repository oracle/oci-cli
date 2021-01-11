#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides example of how to launch DB System on Exadata with Sparse Diskgroup option

# The following variables must be populated at the top of this script:
#   * The compartment ID where the Database system will be created
#   * The availability domain where the Database system will be launched
#   * Subnet Id of the subnet the DB system is associated with
#   * Bacup subnet Id of the subnet required for DB system that is launched on Exadata
#   * sparseDiskGroup option - True, if Sparse Diskgroup needs to be configured for Exadata dbsystem
#   * Filename of a file containing one or more public SSH keys to use for SSH access to the DB System

set -e

COMPARTMENT_ID=""
AVAILABILITY_DOMAIN=""
SUBNET_ID=""
DBSYSTEM_SHAPE="Exadata.Quarter2.92"
HOSTNAME="cli-example-db-host"
CPU="2"
DB_EDITION="ENTERPRISE_EDITION_EXTREME_PERFORMANCE"
DISPLAY_NAME="displayName"
BACKUP_SUBNET_ID=""
SPARSE_DISKGROUP=""
ADMIN_PASSWORD="DBaaS12345_#"
DB_NAME="testdb"
DB_VERSION="12.2.0.1"
TIME_ZONE="US/Pacific"
SSH_KEYS_FILE=""

##############################################################################AutonomousDataWarehouse##############################################################################

echo 'Starting Launch DB System Examples'

echo 'Create DB System with Exadata shape...'
LAUNCH_DBSYSTEM=$(oci db system launch -c $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN --subnet-id $SUBNET_ID \
                    --shape $DBSYSTEM_SHAPE --hostname $HOSTNAME --cpu-core-count $CPU --database-edition $DB_EDITION \
                    --display-name $DISPLAY_NAME --backup-subnet-id $BACKUP_SUBNET_ID --sparse-diskgroup $SPARSE_DISKGROUP \
                    --admin-password $ADMIN_PASSWORD --db-name $DB_NAME --db-version $DB_VERSION --time-zone $TIME_ZONE --ssh-authorized-keys-file $SSH_KEYS_FILE)

DBSYSTEM_ID=$(jq -r '.data.id' <<< "$LAUNCH_DBSYSTEM")

echo "Created DBSYSTEM on Exadata with OCID:"
echo $DBSYSTEM_ID

echo 'Get Exadata DB System'
oci db system get --db-system-id $DBSYSTEM_ID

echo 'Terminate Exadata DB System'
oci db system terminate --db-system-id $DBSYSTEM_ID
echo 'Terminated Exadata DB System'

echo 'End of Lauch DB System on Exadata Examples.'
