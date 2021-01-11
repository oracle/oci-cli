#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides example of how to launch DB System with Fault Domains

# The following variables must be populated at the top of this script:
#   * The compartment ID where the Database system will be created
#   * The availability domain where the Database system will be launched
#   * The fault domains is where the Db Nodes are placed
#   * Subnet Id of the subnet the DB system is associated with
#   * Bacup subnet Id of the subnet required for DB system that is launched 
#   * sparseDiskGroup option - True, if Sparse Diskgroup needs to be configured for dbsystem
#   * Filename of a file containing one or more public SSH keys to use for SSH access to the DB System

set -e

# Eg: COMPARTMENT_ID=""
if [[ -z "$COMPARTMENT_ID" ]];then
    echo "COMPARTMENT_ID must be defined in the environment. "
    exit 1
fi

# Eg: AVAILABILITY_DOMAIN=""
if [[ -z "$AVAILABILITY_DOMAIN" ]];then
    echo "AVAILABILITY_DOMAIN must be defined in the environment. "
    exit 1
fi

# Eg: FAULT_DOMAINS="[\"FAULT-DOMAIN-1\"]"
if [[ -z "$FAULT_DOMAINS" ]];then
    echo "FAULT_DOMAINS must be defined in the environment. "
    exit 1
fi

# Eg: SUBNET_ID=""
if [[ -z "$SUBNET_ID" ]];then
    echo "SUBNET_ID must be defined in the environment. "
    exit 1
fi

# Eg: DBSYSTEM_SHAPE="VM.Standard1.1"
if [[ -z "$DBSYSTEM_SHAPE" ]];then
    echo "DBSYSTEM_SHAPE must be defined in the environment. "
    exit 1
fi

# Eg: HOSTNAME="cli-example-db-host"
if [[ -z "$HOSTNAME" ]];then
    echo "HOSTNAME must be defined in the environment. "
    exit 1
fi

# Eg: CPU="2"
if [[ -z "$CPU" ]];then
    echo "CPU must be defined in the environment. "
    exit 1
fi

# Eg: DB_EDITION="ENTERPRISE_EDITION_EXTREME_PERFORMANCE"
if [[ -z "$DB_EDITION" ]];then
    echo "DB_EDITION must be defined in the environment. "
    exit 1
fi

# Eg: DISPLAY_NAME="displayName"
if [[ -z "$DISPLAY_NAME" ]];then
    echo "DISPLAY_NAME must be defined in the environment. "
    exit 1
fi

# Eg: ADMIN_PASSWORD="DBaaS12345_#"
if [[ -z "$ADMIN_PASSWORD" ]];then
    echo "ADMIN_PASSWORD must be defined in the environment. "
    exit 1
fi

# Eg: DB_NAME="testdb"
if [[ -z "$DB_NAME" ]];then
    echo "DB_NAME must be defined in the environment. "
    exit 1
fi

# Eg: DB_VERSION="12.2.0.1"
if [[ -z "$DB_VERSION" ]];then
    echo "DB_VERSION must be defined in the environment. "
    exit 1
fi

# Eg: SSH_KEYS_FILE=""
if [[ -z "$SSH_KEYS_FILE" ]];then
    echo "SSH_KEYS_FILE must be defined in the environment. "
    exit 1
fi
##############################################################################AutonomousDataWarehouse##############################################################################

echo 'Starting Launch DB System Examples'

echo 'Create DB System with VM shape...'
LAUNCH_DBSYSTEM=$(oci db system launch -c $COMPARTMENT_ID --availability-domain $AVAILABILITY_DOMAIN --subnet-id $SUBNET_ID \
                    --shape $DBSYSTEM_SHAPE --hostname $HOSTNAME --cpu-core-count $CPU --database-edition $DB_EDITION \
                    --display-name $DISPLAY_NAME --fault-domains $FAULT_DOMAINS\
                    --admin-password $ADMIN_PASSWORD --db-name $DB_NAME --db-version $DB_VERSION --ssh-authorized-keys-file $SSH_KEYS_FILE) 

DBSYSTEM_ID=$(jq -r '.data.id' <<< "$LAUNCH_DBSYSTEM")

echo "Created DBSYSTEM on VM with OCID:"
echo $DBSYSTEM_ID

echo 'Get VM DB System'
oci db system get --db-system-id $DBSYSTEM_ID

echo 'Terminate VM DB System'
oci db system terminate --db-system-id $DBSYSTEM_ID
echo 'Terminated VM DB System'

echo 'End of Lauch DB System on VM Examples.'
