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
from services.mysql.src.oci_cli_mysql.generated import mysql_service_cli


@click.command(cli_util.override('mysqlaas.mysqlaas_root_group.command_name', 'mysqlaas'), cls=CommandGroupWithAlias, help=cli_util.override('mysqlaas.mysqlaas_root_group.help', """The API for the MySQL Database Service"""), short_help=cli_util.override('mysqlaas.mysqlaas_root_group.short_help', """MySQL Database Service API"""))
@cli_util.help_option_group
def mysqlaas_root_group():
    pass


@click.command(cli_util.override('mysqlaas.shape_group.command_name', 'shape'), cls=CommandGroupWithAlias, help="""The shape of the DB System. The shape determines resources to allocate to the DB System - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes.  For a description of shapes, see [DB System Shape Options].""")
@cli_util.help_option_group
def shape_group():
    pass


@click.command(cli_util.override('mysqlaas.configuration_group.command_name', 'configuration'), cls=CommandGroupWithAlias, help="""The set of MySQL variables to be used when deploying a MySQL Database Service DB System.""")
@cli_util.help_option_group
def configuration_group():
    pass


@click.command(cli_util.override('mysqlaas.version_group.command_name', 'version'), cls=CommandGroupWithAlias, help="""A supported MySQL Version.""")
@cli_util.help_option_group
def version_group():
    pass


mysql_service_cli.mysql_service_group.add_command(mysqlaas_root_group)
mysqlaas_root_group.add_command(shape_group)
mysqlaas_root_group.add_command(configuration_group)
mysqlaas_root_group.add_command(version_group)


@configuration_group.command(name=cli_util.override('mysqlaas.create_configuration.command_name', 'create'), help=u"""Creates a new Configuration. \n[Command Reference](createConfiguration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--shape-name', required=True, help=u"""The name of the associated Shape.""")
@cli_util.option('--variables', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""User-provided data about the Configuration.""")
@cli_util.option('--display-name', help=u"""The display name of the Configuration.""")
@cli_util.option('--parent-configuration-id', help=u"""The OCID of the Configuration from which the new Configuration is derived. The values in CreateConfigurationDetails.variables supersede the variables of the parent Configuration.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'variables': {'module': 'mysql', 'class': 'ConfigurationVariables'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'variables': {'module': 'mysql', 'class': 'ConfigurationVariables'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'mysql', 'class': 'Configuration'})
@cli_util.wrap_exceptions
def create_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, shape_name, variables, description, display_name, parent_configuration_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['shapeName'] = shape_name
    _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if parent_configuration_id is not None:
        _details['parentConfigurationId'] = parent_configuration_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('mysql', 'mysqlaas', ctx)
    result = client.create_configuration(
        create_configuration_details=_details,
        **kwargs
    )
    if wait_for_state:

        client = cli_util.build_client('mysql', 'work_requests', ctx)

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


@configuration_group.command(name=cli_util.override('mysqlaas.delete_configuration.command_name', 'delete'), help=u"""Deletes a Configuration. The Configuration must not be in use by any DB Systems. \n[Command Reference](deleteConfiguration)""")
@cli_util.option('--configuration-id', required=True, help=u"""The OCID of the Configuration.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, configuration_id, if_match):

    if isinstance(configuration_id, six.string_types) and len(configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('mysql', 'mysqlaas', ctx)
    result = client.delete_configuration(
        configuration_id=configuration_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_configuration') and callable(getattr(client, 'get_configuration')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_configuration(configuration_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@configuration_group.command(name=cli_util.override('mysqlaas.get_configuration.command_name', 'get'), help=u"""Get the full details of the specified Configuration, including the list of MySQL Variables and their values. \n[Command Reference](getConfiguration)""")
@cli_util.option('--configuration-id', required=True, help=u"""The OCID of the Configuration.""")
@cli_util.option('--if-none-match', help=u"""For conditional requests. In the GET call for a resource, set the `If-None-Match` header to the value of the ETag from a previous GET (or POST or PUT) response for that resource. The server will return with either a 304 Not Modified response if the resource has not changed, or a 200 OK response with the updated representation.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'mysql', 'class': 'Configuration'})
@cli_util.wrap_exceptions
def get_configuration(ctx, from_json, configuration_id, if_none_match):

    if isinstance(configuration_id, six.string_types) and len(configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('mysql', 'mysqlaas', ctx)
    result = client.get_configuration(
        configuration_id=configuration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@configuration_group.command(name=cli_util.override('mysqlaas.list_configurations.command_name', 'list'), help=u"""Lists the Configurations available when creating a DB System.

This may include DEFAULT configurations per Shape and CUSTOM configurations.

The default sort order is a multi-part sort by:   - shapeName, ascending   - DEFAULT-before-CUSTOM   - displayName ascending \n[Command Reference](listConfigurations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--configuration-id', help=u"""The requested Configuration instance.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), help=u"""Configuration Lifecycle State""")
@cli_util.option('--type', type=custom_types.CliCaseInsensitiveChoice(["DEFAULT", "CUSTOM"]), multiple=True, help=u"""The requested Configuration types.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resource matching the given display name exactly.""")
@cli_util.option('--shape-name', help=u"""The requested Shape name.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "shapeName", "timeCreated", "timeUpdated"]), help=u"""The field to sort by. Only one sort order may be provided. Time fields are default ordered as descending. Display name is default ordered as ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use (ASC or DESC).""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated list call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` or `opc-prev-page` response header from the previous list call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'mysql', 'class': 'list[ConfigurationSummary]'})
@cli_util.wrap_exceptions
def list_configurations(ctx, from_json, all_pages, page_size, compartment_id, configuration_id, lifecycle_state, type, display_name, shape_name, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if configuration_id is not None:
        kwargs['configuration_id'] = configuration_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if type is not None and len(type) > 0:
        kwargs['type'] = type
    if display_name is not None:
        kwargs['display_name'] = display_name
    if shape_name is not None:
        kwargs['shape_name'] = shape_name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('mysql', 'mysqlaas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_configurations,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_configurations,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_configurations(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@shape_group.command(name=cli_util.override('mysqlaas.list_shapes.command_name', 'list'), help=u"""Gets a list of the shapes you can use to create a new MySQL DB System. The shape determines the resources allocated to the DB System: CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. \n[Command Reference](listShapes)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--is-supported-for', type=custom_types.CliCaseInsensitiveChoice(["DBSYSTEM", "ANALYTICSCLUSTER"]), multiple=True, help=u"""Return shapes that are supported by the service feature.""")
@cli_util.option('--availability-domain', help=u"""The name of the Availability Domain.""")
@cli_util.option('--name', help=u"""Name""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'mysql', 'class': 'list[ShapeSummary]'})
@cli_util.wrap_exceptions
def list_shapes(ctx, from_json, all_pages, compartment_id, is_supported_for, availability_domain, name):

    kwargs = {}
    if is_supported_for is not None and len(is_supported_for) > 0:
        kwargs['is_supported_for'] = is_supported_for
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
    if name is not None:
        kwargs['name'] = name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('mysql', 'mysqlaas', ctx)
    result = client.list_shapes(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@version_group.command(name=cli_util.override('mysqlaas.list_versions.command_name', 'list'), help=u"""Get a list of supported and available MySQL database major versions.

The list is sorted by version family. \n[Command Reference](listVersions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'mysql', 'class': 'list[VersionSummary]'})
@cli_util.wrap_exceptions
def list_versions(ctx, from_json, all_pages, compartment_id):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('mysql', 'mysqlaas', ctx)
    result = client.list_versions(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@configuration_group.command(name=cli_util.override('mysqlaas.update_configuration.command_name', 'update'), help=u"""Updates the Configuration details. \n[Command Reference](updateConfiguration)""")
@cli_util.option('--configuration-id', required=True, help=u"""The OCID of the Configuration.""")
@cli_util.option('--description', help=u"""User-provided data about the Configuration.""")
@cli_util.option('--display-name', help=u"""A new display name for the Configuration.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'mysql', 'class': 'Configuration'})
@cli_util.wrap_exceptions
def update_configuration(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, configuration_id, description, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(configuration_id, six.string_types) and len(configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --configuration-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('mysql', 'mysqlaas', ctx)
    result = client.update_configuration(
        configuration_id=configuration_id,
        update_configuration_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_configuration') and callable(getattr(client, 'get_configuration')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_configuration(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
