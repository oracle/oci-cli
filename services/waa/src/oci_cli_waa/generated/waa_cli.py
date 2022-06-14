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
from services.waa.src.oci_cli_waa.generated import waa_service_cli


@click.command(cli_util.override('waa.waa_root_group.command_name', 'waa'), cls=CommandGroupWithAlias, help=cli_util.override('waa.waa_root_group.help', """API for the Web Application Acceleration service.
Use this API to manage regional Web App Acceleration policies such as Caching and Compression
for accelerating HTTP services."""), short_help=cli_util.override('waa.waa_root_group.short_help', """Web Application Acceleration (WAA) API"""))
@cli_util.help_option_group
def waa_root_group():
    pass


@click.command(cli_util.override('waa.web_app_acceleration_policy_group.command_name', 'web-app-acceleration-policy'), cls=CommandGroupWithAlias, help="""The details of WebAppAccelerationPolicy. A policy is comprised of rules, which allows enablement of Caching and Compression of HTTP response. Caching can be enabled for a particular path Compression is enabled at global level""")
@cli_util.help_option_group
def web_app_acceleration_policy_group():
    pass


@click.command(cli_util.override('waa.web_app_acceleration_group.command_name', 'web-app-acceleration'), cls=CommandGroupWithAlias, help="""A resource connecting a WebAppAccelerationPolicy to a backend of particular type, applying that policy's coverage to the backend.""")
@cli_util.help_option_group
def web_app_acceleration_group():
    pass


waa_service_cli.waa_service_group.add_command(waa_root_group)
waa_root_group.add_command(web_app_acceleration_policy_group)
waa_root_group.add_command(web_app_acceleration_group)
# oci waa waa --> oci waa
waa_service_cli.waa_service_group.commands.pop(waa_root_group.name)
waa_service_cli.waa_service_group.add_command(web_app_acceleration_policy_group)
waa_service_cli.waa_service_group.add_command(web_app_acceleration_group)


@web_app_acceleration_group.command(name=cli_util.override('waa.change_web_app_acceleration_compartment.command_name', 'change-compartment'), help=u"""Moves a Web App Acceleration resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeWebAppAccelerationCompartment)""")
@cli_util.option('--web-app-acceleration-id', required=True, help=u"""The [OCID] of the WebAppAcceleration.""")
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
def change_web_app_acceleration_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, web_app_acceleration_id, compartment_id, if_match):

    if isinstance(web_app_acceleration_id, six.string_types) and len(web_app_acceleration_id.strip()) == 0:
        raise click.UsageError('Parameter --web-app-acceleration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('waa', 'waa', ctx)
    result = client.change_web_app_acceleration_compartment(
        web_app_acceleration_id=web_app_acceleration_id,
        change_web_app_acceleration_compartment_details=_details,
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


@web_app_acceleration_policy_group.command(name=cli_util.override('waa.change_web_app_acceleration_policy_compartment.command_name', 'change-compartment'), help=u"""Moves a WebAppAccelerationfPolicy resource from one compartment to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeWebAppAccelerationPolicyCompartment)""")
@cli_util.option('--web-app-acceleration-policy-id', required=True, help=u"""The [OCID] of the WebAppAccelerationPolicy.""")
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
def change_web_app_acceleration_policy_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, web_app_acceleration_policy_id, compartment_id, if_match):

    if isinstance(web_app_acceleration_policy_id, six.string_types) and len(web_app_acceleration_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --web-app-acceleration-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('waa', 'waa', ctx)
    result = client.change_web_app_acceleration_policy_compartment(
        web_app_acceleration_policy_id=web_app_acceleration_policy_id,
        change_web_app_acceleration_policy_compartment_details=_details,
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


@web_app_acceleration_group.command(name=cli_util.override('waa.create_web_app_acceleration.command_name', 'create'), help=u"""Creates a new WebAppAcceleration. \n[Command Reference](createWebAppAcceleration)""")
@cli_util.option('--backend-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["LOAD_BALANCER"]), help=u"""Type of the WebAppFirewall, as example LOAD_BALANCER.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--web-app-acceleration-policy-id', required=True, help=u"""The [OCID] of WebAppAccelerationPolicy, which is attached to the resource.""")
@cli_util.option('--display-name', help=u"""WebAppAcceleration display name, can be renamed.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'waa', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'waa', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'waa', 'class': 'WebAppAcceleration'})
@cli_util.wrap_exceptions
def create_web_app_acceleration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, backend_type, compartment_id, web_app_acceleration_policy_id, display_name, freeform_tags, defined_tags, system_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['backendType'] = backend_type
    _details['compartmentId'] = compartment_id
    _details['webAppAccelerationPolicyId'] = web_app_acceleration_policy_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('waa', 'waa', ctx)
    result = client.create_web_app_acceleration(
        create_web_app_acceleration_details=_details,
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


@web_app_acceleration_group.command(name=cli_util.override('waa.create_web_app_acceleration_create_web_app_acceleration_load_balancer_details.command_name', 'create-web-app-acceleration-create-web-app-acceleration-load-balancer-details'), help=u"""Creates a new WebAppAcceleration. \n[Command Reference](createWebAppAcceleration)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--web-app-acceleration-policy-id', required=True, help=u"""The [OCID] of WebAppAccelerationPolicy, which is attached to the resource.""")
@cli_util.option('--load-balancer-id', required=True, help=u"""LoadBalancer [OCID] to which the WebAppAccelerationPolicy is attached to.""")
@cli_util.option('--display-name', help=u"""WebAppAcceleration display name, can be renamed.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'waa', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'waa', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'waa', 'class': 'WebAppAcceleration'})
@cli_util.wrap_exceptions
def create_web_app_acceleration_create_web_app_acceleration_load_balancer_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, web_app_acceleration_policy_id, load_balancer_id, display_name, freeform_tags, defined_tags, system_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['webAppAccelerationPolicyId'] = web_app_acceleration_policy_id
    _details['loadBalancerId'] = load_balancer_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    _details['backendType'] = 'LOAD_BALANCER'

    client = cli_util.build_client('waa', 'waa', ctx)
    result = client.create_web_app_acceleration(
        create_web_app_acceleration_details=_details,
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


@web_app_acceleration_policy_group.command(name=cli_util.override('waa.create_web_app_acceleration_policy.command_name', 'create'), help=u"""Creates a new WebAppAccelerationPolicy. \n[Command Reference](createWebAppAccelerationPolicy)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment.""")
@cli_util.option('--display-name', help=u"""WebAppAccelerationPolicy display name, can be renamed.""")
@cli_util.option('--response-caching-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--response-compression-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'response-caching-policy': {'module': 'waa', 'class': 'ResponseCachingPolicy'}, 'response-compression-policy': {'module': 'waa', 'class': 'ResponseCompressionPolicy'}, 'freeform-tags': {'module': 'waa', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'response-caching-policy': {'module': 'waa', 'class': 'ResponseCachingPolicy'}, 'response-compression-policy': {'module': 'waa', 'class': 'ResponseCompressionPolicy'}, 'freeform-tags': {'module': 'waa', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'waa', 'class': 'WebAppAccelerationPolicy'})
@cli_util.wrap_exceptions
def create_web_app_acceleration_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, response_caching_policy, response_compression_policy, freeform_tags, defined_tags, system_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if response_caching_policy is not None:
        _details['responseCachingPolicy'] = cli_util.parse_json_parameter("response_caching_policy", response_caching_policy)

    if response_compression_policy is not None:
        _details['responseCompressionPolicy'] = cli_util.parse_json_parameter("response_compression_policy", response_compression_policy)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('waa', 'waa', ctx)
    result = client.create_web_app_acceleration_policy(
        create_web_app_acceleration_policy_details=_details,
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


@web_app_acceleration_group.command(name=cli_util.override('waa.delete_web_app_acceleration.command_name', 'delete'), help=u"""Deletes a WebAppAcceleration resource identified by the OCID. \n[Command Reference](deleteWebAppAcceleration)""")
@cli_util.option('--web-app-acceleration-id', required=True, help=u"""The [OCID] of the WebAppAcceleration.""")
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
def delete_web_app_acceleration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, web_app_acceleration_id, if_match):

    if isinstance(web_app_acceleration_id, six.string_types) and len(web_app_acceleration_id.strip()) == 0:
        raise click.UsageError('Parameter --web-app-acceleration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waa', 'waa', ctx)
    result = client.delete_web_app_acceleration(
        web_app_acceleration_id=web_app_acceleration_id,
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


@web_app_acceleration_policy_group.command(name=cli_util.override('waa.delete_web_app_acceleration_policy.command_name', 'delete'), help=u"""Deletes a WebAppAccelerationPolicy resource identified by the OCID. \n[Command Reference](deleteWebAppAccelerationPolicy)""")
@cli_util.option('--web-app-acceleration-policy-id', required=True, help=u"""The [OCID] of the WebAppAccelerationPolicy.""")
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
def delete_web_app_acceleration_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, web_app_acceleration_policy_id, if_match):

    if isinstance(web_app_acceleration_policy_id, six.string_types) and len(web_app_acceleration_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --web-app-acceleration-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waa', 'waa', ctx)
    result = client.delete_web_app_acceleration_policy(
        web_app_acceleration_policy_id=web_app_acceleration_policy_id,
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


@web_app_acceleration_group.command(name=cli_util.override('waa.get_web_app_acceleration.command_name', 'get'), help=u"""Gets a WebAppAcceleration by OCID. \n[Command Reference](getWebAppAcceleration)""")
@cli_util.option('--web-app-acceleration-id', required=True, help=u"""The [OCID] of the WebAppAcceleration.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waa', 'class': 'WebAppAcceleration'})
@cli_util.wrap_exceptions
def get_web_app_acceleration(ctx, from_json, web_app_acceleration_id):

    if isinstance(web_app_acceleration_id, six.string_types) and len(web_app_acceleration_id.strip()) == 0:
        raise click.UsageError('Parameter --web-app-acceleration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waa', 'waa', ctx)
    result = client.get_web_app_acceleration(
        web_app_acceleration_id=web_app_acceleration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@web_app_acceleration_policy_group.command(name=cli_util.override('waa.get_web_app_acceleration_policy.command_name', 'get'), help=u"""Gets a WebAppAccelerationPolicy with the given OCID. \n[Command Reference](getWebAppAccelerationPolicy)""")
@cli_util.option('--web-app-acceleration-policy-id', required=True, help=u"""The [OCID] of the WebAppAccelerationPolicy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waa', 'class': 'WebAppAccelerationPolicy'})
@cli_util.wrap_exceptions
def get_web_app_acceleration_policy(ctx, from_json, web_app_acceleration_policy_id):

    if isinstance(web_app_acceleration_policy_id, six.string_types) and len(web_app_acceleration_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --web-app-acceleration-policy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waa', 'waa', ctx)
    result = client.get_web_app_acceleration_policy(
        web_app_acceleration_policy_id=web_app_acceleration_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@web_app_acceleration_policy_group.command(name=cli_util.override('waa.list_web_app_acceleration_policies.command_name', 'list'), help=u"""Gets a list of all WebAppAccelerationPolicies in a compartment. \n[Command Reference](listWebAppAccelerationPolicies)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to list resources.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help=u"""A filter to return only resources that match the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""A filter to return only the WebAppAccelerationPolicy with the given [OCID].""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waa', 'class': 'WebAppAccelerationPolicyCollection'})
@cli_util.wrap_exceptions
def list_web_app_acceleration_policies(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None and len(lifecycle_state) > 0:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waa', 'waa', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_web_app_acceleration_policies,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_web_app_acceleration_policies,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_web_app_acceleration_policies(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@web_app_acceleration_group.command(name=cli_util.override('waa.list_web_app_accelerations.command_name', 'list'), help=u"""Gets a list of all WebAppAccelerations in a compartment. \n[Command Reference](listWebAppAccelerations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to list resources.""")
@cli_util.option('--id', help=u"""A filter to return only the WebAppAcceleration with the given [OCID].""")
@cli_util.option('--web-app-acceleration-policy-id', help=u"""A filter to return only the WebAppAcceleration with the given [OCID] of related WebAppAccelerationPolicy.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help=u"""A filter to return only resources that match the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waa', 'class': 'WebAppAccelerationCollection'})
@cli_util.wrap_exceptions
def list_web_app_accelerations(ctx, from_json, all_pages, page_size, compartment_id, id, web_app_acceleration_policy_id, lifecycle_state, display_name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if web_app_acceleration_policy_id is not None:
        kwargs['web_app_acceleration_policy_id'] = web_app_acceleration_policy_id
    if lifecycle_state is not None and len(lifecycle_state) > 0:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waa', 'waa', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_web_app_accelerations,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_web_app_accelerations,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_web_app_accelerations(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@web_app_acceleration_group.command(name=cli_util.override('waa.purge_web_app_acceleration_cache.command_name', 'purge-web-app-acceleration-cache'), help=u"""Clears resources from the cache of the WebAppAcceleration. Each new request for a purged resource will be forwarded to the origin server to fetch a new version of the resource. \n[Command Reference](purgeWebAppAccelerationCache)""")
@cli_util.option('--web-app-acceleration-id', required=True, help=u"""The [OCID] of the WebAppAcceleration.""")
@cli_util.option('--purge-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["ENTIRE_CACHE"]), help=u"""Type of cache purge to perform.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def purge_web_app_acceleration_cache(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, web_app_acceleration_id, purge_type):

    if isinstance(web_app_acceleration_id, six.string_types) and len(web_app_acceleration_id.strip()) == 0:
        raise click.UsageError('Parameter --web-app-acceleration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['purgeType'] = purge_type

    client = cli_util.build_client('waa', 'waa', ctx)
    result = client.purge_web_app_acceleration_cache(
        web_app_acceleration_id=web_app_acceleration_id,
        purge_web_app_acceleration_cache_details=_details,
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


@web_app_acceleration_group.command(name=cli_util.override('waa.purge_web_app_acceleration_cache_purge_entire_web_app_acceleration_cache_details.command_name', 'purge-web-app-acceleration-cache-purge-entire-web-app-acceleration-cache-details'), help=u"""Clears resources from the cache of the WebAppAcceleration. Each new request for a purged resource will be forwarded to the origin server to fetch a new version of the resource. \n[Command Reference](purgeWebAppAccelerationCache)""")
@cli_util.option('--web-app-acceleration-id', required=True, help=u"""The [OCID] of the WebAppAcceleration.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def purge_web_app_acceleration_cache_purge_entire_web_app_acceleration_cache_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, web_app_acceleration_id):

    if isinstance(web_app_acceleration_id, six.string_types) and len(web_app_acceleration_id.strip()) == 0:
        raise click.UsageError('Parameter --web-app-acceleration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    _details['purgeType'] = 'ENTIRE_CACHE'

    client = cli_util.build_client('waa', 'waa', ctx)
    result = client.purge_web_app_acceleration_cache(
        web_app_acceleration_id=web_app_acceleration_id,
        purge_web_app_acceleration_cache_details=_details,
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


@web_app_acceleration_group.command(name=cli_util.override('waa.update_web_app_acceleration.command_name', 'update'), help=u"""Updates the WebAppAcceleration identified by the OCID. \n[Command Reference](updateWebAppAcceleration)""")
@cli_util.option('--web-app-acceleration-id', required=True, help=u"""The [OCID] of the WebAppAcceleration.""")
@cli_util.option('--display-name', help=u"""WebAppAcceleration display name, can be renamed.""")
@cli_util.option('--web-app-acceleration-policy-id', help=u"""The [OCID] of WebAppAccelerationPolicy, which is attached to the resource. This update guarantees that the resource always has WebAppAccelerationPolicy attached at any time.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'waa', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'waa', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_web_app_acceleration(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, web_app_acceleration_id, display_name, web_app_acceleration_policy_id, freeform_tags, defined_tags, system_tags, if_match):

    if isinstance(web_app_acceleration_id, six.string_types) and len(web_app_acceleration_id.strip()) == 0:
        raise click.UsageError('Parameter --web-app-acceleration-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or system_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and system-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if web_app_acceleration_policy_id is not None:
        _details['webAppAccelerationPolicyId'] = web_app_acceleration_policy_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('waa', 'waa', ctx)
    result = client.update_web_app_acceleration(
        web_app_acceleration_id=web_app_acceleration_id,
        update_web_app_acceleration_details=_details,
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


@web_app_acceleration_policy_group.command(name=cli_util.override('waa.update_web_app_acceleration_policy.command_name', 'update'), help=u"""Update the WebAppAccelerationPolicy identified by the OCID. \n[Command Reference](updateWebAppAccelerationPolicy)""")
@cli_util.option('--web-app-acceleration-policy-id', required=True, help=u"""The [OCID] of the WebAppAccelerationPolicy.""")
@cli_util.option('--display-name', help=u"""WebAppAccelerationPolicy display name, can be renamed.""")
@cli_util.option('--response-caching-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--response-compression-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--system-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of system tag keys. These predefined keys are scoped to namespaces. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'response-caching-policy': {'module': 'waa', 'class': 'ResponseCachingPolicy'}, 'response-compression-policy': {'module': 'waa', 'class': 'ResponseCompressionPolicy'}, 'freeform-tags': {'module': 'waa', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'response-caching-policy': {'module': 'waa', 'class': 'ResponseCachingPolicy'}, 'response-compression-policy': {'module': 'waa', 'class': 'ResponseCompressionPolicy'}, 'freeform-tags': {'module': 'waa', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}, 'system-tags': {'module': 'waa', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_web_app_acceleration_policy(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, web_app_acceleration_policy_id, display_name, response_caching_policy, response_compression_policy, freeform_tags, defined_tags, system_tags, if_match):

    if isinstance(web_app_acceleration_policy_id, six.string_types) and len(web_app_acceleration_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --web-app-acceleration-policy-id cannot be whitespace or empty string')
    if not force:
        if response_caching_policy or response_compression_policy or freeform_tags or defined_tags or system_tags:
            if not click.confirm("WARNING: Updates to response-caching-policy and response-compression-policy and freeform-tags and defined-tags and system-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if response_caching_policy is not None:
        _details['responseCachingPolicy'] = cli_util.parse_json_parameter("response_caching_policy", response_caching_policy)

    if response_compression_policy is not None:
        _details['responseCompressionPolicy'] = cli_util.parse_json_parameter("response_compression_policy", response_compression_policy)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if system_tags is not None:
        _details['systemTags'] = cli_util.parse_json_parameter("system_tags", system_tags)

    client = cli_util.build_client('waa', 'waa', ctx)
    result = client.update_web_app_acceleration_policy(
        web_app_acceleration_policy_id=web_app_acceleration_policy_id,
        update_web_app_acceleration_policy_details=_details,
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
