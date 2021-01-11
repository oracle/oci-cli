#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

set -e
############################################################################## VM Data Guard ##############################################################################

##Pre requisite to have VCN, Subnet and a VM Database in AVAILABLE state

# Please fill the following env variables
# AVAILABILITY_DOMAIN
# SUBNET_ID
# DATABASE_ID
# COMPARTMENT_ID

# Below are sample values. Please update if needed.
DISPLAY_NAME1="displayName"
PASSWORD1="DBaaS12345_#"
DB_SYSTEM_SHAPE="VM.Standard1.1"

if [[ -z "$AVAILABILITY_DOMAIN" ]];then
    echo "AVAILABILITY_DOMAIN must be defined in the environment. "
    exit 1
fi

if [[ -z "$SUBNET_ID" ]];then
    echo "SUBNET_ID must be defined in the environment. "
    exit 1
fi

if [[ -z "$DATABASE_ID" ]];then
    echo "DATABASE_ID must be defined in the environment. "
    exit 1
fi

if [[ -z "$COMPARTMENT_ID" ]];then
    echo "COMPARTMENT_ID must be defined in the environment. "
    exit 1
fi


# Below are sample values. Please update if needed.
HOST_NAME="cli-example-db-host"

echo 'Starting DataGuard for VM Examples'

#Step-1 Create Dataguard
echo 'Create Data Guard...'
CREATE_VMDG=$(oci db data-guard-association create with-new-db-system --database-id $DATABASE_ID  \
                    --database-admin-password $PASSWORD1 --protection-mode 'MAXIMUM_PERFORMANCE'  \
                    --transport-type 'ASYNC' --creation-type 'NewDbSystem' --display-name $DISPLAY_NAME1  \
                    --hostname $HOST_NAME --availability-domain $AVAILABILITY_DOMAIN --subnet-id $SUBNET_ID  \
                    --wait-for-state AVAILABLE)
VMDG_ID=$(jq -r '.data.id' <<< "$CREATE_VMDG")

#Step-2 Once DataGuard is AVAILABLE, do Switchover
echo 'Switchover on current primary'
SWITCHOVER_DG=$(oci db data-guard-association switchover --database-id $DATABASE_ID  --data-guard-association-id $VMDG_ID \
                    --database-admin-password $PASSWORD1 --wait-for-state AVAILABLE)

#Step-3 Failover
echo 'After switch over old primary will become standby. Failover on current standby'
FAILOVER_DG=$(oci db data-guard-association failover --database-id $DATABASE_ID  --data-guard-association-id $VMDG_ID \
                    --database-admin-password $PASSWORD1 --wait-for-state AVAILABLE)

#Step-4 Reinstate
echo 'Reinstate current primary'
REINSTATE_DG=$(oci db data-guard-association reinstate --database-id $DATABASE_ID  --data-guard-association-id $VMDG_ID \
                    --database-admin-password $PASSWORD1 --wait-for-state AVAILABLE)

############################################################################## DB VERSIONS ##############################################################################
echo 'Trying to List Oracle DB Versions for compartment and shape.'
oci db version list -c $COMPARTMENT_ID --db-system-shape $DB_SYSTEM_SHAPE
echo 'End of List Oracle DB Versions Examples.'
