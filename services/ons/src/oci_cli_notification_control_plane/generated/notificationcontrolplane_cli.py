# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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
from services.ons.src.oci_cli_ons.generated import ons_service_cli


@click.command(cli_util.override('notification_control_plane.notification_control_plane_root_group.command_name', 'notification-control-plane'), cls=CommandGroupWithAlias, help=cli_util.override('notification_control_plane.notification_control_plane_root_group.help', """Use the Notifications API to broadcast messages to distributed components by topic, using a publish-subscribe pattern.
For information about managing topics, subscriptions, and messages, see [Notifications Overview]."""), short_help=cli_util.override('notification_control_plane.notification_control_plane_root_group.short_help', """Notifications API"""))
@cli_util.help_option_group
def notification_control_plane_root_group():
    pass


@click.command(cli_util.override('notification_control_plane.notification_topic_group.command_name', 'notification-topic'), cls=CommandGroupWithAlias, help="""The properties that define a topic. For general information about topics, see [Notifications Overview].""")
@cli_util.help_option_group
def notification_topic_group():
    pass


ons_service_cli.ons_service_group.add_command(notification_control_plane_root_group)
notification_control_plane_root_group.add_command(notification_topic_group)


@notification_topic_group.command(name=cli_util.override('notification_control_plane.change_topic_compartment.command_name', 'change-compartment'), help=u"""Moves a topic into a different compartment within the same tenancy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60. \n[Command Reference](changeTopicCompartment)""")
@cli_util.option('--topic-id', required=True, help=u"""The [OCID] of the topic to move.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to move the specified topic or subscription to.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_topic_compartment(ctx, from_json, topic_id, compartment_id, if_match):

    if isinstance(topic_id, six.string_types) and len(topic_id.strip()) == 0:
        raise click.UsageError('Parameter --topic-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('ons', 'notification_control_plane', ctx)
    result = client.change_topic_compartment(
        topic_id=topic_id,
        change_topic_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@notification_topic_group.command(name=cli_util.override('notification_control_plane.create_topic.command_name', 'create-topic'), help=u"""Creates a topic in the specified compartment. For general information about topics, see [Managing Topics and Subscriptions].

For the purposes of access control, you must provide the OCID of the compartment where you want the topic to reside. For information about access control and compartments, see [Overview of the IAM Service].

You must specify a display name for the topic.

All Oracle Cloud Infrastructure resources, including topics, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID). When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console. For more information, see [Resource Identifiers].

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60. \n[Command Reference](createTopic)""")
@cli_util.option('--name', required=True, help=u"""The name of the topic being created. The topic name must be unique across the tenancy. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment to create the topic in.""")
@cli_util.option('--description', help=u"""The description of the topic being created. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ons', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ons', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ons', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ons', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ons', 'class': 'NotificationTopic'})
@cli_util.wrap_exceptions
def create_topic(ctx, from_json, name, compartment_id, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ons', 'notification_control_plane', ctx)
    result = client.create_topic(
        create_topic_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@notification_topic_group.command(name=cli_util.override('notification_control_plane.delete_topic.command_name', 'delete-topic'), help=u"""Deletes the specified topic.

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60. \n[Command Reference](deleteTopic)""")
@cli_util.option('--topic-id', required=True, help=u"""The [OCID] of the topic to delete.""")
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_topic(ctx, from_json, topic_id, if_match):

    if isinstance(topic_id, six.string_types) and len(topic_id.strip()) == 0:
        raise click.UsageError('Parameter --topic-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ons', 'notification_control_plane', ctx)
    result = client.delete_topic(
        topic_id=topic_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@notification_topic_group.command(name=cli_util.override('notification_control_plane.get_topic.command_name', 'get-topic'), help=u"""Gets the specified topic's configuration information. \n[Command Reference](getTopic)""")
@cli_util.option('--topic-id', required=True, help=u"""The [OCID] of the topic to retrieve.

Transactions Per Minute (TPM) per-tenancy limit for this operation: 120.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ons', 'class': 'NotificationTopic'})
@cli_util.wrap_exceptions
def get_topic(ctx, from_json, topic_id):

    if isinstance(topic_id, six.string_types) and len(topic_id.strip()) == 0:
        raise click.UsageError('Parameter --topic-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ons', 'notification_control_plane', ctx)
    result = client.get_topic(
        topic_id=topic_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@notification_topic_group.command(name=cli_util.override('notification_control_plane.list_topics.command_name', 'list-topics'), help=u"""Lists topics in the specified compartment.

Transactions Per Minute (TPM) per-tenancy limit for this operation: 120. \n[Command Reference](listTopics)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--id', help=u"""A filter to only return resources that match the given id exactly.""")
@cli_util.option('--name', help=u"""A filter to only return resources that match the given name exactly.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the opc-next-page response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "LIFECYCLESTATE"]), help=u"""The field to sort by. Only one field can be selected for sorting.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use (ascending or descending).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETING", "CREATING"]), help=u"""Filter returned list by specified lifecycle state. This parameter is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ons', 'class': 'list[NotificationTopicSummary]'})
@cli_util.wrap_exceptions
def list_topics(ctx, from_json, all_pages, page_size, compartment_id, id, name, page, limit, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if name is not None:
        kwargs['name'] = name
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('ons', 'notification_control_plane', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_topics,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_topics,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_topics(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@notification_topic_group.command(name=cli_util.override('notification_control_plane.update_topic.command_name', 'update-topic'), help=u"""Updates the specified topic's configuration.

Transactions Per Minute (TPM) per-tenancy limit for this operation: 60. \n[Command Reference](updateTopic)""")
@cli_util.option('--topic-id', required=True, help=u"""The [OCID] of the topic to update.""")
@cli_util.option('--description', required=True, help=u"""The description of the topic. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Used for optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'ons', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ons', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ons', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ons', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ons', 'class': 'NotificationTopic'})
@cli_util.wrap_exceptions
def update_topic(ctx, from_json, force, topic_id, description, freeform_tags, defined_tags, if_match):

    if isinstance(topic_id, six.string_types) and len(topic_id.strip()) == 0:
        raise click.UsageError('Parameter --topic-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('ons', 'notification_control_plane', ctx)
    result = client.update_topic(
        topic_id=topic_id,
        topic_attributes_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
