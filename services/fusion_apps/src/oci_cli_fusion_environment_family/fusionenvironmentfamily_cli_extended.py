# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.fusion_apps.src.oci_cli_fusion_environment_family.generated import fusionenvironmentfamily_cli
from services.fusion_apps.src.oci_cli_fusion_apps.generated import fusion_apps_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci fusion-apps fusion-environment-family fusion-environment-family' -> 'oci fusion-apps fusion-environment-family'
fusionenvironmentfamily_cli.fusion_environment_family_root_group.commands.pop(fusionenvironmentfamily_cli.fusion_environment_family_group.name)
fusionenvironmentfamily_cli.fusion_environment_family_root_group.add_command(fusionenvironmentfamily_cli.change_fusion_environment_family_compartment)
fusionenvironmentfamily_cli.fusion_environment_family_root_group.add_command(fusionenvironmentfamily_cli.create_fusion_environment_family)
fusionenvironmentfamily_cli.fusion_environment_family_root_group.add_command(fusionenvironmentfamily_cli.delete_fusion_environment_family)
fusionenvironmentfamily_cli.fusion_environment_family_root_group.add_command(fusionenvironmentfamily_cli.get_fusion_environment_family)
fusionenvironmentfamily_cli.fusion_environment_family_root_group.add_command(fusionenvironmentfamily_cli.get_fusion_environment_family_subscription_detail)
fusionenvironmentfamily_cli.fusion_environment_family_root_group.add_command(fusionenvironmentfamily_cli.list_fusion_environment_families)
fusionenvironmentfamily_cli.fusion_environment_family_root_group.add_command(fusionenvironmentfamily_cli.update_fusion_environment_family)

# Move commands under 'oci fusion-apps fusion-environment-family fusion-environment-family-limits-and-usage -> oci fusion-apps fusion-environment-family-limits-and-usage'
fusionenvironmentfamily_cli.fusion_environment_family_root_group.commands.pop(fusionenvironmentfamily_cli.fusion_environment_family_limits_and_usage_group.name)
fusion_apps_service_cli.fusion_apps_service_group.add_command(fusionenvironmentfamily_cli.fusion_environment_family_limits_and_usage_group)
