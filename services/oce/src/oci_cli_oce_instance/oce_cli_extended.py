# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.oce.src.oci_cli_oce_instance.generated import oceinstance_cli
from oci_cli import cli_util
from oci_cli import custom_types
from oci_cli import json_skeleton_utils
import click

# Make sure these commands don't have the "--all-pages" option.
# oci oce oce-instance list --compartment-id, --all-pages, --display-name
# oci oce work-request list --compartment-id, --all-pages, --resource-id
# oci oce work-request-error list --work-request-id, --all-pages
# oci oce work-request-log-entry list --work-request-id, --all-pages
oceinstance_cli.oce_root_group.short_help = "Oracle Content and Experience"
oceinstance_cli.oce_instance_group.commands.pop(oceinstance_cli.list_oce_instances.name)
oceinstance_cli.work_request_group.commands.pop(oceinstance_cli.list_work_requests.name)
oceinstance_cli.work_request_error_group.commands.pop(oceinstance_cli.list_work_request_errors.name)
oceinstance_cli.work_request_log_entry_group.commands.pop(oceinstance_cli.list_work_request_logs.name)

cli_util.update_param_help(oceinstance_cli.create_oce_instance, 'identity_stripe', """Details of the identity stripe used for OceInstance, including name of the Identity Cloud Service instance in my services to be used and value of the Identity Cloud Service tenancy. Example: `{\"serviceName\": \"secondstripe\"; \"tenancy\": \"idcs-8416ebdd0d674f84803f4193cce026e9\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)


@cli_util.copy_params_from_generated_command(oceinstance_cli.list_oce_instances, params_to_exclude=['all', 'all_pages'])
@oceinstance_cli.oce_instance_group.command(name='list', help=oceinstance_cli.list_oce_instances.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oce', 'class': 'list[OceInstanceSummary]'})
@cli_util.wrap_exceptions
def list_oce_instances(ctx, **kwargs):
    ctx.invoke(oceinstance_cli.list_oce_instances, **kwargs)


@cli_util.copy_params_from_generated_command(oceinstance_cli.list_work_requests, params_to_exclude=['all', 'all_pages'])
@oceinstance_cli.work_request_group.command(name='list', help=oceinstance_cli.list_work_requests.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oce', 'class': 'list[WorkRequest]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, **kwargs):
    ctx.invoke(oceinstance_cli.list_work_requests, **kwargs)


@cli_util.copy_params_from_generated_command(oceinstance_cli.list_work_request_errors, params_to_exclude=['all', 'all_pages'])
@oceinstance_cli.work_request_error_group.command(name='list', help=oceinstance_cli.list_work_request_errors.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oce', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, **kwargs):
    ctx.invoke(oceinstance_cli.list_work_request_errors, **kwargs)


@cli_util.copy_params_from_generated_command(oceinstance_cli.list_work_request_logs, params_to_exclude=['all', 'all_pages'])
@oceinstance_cli.work_request_log_entry_group.command(name='list', help=oceinstance_cli.list_work_request_logs.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'oce', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, **kwargs):
    ctx.invoke(oceinstance_cli.list_work_request_logs, **kwargs)
