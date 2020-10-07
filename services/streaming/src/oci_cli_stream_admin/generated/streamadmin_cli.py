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
from services.streaming.src.oci_cli_streaming.generated import streaming_service_cli


@click.command(cli_util.override('stream_admin.stream_admin_root_group.command_name', 'stream-admin'), cls=CommandGroupWithAlias, help=cli_util.override('stream_admin.stream_admin_root_group.help', """The API for the Streaming Service."""), short_help=cli_util.override('stream_admin.stream_admin_root_group.short_help', """Streaming Service API"""))
@cli_util.help_option_group
def stream_admin_root_group():
    pass


@click.command(cli_util.override('stream_admin.stream_pool_group.command_name', 'stream-pool'), cls=CommandGroupWithAlias, help="""The details of a stream pool.""")
@cli_util.help_option_group
def stream_pool_group():
    pass


@click.command(cli_util.override('stream_admin.stream_group.command_name', 'stream'), cls=CommandGroupWithAlias, help="""Detailed representation of a stream, including all its partitions.""")
@cli_util.help_option_group
def stream_group():
    pass


@click.command(cli_util.override('stream_admin.connect_harness_group.command_name', 'connect-harness'), cls=CommandGroupWithAlias, help="""Detailed representation of a connect harness.""")
@cli_util.help_option_group
def connect_harness_group():
    pass


streaming_service_cli.streaming_service_group.add_command(stream_admin_root_group)
stream_admin_root_group.add_command(stream_pool_group)
stream_admin_root_group.add_command(stream_group)
stream_admin_root_group.add_command(connect_harness_group)


@connect_harness_group.command(name=cli_util.override('stream_admin.change_connect_harness_compartment.command_name', 'change-compartment'), help=u"""Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeConnectHarnessCompartment)""")
@cli_util.option('--connect-harness-id', required=True, help=u"""The OCID of the connect harness.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_connect_harness_compartment(ctx, from_json, connect_harness_id, compartment_id, if_match):

    if isinstance(connect_harness_id, six.string_types) and len(connect_harness_id.strip()) == 0:
        raise click.UsageError('Parameter --connect-harness-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.change_connect_harness_compartment(
        connect_harness_id=connect_harness_id,
        change_connect_harness_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@stream_group.command(name=cli_util.override('stream_admin.change_stream_compartment.command_name', 'change-compartment'), help=u"""Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource. The stream will also be moved into the default stream pool in the destination compartment. \n[Command Reference](changeStreamCompartment)""")
@cli_util.option('--stream-id', required=True, help=u"""The OCID of the stream.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_stream_compartment(ctx, from_json, stream_id, compartment_id, if_match):

    if isinstance(stream_id, six.string_types) and len(stream_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.change_stream_compartment(
        stream_id=stream_id,
        change_stream_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@stream_pool_group.command(name=cli_util.override('stream_admin.change_stream_pool_compartment.command_name', 'change-compartment'), help=u"""Moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeStreamPoolCompartment)""")
@cli_util.option('--stream-pool-id', required=True, help=u"""The OCID of the stream pool.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_stream_pool_compartment(ctx, from_json, stream_pool_id, compartment_id, if_match):

    if isinstance(stream_pool_id, six.string_types) and len(stream_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-pool-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.change_stream_pool_compartment(
        stream_pool_id=stream_pool_id,
        change_stream_pool_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connect_harness_group.command(name=cli_util.override('stream_admin.create_connect_harness.command_name', 'create'), help=u"""Starts the provisioning of a new connect harness. To track the progress of the provisioning, you can periodically call [GetConnectHarness]. In the response, the `lifecycleState` parameter of the [ConnectHarness] object tells you its current state. \n[Command Reference](createConnectHarness)""")
@cli_util.option('--name', required=True, help=u"""The name of the connect harness. Avoid entering confidential information.

Example: `JDBCConnector`""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the connect harness.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'streaming', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'streaming', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'streaming', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'streaming', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'streaming', 'class': 'ConnectHarness'})
@cli_util.wrap_exceptions
def create_connect_harness(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.create_connect_harness(
        create_connect_harness_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_connect_harness') and callable(getattr(client, 'get_connect_harness')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_connect_harness(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@stream_group.command(name=cli_util.override('stream_admin.create_stream.command_name', 'create'), help=u"""Starts the provisioning of a new stream. The stream will be created in the given compartment id or stream pool id, depending on which parameter is specified. Compartment id and stream pool id cannot be specified at the same time. To track the progress of the provisioning, you can periodically call [GetStream]. In the response, the `lifecycleState` parameter of the [Stream] object tells you its current state. \n[Command Reference](createStream)""")
@cli_util.option('--name', required=True, help=u"""The name of the stream. Avoid entering confidential information.

Example: `TelemetryEvents`""")
@cli_util.option('--partitions', required=True, type=click.INT, help=u"""The number of partitions in the stream.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment that contains the stream.""")
@cli_util.option('--stream-pool-id', help=u"""The OCID of the stream pool that contains the stream.""")
@cli_util.option('--retention-in-hours', type=click.INT, help=u"""The retention period of the stream, in hours. Accepted values are between 24 and 168 (7 days). If not specified, the stream will have a retention period of 24 hours.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'streaming', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'streaming', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'streaming', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'streaming', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'streaming', 'class': 'Stream'})
@cli_util.wrap_exceptions
def create_stream(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, partitions, compartment_id, stream_pool_id, retention_in_hours, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['partitions'] = partitions

    if compartment_id is not None:
        _details['compartmentId'] = compartment_id

    if stream_pool_id is not None:
        _details['streamPoolId'] = stream_pool_id

    if retention_in_hours is not None:
        _details['retentionInHours'] = retention_in_hours

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.create_stream(
        create_stream_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream') and callable(getattr(client, 'get_stream')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@stream_pool_group.command(name=cli_util.override('stream_admin.create_stream_pool.command_name', 'create'), help=u"""Starts the provisioning of a new stream pool. To track the progress of the provisioning, you can periodically call GetStreamPool. In the response, the `lifecycleState` parameter of the object tells you its current state. \n[Command Reference](createStreamPool)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment that contains the stream.""")
@cli_util.option('--name', required=True, help=u"""The name of the stream pool. Avoid entering confidential information.

Example: `MyStreamPool`""")
@cli_util.option('--kafka-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--custom-encryption-key-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--private-endpoint-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'kafka-settings': {'module': 'streaming', 'class': 'KafkaSettings'}, 'custom-encryption-key-details': {'module': 'streaming', 'class': 'CustomEncryptionKeyDetails'}, 'private-endpoint-details': {'module': 'streaming', 'class': 'PrivateEndpointDetails'}, 'freeform-tags': {'module': 'streaming', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'streaming', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'kafka-settings': {'module': 'streaming', 'class': 'KafkaSettings'}, 'custom-encryption-key-details': {'module': 'streaming', 'class': 'CustomEncryptionKeyDetails'}, 'private-endpoint-details': {'module': 'streaming', 'class': 'PrivateEndpointDetails'}, 'freeform-tags': {'module': 'streaming', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'streaming', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'streaming', 'class': 'StreamPool'})
@cli_util.wrap_exceptions
def create_stream_pool(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, name, kafka_settings, custom_encryption_key_details, private_endpoint_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['name'] = name

    if kafka_settings is not None:
        _details['kafkaSettings'] = cli_util.parse_json_parameter("kafka_settings", kafka_settings)

    if custom_encryption_key_details is not None:
        _details['customEncryptionKeyDetails'] = cli_util.parse_json_parameter("custom_encryption_key_details", custom_encryption_key_details)

    if private_endpoint_details is not None:
        _details['privateEndpointDetails'] = cli_util.parse_json_parameter("private_endpoint_details", private_endpoint_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.create_stream_pool(
        create_stream_pool_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_pool') and callable(getattr(client, 'get_stream_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@connect_harness_group.command(name=cli_util.override('stream_admin.delete_connect_harness.command_name', 'delete'), help=u"""Deletes a connect harness and its content. Connect harness contents are deleted immediately. The service retains records of the connect harness itself for 90 days after deletion. The `lifecycleState` parameter of the `ConnectHarness` object changes to `DELETING` and the connect harness becomes inaccessible for read or write operations. To verify that a connect harness has been deleted, make a [GetConnectHarness] request. If the call returns the connect harness's lifecycle state as `DELETED`, then the connect harness has been deleted. If the call returns a \"404 Not Found\" error, that means all records of the connect harness have been deleted. \n[Command Reference](deleteConnectHarness)""")
@cli_util.option('--connect-harness-id', required=True, help=u"""The OCID of the connect harness.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_connect_harness(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, connect_harness_id, if_match):

    if isinstance(connect_harness_id, six.string_types) and len(connect_harness_id.strip()) == 0:
        raise click.UsageError('Parameter --connect-harness-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.delete_connect_harness(
        connect_harness_id=connect_harness_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_connect_harness') and callable(getattr(client, 'get_connect_harness')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_connect_harness(connect_harness_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@stream_group.command(name=cli_util.override('stream_admin.delete_stream.command_name', 'delete'), help=u"""Deletes a stream and its content. Stream contents are deleted immediately. The service retains records of the stream itself for 90 days after deletion. The `lifecycleState` parameter of the `Stream` object changes to `DELETING` and the stream becomes inaccessible for read or write operations. To verify that a stream has been deleted, make a [GetStream] request. If the call returns the stream's lifecycle state as `DELETED`, then the stream has been deleted. If the call returns a \"404 Not Found\" error, that means all records of the stream have been deleted. \n[Command Reference](deleteStream)""")
@cli_util.option('--stream-id', required=True, help=u"""The OCID of the stream.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_stream(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stream_id, if_match):

    if isinstance(stream_id, six.string_types) and len(stream_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.delete_stream(
        stream_id=stream_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream') and callable(getattr(client, 'get_stream')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_stream(stream_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@stream_pool_group.command(name=cli_util.override('stream_admin.delete_stream_pool.command_name', 'delete'), help=u"""Deletes a stream pool. All containing streams will also be deleted. The default stream pool of a compartment cannot be deleted. \n[Command Reference](deleteStreamPool)""")
@cli_util.option('--stream-pool-id', required=True, help=u"""The OCID of the stream pool.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_stream_pool(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, stream_pool_id, if_match):

    if isinstance(stream_pool_id, six.string_types) and len(stream_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-pool-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.delete_stream_pool(
        stream_pool_id=stream_pool_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_pool') and callable(getattr(client, 'get_stream_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_stream_pool(stream_pool_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@connect_harness_group.command(name=cli_util.override('stream_admin.get_connect_harness.command_name', 'get'), help=u"""Gets detailed information about a connect harness. \n[Command Reference](getConnectHarness)""")
@cli_util.option('--connect-harness-id', required=True, help=u"""The OCID of the connect harness.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'streaming', 'class': 'ConnectHarness'})
@cli_util.wrap_exceptions
def get_connect_harness(ctx, from_json, connect_harness_id):

    if isinstance(connect_harness_id, six.string_types) and len(connect_harness_id.strip()) == 0:
        raise click.UsageError('Parameter --connect-harness-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.get_connect_harness(
        connect_harness_id=connect_harness_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@stream_group.command(name=cli_util.override('stream_admin.get_stream.command_name', 'get'), help=u"""Gets detailed information about a stream, including the number of partitions. \n[Command Reference](getStream)""")
@cli_util.option('--stream-id', required=True, help=u"""The OCID of the stream.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'streaming', 'class': 'Stream'})
@cli_util.wrap_exceptions
def get_stream(ctx, from_json, stream_id):

    if isinstance(stream_id, six.string_types) and len(stream_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.get_stream(
        stream_id=stream_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@stream_pool_group.command(name=cli_util.override('stream_admin.get_stream_pool.command_name', 'get'), help=u"""Gets detailed information about the stream pool, such as Kafka settings. \n[Command Reference](getStreamPool)""")
@cli_util.option('--stream-pool-id', required=True, help=u"""The OCID of the stream pool.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'streaming', 'class': 'StreamPool'})
@cli_util.wrap_exceptions
def get_stream_pool(ctx, from_json, stream_pool_id):

    if isinstance(stream_pool_id, six.string_types) and len(stream_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-pool-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.get_stream_pool(
        stream_pool_id=stream_pool_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connect_harness_group.command(name=cli_util.override('stream_admin.list_connect_harnesses.command_name', 'list'), help=u"""Lists the connectharness. \n[Command Reference](listConnectHarnesses)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--id', help=u"""A filter to return only resources that match the given ID exactly.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the given name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return. The value must be between 1 and 50. The default is 10.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. You can provide no more than one sort order. By default, `TIMECREATED` sorts results in descending order and `NAME` sorts results in ascending order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]), help=u"""A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'streaming', 'class': 'list[ConnectHarnessSummary]'})
@cli_util.wrap_exceptions
def list_connect_harnesses(ctx, from_json, all_pages, page_size, compartment_id, id, name, limit, page, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_connect_harnesses,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_connect_harnesses,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_connect_harnesses(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@stream_pool_group.command(name=cli_util.override('stream_admin.list_stream_pools.command_name', 'list'), help=u"""List the stream pools for a given compartment ID. \n[Command Reference](listStreamPools)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--id', help=u"""A filter to return only resources that match the given ID exactly.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the given name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return. The value must be between 1 and 50. The default is 10.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. You can provide no more than one sort order. By default, `TIMECREATED` sorts results in descending order and `NAME` sorts results in ascending order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]), help=u"""A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'streaming', 'class': 'list[StreamPoolSummary]'})
@cli_util.wrap_exceptions
def list_stream_pools(ctx, from_json, all_pages, page_size, compartment_id, id, name, limit, page, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_stream_pools,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_stream_pools,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_stream_pools(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@stream_group.command(name=cli_util.override('stream_admin.list_streams.command_name', 'list'), help=u"""Lists the streams in the given compartment id. If the compartment id is specified, it will list streams in the compartment, regardless of their stream pool. If the stream pool id is specified, the action will be scoped to that stream pool. The compartment id and stream pool id cannot be specified at the same time. \n[Command Reference](listStreams)""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment. Is exclusive with the `streamPoolId` parameter. One of them is required.""")
@cli_util.option('--stream-pool-id', help=u"""The OCID of the stream pool. Is exclusive with the `compartmentId` parameter. One of them is required.""")
@cli_util.option('--id', help=u"""A filter to return only resources that match the given ID exactly.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the given name exactly.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return. The value must be between 1 and 50. The default is 10.""")
@cli_util.option('--page', help=u"""The page at which to start retrieving results.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["NAME", "TIMECREATED"]), help=u"""The field to sort by. You can provide no more than one sort order. By default, `TIMECREATED` sorts results in descending order and `NAME` sorts results in ascending order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]), help=u"""A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'streaming', 'class': 'list[StreamSummary]'})
@cli_util.wrap_exceptions
def list_streams(ctx, from_json, all_pages, page_size, compartment_id, stream_pool_id, id, name, limit, page, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if stream_pool_id is not None:
        kwargs['stream_pool_id'] = stream_pool_id
    if id is not None:
        kwargs['id'] = id
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_streams,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_streams,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_streams(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@connect_harness_group.command(name=cli_util.override('stream_admin.update_connect_harness.command_name', 'update'), help=u"""Updates the tags applied to the connect harness. \n[Command Reference](updateConnectHarness)""")
@cli_util.option('--connect-harness-id', required=True, help=u"""The OCID of the connect harness.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'streaming', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'streaming', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'streaming', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'streaming', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'streaming', 'class': 'ConnectHarness'})
@cli_util.wrap_exceptions
def update_connect_harness(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, connect_harness_id, freeform_tags, defined_tags, if_match):

    if isinstance(connect_harness_id, six.string_types) and len(connect_harness_id.strip()) == 0:
        raise click.UsageError('Parameter --connect-harness-id cannot be whitespace or empty string')
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

    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.update_connect_harness(
        connect_harness_id=connect_harness_id,
        update_connect_harness_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_connect_harness') and callable(getattr(client, 'get_connect_harness')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_connect_harness(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@stream_group.command(name=cli_util.override('stream_admin.update_stream.command_name', 'update'), help=u"""Updates the stream. Only specified values will be updated. \n[Command Reference](updateStream)""")
@cli_util.option('--stream-id', required=True, help=u"""The OCID of the stream.""")
@cli_util.option('--stream-pool-id', help=u"""The [OCID] of the stream pool where the stream should be moved.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'streaming', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'streaming', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'streaming', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'streaming', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'streaming', 'class': 'Stream'})
@cli_util.wrap_exceptions
def update_stream(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stream_id, stream_pool_id, freeform_tags, defined_tags, if_match):

    if isinstance(stream_id, six.string_types) and len(stream_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if stream_pool_id is not None:
        _details['streamPoolId'] = stream_pool_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.update_stream(
        stream_id=stream_id,
        update_stream_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream') and callable(getattr(client, 'get_stream')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@stream_pool_group.command(name=cli_util.override('stream_admin.update_stream_pool.command_name', 'update'), help=u"""Updates the specified stream pool. \n[Command Reference](updateStreamPool)""")
@cli_util.option('--stream-pool-id', required=True, help=u"""The OCID of the stream pool.""")
@cli_util.option('--name', help=u"""""")
@cli_util.option('--kafka-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--custom-encryption-key-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair that is applied with no predefined name, type, or namespace. Exists for cross-compatibility only. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the if-match parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'kafka-settings': {'module': 'streaming', 'class': 'KafkaSettings'}, 'custom-encryption-key-details': {'module': 'streaming', 'class': 'CustomEncryptionKeyDetails'}, 'freeform-tags': {'module': 'streaming', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'streaming', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'kafka-settings': {'module': 'streaming', 'class': 'KafkaSettings'}, 'custom-encryption-key-details': {'module': 'streaming', 'class': 'CustomEncryptionKeyDetails'}, 'freeform-tags': {'module': 'streaming', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'streaming', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'streaming', 'class': 'StreamPool'})
@cli_util.wrap_exceptions
def update_stream_pool(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, stream_pool_id, name, kafka_settings, custom_encryption_key_details, freeform_tags, defined_tags, if_match):

    if isinstance(stream_pool_id, six.string_types) and len(stream_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --stream-pool-id cannot be whitespace or empty string')
    if not force:
        if kafka_settings or custom_encryption_key_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to kafka-settings and custom-encryption-key-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if name is not None:
        _details['name'] = name

    if kafka_settings is not None:
        _details['kafkaSettings'] = cli_util.parse_json_parameter("kafka_settings", kafka_settings)

    if custom_encryption_key_details is not None:
        _details['customEncryptionKeyDetails'] = cli_util.parse_json_parameter("custom_encryption_key_details", custom_encryption_key_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('streaming', 'stream_admin', ctx)
    result = client.update_stream_pool(
        stream_pool_id=stream_pool_id,
        update_stream_pool_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_stream_pool') and callable(getattr(client, 'get_stream_pool')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_stream_pool(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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
