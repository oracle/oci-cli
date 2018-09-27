#!/bin/bash
# This script provides basic examples on the usage of the KMS service with the CLI.
#
# These examples assume you already have a Vault in ACTIVE state. If you need to create a new Vault, please
# refer to the command in the comments section of this file. Please keep in mind that KMS does not support immediate
# deletion of Vaults because of the high risk; instead, you need to schedule the deletion of a Vault and a
# retention period of 7-30 days will be enforced before the Vault is deleted. During the retention period, you
# can cancel the deletion and the Vault will be ACTIVE again. Be careful before creating a Vault to avoid
# unnecessary expenses.
#
# As a reference, here is the command you can use to create a new Vault with OCI CLI, replace the compartment-id and
# display-name with your own values:
#
#  oci kms management vault create --compartment-id $COMPARTMENT_ID --display-name $VAULT_NAME --vault-type VIRTUAL_PRIVATE --wait-for-state ACTIVE
#
# Here are some parameters that need to be specified first:
#
#   * COMPARTMENT_ID: The OCID of the compartment where KMS resources will be created
#   * VAULT_NAME_NEW: A new name for the Vault
#   * KEY_NAME: A user friendly name of Key
#   * KEY_NAME_NEW: A new name for the Key
#   * KEY_SHAPE: The shape of the Key. An example: '{"algorithm":"AES","length":"16"}'
#   * PLAINTEXT: The Base64-Encoded plaintext that will be encrypted
#
# Requirements for running this script:
#   - OCI CLI v2.4.31 or later (you can check this by running oci --version)
#   - Please make sure the user and tenancy used by the CLI have the appropriate permissions for these operations

set -e

# Fill up the values of the following parameters
VAULT_OCID=""
COMPARTMENT_ID=""
VAULT_NAME_NEW=""
KEY_NAME=""
KEY_NAME_NEW=""
# Use this one by default or replace with yours
KEY_SHAPE='{"algorithm":"AES","length":"16"}'
PLAINTEXT=""

# KMS Vault Operations
echo ""
echo "===========================================  KMS Vault Operations (oci kms management vault)  ==========================================="
echo ""

# Retrieve the details of the existing Vault in ACTIVE state.
# The Vault may be in CREATING state for a short period of time and then transit to ACTIVE state
echo "Get KMS Vault with OCID: $VAULT_OCID"
oci kms management vault get --vault-id $VAULT_OCID
MANAGEMENT_ENDPOINT=$(oci kms management vault get --vault-id $VAULT_OCID --query 'data."management-endpoint"' --raw-output)
CRYPTO_ENDPOINT=$(oci kms management vault get --vault-id $VAULT_OCID --query 'data."crypto-endpoint"' --raw-output)

# Update the display name of the Vault
echo "Updating display name of Vault with OCID: $VAULT_OCID"
oci kms management vault update --vault-id $VAULT_OCID --display-name $VAULT_NAME_NEW

# List all Vaults in the compartment
echo "Listing all Vaults in the compartment with OCID: $COMPARTMENT_ID"
oci kms management vault list --compartment-id $COMPARTMENT_ID --all

# Schedule deletion of the Vault.
# An optional parameter, time-of-deletion, can be used to specify when the deletion shall happen. Here the parameter is
# ignored and the default time (30 days after the time of request) will be used.
# The Vault may stay in SCHEDULING_DELETION state for a short period of time, and then transit to PENDING_DELETION state
echo "Scheduling deletion of Vault with OCID: $VAULT_OCID"
oci kms management vault schedule-deletion --vault-id $VAULT_OCID
echo "Wait a bit for Vault deletion to be scheduled"
sleep 30

# Cancel the deletion of the Vault
# The Vault may stay in CANCELLING_DELETION state for a short period of time, and then transit to ACTIVE state
echo "Cancelling deletion of Vault with OCID: $VAULT_OCID"
oci kms management vault cancel-deletion --vault-id $VAULT_OCID
echo "Wait a bit for Vault deletion to be cancelled"
sleep 30

# KMS Key Operations
echo " "
echo "===========================================  KMS Key Operations (oci kms management key) ==========================================="
echo " "

# Create a new Key in the Vault above, using the management-endpoint of the Vault
echo "Creating Key in Vault: $VAULT_OCID"
KEY_OCID=$(oci kms management key create --compartment-id $COMPARTMENT_ID --display-name $KEY_NAME --key-shape $KEY_SHAPE --query 'data.id' --raw-output --endpoint $MANAGEMENT_ENDPOINT) --wait-for-state ENABLED
echo "Wait a bit for Key creation to complete"

# Retrieve the details of the Key
echo "Retrieving KMS Key, OCID: $KEY_OCID"
oci kms management key get --key-id $KEY_OCID --endpoint $MANAGEMENT_ENDPOINT

# List all Keys in the Vault
echo "List all Keys in Vault with OCID: $VAULT_OCID"
oci kms management key list --compartment-id $COMPARTMENT_ID --endpoint $MANAGEMENT_ENDPOINT --all

# Create a new KeyVersion of the Key. This has the same effects of rotating a Key.
echo "Creating a new KeyVersion for Key with OCID: $KEY_OCID"
oci kms management key-version create --key-id $KEY_OCID --endpoint $MANAGEMENT_ENDPOINT
echo "Wait a bit for Key-Version to be created"
sleep 30

# List all KeyVersions of the Key
echo "Listing all KeyVersions of Key with OCID: $KEY_OCID"
oci kms management key-version list --key-id $KEY_OCID --endpoint $MANAGEMENT_ENDPOINT --all

# Disable the Key
# The Key may stay in DISABLING state for a short period of time, and then transit to DISABLED state
echo "Disabling Key with OCID: $KEY_OCID"
oci kms management key disable --key-id $KEY_OCID --endpoint $MANAGEMENT_ENDPOINT
echo "Wait a bit for Key to be disabled"
sleep 30

# Enable the Key
# The Key may stay in ENABLING state for a short period of time, and then transit to ENABLED state
echo "Enabling Key with OCID: $KEY_OCID"
oci kms management key enable --key-id $KEY_OCID --endpoint $MANAGEMENT_ENDPOINT
echo "Wait a bit for Key to be enabled"
sleep 30

# Update the display name of the Key
echo "Updating DisplayName of Key with OCID: $KEY_OCID"
oci kms management key update --key-id $KEY_OCID --display-name $KEY_NAME_NEW --endpoint $MANAGEMENT_ENDPOINT

echo " "
echo "===========================================  KMS Crypto Operations (oci kms crypto)  ==========================================="
echo " "

# Encrypt some data with the Key, the plaintext must be base64 encoded
echo "Encrypting plaintext with Key with OCID: $KEY_OCID"
oci kms crypto encrypt --key-id $KEY_OCID --plaintext $PLAINTEXT --endpoint $CRYPTO_ENDPOINT
CIPHERTEXT=$(oci kms crypto encrypt --key-id $KEY_OCID --plaintext $PLAINTEXT --endpoint $CRYPTO_ENDPOINT --query 'data.ciphertext' --raw-output)

# Decrypt the data we just encrypted previously
echo "Decrypting ciphertext with Key with OCID: $KEY_OCID"
oci kms crypto decrypt --key-id $KEY_OCID --ciphertext $CIPHERTEXT --endpoint $CRYPTO_ENDPOINT

# Generate DataEncryptionKey (A key that you can use to encrypt or decrypt data).
echo "Generating DataEncryptionKey (DEK) with Key with OCID: $KEY_OCID"
oci kms crypto generate-data-encryption-key --key-id $KEY_OCID --include-plaintext-key true --key-shape $KEY_SHAPE --endpoint $CRYPTO_ENDPOINT