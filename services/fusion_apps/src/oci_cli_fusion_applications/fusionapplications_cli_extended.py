# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.fusion_apps.src.oci_cli_fusion_applications.generated import fusionapplications_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


@cli_util.copy_params_from_generated_command(fusionapplications_cli.create_fusion_environment, params_to_exclude=['is_i_pv6_dual_stack_enabled'])
@fusionapplications_cli.fusion_environment_group.command(name=fusionapplications_cli.create_fusion_environment.name, help=fusionapplications_cli.create_fusion_environment.help)
@cli_util.option('--ipv6-dual-stack-enabled', type=click.BOOL, help=u"""Enable IPv4/IPv6 dual stack support for the environment.  Setting to true will assign an IPv6 address to the environment in addition to an IPv4 address. Default value will be false if not set""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'maintenance-policy': {'module': 'fusion_apps', 'class': 'MaintenancePolicy'}, 'additional-language-packs': {'module': 'fusion_apps', 'class': 'list[string]'}, 'rules': {'module': 'fusion_apps', 'class': 'list[Rule]'}, 'create-fusion-environment-admin-user-details': {'module': 'fusion_apps', 'class': 'CreateFusionEnvironmentAdminUserDetails'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_fusion_environment_extended(ctx, **kwargs):

    if 'ipv6_dual_stack_enabled' in kwargs:
        kwargs['is_i_pv6_dual_stack_enabled'] = kwargs['ipv6_dual_stack_enabled']
        kwargs.pop('ipv6_dual_stack_enabled')

    ctx.invoke(fusionapplications_cli.create_fusion_environment, **kwargs)


@cli_util.copy_params_from_generated_command(fusionapplications_cli.update_fusion_environment, params_to_exclude=['is_i_pv6_dual_stack_enabled'])
@fusionapplications_cli.fusion_environment_group.command(name=fusionapplications_cli.update_fusion_environment.name, help=fusionapplications_cli.update_fusion_environment.help)
@cli_util.option('--ipv6-dual-stack-enabled', type=click.BOOL, help=u"""Enable IPv4/IPv6 dual stack support for the environment.  Setting to true will assign an IPv6 address to the environment in addition to an IPv4 address.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'maintenance-policy': {'module': 'fusion_apps', 'class': 'MaintenancePolicy'}, 'additional-language-packs': {'module': 'fusion_apps', 'class': 'list[string]'}, 'rules': {'module': 'fusion_apps', 'class': 'list[Rule]'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_fusion_environment_extended(ctx, **kwargs):

    if 'ipv6_dual_stack_enabled' in kwargs:
        kwargs['is_i_pv6_dual_stack_enabled'] = kwargs['ipv6_dual_stack_enabled']
        kwargs.pop('ipv6_dual_stack_enabled')

    ctx.invoke(fusionapplications_cli.update_fusion_environment, **kwargs)
