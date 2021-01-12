#!/usr/bin/env bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.
# This script provides an example of how to use the kms management CLI in terms of:
#   - Backup vault using bucket name, namespace and object name
#   - Backup vault using uri
#   - Restore vault using bucket name, namespace and object name
#   - Restore vault using uri
#   - restore vault from file
#   - Backup key using bucket name, namespace and object name
#   - Backup key using uri
#   - Restore key using bucket name, namespace and object name
#   - Restore key using uri
#   - restore key from file
#
# For more help with specific kms management commands, see:
#   oci kms management -h
#
# For more help with kms management key commands, see:
#   oci kms management key -h
#
# For more help with kms management vault commands, see:
#   oci kms management vault -h
#
# Requirements for running this script:
#   - OCI CLI v2.4.41 or later (you can check this by running oci --version)
# ToDo: Fill and add the following variables into your environment variable
# export COMPARTMENT_ID=
# export VAULT_NAME_NEW="CliVault"
# export VAULT_OCID=<<Vault should be active>>
# export KEY_OCID=""
# export BUCKET_NAME=
# export NAMESPACE=
# export OBJECT_NAME=
# export OBJECT_LOCATION_URI=
# export KEY_BINARY_FILE_EXAMPLE_LOCATION=
# export VAULT_BINARY_FILE_EXAMPLE_LOCATION=


set -e

echo ""
echo "===========================================  KMS Vault backup (oci kms management vault)  ==========================================="
echo ""

echo "Backup KMS Vault with OCID: $VAULT_OCID using bucket name, namespace and object name"
oci kms management vault backup --vault-id $VAULT_OCID --bucket-name $BUCKET_NAME --namespace $NAMESPACE --object-name $OBJECT_NAME

echo "Backup KMS Vault with OCID: $VAULT_OCID using object location uri"
oci kms management vault backup --vault-id $VAULT_OCID --uri $OBJECT_LOCATION_URI

echo ""
echo "===========================================  KMS Vault restore (oci kms management vault)  ==========================================="
echo ""

echo "Restore KMS Vault with OCID: $VAULT_OCID using bucket name, namespace and object name"
oci kms management vault restore --compartment-id $COMPARTMENT_ID --bucket-name $BUCKET_NAME --namespace $NAMESPACE --object-name $OBJECT_NAME

echo "Restore KMS Vault with OCID: $VAULT_OCID using object location uri"
oci kms management vault restore --compartment-id $COMPARTMENT_ID --uri $OBJECT_LOCATION_URI

echo "Restore KMS Vault with OCID: $VAULT_OCID from file"
oci kms management vault restore-from-file --compartment-id $COMPARTMENT_ID --restore-vault-from-file-location $VAULT_BINARY_FILE_EXAMPLE_LOCATION


echo ""
echo "===========================================  KMS Key backup (oci kms management key)  ==========================================="
echo ""

echo "Backup KMS Key with OCID: $KEY_OCID using bucket name, namespace and object name"
oci kms management key backup --key-id $KEY_OCID --bucket-name $BUCKET_NAME --namespace $NAMESPACE --object-name $OBJECT_NAME

echo "Backup KMS Key with OCID: $KEY_OCID using object location uri"
oci kms management key backup --key-id $KEY_OCID --uri $OBJECT_LOCATION_URI

echo ""
echo "===========================================  KMS Key restore (oci kms management key)  ==========================================="
echo ""

echo "Restore KMS Key with OCID: $KEY_OCID using bucket name, namespace and object name"
oci kms management key restore --bucket-name $BUCKET_NAME --namespace $NAMESPACE --object-name $OBJECT_NAME

echo "Restore KMS Key with OCID: $KEY_OCID using object location uri"
oci kms management key restore --uri $OBJECT_LOCATION_URI

echo "Restore KMS Key with OCID: $KEY_OCID from file"
oci kms management key restore-from-file --restore-key-from-file-location $KEY_BINARY_FILE_EXAMPLE_LOCATION

