# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.vault.src.oci_cli_vaults.generated import vaults_cli
from oci_cli import cli_util

cli_util.rename_command(vaults_cli, vaults_cli.secret_group, vaults_cli.create_secret_base64_secret_content_details, "create-base64")
cli_util.rename_command(vaults_cli, vaults_cli.secret_group, vaults_cli.update_secret_base64_secret_content_details, "update-base64")
vaults_cli.secret_group.commands.pop(vaults_cli.create_secret.name)
cli_util.rename_command(vaults_cli, vaults_cli.secret_version_group, vaults_cli.schedule_secret_version_deletion, "schedule-deletion")
cli_util.rename_command(vaults_cli, vaults_cli.secret_version_group, vaults_cli.cancel_secret_version_deletion, "cancel-deletion")
