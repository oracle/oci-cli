# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.key_management.src.oci_cli_key_management.generated import kms_service_cli
from services.key_management.src.oci_cli_kms_management.generated import kmsmanagement_cli
from services.key_management.src.oci_cli_kms_crypto.generated import kmscrypto_cli
from services.key_management.src.oci_cli_kms_vault.generated import kmsvault_cli
from oci_cli import cli_util

# move kms vault commands under kms management vault
kms_service_cli.kms_service_group.commands.pop(kmsvault_cli.kms_vault_root_group.name)
kmsvault_cli.vault_group.add_command(kmsvault_cli.vault_usage_group)
kmsmanagement_cli.kms_management_root_group.add_command(kmsvault_cli.vault_group)

cli_util.rename_command(kmsvault_cli, None, kmsvault_cli.kms_vault_root_group, "vault")
cli_util.rename_command(kmsvault_cli, kmsvault_cli.vault_group, kmsvault_cli.cancel_vault_deletion, "cancel-deletion")
cli_util.rename_command(kmsvault_cli, kmsvault_cli.vault_group, kmsvault_cli.schedule_vault_deletion, "schedule-deletion")
cli_util.rename_command(kmscrypto_cli, kms_service_cli.kms_service_group, kmscrypto_cli.kms_crypto_root_group, "crypto")
cli_util.rename_command(kmsmanagement_cli, kms_service_cli.kms_service_group, kmsmanagement_cli.kms_management_root_group, "management")

cli_util.rename_command(kmsmanagement_cli, kmsmanagement_cli.key_version_group, kmsmanagement_cli.cancel_key_version_deletion, 'cancel-deletion')
cli_util.rename_command(kmsmanagement_cli, kmsmanagement_cli.key_version_group, kmsmanagement_cli.schedule_key_version_deletion, 'schedule-deletion')
cli_util.rename_command(kmsvault_cli, kmsvault_cli.vault_group, kmsvault_cli.vault_usage_group, "usage")

# remove one nested layer from crypto commands (e.g. kms crypto encrypted-data encrypt -> kms crypto encrypt)
kmscrypto_cli.kms_crypto_root_group.commands.pop(kmscrypto_cli.encrypted_data_group.name)
kmscrypto_cli.kms_crypto_root_group.commands.pop(kmscrypto_cli.decrypted_data_group.name)
kmscrypto_cli.kms_crypto_root_group.commands.pop(kmscrypto_cli.generated_key_group.name)
kmscrypto_cli.kms_crypto_root_group.add_command(kmscrypto_cli.decrypt)
kmscrypto_cli.kms_crypto_root_group.add_command(kmscrypto_cli.encrypt)
kmscrypto_cli.kms_crypto_root_group.add_command(kmscrypto_cli.generate_data_encryption_key)

# override help text that is not provided
cli_util.override_command_short_help_and_help(kmsmanagement_cli.key_group, "Source of cryptographic material used to encrypt and decrypt data")
cli_util.override_command_short_help_and_help(kmsmanagement_cli.key_version_group, "A specific version of a Key. Each master encryption key is automatically assigned a key version")
cli_util.override_command_short_help_and_help(kmsvault_cli.vault_group, "A logical entity where Key Management creates and stores your keys")

cli_util.override_command_short_help_and_help(kmsmanagement_cli.kms_management_root_group, "Operations for managing keys and vaults.")
cli_util.override_command_short_help_and_help(kmscrypto_cli.kms_crypto_root_group, "Operations for performing data encryption, decryption and generation of data encryption keys.")
cli_util.override_command_short_help_and_help(kms_service_cli.kms_service_group, "Key Management")

cli_util.rename_command(kmsmanagement_cli, kmsmanagement_cli.key_group, kmsmanagement_cli.schedule_key_deletion, "schedule-deletion")
cli_util.rename_command(kmsmanagement_cli, kmsmanagement_cli.key_group, kmsmanagement_cli.cancel_key_deletion, "cancel-deletion")

# TODO: Potentially integrate with a specific --vault-endpoint parameter or find a way to translate a vault
# (e.g. a vault's OCID) to the relevant endpoint
cli_util.SERVICES_REQUIRING_ENDPOINTS.append("kms_crypto")
cli_util.SERVICES_REQUIRING_ENDPOINTS.append("kms_management")
