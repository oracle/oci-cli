# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.secrets.src.oci_cli_secrets.generated import secrets_cli
from oci_cli import cli_util

cli_util.rename_command(secrets_cli, secrets_cli.secret_bundle_version_summary_group, secrets_cli.list_secret_bundle_versions, "list-versions")
cli_util.rename_command(secrets_cli, secrets_cli.secrets_root_group, secrets_cli.secret_bundle_version_summary_group, "secret-bundle-version")
secrets_cli.secrets_root_group.help += " To manage secrets, see `Secret Management (vault) <https://docs.cloud.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/vault.html>"
