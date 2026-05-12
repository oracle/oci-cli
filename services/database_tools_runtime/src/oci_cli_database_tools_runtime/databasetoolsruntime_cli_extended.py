# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
import oci
import sys
from services.database_tools_runtime.src.oci_cli_database_tools_runtime.generated import databasetoolsruntime_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


def _wait_on_work_request_if_needed(ctx, client, result, wait_for_state, max_wait_seconds, wait_interval_seconds):
    if not wait_for_state:
        return result

    if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
        try:
            wait_period_kwargs = {}
            if max_wait_seconds is not None:
                wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
            if wait_interval_seconds is not None:
                wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds
            if 'opc-work-request-id' not in result.headers:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state')
                cli_util.render_response(result, ctx)
                return result

            click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
            return oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
        except oci.exceptions.MaximumWaitTimeExceeded:
            click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
            cli_util.render_response(result, ctx)
            sys.exit(2)
        except Exception:
            click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
            cli_util.render_response(result, ctx)
            raise
    else:
        click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    return result


def _render_async_execute_sql_response(ctx, client, result, wait_for_state, max_wait_seconds, wait_interval_seconds):
    result = _wait_on_work_request_if_needed(ctx, client, result, wait_for_state, max_wait_seconds, wait_interval_seconds)
    cli_util.render_response(result, ctx)


def _execute_sql_database_tools_connection_without_response_model(ctx, client, connection_id, details, kwargs_for_call):
    operation_name = 'execute_sql_database_tools_connection'
    path = '/databaseToolsConnections/{databaseToolsConnectionId}/actions/executeSql'.format(databaseToolsConnectionId=connection_id)

    return client.base_client.call_api(
        resource_path=path,
        method='POST',
        header_params={
            'accept': 'application/json',
            'content-type': 'application/json',
            'opc-request-id': kwargs_for_call.get('opc_request_id'),
            'if-match': kwargs_for_call.get('if_match')
        },
        body=details,
        response_type='object',
        allow_control_chars=False,
        operation_name=operation_name,
        required_arguments=['databaseToolsConnectionId'],
        enforce_content_headers=True
    )

# oci dbtools-runtime user credential


@click.command('user', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='User resources.')
@cli_util.help_option_group
def user_group():
    pass


@click.command('credential', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='User credential resources.')
@cli_util.help_option_group
def user_credential_nested_group():
    pass


user_group.add_command(user_credential_nested_group)
databasetoolsruntime_cli.dbtools_runtime_root_group.add_command(user_group)


# oci dbtools-runtime connection execute-sql
@click.command('execute-sql', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='Execute SQL using a connection.')
@cli_util.help_option_group
def connection_execute_sql_group():
    pass


# oci dbtools-runtime connection validate

# oci database-tools-runtime user-credential-collection list-user-credentials -> oci database-tools-runtime user-credential-collection list
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.user_credential_collection_group, databasetoolsruntime_cli.list_user_credentials, "list")


# oci database-tools-runtime credential-collection list-credentials -> oci database-tools-runtime credential-collection list
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.credential_collection_group, databasetoolsruntime_cli.list_credentials, "list")


# oci database-tools-runtime credential-execute-grantee-collection list-credential-execute-grantees -> oci database-tools-runtime credential-execute-grantee-collection list
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.credential_execute_grantee_collection_group, databasetoolsruntime_cli.list_credential_execute_grantees, "list")


# oci database-tools-runtime credential-public-synonym-collection list-credential-public-synonyms -> oci database-tools-runtime credential-public-synonym-collection list
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.credential_public_synonym_collection_group, databasetoolsruntime_cli.list_credential_public_synonyms, "list")


# oci dbtools-runtime work-request-log-entry list-work-request-logs -> oci dbtools-runtime work-request-log-entry list
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.work_request_log_entry_group, databasetoolsruntime_cli.list_work_request_logs, "list")


# oci dbtools-runtime credential-execute-grantee -> oci dbtools-runtime execute-grantee
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.dbtools_runtime_root_group, databasetoolsruntime_cli.credential_execute_grantee_group, "execute-grantee")

# Add execute-grantee list under oci dbtools-runtime execute-grantee
databasetoolsruntime_cli.credential_execute_grantee_group.add_command(databasetoolsruntime_cli.list_credential_execute_grantees)

# oci dbtools-runtime execute-grantee list-credential-execute-grantees -> oci dbtools-runtime execute-grantee list
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.credential_execute_grantee_group, databasetoolsruntime_cli.list_credential_execute_grantees, "list")


# oci dbtools-runtime credential-public-synonym -> oci dbtools-runtime public-synonym
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.dbtools_runtime_root_group, databasetoolsruntime_cli.credential_public_synonym_group, "public-synonym")

# Add public-synonym list under oci dbtools-runtime public-synonym
databasetoolsruntime_cli.credential_public_synonym_group.add_command(databasetoolsruntime_cli.list_credential_public_synonyms)

# oci dbtools-runtime public-synonym list-credential-public-synonyms -> oci dbtools-runtime public-synonym list
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.credential_public_synonym_group, databasetoolsruntime_cli.list_credential_public_synonyms, "list")


# oci dbtools-runtime database-tools-connection -> oci dbtools-runtime connection
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.dbtools_runtime_root_group, databasetoolsruntime_cli.database_tools_connection_group, "connection")
databasetoolsruntime_cli.database_tools_connection_group.help = 'Database Tools connection resources.'


# oci dbtools-runtime database-tools-database-api-gateway-config -> oci dbtools-runtime database-api-gateway-config
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.dbtools_runtime_root_group, databasetoolsruntime_cli.database_tools_database_api_gateway_config_group, "database-api-gateway-config")
databasetoolsruntime_cli.database_tools_database_api_gateway_config_group.help = 'Database API Gateway configuration resources.'

# Remove pool list/delete commands from oci dbtools-runtime database-api-gateway-config root; they are exposed via dedicated groups
databasetoolsruntime_cli.database_tools_database_api_gateway_config_group.commands.pop(databasetoolsruntime_cli.list_database_tools_database_api_gateway_config_pools.name, None)
databasetoolsruntime_cli.database_tools_database_api_gateway_config_group.commands.pop(databasetoolsruntime_cli.list_database_tools_database_api_gateway_config_pool_api_specs.name, None)
databasetoolsruntime_cli.database_tools_database_api_gateway_config_group.commands.pop(databasetoolsruntime_cli.list_database_tools_database_api_gateway_config_pool_auto_api_specs.name, None)
databasetoolsruntime_cli.database_tools_database_api_gateway_config_group.commands.pop(databasetoolsruntime_cli.delete_database_tools_database_api_gateway_config_pool.name, None)
databasetoolsruntime_cli.database_tools_database_api_gateway_config_group.commands.pop(databasetoolsruntime_cli.delete_database_tools_database_api_gateway_config_pool_api_spec.name, None)
databasetoolsruntime_cli.database_tools_database_api_gateway_config_group.commands.pop(databasetoolsruntime_cli.delete_database_tools_database_api_gateway_config_pool_auto_api_spec.name, None)


# oci dbtools-runtime database-tools-database-api-gateway-config-global -> oci dbtools-runtime database-api-gateway-config-global
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.dbtools_runtime_root_group, databasetoolsruntime_cli.database_tools_database_api_gateway_config_global_group, "database-api-gateway-config-global")


# oci dbtools-runtime database-tools-database-api-gateway-config-pool -> oci dbtools-runtime database-api-gateway-config-pool
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.dbtools_runtime_root_group, databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_group, "database-api-gateway-config-pool")


# oci dbtools-runtime database-tools-database-api-gateway-config-pool-api-spec -> oci dbtools-runtime database-api-gateway-config-pool-api-spec
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.dbtools_runtime_root_group, databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_api_spec_group, "database-api-gateway-config-pool-api-spec")


# oci dbtools-runtime database-tools-database-api-gateway-config-pool-auto-api-spec -> oci dbtools-runtime database-api-gateway-config-pool-auto-api-spec
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.dbtools_runtime_root_group, databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_auto_api_spec_group, "database-api-gateway-config-pool-auto-api-spec")


# oci dbtools-runtime database-tools-database-api-gateway-config-advanced-property-summary -> oci dbtools-runtime database-api-gateway-config-advanced-properties
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.dbtools_runtime_root_group, databasetoolsruntime_cli.database_tools_database_api_gateway_config_advanced_property_summary_group, "database-api-gateway-config-advanced-properties")


# oci dbtools-runtime database-tools-identity -> oci dbtools-runtime identity
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.dbtools_runtime_root_group, databasetoolsruntime_cli.database_tools_identity_group, "identity")


# oci dbtools-runtime user-credential-collection -> oci dbtools-runtime user-credential
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.dbtools_runtime_root_group, databasetoolsruntime_cli.user_credential_collection_group, "user-credential")


# Remove credential-collection from oci dbtools-runtime
databasetoolsruntime_cli.dbtools_runtime_root_group.commands.pop(databasetoolsruntime_cli.credential_collection_group.name, None)


# Remove list-credentials from oci dbtools-runtime credential before re-adding it as list
databasetoolsruntime_cli.credential_group.commands.pop(databasetoolsruntime_cli.list_credentials.name, None)
databasetoolsruntime_cli.credential_group.commands.pop('list', None)


# Move user credential commands under oci dbtools-runtime user credential
databasetoolsruntime_cli.dbtools_runtime_root_group.commands.pop(databasetoolsruntime_cli.user_credential_group.name, None)
databasetoolsruntime_cli.dbtools_runtime_root_group.commands.pop("user-credential", None)

user_credential_nested_group.add_command(databasetoolsruntime_cli.get_user_credential)
user_credential_nested_group.add_command(databasetoolsruntime_cli.list_user_credentials)

# oci dbtools-runtime user credential get -> oci dbtools-runtime user credential get
cli_util.rename_command(databasetoolsruntime_cli, user_credential_nested_group, databasetoolsruntime_cli.get_user_credential, "get")

# oci dbtools-runtime user credential list-user-credentials -> oci dbtools-runtime user credential list
cli_util.rename_command(databasetoolsruntime_cli, user_credential_nested_group, databasetoolsruntime_cli.list_user_credentials, "list")


# Add credential list under oci dbtools-runtime credential
databasetoolsruntime_cli.credential_group.add_command(databasetoolsruntime_cli.list_credential_execute_grantees)
databasetoolsruntime_cli.credential_group.add_command(databasetoolsruntime_cli.list_credential_public_synonyms)


# oci dbtools-runtime credential list
@click.command('list', help=databasetoolsruntime_cli.list_credentials.help)
@cli_util.option('--connection-id', required=True, help='''The [OCID] of a Database Tools connection.''')
@cli_util.option('--if-match', help='''For optimistic concurrency control.''')
@cli_util.option('--limit', type=click.INT, help='''The maximum number of items to return.''')
@cli_util.option('--page', help='''The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.''')
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help='''The sort order to use, either 'asc' or 'desc'.''')
@cli_util.option('--all', 'all_pages', is_flag=True, help='''Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.''')
@cli_util.option('--page-size', type=click.INT, help='''When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.''')
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'database_tools_runtime', 'class': 'CredentialCollection'})
@cli_util.wrap_exceptions
def credential_list_extended(ctx, from_json, all_pages, page_size, connection_id, if_match, limit, page, sort_order):
    ctx.invoke(
        databasetoolsruntime_cli.list_credentials,
        from_json=from_json,
        all_pages=all_pages,
        page_size=page_size,
        connection_id=connection_id,
        if_match=if_match,
        limit=limit,
        page=page,
        sort_order=sort_order
    )


databasetoolsruntime_cli.credential_group.commands.pop('list', None)
databasetoolsruntime_cli.credential_group.add_command(credential_list_extended)

# oci dbtools-runtime credential list-credential-execute-grantees -> oci dbtools-runtime credential list-execute-grantees
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.credential_group, databasetoolsruntime_cli.list_credential_execute_grantees, "list-execute-grantees")

# oci dbtools-runtime credential list-credential-public-synonyms -> oci dbtools-runtime credential list-public-synonyms
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.credential_group, databasetoolsruntime_cli.list_credential_public_synonyms, "list-public-synonyms")


# Add connection list-credentials under oci dbtools-runtime connection
databasetoolsruntime_cli.database_tools_connection_group.add_command(databasetoolsruntime_cli.list_credentials)

# oci dbtools-runtime connection list-credentials -> oci dbtools-runtime connection list-credentials
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.database_tools_connection_group, databasetoolsruntime_cli.list_credentials, "list-credentials")


# Move credential create basic-details command under oci dbtools-runtime credential create
databasetoolsruntime_cli.credential_group.commands.pop(databasetoolsruntime_cli.create_credential_create_credential_basic_details.name, None)


# oci dbtools-runtime credential create
@click.command('create', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='Create a database credential.')
@cli_util.help_option_group
def credential_create_group():
    pass


databasetoolsruntime_cli.credential_group.add_command(credential_create_group)
credential_create_group.add_command(databasetoolsruntime_cli.create_credential_create_credential_basic_details)

# oci dbtools-runtime credential create create-credential-create-credential-basic-details -> oci dbtools-runtime credential create basic
cli_util.rename_command(databasetoolsruntime_cli, credential_create_group, databasetoolsruntime_cli.create_credential_create_credential_basic_details, "basic")


# Remove create-credential from oci database-tools-runtime database-tools-connection
databasetoolsruntime_cli.database_tools_connection_group.commands.pop(databasetoolsruntime_cli.create_credential.name)


# Remove update from oci database-tools-runtime credential
databasetoolsruntime_cli.credential_group.commands.pop(databasetoolsruntime_cli.update_credential.name)


# Move credential update basic-details command under oci dbtools-runtime credential update
databasetoolsruntime_cli.credential_group.commands.pop(databasetoolsruntime_cli.update_credential_update_credential_basic_details.name, None)


# oci dbtools-runtime credential update
@click.command('update', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='Update a database credential.')
@cli_util.help_option_group
def credential_update_group():
    pass


databasetoolsruntime_cli.credential_group.add_command(credential_update_group)
credential_update_group.add_command(databasetoolsruntime_cli.update_credential_update_credential_basic_details)

# oci dbtools-runtime credential update update-credential-update-credential-basic-details -> oci dbtools-runtime credential update basic
cli_util.rename_command(databasetoolsruntime_cli, credential_update_group, databasetoolsruntime_cli.update_credential_update_credential_basic_details, "basic")


# Remove execute-sql from oci database-tools-runtime database-tools-connection
databasetoolsruntime_cli.database_tools_connection_group.commands.pop(databasetoolsruntime_cli.execute_sql_database_tools_connection.name)
databasetoolsruntime_cli.database_tools_connection_group.commands.pop(databasetoolsruntime_cli.execute_sql_database_tools_connection_execute_sql_database_tools_connection_asynchronous_details.name)
databasetoolsruntime_cli.database_tools_connection_group.commands.pop(databasetoolsruntime_cli.execute_sql_database_tools_connection_execute_sql_database_tools_connection_synchronous_details.name)
databasetoolsruntime_cli.database_tools_connection_group.commands.pop(databasetoolsruntime_cli.execute_sql_database_tools_connection_execute_sql_output_object_storage_details.name)

databasetoolsruntime_cli.database_tools_connection_group.add_command(connection_execute_sql_group)


@connection_execute_sql_group.command('async', help=databasetoolsruntime_cli.execute_sql_database_tools_connection_execute_sql_database_tools_connection_asynchronous_details.help)
@cli_util.option('--connection-id', required=True, help='''The [OCID] of a Database Tools connection.''')
@cli_util.option('--request-input', required=True, type=custom_types.CLI_COMPLEX_TYPE, help='''Request input payload.''' + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--request-output', type=custom_types.CLI_COMPLEX_TYPE, help='''Request output payload.''' + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-time-of-deletion', type=custom_types.CLI_DATETIME, help='''The time when the object becomes eligible for deletion, expressed as an RFC 3339 date-time string.''' + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--timeout-in-seconds', type=click.INT, help='''The timeout in seconds.''')
@cli_util.option('--if-match', help='''For optimistic concurrency control.''')
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "WAITING"]), multiple=True, help='''Wait for a given work request state.''')
@cli_util.option('--max-wait-seconds', type=click.INT, help='''Maximum wait time in seconds.''')
@cli_util.option('--wait-interval-seconds', type=click.INT, help='''Check interval while waiting.''')
@json_skeleton_utils.get_cli_json_input_option({'request-input': {'module': 'database_tools_runtime', 'class': 'ExecuteSqlAsynchronousInputDetails'}, 'request-output': {'module': 'database_tools_runtime', 'class': 'ExecuteSqlOutputDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'request-input': {'module': 'database_tools_runtime', 'class': 'ExecuteSqlAsynchronousInputDetails'}, 'request-output': {'module': 'database_tools_runtime', 'class': 'ExecuteSqlOutputDetails'}})
@cli_util.wrap_exceptions
def execute_sql_async_extended(ctx, **kwargs):
    cli_util.load_context_obj_values_from_defaults(ctx)
    if ctx.obj.get('generate_param_json_input') or ctx.obj.get('generate_full_command_json_input'):
        return
    connection_id = kwargs['connection_id']
    wait_for_state = kwargs.get('wait_for_state')
    max_wait_seconds = kwargs.get('max_wait_seconds')
    wait_interval_seconds = kwargs.get('wait_interval_seconds')
    request_output = kwargs.pop('request_output', None)
    output_time_of_deletion = kwargs.pop('output_time_of_deletion', None)
    if request_output is not None:
        kwargs['output_parameterconflict'] = cli_util.parse_json_parameter('request_output', request_output)
    if request_output is not None and output_time_of_deletion is not None:
        kwargs['output_parameterconflict']['timeOfDeletion'] = output_time_of_deletion
    parsed_input = cli_util.parse_json_parameter('request_input', kwargs['request_input'])
    kwargs_for_call = {}
    if kwargs.get('if_match') is not None:
        kwargs_for_call['if_match'] = kwargs.get('if_match')
    kwargs_for_call['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {
        'type': 'ASYNCHRONOUS',
        'input': parsed_input
    }
    if kwargs.get('timeout_in_seconds') is not None:
        details['timeoutInSeconds'] = kwargs.get('timeout_in_seconds')
    if kwargs.get('output_parameterconflict') is not None:
        details['output'] = kwargs.get('output_parameterconflict')

    client = cli_util.build_client('database_tools_runtime', 'database_tools_runtime', ctx)
    result = _execute_sql_database_tools_connection_without_response_model(ctx, client, connection_id, details, kwargs_for_call)
    _render_async_execute_sql_response(ctx, client, result, wait_for_state, max_wait_seconds, wait_interval_seconds)


execute_sql_async_extended.help = 'Execute SQL asynchronously using a connection.'


@connection_execute_sql_group.command('sync', help=databasetoolsruntime_cli.execute_sql_database_tools_connection_execute_sql_database_tools_connection_synchronous_details.help)
@cli_util.option('--connection-id', required=True, help='''The [OCID] of a Database Tools connection.''')
@cli_util.option('--request-input', required=True, type=custom_types.CLI_COMPLEX_TYPE, help='''Request input payload.''' + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help='''For optimistic concurrency control.''')
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "WAITING"]), multiple=True, help='''Wait for a given work request state.''')
@cli_util.option('--max-wait-seconds', type=click.INT, help='''Maximum wait time in seconds.''')
@cli_util.option('--wait-interval-seconds', type=click.INT, help='''Check interval while waiting.''')
@json_skeleton_utils.get_cli_json_input_option({'request-input': {'module': 'database_tools_runtime', 'class': 'ExecuteSqlInputDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'request-input': {'module': 'database_tools_runtime', 'class': 'ExecuteSqlInputDetails'}})
@cli_util.wrap_exceptions
def execute_sql_sync_extended(ctx, **kwargs):
    cli_util.load_context_obj_values_from_defaults(ctx)
    if ctx.obj.get('generate_param_json_input') or ctx.obj.get('generate_full_command_json_input'):
        return
    kwargs['input'] = kwargs.pop('request_input')
    ctx.invoke(databasetoolsruntime_cli.execute_sql_database_tools_connection_execute_sql_database_tools_connection_synchronous_details, **kwargs)


execute_sql_sync_extended.help = 'Execute SQL synchronously using a connection.'


# Remove validate from oci database-tools-runtime database-tools-connection
databasetoolsruntime_cli.database_tools_connection_group.commands.pop(databasetoolsruntime_cli.validate_database_tools_connection.name)


# Move validate detail commands under oci dbtools-runtime connection validate
databasetoolsruntime_cli.database_tools_connection_group.commands.pop(databasetoolsruntime_cli.validate_database_tools_connection_validate_database_tools_connection_my_sql_details.name)
databasetoolsruntime_cli.database_tools_connection_group.commands.pop(databasetoolsruntime_cli.validate_database_tools_connection_validate_database_tools_connection_oracle_database_details.name)
databasetoolsruntime_cli.database_tools_connection_group.commands.pop(databasetoolsruntime_cli.validate_database_tools_connection_validate_database_tools_connection_postgresql_details.name)


# Remove obsolete collection groups from oci dbtools-runtime root
databasetoolsruntime_cli.dbtools_runtime_root_group.commands.pop(databasetoolsruntime_cli.credential_execute_grantee_collection_group.name, None)
databasetoolsruntime_cli.dbtools_runtime_root_group.commands.pop(databasetoolsruntime_cli.credential_public_synonym_collection_group.name, None)


# oci dbtools-runtime connection validate
@click.command('validate', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help=databasetoolsruntime_cli.validate_database_tools_connection.help)
@cli_util.help_option_group
def database_tools_connection_validate_group():
    pass


databasetoolsruntime_cli.database_tools_connection_group.add_command(database_tools_connection_validate_group)

database_tools_connection_validate_group.add_command(databasetoolsruntime_cli.validate_database_tools_connection_validate_database_tools_connection_my_sql_details)
database_tools_connection_validate_group.add_command(databasetoolsruntime_cli.validate_database_tools_connection_validate_database_tools_connection_oracle_database_details)
database_tools_connection_validate_group.add_command(databasetoolsruntime_cli.validate_database_tools_connection_validate_database_tools_connection_postgresql_details)

# oci dbtools-runtime connection validate validate-database-tools-connection-validate-database-tools-connection-my-sql-details -> oci dbtools-runtime connection validate mysql
cli_util.rename_command(databasetoolsruntime_cli, database_tools_connection_validate_group, databasetoolsruntime_cli.validate_database_tools_connection_validate_database_tools_connection_my_sql_details, "mysql")

# oci dbtools-runtime connection validate validate-database-tools-connection-validate-database-tools-connection-oracle-database-details -> oci dbtools-runtime connection validate oracle-database
cli_util.rename_command(databasetoolsruntime_cli, database_tools_connection_validate_group, databasetoolsruntime_cli.validate_database_tools_connection_validate_database_tools_connection_oracle_database_details, "oracle-database")

# oci dbtools-runtime connection validate validate-database-tools-connection-validate-database-tools-connection-postgresql-details -> oci dbtools-runtime connection validate postgresql
cli_util.rename_command(databasetoolsruntime_cli, database_tools_connection_validate_group, databasetoolsruntime_cli.validate_database_tools_connection_validate_database_tools_connection_postgresql_details, "postgresql")


# Move get content command under oci dbtools-runtime database-api-gateway-config get
databasetoolsruntime_cli.database_tools_database_api_gateway_config_group.commands.pop(databasetoolsruntime_cli.get_database_tools_database_api_gateway_config_content.name)


# oci dbtools-runtime database-api-gateway-config get
@click.command('get', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='Get database API gateway config resources.')
@cli_util.help_option_group
def database_api_gateway_config_get_group():
    pass


databasetoolsruntime_cli.database_tools_database_api_gateway_config_group.add_command(database_api_gateway_config_get_group)
database_api_gateway_config_get_group.add_command(databasetoolsruntime_cli.get_database_tools_database_api_gateway_config_content)

# oci dbtools-runtime database-api-gateway-config get get-database-tools-database-api-gateway-config-content -> oci dbtools-runtime database-api-gateway-config get content
cli_util.rename_command(databasetoolsruntime_cli, database_api_gateway_config_get_group, databasetoolsruntime_cli.get_database_tools_database_api_gateway_config_content, "content")


# oci dbtools-runtime database-api-gateway-config-advanced-properties list-database-tools-database-api-gateway-config-advanced-properties -> oci dbtools-runtime database-api-gateway-config-advanced-properties list
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.database_tools_database_api_gateway_config_advanced_property_summary_group, databasetoolsruntime_cli.list_database_tools_database_api_gateway_config_advanced_properties, "list")


# Remove update from oci database-tools-runtime database-tools-database-api-gateway-config-global
databasetoolsruntime_cli.database_tools_database_api_gateway_config_global_group.commands.pop(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_global.name)


# Move database-api-gateway-config-global update detail commands under oci dbtools-runtime database-api-gateway-config-global update
databasetoolsruntime_cli.database_tools_database_api_gateway_config_global_group.commands.pop(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_global_update_database_tools_database_api_gateway_config_global_default_details.name, None)
databasetoolsruntime_cli.database_tools_database_api_gateway_config_global_group.commands.pop(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_global_database_api_gateway_config_certificate_bundle_file_name.name, None)
databasetoolsruntime_cli.database_tools_database_api_gateway_config_global_group.commands.pop(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_global_database_api_gateway_config_certificate_bundle_self_signed.name, None)


# oci dbtools-runtime database-api-gateway-config-global update
@click.command('update', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='Update database API gateway config global settings.')
@cli_util.help_option_group
def database_api_gateway_config_global_update_group():
    pass


databasetoolsruntime_cli.database_tools_database_api_gateway_config_global_group.add_command(database_api_gateway_config_global_update_group)
database_api_gateway_config_global_update_group.add_command(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_global_update_database_tools_database_api_gateway_config_global_default_details)

# oci dbtools-runtime database-api-gateway-config-global update update-database-tools-database-api-gateway-config-global-update-database-tools-database-api-gateway-config-global-default-details -> oci dbtools-runtime database-api-gateway-config-global update default
cli_util.rename_command(databasetoolsruntime_cli, database_api_gateway_config_global_update_group, databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_global_update_database_tools_database_api_gateway_config_global_default_details, "default")


# Remove create from oci database-tools-runtime database-tools-database-api-gateway-config-pool
databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_group.commands.pop(databasetoolsruntime_cli.create_database_tools_database_api_gateway_config_pool.name)


# Move create default-details command under oci dbtools-runtime database-api-gateway-config-pool create
databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_group.commands.pop(databasetoolsruntime_cli.create_database_tools_database_api_gateway_config_pool_create_database_tools_database_api_gateway_config_pool_default_details.name)


# oci dbtools-runtime database-api-gateway-config-pool create
@click.command('create', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='Create database API gateway config pool resources.')
@cli_util.help_option_group
def database_api_gateway_config_pool_create_group():
    pass


databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_group.add_command(database_api_gateway_config_pool_create_group)
database_api_gateway_config_pool_create_group.add_command(databasetoolsruntime_cli.create_database_tools_database_api_gateway_config_pool_create_database_tools_database_api_gateway_config_pool_default_details)

# oci dbtools-runtime database-api-gateway-config-pool create create-database-tools-database-api-gateway-config-pool-create-database-tools-database-api-gateway-config-pool-default-details -> oci dbtools-runtime database-api-gateway-config-pool create default
cli_util.rename_command(databasetoolsruntime_cli, database_api_gateway_config_pool_create_group, databasetoolsruntime_cli.create_database_tools_database_api_gateway_config_pool_create_database_tools_database_api_gateway_config_pool_default_details, "default")

# oci dbtools-runtime database-api-gateway-config-pool list-database-tools-database-api-gateway-config-pools -> oci dbtools-runtime database-api-gateway-config-pool list
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_group, databasetoolsruntime_cli.list_database_tools_database_api_gateway_config_pools, "list")

# oci dbtools-runtime database-api-gateway-config-pool delete-database-tools-database-api-gateway-config-pool -> oci dbtools-runtime database-api-gateway-config-pool delete
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_group, databasetoolsruntime_cli.delete_database_tools_database_api_gateway_config_pool, "delete")


# Remove update from oci database-tools-runtime database-tools-database-api-gateway-config-pool
databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_group.commands.pop(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_pool.name)


# Move update default-details command under oci dbtools-runtime database-api-gateway-config-pool update
databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_group.commands.pop(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_pool_update_database_tools_database_api_gateway_config_pool_default_details.name)


# oci dbtools-runtime database-api-gateway-config-pool update
@click.command('update', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='Update database API gateway config pool resources.')
@cli_util.help_option_group
def database_api_gateway_config_pool_update_group():
    pass


databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_group.add_command(database_api_gateway_config_pool_update_group)
database_api_gateway_config_pool_update_group.add_command(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_pool_update_database_tools_database_api_gateway_config_pool_default_details)

# oci dbtools-runtime database-api-gateway-config-pool update update-database-tools-database-api-gateway-config-pool-update-database-tools-database-api-gateway-config-pool-default-details -> oci dbtools-runtime database-api-gateway-config-pool update default
cli_util.rename_command(databasetoolsruntime_cli, database_api_gateway_config_pool_update_group, databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_pool_update_database_tools_database_api_gateway_config_pool_default_details, "default")


# Remove create from oci database-tools-runtime database-tools-database-api-gateway-config-pool-api-spec
databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_api_spec_group.commands.pop(databasetoolsruntime_cli.create_database_tools_database_api_gateway_config_pool_api_spec.name)


# Move create default-details command under oci dbtools-runtime database-api-gateway-config-pool-api-spec create
databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_api_spec_group.commands.pop(databasetoolsruntime_cli.create_database_tools_database_api_gateway_config_pool_api_spec_create_database_tools_database_api_gateway_config_pool_api_spec_default_details.name)


# oci dbtools-runtime database-api-gateway-config-pool-api-spec create
@click.command('create', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='Create database API gateway config pool API spec resources.')
@cli_util.help_option_group
def database_api_gateway_config_pool_api_spec_create_group():
    pass


databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_api_spec_group.add_command(database_api_gateway_config_pool_api_spec_create_group)
database_api_gateway_config_pool_api_spec_create_group.add_command(databasetoolsruntime_cli.create_database_tools_database_api_gateway_config_pool_api_spec_create_database_tools_database_api_gateway_config_pool_api_spec_default_details)

# oci dbtools-runtime database-api-gateway-config-pool-api-spec create create-database-tools-database-api-gateway-config-pool-api-spec-create-database-tools-database-api-gateway-config-pool-api-spec-default-details -> oci dbtools-runtime database-api-gateway-config-pool-api-spec create default
cli_util.rename_command(databasetoolsruntime_cli, database_api_gateway_config_pool_api_spec_create_group, databasetoolsruntime_cli.create_database_tools_database_api_gateway_config_pool_api_spec_create_database_tools_database_api_gateway_config_pool_api_spec_default_details, "default")

# oci dbtools-runtime database-api-gateway-config-pool-api-spec list-database-tools-database-api-gateway-config-pool-api-specs -> oci dbtools-runtime database-api-gateway-config-pool-api-spec list
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_api_spec_group, databasetoolsruntime_cli.list_database_tools_database_api_gateway_config_pool_api_specs, "list")

# oci dbtools-runtime database-api-gateway-config-pool-api-spec delete-database-tools-database-api-gateway-config-pool-api-spec -> oci dbtools-runtime database-api-gateway-config-pool-api-spec delete
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_api_spec_group, databasetoolsruntime_cli.delete_database_tools_database_api_gateway_config_pool_api_spec, "delete")


# Remove update from oci database-tools-runtime database-tools-database-api-gateway-config-pool-api-spec
databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_api_spec_group.commands.pop(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_pool_api_spec.name)


# Move update default-details command under oci dbtools-runtime database-api-gateway-config-pool-api-spec update
databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_api_spec_group.commands.pop(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_pool_api_spec_update_database_tools_database_api_gateway_config_pool_api_spec_default_details.name)


# oci dbtools-runtime database-api-gateway-config-pool-api-spec update
@click.command('update', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='Update database API gateway config pool API spec resources.')
@cli_util.help_option_group
def database_api_gateway_config_pool_api_spec_update_group():
    pass


databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_api_spec_group.add_command(database_api_gateway_config_pool_api_spec_update_group)
database_api_gateway_config_pool_api_spec_update_group.add_command(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_pool_api_spec_update_database_tools_database_api_gateway_config_pool_api_spec_default_details)

# oci dbtools-runtime database-api-gateway-config-pool-api-spec update update-database-tools-database-api-gateway-config-pool-api-spec-update-database-tools-database-api-gateway-config-pool-api-spec-default-details -> oci dbtools-runtime database-api-gateway-config-pool-api-spec update default
cli_util.rename_command(databasetoolsruntime_cli, database_api_gateway_config_pool_api_spec_update_group, databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_pool_api_spec_update_database_tools_database_api_gateway_config_pool_api_spec_default_details, "default")


# Remove create from oci database-tools-runtime database-tools-database-api-gateway-config-pool-auto-api-spec
databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_auto_api_spec_group.commands.pop(databasetoolsruntime_cli.create_database_tools_database_api_gateway_config_pool_auto_api_spec.name)


# Move create default-details command under oci dbtools-runtime database-api-gateway-config-pool-auto-api-spec create
databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_auto_api_spec_group.commands.pop(databasetoolsruntime_cli.create_database_tools_database_api_gateway_config_pool_auto_api_spec_create_database_tools_database_api_gateway_config_pool_auto_api_spec_default_details.name)


# oci dbtools-runtime database-api-gateway-config-pool-auto-api-spec create
@click.command('create', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='Create database API gateway config pool auto API spec resources.')
@cli_util.help_option_group
def database_api_gateway_config_pool_auto_api_spec_create_group():
    pass


databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_auto_api_spec_group.add_command(database_api_gateway_config_pool_auto_api_spec_create_group)
database_api_gateway_config_pool_auto_api_spec_create_group.add_command(databasetoolsruntime_cli.create_database_tools_database_api_gateway_config_pool_auto_api_spec_create_database_tools_database_api_gateway_config_pool_auto_api_spec_default_details)

# oci dbtools-runtime database-api-gateway-config-pool-auto-api-spec create create-database-tools-database-api-gateway-config-pool-auto-api-spec-create-database-tools-database-api-gateway-config-pool-auto-api-spec-default-details -> oci dbtools-runtime database-api-gateway-config-pool-auto-api-spec create default
cli_util.rename_command(databasetoolsruntime_cli, database_api_gateway_config_pool_auto_api_spec_create_group, databasetoolsruntime_cli.create_database_tools_database_api_gateway_config_pool_auto_api_spec_create_database_tools_database_api_gateway_config_pool_auto_api_spec_default_details, "default")

# oci dbtools-runtime database-api-gateway-config-pool-auto-api-spec list-database-tools-database-api-gateway-config-pool-auto-api-specs -> oci dbtools-runtime database-api-gateway-config-pool-auto-api-spec list
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_auto_api_spec_group, databasetoolsruntime_cli.list_database_tools_database_api_gateway_config_pool_auto_api_specs, "list")

# oci dbtools-runtime database-api-gateway-config-pool-auto-api-spec delete-database-tools-database-api-gateway-config-pool-auto-api-spec -> oci dbtools-runtime database-api-gateway-config-pool-auto-api-spec delete
cli_util.rename_command(databasetoolsruntime_cli, databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_auto_api_spec_group, databasetoolsruntime_cli.delete_database_tools_database_api_gateway_config_pool_auto_api_spec, "delete")


# Remove update from oci database-tools-runtime database-tools-database-api-gateway-config-pool-auto-api-spec
databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_auto_api_spec_group.commands.pop(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_pool_auto_api_spec.name)


# Move update default-details command under oci dbtools-runtime database-api-gateway-config-pool-auto-api-spec update
databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_auto_api_spec_group.commands.pop(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_pool_auto_api_spec_update_database_tools_database_api_gateway_config_pool_auto_api_spec_default_details.name)


# oci dbtools-runtime database-api-gateway-config-pool-auto-api-spec update
@click.command('update', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='Update database API gateway config pool auto API spec resources.')
@cli_util.help_option_group
def database_api_gateway_config_pool_auto_api_spec_update_group():
    pass


databasetoolsruntime_cli.database_tools_database_api_gateway_config_pool_auto_api_spec_group.add_command(database_api_gateway_config_pool_auto_api_spec_update_group)
database_api_gateway_config_pool_auto_api_spec_update_group.add_command(databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_pool_auto_api_spec_update_database_tools_database_api_gateway_config_pool_auto_api_spec_default_details)

# oci dbtools-runtime database-api-gateway-config-pool-auto-api-spec update update-database-tools-database-api-gateway-config-pool-auto-api-spec-update-database-tools-database-api-gateway-config-pool-auto-api-spec-default-details -> oci dbtools-runtime database-api-gateway-config-pool-auto-api-spec update default
cli_util.rename_command(databasetoolsruntime_cli, database_api_gateway_config_pool_auto_api_spec_update_group, databasetoolsruntime_cli.update_database_tools_database_api_gateway_config_pool_auto_api_spec_update_database_tools_database_api_gateway_config_pool_auto_api_spec_default_details, "default")


# Remove validate-database-tools-identity-credential from oci database-tools-runtime database-tools-identity
databasetoolsruntime_cli.database_tools_identity_group.commands.pop(databasetoolsruntime_cli.validate_database_tools_identity_credential.name)


# Move validate detail command under oci dbtools-runtime identity validate
databasetoolsruntime_cli.database_tools_identity_group.commands.pop(databasetoolsruntime_cli.validate_database_tools_identity_credential_validate_database_tools_identity_credential_oracle_database_resource_principal_details.name)


# oci dbtools-runtime identity validate
@click.command('validate', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help=databasetoolsruntime_cli.validate_database_tools_identity_credential.help)
@cli_util.help_option_group
def database_tools_identity_validate_group():
    pass


databasetoolsruntime_cli.database_tools_identity_group.add_command(database_tools_identity_validate_group)
database_tools_identity_validate_group.add_command(databasetoolsruntime_cli.validate_database_tools_identity_credential_validate_database_tools_identity_credential_oracle_database_resource_principal_details)

# oci dbtools-runtime identity validate validate-database-tools-identity-credential-validate-database-tools-identity-credential-oracle-database-resource-principal-details -> oci dbtools-runtime identity validate oracle-database-resource-principal
cli_util.rename_command(databasetoolsruntime_cli, database_tools_identity_validate_group, databasetoolsruntime_cli.validate_database_tools_identity_credential_validate_database_tools_identity_credential_oracle_database_resource_principal_details, "oracle-database-resource-principal")


# Remove update from oci database-tools-runtime property-set
databasetoolsruntime_cli.property_set_group.commands.pop(databasetoolsruntime_cli.update_property_set.name)


# Move property-set update detail commands under oci dbtools-runtime property-set update
databasetoolsruntime_cli.property_set_group.commands.pop(databasetoolsruntime_cli.update_property_set_update_property_set_apex_document_generator_details.name)
databasetoolsruntime_cli.property_set_group.commands.pop(databasetoolsruntime_cli.update_property_set_update_property_set_apex_fa_integration_details.name)
databasetoolsruntime_cli.property_set_group.commands.pop(databasetoolsruntime_cli.update_property_set_update_property_set_oracle_database_external_authentication_details.name)


# oci dbtools-runtime property-set update
@click.command('update', cls=databasetoolsruntime_cli.CommandGroupWithAlias, help='Update property set resources.')
@cli_util.help_option_group
def property_set_update_group():
    pass


databasetoolsruntime_cli.property_set_group.add_command(property_set_update_group)
property_set_update_group.add_command(databasetoolsruntime_cli.update_property_set_update_property_set_apex_document_generator_details)
property_set_update_group.add_command(databasetoolsruntime_cli.update_property_set_update_property_set_apex_fa_integration_details)
property_set_update_group.add_command(databasetoolsruntime_cli.update_property_set_update_property_set_oracle_database_external_authentication_details)

# oci dbtools-runtime property-set update update-property-set-update-property-set-apex-document-generator-details -> oci dbtools-runtime property-set update apex-document-generator-details
cli_util.rename_command(databasetoolsruntime_cli, property_set_update_group, databasetoolsruntime_cli.update_property_set_update_property_set_apex_document_generator_details, "apex-document-generator-details")
databasetoolsruntime_cli.update_property_set_update_property_set_apex_document_generator_details.help = 'Update the APEX Document Generator property set.'

# oci dbtools-runtime property-set update update-property-set-update-property-set-apex-fa-integration-details -> oci dbtools-runtime property-set update apex-fa-integration-details
cli_util.rename_command(databasetoolsruntime_cli, property_set_update_group, databasetoolsruntime_cli.update_property_set_update_property_set_apex_fa_integration_details, "apex-fa-integration-details")
databasetoolsruntime_cli.update_property_set_update_property_set_apex_fa_integration_details.help = 'Update the APEX FA Integration property set.'

# oci dbtools-runtime property-set update update-property-set-update-property-set-oracle-database-external-authentication-details -> oci dbtools-runtime property-set update oracle-database-external-authentication-details
cli_util.rename_command(databasetoolsruntime_cli, property_set_update_group, databasetoolsruntime_cli.update_property_set_update_property_set_oracle_database_external_authentication_details, "oracle-database-external-authentication-details")
databasetoolsruntime_cli.update_property_set_update_property_set_oracle_database_external_authentication_details.help = 'Update the Oracle Database External Authentication property set.'


# oci database-tools-runtime database-tools-connection create-credential-create-credential-basic-details -> oci database-tools-runtime credential
databasetoolsruntime_cli.database_tools_connection_group.commands.pop(databasetoolsruntime_cli.create_credential_create_credential_basic_details.name, None)

# Ensure create-credential-create-credential-basic-details is removed from oci dbtools-runtime connection
databasetoolsruntime_cli.database_tools_connection_group.commands.pop("create-credential-create-credential-basic-details", None)


# Final credential list registration: add it at the very end so no later mutation can overwrite/remove it.
databasetoolsruntime_cli.credential_group.commands.pop('list', None)
databasetoolsruntime_cli.credential_group.add_command(credential_list_extended)
