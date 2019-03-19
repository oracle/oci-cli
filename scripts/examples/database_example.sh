#!/bin/bash
# This script provides examples of how to create the following resources in Database Service
#    1 - Autonomous DataWarehouse
#    2 - AutonomousTransaction Processing (Autonomous Database)

# The following variables must be populated at the top of this script:
#   * The compartment ID where the Database Service resources will be created

set -e

COMPARTMENT_ID=""
DISPLAY_NAME1="displayName"
DISPLAY_NAME2="newDisplayName"
DB_NAME1="cliTest1"
DB_NAME2="cliTest2"
PASSWORD1="DBaaS12345_#"
CPU="1"
SCALED_CPU="2"
SCALED_STORAGE="2"
STORAGE="1"
LICENSE_TYPE="LICENSE_INCLUDED"
DB_SYSTEM_SHAPE="VM.Standard1.1"
CLONE_TYPE="FULL"
SOURCE_ID=""


##############################################################################AutonomousDataWarehouse##############################################################################

echo 'Starting Autonomous DataWarehouse Examples'

echo 'Create AutonomousDatawarehouse...'
CREATE_ADW=$(oci db autonomous-data-warehouse create -c $COMPARTMENT_ID --db-name $DB_NAME1 --admin-password $PASSWORD1 --cpu-core-count $CPU \
                    --data-storage-size-in-tbs $STORAGE --display-name $DISPLAY_NAME1 --license-model $LICENSE_TYPE \
                    --wait-for-state AVAILABLE)

ADW_ID=$(jq -r '.data.id' <<< "$CREATE_ADW")

echo "Created AutonomousDatawarehouse with OCID:"
echo $CREATE_ADW

echo 'Get AutonomousDatawarehouse'
oci db autonomous-data-warehouse get --autonomous-data-warehouse-id $ADW_ID

echo 'List all AutonomousDatawarehouses in compartment'
oci db autonomous-data-warehouse list --compartment-id $COMPARTMENT_ID

echo 'List all AutonomousDatawarehouses in compartment in AVAILABLE state'
oci db autonomous-data-warehouse list --compartment-id $COMPARTMENT_ID --lifecycle-state AVAILABLE

echo 'List 2 AutonomousDatawarehouses in compartment'
oci db autonomous-data-warehouse list --compartment-id $COMPARTMENT_ID --limit 2

echo 'List all AutonomousDatawarehouses in compartment with specific display name, in descending order'
oci db autonomous-data-warehouse list --compartment-id $COMPARTMENT_ID --sort-by $DISPLAY_NAME1 --sort-order DESC

echo 'Update AutonomousDatawarehouse DisplayName'
oci db autonomous-data-warehouse update --autonomous-data-warehouse-id $ADW_ID --display-name $DISPLAY_NAME2
echo 'Updated AutonomousDatawarehouse DisplayName'

echo 'Update AutonomousDatawarehouse cpuCoreCount and storage'
oci db autonomous-data-warehouse update --autonomous-data-warehouse-id $ADW_ID --data-storage-size-in-tbs $SCALED_STORAGE \
                --cpu-core-count $SCALED_CPU --wait-for-state AVAILABLE
echo 'Updated AutonomousDatawarehouse cpuCoreCount and storageSize'

echo 'Generate and download AutonomousDatawarehouse wallet'
oci db autonomous-data-warehouse generate-wallet --autonomous-data-warehouse-id $ADW_ID  --password $PASSWORD1 --file  wallet_adw.zip

echo 'Delete AutonomousDatawarehouse'
oci db autonomous-data-warehouse delete --autonomous-data-warehouse-id $ADW_ID --force --wait-for-state TERMINATED
echo 'Deleted AutonomousDatawarehouse'

echo 'Trying to Get Deleted AutonomousDatawarehouse. Should not find it.'
oci db autonomous-data-warehouse get --autonomous-data-warehouse-id $ADW_ID

echo 'End of AutonomousDatawarehouse Examples.'

##############################################################################Autonomous Transaction Processing##############################################################################

echo 'Starting Autonomous Transaction Processing Examples'

echo 'Create Autonomous Transaction Processing...'
CREATE_ATP=$(oci db autonomous-database create -c $COMPARTMENT_ID --db-name $DB_NAME2 --admin-password $PASSWORD1 --cpu-core-count $CPU \
                    --data-storage-size-in-tbs $STORAGE --display-name $DISPLAY_NAME1 --license-model $LICENSE_TYPE \
                    --wait-for-state AVAILABLE)

ADB_ID=$(jq -r '.data.id' <<< "$CREATE_ATP")

echo "Created Autonomous Transaction Processing with OCID:"
echo $CREATE_ATP

echo 'Get Autonomous Transaction Processing'
oci db autonomous-database get --autonomous-database-id $ADB_ID

echo 'List all Autonomous Transaction Processings in compartment'
oci db autonomous-database list --compartment-id $COMPARTMENT_ID

echo 'List all Autonomous Transaction Processings in compartment in AVAILABLE state'
oci db autonomous-database list --compartment-id $COMPARTMENT_ID --lifecycle-state AVAILABLE

echo 'List 2 Autonomous Transaction Processings in compartment'
oci db autonomous-database list --compartment-id $COMPARTMENT_ID --limit 2

echo 'List all Autonomous Transaction Processings in compartment with specific display name, in descending order'
oci db autonomous-database list --compartment-id $COMPARTMENT_ID --sort-by $DISPLAY_NAME1 --sort-order DESC

echo 'Update Autonomous Transaction Processing DisplayName'
oci db autonomous-database update --autonomous-database-id $ADB_ID --display-name $DISPLAY_NAME2
echo 'Updated Autonomous Transaction Processing DisplayName'

echo 'Update Autonomous Transaction Processing cpuCoreCount and storage'
oci db autonomous-database update --autonomous-database-id $ADB_ID --data-storage-size-in-tbs $SCALED_STORAGE \
                --cpu-core-count $SCALED_CPU --wait-for-state AVAILABLE
echo 'Updated Autonomous Transaction Processing cpuCoreCount and storageSize'

echo 'Generate and download AutonomousDatabase wallet'
oci db autonomous-database generate-wallet --autonomous-database-id $ADB_ID --password $PASSWORD1 --file  wallet_adb.zip

echo 'Delete Autonomous Transaction Processing'
oci db autonomous-database delete --autonomous-database-id $ADB_ID --force --wait-for-state TERMINATED
echo 'Deleted Autonomous Transaction Processing'

echo 'Trying to Get Deleted Autonomous Transaction Processing. Should not find it.'
oci db autonomous-database get --autonomous-database-id $ADB_ID

echo 'Cloning Autonomous Transaction Processing...'
CLONE_ATP=$(oci db autonomous-database create-from-clone -c $COMPARTMENT_ID --db-name $DB_NAME2 --admin-password $PASSWORD1 --cpu-core-count $CPU \
                    --data-storage-size-in-tbs $STORAGE --display-name $DISPLAY_NAME1 --license-model $LICENSE_TYPE \
                    --source-id $SOURCE_ID --clone-type $CLONE_TYPE
                    --wait-for-state AVAILABLE)

ADB_ID=$(jq -r '.data.id' <<< "CLONE_ATP")

echo "Cloning Autonomous Transaction Processing with OCID:"
echo CLONE_ATP

echo 'End of Autonomous Transaction Processing Examples.'


############################################################################## VM Data Guard ##############################################################################

##Pre requisite to have VCN, Subnet and a VM Database in AVAILABLE state
## Below are Sample values - Replace with actuals
AVAILABILITY_DOMAIN="XXIT:PHX-AD-3"
SUBNET_ID="ocid1.subnet.oc1.phx.aaaaaaaa5ydvrdwdhk7chxgy4wt5eje4fporgd7wckvzezvqbezblantmyxq"
DATABASE_ID="ocid1.database.oc1.phx.abyhqljthelork4yotrsbpiaoimbvh7heod33qp4dnsqf34gfzksmk5t4egq"

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

echo 'Trying to List Oracle DB Versions for compartment and shape.'
oci db version list -c $COMPARTMENT_ID --db-system-shape $DB_SYSTEM_SHAPE
echo 'End of List Oracle DB Versions Examples.'
