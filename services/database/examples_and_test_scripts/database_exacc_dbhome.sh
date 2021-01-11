#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides example of how to launch DB System using backup ID
# The following variables must be populated at the top of this script:
#   * A VmCluster OCID
#   * A region
#   Please fill the following env variables:
#   * VM_CLUSTER_ID
#   The script also honors the following env variables but if they are absent values will be automatically generated:
#   * REGION
#       A region identifier
#   * DB_NAME
#       The DbName of te database to be created
#   * DB_UNIQUE_NAME
#       The DbUniqueName of the database to be created
#   * DB_VERSION
#       The version of the database
#   * DB_PASSWORD
#       The admin password of the database to be created

# Usage: ./database_exacc_dbhome.sh

if [[ -z "$VM_CLUSTER_ID" ]];then
    echo "VM_CLUSTER_ID must be defined in the environment. "
    exit 1
fi

if [[ -z "REGION" ]];then
    echo "REGION must be defined in the environment. "
    exit 1
fi

DB_NAME=${DB_NAME:=aaa$RANDOM}
DB_UNIQUE_NAME=${DB_UNIQUE_NAME:=${DB_NAME}_aaa$RANDOM}
DB_PASSWORD=${DB_PASSWORD:=saaBB33__$RANDOM}
DB_VERSION=${DB_VERSION:="18.0.0.0"}

echo "Create the DbHome ${DB_NAME} in ${VM_CLUSTER_ID}"
DB_HOME_RESPONSE=$(oci --region ${REGION} db database create --db-name ${DB_NAME} --admin-password ${DB_PASSWORD} --db-version ${DB_VERSION} --vm-cluster-id ${VM_CLUSTER_ID})

# Extract COMPARTMENT_ID from response (needed for list)
COMPARTMENT_ID=$(echo ${DB_HOME_RESPONSE} | sed 's/.*"compartment-id"\s*:\s*\"\(ocid[^\"]\+\).*/\1/g')

# Extract DB_HOME_ID from response (needed for get)
DB_HOME_ID=$(echo ${DB_HOME_RESPONSE} | sed 's/.*"id"\s*:\s*\"\(ocid[^\"]\+\).*/\1/g')

echo ${DB_HOME_RESPONSE}

echo "Get the DbHome ${DB_HOME_ID}"
oci --region ${REGION} db database get --database-id ${DB_HOME_ID}

echo "List the DbHomes in ${VM_CLUSTER_ID} and compartment id ${COMPARTMENT_ID}"
oci --region ${REGION}  db database list --compartment-id ${COMPARTMENT_ID} --vm-cluster-id ${VM_CLUSTER_ID}

