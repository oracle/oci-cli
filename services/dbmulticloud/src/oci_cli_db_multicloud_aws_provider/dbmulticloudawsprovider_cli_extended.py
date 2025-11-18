# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.dbmulticloud.src.oci_cli_db_multicloud_aws_provider.generated import dbmulticloudawsprovider_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

from services.dbmulticloud.src.oci_cli_dbmulticloud.generated import dbmulticloud_service_cli

# Move commands under 'oci dbmulticloud db-multicloud-aws-provider' -> 'oci dbmulticloud'
dbmulticloud_service_cli.dbmulticloud_service_group.commands.pop(dbmulticloudawsprovider_cli.db_multicloud_aws_provider_root_group.name)
dbmulticloud_service_cli.dbmulticloud_service_group.add_command(dbmulticloudawsprovider_cli.oracle_db_aws_identity_connector_group)
dbmulticloud_service_cli.dbmulticloud_service_group.add_command(dbmulticloudawsprovider_cli.oracle_db_aws_key_group)
