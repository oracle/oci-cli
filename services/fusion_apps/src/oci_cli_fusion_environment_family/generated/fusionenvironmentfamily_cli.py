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


@click.command(cli_util.override('fusion_environment_family.fusion_environment_family_root_group.command_name', 'fusion-environment-family'), cls=CommandGroupWithAlias, help=cli_util.override('fusion_environment_family.fusion_environment_family_root_group.help', """Use the Fusion Applications Environment Management API to manage the environments where your Fusion Applications run. For more information, see the [Fusion Applications Environment Management documentation]."""), short_help=cli_util.override('fusion_environment_family.fusion_environment_family_root_group.short_help', """Fusion Applications Environment Management API"""))
@cli_util.help_option_group
def fusion_environment_family_root_group():
    pass


@click.command(cli_util.override('fusion_environment_family.fusion_environment_family_group.command_name', 'fusion-environment-family'), cls=CommandGroupWithAlias, help="""Details of a Fusion environment family. An environment family is a logical grouping of environments. The environment family defines a set of characteristics that are shared across the environments to allow consistent management and maintenance across your production, test, and development environments. For more information, see [Planning an Environment Family].""")
@cli_util.help_option_group
def fusion_environment_family_group():
    pass


@click.command(cli_util.override('fusion_environment_family.fusion_environment_family_limits_and_usage_group.command_name', 'fusion-environment-family-limits-and-usage'), cls=CommandGroupWithAlias, help="""Details of EnvironmentLimits.""")
@cli_util.help_option_group
def fusion_environment_family_limits_and_usage_group():
    pass


fusion_apps_service_cli.fusion_apps_service_group.add_command(fusion_environment_family_root_group)
fusion_environment_family_root_group.add_command(fusion_environment_family_group)
fusion_environment_family_root_group.add_command(fusion_environment_family_limits_and_usage_group)


@fusion_environment_family_group.command(name=cli_util.override('fusion_environment_family.change_fusion_environment_family_compartment.command_name', 'change-compartment'), help=u"""Moves a FusionEnvironmentFamily into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeFusionEnvironmentFamilyCompartment)""")
@cli_util.option('--fusion-environment-family-id', required=True, help=u"""The unique identifier (OCID) of the FusionEnvironmentFamily.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_fusion_environment_family_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, fusion_environment_family_id, compartment_id, if_match):

    if isinstance(fusion_environment_family_id, six.string_types) and len(fusion_environment_family_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-family-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('fusion_apps', 'fusion_environment_family', ctx)
    result = client.change_fusion_environment_family_compartment(
        fusion_environment_family_id=fusion_environment_family_id,
        change_fusion_environment_family_compartment_details=_details,
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


@fusion_environment_family_group.command(name=cli_util.override('fusion_environment_family.create_fusion_environment_family.command_name', 'create'), help=u"""Creates a new FusionEnvironmentFamily. \n[Command Reference](createFusionEnvironmentFamily)""")
@cli_util.option('--display-name', required=True, help=u"""A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where the environment family is located.""")
@cli_util.option('--subscription-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of the IDs of the applications subscriptions that are associated with the environment family.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--family-maintenance-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--opc-provision-option', help=u"""For Oracle internal use only.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'family-maintenance-policy': {'module': 'fusion_apps', 'class': 'FamilyMaintenancePolicy'}, 'subscription-ids': {'module': 'fusion_apps', 'class': 'list[string]'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'family-maintenance-policy': {'module': 'fusion_apps', 'class': 'FamilyMaintenancePolicy'}, 'subscription-ids': {'module': 'fusion_apps', 'class': 'list[string]'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_fusion_environment_family(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, subscription_ids, family_maintenance_policy, freeform_tags, defined_tags, opc_provision_option):

    kwargs = {}
    if opc_provision_option is not None:
        kwargs['opc_provision_option'] = opc_provision_option
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id
    _details['subscriptionIds'] = cli_util.parse_json_parameter("subscription_ids", subscription_ids)

    if family_maintenance_policy is not None:
        _details['familyMaintenancePolicy'] = cli_util.parse_json_parameter("family_maintenance_policy", family_maintenance_policy)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('fusion_apps', 'fusion_environment_family', ctx)
    result = client.create_fusion_environment_family(
        create_fusion_environment_family_details=_details,
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


@fusion_environment_family_group.command(name=cli_util.override('fusion_environment_family.delete_fusion_environment_family.command_name', 'delete'), help=u"""Deletes a FusionEnvironmentFamily resource by identifier \n[Command Reference](deleteFusionEnvironmentFamily)""")
@cli_util.option('--fusion-environment-family-id', required=True, help=u"""The unique identifier (OCID) of the FusionEnvironmentFamily.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_fusion_environment_family(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, fusion_environment_family_id, if_match):

    if isinstance(fusion_environment_family_id, six.string_types) and len(fusion_environment_family_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-family-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_environment_family', ctx)
    result = client.delete_fusion_environment_family(
        fusion_environment_family_id=fusion_environment_family_id,
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
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@fusion_environment_family_group.command(name=cli_util.override('fusion_environment_family.get_fusion_environment_family.command_name', 'get'), help=u"""Retrieves a fusion environment family identified by its OCID. \n[Command Reference](getFusionEnvironmentFamily)""")
@cli_util.option('--fusion-environment-family-id', required=True, help=u"""The unique identifier (OCID) of the FusionEnvironmentFamily.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'FusionEnvironmentFamily'})
@cli_util.wrap_exceptions
def get_fusion_environment_family(ctx, from_json, fusion_environment_family_id):

    if isinstance(fusion_environment_family_id, six.string_types) and len(fusion_environment_family_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-family-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_environment_family', ctx)
    result = client.get_fusion_environment_family(
        fusion_environment_family_id=fusion_environment_family_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fusion_environment_family_limits_and_usage_group.command(name=cli_util.override('fusion_environment_family.get_fusion_environment_family_limits_and_usage.command_name', 'get'), help=u"""Gets the number of environments (usage) of each type in the fusion environment family, as well as the limit that's allowed to be created based on the group's associated subscriptions. \n[Command Reference](getFusionEnvironmentFamilyLimitsAndUsage)""")
@cli_util.option('--fusion-environment-family-id', required=True, help=u"""The unique identifier (OCID) of the FusionEnvironmentFamily.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'FusionEnvironmentFamilyLimitsAndUsage'})
@cli_util.wrap_exceptions
def get_fusion_environment_family_limits_and_usage(ctx, from_json, fusion_environment_family_id):

    if isinstance(fusion_environment_family_id, six.string_types) and len(fusion_environment_family_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-family-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_environment_family', ctx)
    result = client.get_fusion_environment_family_limits_and_usage(
        fusion_environment_family_id=fusion_environment_family_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fusion_environment_family_group.command(name=cli_util.override('fusion_environment_family.get_fusion_environment_family_subscription_detail.command_name', 'get-fusion-environment-family-subscription-detail'), help=u"""Gets the subscription details of an fusion environment family. \n[Command Reference](getFusionEnvironmentFamilySubscriptionDetail)""")
@cli_util.option('--fusion-environment-family-id', required=True, help=u"""The unique identifier (OCID) of the FusionEnvironmentFamily.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'SubscriptionDetail'})
@cli_util.wrap_exceptions
def get_fusion_environment_family_subscription_detail(ctx, from_json, fusion_environment_family_id):

    if isinstance(fusion_environment_family_id, six.string_types) and len(fusion_environment_family_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-family-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('fusion_apps', 'fusion_environment_family', ctx)
    result = client.get_fusion_environment_family_subscription_detail(
        fusion_environment_family_id=fusion_environment_family_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@fusion_environment_family_group.command(name=cli_util.override('fusion_environment_family.list_fusion_environment_families.command_name', 'list'), help=u"""Returns a list of FusionEnvironmentFamilies. \n[Command Reference](listFusionEnvironmentFamilies)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--fusion-environment-family-id', help=u"""The ID of the fusion environment family in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter that returns all resources that match the specified lifecycle state.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'fusion_apps', 'class': 'FusionEnvironmentFamilyCollection'})
@cli_util.wrap_exceptions
def list_fusion_environment_families(ctx, from_json, all_pages, page_size, compartment_id, fusion_environment_family_id, display_name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if fusion_environment_family_id is not None:
        kwargs['fusion_environment_family_id'] = fusion_environment_family_id
    if display_name is not None:
        kwargs['display_name'] = display_name
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
    client = cli_util.build_client('fusion_apps', 'fusion_environment_family', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_fusion_environment_families,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_fusion_environment_families,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_fusion_environment_families(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@fusion_environment_family_group.command(name=cli_util.override('fusion_environment_family.update_fusion_environment_family.command_name', 'update'), help=u"""Updates the FusionEnvironmentFamily \n[Command Reference](updateFusionEnvironmentFamily)""")
@cli_util.option('--fusion-environment-family-id', required=True, help=u"""The unique identifier (OCID) of the FusionEnvironmentFamily.""")
@cli_util.option('--display-name', help=u"""A friendly name for the environment family. The name must contain only letters, numbers, dashes, and underscores. Can be changed later.""")
@cli_util.option('--family-maintenance-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--subscription-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of the IDs of the applications subscriptions that are associated with the environment family.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'family-maintenance-policy': {'module': 'fusion_apps', 'class': 'UpdateFamilyMaintenancePolicyDetails'}, 'subscription-ids': {'module': 'fusion_apps', 'class': 'list[string]'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'family-maintenance-policy': {'module': 'fusion_apps', 'class': 'UpdateFamilyMaintenancePolicyDetails'}, 'subscription-ids': {'module': 'fusion_apps', 'class': 'list[string]'}, 'freeform-tags': {'module': 'fusion_apps', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'fusion_apps', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_fusion_environment_family(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, fusion_environment_family_id, display_name, family_maintenance_policy, subscription_ids, freeform_tags, defined_tags, if_match):

    if isinstance(fusion_environment_family_id, six.string_types) and len(fusion_environment_family_id.strip()) == 0:
        raise click.UsageError('Parameter --fusion-environment-family-id cannot be whitespace or empty string')
    if not force:
        if family_maintenance_policy or subscription_ids or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to family-maintenance-policy and subscription-ids and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if family_maintenance_policy is not None:
        _details['familyMaintenancePolicy'] = cli_util.parse_json_parameter("family_maintenance_policy", family_maintenance_policy)

    if subscription_ids is not None:
        _details['subscriptionIds'] = cli_util.parse_json_parameter("subscription_ids", subscription_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('fusion_apps', 'fusion_environment_family', ctx)
    result = client.update_fusion_environment_family(
        fusion_environment_family_id=fusion_environment_family_id,
        update_fusion_environment_family_details=_details,
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
