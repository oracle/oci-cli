# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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


@click.command(cli_util.override('db_backups.db_backups_root_group.command_name', 'db-backups'), cls=CommandGroupWithAlias, help=cli_util.override('db_backups.db_backups_root_group.help', """The API for the MySQL Database Service"""), short_help=cli_util.override('db_backups.db_backups_root_group.short_help', """MySQL Database Service API"""))
@cli_util.help_option_group
def db_backups_root_group():
    pass


@click.command(cli_util.override('db_backups.backup_group.command_name', 'backup'), cls=CommandGroupWithAlias, help="""A full or incremental copy of a DB System which can be used to create a new DB System or recover a DB System.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def backup_group():
    pass


mysql_service_cli.mysql_service_group.add_command(db_backups_root_group)
db_backups_root_group.add_command(backup_group)


@backup_group.command(name=cli_util.override('db_backups.create_backup.command_name', 'create'), help=u"""Create a backup of a DB System. \n[Command Reference](createBackup)""")
@cli_util.option('--db-system-id', required=True, help=u"""The OCID of the DB System the Backup is associated with.""")
@cli_util.option('--display-name', help=u"""A user-supplied display name for the backup.""")
@cli_util.option('--description', help=u"""A user-supplied description for the backup.""")
@cli_util.option('--backup-type', type=custom_types.CliCaseInsensitiveChoice(["FULL", "INCREMENTAL"]), help=u"""The type of backup.""")
@cli_util.option('--retention-in-days', type=click.INT, help=u"""Number of days to retain this backup.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'mysql', 'class': 'Backup'})
@cli_util.wrap_exceptions
def create_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, display_name, description, backup_type, retention_in_days, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dbSystemId'] = db_system_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if backup_type is not None:
        _details['backupType'] = backup_type

    if retention_in_days is not None:
        _details['retentionInDays'] = retention_in_days

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('mysql', 'db_backups', ctx)
    result = client.create_backup(
        create_backup_details=_details,
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


@backup_group.command(name=cli_util.override('db_backups.delete_backup.command_name', 'delete'), help=u"""Delete a Backup. \n[Command Reference](deleteBackup)""")
@cli_util.option('--backup-id', required=True, help=u"""The OCID of the Backup""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_backup(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, backup_id, if_match):

    if isinstance(backup_id, six.string_types) and len(backup_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('mysql', 'db_backups', ctx)
    result = client.delete_backup(
        backup_id=backup_id,
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


@backup_group.command(name=cli_util.override('db_backups.get_backup.command_name', 'get'), help=u"""Get information about the specified Backup \n[Command Reference](getBackup)""")
@cli_util.option('--backup-id', required=True, help=u"""The OCID of the Backup""")
@cli_util.option('--if-none-match', help=u"""For conditional requests. In the GET call for a resource, set the `If-None-Match` header to the value of the ETag from a previous GET (or POST or PUT) response for that resource. The server will return with either a 304 Not Modified response if the resource has not changed, or a 200 OK response with the updated representation.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'mysql', 'class': 'Backup'})
@cli_util.wrap_exceptions
def get_backup(ctx, from_json, backup_id, if_none_match):

    if isinstance(backup_id, six.string_types) and len(backup_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('mysql', 'db_backups', ctx)
    result = client.get_backup(
        backup_id=backup_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@backup_group.command(name=cli_util.override('db_backups.list_backups.command_name', 'list'), help=u"""Get a list of DB System backups. \n[Command Reference](listBackups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--backup-id', help=u"""Backup OCID""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""Backup Lifecycle State""")
@cli_util.option('--db-system-id', help=u"""The DB System [OCID].""")
@cli_util.option('--display-name', help=u"""A filter to return only the resource matching the given display name exactly.""")
@cli_util.option('--creation-type', type=custom_types.CliCaseInsensitiveChoice(["MANUAL", "AUTOMATIC"]), help=u"""Backup creationType""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "timeUpdated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Time fields are default ordered as descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use (ASC or DESC).""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated list call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` or `opc-prev-page` response header from the previous list call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'mysql', 'class': 'list[BackupSummary]'})
@cli_util.wrap_exceptions
def list_backups(ctx, from_json, all_pages, page_size, compartment_id, backup_id, lifecycle_state, db_system_id, display_name, creation_type, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if backup_id is not None:
        kwargs['backup_id'] = backup_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if db_system_id is not None:
        kwargs['db_system_id'] = db_system_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if creation_type is not None:
        kwargs['creation_type'] = creation_type
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('mysql', 'db_backups', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_backups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_backups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_backups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@backup_group.command(name=cli_util.override('db_backups.update_backup.command_name', 'update'), help=u"""Update the metadata of a Backup. Metadata such as the displayName or description \n[Command Reference](updateBackup)""")
@cli_util.option('--backup-id', required=True, help=u"""The OCID of the Backup""")
@cli_util.option('--display-name', help=u"""A user-supplied display name for the backup.""")
@cli_util.option('--description', help=u"""A user-supplied description for the backup.""")
@cli_util.option('--retention-in-days', type=click.INT, help=u"""The number of days backups are retained.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_backup(ctx, from_json, force, backup_id, display_name, description, retention_in_days, freeform_tags, defined_tags, if_match):

    if isinstance(backup_id, six.string_types) and len(backup_id.strip()) == 0:
        raise click.UsageError('Parameter --backup-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if retention_in_days is not None:
        _details['retentionInDays'] = retention_in_days

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('mysql', 'db_backups', ctx)
    result = client.update_backup(
        backup_id=backup_id,
        update_backup_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
