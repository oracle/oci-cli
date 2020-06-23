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


@cli.command(cli_util.override('data_integration.data_integration_root_group.command_name', 'data-integration'), cls=CommandGroupWithAlias, help=cli_util.override('data_integration.data_integration_root_group.help', """Use the Data Integration Service APIs to perform common extract, load, and transform (ETL) tasks."""), short_help=cli_util.override('data_integration.data_integration_root_group.short_help', """Data Integration API"""))
@cli_util.help_option_group
def data_integration_root_group():
    pass


@click.command(cli_util.override('data_integration.task_run_log_group.command_name', 'task-run-log'), cls=CommandGroupWithAlias, help="""A log message from the execution of a task.""")
@cli_util.help_option_group
def task_run_log_group():
    pass


@click.command(cli_util.override('data_integration.schema_group.command_name', 'schema'), cls=CommandGroupWithAlias, help="""The schema object.""")
@cli_util.help_option_group
def schema_group():
    pass


@click.command(cli_util.override('data_integration.workspace_group.command_name', 'workspace'), cls=CommandGroupWithAlias, help="""A workspace is an organizational construct to keep multiple data integration solutions and their resources (data assets, data flows, tasks, and so on) separate from each other, helping you to stay organized. For example, you could have separate workspaces for development, testing, and production.""")
@cli_util.help_option_group
def workspace_group():
    pass


@click.command(cli_util.override('data_integration.task_run_group.command_name', 'task-run'), cls=CommandGroupWithAlias, help="""The information about TaskRun.""")
@cli_util.help_option_group
def task_run_group():
    pass


@click.command(cli_util.override('data_integration.task_validation_group.command_name', 'task-validation'), cls=CommandGroupWithAlias, help="""The information about task validation""")
@cli_util.help_option_group
def task_validation_group():
    pass


@click.command(cli_util.override('data_integration.connection_validation_group.command_name', 'connection-validation'), cls=CommandGroupWithAlias, help="""The information about connection validation""")
@cli_util.help_option_group
def connection_validation_group():
    pass


@click.command(cli_util.override('data_integration.project_group.command_name', 'project'), cls=CommandGroupWithAlias, help="""The project type contains the audit summary information and the definition of the project.""")
@cli_util.help_option_group
def project_group():
    pass


@click.command(cli_util.override('data_integration.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""The API operations used to create and configure Data Integration resources do not take effect immediately. In these cases, the operation spawns an asynchronous workflow to fulfill the request. Work requests provide visibility into the status of these in-progress, long-running asynchronous workflows.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('data_integration.data_flow_group.command_name', 'data-flow'), cls=CommandGroupWithAlias, help="""The data flow type contains the audit summary information and the definition of the data flow.""")
@cli_util.help_option_group
def data_flow_group():
    pass


@click.command(cli_util.override('data_integration.data_entity_group.command_name', 'data-entity'), cls=CommandGroupWithAlias, help="""The data entity object.""")
@cli_util.help_option_group
def data_entity_group():
    pass


@click.command(cli_util.override('data_integration.data_flow_validation_group.command_name', 'data-flow-validation'), cls=CommandGroupWithAlias, help="""The information about dataflow validation""")
@cli_util.help_option_group
def data_flow_validation_group():
    pass


@click.command(cli_util.override('data_integration.folder_group.command_name', 'folder'), cls=CommandGroupWithAlias, help="""The folder type contains the audit summary information and the definition of the folder.""")
@cli_util.help_option_group
def folder_group():
    pass


@click.command(cli_util.override('data_integration.task_group.command_name', 'task'), cls=CommandGroupWithAlias, help="""The task type contains the audit summary information and the definition of the task.""")
@cli_util.help_option_group
def task_group():
    pass


@click.command(cli_util.override('data_integration.application_group.command_name', 'application'), cls=CommandGroupWithAlias, help="""The application type contains the audit summary information and the definition of the application.""")
@cli_util.help_option_group
def application_group():
    pass


@click.command(cli_util.override('data_integration.data_asset_group.command_name', 'data-asset'), cls=CommandGroupWithAlias, help="""The data asset type.""")
@cli_util.help_option_group
def data_asset_group():
    pass


@click.command(cli_util.override('data_integration.connection_group.command_name', 'connection'), cls=CommandGroupWithAlias, help="""The connection object.""")
@cli_util.help_option_group
def connection_group():
    pass


data_integration_root_group.add_command(task_run_log_group)
data_integration_root_group.add_command(schema_group)
data_integration_root_group.add_command(workspace_group)
data_integration_root_group.add_command(task_run_group)
data_integration_root_group.add_command(task_validation_group)
data_integration_root_group.add_command(connection_validation_group)
data_integration_root_group.add_command(project_group)
data_integration_root_group.add_command(work_request_group)
data_integration_root_group.add_command(data_flow_group)
data_integration_root_group.add_command(data_entity_group)
data_integration_root_group.add_command(data_flow_validation_group)
data_integration_root_group.add_command(folder_group)
data_integration_root_group.add_command(task_group)
data_integration_root_group.add_command(application_group)
data_integration_root_group.add_command(data_asset_group)
data_integration_root_group.add_command(connection_group)


@workspace_group.command(name=cli_util.override('data_integration.change_compartment.command_name', 'change-compartment'), help=u"""The workspace will be moved to the desired compartment.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment to move the the workspace to.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, workspace_id, compartment_id, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.change_compartment(
        workspace_id=workspace_id,
        change_compartment_details=_details,
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


@application_group.command(name=cli_util.override('data_integration.create_application.command_name', 'create'), help=u"""Creates an application.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--key', help=u"""Currently not used on application creation. Reserved for future.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--model-type', type=custom_types.CliCaseInsensitiveChoice(["INTEGRATION_APPLICATION"]), help=u"""The type of the application.""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Application'})
@cli_util.wrap_exceptions
def create_application(ctx, from_json, workspace_id, name, identifier, key, model_version, model_type, description, object_status, registry_metadata):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if model_type is not None:
        _details['modelType'] = model_type

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_application(
        workspace_id=workspace_id,
        create_application_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_integration.create_connection.command_name', 'create'), help=u"""Creates a connection under an existing data asset.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--model-type', type=custom_types.CliCaseInsensitiveChoice(["ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION"]), help=u"""The type of the connection.""")
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection(ctx, from_json, workspace_id, name, identifier, model_type, key, model_version, parent_ref, description, object_status, connection_properties, registry_metadata):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier

    if model_type is not None:
        _details['modelType'] = model_type

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if connection_properties is not None:
        _details['connectionProperties'] = cli_util.parse_json_parameter("connection_properties", connection_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection(
        workspace_id=workspace_id,
        create_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_integration.create_connection_create_connection_from_atp.command_name', 'create-connection-create-connection-from-atp'), help=u"""Creates a connection under an existing data asset.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--username', help=u"""The user name for the connection.""")
@cli_util.option('--password', help=u"""The password for the connection.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_connection_from_atp(ctx, from_json, workspace_id, name, identifier, key, model_version, parent_ref, description, object_status, connection_properties, registry_metadata, username, password):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if connection_properties is not None:
        _details['connectionProperties'] = cli_util.parse_json_parameter("connection_properties", connection_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if username is not None:
        _details['username'] = username

    if password is not None:
        _details['password'] = password

    _details['modelType'] = 'ORACLE_ATP_CONNECTION'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection(
        workspace_id=workspace_id,
        create_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_integration.create_connection_create_connection_from_adwc.command_name', 'create-connection-create-connection-from-adwc'), help=u"""Creates a connection under an existing data asset.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--username', help=u"""The user name for the connection.""")
@cli_util.option('--password', help=u"""The password for the connection.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_connection_from_adwc(ctx, from_json, workspace_id, name, identifier, key, model_version, parent_ref, description, object_status, connection_properties, registry_metadata, username, password):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if connection_properties is not None:
        _details['connectionProperties'] = cli_util.parse_json_parameter("connection_properties", connection_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if username is not None:
        _details['username'] = username

    if password is not None:
        _details['password'] = password

    _details['modelType'] = 'ORACLE_ADWC_CONNECTION'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection(
        workspace_id=workspace_id,
        create_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_integration.create_connection_create_connection_from_oracle.command_name', 'create-connection-create-connection-from-oracle'), help=u"""Creates a connection under an existing data asset.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--username', help=u"""The user name for the connection.""")
@cli_util.option('--password', help=u"""The password for the connection.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_connection_from_oracle(ctx, from_json, workspace_id, name, identifier, key, model_version, parent_ref, description, object_status, connection_properties, registry_metadata, username, password):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if connection_properties is not None:
        _details['connectionProperties'] = cli_util.parse_json_parameter("connection_properties", connection_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if username is not None:
        _details['username'] = username

    if password is not None:
        _details['password'] = password

    _details['modelType'] = 'ORACLEDB_CONNECTION'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection(
        workspace_id=workspace_id,
        create_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_integration.create_connection_create_connection_from_object_storage.command_name', 'create-connection-create-connection-from-object-storage'), help=u"""Creates a connection under an existing data asset.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--credential-file-content', help=u"""The credential file content from a wallet for the data asset.""")
@cli_util.option('--user-id', help=u"""The OCI user OCID for the user to connect to.""")
@cli_util.option('--finger-print', help=u"""The fingeprint for the user.""")
@cli_util.option('--pass-phrase', help=u"""The pass phrase for the connection.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection_create_connection_from_object_storage(ctx, from_json, workspace_id, name, identifier, key, model_version, parent_ref, description, object_status, connection_properties, registry_metadata, credential_file_content, user_id, finger_print, pass_phrase):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if connection_properties is not None:
        _details['connectionProperties'] = cli_util.parse_json_parameter("connection_properties", connection_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if credential_file_content is not None:
        _details['credentialFileContent'] = credential_file_content

    if user_id is not None:
        _details['userId'] = user_id

    if finger_print is not None:
        _details['fingerPrint'] = finger_print

    if pass_phrase is not None:
        _details['passPhrase'] = pass_phrase

    _details['modelType'] = 'ORACLE_OBJECT_STORAGE_CONNECTION'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection(
        workspace_id=workspace_id,
        create_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_validation_group.command(name=cli_util.override('data_integration.create_connection_validation.command_name', 'create'), help=u"""Creates a connection validation.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'data-asset': {'module': 'data_integration', 'class': 'CreateDataAssetDetails'}, 'connection': {'module': 'data_integration', 'class': 'CreateConnectionDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'data-asset': {'module': 'data_integration', 'class': 'CreateDataAssetDetails'}, 'connection': {'module': 'data_integration', 'class': 'CreateConnectionDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'ConnectionValidation'})
@cli_util.wrap_exceptions
def create_connection_validation(ctx, from_json, workspace_id, data_asset, connection, registry_metadata):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection_validation(
        workspace_id=workspace_id,
        create_connection_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_validation_group.command(name=cli_util.override('data_integration.create_connection_validation_create_data_asset_from_oracle.command_name', 'create-connection-validation-create-data-asset-from-oracle'), help=u"""Creates a connection validation.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-asset-name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--data-asset-identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset-key', help=u"""Currently not used on data asset creation. Reserved for future.""")
@cli_util.option('--data-asset-model-version', help=u"""The model version of an object.""")
@cli_util.option('--data-asset-description', help=u"""Detailed description for the object.""")
@cli_util.option('--data-asset-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-asset-external-key', help=u"""The external key for the object""")
@cli_util.option('--data-asset-asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset-registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset-host', help=u"""The host details for the data asset.""")
@cli_util.option('--data-asset-port', help=u"""The port details for the data asset.""")
@cli_util.option('--data-asset-service-name', help=u"""The service name for the data asset.""")
@cli_util.option('--data-asset-driver-class', help=u"""The driver class for the data asset.""")
@cli_util.option('--data-asset-sid', help=u"""sid""")
@cli_util.option('--data-asset-credential-file-content', help=u"""The credential file content from a wallet for the data asset.""")
@cli_util.option('--data-asset-default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'connection': {'module': 'data_integration', 'class': 'CreateConnectionDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'data-asset-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromOracle'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection': {'module': 'data_integration', 'class': 'CreateConnectionDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'data-asset-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromOracle'}}, output_type={'module': 'data_integration', 'class': 'ConnectionValidation'})
@cli_util.wrap_exceptions
def create_connection_validation_create_data_asset_from_oracle(ctx, from_json, workspace_id, data_asset_name, data_asset_identifier, connection, registry_metadata, data_asset_key, data_asset_model_version, data_asset_description, data_asset_object_status, data_asset_external_key, data_asset_asset_properties, data_asset_registry_metadata, data_asset_host, data_asset_port, data_asset_service_name, data_asset_driver_class, data_asset_sid, data_asset_credential_file_content, data_asset_default_connection):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataAsset'] = {}
    _details['dataAsset']['name'] = data_asset_name
    _details['dataAsset']['identifier'] = data_asset_identifier

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if data_asset_key is not None:
        _details['dataAsset']['key'] = data_asset_key

    if data_asset_model_version is not None:
        _details['dataAsset']['modelVersion'] = data_asset_model_version

    if data_asset_description is not None:
        _details['dataAsset']['description'] = data_asset_description

    if data_asset_object_status is not None:
        _details['dataAsset']['objectStatus'] = data_asset_object_status

    if data_asset_external_key is not None:
        _details['dataAsset']['externalKey'] = data_asset_external_key

    if data_asset_asset_properties is not None:
        _details['dataAsset']['assetProperties'] = cli_util.parse_json_parameter("data_asset_asset_properties", data_asset_asset_properties)

    if data_asset_registry_metadata is not None:
        _details['dataAsset']['registryMetadata'] = cli_util.parse_json_parameter("data_asset_registry_metadata", data_asset_registry_metadata)

    if data_asset_host is not None:
        _details['dataAsset']['host'] = data_asset_host

    if data_asset_port is not None:
        _details['dataAsset']['port'] = data_asset_port

    if data_asset_service_name is not None:
        _details['dataAsset']['serviceName'] = data_asset_service_name

    if data_asset_driver_class is not None:
        _details['dataAsset']['driverClass'] = data_asset_driver_class

    if data_asset_sid is not None:
        _details['dataAsset']['sid'] = data_asset_sid

    if data_asset_credential_file_content is not None:
        _details['dataAsset']['credentialFileContent'] = data_asset_credential_file_content

    if data_asset_default_connection is not None:
        _details['dataAsset']['defaultConnection'] = cli_util.parse_json_parameter("data_asset_default_connection", data_asset_default_connection)

    _details['dataAsset']['modelType'] = 'ORACLE_DATA_ASSET'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection_validation(
        workspace_id=workspace_id,
        create_connection_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_validation_group.command(name=cli_util.override('data_integration.create_connection_validation_create_data_asset_from_adwc.command_name', 'create-connection-validation-create-data-asset-from-adwc'), help=u"""Creates a connection validation.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-asset-name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--data-asset-identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset-key', help=u"""Currently not used on data asset creation. Reserved for future.""")
@cli_util.option('--data-asset-model-version', help=u"""The model version of an object.""")
@cli_util.option('--data-asset-description', help=u"""Detailed description for the object.""")
@cli_util.option('--data-asset-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-asset-external-key', help=u"""The external key for the object""")
@cli_util.option('--data-asset-asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset-registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset-service-name', help=u"""The service name for the data asset.""")
@cli_util.option('--data-asset-driver-class', help=u"""The driver class for the data asset.""")
@cli_util.option('--data-asset-credential-file-content', help=u"""The credential file content from a wallet for the data asset.""")
@cli_util.option('--data-asset-default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'connection': {'module': 'data_integration', 'class': 'CreateConnectionDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'data-asset-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromAdwc'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection': {'module': 'data_integration', 'class': 'CreateConnectionDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'data-asset-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromAdwc'}}, output_type={'module': 'data_integration', 'class': 'ConnectionValidation'})
@cli_util.wrap_exceptions
def create_connection_validation_create_data_asset_from_adwc(ctx, from_json, workspace_id, data_asset_name, data_asset_identifier, connection, registry_metadata, data_asset_key, data_asset_model_version, data_asset_description, data_asset_object_status, data_asset_external_key, data_asset_asset_properties, data_asset_registry_metadata, data_asset_service_name, data_asset_driver_class, data_asset_credential_file_content, data_asset_default_connection):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataAsset'] = {}
    _details['dataAsset']['name'] = data_asset_name
    _details['dataAsset']['identifier'] = data_asset_identifier

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if data_asset_key is not None:
        _details['dataAsset']['key'] = data_asset_key

    if data_asset_model_version is not None:
        _details['dataAsset']['modelVersion'] = data_asset_model_version

    if data_asset_description is not None:
        _details['dataAsset']['description'] = data_asset_description

    if data_asset_object_status is not None:
        _details['dataAsset']['objectStatus'] = data_asset_object_status

    if data_asset_external_key is not None:
        _details['dataAsset']['externalKey'] = data_asset_external_key

    if data_asset_asset_properties is not None:
        _details['dataAsset']['assetProperties'] = cli_util.parse_json_parameter("data_asset_asset_properties", data_asset_asset_properties)

    if data_asset_registry_metadata is not None:
        _details['dataAsset']['registryMetadata'] = cli_util.parse_json_parameter("data_asset_registry_metadata", data_asset_registry_metadata)

    if data_asset_service_name is not None:
        _details['dataAsset']['serviceName'] = data_asset_service_name

    if data_asset_driver_class is not None:
        _details['dataAsset']['driverClass'] = data_asset_driver_class

    if data_asset_credential_file_content is not None:
        _details['dataAsset']['credentialFileContent'] = data_asset_credential_file_content

    if data_asset_default_connection is not None:
        _details['dataAsset']['defaultConnection'] = cli_util.parse_json_parameter("data_asset_default_connection", data_asset_default_connection)

    _details['dataAsset']['modelType'] = 'ORACLE_ADWC_DATA_ASSET'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection_validation(
        workspace_id=workspace_id,
        create_connection_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_validation_group.command(name=cli_util.override('data_integration.create_connection_validation_create_data_asset_from_atp.command_name', 'create-connection-validation-create-data-asset-from-atp'), help=u"""Creates a connection validation.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-asset-name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--data-asset-identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset-key', help=u"""Currently not used on data asset creation. Reserved for future.""")
@cli_util.option('--data-asset-model-version', help=u"""The model version of an object.""")
@cli_util.option('--data-asset-description', help=u"""Detailed description for the object.""")
@cli_util.option('--data-asset-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-asset-external-key', help=u"""The external key for the object""")
@cli_util.option('--data-asset-asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset-registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset-service-name', help=u"""The service name for the data asset.""")
@cli_util.option('--data-asset-driver-class', help=u"""The driver class for the data asset.""")
@cli_util.option('--data-asset-credential-file-content', help=u"""The credential file content from a wallet for the data asset.""")
@cli_util.option('--data-asset-default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'connection': {'module': 'data_integration', 'class': 'CreateConnectionDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'data-asset-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromAtp'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection': {'module': 'data_integration', 'class': 'CreateConnectionDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'data-asset-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromAtp'}}, output_type={'module': 'data_integration', 'class': 'ConnectionValidation'})
@cli_util.wrap_exceptions
def create_connection_validation_create_data_asset_from_atp(ctx, from_json, workspace_id, data_asset_name, data_asset_identifier, connection, registry_metadata, data_asset_key, data_asset_model_version, data_asset_description, data_asset_object_status, data_asset_external_key, data_asset_asset_properties, data_asset_registry_metadata, data_asset_service_name, data_asset_driver_class, data_asset_credential_file_content, data_asset_default_connection):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataAsset'] = {}
    _details['dataAsset']['name'] = data_asset_name
    _details['dataAsset']['identifier'] = data_asset_identifier

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if data_asset_key is not None:
        _details['dataAsset']['key'] = data_asset_key

    if data_asset_model_version is not None:
        _details['dataAsset']['modelVersion'] = data_asset_model_version

    if data_asset_description is not None:
        _details['dataAsset']['description'] = data_asset_description

    if data_asset_object_status is not None:
        _details['dataAsset']['objectStatus'] = data_asset_object_status

    if data_asset_external_key is not None:
        _details['dataAsset']['externalKey'] = data_asset_external_key

    if data_asset_asset_properties is not None:
        _details['dataAsset']['assetProperties'] = cli_util.parse_json_parameter("data_asset_asset_properties", data_asset_asset_properties)

    if data_asset_registry_metadata is not None:
        _details['dataAsset']['registryMetadata'] = cli_util.parse_json_parameter("data_asset_registry_metadata", data_asset_registry_metadata)

    if data_asset_service_name is not None:
        _details['dataAsset']['serviceName'] = data_asset_service_name

    if data_asset_driver_class is not None:
        _details['dataAsset']['driverClass'] = data_asset_driver_class

    if data_asset_credential_file_content is not None:
        _details['dataAsset']['credentialFileContent'] = data_asset_credential_file_content

    if data_asset_default_connection is not None:
        _details['dataAsset']['defaultConnection'] = cli_util.parse_json_parameter("data_asset_default_connection", data_asset_default_connection)

    _details['dataAsset']['modelType'] = 'ORACLE_ATP_DATA_ASSET'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection_validation(
        workspace_id=workspace_id,
        create_connection_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_validation_group.command(name=cli_util.override('data_integration.create_connection_validation_create_data_asset_from_object_storage.command_name', 'create-connection-validation-create-data-asset-from-object-storage'), help=u"""Creates a connection validation.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-asset-name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--data-asset-identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset-key', help=u"""Currently not used on data asset creation. Reserved for future.""")
@cli_util.option('--data-asset-model-version', help=u"""The model version of an object.""")
@cli_util.option('--data-asset-description', help=u"""Detailed description for the object.""")
@cli_util.option('--data-asset-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--data-asset-external-key', help=u"""The external key for the object""")
@cli_util.option('--data-asset-asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset-registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-asset-url', help=u"""url""")
@cli_util.option('--data-asset-tenancy-id', help=u"""The OCI tenancy OCID.""")
@cli_util.option('--data-asset-namespace', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--data-asset-default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'connection': {'module': 'data_integration', 'class': 'CreateConnectionDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'data-asset-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromObjectStorage'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection': {'module': 'data_integration', 'class': 'CreateConnectionDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'data-asset-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-asset-default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromObjectStorage'}}, output_type={'module': 'data_integration', 'class': 'ConnectionValidation'})
@cli_util.wrap_exceptions
def create_connection_validation_create_data_asset_from_object_storage(ctx, from_json, workspace_id, data_asset_name, data_asset_identifier, connection, registry_metadata, data_asset_key, data_asset_model_version, data_asset_description, data_asset_object_status, data_asset_external_key, data_asset_asset_properties, data_asset_registry_metadata, data_asset_url, data_asset_tenancy_id, data_asset_namespace, data_asset_default_connection):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dataAsset'] = {}
    _details['dataAsset']['name'] = data_asset_name
    _details['dataAsset']['identifier'] = data_asset_identifier

    if connection is not None:
        _details['connection'] = cli_util.parse_json_parameter("connection", connection)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if data_asset_key is not None:
        _details['dataAsset']['key'] = data_asset_key

    if data_asset_model_version is not None:
        _details['dataAsset']['modelVersion'] = data_asset_model_version

    if data_asset_description is not None:
        _details['dataAsset']['description'] = data_asset_description

    if data_asset_object_status is not None:
        _details['dataAsset']['objectStatus'] = data_asset_object_status

    if data_asset_external_key is not None:
        _details['dataAsset']['externalKey'] = data_asset_external_key

    if data_asset_asset_properties is not None:
        _details['dataAsset']['assetProperties'] = cli_util.parse_json_parameter("data_asset_asset_properties", data_asset_asset_properties)

    if data_asset_registry_metadata is not None:
        _details['dataAsset']['registryMetadata'] = cli_util.parse_json_parameter("data_asset_registry_metadata", data_asset_registry_metadata)

    if data_asset_url is not None:
        _details['dataAsset']['url'] = data_asset_url

    if data_asset_tenancy_id is not None:
        _details['dataAsset']['tenancyId'] = data_asset_tenancy_id

    if data_asset_namespace is not None:
        _details['dataAsset']['namespace'] = data_asset_namespace

    if data_asset_default_connection is not None:
        _details['dataAsset']['defaultConnection'] = cli_util.parse_json_parameter("data_asset_default_connection", data_asset_default_connection)

    _details['dataAsset']['modelType'] = 'ORACLE_OBJECT_STORAGE_DATA_ASSET'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection_validation(
        workspace_id=workspace_id,
        create_connection_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_validation_group.command(name=cli_util.override('data_integration.create_connection_validation_create_connection_from_atp.command_name', 'create-connection-validation-create-connection-from-atp'), help=u"""Creates a connection validation.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--connection-identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-key', help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--connection-model-version', help=u"""The model version of an object.""")
@cli_util.option('--connection-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-description', help=u"""Detailed description for the object.""")
@cli_util.option('--connection-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--connection-connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-username', help=u"""The user name for the connection.""")
@cli_util.option('--connection-password', help=u"""The password for the connection.""")
@json_skeleton_utils.get_cli_json_input_option({'data-asset': {'module': 'data_integration', 'class': 'CreateDataAssetDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'connection-parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'connection-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'data-asset': {'module': 'data_integration', 'class': 'CreateDataAssetDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'connection-parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'connection-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'ConnectionValidation'})
@cli_util.wrap_exceptions
def create_connection_validation_create_connection_from_atp(ctx, from_json, workspace_id, connection_name, connection_identifier, data_asset, registry_metadata, connection_key, connection_model_version, connection_parent_ref, connection_description, connection_object_status, connection_connection_properties, connection_registry_metadata, connection_username, connection_password):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['connection'] = {}
    _details['connection']['name'] = connection_name
    _details['connection']['identifier'] = connection_identifier

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if connection_key is not None:
        _details['connection']['key'] = connection_key

    if connection_model_version is not None:
        _details['connection']['modelVersion'] = connection_model_version

    if connection_parent_ref is not None:
        _details['connection']['parentRef'] = cli_util.parse_json_parameter("connection_parent_ref", connection_parent_ref)

    if connection_description is not None:
        _details['connection']['description'] = connection_description

    if connection_object_status is not None:
        _details['connection']['objectStatus'] = connection_object_status

    if connection_connection_properties is not None:
        _details['connection']['connectionProperties'] = cli_util.parse_json_parameter("connection_connection_properties", connection_connection_properties)

    if connection_registry_metadata is not None:
        _details['connection']['registryMetadata'] = cli_util.parse_json_parameter("connection_registry_metadata", connection_registry_metadata)

    if connection_username is not None:
        _details['connection']['username'] = connection_username

    if connection_password is not None:
        _details['connection']['password'] = connection_password

    _details['connection']['modelType'] = 'ORACLE_ATP_CONNECTION'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection_validation(
        workspace_id=workspace_id,
        create_connection_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_validation_group.command(name=cli_util.override('data_integration.create_connection_validation_create_connection_from_adwc.command_name', 'create-connection-validation-create-connection-from-adwc'), help=u"""Creates a connection validation.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--connection-identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-key', help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--connection-model-version', help=u"""The model version of an object.""")
@cli_util.option('--connection-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-description', help=u"""Detailed description for the object.""")
@cli_util.option('--connection-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--connection-connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-username', help=u"""The user name for the connection.""")
@cli_util.option('--connection-password', help=u"""The password for the connection.""")
@json_skeleton_utils.get_cli_json_input_option({'data-asset': {'module': 'data_integration', 'class': 'CreateDataAssetDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'connection-parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'connection-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'data-asset': {'module': 'data_integration', 'class': 'CreateDataAssetDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'connection-parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'connection-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'ConnectionValidation'})
@cli_util.wrap_exceptions
def create_connection_validation_create_connection_from_adwc(ctx, from_json, workspace_id, connection_name, connection_identifier, data_asset, registry_metadata, connection_key, connection_model_version, connection_parent_ref, connection_description, connection_object_status, connection_connection_properties, connection_registry_metadata, connection_username, connection_password):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['connection'] = {}
    _details['connection']['name'] = connection_name
    _details['connection']['identifier'] = connection_identifier

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if connection_key is not None:
        _details['connection']['key'] = connection_key

    if connection_model_version is not None:
        _details['connection']['modelVersion'] = connection_model_version

    if connection_parent_ref is not None:
        _details['connection']['parentRef'] = cli_util.parse_json_parameter("connection_parent_ref", connection_parent_ref)

    if connection_description is not None:
        _details['connection']['description'] = connection_description

    if connection_object_status is not None:
        _details['connection']['objectStatus'] = connection_object_status

    if connection_connection_properties is not None:
        _details['connection']['connectionProperties'] = cli_util.parse_json_parameter("connection_connection_properties", connection_connection_properties)

    if connection_registry_metadata is not None:
        _details['connection']['registryMetadata'] = cli_util.parse_json_parameter("connection_registry_metadata", connection_registry_metadata)

    if connection_username is not None:
        _details['connection']['username'] = connection_username

    if connection_password is not None:
        _details['connection']['password'] = connection_password

    _details['connection']['modelType'] = 'ORACLE_ADWC_CONNECTION'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection_validation(
        workspace_id=workspace_id,
        create_connection_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_validation_group.command(name=cli_util.override('data_integration.create_connection_validation_create_connection_from_oracle.command_name', 'create-connection-validation-create-connection-from-oracle'), help=u"""Creates a connection validation.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--connection-identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-key', help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--connection-model-version', help=u"""The model version of an object.""")
@cli_util.option('--connection-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-description', help=u"""Detailed description for the object.""")
@cli_util.option('--connection-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--connection-connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-username', help=u"""The user name for the connection.""")
@cli_util.option('--connection-password', help=u"""The password for the connection.""")
@json_skeleton_utils.get_cli_json_input_option({'data-asset': {'module': 'data_integration', 'class': 'CreateDataAssetDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'connection-parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'connection-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'data-asset': {'module': 'data_integration', 'class': 'CreateDataAssetDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'connection-parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'connection-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'ConnectionValidation'})
@cli_util.wrap_exceptions
def create_connection_validation_create_connection_from_oracle(ctx, from_json, workspace_id, connection_name, connection_identifier, data_asset, registry_metadata, connection_key, connection_model_version, connection_parent_ref, connection_description, connection_object_status, connection_connection_properties, connection_registry_metadata, connection_username, connection_password):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['connection'] = {}
    _details['connection']['name'] = connection_name
    _details['connection']['identifier'] = connection_identifier

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if connection_key is not None:
        _details['connection']['key'] = connection_key

    if connection_model_version is not None:
        _details['connection']['modelVersion'] = connection_model_version

    if connection_parent_ref is not None:
        _details['connection']['parentRef'] = cli_util.parse_json_parameter("connection_parent_ref", connection_parent_ref)

    if connection_description is not None:
        _details['connection']['description'] = connection_description

    if connection_object_status is not None:
        _details['connection']['objectStatus'] = connection_object_status

    if connection_connection_properties is not None:
        _details['connection']['connectionProperties'] = cli_util.parse_json_parameter("connection_connection_properties", connection_connection_properties)

    if connection_registry_metadata is not None:
        _details['connection']['registryMetadata'] = cli_util.parse_json_parameter("connection_registry_metadata", connection_registry_metadata)

    if connection_username is not None:
        _details['connection']['username'] = connection_username

    if connection_password is not None:
        _details['connection']['password'] = connection_password

    _details['connection']['modelType'] = 'ORACLEDB_CONNECTION'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection_validation(
        workspace_id=workspace_id,
        create_connection_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_validation_group.command(name=cli_util.override('data_integration.create_connection_validation_create_connection_from_object_storage.command_name', 'create-connection-validation-create-connection-from-object-storage'), help=u"""Creates a connection validation.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--connection-identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--data-asset', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-key', help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--connection-model-version', help=u"""The model version of an object.""")
@cli_util.option('--connection-parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-description', help=u"""Detailed description for the object.""")
@cli_util.option('--connection-object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--connection-connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-credential-file-content', help=u"""The credential file content from a wallet for the data asset.""")
@cli_util.option('--connection-user-id', help=u"""The OCI user OCID for the user to connect to.""")
@cli_util.option('--connection-finger-print', help=u"""The fingeprint for the user.""")
@cli_util.option('--connection-pass-phrase', help=u"""The pass phrase for the connection.""")
@json_skeleton_utils.get_cli_json_input_option({'data-asset': {'module': 'data_integration', 'class': 'CreateDataAssetDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'connection-parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'connection-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'data-asset': {'module': 'data_integration', 'class': 'CreateDataAssetDetails'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'connection-parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'connection-registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'ConnectionValidation'})
@cli_util.wrap_exceptions
def create_connection_validation_create_connection_from_object_storage(ctx, from_json, workspace_id, connection_name, connection_identifier, data_asset, registry_metadata, connection_key, connection_model_version, connection_parent_ref, connection_description, connection_object_status, connection_connection_properties, connection_registry_metadata, connection_credential_file_content, connection_user_id, connection_finger_print, connection_pass_phrase):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['connection'] = {}
    _details['connection']['name'] = connection_name
    _details['connection']['identifier'] = connection_identifier

    if data_asset is not None:
        _details['dataAsset'] = cli_util.parse_json_parameter("data_asset", data_asset)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if connection_key is not None:
        _details['connection']['key'] = connection_key

    if connection_model_version is not None:
        _details['connection']['modelVersion'] = connection_model_version

    if connection_parent_ref is not None:
        _details['connection']['parentRef'] = cli_util.parse_json_parameter("connection_parent_ref", connection_parent_ref)

    if connection_description is not None:
        _details['connection']['description'] = connection_description

    if connection_object_status is not None:
        _details['connection']['objectStatus'] = connection_object_status

    if connection_connection_properties is not None:
        _details['connection']['connectionProperties'] = cli_util.parse_json_parameter("connection_connection_properties", connection_connection_properties)

    if connection_registry_metadata is not None:
        _details['connection']['registryMetadata'] = cli_util.parse_json_parameter("connection_registry_metadata", connection_registry_metadata)

    if connection_credential_file_content is not None:
        _details['connection']['credentialFileContent'] = connection_credential_file_content

    if connection_user_id is not None:
        _details['connection']['userId'] = connection_user_id

    if connection_finger_print is not None:
        _details['connection']['fingerPrint'] = connection_finger_print

    if connection_pass_phrase is not None:
        _details['connection']['passPhrase'] = connection_pass_phrase

    _details['connection']['modelType'] = 'ORACLE_OBJECT_STORAGE_CONNECTION'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_connection_validation(
        workspace_id=workspace_id,
        create_connection_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_integration.create_data_asset.command_name', 'create'), help=u"""Creates a data asset with default connection.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--model-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET"]), help=u"""The type of the data asset.""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--key', help=u"""Currently not used on data asset creation. Reserved for future.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset(ctx, from_json, workspace_id, model_type, name, identifier, key, model_version, description, object_status, external_key, asset_properties, registry_metadata):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelType'] = model_type
    _details['name'] = name
    _details['identifier'] = identifier

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if external_key is not None:
        _details['externalKey'] = external_key

    if asset_properties is not None:
        _details['assetProperties'] = cli_util.parse_json_parameter("asset_properties", asset_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_data_asset(
        workspace_id=workspace_id,
        create_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_integration.create_data_asset_create_data_asset_from_oracle.command_name', 'create-data-asset-create-data-asset-from-oracle'), help=u"""Creates a data asset with default connection.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--key', help=u"""Currently not used on data asset creation. Reserved for future.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--host', help=u"""The host details for the data asset.""")
@cli_util.option('--port', help=u"""The port details for the data asset.""")
@cli_util.option('--service-name', help=u"""The service name for the data asset.""")
@cli_util.option('--driver-class', help=u"""The driver class for the data asset.""")
@cli_util.option('--sid', help=u"""sid""")
@cli_util.option('--credential-file-content', help=u"""The credential file content from a wallet for the data asset.""")
@cli_util.option('--default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromOracle'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromOracle'}}, output_type={'module': 'data_integration', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset_create_data_asset_from_oracle(ctx, from_json, workspace_id, name, identifier, key, model_version, description, object_status, external_key, asset_properties, registry_metadata, host, port, service_name, driver_class, sid, credential_file_content, default_connection):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if external_key is not None:
        _details['externalKey'] = external_key

    if asset_properties is not None:
        _details['assetProperties'] = cli_util.parse_json_parameter("asset_properties", asset_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if host is not None:
        _details['host'] = host

    if port is not None:
        _details['port'] = port

    if service_name is not None:
        _details['serviceName'] = service_name

    if driver_class is not None:
        _details['driverClass'] = driver_class

    if sid is not None:
        _details['sid'] = sid

    if credential_file_content is not None:
        _details['credentialFileContent'] = credential_file_content

    if default_connection is not None:
        _details['defaultConnection'] = cli_util.parse_json_parameter("default_connection", default_connection)

    _details['modelType'] = 'ORACLE_DATA_ASSET'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_data_asset(
        workspace_id=workspace_id,
        create_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_integration.create_data_asset_create_data_asset_from_adwc.command_name', 'create-data-asset-create-data-asset-from-adwc'), help=u"""Creates a data asset with default connection.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--key', help=u"""Currently not used on data asset creation. Reserved for future.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--service-name', help=u"""The service name for the data asset.""")
@cli_util.option('--driver-class', help=u"""The driver class for the data asset.""")
@cli_util.option('--credential-file-content', help=u"""The credential file content from a wallet for the data asset.""")
@cli_util.option('--default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromAdwc'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromAdwc'}}, output_type={'module': 'data_integration', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset_create_data_asset_from_adwc(ctx, from_json, workspace_id, name, identifier, key, model_version, description, object_status, external_key, asset_properties, registry_metadata, service_name, driver_class, credential_file_content, default_connection):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if external_key is not None:
        _details['externalKey'] = external_key

    if asset_properties is not None:
        _details['assetProperties'] = cli_util.parse_json_parameter("asset_properties", asset_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if service_name is not None:
        _details['serviceName'] = service_name

    if driver_class is not None:
        _details['driverClass'] = driver_class

    if credential_file_content is not None:
        _details['credentialFileContent'] = credential_file_content

    if default_connection is not None:
        _details['defaultConnection'] = cli_util.parse_json_parameter("default_connection", default_connection)

    _details['modelType'] = 'ORACLE_ADWC_DATA_ASSET'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_data_asset(
        workspace_id=workspace_id,
        create_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_integration.create_data_asset_create_data_asset_from_atp.command_name', 'create-data-asset-create-data-asset-from-atp'), help=u"""Creates a data asset with default connection.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--key', help=u"""Currently not used on data asset creation. Reserved for future.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--service-name', help=u"""The service name for the data asset.""")
@cli_util.option('--driver-class', help=u"""The driver class for the data asset.""")
@cli_util.option('--credential-file-content', help=u"""The credential file content from a wallet for the data asset.""")
@cli_util.option('--default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromAtp'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromAtp'}}, output_type={'module': 'data_integration', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset_create_data_asset_from_atp(ctx, from_json, workspace_id, name, identifier, key, model_version, description, object_status, external_key, asset_properties, registry_metadata, service_name, driver_class, credential_file_content, default_connection):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if external_key is not None:
        _details['externalKey'] = external_key

    if asset_properties is not None:
        _details['assetProperties'] = cli_util.parse_json_parameter("asset_properties", asset_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if service_name is not None:
        _details['serviceName'] = service_name

    if driver_class is not None:
        _details['driverClass'] = driver_class

    if credential_file_content is not None:
        _details['credentialFileContent'] = credential_file_content

    if default_connection is not None:
        _details['defaultConnection'] = cli_util.parse_json_parameter("default_connection", default_connection)

    _details['modelType'] = 'ORACLE_ATP_DATA_ASSET'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_data_asset(
        workspace_id=workspace_id,
        create_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_integration.create_data_asset_create_data_asset_from_object_storage.command_name', 'create-data-asset-create-data-asset-from-object-storage'), help=u"""Creates a data asset with default connection.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--key', help=u"""Currently not used on data asset creation. Reserved for future.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--url', help=u"""url""")
@cli_util.option('--tenancy-id', help=u"""The OCI tenancy OCID.""")
@cli_util.option('--namespace', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromObjectStorage'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'CreateConnectionFromObjectStorage'}}, output_type={'module': 'data_integration', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset_create_data_asset_from_object_storage(ctx, from_json, workspace_id, name, identifier, key, model_version, description, object_status, external_key, asset_properties, registry_metadata, url, tenancy_id, namespace, default_connection):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if external_key is not None:
        _details['externalKey'] = external_key

    if asset_properties is not None:
        _details['assetProperties'] = cli_util.parse_json_parameter("asset_properties", asset_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if url is not None:
        _details['url'] = url

    if tenancy_id is not None:
        _details['tenancyId'] = tenancy_id

    if namespace is not None:
        _details['namespace'] = namespace

    if default_connection is not None:
        _details['defaultConnection'] = cli_util.parse_json_parameter("default_connection", default_connection)

    _details['modelType'] = 'ORACLE_OBJECT_STORAGE_DATA_ASSET'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_data_asset(
        workspace_id=workspace_id,
        create_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_flow_group.command(name=cli_util.override('data_integration.create_data_flow.command_name', 'create'), help=u"""Creates a new data flow in a project or folder ready for performing data integrations.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--registry-metadata', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--nodes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of nodes.

This option is a JSON list with items of type FlowNode.  For documentation on FlowNode please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/FlowNode.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--flow-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'nodes': {'module': 'data_integration', 'class': 'list[FlowNode]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'flow-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'nodes': {'module': 'data_integration', 'class': 'list[FlowNode]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'flow-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'DataFlow'})
@cli_util.wrap_exceptions
def create_data_flow(ctx, from_json, workspace_id, name, identifier, registry_metadata, key, model_version, parent_ref, nodes, parameters, description, flow_config_values, object_status):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier
    _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if nodes is not None:
        _details['nodes'] = cli_util.parse_json_parameter("nodes", nodes)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if description is not None:
        _details['description'] = description

    if flow_config_values is not None:
        _details['flowConfigValues'] = cli_util.parse_json_parameter("flow_config_values", flow_config_values)

    if object_status is not None:
        _details['objectStatus'] = object_status

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_data_flow(
        workspace_id=workspace_id,
        create_data_flow_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_flow_validation_group.command(name=cli_util.override('data_integration.create_data_flow_validation.command_name', 'create'), help=u"""The endpoint accepts the DataFlow object definition in the request payload and creates a DataFlow object validation.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.""")
@cli_util.option('--model-type', help=u"""The type of the object.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--nodes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of nodes.

This option is a JSON list with items of type FlowNode.  For documentation on FlowNode please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/FlowNode.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--flow-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key-map', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map, if provided key is replaced with generated key, this structure provides mapping between user provided key and generated key""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'nodes': {'module': 'data_integration', 'class': 'list[FlowNode]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'flow-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'metadata': {'module': 'data_integration', 'class': 'ObjectMetadata'}, 'key-map': {'module': 'data_integration', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'nodes': {'module': 'data_integration', 'class': 'list[FlowNode]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'flow-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'metadata': {'module': 'data_integration', 'class': 'ObjectMetadata'}, 'key-map': {'module': 'data_integration', 'class': 'dict(str, string)'}}, output_type={'module': 'data_integration', 'class': 'DataFlowValidation'})
@cli_util.wrap_exceptions
def create_data_flow_validation(ctx, from_json, workspace_id, key, model_type, model_version, parent_ref, name, identifier, object_version, nodes, parameters, description, flow_config_values, object_status, metadata, key_map):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if key is not None:
        _details['key'] = key

    if model_type is not None:
        _details['modelType'] = model_type

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if identifier is not None:
        _details['identifier'] = identifier

    if object_version is not None:
        _details['objectVersion'] = object_version

    if nodes is not None:
        _details['nodes'] = cli_util.parse_json_parameter("nodes", nodes)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if description is not None:
        _details['description'] = description

    if flow_config_values is not None:
        _details['flowConfigValues'] = cli_util.parse_json_parameter("flow_config_values", flow_config_values)

    if object_status is not None:
        _details['objectStatus'] = object_status

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if key_map is not None:
        _details['keyMap'] = cli_util.parse_json_parameter("key_map", key_map)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_data_flow_validation(
        workspace_id=workspace_id,
        create_data_flow_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_entity_group.command(name=cli_util.override('data_integration.create_entity_shape.command_name', 'create-entity-shape'), help=u"""Retrieves the data entity shape from the end data system. The input can specify the data entity to get the shape for. For databases, this can be retrieved from the database data dictionary. For files, some hints as to the file properties can also be supplied in the input.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key""")
@cli_util.option('--schema-resource-name', required=True, help=u"""Schema resource name used for retrieving schemas""")
@cli_util.option('--model-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["FILE_ENTITY"]), help=u"""The data entity type.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'EntityShape'})
@cli_util.wrap_exceptions
def create_entity_shape(ctx, from_json, workspace_id, connection_key, schema_resource_name, model_type, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelType'] = model_type

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_entity_shape(
        workspace_id=workspace_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        create_entity_shape_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_entity_group.command(name=cli_util.override('data_integration.create_entity_shape_create_entity_shape_from_file.command_name', 'create-entity-shape-create-entity-shape-from-file'), help=u"""Retrieves the data entity shape from the end data system. The input can specify the data entity to get the shape for. For databases, this can be retrieved from the database data dictionary. For files, some hints as to the file properties can also be supplied in the input.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key""")
@cli_util.option('--schema-resource-name', required=True, help=u"""Schema resource name used for retrieving schemas""")
@cli_util.option('--key', help=u"""The key of the object.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--external-key', help=u"""The external key for the object.""")
@cli_util.option('--shape', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--shape-id', help=u"""The shape ID.""")
@cli_util.option('--types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--entity-type', type=custom_types.CliCaseInsensitiveChoice(["TABLE", "VIEW", "FILE", "QUEUE", "STREAM", "OTHER"]), help=u"""The entity type.""")
@cli_util.option('--other-type-label', help=u"""Specifies other type label.""")
@cli_util.option('--unique-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of unique keys.

This option is a JSON list with items of type UniqueKey.  For documentation on UniqueKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/UniqueKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--foreign-keys', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of foreign keys.

This option is a JSON list with items of type ForeignKey.  For documentation on ForeignKey please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ForeignKey.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource-name', help=u"""The resource name.""")
@cli_util.option('--data-format', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'shape': {'module': 'data_integration', 'class': 'Shape'}, 'types': {'module': 'data_integration', 'class': 'TypeLibrary'}, 'unique-keys': {'module': 'data_integration', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_integration', 'class': 'list[ForeignKey]'}, 'data-format': {'module': 'data_integration', 'class': 'DataFormat'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'shape': {'module': 'data_integration', 'class': 'Shape'}, 'types': {'module': 'data_integration', 'class': 'TypeLibrary'}, 'unique-keys': {'module': 'data_integration', 'class': 'list[UniqueKey]'}, 'foreign-keys': {'module': 'data_integration', 'class': 'list[ForeignKey]'}, 'data-format': {'module': 'data_integration', 'class': 'DataFormat'}}, output_type={'module': 'data_integration', 'class': 'EntityShape'})
@cli_util.wrap_exceptions
def create_entity_shape_create_entity_shape_from_file(ctx, from_json, workspace_id, connection_key, schema_resource_name, key, model_version, parent_ref, name, description, object_version, external_key, shape, shape_id, types, entity_type, other_type_label, unique_keys, foreign_keys, resource_name, data_format, object_status, identifier, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_version is not None:
        _details['objectVersion'] = object_version

    if external_key is not None:
        _details['externalKey'] = external_key

    if shape is not None:
        _details['shape'] = cli_util.parse_json_parameter("shape", shape)

    if shape_id is not None:
        _details['shapeId'] = shape_id

    if types is not None:
        _details['types'] = cli_util.parse_json_parameter("types", types)

    if entity_type is not None:
        _details['entityType'] = entity_type

    if other_type_label is not None:
        _details['otherTypeLabel'] = other_type_label

    if unique_keys is not None:
        _details['uniqueKeys'] = cli_util.parse_json_parameter("unique_keys", unique_keys)

    if foreign_keys is not None:
        _details['foreignKeys'] = cli_util.parse_json_parameter("foreign_keys", foreign_keys)

    if resource_name is not None:
        _details['resourceName'] = resource_name

    if data_format is not None:
        _details['dataFormat'] = cli_util.parse_json_parameter("data_format", data_format)

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    _details['modelType'] = 'FILE_ENTITY'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_entity_shape(
        workspace_id=workspace_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        create_entity_shape_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@folder_group.command(name=cli_util.override('data_integration.create_folder.command_name', 'create'), help=u"""Creates a folder in a project or in another folder, limited to two levels of folders. | Folders are used to organize your design-time resources, such as tasks or data flows.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--registry-metadata', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key', help=u"""Currently not used on folder creation. Reserved for future.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--category-name', help=u"""categoryName""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@json_skeleton_utils.get_cli_json_input_option({'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Folder'})
@cli_util.wrap_exceptions
def create_folder(ctx, from_json, workspace_id, name, identifier, registry_metadata, key, model_version, description, category_name, object_status):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier
    _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if description is not None:
        _details['description'] = description

    if category_name is not None:
        _details['categoryName'] = category_name

    if object_status is not None:
        _details['objectStatus'] = object_status

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_folder(
        workspace_id=workspace_id,
        create_folder_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('data_integration.create_patch.command_name', 'create-patch'), help=u"""Creates a patch in an application.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--patch-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["PUBLISH", "UNPUBLISH"]), help=u"""The type of the patch applied or being applied on the application.""")
@cli_util.option('--object-keys', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The array of object keys to publish into application.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key', help=u"""The key of the object.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'object-keys': {'module': 'data_integration', 'class': 'list[string]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'object-keys': {'module': 'data_integration', 'class': 'list[string]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Patch'})
@cli_util.wrap_exceptions
def create_patch(ctx, from_json, workspace_id, application_key, name, identifier, patch_type, object_keys, key, model_version, description, object_status, registry_metadata):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier
    _details['patchType'] = patch_type
    _details['objectKeys'] = cli_util.parse_json_parameter("object_keys", object_keys)

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_patch(
        workspace_id=workspace_id,
        application_key=application_key,
        create_patch_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('data_integration.create_project.command_name', 'create'), help=u"""Creates a project. Projects are organizational constructs within a workspace that you use to organize your design-time resources, such as tasks or data flows. Projects can be organized into folders.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify project.""")
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Project'})
@cli_util.wrap_exceptions
def create_project(ctx, from_json, workspace_id, name, identifier, model_version, description, object_status, key, registry_metadata):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier

    if model_version is not None:
        _details['modelVersion'] = model_version

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if key is not None:
        _details['key'] = key

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_project(
        workspace_id=workspace_id,
        create_project_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_group.command(name=cli_util.override('data_integration.create_task.command_name', 'create'), help=u"""Creates a new task ready for performing data integrations. There are specialized types of tasks that include data loader and integration tasks.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--model-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["INTEGRATION_TASK", "DATA_LOADER_TASK"]), help=u"""The type of the task.""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--registry-metadata', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--input-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of input ports.

This option is a JSON list with items of type InputPort.  For documentation on InputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/InputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of output ports.

This option is a JSON list with items of type OutputPort.  For documentation on OutputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/OutputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--op-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-provider-delegate', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'CreateConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'CreateConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Task'})
@cli_util.wrap_exceptions
def create_task(ctx, from_json, workspace_id, model_type, name, identifier, registry_metadata, key, model_version, parent_ref, description, object_status, input_ports, output_ports, parameters, op_config_values, config_provider_delegate):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelType'] = model_type
    _details['name'] = name
    _details['identifier'] = identifier
    _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if input_ports is not None:
        _details['inputPorts'] = cli_util.parse_json_parameter("input_ports", input_ports)

    if output_ports is not None:
        _details['outputPorts'] = cli_util.parse_json_parameter("output_ports", output_ports)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if op_config_values is not None:
        _details['opConfigValues'] = cli_util.parse_json_parameter("op_config_values", op_config_values)

    if config_provider_delegate is not None:
        _details['configProviderDelegate'] = cli_util.parse_json_parameter("config_provider_delegate", config_provider_delegate)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_task(
        workspace_id=workspace_id,
        create_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_group.command(name=cli_util.override('data_integration.create_task_create_task_from_integration_task.command_name', 'create-task-create-task-from-integration-task'), help=u"""Creates a new task ready for performing data integrations. There are specialized types of tasks that include data loader and integration tasks.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--registry-metadata', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--input-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of input ports.

This option is a JSON list with items of type InputPort.  For documentation on InputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/InputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of output ports.

This option is a JSON list with items of type OutputPort.  For documentation on OutputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/OutputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--op-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-provider-delegate', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-flow', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'CreateConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-flow': {'module': 'data_integration', 'class': 'DataFlow'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'CreateConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-flow': {'module': 'data_integration', 'class': 'DataFlow'}}, output_type={'module': 'data_integration', 'class': 'Task'})
@cli_util.wrap_exceptions
def create_task_create_task_from_integration_task(ctx, from_json, workspace_id, name, identifier, registry_metadata, key, model_version, parent_ref, description, object_status, input_ports, output_ports, parameters, op_config_values, config_provider_delegate, data_flow):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier
    _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if input_ports is not None:
        _details['inputPorts'] = cli_util.parse_json_parameter("input_ports", input_ports)

    if output_ports is not None:
        _details['outputPorts'] = cli_util.parse_json_parameter("output_ports", output_ports)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if op_config_values is not None:
        _details['opConfigValues'] = cli_util.parse_json_parameter("op_config_values", op_config_values)

    if config_provider_delegate is not None:
        _details['configProviderDelegate'] = cli_util.parse_json_parameter("config_provider_delegate", config_provider_delegate)

    if data_flow is not None:
        _details['dataFlow'] = cli_util.parse_json_parameter("data_flow", data_flow)

    _details['modelType'] = 'INTEGRATION_TASK'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_task(
        workspace_id=workspace_id,
        create_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_group.command(name=cli_util.override('data_integration.create_task_create_task_from_data_loader_task.command_name', 'create-task-create-task-from-data-loader-task'), help=u"""Creates a new task ready for performing data integrations. There are specialized types of tasks that include data loader and integration tasks.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', required=True, help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', required=True, help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--registry-metadata', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--input-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of input ports.

This option is a JSON list with items of type InputPort.  For documentation on InputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/InputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of output ports.

This option is a JSON list with items of type OutputPort.  For documentation on OutputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/OutputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--op-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-provider-delegate', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-flow', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'CreateConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-flow': {'module': 'data_integration', 'class': 'DataFlow'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'CreateConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-flow': {'module': 'data_integration', 'class': 'DataFlow'}}, output_type={'module': 'data_integration', 'class': 'Task'})
@cli_util.wrap_exceptions
def create_task_create_task_from_data_loader_task(ctx, from_json, workspace_id, name, identifier, registry_metadata, key, model_version, parent_ref, description, object_status, input_ports, output_ports, parameters, op_config_values, config_provider_delegate, data_flow):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['identifier'] = identifier
    _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if input_ports is not None:
        _details['inputPorts'] = cli_util.parse_json_parameter("input_ports", input_ports)

    if output_ports is not None:
        _details['outputPorts'] = cli_util.parse_json_parameter("output_ports", output_ports)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if op_config_values is not None:
        _details['opConfigValues'] = cli_util.parse_json_parameter("op_config_values", op_config_values)

    if config_provider_delegate is not None:
        _details['configProviderDelegate'] = cli_util.parse_json_parameter("config_provider_delegate", config_provider_delegate)

    if data_flow is not None:
        _details['dataFlow'] = cli_util.parse_json_parameter("data_flow", data_flow)

    _details['modelType'] = 'DATA_LOADER_TASK'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_task(
        workspace_id=workspace_id,
        create_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_run_group.command(name=cli_util.override('data_integration.create_task_run.command_name', 'create'), help=u"""Creates a data integration task or task run. The task can be based on a dataflow design or a task.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--key', help=u"""The key of the object.""")
@cli_util.option('--model-type', help=u"""The type of the object.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--config-provider', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'config-provider': {'module': 'data_integration', 'class': 'CreateConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'config-provider': {'module': 'data_integration', 'class': 'CreateConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'TaskRun'})
@cli_util.wrap_exceptions
def create_task_run(ctx, from_json, workspace_id, application_key, key, model_type, model_version, name, description, config_provider, identifier, registry_metadata):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if key is not None:
        _details['key'] = key

    if model_type is not None:
        _details['modelType'] = model_type

    if model_version is not None:
        _details['modelVersion'] = model_version

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if config_provider is not None:
        _details['configProvider'] = cli_util.parse_json_parameter("config_provider", config_provider)

    if identifier is not None:
        _details['identifier'] = identifier

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_task_run(
        workspace_id=workspace_id,
        application_key=application_key,
        create_task_run_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_validation_group.command(name=cli_util.override('data_integration.create_task_validation.command_name', 'create'), help=u"""Validates a specific task.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--model-type', type=custom_types.CliCaseInsensitiveChoice(["INTEGRATION_TASK", "DATA_LOADER_TASK"]), help=u"""The type of the task.""")
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--input-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of input ports.

This option is a JSON list with items of type InputPort.  For documentation on InputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/InputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of output ports.

This option is a JSON list with items of type OutputPort.  For documentation on OutputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/OutputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--op-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-provider-delegate', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'metadata': {'module': 'data_integration', 'class': 'ObjectMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'metadata': {'module': 'data_integration', 'class': 'ObjectMetadata'}}, output_type={'module': 'data_integration', 'class': 'TaskValidation'})
@cli_util.wrap_exceptions
def create_task_validation(ctx, from_json, workspace_id, model_type, key, model_version, parent_ref, name, description, object_version, object_status, identifier, input_ports, output_ports, parameters, op_config_values, config_provider_delegate, metadata):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if model_type is not None:
        _details['modelType'] = model_type

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_version is not None:
        _details['objectVersion'] = object_version

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if input_ports is not None:
        _details['inputPorts'] = cli_util.parse_json_parameter("input_ports", input_ports)

    if output_ports is not None:
        _details['outputPorts'] = cli_util.parse_json_parameter("output_ports", output_ports)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if op_config_values is not None:
        _details['opConfigValues'] = cli_util.parse_json_parameter("op_config_values", op_config_values)

    if config_provider_delegate is not None:
        _details['configProviderDelegate'] = cli_util.parse_json_parameter("config_provider_delegate", config_provider_delegate)

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_task_validation(
        workspace_id=workspace_id,
        create_task_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_validation_group.command(name=cli_util.override('data_integration.create_task_validation_create_task_validation_from_data_loader_task.command_name', 'create-task-validation-create-task-validation-from-data-loader-task'), help=u"""Validates a specific task.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--input-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of input ports.

This option is a JSON list with items of type InputPort.  For documentation on InputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/InputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of output ports.

This option is a JSON list with items of type OutputPort.  For documentation on OutputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/OutputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--op-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-provider-delegate', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-flow', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'metadata': {'module': 'data_integration', 'class': 'ObjectMetadata'}, 'data-flow': {'module': 'data_integration', 'class': 'DataFlow'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'metadata': {'module': 'data_integration', 'class': 'ObjectMetadata'}, 'data-flow': {'module': 'data_integration', 'class': 'DataFlow'}}, output_type={'module': 'data_integration', 'class': 'TaskValidation'})
@cli_util.wrap_exceptions
def create_task_validation_create_task_validation_from_data_loader_task(ctx, from_json, workspace_id, key, model_version, parent_ref, name, description, object_version, object_status, identifier, input_ports, output_ports, parameters, op_config_values, config_provider_delegate, metadata, data_flow):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_version is not None:
        _details['objectVersion'] = object_version

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if input_ports is not None:
        _details['inputPorts'] = cli_util.parse_json_parameter("input_ports", input_ports)

    if output_ports is not None:
        _details['outputPorts'] = cli_util.parse_json_parameter("output_ports", output_ports)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if op_config_values is not None:
        _details['opConfigValues'] = cli_util.parse_json_parameter("op_config_values", op_config_values)

    if config_provider_delegate is not None:
        _details['configProviderDelegate'] = cli_util.parse_json_parameter("config_provider_delegate", config_provider_delegate)

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if data_flow is not None:
        _details['dataFlow'] = cli_util.parse_json_parameter("data_flow", data_flow)

    _details['modelType'] = 'DATA_LOADER_TASK'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_task_validation(
        workspace_id=workspace_id,
        create_task_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_validation_group.command(name=cli_util.override('data_integration.create_task_validation_create_task_validation_from_integration_task.command_name', 'create-task-validation-create-task-validation-from-integration-task'), help=u"""Validates a specific task.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--key', help=u"""Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--input-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of input ports.

This option is a JSON list with items of type InputPort.  For documentation on InputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/InputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of output ports.

This option is a JSON list with items of type OutputPort.  For documentation on OutputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/OutputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--op-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-provider-delegate', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-flow', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'metadata': {'module': 'data_integration', 'class': 'ObjectMetadata'}, 'data-flow': {'module': 'data_integration', 'class': 'DataFlow'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'metadata': {'module': 'data_integration', 'class': 'ObjectMetadata'}, 'data-flow': {'module': 'data_integration', 'class': 'DataFlow'}}, output_type={'module': 'data_integration', 'class': 'TaskValidation'})
@cli_util.wrap_exceptions
def create_task_validation_create_task_validation_from_integration_task(ctx, from_json, workspace_id, key, model_version, parent_ref, name, description, object_version, object_status, identifier, input_ports, output_ports, parameters, op_config_values, config_provider_delegate, metadata, data_flow):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if key is not None:
        _details['key'] = key

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_version is not None:
        _details['objectVersion'] = object_version

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if input_ports is not None:
        _details['inputPorts'] = cli_util.parse_json_parameter("input_ports", input_ports)

    if output_ports is not None:
        _details['outputPorts'] = cli_util.parse_json_parameter("output_ports", output_ports)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if op_config_values is not None:
        _details['opConfigValues'] = cli_util.parse_json_parameter("op_config_values", op_config_values)

    if config_provider_delegate is not None:
        _details['configProviderDelegate'] = cli_util.parse_json_parameter("config_provider_delegate", config_provider_delegate)

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    if data_flow is not None:
        _details['dataFlow'] = cli_util.parse_json_parameter("data_flow", data_flow)

    _details['modelType'] = 'INTEGRATION_TASK'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_task_validation(
        workspace_id=workspace_id,
        create_task_validation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@workspace_group.command(name=cli_util.override('data_integration.create_workspace.command_name', 'create'), help=u"""Creates a new Data Integration Workspace ready for performing data integration.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name for the workspace. Does not have to be unique, and can be modified. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the workspace.""")
@cli_util.option('--vcn-id', help=u"""The OCID of the VCN the subnet is in.""")
@cli_util.option('--subnet-id', help=u"""The OCID of the subnet for customer connected databases.""")
@cli_util.option('--dns-server-ip', help=u"""The IP of the custom DNS.""")
@cli_util.option('--dns-server-zone', help=u"""The DNS zone of the custom DNS to use to resolve names.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A detailed description for the workspace.""")
@cli_util.option('--is-private-network-enabled', type=click.BOOL, help=u"""Whether the private network connection is enabled or disabled.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_integration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_integration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_workspace(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, compartment_id, vcn_id, subnet_id, dns_server_ip, dns_server_zone, freeform_tags, defined_tags, description, is_private_network_enabled):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['compartmentId'] = compartment_id

    if vcn_id is not None:
        _details['vcnId'] = vcn_id

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if dns_server_ip is not None:
        _details['dnsServerIp'] = dns_server_ip

    if dns_server_zone is not None:
        _details['dnsServerZone'] = dns_server_zone

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if is_private_network_enabled is not None:
        _details['isPrivateNetworkEnabled'] = is_private_network_enabled

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.create_workspace(
        create_workspace_details=_details,
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


@application_group.command(name=cli_util.override('data_integration.delete_application.command_name', 'delete'), help=u"""Removes an application using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_application(ctx, from_json, workspace_id, application_key, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.delete_application(
        workspace_id=workspace_id,
        application_key=application_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_integration.delete_connection.command_name', 'delete'), help=u"""Removes a connection using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_connection(ctx, from_json, workspace_id, connection_key, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.delete_connection(
        workspace_id=workspace_id,
        connection_key=connection_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_validation_group.command(name=cli_util.override('data_integration.delete_connection_validation.command_name', 'delete'), help=u"""Successfully accepted the delete request. The connection validation will be deleted.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-validation-key', required=True, help=u"""key of the connection validation.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_connection_validation(ctx, from_json, workspace_id, connection_validation_key, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_validation_key, six.string_types) and len(connection_validation_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-validation-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.delete_connection_validation(
        workspace_id=workspace_id,
        connection_validation_key=connection_validation_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_integration.delete_data_asset.command_name', 'delete'), help=u"""Removes a data asset using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-asset-key', required=True, help=u"""Data asset key.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_data_asset(ctx, from_json, workspace_id, data_asset_key, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.delete_data_asset(
        workspace_id=workspace_id,
        data_asset_key=data_asset_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_flow_group.command(name=cli_util.override('data_integration.delete_data_flow.command_name', 'delete'), help=u"""Removes a data flow from a project or folder using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-flow-key', required=True, help=u"""DIS DataFlow key""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_data_flow(ctx, from_json, workspace_id, data_flow_key, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(data_flow_key, six.string_types) and len(data_flow_key.strip()) == 0:
        raise click.UsageError('Parameter --data-flow-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.delete_data_flow(
        workspace_id=workspace_id,
        data_flow_key=data_flow_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_flow_validation_group.command(name=cli_util.override('data_integration.delete_data_flow_validation.command_name', 'delete'), help=u"""Removes a data flow validation using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-flow-validation-key', required=True, help=u"""key of the dataflow validation.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_data_flow_validation(ctx, from_json, workspace_id, data_flow_validation_key, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(data_flow_validation_key, six.string_types) and len(data_flow_validation_key.strip()) == 0:
        raise click.UsageError('Parameter --data-flow-validation-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.delete_data_flow_validation(
        workspace_id=workspace_id,
        data_flow_validation_key=data_flow_validation_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@folder_group.command(name=cli_util.override('data_integration.delete_folder.command_name', 'delete'), help=u"""Removes a folder from a project using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--folder-key', required=True, help=u"""DIS Folder key""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_folder(ctx, from_json, workspace_id, folder_key, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(folder_key, six.string_types) and len(folder_key.strip()) == 0:
        raise click.UsageError('Parameter --folder-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.delete_folder(
        workspace_id=workspace_id,
        folder_key=folder_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('data_integration.delete_patch.command_name', 'delete-patch'), help=u"""Removes a patch using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--patch-key', required=True, help=u"""DIS patch key""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_patch(ctx, from_json, workspace_id, application_key, patch_key, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    if isinstance(patch_key, six.string_types) and len(patch_key.strip()) == 0:
        raise click.UsageError('Parameter --patch-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.delete_patch(
        workspace_id=workspace_id,
        application_key=application_key,
        patch_key=patch_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('data_integration.delete_project.command_name', 'delete'), help=u"""Removes a project from the workspace using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--project-key', required=True, help=u"""DIS Project key""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_project(ctx, from_json, workspace_id, project_key, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(project_key, six.string_types) and len(project_key.strip()) == 0:
        raise click.UsageError('Parameter --project-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.delete_project(
        workspace_id=workspace_id,
        project_key=project_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_group.command(name=cli_util.override('data_integration.delete_task.command_name', 'delete'), help=u"""Removes a task using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--task-key', required=True, help=u"""DIS Task key""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_task(ctx, from_json, workspace_id, task_key, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(task_key, six.string_types) and len(task_key.strip()) == 0:
        raise click.UsageError('Parameter --task-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.delete_task(
        workspace_id=workspace_id,
        task_key=task_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_run_group.command(name=cli_util.override('data_integration.delete_task_run.command_name', 'delete'), help=u"""Deletes a task run using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--task-run-key', required=True, help=u"""DIS taskRun key""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_task_run(ctx, from_json, workspace_id, application_key, task_run_key, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    if isinstance(task_run_key, six.string_types) and len(task_run_key.strip()) == 0:
        raise click.UsageError('Parameter --task-run-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.delete_task_run(
        workspace_id=workspace_id,
        application_key=application_key,
        task_run_key=task_run_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_group.command(name=cli_util.override('data_integration.delete_task_validation.command_name', 'delete-task-validation'), help=u"""Removes a task validation using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--task-validation-key', required=True, help=u"""key of the task validation.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_task_validation(ctx, from_json, workspace_id, task_validation_key, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(task_validation_key, six.string_types) and len(task_validation_key.strip()) == 0:
        raise click.UsageError('Parameter --task-validation-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.delete_task_validation(
        workspace_id=workspace_id,
        task_validation_key=task_validation_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@workspace_group.command(name=cli_util.override('data_integration.delete_workspace.command_name', 'delete'), help=u"""Deletes a Data Integration Workspace resource by identifier""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--quiesce-timeout', type=click.INT, help=u"""This parameter allows users to set the timeout for DIS to gracefully close down any running jobs before stopping the workspace.""")
@cli_util.option('--is-force-operation', type=click.BOOL, help=u"""This parameter allows users to force close down the workspace.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_workspace(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, workspace_id, quiesce_timeout, is_force_operation, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if quiesce_timeout is not None:
        kwargs['quiesce_timeout'] = quiesce_timeout
    if is_force_operation is not None:
        kwargs['is_force_operation'] = is_force_operation
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.delete_workspace(
        workspace_id=workspace_id,
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


@application_group.command(name=cli_util.override('data_integration.get_application.command_name', 'get'), help=u"""Retrieves an application using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'Application'})
@cli_util.wrap_exceptions
def get_application(ctx, from_json, workspace_id, application_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_application(
        workspace_id=workspace_id,
        application_key=application_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_integration.get_connection.command_name', 'get'), help=u"""Retrieves the connection details using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def get_connection(ctx, from_json, workspace_id, connection_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_connection(
        workspace_id=workspace_id,
        connection_key=connection_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_validation_group.command(name=cli_util.override('data_integration.get_connection_validation.command_name', 'get'), help=u"""Retrieves a connection validation using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-validation-key', required=True, help=u"""key of the connection validation.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'ConnectionValidation'})
@cli_util.wrap_exceptions
def get_connection_validation(ctx, from_json, workspace_id, connection_validation_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_validation_key, six.string_types) and len(connection_validation_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-validation-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_connection_validation(
        workspace_id=workspace_id,
        connection_validation_key=connection_validation_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('data_integration.get_count_statistic.command_name', 'get-count-statistic'), help=u"""Retrieves statistics on a workspace. It returns an object with an array of property values, such as the number of projects, |        applications, data assets, and so on.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--count-statistic-key', required=True, help=u"""A unique key of the container object, such as workspace, project, and so on, to count statistics for. The statistics is fetched for the given key.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'CountStatistic'})
@cli_util.wrap_exceptions
def get_count_statistic(ctx, from_json, workspace_id, count_statistic_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(count_statistic_key, six.string_types) and len(count_statistic_key.strip()) == 0:
        raise click.UsageError('Parameter --count-statistic-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_count_statistic(
        workspace_id=workspace_id,
        count_statistic_key=count_statistic_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_integration.get_data_asset.command_name', 'get'), help=u"""Retrieves details of a data asset using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-asset-key', required=True, help=u"""Data asset key.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def get_data_asset(ctx, from_json, workspace_id, data_asset_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_data_asset(
        workspace_id=workspace_id,
        data_asset_key=data_asset_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_entity_group.command(name=cli_util.override('data_integration.get_data_entity.command_name', 'get'), help=u"""Retrieves the data entity details with the given name from live schema.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key""")
@cli_util.option('--schema-resource-name', required=True, help=u"""Schema resource name used for retrieving schemas""")
@cli_util.option('--data-entity-key', required=True, help=u"""Name of the data entity""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'DataEntity'})
@cli_util.wrap_exceptions
def get_data_entity(ctx, from_json, workspace_id, connection_key, schema_resource_name, data_entity_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    if isinstance(data_entity_key, six.string_types) and len(data_entity_key.strip()) == 0:
        raise click.UsageError('Parameter --data-entity-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_data_entity(
        workspace_id=workspace_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        data_entity_key=data_entity_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_flow_group.command(name=cli_util.override('data_integration.get_data_flow.command_name', 'get'), help=u"""Retrieves a data flow using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-flow-key', required=True, help=u"""DIS DataFlow key""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'DataFlow'})
@cli_util.wrap_exceptions
def get_data_flow(ctx, from_json, workspace_id, data_flow_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(data_flow_key, six.string_types) and len(data_flow_key.strip()) == 0:
        raise click.UsageError('Parameter --data-flow-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_data_flow(
        workspace_id=workspace_id,
        data_flow_key=data_flow_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_flow_validation_group.command(name=cli_util.override('data_integration.get_data_flow_validation.command_name', 'get'), help=u"""Retrieves a data flow validation using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-flow-validation-key', required=True, help=u"""key of the dataflow validation.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'DataFlowValidation'})
@cli_util.wrap_exceptions
def get_data_flow_validation(ctx, from_json, workspace_id, data_flow_validation_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(data_flow_validation_key, six.string_types) and len(data_flow_validation_key.strip()) == 0:
        raise click.UsageError('Parameter --data-flow-validation-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_data_flow_validation(
        workspace_id=workspace_id,
        data_flow_validation_key=data_flow_validation_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('data_integration.get_dependent_object.command_name', 'get-dependent-object'), help=u"""Retrieves the details of a dependent object from an application.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--dependent-object-key', required=True, help=u"""DIS dependent object key""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'DependentObject'})
@cli_util.wrap_exceptions
def get_dependent_object(ctx, from_json, workspace_id, application_key, dependent_object_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    if isinstance(dependent_object_key, six.string_types) and len(dependent_object_key.strip()) == 0:
        raise click.UsageError('Parameter --dependent-object-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_dependent_object(
        workspace_id=workspace_id,
        application_key=application_key,
        dependent_object_key=dependent_object_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@folder_group.command(name=cli_util.override('data_integration.get_folder.command_name', 'get'), help=u"""Retrieves a folder using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--folder-key', required=True, help=u"""DIS Folder key""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'Folder'})
@cli_util.wrap_exceptions
def get_folder(ctx, from_json, workspace_id, folder_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(folder_key, six.string_types) and len(folder_key.strip()) == 0:
        raise click.UsageError('Parameter --folder-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_folder(
        workspace_id=workspace_id,
        folder_key=folder_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('data_integration.get_patch.command_name', 'get-patch'), help=u"""Retrieves a patch in an application using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--patch-key', required=True, help=u"""DIS patch key""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'Patch'})
@cli_util.wrap_exceptions
def get_patch(ctx, from_json, workspace_id, application_key, patch_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    if isinstance(patch_key, six.string_types) and len(patch_key.strip()) == 0:
        raise click.UsageError('Parameter --patch-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_patch(
        workspace_id=workspace_id,
        application_key=application_key,
        patch_key=patch_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('data_integration.get_project.command_name', 'get'), help=u"""Retrieves a project using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--project-key', required=True, help=u"""DIS Project key""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'Project'})
@cli_util.wrap_exceptions
def get_project(ctx, from_json, workspace_id, project_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(project_key, six.string_types) and len(project_key.strip()) == 0:
        raise click.UsageError('Parameter --project-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_project(
        workspace_id=workspace_id,
        project_key=project_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('data_integration.get_published_object.command_name', 'get-published-object'), help=u"""Retrieves the details of a published object from an application.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--published-object-key', required=True, help=u"""DIS published object key""")
@cli_util.option('--expand-references', help=u"""This is used to expand references of the object. If value is true, then all referenced objects will be expanded. If value is false, then shallow objects will be returned in place of references. Default is false. <br><br><B>Examples:-</B><br> <ul> <li><B>?expandReferences=true</B> returns all objects of type data loader task</li> </ul>""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'PublishedObject'})
@cli_util.wrap_exceptions
def get_published_object(ctx, from_json, workspace_id, application_key, published_object_key, expand_references):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    if isinstance(published_object_key, six.string_types) and len(published_object_key.strip()) == 0:
        raise click.UsageError('Parameter --published-object-key cannot be whitespace or empty string')

    kwargs = {}
    if expand_references is not None:
        kwargs['expand_references'] = expand_references
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_published_object(
        workspace_id=workspace_id,
        application_key=application_key,
        published_object_key=published_object_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@schema_group.command(name=cli_util.override('data_integration.get_schema.command_name', 'get'), help=u"""Retrieves a schema that can be accessed using the specified connection.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key""")
@cli_util.option('--schema-resource-name', required=True, help=u"""Schema resource name used for retrieving schemas""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'Schema'})
@cli_util.wrap_exceptions
def get_schema(ctx, from_json, workspace_id, connection_key, schema_resource_name):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_schema(
        workspace_id=workspace_id,
        connection_key=connection_key,
        schema_resource_name=schema_resource_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_group.command(name=cli_util.override('data_integration.get_task.command_name', 'get'), help=u"""Retrieves a task using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--task-key', required=True, help=u"""DIS Task key""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'Task'})
@cli_util.wrap_exceptions
def get_task(ctx, from_json, workspace_id, task_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(task_key, six.string_types) and len(task_key.strip()) == 0:
        raise click.UsageError('Parameter --task-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_task(
        workspace_id=workspace_id,
        task_key=task_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_run_group.command(name=cli_util.override('data_integration.get_task_run.command_name', 'get'), help=u"""Retrieves a task run using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--task-run-key', required=True, help=u"""DIS taskRun key""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'TaskRun'})
@cli_util.wrap_exceptions
def get_task_run(ctx, from_json, workspace_id, application_key, task_run_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    if isinstance(task_run_key, six.string_types) and len(task_run_key.strip()) == 0:
        raise click.UsageError('Parameter --task-run-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_task_run(
        workspace_id=workspace_id,
        application_key=application_key,
        task_run_key=task_run_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_group.command(name=cli_util.override('data_integration.get_task_validation.command_name', 'get-task-validation'), help=u"""Retrieves a task validation using the specified identifier.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--task-validation-key', required=True, help=u"""key of the task validation.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'TaskValidation'})
@cli_util.wrap_exceptions
def get_task_validation(ctx, from_json, workspace_id, task_validation_key):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(task_validation_key, six.string_types) and len(task_validation_key.strip()) == 0:
        raise click.UsageError('Parameter --task-validation-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_task_validation(
        workspace_id=workspace_id,
        task_validation_key=task_validation_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_integration.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@workspace_group.command(name=cli_util.override('data_integration.get_workspace.command_name', 'get'), help=u"""Gets a Data Integration Workspace by identifier""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'Workspace'})
@cli_util.wrap_exceptions
def get_workspace(ctx, from_json, workspace_id):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.get_workspace(
        workspace_id=workspace_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('data_integration.list_applications.command_name', 'list'), help=u"""Retrieves a list of applications and provides options to filter the list.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--identifier', multiple=True, help=u"""This filter parameter can be used to filter by the identifier of the published object.""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'identifier': {'module': 'data_integration', 'class': 'list[string]'}, 'fields': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'identifier': {'module': 'data_integration', 'class': 'list[string]'}, 'fields': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'ApplicationSummaryCollection'})
@cli_util.wrap_exceptions
def list_applications(ctx, from_json, all_pages, page_size, workspace_id, name, identifier, fields, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if identifier is not None and len(identifier) > 0:
        kwargs['identifier'] = identifier
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_applications,
            workspace_id=workspace_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_applications,
            limit,
            page_size,
            workspace_id=workspace_id,
            **kwargs
        )
    else:
        result = client.list_applications(
            workspace_id=workspace_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@connection_validation_group.command(name=cli_util.override('data_integration.list_connection_validations.command_name', 'list'), help=u"""Retrieves a list of connection validations within the specified workspace.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--key', help=u"""This filter parameter can be used to filter by the key of the object.""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--identifier', help=u"""This filter parameter can be used to filter by the identifier of the object.""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'ConnectionValidationSummaryCollection'})
@cli_util.wrap_exceptions
def list_connection_validations(ctx, from_json, all_pages, page_size, workspace_id, key, name, identifier, fields, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if name is not None:
        kwargs['name'] = name
    if identifier is not None:
        kwargs['identifier'] = identifier
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_connection_validations,
            workspace_id=workspace_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_connection_validations,
            limit,
            page_size,
            workspace_id=workspace_id,
            **kwargs
        )
    else:
        result = client.list_connection_validations(
            workspace_id=workspace_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_integration.list_connections.command_name', 'list'), help=u"""Retrieves a list of all connections.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-asset-key', required=True, help=u"""This filter parameter can be used to filter by the data asset key of the object.""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--type', help=u"""Type of the object to filter the results with.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'ConnectionSummaryCollection'})
@cli_util.wrap_exceptions
def list_connections(ctx, from_json, all_pages, page_size, workspace_id, data_asset_key, name, page, limit, fields, type, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if type is not None:
        kwargs['type'] = type
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_connections,
            workspace_id=workspace_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_connections,
            limit,
            page_size,
            workspace_id=workspace_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    else:
        result = client.list_connections(
            workspace_id=workspace_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_integration.list_data_assets.command_name', 'list'), help=u"""This endpoint can be used to list all data asset summaries""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--type', help=u"""Type of the object to filter the results with.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'DataAssetSummaryCollection'})
@cli_util.wrap_exceptions
def list_data_assets(ctx, from_json, all_pages, page_size, workspace_id, page, limit, fields, type, sort_by, sort_order, name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if type is not None:
        kwargs['type'] = type
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if name is not None:
        kwargs['name'] = name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_assets,
            workspace_id=workspace_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_assets,
            limit,
            page_size,
            workspace_id=workspace_id,
            **kwargs
        )
    else:
        result = client.list_data_assets(
            workspace_id=workspace_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_entity_group.command(name=cli_util.override('data_integration.list_data_entities.command_name', 'list'), help=u"""Retrieves a list of summaries of data entities present in the schema identified by schema name. | A live query is run on the data asset identified via the connection specified.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key""")
@cli_util.option('--schema-resource-name', required=True, help=u"""Schema resource name used for retrieving schemas""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--type', help=u"""Type of the object to filter the results with.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'DataEntitySummaryCollection'})
@cli_util.wrap_exceptions
def list_data_entities(ctx, from_json, all_pages, page_size, workspace_id, connection_key, schema_resource_name, name, page, type, limit, fields, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    if isinstance(schema_resource_name, six.string_types) and len(schema_resource_name.strip()) == 0:
        raise click.UsageError('Parameter --schema-resource-name cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if page is not None:
        kwargs['page'] = page
    if type is not None:
        kwargs['type'] = type
    if limit is not None:
        kwargs['limit'] = limit
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_entities,
            workspace_id=workspace_id,
            connection_key=connection_key,
            schema_resource_name=schema_resource_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_entities,
            limit,
            page_size,
            workspace_id=workspace_id,
            connection_key=connection_key,
            schema_resource_name=schema_resource_name,
            **kwargs
        )
    else:
        result = client.list_data_entities(
            workspace_id=workspace_id,
            connection_key=connection_key,
            schema_resource_name=schema_resource_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_flow_validation_group.command(name=cli_util.override('data_integration.list_data_flow_validations.command_name', 'list'), help=u"""Retrieves a list of data flow validations within the specified workspace""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--key', help=u"""This filter parameter can be used to filter by the key of the object.""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--identifier', help=u"""This filter parameter can be used to filter by the identifier of the object.""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'DataFlowValidationSummaryCollection'})
@cli_util.wrap_exceptions
def list_data_flow_validations(ctx, from_json, all_pages, page_size, workspace_id, key, name, identifier, fields, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if name is not None:
        kwargs['name'] = name
    if identifier is not None:
        kwargs['identifier'] = identifier
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_flow_validations,
            workspace_id=workspace_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_flow_validations,
            limit,
            page_size,
            workspace_id=workspace_id,
            **kwargs
        )
    else:
        result = client.list_data_flow_validations(
            workspace_id=workspace_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_flow_group.command(name=cli_util.override('data_integration.list_data_flows.command_name', 'list'), help=u"""Retrieves a list of data flows in a project or folder.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--folder-id', help=u"""Unique key of the folder""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--identifier', multiple=True, help=u"""This filter parameter can be used to filter by the identifier of the object.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'DataFlowSummaryCollection'})
@cli_util.wrap_exceptions
def list_data_flows(ctx, from_json, all_pages, page_size, workspace_id, folder_id, fields, name, identifier, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if folder_id is not None:
        kwargs['folder_id'] = folder_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if name is not None:
        kwargs['name'] = name
    if identifier is not None and len(identifier) > 0:
        kwargs['identifier'] = identifier
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_flows,
            workspace_id=workspace_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_flows,
            limit,
            page_size,
            workspace_id=workspace_id,
            **kwargs
        )
    else:
        result = client.list_data_flows(
            workspace_id=workspace_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('data_integration.list_dependent_objects.command_name', 'list-dependent-objects'), help=u"""Retrieves a list of all dependent objects for a specific application.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--identifier', multiple=True, help=u"""This filter parameter can be used to filter by the identifier of the published object.""")
@cli_util.option('--type', multiple=True, help=u"""This filter parameter can be used to filter by the object type of the object. This parameter can be suffixed with an optional filter operator InSubtree. For DIS APIs we will filter based on type Task.""")
@cli_util.option('--type-in-subtree', help=u"""This is used in association with type parameter. If value is true, then type all sub types of the given type parameter is considered. If value is false, then sub types are not considered. Default is false.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}, 'type': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}, 'type': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'DependentObjectSummaryCollection'})
@cli_util.wrap_exceptions
def list_dependent_objects(ctx, from_json, all_pages, page_size, workspace_id, application_key, fields, name, identifier, type, type_in_subtree, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if name is not None:
        kwargs['name'] = name
    if identifier is not None and len(identifier) > 0:
        kwargs['identifier'] = identifier
    if type is not None and len(type) > 0:
        kwargs['type'] = type
    if type_in_subtree is not None:
        kwargs['type_in_subtree'] = type_in_subtree
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dependent_objects,
            workspace_id=workspace_id,
            application_key=application_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dependent_objects,
            limit,
            page_size,
            workspace_id=workspace_id,
            application_key=application_key,
            **kwargs
        )
    else:
        result = client.list_dependent_objects(
            workspace_id=workspace_id,
            application_key=application_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@folder_group.command(name=cli_util.override('data_integration.list_folders.command_name', 'list'), help=u"""Retrieves a list of folders in a project and provides options to filter the list.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--aggregator-key', help=u"""This filter parameter can be used to filter by the project or the folder object.""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--identifier', multiple=True, help=u"""This filter parameter can be used to filter by the identifier of the object.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'FolderSummaryCollection'})
@cli_util.wrap_exceptions
def list_folders(ctx, from_json, all_pages, page_size, workspace_id, aggregator_key, fields, name, identifier, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if aggregator_key is not None:
        kwargs['aggregator_key'] = aggregator_key
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if name is not None:
        kwargs['name'] = name
    if identifier is not None and len(identifier) > 0:
        kwargs['identifier'] = identifier
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_folders,
            workspace_id=workspace_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_folders,
            limit,
            page_size,
            workspace_id=workspace_id,
            **kwargs
        )
    else:
        result = client.list_folders(
            workspace_id=workspace_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('data_integration.list_patches.command_name', 'list-patches'), help=u"""Retrieves a list of patches in an application and provides options to filter the list.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--identifier', multiple=True, help=u"""This filter parameter can be used to filter by the identifier of the published object.""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'identifier': {'module': 'data_integration', 'class': 'list[string]'}, 'fields': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'identifier': {'module': 'data_integration', 'class': 'list[string]'}, 'fields': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'PatchSummaryCollection'})
@cli_util.wrap_exceptions
def list_patches(ctx, from_json, all_pages, page_size, workspace_id, application_key, name, identifier, fields, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if identifier is not None and len(identifier) > 0:
        kwargs['identifier'] = identifier
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_patches,
            workspace_id=workspace_id,
            application_key=application_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_patches,
            limit,
            page_size,
            workspace_id=workspace_id,
            application_key=application_key,
            **kwargs
        )
    else:
        result = client.list_patches(
            workspace_id=workspace_id,
            application_key=application_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('data_integration.list_projects.command_name', 'list'), help=u"""Retrieves a lists of projects in a workspace and provides options to filter the list.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--identifier', multiple=True, help=u"""This filter parameter can be used to filter by the identifier of the object.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'ProjectSummaryCollection'})
@cli_util.wrap_exceptions
def list_projects(ctx, from_json, all_pages, page_size, workspace_id, fields, name, identifier, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if name is not None:
        kwargs['name'] = name
    if identifier is not None and len(identifier) > 0:
        kwargs['identifier'] = identifier
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_projects,
            workspace_id=workspace_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_projects,
            limit,
            page_size,
            workspace_id=workspace_id,
            **kwargs
        )
    else:
        result = client.list_projects(
            workspace_id=workspace_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@application_group.command(name=cli_util.override('data_integration.list_published_objects.command_name', 'list-published-objects'), help=u"""Retrieves a list of all the published objects for a specified application.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--identifier', multiple=True, help=u"""This filter parameter can be used to filter by the identifier of the published object.""")
@cli_util.option('--type', multiple=True, help=u"""This filter parameter can be used to filter by the object type of the object. This parameter can be suffixed with an optional filter operator InSubtree. For DIS APIs we will filter based on type Task.""")
@cli_util.option('--type-in-subtree', help=u"""This is used in association with type parameter. If value is true, then type all sub types of the given type parameter is considered. If value is false, then sub types are not considered. Default is false.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}, 'type': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}, 'type': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'PublishedObjectSummaryCollection'})
@cli_util.wrap_exceptions
def list_published_objects(ctx, from_json, all_pages, page_size, workspace_id, application_key, fields, name, identifier, type, type_in_subtree, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if name is not None:
        kwargs['name'] = name
    if identifier is not None and len(identifier) > 0:
        kwargs['identifier'] = identifier
    if type is not None and len(type) > 0:
        kwargs['type'] = type
    if type_in_subtree is not None:
        kwargs['type_in_subtree'] = type_in_subtree
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_published_objects,
            workspace_id=workspace_id,
            application_key=application_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_published_objects,
            limit,
            page_size,
            workspace_id=workspace_id,
            application_key=application_key,
            **kwargs
        )
    else:
        result = client.list_published_objects(
            workspace_id=workspace_id,
            application_key=application_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@schema_group.command(name=cli_util.override('data_integration.list_schemas.command_name', 'list'), help=u"""Retrieves a list of all the schemas that can be accessed using the specified connection.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key""")
@cli_util.option('--schema-resource-name', required=True, help=u"""Schema resource name used for retrieving schemas""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'SchemaSummaryCollection'})
@cli_util.wrap_exceptions
def list_schemas(ctx, from_json, all_pages, page_size, workspace_id, connection_key, schema_resource_name, page, limit, fields, sort_by, sort_order, name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if name is not None:
        kwargs['name'] = name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_schemas,
            workspace_id=workspace_id,
            connection_key=connection_key,
            schema_resource_name=schema_resource_name,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_schemas,
            limit,
            page_size,
            workspace_id=workspace_id,
            connection_key=connection_key,
            schema_resource_name=schema_resource_name,
            **kwargs
        )
    else:
        result = client.list_schemas(
            workspace_id=workspace_id,
            connection_key=connection_key,
            schema_resource_name=schema_resource_name,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@task_run_log_group.command(name=cli_util.override('data_integration.list_task_run_logs.command_name', 'list'), help=u"""Get log entries for task runs using its key""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--task-run-key', required=True, help=u"""DIS taskRun key""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'list[TaskRunLogSummary]'})
@cli_util.wrap_exceptions
def list_task_run_logs(ctx, from_json, all_pages, page_size, workspace_id, application_key, task_run_key, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    if isinstance(task_run_key, six.string_types) and len(task_run_key.strip()) == 0:
        raise click.UsageError('Parameter --task-run-key cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_task_run_logs,
            workspace_id=workspace_id,
            application_key=application_key,
            task_run_key=task_run_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_task_run_logs,
            limit,
            page_size,
            workspace_id=workspace_id,
            application_key=application_key,
            task_run_key=task_run_key,
            **kwargs
        )
    else:
        result = client.list_task_run_logs(
            workspace_id=workspace_id,
            application_key=application_key,
            task_run_key=task_run_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@task_run_group.command(name=cli_util.override('data_integration.list_task_runs.command_name', 'list'), help=u"""Retrieves a list of task runs and provides options to filter the list.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--identifier', multiple=True, help=u"""This filter parameter can be used to filter by the identifier of the object.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'TaskRunSummaryCollection'})
@cli_util.wrap_exceptions
def list_task_runs(ctx, from_json, all_pages, page_size, workspace_id, application_key, fields, name, identifier, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if name is not None:
        kwargs['name'] = name
    if identifier is not None and len(identifier) > 0:
        kwargs['identifier'] = identifier
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_task_runs,
            workspace_id=workspace_id,
            application_key=application_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_task_runs,
            limit,
            page_size,
            workspace_id=workspace_id,
            application_key=application_key,
            **kwargs
        )
    else:
        result = client.list_task_runs(
            workspace_id=workspace_id,
            application_key=application_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@task_group.command(name=cli_util.override('data_integration.list_task_validations.command_name', 'list-task-validations'), help=u"""Retrieves a list of task validations within the specified workspace.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--key', help=u"""This filter parameter can be used to filter by the key of the object.""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--identifier', help=u"""This filter parameter can be used to filter by the identifier of the object.""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'TaskValidationSummaryCollection'})
@cli_util.wrap_exceptions
def list_task_validations(ctx, from_json, all_pages, page_size, workspace_id, key, name, identifier, fields, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if key is not None:
        kwargs['key'] = key
    if name is not None:
        kwargs['name'] = name
    if identifier is not None:
        kwargs['identifier'] = identifier
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_task_validations,
            workspace_id=workspace_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_task_validations,
            limit,
            page_size,
            workspace_id=workspace_id,
            **kwargs
        )
    else:
        result = client.list_task_validations(
            workspace_id=workspace_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@task_group.command(name=cli_util.override('data_integration.list_tasks.command_name', 'list'), help=u"""Retrieves a list of all tasks in a specified project or folder.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--folder-id', help=u"""Unique key of the folder""")
@cli_util.option('--fields', multiple=True, help=u"""This parameter allows users to specify which fields to get for an object.""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--key', multiple=True, help=u"""This filter parameter can be used to filter by the key of the object.""")
@cli_util.option('--identifier', multiple=True, help=u"""This filter parameter can be used to filter by the identifier of the object.""")
@cli_util.option('--type', multiple=True, help=u"""This filter parameter can be used to filter by the object type of the object. This parameter can be suffixed with an optional filter operator InSubtree. If this operator is not specified, then exact match is considered. <br><br><B>Examples:-</B><br> <ul> <li><B>?type=DATA_LOADER_TASK&typeInSubtree=false</B> returns all objects of type data loader task</li> <li><B>?type=DATA_LOADER_TASK</B> returns all objects of type data loader task</li> <li><B>?type=DATA_LOADER_TASK&typeInSubtree=true</B> returns all objects of type data loader task</li> </ul>""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'key': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}, 'type': {'module': 'data_integration', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'fields': {'module': 'data_integration', 'class': 'list[string]'}, 'key': {'module': 'data_integration', 'class': 'list[string]'}, 'identifier': {'module': 'data_integration', 'class': 'list[string]'}, 'type': {'module': 'data_integration', 'class': 'list[string]'}}, output_type={'module': 'data_integration', 'class': 'TaskSummaryCollection'})
@cli_util.wrap_exceptions
def list_tasks(ctx, from_json, all_pages, page_size, workspace_id, folder_id, fields, name, key, identifier, type, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if folder_id is not None:
        kwargs['folder_id'] = folder_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if name is not None:
        kwargs['name'] = name
    if key is not None and len(key) > 0:
        kwargs['key'] = key
    if identifier is not None and len(identifier) > 0:
        kwargs['identifier'] = identifier
    if type is not None and len(type) > 0:
        kwargs['type'] = type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_tasks,
            workspace_id=workspace_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_tasks,
            limit,
            page_size,
            workspace_id=workspace_id,
            **kwargs
        )
    else:
        result = client.list_tasks(
            workspace_id=workspace_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_integration.list_work_request_errors.command_name', 'list-work-request-errors'), help=u"""Return a (paginated) list of errors for a given work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
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


@work_request_group.command(name=cli_util.override('data_integration.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
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


@work_request_group.command(name=cli_util.override('data_integration.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""Work Request status.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_status, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if work_request_status is not None:
        kwargs['work_request_status'] = work_request_status
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
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


@workspace_group.command(name=cli_util.override('data_integration.list_workspaces.command_name', 'list'), help=u"""Returns a list of Data Integration Workspaces.""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--name', help=u"""This filter parameter can be used to filter by the name of the object.""")
@cli_util.option('--limit', type=click.INT, help=u"""This parameter allows users to set the maximum number of items to return per page.  The value must be between 1 and 100 (inclusive).  Default value is 100.""")
@cli_util.option('--page', help=u"""This parameter will control pagination.  Values for the parameter should come from the `opc-next-page` or `opc-prev-page` header in previous response.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "STOPPING", "STOPPED", "FAILED"]), help=u"""Lifecycle state of the resource.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""This parameter is used to control the sort order.  Supported values are `ASC` (ascending) and `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIME_CREATED", "DISPLAY_NAME"]), help=u"""This parameter allows users to specify a sort field.  Supported sort fields are `name`, `identifier`, `timeCreated`, and `timeUpdated`.  Default sort order is the descending order of `timeCreated` (most recently created objects at the top).  Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is by relevance score in descending order).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_integration', 'class': 'list[WorkspaceSummary]'})
@cli_util.wrap_exceptions
def list_workspaces(ctx, from_json, all_pages, page_size, compartment_id, name, limit, page, lifecycle_state, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_workspaces,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_workspaces,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_workspaces(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@workspace_group.command(name=cli_util.override('data_integration.start_workspace.command_name', 'start'), help=u"""The workspace will be started.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def start_workspace(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, workspace_id, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.start_workspace(
        workspace_id=workspace_id,
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


@workspace_group.command(name=cli_util.override('data_integration.stop_workspace.command_name', 'stop'), help=u"""The workspace will be stopped.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--quiesce-timeout', type=click.INT, help=u"""This parameter allows users to set the timeout for DIS to gracefully close down any running jobs before stopping the workspace.""")
@cli_util.option('--is-force-operation', type=click.BOOL, help=u"""This parameter allows users to force close down the workspace.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def stop_workspace(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, workspace_id, quiesce_timeout, is_force_operation, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    kwargs = {}
    if quiesce_timeout is not None:
        kwargs['quiesce_timeout'] = quiesce_timeout
    if is_force_operation is not None:
        kwargs['is_force_operation'] = is_force_operation
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.stop_workspace(
        workspace_id=workspace_id,
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


@application_group.command(name=cli_util.override('data_integration.update_application.command_name', 'update'), help=u"""Updates an application.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify application.""")
@cli_util.option('--model-type', required=True, help=u"""The type of the object.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--application-version', type=click.INT, help=u"""version""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'metadata': {'module': 'data_integration', 'class': 'ObjectMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'metadata': {'module': 'data_integration', 'class': 'ObjectMetadata'}}, output_type={'module': 'data_integration', 'class': 'Application'})
@cli_util.wrap_exceptions
def update_application(ctx, from_json, force, workspace_id, application_key, key, model_type, object_version, model_version, name, description, application_version, object_status, identifier, parent_ref, metadata, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')
    if not force:
        if parent_ref or metadata:
            if not click.confirm("WARNING: Updates to parent-ref and metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['modelType'] = model_type
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if application_version is not None:
        _details['applicationVersion'] = application_version

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if metadata is not None:
        _details['metadata'] = cli_util.parse_json_parameter("metadata", metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_application(
        workspace_id=workspace_id,
        application_key=application_key,
        update_application_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_integration.update_connection.command_name', 'update'), help=u"""Updates a connection under a data asset.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key""")
@cli_util.option('--model-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ORACLE_ADWC_CONNECTION", "ORACLE_ATP_CONNECTION", "ORACLE_OBJECT_STORAGE_CONNECTION", "ORACLEDB_CONNECTION"]), help=u"""The type of the connection.""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection(ctx, from_json, force, workspace_id, connection_key, model_type, key, object_version, model_version, parent_ref, name, description, object_status, identifier, connection_properties, registry_metadata, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')
    if not force:
        if parent_ref or connection_properties or registry_metadata:
            if not click.confirm("WARNING: Updates to parent-ref and connection-properties and registry-metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelType'] = model_type
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if connection_properties is not None:
        _details['connectionProperties'] = cli_util.parse_json_parameter("connection_properties", connection_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_connection(
        workspace_id=workspace_id,
        connection_key=connection_key,
        update_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_integration.update_connection_update_connection_from_object_storage.command_name', 'update-connection-update-connection-from-object-storage'), help=u"""Updates a connection under a data asset.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--credential-file-content', help=u"""The credential file content from a wallet for the data asset.""")
@cli_util.option('--user-id', help=u"""The OCI user OCID for the user to connect to.""")
@cli_util.option('--finger-print', help=u"""The fingeprint for the user.""")
@cli_util.option('--pass-phrase', help=u"""The pass phrase for the connection.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection_update_connection_from_object_storage(ctx, from_json, force, workspace_id, connection_key, key, object_version, model_version, parent_ref, name, description, object_status, identifier, connection_properties, registry_metadata, credential_file_content, user_id, finger_print, pass_phrase, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')
    if not force:
        if parent_ref or connection_properties or registry_metadata:
            if not click.confirm("WARNING: Updates to parent-ref and connection-properties and registry-metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if connection_properties is not None:
        _details['connectionProperties'] = cli_util.parse_json_parameter("connection_properties", connection_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if credential_file_content is not None:
        _details['credentialFileContent'] = credential_file_content

    if user_id is not None:
        _details['userId'] = user_id

    if finger_print is not None:
        _details['fingerPrint'] = finger_print

    if pass_phrase is not None:
        _details['passPhrase'] = pass_phrase

    _details['modelType'] = 'ORACLE_OBJECT_STORAGE_CONNECTION'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_connection(
        workspace_id=workspace_id,
        connection_key=connection_key,
        update_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_integration.update_connection_update_connection_from_atp.command_name', 'update-connection-update-connection-from-atp'), help=u"""Updates a connection under a data asset.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--username', help=u"""The user name for the connection.""")
@cli_util.option('--password', help=u"""The password for the connection.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection_update_connection_from_atp(ctx, from_json, force, workspace_id, connection_key, key, object_version, model_version, parent_ref, name, description, object_status, identifier, connection_properties, registry_metadata, username, password, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')
    if not force:
        if parent_ref or connection_properties or registry_metadata:
            if not click.confirm("WARNING: Updates to parent-ref and connection-properties and registry-metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if connection_properties is not None:
        _details['connectionProperties'] = cli_util.parse_json_parameter("connection_properties", connection_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if username is not None:
        _details['username'] = username

    if password is not None:
        _details['password'] = password

    _details['modelType'] = 'ORACLE_ATP_CONNECTION'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_connection(
        workspace_id=workspace_id,
        connection_key=connection_key,
        update_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_integration.update_connection_update_connection_from_oracle.command_name', 'update-connection-update-connection-from-oracle'), help=u"""Updates a connection under a data asset.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--username', help=u"""The user name for the connection.""")
@cli_util.option('--password', help=u"""The password for the connection.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection_update_connection_from_oracle(ctx, from_json, force, workspace_id, connection_key, key, object_version, model_version, parent_ref, name, description, object_status, identifier, connection_properties, registry_metadata, username, password, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')
    if not force:
        if parent_ref or connection_properties or registry_metadata:
            if not click.confirm("WARNING: Updates to parent-ref and connection-properties and registry-metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if connection_properties is not None:
        _details['connectionProperties'] = cli_util.parse_json_parameter("connection_properties", connection_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if username is not None:
        _details['username'] = username

    if password is not None:
        _details['password'] = password

    _details['modelType'] = 'ORACLEDB_CONNECTION'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_connection(
        workspace_id=workspace_id,
        connection_key=connection_key,
        update_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_integration.update_connection_update_connection_from_adwc.command_name', 'update-connection-update-connection-from-adwc'), help=u"""Updates a connection under a data asset.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--connection-key', required=True, help=u"""The connection key""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can be passed in create.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--connection-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The properties for the connection.

This option is a JSON list with items of type ConnectionProperty.  For documentation on ConnectionProperty please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/ConnectionProperty.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--username', help=u"""The user name for the connection.""")
@cli_util.option('--password', help=u"""The password for the connection.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'connection-properties': {'module': 'data_integration', 'class': 'list[ConnectionProperty]'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection_update_connection_from_adwc(ctx, from_json, force, workspace_id, connection_key, key, object_version, model_version, parent_ref, name, description, object_status, identifier, connection_properties, registry_metadata, username, password, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')
    if not force:
        if parent_ref or connection_properties or registry_metadata:
            if not click.confirm("WARNING: Updates to parent-ref and connection-properties and registry-metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if connection_properties is not None:
        _details['connectionProperties'] = cli_util.parse_json_parameter("connection_properties", connection_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if username is not None:
        _details['username'] = username

    if password is not None:
        _details['password'] = password

    _details['modelType'] = 'ORACLE_ADWC_CONNECTION'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_connection(
        workspace_id=workspace_id,
        connection_key=connection_key,
        update_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_integration.update_data_asset.command_name', 'update'), help=u"""Updates a specific data asset with default connection.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-asset-key', required=True, help=u"""Data asset key.""")
@cli_util.option('--model-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ORACLE_DATA_ASSET", "ORACLE_OBJECT_STORAGE_DATA_ASSET", "ORACLE_ATP_DATA_ASSET", "ORACLE_ADWC_DATA_ASSET"]), help=u"""The type of the data asset.""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify data asset.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def update_data_asset(ctx, from_json, force, workspace_id, data_asset_key, model_type, key, object_version, model_version, name, description, object_status, identifier, external_key, asset_properties, registry_metadata, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')
    if not force:
        if asset_properties or registry_metadata:
            if not click.confirm("WARNING: Updates to asset-properties and registry-metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelType'] = model_type
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if external_key is not None:
        _details['externalKey'] = external_key

    if asset_properties is not None:
        _details['assetProperties'] = cli_util.parse_json_parameter("asset_properties", asset_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_data_asset(
        workspace_id=workspace_id,
        data_asset_key=data_asset_key,
        update_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_integration.update_data_asset_update_data_asset_from_atp.command_name', 'update-data-asset-update-data-asset-from-atp'), help=u"""Updates a specific data asset with default connection.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-asset-key', required=True, help=u"""Data asset key.""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify data asset.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--service-name', help=u"""The service name for the data asset.""")
@cli_util.option('--driver-class', help=u"""The driver class for the data asset.""")
@cli_util.option('--credential-file-content', help=u"""The credential file content from a wallet for the data asset.""")
@cli_util.option('--default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'UpdateConnectionFromAtp'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'UpdateConnectionFromAtp'}}, output_type={'module': 'data_integration', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def update_data_asset_update_data_asset_from_atp(ctx, from_json, force, workspace_id, data_asset_key, key, object_version, model_version, name, description, object_status, identifier, external_key, asset_properties, registry_metadata, service_name, driver_class, credential_file_content, default_connection, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')
    if not force:
        if asset_properties or registry_metadata or default_connection:
            if not click.confirm("WARNING: Updates to asset-properties and registry-metadata and default-connection will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if external_key is not None:
        _details['externalKey'] = external_key

    if asset_properties is not None:
        _details['assetProperties'] = cli_util.parse_json_parameter("asset_properties", asset_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if service_name is not None:
        _details['serviceName'] = service_name

    if driver_class is not None:
        _details['driverClass'] = driver_class

    if credential_file_content is not None:
        _details['credentialFileContent'] = credential_file_content

    if default_connection is not None:
        _details['defaultConnection'] = cli_util.parse_json_parameter("default_connection", default_connection)

    _details['modelType'] = 'ORACLE_ATP_DATA_ASSET'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_data_asset(
        workspace_id=workspace_id,
        data_asset_key=data_asset_key,
        update_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_integration.update_data_asset_update_data_asset_from_adwc.command_name', 'update-data-asset-update-data-asset-from-adwc'), help=u"""Updates a specific data asset with default connection.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-asset-key', required=True, help=u"""Data asset key.""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify data asset.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--service-name', help=u"""The service name for the data asset.""")
@cli_util.option('--driver-class', help=u"""The driver class for the data asset.""")
@cli_util.option('--credential-file-content', help=u"""The credential file content from a wallet for the data asset.""")
@cli_util.option('--default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'UpdateConnectionFromAdwc'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'UpdateConnectionFromAdwc'}}, output_type={'module': 'data_integration', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def update_data_asset_update_data_asset_from_adwc(ctx, from_json, force, workspace_id, data_asset_key, key, object_version, model_version, name, description, object_status, identifier, external_key, asset_properties, registry_metadata, service_name, driver_class, credential_file_content, default_connection, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')
    if not force:
        if asset_properties or registry_metadata or default_connection:
            if not click.confirm("WARNING: Updates to asset-properties and registry-metadata and default-connection will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if external_key is not None:
        _details['externalKey'] = external_key

    if asset_properties is not None:
        _details['assetProperties'] = cli_util.parse_json_parameter("asset_properties", asset_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if service_name is not None:
        _details['serviceName'] = service_name

    if driver_class is not None:
        _details['driverClass'] = driver_class

    if credential_file_content is not None:
        _details['credentialFileContent'] = credential_file_content

    if default_connection is not None:
        _details['defaultConnection'] = cli_util.parse_json_parameter("default_connection", default_connection)

    _details['modelType'] = 'ORACLE_ADWC_DATA_ASSET'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_data_asset(
        workspace_id=workspace_id,
        data_asset_key=data_asset_key,
        update_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_integration.update_data_asset_update_data_asset_from_object_storage.command_name', 'update-data-asset-update-data-asset-from-object-storage'), help=u"""Updates a specific data asset with default connection.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-asset-key', required=True, help=u"""Data asset key.""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify data asset.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--url', help=u"""url""")
@cli_util.option('--tenancy-id', help=u"""The OCI tenancy OCID.""")
@cli_util.option('--namespace', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'UpdateConnectionFromObjectStorage'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'UpdateConnectionFromObjectStorage'}}, output_type={'module': 'data_integration', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def update_data_asset_update_data_asset_from_object_storage(ctx, from_json, force, workspace_id, data_asset_key, key, object_version, model_version, name, description, object_status, identifier, external_key, asset_properties, registry_metadata, url, tenancy_id, namespace, default_connection, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')
    if not force:
        if asset_properties or registry_metadata or default_connection:
            if not click.confirm("WARNING: Updates to asset-properties and registry-metadata and default-connection will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if external_key is not None:
        _details['externalKey'] = external_key

    if asset_properties is not None:
        _details['assetProperties'] = cli_util.parse_json_parameter("asset_properties", asset_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if url is not None:
        _details['url'] = url

    if tenancy_id is not None:
        _details['tenancyId'] = tenancy_id

    if namespace is not None:
        _details['namespace'] = namespace

    if default_connection is not None:
        _details['defaultConnection'] = cli_util.parse_json_parameter("default_connection", default_connection)

    _details['modelType'] = 'ORACLE_OBJECT_STORAGE_DATA_ASSET'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_data_asset(
        workspace_id=workspace_id,
        data_asset_key=data_asset_key,
        update_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_integration.update_data_asset_update_data_asset_from_oracle.command_name', 'update-data-asset-update-data-asset-from-oracle'), help=u"""Updates a specific data asset with default connection.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-asset-key', required=True, help=u"""Data asset key.""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify data asset.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--external-key', help=u"""The external key for the object""")
@cli_util.option('--asset-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""assetProperties""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--host', help=u"""The host details for the data asset.""")
@cli_util.option('--port', help=u"""The port details for the data asset.""")
@cli_util.option('--service-name', help=u"""The service name for the data asset.""")
@cli_util.option('--driver-class', help=u"""The driver class for the data asset.""")
@cli_util.option('--sid', help=u"""sid""")
@cli_util.option('--credential-file-content', help=u"""The credential file content from a wallet for the data asset.""")
@cli_util.option('--default-connection', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'UpdateConnectionFromOracle'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'asset-properties': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'default-connection': {'module': 'data_integration', 'class': 'UpdateConnectionFromOracle'}}, output_type={'module': 'data_integration', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def update_data_asset_update_data_asset_from_oracle(ctx, from_json, force, workspace_id, data_asset_key, key, object_version, model_version, name, description, object_status, identifier, external_key, asset_properties, registry_metadata, host, port, service_name, driver_class, sid, credential_file_content, default_connection, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')
    if not force:
        if asset_properties or registry_metadata or default_connection:
            if not click.confirm("WARNING: Updates to asset-properties and registry-metadata and default-connection will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if external_key is not None:
        _details['externalKey'] = external_key

    if asset_properties is not None:
        _details['assetProperties'] = cli_util.parse_json_parameter("asset_properties", asset_properties)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if host is not None:
        _details['host'] = host

    if port is not None:
        _details['port'] = port

    if service_name is not None:
        _details['serviceName'] = service_name

    if driver_class is not None:
        _details['driverClass'] = driver_class

    if sid is not None:
        _details['sid'] = sid

    if credential_file_content is not None:
        _details['credentialFileContent'] = credential_file_content

    if default_connection is not None:
        _details['defaultConnection'] = cli_util.parse_json_parameter("default_connection", default_connection)

    _details['modelType'] = 'ORACLE_DATA_ASSET'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_data_asset(
        workspace_id=workspace_id,
        data_asset_key=data_asset_key,
        update_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_flow_group.command(name=cli_util.override('data_integration.update_data_flow.command_name', 'update'), help=u"""Updates a specific data flow.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--data-flow-key', required=True, help=u"""DIS DataFlow key""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.""")
@cli_util.option('--model-type', required=True, help=u"""The type of the object.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--nodes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of nodes.

This option is a JSON list with items of type FlowNode.  For documentation on FlowNode please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/FlowNode.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--flow-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'nodes': {'module': 'data_integration', 'class': 'list[FlowNode]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'flow-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'nodes': {'module': 'data_integration', 'class': 'list[FlowNode]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'flow-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'DataFlow'})
@cli_util.wrap_exceptions
def update_data_flow(ctx, from_json, force, workspace_id, data_flow_key, key, model_type, object_version, model_version, parent_ref, name, identifier, nodes, parameters, description, flow_config_values, object_status, registry_metadata, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(data_flow_key, six.string_types) and len(data_flow_key.strip()) == 0:
        raise click.UsageError('Parameter --data-flow-key cannot be whitespace or empty string')
    if not force:
        if parent_ref or nodes or parameters or flow_config_values or registry_metadata:
            if not click.confirm("WARNING: Updates to parent-ref and nodes and parameters and flow-config-values and registry-metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['modelType'] = model_type
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if identifier is not None:
        _details['identifier'] = identifier

    if nodes is not None:
        _details['nodes'] = cli_util.parse_json_parameter("nodes", nodes)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if description is not None:
        _details['description'] = description

    if flow_config_values is not None:
        _details['flowConfigValues'] = cli_util.parse_json_parameter("flow_config_values", flow_config_values)

    if object_status is not None:
        _details['objectStatus'] = object_status

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_data_flow(
        workspace_id=workspace_id,
        data_flow_key=data_flow_key,
        update_data_flow_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@folder_group.command(name=cli_util.override('data_integration.update_folder.command_name', 'update'), help=u"""Updates a specific folder.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--folder-key', required=True, help=u"""DIS Folder key""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify folder.""")
@cli_util.option('--model-type', required=True, help=u"""The type of the object.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--category-name', help=u"""categoryName""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Folder'})
@cli_util.wrap_exceptions
def update_folder(ctx, from_json, force, workspace_id, folder_key, key, model_type, object_version, model_version, name, description, category_name, object_status, identifier, parent_ref, registry_metadata, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(folder_key, six.string_types) and len(folder_key.strip()) == 0:
        raise click.UsageError('Parameter --folder-key cannot be whitespace or empty string')
    if not force:
        if parent_ref or registry_metadata:
            if not click.confirm("WARNING: Updates to parent-ref and registry-metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['modelType'] = model_type
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if category_name is not None:
        _details['categoryName'] = category_name

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_folder(
        workspace_id=workspace_id,
        folder_key=folder_key,
        update_folder_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@project_group.command(name=cli_util.override('data_integration.update_project.command_name', 'update'), help=u"""Updates a specific project.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--project-key', required=True, help=u"""DIS Project key""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify project.""")
@cli_util.option('--model-type', required=True, help=u"""The type of the object.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Project'})
@cli_util.wrap_exceptions
def update_project(ctx, from_json, force, workspace_id, project_key, key, model_type, object_version, model_version, name, description, object_status, identifier, parent_ref, registry_metadata, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(project_key, six.string_types) and len(project_key.strip()) == 0:
        raise click.UsageError('Parameter --project-key cannot be whitespace or empty string')
    if not force:
        if parent_ref or registry_metadata:
            if not click.confirm("WARNING: Updates to parent-ref and registry-metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['modelType'] = model_type
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_project(
        workspace_id=workspace_id,
        project_key=project_key,
        update_project_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_group.command(name=cli_util.override('data_integration.update_task.command_name', 'update'), help=u"""Updates a specific task. For example, you can update the task description or move the task to a different folder by changing the `aggregatorKey` to a different folder in the registry.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--task-key', required=True, help=u"""DIS Task key""")
@cli_util.option('--model-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["INTEGRATION_TASK", "DATA_LOADER_TASK"]), help=u"""The type of the task.""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--input-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of input ports.

This option is a JSON list with items of type InputPort.  For documentation on InputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/InputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of output ports.

This option is a JSON list with items of type OutputPort.  For documentation on OutputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/OutputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--op-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-provider-delegate', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'Task'})
@cli_util.wrap_exceptions
def update_task(ctx, from_json, force, workspace_id, task_key, model_type, key, object_version, model_version, parent_ref, name, description, object_status, identifier, input_ports, output_ports, parameters, op_config_values, config_provider_delegate, registry_metadata, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(task_key, six.string_types) and len(task_key.strip()) == 0:
        raise click.UsageError('Parameter --task-key cannot be whitespace or empty string')
    if not force:
        if parent_ref or input_ports or output_ports or parameters or op_config_values or config_provider_delegate or registry_metadata:
            if not click.confirm("WARNING: Updates to parent-ref and input-ports and output-ports and parameters and op-config-values and config-provider-delegate and registry-metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['modelType'] = model_type
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if input_ports is not None:
        _details['inputPorts'] = cli_util.parse_json_parameter("input_ports", input_ports)

    if output_ports is not None:
        _details['outputPorts'] = cli_util.parse_json_parameter("output_ports", output_ports)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if op_config_values is not None:
        _details['opConfigValues'] = cli_util.parse_json_parameter("op_config_values", op_config_values)

    if config_provider_delegate is not None:
        _details['configProviderDelegate'] = cli_util.parse_json_parameter("config_provider_delegate", config_provider_delegate)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_task(
        workspace_id=workspace_id,
        task_key=task_key,
        update_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_group.command(name=cli_util.override('data_integration.update_task_update_task_from_data_loader_task.command_name', 'update-task-update-task-from-data-loader-task'), help=u"""Updates a specific task. For example, you can update the task description or move the task to a different folder by changing the `aggregatorKey` to a different folder in the registry.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--task-key', required=True, help=u"""DIS Task key""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--input-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of input ports.

This option is a JSON list with items of type InputPort.  For documentation on InputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/InputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of output ports.

This option is a JSON list with items of type OutputPort.  For documentation on OutputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/OutputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--op-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-provider-delegate', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-flow', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-flow': {'module': 'data_integration', 'class': 'DataFlow'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-flow': {'module': 'data_integration', 'class': 'DataFlow'}}, output_type={'module': 'data_integration', 'class': 'Task'})
@cli_util.wrap_exceptions
def update_task_update_task_from_data_loader_task(ctx, from_json, force, workspace_id, task_key, key, object_version, model_version, parent_ref, name, description, object_status, identifier, input_ports, output_ports, parameters, op_config_values, config_provider_delegate, registry_metadata, data_flow, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(task_key, six.string_types) and len(task_key.strip()) == 0:
        raise click.UsageError('Parameter --task-key cannot be whitespace or empty string')
    if not force:
        if parent_ref or input_ports or output_ports or parameters or op_config_values or config_provider_delegate or registry_metadata or data_flow:
            if not click.confirm("WARNING: Updates to parent-ref and input-ports and output-ports and parameters and op-config-values and config-provider-delegate and registry-metadata and data-flow will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if input_ports is not None:
        _details['inputPorts'] = cli_util.parse_json_parameter("input_ports", input_ports)

    if output_ports is not None:
        _details['outputPorts'] = cli_util.parse_json_parameter("output_ports", output_ports)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if op_config_values is not None:
        _details['opConfigValues'] = cli_util.parse_json_parameter("op_config_values", op_config_values)

    if config_provider_delegate is not None:
        _details['configProviderDelegate'] = cli_util.parse_json_parameter("config_provider_delegate", config_provider_delegate)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if data_flow is not None:
        _details['dataFlow'] = cli_util.parse_json_parameter("data_flow", data_flow)

    _details['modelType'] = 'DATA_LOADER_TASK'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_task(
        workspace_id=workspace_id,
        task_key=task_key,
        update_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_group.command(name=cli_util.override('data_integration.update_task_update_task_from_integration_task.command_name', 'update-task-update-task-from-integration-task'), help=u"""Updates a specific task. For example, you can update the task description or move the task to a different folder by changing the `aggregatorKey` to a different folder in the registry.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--task-key', required=True, help=u"""DIS Task key""")
@cli_util.option('--key', required=True, help=u"""Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.""")
@cli_util.option('--object-version', required=True, type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--parent-ref', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-status', type=click.INT, help=u"""The status of an object that can be set to value 1 for shallow references across objects, other values reserved.""")
@cli_util.option('--identifier', help=u"""Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.""")
@cli_util.option('--input-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of input ports.

This option is a JSON list with items of type InputPort.  For documentation on InputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/InputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--output-ports', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of output ports.

This option is a JSON list with items of type OutputPort.  For documentation on OutputPort please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/OutputPort.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of parameters.

This option is a JSON list with items of type Parameter.  For documentation on Parameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/dataintegration/20200430/datatypes/Parameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--op-config-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--config-provider-delegate', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--data-flow', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-flow': {'module': 'data_integration', 'class': 'DataFlow'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parent-ref': {'module': 'data_integration', 'class': 'ParentReference'}, 'input-ports': {'module': 'data_integration', 'class': 'list[InputPort]'}, 'output-ports': {'module': 'data_integration', 'class': 'list[OutputPort]'}, 'parameters': {'module': 'data_integration', 'class': 'list[Parameter]'}, 'op-config-values': {'module': 'data_integration', 'class': 'ConfigValues'}, 'config-provider-delegate': {'module': 'data_integration', 'class': 'ConfigProvider'}, 'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}, 'data-flow': {'module': 'data_integration', 'class': 'DataFlow'}}, output_type={'module': 'data_integration', 'class': 'Task'})
@cli_util.wrap_exceptions
def update_task_update_task_from_integration_task(ctx, from_json, force, workspace_id, task_key, key, object_version, model_version, parent_ref, name, description, object_status, identifier, input_ports, output_ports, parameters, op_config_values, config_provider_delegate, registry_metadata, data_flow, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(task_key, six.string_types) and len(task_key.strip()) == 0:
        raise click.UsageError('Parameter --task-key cannot be whitespace or empty string')
    if not force:
        if parent_ref or input_ports or output_ports or parameters or op_config_values or config_provider_delegate or registry_metadata or data_flow:
            if not click.confirm("WARNING: Updates to parent-ref and input-ports and output-ports and parameters and op-config-values and config-provider-delegate and registry-metadata and data-flow will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['key'] = key
    _details['objectVersion'] = object_version

    if model_version is not None:
        _details['modelVersion'] = model_version

    if parent_ref is not None:
        _details['parentRef'] = cli_util.parse_json_parameter("parent_ref", parent_ref)

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_status is not None:
        _details['objectStatus'] = object_status

    if identifier is not None:
        _details['identifier'] = identifier

    if input_ports is not None:
        _details['inputPorts'] = cli_util.parse_json_parameter("input_ports", input_ports)

    if output_ports is not None:
        _details['outputPorts'] = cli_util.parse_json_parameter("output_ports", output_ports)

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if op_config_values is not None:
        _details['opConfigValues'] = cli_util.parse_json_parameter("op_config_values", op_config_values)

    if config_provider_delegate is not None:
        _details['configProviderDelegate'] = cli_util.parse_json_parameter("config_provider_delegate", config_provider_delegate)

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    if data_flow is not None:
        _details['dataFlow'] = cli_util.parse_json_parameter("data_flow", data_flow)

    _details['modelType'] = 'INTEGRATION_TASK'

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_task(
        workspace_id=workspace_id,
        task_key=task_key,
        update_task_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@task_run_group.command(name=cli_util.override('data_integration.update_task_run.command_name', 'update'), help=u"""Updates the status of the task run. For example, aborts a task run.""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--application-key', required=True, help=u"""DIS application key""")
@cli_util.option('--task-run-key', required=True, help=u"""DIS taskRun key""")
@cli_util.option('--key', help=u"""The key of the object.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["TERMINATING"]), help=u"""status""")
@cli_util.option('--model-type', help=u"""The type of the object.""")
@cli_util.option('--model-version', help=u"""The model version of an object.""")
@cli_util.option('--name', help=u"""Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters""")
@cli_util.option('--description', help=u"""Detailed description for the object.""")
@cli_util.option('--object-version', type=click.INT, help=u"""The version of the object that is used to track changes in the object instance.""")
@cli_util.option('--registry-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'registry-metadata': {'module': 'data_integration', 'class': 'RegistryMetadata'}}, output_type={'module': 'data_integration', 'class': 'TaskRunDetails'})
@cli_util.wrap_exceptions
def update_task_run(ctx, from_json, force, workspace_id, application_key, task_run_key, key, status, model_type, model_version, name, description, object_version, registry_metadata, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')

    if isinstance(application_key, six.string_types) and len(application_key.strip()) == 0:
        raise click.UsageError('Parameter --application-key cannot be whitespace or empty string')

    if isinstance(task_run_key, six.string_types) and len(task_run_key.strip()) == 0:
        raise click.UsageError('Parameter --task-run-key cannot be whitespace or empty string')
    if not force:
        if registry_metadata:
            if not click.confirm("WARNING: Updates to registry-metadata will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if key is not None:
        _details['key'] = key

    if status is not None:
        _details['status'] = status

    if model_type is not None:
        _details['modelType'] = model_type

    if model_version is not None:
        _details['modelVersion'] = model_version

    if name is not None:
        _details['name'] = name

    if description is not None:
        _details['description'] = description

    if object_version is not None:
        _details['objectVersion'] = object_version

    if registry_metadata is not None:
        _details['registryMetadata'] = cli_util.parse_json_parameter("registry_metadata", registry_metadata)

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_task_run(
        workspace_id=workspace_id,
        application_key=application_key,
        task_run_key=task_run_key,
        update_task_run_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@workspace_group.command(name=cli_util.override('data_integration.update_workspace.command_name', 'update'), help=u"""Updates the Data Integration Workspace""")
@cli_util.option('--workspace-id', required=True, help=u"""DIS workspace id""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. See [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A detailed description for the workspace.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name for the workspace. Does not have to be unique, and can be modified. Avoid entering confidential information.""")
@cli_util.option('--if-match', help=u"""Update and Delete operations should accept an optional If-Match header, in which clients can send a previously-received ETag. When If-Match is provided and its value does not exactly match the ETag of the resource on the server, the request should fail with HTTP response status code 412""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_integration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_integration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_integration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_integration', 'class': 'Workspace'})
@cli_util.wrap_exceptions
def update_workspace(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, workspace_id, freeform_tags, defined_tags, description, display_name, if_match):

    if isinstance(workspace_id, six.string_types) and len(workspace_id.strip()) == 0:
        raise click.UsageError('Parameter --workspace-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('data_integration', 'data_integration', ctx)
    result = client.update_workspace(
        workspace_id=workspace_id,
        update_workspace_details=_details,
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
