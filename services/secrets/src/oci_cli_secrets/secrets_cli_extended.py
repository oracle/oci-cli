# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from services.secrets.src.oci_cli_secrets.generated import secrets_cli
from oci_cli import cli_util

cli_util.rename_command(secrets_cli, secrets_cli.secret_bundle_version_summary_group, secrets_cli.list_secret_bundle_versions, "list-versions")
cli_util.rename_command(secrets_cli, secrets_cli.secrets_root_group, secrets_cli.secret_bundle_version_summary_group, "secret-bundle-version")
