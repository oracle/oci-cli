# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.apiaccesscontrol.src.oci_cli_privileged_api_control.generated import privilegedapicontrol_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci apiaccesscontrol privileged-api-control privileged-api-control' -> 'oci apiaccesscontrol privileged-api-control'
privilegedapicontrol_cli.privileged_api_control_root_group.commands.pop(privilegedapicontrol_cli.privileged_api_control_group.name)
privilegedapicontrol_cli.privileged_api_control_root_group.add_command(privilegedapicontrol_cli.change_privileged_api_control_compartment)
privilegedapicontrol_cli.privileged_api_control_root_group.add_command(privilegedapicontrol_cli.create_privileged_api_control)
privilegedapicontrol_cli.privileged_api_control_root_group.add_command(privilegedapicontrol_cli.delete_privileged_api_control)
privilegedapicontrol_cli.privileged_api_control_root_group.add_command(privilegedapicontrol_cli.get_privileged_api_control)
privilegedapicontrol_cli.privileged_api_control_root_group.add_command(privilegedapicontrol_cli.update_privileged_api_control)


# Move commands under 'oci apiaccesscontrol privileged-api-control privileged-api-control-collection' -> 'oci apiaccesscontrol privileged-api-control'
privilegedapicontrol_cli.privileged_api_control_root_group.commands.pop(privilegedapicontrol_cli.privileged_api_control_collection_group.name)
privilegedapicontrol_cli.privileged_api_control_root_group.add_command(privilegedapicontrol_cli.list_privileged_api_controls)
