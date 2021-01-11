#!/bin/bash
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
#
# If you wish to create a new vault with tag associated, append the following optional argument:
#
#  oci kms management vault create --compartment-id $COMPARTMENT_ID --display-name $VAULT_NAME --vault-type VIRTUAL_PRIVATE
#   --freeform-tags $FREEFORM_TAG_PAIR --defined-tags $DEFINED_TAG_PAIR --wait-for-state ACTIVE
# where you can provide one or multiple key value pairs as JSON format in --freeform-tags and --defined-tags.
#
# Here are the environment variables that need to be populated before running this script:
#    export COMPARTMENT_ID = # <The OCID of the compartment where KMS resources will be created>
#    export VAULT_NAME_NEW = # <A new name for the Vault>
#    export KEY_NAME = # <A user friendly name of Key>
#    export KEY_NAME_NEW = # <A new name for the Key>
#    export KEY_SHAPE = # <The shape of the Key. An example: '{"algorithm":"AES","length":"16"}'>
#    export PLAINTEXT = # <The Base64-Encoded plaintext that will be encrypted>
#    export FREEFORM_TAG_PAIR = # <optional freeform tag key value pair for resource creation API>
#    export FREEFORM_TAG_NEW_PAIR = # <optional different freeform tag key value pair for resource update API to append tag to existing resource>
#    export DEFINED_TAG_PAIR = # <optional defined tag namespace and key value pairs for resource creation API>
#    export LOGGING_CONTEXT = # <optional logging context for kms crypto audit logging. An example: '{"loggingContextKey":"loggingContextValue"}'>
#    export TARGET_COMPARTMENT_ID - Target compartment for key/vault move operation
#    export ALGORITHM = # <Encryption algorithm to be used to encrypt the software key. An example: 'RSA_OAEP_SHA256'>
#    export PUBLIC_KEY = # <PEM format of RSA2048/RSA3072/RSA4096 Public Key, to be used to encrypt the key.>
# Requirements for running this script:
#   - OCI CLI v2.4.31 or later (you can check this by running oci --version)
#   - Please make sure the user and tenancy used by the CLI have the appropriate permissions for these operations


set -e

if [[ -z "$FREEFORM_TAG_PAIR" || -z "$FREEFORM_TAG_NEW_PAIR" || -z "$DEFINED_TAG_PAIR" || -z "$VAULT_OCID" || -z "$COMPARTMENT_ID" || -z "$VAULT_NAME_NEW" || -z "$KEY_NAME" || -z "$KEY_NAME_NEW" || -z "$KEY_SHAPE" || -z "$PLAINTEXT" || -z "$LOGGING_CONTEXT" || -z "$TARGET_COMPARTMENT_ID" ]];then
echo "FREEFORM_TAG_PAIR, FREEFORM_TAG_NEW_PAIR, DEFINED_TAG_PAIR, VAULT_OCID, COMPARTMENT_ID, VAULT_NAME_NEW, KEY_NAME, KEY_NAME_NEW, KEY_SHAPE, PLAINTEXT, LOGGING_CONTEXT and TARGET_COMPARTMENT_ID must be defined in the environment. "
exit 1
fi

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

# Update the display name and tags of the Vault
# to reset tags you can specify empty list Eg) --freeform-tags '{}' --defined-tags '{}'
echo "Updating display name of Vault with OCID: $VAULT_OCID"
oci kms management vault update --vault-id $VAULT_OCID --display-name $VAULT_NAME_NEW --freeform-tags FREEFORM_TAG_NEW_PAIR --defined-tags $DEFINED_TAG_PAIR


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

# Update the compartment of the vault
echo "Changing compartment of the vault with OCID: $VAULT_OCID"
oci kms management vault change-compartment --key-id $KEY_OCID --compartment-id $TARGET_COMPARTMENT_ID --endpoint $MANAGEMENT_ENDPOINT
echo "Wait a bit for vault compartment to be updated"
sleep 30

# KMS Key Operations
echo " "
echo "===========================================  KMS Key Operations (oci kms management key) ==========================================="
echo " "

# Create a new Key in the Vault above, using the management-endpoint of the Vault
echo "Creating Key in Vault: $VAULT_OCID"
KEY_OCID=$(oci kms management key create --compartment-id $COMPARTMENT_ID --display-name $KEY_NAME --key-shape $KEY_SHAPE --query 'data.id' --raw-output --endpoint $MANAGEMENT_ENDPOINT) --wait-for-state ENABLED
echo "Wait a bit for Key creation to complete"

# Create another new key in the vault above that has freeform and defined tags associated to it
oci kms management key create --compartment-id $COMPARTMENT_ID --display-name $KEY_NAME --key-shape $KEY_SHAPE --freeform-tags $FREEFORM_TAG_PAIR --defined-tags $DEFINED_TAG_PAIR

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
oci kms management key disable --key-id $KEY_OCID --endpoint $MANAGEMENT_ENDPOINT --wait-for-state DISABLED

# Enable the Key
# The Key may stay in ENABLING state for a short period of time, and then transit to ENABLED state
echo "Enabling Key with OCID: $KEY_OCID"
oci kms management key enable --key-id $KEY_OCID --endpoint $MANAGEMENT_ENDPOINT --wait-for-state ENABLED

# Schedule deletion for the Key
# The Key may stay in SCHEDULING_DELETION state for a short period of time, and then transit to PENDING_DELETION state
echo "Scheduling Key deletion with OCID: $KEY_OCID"
oci kms management key schedule-deletion --key-id $KEY_OCID --endpoint $MANAGEMENT_ENDPOINT --wait-for-state PENDING_DELETION

# Cancel deletion for the Key
# The Key may stay in CANCELING_DELETION state for a short period of time, and then transit to ENABLED state
echo "Canceling Key deletion with OCID: $KEY_OCID"
oci kms management key cancel-deletion --key-id $KEY_OCID --endpoint $MANAGEMENT_ENDPOINT --wait-for-state ENABLED

# Update the compartment of the key
echo "Changing compartment of the key with OCID: $KEY_OCID"
oci kms management key change-compartment --key-id $KEY_OCID --compartment-id $TARGET_COMPARTMENT_ID --endpoint $MANAGEMENT_ENDPOINT
echo "Wait a bit for Key compartment to be updated"
sleep 30

# Update the display name and tags of the Key
echo "Updating DisplayName and tags of Key with OCID: $KEY_OCID"
oci kms management key update --key-id $KEY_OCID --display-name $KEY_NAME_NEW --freeform-tags $FREEFORM_TAG_NEW_PAIR --defined-tags $DEFINED_TAG_PAIR --endpoint $MANAGEMENT_ENDPOINT

echo " "
echo "===========================================  KMS Crypto Operations (oci kms crypto)  ==========================================="
echo " "

# Encrypt some data with the Key, the plaintext must be base64 encoded
# Passing in a loggingContext here, which will be added to the Audit logs (if Audit Logging is enabled)
echo "Encrypting plaintext with Key with OCID: $KEY_OCID"
oci kms crypto encrypt --key-id $KEY_OCID --plaintext $PLAINTEXT --logging-context $LOGGING_CONTEXT --endpoint $CRYPTO_ENDPOINT
CIPHERTEXT=$(oci kms crypto encrypt --key-id $KEY_OCID --plaintext $PLAINTEXT --endpoint $CRYPTO_ENDPOINT --query 'data.ciphertext' --raw-output)

# Decrypt the data we just encrypted previously
echo "Decrypting ciphertext with Key with OCID: $KEY_OCID"
oci kms crypto decrypt --key-id $KEY_OCID --ciphertext $CIPHERTEXT --endpoint $CRYPTO_ENDPOINT

# Generate DataEncryptionKey (A key that you can use to encrypt or decrypt data).
echo "Generating DataEncryptionKey (DEK) with Key with OCID: $KEY_OCID"
oci kms crypto generate-data-encryption-key --key-id $KEY_OCID --include-plaintext-key true --key-shape $KEY_SHAPE --endpoint $CRYPTO_ENDPOINT

# Export Key from KMS. (This operation is only supported for Software Keys)
echo "Export Key with OCID: $KEY_OCID"
oci kms crypto key export --algorithm $ALGORITHM --key-id $KEY_OCID --public-key $PUBLIC_KEY --endpoint $CRYPTO_ENDPOINT