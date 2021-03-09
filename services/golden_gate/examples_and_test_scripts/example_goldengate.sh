#!/usr/bin/env bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# This script provides a basic example of how to use the Email Service in the CLI.
# It will demonstrate:
#
#   * Creating, retrieving, updating, moving, listing, and deleting database registrations
#   * Creating, retrieving, updating, moving, listing, and deleting deployments
#   * Creating, retrieving, updating, moving, listing, and deleting deployment-backups
#
# The following three variables must be populated from the environment:
#
#   * TENANCY_ID: The tenancy ID where the resources will be created
#   * COMPARTMENT_ID: The compartment ID where resources will be created
#   * TARGET_COMPARTMENT_ID: The compartment ID where resources will be moved to
#
# This script will create and delete these resources:
#
#   * DB1, DB2: Two Database Registrations
#   * DEP1: A deployment
#
# Requirements for running this script:
#   - OCI CLI v2.4.42 or later (you can check this by running oci --version)
#   - region set in the ~/.oci/config DEFAULT profile
#   - jq (https://stedolan.github.io/jq/) for JSON querying of CLI output. This useful utility may also
#     be used to help cater to scenarios which can't be wholly addressed by the --query option in the CLI

set -e

if [ "${TENANCY_ID}" == "" ]; then
  echo $0: "TENANCY_ID must be defined in the environment"
  exit 1
fi

if [ "${COMPARTMENT_ID}" == "" ]; then
  echo $0: "COMPARTMENT_ID must be defined in the environment"
  exit 1
fi

#if [ "${TARGET_COMPARTMENT_ID}" == "" ]; then
#  echo $0: "TARGET_COMPARTMENT_ID must be defined in the environment"
#  exit 1
#fi

export OCI_CLI_SUPPRESS_FILE_PERMISSIONS_WARNING=True

BORDER="=========================================="

function print_header() {
    echo $BORDER
    echo $1
    echo $BORDER
}

print_header "Database Registration Operations"
echo "Creating Database Registration"
export DISPLAY_NAME="DBReg_Test1"
export ALIAS_NAME="DB1"
export USERNAME="DBUSER"
export PASSWORD="DBPASS"
export SUBNET_ID="ocid1.subnet.oc1.phx.aaaaaaaarspo574lwnih7zgjzk4fcdqttxfh2ih3n7gfwcyjwadazyd6lb2q"
export FQDN="db1.mydomain.com"
RESPONSE=$(oci goldengate database-registration create \
         --config-file ${OCI_CLI_CONFIG_FILE} \
         -c ${COMPARTMENT_ID} \
         --display-name ${DISPLAY_NAME} \
         --alias-name ${ALIAS_NAME} \
         --username ${USERNAME} \
         --password ${PASSWORD} \
         --subnet-id ${SUBNET_ID} \
         --fqdn ${FQDN} \
         --wait-for-state SUCCEEDED)
RESP1=$(sed '/^Action/d' <<< "${RESPONSE}")
ID=$(jq -r '.data.resources[0].identifier' <<< "${RESP1}")

echo "Getting database-registration"
oci goldengate database-registration get \
         --config-file ${OCI_CLI_CONFIG_FILE} \
         --database-registration-id ${ID}

echo "Updating database-registration"
oci goldengate database-registration update \
         --config-file ${OCI_CLI_CONFIG_FILE} \
         --database-registration-id ${ID} \
         --description "Updated description" \
         --wait-for-state SUCCEEDED

echo "Listing database-registration"
oci goldengate database-registration list \
         --config-file ${OCI_CLI_CONFIG_FILE} \
         -c ${COMPARTMENT_ID} 

echo "Deleting database-registration"
oci goldengate database-registration delete \
         --config-file ${OCI_CLI_CONFIG_FILE} \
         --database-registration-id ${ID} \
         --wait-for-state SUCCEEDED \
         --force

print_header "Deployment Operations"
echo "Creating Deployment"
export DISPLAY_NAME="Deployment_1"
export SUBNET_ID="ocid1.subnet.oc1.phx.aaaaaaaarspo574lwnih7zgjzk4fcdqttxfh2ih3n7gfwcyjwadazyd6lb2q"
export LICENSE_MODEL="LICENSE_INCLUDED"
export CPU_CORE_COUNT="1"
export AUTO_SCALE_ENABLED="True"
export DEPLOYMENT_NAME="DEP1"
export ADMIN_USERNAME="ADMINUSER"
export ADMIN_PASSWORD="AdminPass!2"
export CERTIFICATE_FILE="test_certificate.pem"
export PRIVATE_KEY_FILE="test_private_key.pem"

echo " Making Certificate file"
rm -f ${PRIVATE_KEY_FILE} ${CERTIFICATE_FILE}
openssl req -newkey rsa:2048 -nodes -sha256 -keyout ${PRIVATE_KEY_FILE} -x509 -days 365 -out ${CERTIFICATE_FILE} -subj '/C=US/ST=WA/L=Seattle/O=Test/CN=www.example.com'

echo "Create Deployment"
RESPONSE=$(oci goldengate deployment create \
         --config-file ${OCI_CLI_CONFIG_FILE} \
         -c ${COMPARTMENT_ID} \
         --display-name ${DISPLAY_NAME} \
         --cpu-core-count ${CPU_CORE_COUNT} \
         --is-auto-scaling-enabled ${AUTO_SCALE_ENABLED} \
         --license-model ${LICENSE_MODEL} \
         --is-public False \
         --fqdn "www.example.com" \
         --subnet-id ${SUBNET_ID} \
         --deployment-name ${DEPLOYMENT_NAME} \
         --admin-username ${ADMIN_USERNAME} \
         --admin-password ${ADMIN_PASSWORD} \
         --certificate-file ${CERTIFICATE_FILE} \
         --private-key-file ${PRIVATE_KEY_FILE} \
         --wait-for-state FAILED \
         --wait-for-state SUCCEEDED)
RESP1=$(sed '/^Action/d' <<< "${RESPONSE}")
ID=$(jq -r '.data.resources[0].identifier' <<< "${RESP1}")

echo "Getting deployment"
oci goldengate deployment get \
         --config-file ${OCI_CLI_CONFIG_FILE} \
         --deployment-id ${ID}

echo "Updating deployment"
oci goldengate deployment update \
         --config-file ${OCI_CLI_CONFIG_FILE} \
         --deployment-id ${ID} \
         --description "Updated description" \
         --force \
         --wait-for-state SUCCEEDED

echo "Listing deployment"
oci goldengate deployment list \
         --config-file ${OCI_CLI_CONFIG_FILE} \
         -c ${COMPARTMENT_ID} 

echo "Deleting deployment"
oci goldengate deployment delete \
         --config-file ${OCI_CLI_CONFIG_FILE} \
         --deployment-id ${ID} \
         --force \
         --wait-for-state SUCCEEDED

echo "Complete."
