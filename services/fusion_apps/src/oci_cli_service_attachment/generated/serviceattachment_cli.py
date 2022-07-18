# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.fusion_apps.src.oci_cli_fusion_apps.generated import fusion_apps_service_cli


@click.command(cli_util.override('service_attachment.service_attachment_root_group.command_name', 'service-attachment'), cls=CommandGroupWithAlias, help=cli_util.override('service_attachment.service_attachment_root_group.help', """Use the Fusion Applications Environment Management API to manage the environments where your Fusion Applications run. For more information, see the [Fusion Applications Environment Management documentation]."""), short_help=cli_util.override('service_attachment.service_attachment_root_group.short_help', """Fusion Applications Environment Management API"""))
@cli_util.help_option_group
def service_attachment_root_group():
    pass


@click.command(cli_util.override('service_attachment.service_attachment_group.command_name', 'service-attachment'), cls=CommandGroupWithAlias, help="""Description of ServiceAttachment.""")
@cli_util.help_option_group
def service_attachment_group():
    pass


fusion_apps_service_cli.fusion_apps_service_group.add_command(service_attachment_root_group)
service_attachment_root_group.add_command(service_attachment_group)


@service_attachment_group.command(name=cli_util.override('service_attachment.get_service_attachment.command_name', 'get'), help=u"""Gets a Service Attachment by identifier \n[Command Reference](getServiceAttachment)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--service-attachment-id', required=True, help=u"""OCID of the Service Attachment""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'ServiceAttachment'})
@cli_util.wrap_exceptions
def get_service_attachment(ctx, from_json, fusion_environment_id, service_attachment_id):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    if isinstance(service_attachment_id, six.string_types) and len(service_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --service-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'service_attachment', ctx)
    result = client.get_service_attachment(
        fusion_environment_id=fusion_environment_id,
        service_attachment_id=service_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@service_attachment_group.command(name=cli_util.override('service_attachment.list_service_attachments.command_name', 'list'), help=u"""Returns a list of service attachments. \n[Command Reference](listServiceAttachments)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter that returns all resources that match the specified lifecycle state.""")
@cli_util.option('--service-instance-type', type=custom_types.CliCaseInsensitiveChoice(["DIGITAL_ASSISTANT", "INTEGRATION_CLOUD", "ANALYTICS_WAREHOUSE", "VBCS", "VISUAL_BUILDER_STUDIO"]), help=u"""A filter that returns all resources that match the specified lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'ServiceAttachmentCollection'})
@cli_util.wrap_exceptions
def list_service_attachments(ctx, from_json, all_pages, page_size, fusion_environment_id, display_name, lifecycle_state, service_instance_type, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if service_instance_type is not None:
        kwargs['service_instance_type'] = service_instance_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'service_attachment', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_service_attachments,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_service_attachments,
            limit,
            page_size,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    else:
        result = client.list_service_attachments(
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
