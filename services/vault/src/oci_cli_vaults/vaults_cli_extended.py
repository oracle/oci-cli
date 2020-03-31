# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from services.vault.src.oci_cli_vaults.generated import vaults_cli
from oci_cli import cli_util

cli_util.rename_command(vaults_cli, vaults_cli.secret_group, vaults_cli.create_secret_base64_secret_content_details, "create-base64")
cli_util.rename_command(vaults_cli, vaults_cli.secret_group, vaults_cli.update_secret_base64_secret_content_details, "update-base64")
vaults_cli.secret_group.commands.pop(vaults_cli.create_secret.name)
cli_util.rename_command(vaults_cli, vaults_cli.secret_version_group, vaults_cli.schedule_secret_version_deletion, "schedule-deletion")
cli_util.rename_command(vaults_cli, vaults_cli.secret_version_group, vaults_cli.cancel_secret_version_deletion, "cancel-deletion")
