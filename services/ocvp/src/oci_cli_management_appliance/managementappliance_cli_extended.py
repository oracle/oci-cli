# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.ocvp.src.oci_cli_management_appliance.generated import managementappliance_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci ocvs management-appliance management-appliance' -> 'oci ocvs management-appliance'
managementappliance_cli.management_appliance_root_group.commands.pop(managementappliance_cli.management_appliance_group.name)
managementappliance_cli.management_appliance_root_group.add_command(managementappliance_cli.create_management_appliance)
managementappliance_cli.management_appliance_root_group.add_command(managementappliance_cli.delete_management_appliance)
managementappliance_cli.management_appliance_root_group.add_command(managementappliance_cli.get_management_appliance)
managementappliance_cli.management_appliance_root_group.add_command(managementappliance_cli.list_management_appliances)
managementappliance_cli.management_appliance_root_group.add_command(managementappliance_cli.update_management_appliance)
