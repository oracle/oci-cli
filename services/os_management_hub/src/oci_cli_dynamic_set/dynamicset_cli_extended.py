# Copyright (c) 2016, 2023, Oracle and/or its affiliates.
#
# This software is dual-licensed to you under the Universal Permissive License
# (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl and Apache License
# 2.0 as shown at https://www.apache.org/licenses/LICENSE-2.0. You may choose
# either license.
#
# If you elect to accept the software under the Apache License, Version 2.0,
# the following applies:
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8
import click  # noqa: F401
import json  # noqa: F401
from services.os_management_hub.src.oci_cli_dynamic_set.generated import dynamicset_cli
from services.os_management_hub.src.oci_cli_os_management_hub.generated import os_management_hub_service_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

# oci os-management-hub dynamic-set list-managed-instances-in -> oci os-management-hub dynamic-set list-managed-instances
cli_util.rename_command(dynamicset_cli, dynamicset_cli.dynamic_set_group, dynamicset_cli.list_managed_instances_in_dynamic_set, "list-managed-instances")


# Move commands under 'oci os-management-hub dynamic-set dynamic-set' -> 'oci os-management-hub dynamic-set'
dynamicset_cli.dynamic_set_root_group.commands.pop(dynamicset_cli.dynamic_set_root_group.name)
os_management_hub_service_cli.os_management_hub_service_group.commands.pop(dynamicset_cli.dynamic_set_root_group.name)
os_management_hub_service_cli.os_management_hub_service_group.add_command(dynamicset_cli.dynamic_set_group)


# oci os-management-hub dynamic-set update-packages - Allow JSON list for --update-types
@cli_util.copy_params_from_generated_command(dynamicset_cli.update_packages_on_dynamic_set, params_to_exclude=['update_types'], copy_from_json=False)
@dynamicset_cli.dynamic_set_group.command(name=dynamicset_cli.update_packages_on_dynamic_set.name, help=dynamicset_cli.update_packages_on_dynamic_set.help)
@cli_util.option('--update-types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The types of updates to be applied.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'managed-instances': {'module': 'os_management_hub', 'class': 'list[string]'}, 'update-types': {'module': 'os_management_hub', 'class': 'list[string]'}, 'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'managed-instances': {'module': 'os_management_hub', 'class': 'list[string]'}, 'work-request-details': {'module': 'os_management_hub', 'class': 'WorkRequestDetails'}, 'update-types': {'module': 'os_management_hub', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_packages_on_dynamic_set_extended(ctx, **kwargs):
    ctx.invoke(dynamicset_cli.update_packages_on_dynamic_set, **kwargs)
