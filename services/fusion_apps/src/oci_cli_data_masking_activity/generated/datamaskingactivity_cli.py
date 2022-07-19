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


@click.command(cli_util.override('data_masking_activity.data_masking_activity_root_group.command_name', 'data-masking-activity'), cls=CommandGroupWithAlias, help=cli_util.override('data_masking_activity.data_masking_activity_root_group.help', """Use the Fusion Applications Environment Management API to manage the environments where your Fusion Applications run. For more information, see the [Fusion Applications Environment Management documentation]."""), short_help=cli_util.override('data_masking_activity.data_masking_activity_root_group.short_help', """Fusion Applications Environment Management API"""))
@cli_util.help_option_group
def data_masking_activity_root_group():
    pass


@click.command(cli_util.override('data_masking_activity.data_masking_activity_group.command_name', 'data-masking-activity'), cls=CommandGroupWithAlias, help="""Details of data masking activity.""")
@cli_util.help_option_group
def data_masking_activity_group():
    pass


fusion_apps_service_cli.fusion_apps_service_group.add_command(data_masking_activity_root_group)
data_masking_activity_root_group.add_command(data_masking_activity_group)


@data_masking_activity_group.command(name=cli_util.override('data_masking_activity.create_data_masking_activity.command_name', 'create'), help=u"""Creates a new DataMaskingActivity. \n[Command Reference](createDataMaskingActivity)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--is-resume-data-masking', type=click.BOOL, help=u"""This allows the Data Safe service to resume the previously failed data masking activity.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_data_masking_activity(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, fusion_environment_id, is_resume_data_masking):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if is_resume_data_masking is not None:
        _details['isResumeDataMasking'] = is_resume_data_masking

    client = cli_util.build_client('fusion_apps', 'data_masking_activity', ctx)
    result = client.create_data_masking_activity(
        fusion_environment_id=fusion_environment_id,
        create_data_masking_activity_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@data_masking_activity_group.command(name=cli_util.override('data_masking_activity.get_data_masking_activity.command_name', 'get'), help=u"""Gets a DataMaskingActivity by identifier \n[Command Reference](getDataMaskingActivity)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--data-masking-activity-id', required=True, help=u"""Unique DataMasking run identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'DataMaskingActivity'})
@cli_util.wrap_exceptions
def get_data_masking_activity(ctx, from_json, fusion_environment_id, data_masking_activity_id):

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    if isinstance(data_masking_activity_id, six.string_types) and len(data_masking_activity_id.strip()) == 0:
        raise click.UsageError('Parameter --data-masking-activity-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'data_masking_activity', ctx)
    result = client.get_data_masking_activity(
        fusion_environment_id=fusion_environment_id,
        data_masking_activity_id=data_masking_activity_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_masking_activity_group.command(name=cli_util.override('data_masking_activity.list_data_masking_activities.command_name', 'list'), help=u"""Returns a list of DataMaskingActivities. \n[Command Reference](listDataMaskingActivities)""")
@cli_util.option('--fusion-environment-id', required=True, help=u"""unique FusionEnvironment identifier""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]), help=u"""A filter that returns all resources that match the specified status""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'DataMaskingActivityCollection'})
@cli_util.wrap_exceptions
def list_data_masking_activities(ctx, from_json, all_pages, page_size, fusion_environment_id, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(fusion_environment_id, six.string_types) and len(fusion_environment_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-id cannot be whitespace or empty string')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'data_masking_activity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_masking_activities,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_masking_activities,
            limit,
            page_size,
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    else:
        result = client.list_data_masking_activities(
            fusion_environment_id=fusion_environment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)
