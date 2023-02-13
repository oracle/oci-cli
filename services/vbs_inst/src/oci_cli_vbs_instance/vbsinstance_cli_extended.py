# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.vbs_inst.src.oci_cli_vbs_instance.generated import vbsinstance_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

# oci vbstudio short help
cli_util.override_command_short_help_and_help(vbsinstance_cli.vbstudio_root_group, "VB Studio Controlplane Instance API")

# oci vbstudio vbs-instance -> oci vbstudio instance
cli_util.rename_command(vbsinstance_cli, vbsinstance_cli.vbstudio_root_group, vbsinstance_cli.vbs_instance_group, "instance")


# oci vbstudio vbs-instance-summary-collection list-vbs-instances -> oci vbstudio vbs-instance-summary-collection list
cli_util.rename_command(vbsinstance_cli, vbsinstance_cli.vbs_instance_summary_collection_group, vbsinstance_cli.list_vbs_instances, "list")


vbsinstance_cli.vbstudio_root_group.commands.pop(vbsinstance_cli.work_request_error_group.name)
vbsinstance_cli.vbstudio_root_group.commands.pop(vbsinstance_cli.work_request_log_entry_group.name)


# oci vbstudio work-request-error list -> oci vbstudio work-request-error errors
cli_util.rename_command(vbsinstance_cli, vbsinstance_cli.work_request_group, vbsinstance_cli.list_work_request_errors, "errors")
vbsinstance_cli.work_request_group.add_command(vbsinstance_cli.list_work_requests)


# oci vbstudio work-request-log-entry list-work-request-logs -> oci vbstudio work-request-log-entry logs
cli_util.rename_command(vbsinstance_cli, vbsinstance_cli.work_request_group, vbsinstance_cli.list_work_request_logs, "logs")


# Remove change-compartment from oci vbstudio vbs-instance
vbsinstance_cli.vbs_instance_group.commands.pop(vbsinstance_cli.change_vbs_instance_compartment.name)


# Move commands under 'oci vbstudio vbs-instance-summary-collection' -> 'oci vbstudio vbs-instance'
vbsinstance_cli.vbstudio_root_group.commands.pop(vbsinstance_cli.vbs_instance_summary_collection_group.name)
vbsinstance_cli.vbs_instance_group.add_command(vbsinstance_cli.list_vbs_instances)


@cli_util.copy_params_from_generated_command(vbsinstance_cli.create_vbs_instance, params_to_exclude=['is_resource_usage_agreement_granted', 'resource_compartment_id'])
@vbsinstance_cli.vbs_instance_group.command(name=vbsinstance_cli.create_vbs_instance.name, help=vbsinstance_cli.create_vbs_instance.help)
@cli_util.option('--is-cicd-authorized', type=click.BOOL, help=u"""Whether VBS is authorized to create and use resources in the customer tenancy""")
@cli_util.option('--cicd-compartment-id', help=u"""Compartment where VBS may create additional resources for the service instance""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'vbs_inst', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'vbs_inst', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_vbs_instance_extended(ctx, **kwargs):
    if 'is_cicd_authorized' in kwargs:
        kwargs['is_resource_usage_agreement_granted'] = kwargs['is_cicd_authorized']
        kwargs.pop('is_cicd_authorized')

    if 'cicd_compartment_id' in kwargs:
        kwargs['resource_compartment_id'] = kwargs['cicd_compartment_id']
        kwargs.pop('cicd_compartment_id')

    ctx.invoke(vbsinstance_cli.create_vbs_instance, **kwargs)


@cli_util.copy_params_from_generated_command(vbsinstance_cli.update_vbs_instance, params_to_exclude=['vbs_instance_id', 'is_resource_usage_agreement_granted', 'resource_compartment_id'])
@vbsinstance_cli.vbs_instance_group.command(name=vbsinstance_cli.update_vbs_instance.name, help=vbsinstance_cli.update_vbs_instance.help)
@cli_util.option('--instance-id', required=True, help=u"""unique VbsInstance identifier [required]""")
@cli_util.option('--is-cicd-authorized', type=click.BOOL, help=u"""Whether VBS is authorized to create and use resources in the customer tenancy""")
@cli_util.option('--cicd-compartment-id', help=u"""Compartment where VBS may create additional resources for the service instance""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'vbs_inst', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'vbs_inst', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_vbs_instance_extended(ctx, **kwargs):
    if 'instance_id' in kwargs:
        kwargs['vbs_instance_id'] = kwargs['instance_id']
        kwargs.pop('instance_id')

    if 'is_cicd_authorized' in kwargs:
        kwargs['is_resource_usage_agreement_granted'] = kwargs['is_cicd_authorized']
        kwargs.pop('is_cicd_authorized')

    if 'cicd_compartment_id' in kwargs:
        kwargs['resource_compartment_id'] = kwargs['cicd_compartment_id']
        kwargs.pop('cicd_compartment_id')

    ctx.invoke(vbsinstance_cli.update_vbs_instance, **kwargs)


@cli_util.copy_params_from_generated_command(vbsinstance_cli.delete_vbs_instance, params_to_exclude=['vbs_instance_id'])
@vbsinstance_cli.vbs_instance_group.command(name=vbsinstance_cli.delete_vbs_instance.name, help=vbsinstance_cli.delete_vbs_instance.help)
@cli_util.option('--instance-id', required=True, help=u"""unique VbsInstance identifier [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_vbs_instance_extended(ctx, **kwargs):
    if 'instance_id' in kwargs:
        kwargs['vbs_instance_id'] = kwargs['instance_id']
        kwargs.pop('instance_id')

    ctx.invoke(vbsinstance_cli.delete_vbs_instance, **kwargs)


@cli_util.copy_params_from_generated_command(vbsinstance_cli.get_vbs_instance, params_to_exclude=['vbs_instance_id'])
@vbsinstance_cli.vbs_instance_group.command(name=vbsinstance_cli.get_vbs_instance.name, help=vbsinstance_cli.get_vbs_instance.help)
@cli_util.option('--instance-id', required=True, help=u"""unique VbsInstance identifier [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'vbs_inst', 'class': 'VbsInstance'})
@cli_util.wrap_exceptions
def get_vbs_instance_extended(ctx, **kwargs):
    if 'instance_id' in kwargs:
        kwargs['vbs_instance_id'] = kwargs['instance_id']
        kwargs.pop('instance_id')

    ctx.invoke(vbsinstance_cli.get_vbs_instance, **kwargs)
