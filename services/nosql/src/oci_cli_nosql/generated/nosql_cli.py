# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('nosql.nosql_root_group.command_name', 'nosql'), cls=CommandGroupWithAlias, help=cli_util.override('nosql.nosql_root_group.help', """The control plane API for NoSQL Database Cloud Service HTTPS
provides endpoints to perform NDCS operations, including creation
and deletion of tables and indexes; population and access of data
in tables; and access of table usage metrics."""), short_help=cli_util.override('nosql.nosql_root_group.short_help', """ndcs-control-plane API"""))
@cli_util.help_option_group
def nosql_root_group():
    pass


@click.command(cli_util.override('nosql.query_result_collection_group.command_name', 'query-result-collection'), cls=CommandGroupWithAlias, help="""The result of a query.""")
@cli_util.help_option_group
def query_result_collection_group():
    pass


@click.command(cli_util.override('nosql.index_group.command_name', 'index'), cls=CommandGroupWithAlias, help="""Information about an index.""")
@cli_util.help_option_group
def index_group():
    pass


@click.command(cli_util.override('nosql.row_group.command_name', 'row'), cls=CommandGroupWithAlias, help="""The result of GetRow.""")
@cli_util.help_option_group
def row_group():
    pass


@click.command(cli_util.override('nosql.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('nosql.table_group.command_name', 'table'), cls=CommandGroupWithAlias, help="""Complete metadata about a table.""")
@cli_util.help_option_group
def table_group():
    pass


nosql_root_group.add_command(query_result_collection_group)
nosql_root_group.add_command(index_group)
nosql_root_group.add_command(row_group)
nosql_root_group.add_command(work_request_group)
nosql_root_group.add_command(table_group)


@table_group.command(name=cli_util.override('nosql.change_table_compartment.command_name', 'change-compartment'), help=u"""Change a table's compartment.""")
@cli_util.option('--table-name-or-id', required=True, help=u"""A table name within the compartment, or a table OCID.""")
@cli_util.option('--to-compartment-id', required=True, help=u"""The OCID of the table's new compartment.""")
@cli_util.option('--from-compartment-id', help=u"""The OCID of the table's current compartment.  Required if the tableNameOrId path parameter is a table name. Optional if tableNameOrId is an OCID.  If tableNameOrId is an OCID, and fromCompartmentId is supplied, the latter must match the identified table's current compartmentId.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_table_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, table_name_or_id, to_compartment_id, from_compartment_id, if_match):

    if isinstance(table_name_or_id, six.string_types) and len(table_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --table-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['toCompartmentId'] = to_compartment_id

    if from_compartment_id is not None:
        _details['fromCompartmentId'] = from_compartment_id

    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.change_table_compartment(
        table_name_or_id=table_name_or_id,
        change_table_compartment_details=_details,
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


@index_group.command(name=cli_util.override('nosql.create_index.command_name', 'create'), help=u"""Create a new index on the table identified by tableNameOrId.""")
@cli_util.option('--table-name-or-id', required=True, help=u"""A table name within the compartment, or a table OCID.""")
@cli_util.option('--name', required=True, help=u"""Index name.""")
@cli_util.option('--keys', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A set of keys for a secondary index.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The OCID of the table's compartment.  Required if the tableNameOrId path parameter is a table name. Optional if tableNameOrId is an OCID.  If tableNameOrId is an OCID, and compartmentId is supplied, the latter must match the identified table's compartmentId.""")
@cli_util.option('--is-if-not-exists', type=click.BOOL, help=u"""If true, the operation completes successfully even when the index exists.  Otherwise, an attempt to create an index that already exists will return an error.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'keys': {'module': 'nosql', 'class': 'list[IndexKey]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'keys': {'module': 'nosql', 'class': 'list[IndexKey]'}})
@cli_util.wrap_exceptions
def create_index(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, table_name_or_id, name, keys, compartment_id, is_if_not_exists):

    if isinstance(table_name_or_id, six.string_types) and len(table_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --table-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['keys'] = cli_util.parse_json_parameter("keys", keys)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if is_if_not_exists is not None:
        _details['isIfNotExists'] = is_if_not_exists

    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.create_index(
        table_name_or_id=table_name_or_id,
        create_index_details=_details,
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


@table_group.command(name=cli_util.override('nosql.create_table.command_name', 'create'), help=u"""Create a new table.""")
@cli_util.option('--name', required=True, help=u"""Table name.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment Identifier.""")
@cli_util.option('--ddl-statement', required=True, help=u"""Complete CREATE TABLE DDL statement.""")
@cli_util.option('--table-limits', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace.  Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'table-limits': {'module': 'nosql', 'class': 'TableLimits'}, 'freeform-tags': {'module': 'nosql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'nosql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'table-limits': {'module': 'nosql', 'class': 'TableLimits'}, 'freeform-tags': {'module': 'nosql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'nosql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_table(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, ddl_statement, table_limits, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['ddlStatement'] = ddl_statement
    _details['tableLimits'] = cli_util.parse_json_parameter("table_limits", table_limits)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.create_table(
        create_table_details=_details,
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


@index_group.command(name=cli_util.override('nosql.delete_index.command_name', 'delete'), help=u"""Delete an index from the table identified by tableNameOrId.""")
@cli_util.option('--table-name-or-id', required=True, help=u"""A table name within the compartment, or a table OCID.""")
@cli_util.option('--index-name', required=True, help=u"""The name of a table's index.""")
@cli_util.option('--compartment-id', help=u"""The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.""")
@cli_util.option('--is-if-exists', type=click.BOOL, help=u"""Set as true to select \"if exists\" behavior.""")
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
def delete_index(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, table_name_or_id, index_name, compartment_id, is_if_exists, if_match):

    if isinstance(table_name_or_id, six.string_types) and len(table_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --table-name-or-id cannot be whitespace or empty string')

    if isinstance(index_name, six.string_types) and len(index_name.strip()) == 0:
        raise click.UsageError('Parameter --index-name cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if is_if_exists is not None:
        kwargs['is_if_exists'] = is_if_exists
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.delete_index(
        table_name_or_id=table_name_or_id,
        index_name=index_name,
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


@row_group.command(name=cli_util.override('nosql.delete_row.command_name', 'delete'), help=u"""Delete a single row from the table, by primary key.""")
@cli_util.option('--table-name-or-id', required=True, help=u"""A table name within the compartment, or a table OCID.""")
@cli_util.option('--key', required=True, multiple=True, help=u"""An array of strings, each of the format \"column-name:value\", representing the primary key of the row.""")
@cli_util.option('--compartment-id', help=u"""The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.""")
@cli_util.option('--is-get-return-row', type=click.BOOL, help=u"""If true, and the operation fails due to an option setting (ifVersion et al), then the existing row will be returned.""")
@cli_util.option('--timeout-in-ms', type=click.INT, help=u"""Timeout setting for this operation.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({'key': {'module': 'nosql', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'key': {'module': 'nosql', 'class': 'list[string]'}}, output_type={'module': 'nosql', 'class': 'DeleteRowResult'})
@cli_util.wrap_exceptions
def delete_row(ctx, from_json, table_name_or_id, key, compartment_id, is_get_return_row, timeout_in_ms, if_match):

    if isinstance(table_name_or_id, six.string_types) and len(table_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --table-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if is_get_return_row is not None:
        kwargs['is_get_return_row'] = is_get_return_row
    if timeout_in_ms is not None:
        kwargs['timeout_in_ms'] = timeout_in_ms
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.delete_row(
        table_name_or_id=table_name_or_id,
        key=key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@table_group.command(name=cli_util.override('nosql.delete_table.command_name', 'delete'), help=u"""Delete a table by tableNameOrId.""")
@cli_util.option('--table-name-or-id', required=True, help=u"""A table name within the compartment, or a table OCID.""")
@cli_util.option('--compartment-id', help=u"""The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.""")
@cli_util.option('--is-if-exists', type=click.BOOL, help=u"""Set as true to select \"if exists\" behavior.""")
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
def delete_table(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, table_name_or_id, compartment_id, is_if_exists, if_match):

    if isinstance(table_name_or_id, six.string_types) and len(table_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --table-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if is_if_exists is not None:
        kwargs['is_if_exists'] = is_if_exists
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.delete_table(
        table_name_or_id=table_name_or_id,
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


@work_request_group.command(name=cli_util.override('nosql.delete_work_request.command_name', 'delete'), help=u"""Cancel a work request operation with the given ID.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
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
def delete_work_request(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.delete_work_request(
        work_request_id=work_request_id,
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


@index_group.command(name=cli_util.override('nosql.get_index.command_name', 'get'), help=u"""Get information about a single index.""")
@cli_util.option('--table-name-or-id', required=True, help=u"""A table name within the compartment, or a table OCID.""")
@cli_util.option('--index-name', required=True, help=u"""The name of a table's index.""")
@cli_util.option('--compartment-id', help=u"""The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'nosql', 'class': 'Index'})
@cli_util.wrap_exceptions
def get_index(ctx, from_json, table_name_or_id, index_name, compartment_id):

    if isinstance(table_name_or_id, six.string_types) and len(table_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --table-name-or-id cannot be whitespace or empty string')

    if isinstance(index_name, six.string_types) and len(index_name.strip()) == 0:
        raise click.UsageError('Parameter --index-name cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.get_index(
        table_name_or_id=table_name_or_id,
        index_name=index_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@row_group.command(name=cli_util.override('nosql.get_row.command_name', 'get'), help=u"""Get a single row from the table by primary key.""")
@cli_util.option('--table-name-or-id', required=True, help=u"""A table name within the compartment, or a table OCID.""")
@cli_util.option('--key', required=True, multiple=True, help=u"""An array of strings, each of the format \"column-name:value\", representing the primary key of the row.""")
@cli_util.option('--compartment-id', help=u"""The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.""")
@cli_util.option('--consistency', type=custom_types.CliCaseInsensitiveChoice(["EVENTUAL", "ABSOLUTE"]), help=u"""Consistency requirement for a read operation.""")
@cli_util.option('--timeout-in-ms', type=click.INT, help=u"""Timeout setting for this operation.""")
@json_skeleton_utils.get_cli_json_input_option({'key': {'module': 'nosql', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'key': {'module': 'nosql', 'class': 'list[string]'}}, output_type={'module': 'nosql', 'class': 'Row'})
@cli_util.wrap_exceptions
def get_row(ctx, from_json, table_name_or_id, key, compartment_id, consistency, timeout_in_ms):

    if isinstance(table_name_or_id, six.string_types) and len(table_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --table-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if consistency is not None:
        kwargs['consistency'] = consistency
    if timeout_in_ms is not None:
        kwargs['timeout_in_ms'] = timeout_in_ms
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.get_row(
        table_name_or_id=table_name_or_id,
        key=key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@table_group.command(name=cli_util.override('nosql.get_table.command_name', 'get'), help=u"""Get table info by identifier.""")
@cli_util.option('--table-name-or-id', required=True, help=u"""A table name within the compartment, or a table OCID.""")
@cli_util.option('--compartment-id', help=u"""The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'nosql', 'class': 'Table'})
@cli_util.wrap_exceptions
def get_table(ctx, from_json, table_name_or_id, compartment_id):

    if isinstance(table_name_or_id, six.string_types) and len(table_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --table-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.get_table(
        table_name_or_id=table_name_or_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('nosql.get_work_request.command_name', 'get'), help=u"""Get the status of the work request with the given ID.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'nosql', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@index_group.command(name=cli_util.override('nosql.list_indexes.command_name', 'list'), help=u"""Get a list of indexes on a table.""")
@cli_util.option('--table-name-or-id', required=True, help=u"""A table name within the compartment, or a table OCID.""")
@cli_util.option('--compartment-id', help=u"""The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.""")
@cli_util.option('--name', help=u"""A shell-globbing-style (*?[]) filter for names.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ALL", "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""Filter list by the lifecycle state of the item.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for name is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'nosql', 'class': 'IndexCollection'})
@cli_util.wrap_exceptions
def list_indexes(ctx, from_json, all_pages, page_size, table_name_or_id, compartment_id, name, lifecycle_state, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(table_name_or_id, six.string_types) and len(table_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --table-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if name is not None:
        kwargs['name'] = name
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
    client = cli_util.build_client('nosql', 'nosql', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_indexes,
            table_name_or_id=table_name_or_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_indexes,
            limit,
            page_size,
            table_name_or_id=table_name_or_id,
            **kwargs
        )
    else:
        result = client.list_indexes(
            table_name_or_id=table_name_or_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@table_group.command(name=cli_util.override('nosql.list_table_usage.command_name', 'list-table-usage'), help=u"""Get table usage info.""")
@cli_util.option('--table-name-or-id', required=True, help=u"""A table name within the compartment, or a table OCID.""")
@cli_util.option('--compartment-id', help=u"""The ID of a table's compartment. When a table is identified by name, the compartmentId is often needed to provide context for interpreting the name.""")
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help=u"""The start time to use for the request. If no time range is set for this request, the most recent complete usage record is returned.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help=u"""The end time to use for the request.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'nosql', 'class': 'TableUsageCollection'})
@cli_util.wrap_exceptions
def list_table_usage(ctx, from_json, all_pages, page_size, table_name_or_id, compartment_id, time_start, time_end, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(table_name_or_id, six.string_types) and len(table_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --table-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if time_start is not None:
        kwargs['time_start'] = time_start
    if time_end is not None:
        kwargs['time_end'] = time_end
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_table_usage,
            table_name_or_id=table_name_or_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_table_usage,
            limit,
            page_size,
            table_name_or_id=table_name_or_id,
            **kwargs
        )
    else:
        result = client.list_table_usage(
            table_name_or_id=table_name_or_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@table_group.command(name=cli_util.override('nosql.list_tables.command_name', 'list'), help=u"""Get a list of tables in a compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of a table's compartment.""")
@cli_util.option('--name', help=u"""A shell-globbing-style (*?[]) filter for names.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for name is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ALL", "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""Filter list by the lifecycle state of the item.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'nosql', 'class': 'TableCollection'})
@cli_util.wrap_exceptions
def list_tables(ctx, from_json, all_pages, page_size, compartment_id, name, limit, page, sort_order, sort_by, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_tables,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_tables,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_tables(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('nosql.list_work_request_errors.command_name', 'list-work-request-errors'), help=u"""Return a (paginated) list of errors for a given work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'nosql', 'class': 'WorkRequestErrorCollection'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('nosql.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'nosql', 'class': 'WorkRequestLogEntryCollection'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('nosql.list_work_requests.command_name', 'list'), help=u"""List the work requests in a compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of a table's compartment.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'nosql', 'class': 'WorkRequestCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@query_result_collection_group.command(name=cli_util.override('nosql.prepare_statement.command_name', 'prepare-statement'), help=u"""Prepare a SQL statement for use in a query with variable substitution.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of a table's compartment.""")
@cli_util.option('--statement', required=True, help=u"""A NoSQL SQL statement.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'nosql', 'class': 'PreparedStatement'})
@cli_util.wrap_exceptions
def prepare_statement(ctx, from_json, compartment_id, statement):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.prepare_statement(
        compartment_id=compartment_id,
        statement=statement,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_result_collection_group.command(name=cli_util.override('nosql.query.command_name', 'query'), help=u"""Execute a SQL query.""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment OCID, to provide context for a table name in the given statement.""")
@cli_util.option('--statement', required=True, help=u"""A NoSQL SQL query statement; or a Base64-encoded prepared statement.""")
@cli_util.option('--is-prepared', type=click.BOOL, help=u"""If true, the statement is a prepared statement.""")
@cli_util.option('--consistency', type=custom_types.CliCaseInsensitiveChoice(["EVENTUAL", "ABSOLUTE"]), help=u"""Consistency requirement for a read operation.""")
@cli_util.option('--max-read-in-k-bs', type=click.INT, help=u"""A limit on the total amount of data read during this operation, in KB.""")
@cli_util.option('--variables', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of prepared statement variables to values.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--timeout-in-ms', type=click.INT, help=u"""Timeout setting for the query.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({'variables': {'module': 'nosql', 'class': 'dict(str, object)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'variables': {'module': 'nosql', 'class': 'dict(str, object)'}}, output_type={'module': 'nosql', 'class': 'QueryResultCollection'})
@cli_util.wrap_exceptions
def query(ctx, from_json, compartment_id, statement, is_prepared, consistency, max_read_in_k_bs, variables, timeout_in_ms, limit, page):

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['statement'] = statement

    if is_prepared is not None:
        _details['isPrepared'] = is_prepared

    if consistency is not None:
        _details['consistency'] = consistency

    if max_read_in_k_bs is not None:
        _details['maxReadInKBs'] = max_read_in_k_bs

    if variables is not None:
        _details['variables'] = cli_util.parse_json_parameter("variables", variables)

    if timeout_in_ms is not None:
        _details['timeoutInMs'] = timeout_in_ms

    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.query(
        query_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@query_result_collection_group.command(name=cli_util.override('nosql.summarize_statement.command_name', 'summarize-statement'), help=u"""Check the syntax and return a brief summary of a SQL statement.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of a table's compartment.""")
@cli_util.option('--statement', required=True, help=u"""A NoSQL SQL statement.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'nosql', 'class': 'StatementSummary'})
@cli_util.wrap_exceptions
def summarize_statement(ctx, from_json, compartment_id, statement):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.summarize_statement(
        compartment_id=compartment_id,
        statement=statement,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@row_group.command(name=cli_util.override('nosql.update_row.command_name', 'update'), help=u"""Write a single row into the table.""")
@cli_util.option('--table-name-or-id', required=True, help=u"""A table name within the compartment, or a table OCID.""")
@cli_util.option('--value', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The map of values from a row.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The OCID of the table's compartment.  Required if the tableNameOrId path parameter is a table name. Optional if tableNameOrId is an OCID.  If tableNameOrId is an OCID, and compartmentId is supplied, the latter must match the identified table's compartmentId.""")
@cli_util.option('--option', type=custom_types.CliCaseInsensitiveChoice(["IF_ABSENT", "IF_PRESENT"]), help=u"""Specifies a condition for the put operation.""")
@cli_util.option('--is-get-return-row', type=click.BOOL, help=u"""If true, and the put fails due to an option setting, then the existing row will be returned.""")
@cli_util.option('--timeout-in-ms', type=click.INT, help=u"""Timeout setting for the put.""")
@cli_util.option('--ttl', type=click.INT, help=u"""Time-to-live for the row, in days.""")
@cli_util.option('--is-ttl-use-table-default', type=click.BOOL, help=u"""If true, set time-to-live for this row to the table's default.""")
@cli_util.option('--identity-cache-size', type=click.INT, help=u"""Sets the number of generated identity values that are requested from the server during a put. If present and greater than 0, this value takes precedence over a default value for the table.""")
@cli_util.option('--is-exact-match', type=click.BOOL, help=u"""If present and true, the presented row value must exactly match the table's schema.  Otherwise, rows with missing non-key fields or extra fields can be written successfully.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'value': {'module': 'nosql', 'class': 'dict(str, object)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'value': {'module': 'nosql', 'class': 'dict(str, object)'}}, output_type={'module': 'nosql', 'class': 'UpdateRowResult'})
@cli_util.wrap_exceptions
def update_row(ctx, from_json, force, table_name_or_id, value, compartment_id, option, is_get_return_row, timeout_in_ms, ttl, is_ttl_use_table_default, identity_cache_size, is_exact_match, if_match):

    if isinstance(table_name_or_id, six.string_types) and len(table_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --table-name-or-id cannot be whitespace or empty string')
    if not force:
        if value:
            if not click.confirm("WARNING: Updates to value will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['value'] = cli_util.parse_json_parameter("value", value)

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if option is not None:
        _details['option'] = option

    if is_get_return_row is not None:
        _details['isGetReturnRow'] = is_get_return_row

    if timeout_in_ms is not None:
        _details['timeoutInMs'] = timeout_in_ms

    if ttl is not None:
        _details['ttl'] = ttl

    if is_ttl_use_table_default is not None:
        _details['isTtlUseTableDefault'] = is_ttl_use_table_default

    if identity_cache_size is not None:
        _details['identityCacheSize'] = identity_cache_size

    if is_exact_match is not None:
        _details['isExactMatch'] = is_exact_match

    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.update_row(
        table_name_or_id=table_name_or_id,
        update_row_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@table_group.command(name=cli_util.override('nosql.update_table.command_name', 'update'), help=u"""Alter the table identified by tableNameOrId, changing schema, limits, or tags""")
@cli_util.option('--table-name-or-id', required=True, help=u"""A table name within the compartment, or a table OCID.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the table's current compartment.  Required if the tableNameOrId path parameter is a table name. Optional if tableNameOrId is an OCID.  If tableNameOrId is an OCID, and compartmentId is supplied, the latter must match the identified table's compartmentId.""")
@cli_util.option('--ddl-statement', help=u"""Complete ALTER TABLE DDL statement.""")
@cli_util.option('--table-limits', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace.  Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'table-limits': {'module': 'nosql', 'class': 'TableLimits'}, 'freeform-tags': {'module': 'nosql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'nosql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'table-limits': {'module': 'nosql', 'class': 'TableLimits'}, 'freeform-tags': {'module': 'nosql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'nosql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_table(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, table_name_or_id, compartment_id, ddl_statement, table_limits, freeform_tags, defined_tags, if_match):

    if isinstance(table_name_or_id, six.string_types) and len(table_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --table-name-or-id cannot be whitespace or empty string')
    if not force:
        if table_limits or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to table-limits and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if ddl_statement is not None:
        _details['ddlStatement'] = ddl_statement

    if table_limits is not None:
        _details['tableLimits'] = cli_util.parse_json_parameter("table_limits", table_limits)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('nosql', 'nosql', ctx)
    result = client.update_table(
        table_name_or_id=table_name_or_id,
        update_table_details=_details,
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
