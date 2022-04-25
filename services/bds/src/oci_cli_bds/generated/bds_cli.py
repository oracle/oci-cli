# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('bds.bds_root_group.command_name', 'bds'), cls=CommandGroupWithAlias, help=cli_util.override('bds.bds_root_group.help', """REST API for Oracle Big Data Service. Use this API to build, deploy, and manage fully elastic Big Data Service clusters. Build on Hadoop, Spark and Data Science distributions, which can be fully integrated with existing enterprise data in Oracle Database and Oracle applications."""), short_help=cli_util.override('bds.bds_root_group.short_help', """Big Data Service API"""))
@cli_util.help_option_group
def bds_root_group():
    pass


@click.command(cli_util.override('bds.bds_instance_group.command_name', 'bds-instance'), cls=CommandGroupWithAlias, help="""Description of the cluster.""")
@cli_util.help_option_group
def bds_instance_group():
    pass


@click.command(cli_util.override('bds.bds_api_key_group.command_name', 'bds-api-key'), cls=CommandGroupWithAlias, help="""The API key information.""")
@cli_util.help_option_group
def bds_api_key_group():
    pass


@click.command(cli_util.override('bds.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('bds.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('bds.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""Description of the work request status.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('bds.bds_metastore_configuration_group.command_name', 'bds-metastore-configuration'), cls=CommandGroupWithAlias, help="""The metastore configuration information.""")
@cli_util.help_option_group
def bds_metastore_configuration_group():
    pass


bds_root_group.add_command(bds_instance_group)
bds_root_group.add_command(bds_api_key_group)
bds_root_group.add_command(work_request_error_group)
bds_root_group.add_command(work_request_log_entry_group)
bds_root_group.add_command(work_request_group)
bds_root_group.add_command(bds_metastore_configuration_group)


@bds_metastore_configuration_group.command(name=cli_util.override('bds.activate_bds_metastore_configuration.command_name', 'activate'), help=u"""Activate specified metastore configuration. \n[Command Reference](activateBdsMetastoreConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--metastore-config-id', required=True, help=u"""The metastore configuration ID""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster admin user.""")
@cli_util.option('--bds-api-key-passphrase', help=u"""Base-64 encoded passphrase of the BDS Api Key. Set only if metastore's type is EXTERNAL.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def activate_bds_metastore_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, metastore_config_id, cluster_admin_password, bds_api_key_passphrase, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(metastore_config_id, six.string_types) and len(metastore_config_id.strip()) == 0:
        raise click.UsageError('Parameter --metastore-config-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['clusterAdminPassword'] = cluster_admin_password

    if bds_api_key_passphrase is not None:
        _details['bdsApiKeyPassphrase'] = bds_api_key_passphrase

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.activate_bds_metastore_configuration(
        bds_instance_id=bds_instance_id,
        metastore_config_id=metastore_config_id,
        activate_bds_metastore_configuration_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.add_auto_scaling_configuration.command_name', 'add'), help=u"""Add an autoscale configuration to the cluster. \n[Command Reference](addAutoScalingConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--node-type', required=True, help=u"""A node type that is managed by an autoscale configuration. The only supported types are WORKER and COMPUTE_ONLY_WORKER.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Whether the autoscale configuration is enabled.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.""")
@cli_util.option('--policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--policy-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details': {'module': 'bds', 'class': 'AddAutoScalePolicyDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details': {'module': 'bds', 'class': 'AddAutoScalePolicyDetails'}})
@cli_util.wrap_exceptions
def add_auto_scaling_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, node_type, is_enabled, cluster_admin_password, display_name, policy, policy_details, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['nodeType'] = node_type
    _details['isEnabled'] = is_enabled
    _details['clusterAdminPassword'] = cluster_admin_password

    if display_name is not None:
        _details['displayName'] = display_name

    if policy is not None:
        _details['policy'] = cli_util.parse_json_parameter("policy", policy)

    if policy_details is not None:
        _details['policyDetails'] = cli_util.parse_json_parameter("policy_details", policy_details)

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.add_auto_scaling_configuration(
        bds_instance_id=bds_instance_id,
        add_auto_scaling_configuration_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.add_auto_scaling_configuration_add_metric_based_horizontal_scaling_policy_details.command_name', 'add-auto-scaling-configuration-add-metric-based-horizontal-scaling-policy-details'), help=u"""Add an autoscale configuration to the cluster. \n[Command Reference](addAutoScalingConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--node-type', required=True, help=u"""A node type that is managed by an autoscale configuration. The only supported types are WORKER and COMPUTE_ONLY_WORKER.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Whether the autoscale configuration is enabled.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.""")
@cli_util.option('--policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--policy-details-scale-out-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--policy-details-scale-in-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-scale-out-config': {'module': 'bds', 'class': 'MetricBasedHorizontalScaleOutConfig'}, 'policy-details-scale-in-config': {'module': 'bds', 'class': 'MetricBasedHorizontalScaleInConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-scale-out-config': {'module': 'bds', 'class': 'MetricBasedHorizontalScaleOutConfig'}, 'policy-details-scale-in-config': {'module': 'bds', 'class': 'MetricBasedHorizontalScaleInConfig'}})
@cli_util.wrap_exceptions
def add_auto_scaling_configuration_add_metric_based_horizontal_scaling_policy_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, node_type, is_enabled, cluster_admin_password, display_name, policy, if_match, policy_details_scale_out_config, policy_details_scale_in_config):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['policyDetails'] = {}
    _details['nodeType'] = node_type
    _details['isEnabled'] = is_enabled
    _details['clusterAdminPassword'] = cluster_admin_password

    if display_name is not None:
        _details['displayName'] = display_name

    if policy is not None:
        _details['policy'] = cli_util.parse_json_parameter("policy", policy)

    if policy_details_scale_out_config is not None:
        _details['policyDetails']['scaleOutConfig'] = cli_util.parse_json_parameter("policy_details_scale_out_config", policy_details_scale_out_config)

    if policy_details_scale_in_config is not None:
        _details['policyDetails']['scaleInConfig'] = cli_util.parse_json_parameter("policy_details_scale_in_config", policy_details_scale_in_config)

    _details['policyDetails']['policyType'] = 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.add_auto_scaling_configuration(
        bds_instance_id=bds_instance_id,
        add_auto_scaling_configuration_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.add_auto_scaling_configuration_add_schedule_based_vertical_scaling_policy_details.command_name', 'add-auto-scaling-configuration-add-schedule-based-vertical-scaling-policy-details'), help=u"""Add an autoscale configuration to the cluster. \n[Command Reference](addAutoScalingConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--node-type', required=True, help=u"""A node type that is managed by an autoscale configuration. The only supported types are WORKER and COMPUTE_ONLY_WORKER.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Whether the autoscale configuration is enabled.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.""")
@cli_util.option('--policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--policy-details-timezone', help=u"""The time zone of the execution schedule, in IANA time zone database name format""")
@cli_util.option('--policy-details-schedule-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type VerticalScalingScheduleDetails.  For documentation on VerticalScalingScheduleDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/bds/20190531/datatypes/VerticalScalingScheduleDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-schedule-details': {'module': 'bds', 'class': 'list[VerticalScalingScheduleDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-schedule-details': {'module': 'bds', 'class': 'list[VerticalScalingScheduleDetails]'}})
@cli_util.wrap_exceptions
def add_auto_scaling_configuration_add_schedule_based_vertical_scaling_policy_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, node_type, is_enabled, cluster_admin_password, display_name, policy, if_match, policy_details_timezone, policy_details_schedule_details):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['policyDetails'] = {}
    _details['nodeType'] = node_type
    _details['isEnabled'] = is_enabled
    _details['clusterAdminPassword'] = cluster_admin_password

    if display_name is not None:
        _details['displayName'] = display_name

    if policy is not None:
        _details['policy'] = cli_util.parse_json_parameter("policy", policy)

    if policy_details_timezone is not None:
        _details['policyDetails']['timezone'] = policy_details_timezone

    if policy_details_schedule_details is not None:
        _details['policyDetails']['scheduleDetails'] = cli_util.parse_json_parameter("policy_details_schedule_details", policy_details_schedule_details)

    _details['policyDetails']['policyType'] = 'SCHEDULE_BASED_VERTICAL_SCALING_POLICY'

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.add_auto_scaling_configuration(
        bds_instance_id=bds_instance_id,
        add_auto_scaling_configuration_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.add_auto_scaling_configuration_add_schedule_based_horizontal_scaling_policy_details.command_name', 'add-auto-scaling-configuration-add-schedule-based-horizontal-scaling-policy-details'), help=u"""Add an autoscale configuration to the cluster. \n[Command Reference](addAutoScalingConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--node-type', required=True, help=u"""A node type that is managed by an autoscale configuration. The only supported types are WORKER and COMPUTE_ONLY_WORKER.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Whether the autoscale configuration is enabled.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.""")
@cli_util.option('--policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--policy-details-timezone', help=u"""The time zone of the execution schedule, in IANA time zone database name format""")
@cli_util.option('--policy-details-schedule-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type HorizontalScalingScheduleDetails.  For documentation on HorizontalScalingScheduleDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/bds/20190531/datatypes/HorizontalScalingScheduleDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-schedule-details': {'module': 'bds', 'class': 'list[HorizontalScalingScheduleDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-schedule-details': {'module': 'bds', 'class': 'list[HorizontalScalingScheduleDetails]'}})
@cli_util.wrap_exceptions
def add_auto_scaling_configuration_add_schedule_based_horizontal_scaling_policy_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, node_type, is_enabled, cluster_admin_password, display_name, policy, if_match, policy_details_timezone, policy_details_schedule_details):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['policyDetails'] = {}
    _details['nodeType'] = node_type
    _details['isEnabled'] = is_enabled
    _details['clusterAdminPassword'] = cluster_admin_password

    if display_name is not None:
        _details['displayName'] = display_name

    if policy is not None:
        _details['policy'] = cli_util.parse_json_parameter("policy", policy)

    if policy_details_timezone is not None:
        _details['policyDetails']['timezone'] = policy_details_timezone

    if policy_details_schedule_details is not None:
        _details['policyDetails']['scheduleDetails'] = cli_util.parse_json_parameter("policy_details_schedule_details", policy_details_schedule_details)

    _details['policyDetails']['policyType'] = 'SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY'

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.add_auto_scaling_configuration(
        bds_instance_id=bds_instance_id,
        add_auto_scaling_configuration_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.add_auto_scaling_configuration_add_metric_based_vertical_scaling_policy_details.command_name', 'add-auto-scaling-configuration-add-metric-based-vertical-scaling-policy-details'), help=u"""Add an autoscale configuration to the cluster. \n[Command Reference](addAutoScalingConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--node-type', required=True, help=u"""A node type that is managed by an autoscale configuration. The only supported types are WORKER and COMPUTE_ONLY_WORKER.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Whether the autoscale configuration is enabled.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.""")
@cli_util.option('--policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--policy-details-scale-up-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--policy-details-scale-down-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-scale-up-config': {'module': 'bds', 'class': 'MetricBasedVerticalScaleUpConfig'}, 'policy-details-scale-down-config': {'module': 'bds', 'class': 'MetricBasedVerticalScaleDownConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-scale-up-config': {'module': 'bds', 'class': 'MetricBasedVerticalScaleUpConfig'}, 'policy-details-scale-down-config': {'module': 'bds', 'class': 'MetricBasedVerticalScaleDownConfig'}})
@cli_util.wrap_exceptions
def add_auto_scaling_configuration_add_metric_based_vertical_scaling_policy_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, node_type, is_enabled, cluster_admin_password, display_name, policy, if_match, policy_details_scale_up_config, policy_details_scale_down_config):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['policyDetails'] = {}
    _details['nodeType'] = node_type
    _details['isEnabled'] = is_enabled
    _details['clusterAdminPassword'] = cluster_admin_password

    if display_name is not None:
        _details['displayName'] = display_name

    if policy is not None:
        _details['policy'] = cli_util.parse_json_parameter("policy", policy)

    if policy_details_scale_up_config is not None:
        _details['policyDetails']['scaleUpConfig'] = cli_util.parse_json_parameter("policy_details_scale_up_config", policy_details_scale_up_config)

    if policy_details_scale_down_config is not None:
        _details['policyDetails']['scaleDownConfig'] = cli_util.parse_json_parameter("policy_details_scale_down_config", policy_details_scale_down_config)

    _details['policyDetails']['policyType'] = 'METRIC_BASED_VERTICAL_SCALING_POLICY'

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.add_auto_scaling_configuration(
        bds_instance_id=bds_instance_id,
        add_auto_scaling_configuration_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.add_block_storage.command_name', 'add'), help=u"""Adds block storage to existing worker/compute only worker nodes. The same amount of  storage will be added to all worker/compute only worker nodes. No change will be made to storage that is already attached. Block storage cannot be removed. \n[Command Reference](addBlockStorage)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--block-volume-size-in-gbs', required=True, type=click.INT, help=u"""The size of block volume in GB to be added to each worker node. All the details needed for attaching the block volume are managed by service itself.""")
@cli_util.option('--node-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["WORKER", "COMPUTE_ONLY_WORKER"]), help=u"""Worker node types, can either be Worker Data node or Compute only worker node.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def add_block_storage(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, cluster_admin_password, block_volume_size_in_gbs, node_type, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['clusterAdminPassword'] = cluster_admin_password
    _details['blockVolumeSizeInGBs'] = block_volume_size_in_gbs
    _details['nodeType'] = node_type

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.add_block_storage(
        bds_instance_id=bds_instance_id,
        add_block_storage_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.add_cloud_sql.command_name', 'add'), help=u"""Adds Cloud SQL to your cluster. You can use Cloud SQL to query against non-relational data stored in multiple big data sources, including Apache Hive, HDFS, Oracle NoSQL Database, and Apache HBase. Adding Cloud SQL adds a query server node to the cluster and creates cell servers on all the worker nodes in the cluster. \n[Command Reference](addCloudSql)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--shape', required=True, help=u"""Shape of the node.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--block-volume-size-in-gbs', type=click.INT, help=u"""The size of block volume in GB to be attached to the given node. All details needed for attaching the block volume are managed by the service itself.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def add_cloud_sql(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, shape, cluster_admin_password, block_volume_size_in_gbs, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['shape'] = shape
    _details['clusterAdminPassword'] = cluster_admin_password

    if block_volume_size_in_gbs is not None:
        _details['blockVolumeSizeInGBs'] = block_volume_size_in_gbs

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.add_cloud_sql(
        bds_instance_id=bds_instance_id,
        add_cloud_sql_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.add_worker_nodes.command_name', 'add'), help=u"""Increases the size (scales out) a cluster by adding worker nodes(data/compute). The added worker nodes will have the same shape and will have the same amount of attached block storage as other worker nodes in the cluster. \n[Command Reference](addWorkerNodes)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--number-of-worker-nodes', required=True, type=click.INT, help=u"""Number of additional worker nodes for the cluster.""")
@cli_util.option('--node-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["WORKER", "COMPUTE_ONLY_WORKER"]), help=u"""Worker node types, can either be Worker Data node or Compute only worker node.""")
@cli_util.option('--shape', help=u"""Shape of the node. This has to be specified when adding compute only worker node at the first time. Otherwise, it's a read-only property.""")
@cli_util.option('--block-volume-size-in-gbs', type=click.INT, help=u"""The size of block volume in GB to be attached to the given node. This has to be specified when adding compute only worker node at the first time. Otherwise, it's a read-only property.""")
@cli_util.option('--shape-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'shape-config': {'module': 'bds', 'class': 'ShapeConfigDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'shape-config': {'module': 'bds', 'class': 'ShapeConfigDetails'}})
@cli_util.wrap_exceptions
def add_worker_nodes(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, cluster_admin_password, number_of_worker_nodes, node_type, shape, block_volume_size_in_gbs, shape_config, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['clusterAdminPassword'] = cluster_admin_password
    _details['numberOfWorkerNodes'] = number_of_worker_nodes
    _details['nodeType'] = node_type

    if shape is not None:
        _details['shape'] = shape

    if block_volume_size_in_gbs is not None:
        _details['blockVolumeSizeInGBs'] = block_volume_size_in_gbs

    if shape_config is not None:
        _details['shapeConfig'] = cli_util.parse_json_parameter("shape_config", shape_config)

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.add_worker_nodes(
        bds_instance_id=bds_instance_id,
        add_worker_nodes_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.change_bds_instance_compartment.command_name', 'change-compartment'), help=u"""Moves a Big Data Service cluster into a different compartment. \n[Command Reference](changeBdsInstanceCompartment)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_bds_instance_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, compartment_id, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.change_bds_instance_compartment(
        bds_instance_id=bds_instance_id,
        change_bds_instance_compartment_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.change_shape.command_name', 'change-shape'), help=u"""Changes the size of a cluster by scaling up or scaling down the nodes. Nodes are scaled up or down by changing the shapes of all the nodes of the same type to the next larger or smaller shape. The node types are master, utility, worker, and Cloud SQL. Only nodes with VM-STANDARD shapes can be scaled. \n[Command Reference](changeShape)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--nodes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nodes': {'module': 'bds', 'class': 'ChangeShapeNodes'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nodes': {'module': 'bds', 'class': 'ChangeShapeNodes'}})
@cli_util.wrap_exceptions
def change_shape(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, cluster_admin_password, nodes, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['clusterAdminPassword'] = cluster_admin_password
    _details['nodes'] = cli_util.parse_json_parameter("nodes", nodes)

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.change_shape(
        bds_instance_id=bds_instance_id,
        change_shape_details=_details,
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


@bds_api_key_group.command(name=cli_util.override('bds.create_bds_api_key.command_name', 'create'), help=u"""Create an API key on behalf of the specified user. \n[Command Reference](createBdsApiKey)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user for whom this new generated API key pair will be created.""")
@cli_util.option('--passphrase', required=True, help=u"""Base64 passphrase used to secure the private key which will be created on user behalf.""")
@cli_util.option('--key-alias', required=True, help=u"""User friendly identifier used to uniquely differentiate between different API keys associated with this Big Data Service cluster. Only ASCII alphanumeric characters with no spaces allowed.""")
@cli_util.option('--default-region', help=u"""The name of the region to establish the Object Storage endpoint. See https://docs.oracle.com/en-us/iaas/api/#/en/identity/20160918/Region/ for additional information.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_bds_api_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, user_id, passphrase, key_alias, default_region):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['userId'] = user_id
    _details['passphrase'] = passphrase
    _details['keyAlias'] = key_alias

    if default_region is not None:
        _details['defaultRegion'] = default_region

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.create_bds_api_key(
        bds_instance_id=bds_instance_id,
        create_bds_api_key_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.create_bds_instance.command_name', 'create'), help=u"""Creates a Big Data Service cluster. \n[Command Reference](createBdsInstance)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--display-name', required=True, help=u"""Name of the Big Data Service cluster.""")
@cli_util.option('--cluster-version', required=True, help=u"""Version of the Hadoop distribution.""")
@cli_util.option('--cluster-public-key', required=True, help=u"""The SSH public key used to authenticate the cluster connection.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--is-high-availability', required=True, type=click.BOOL, help=u"""Boolean flag specifying whether or not the cluster is highly available (HA).""")
@cli_util.option('--is-secure', required=True, type=click.BOOL, help=u"""Boolean flag specifying whether or not the cluster should be set up as secure.""")
@cli_util.option('--nodes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of nodes in the Big Data Service cluster.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--bootstrap-script-url', help=u"""Pre-authenticated URL of the script in Object Store that is downloaded and executed.""")
@cli_util.option('--kerberos-realm-name', help=u"""The user-defined kerberos realm name.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. For example, `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For example, `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-config': {'module': 'bds', 'class': 'NetworkConfig'}, 'nodes': {'module': 'bds', 'class': 'list[CreateNodeDetails]'}, 'freeform-tags': {'module': 'bds', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'bds', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-config': {'module': 'bds', 'class': 'NetworkConfig'}, 'nodes': {'module': 'bds', 'class': 'list[CreateNodeDetails]'}, 'freeform-tags': {'module': 'bds', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'bds', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_bds_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, cluster_version, cluster_public_key, cluster_admin_password, is_high_availability, is_secure, nodes, network_config, bootstrap_script_url, kerberos_realm_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['clusterVersion'] = cluster_version
    _details['clusterPublicKey'] = cluster_public_key
    _details['clusterAdminPassword'] = cluster_admin_password
    _details['isHighAvailability'] = is_high_availability
    _details['isSecure'] = is_secure
    _details['nodes'] = cli_util.parse_json_parameter("nodes", nodes)

    if network_config is not None:
        _details['networkConfig'] = cli_util.parse_json_parameter("network_config", network_config)

    if bootstrap_script_url is not None:
        _details['bootstrapScriptUrl'] = bootstrap_script_url

    if kerberos_realm_name is not None:
        _details['kerberosRealmName'] = kerberos_realm_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.create_bds_instance(
        create_bds_instance_details=_details,
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


@bds_metastore_configuration_group.command(name=cli_util.override('bds.create_bds_metastore_configuration.command_name', 'create'), help=u"""Create and activate external metastore configuration. \n[Command Reference](createBdsMetastoreConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--metastore-id', required=True, help=u"""The OCID of the Data Catalog metastore.""")
@cli_util.option('--bds-api-key-id', required=True, help=u"""The ID of BDS Api Key used for Data Catalog metastore integration.""")
@cli_util.option('--bds-api-key-passphrase', required=True, help=u"""Base-64 encoded passphrase of the BDS Api Key.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster admin user.""")
@cli_util.option('--display-name', help=u"""The display name of the metastore configuration""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_bds_metastore_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, metastore_id, bds_api_key_id, bds_api_key_passphrase, cluster_admin_password, display_name):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['metastoreId'] = metastore_id
    _details['bdsApiKeyId'] = bds_api_key_id
    _details['bdsApiKeyPassphrase'] = bds_api_key_passphrase
    _details['clusterAdminPassword'] = cluster_admin_password

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.create_bds_metastore_configuration(
        bds_instance_id=bds_instance_id,
        create_bds_metastore_configuration_details=_details,
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


@bds_api_key_group.command(name=cli_util.override('bds.delete_bds_api_key.command_name', 'delete'), help=u"""Deletes the user's API key represented by the provided ID. \n[Command Reference](deleteBdsApiKey)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--api-key-id', required=True, help=u"""The API key identifier.""")
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
def delete_bds_api_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, api_key_id, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(api_key_id, six.string_types) and len(api_key_id.strip()) == 0:
        raise click.UsageError('Parameter --api-key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.delete_bds_api_key(
        bds_instance_id=bds_instance_id,
        api_key_id=api_key_id,
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


@bds_instance_group.command(name=cli_util.override('bds.delete_bds_instance.command_name', 'delete'), help=u"""Deletes the cluster identified by the given ID. \n[Command Reference](deleteBdsInstance)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
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
def delete_bds_instance(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.delete_bds_instance(
        bds_instance_id=bds_instance_id,
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


@bds_metastore_configuration_group.command(name=cli_util.override('bds.delete_bds_metastore_configuration.command_name', 'delete'), help=u"""Delete the BDS metastore configuration represented by the provided ID. \n[Command Reference](deleteBdsMetastoreConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--metastore-config-id', required=True, help=u"""The metastore configuration ID""")
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
def delete_bds_metastore_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, metastore_config_id, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(metastore_config_id, six.string_types) and len(metastore_config_id.strip()) == 0:
        raise click.UsageError('Parameter --metastore-config-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.delete_bds_metastore_configuration(
        bds_instance_id=bds_instance_id,
        metastore_config_id=metastore_config_id,
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


@bds_instance_group.command(name=cli_util.override('bds.get_auto_scaling_configuration.command_name', 'get-auto-scaling-configuration'), help=u"""Returns details of the autoscale configuration identified by the given ID. \n[Command Reference](getAutoScalingConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""Unique Oracle-assigned identifier of the autoscale configuration.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'AutoScalingConfiguration'})
@cli_util.wrap_exceptions
def get_auto_scaling_configuration(ctx, from_json, bds_instance_id, auto_scaling_configuration_id):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.get_auto_scaling_configuration(
        bds_instance_id=bds_instance_id,
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bds_api_key_group.command(name=cli_util.override('bds.get_bds_api_key.command_name', 'get'), help=u"""Returns the user's API key information for the given ID. \n[Command Reference](getBdsApiKey)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--api-key-id', required=True, help=u"""The API key identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'BdsApiKey'})
@cli_util.wrap_exceptions
def get_bds_api_key(ctx, from_json, bds_instance_id, api_key_id):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(api_key_id, six.string_types) and len(api_key_id.strip()) == 0:
        raise click.UsageError('Parameter --api-key-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.get_bds_api_key(
        bds_instance_id=bds_instance_id,
        api_key_id=api_key_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bds_instance_group.command(name=cli_util.override('bds.get_bds_instance.command_name', 'get'), help=u"""Returns information about the Big Data Service cluster identified by the given ID. \n[Command Reference](getBdsInstance)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'BdsInstance'})
@cli_util.wrap_exceptions
def get_bds_instance(ctx, from_json, bds_instance_id):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.get_bds_instance(
        bds_instance_id=bds_instance_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bds_metastore_configuration_group.command(name=cli_util.override('bds.get_bds_metastore_configuration.command_name', 'get'), help=u"""Returns the BDS Metastore configuration information for the given ID. \n[Command Reference](getBdsMetastoreConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--metastore-config-id', required=True, help=u"""The metastore configuration ID""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'BdsMetastoreConfiguration'})
@cli_util.wrap_exceptions
def get_bds_metastore_configuration(ctx, from_json, bds_instance_id, metastore_config_id):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(metastore_config_id, six.string_types) and len(metastore_config_id.strip()) == 0:
        raise click.UsageError('Parameter --metastore-config-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.get_bds_metastore_configuration(
        bds_instance_id=bds_instance_id,
        metastore_config_id=metastore_config_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('bds.get_work_request.command_name', 'get'), help=u"""Returns the status of the work request identified by the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bds_instance_group.command(name=cli_util.override('bds.install_patch.command_name', 'install-patch'), help=u"""Install the specified patch to this cluster. \n[Command Reference](installPatch)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--version-parameterconflict', required=True, help=u"""The version of the patch to be installed.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster admin user.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def install_patch(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, version_parameterconflict, cluster_admin_password, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['version'] = version_parameterconflict
    _details['clusterAdminPassword'] = cluster_admin_password

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.install_patch(
        bds_instance_id=bds_instance_id,
        install_patch_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.list_auto_scaling_configurations.command_name', 'list-auto-scaling-configurations'), help=u"""Returns information about the autoscaling configurations for a cluster. \n[Command Reference](listAutoScalingConfigurations)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""The state of the autoscale configuration.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'list[AutoScalingConfigurationSummary]'})
@cli_util.wrap_exceptions
def list_auto_scaling_configurations(ctx, from_json, all_pages, page_size, compartment_id, bds_instance_id, page, limit, sort_by, sort_order, display_name, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_auto_scaling_configurations,
            compartment_id=compartment_id,
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_auto_scaling_configurations,
            limit,
            page_size,
            compartment_id=compartment_id,
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    else:
        result = client.list_auto_scaling_configurations(
            compartment_id=compartment_id,
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@bds_api_key_group.command(name=cli_util.override('bds.list_bds_api_keys.command_name', 'list'), help=u"""Returns a list of all API keys associated with this Big Data Service cluster. \n[Command Reference](listBdsApiKeys)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""The state of the API key.""")
@cli_util.option('--user-id', help=u"""The OCID of the user for whom the API key belongs.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'list[BdsApiKeySummary]'})
@cli_util.wrap_exceptions
def list_bds_api_keys(ctx, from_json, all_pages, page_size, bds_instance_id, lifecycle_state, user_id, page, limit, sort_by, sort_order, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if user_id is not None:
        kwargs['user_id'] = user_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_bds_api_keys,
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_bds_api_keys,
            limit,
            page_size,
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    else:
        result = client.list_bds_api_keys(
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@bds_instance_group.command(name=cli_util.override('bds.list_bds_instances.command_name', 'list'), help=u"""Returns a list of all Big Data Service clusters in a compartment. \n[Command Reference](listBdsInstances)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "UPDATING", "SUSPENDING", "SUSPENDED", "RESUMING", "DELETING", "DELETED", "FAILED"]), help=u"""The state of the cluster.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'list[BdsInstanceSummary]'})
@cli_util.wrap_exceptions
def list_bds_instances(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, page, limit, sort_by, sort_order, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_bds_instances,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_bds_instances,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_bds_instances(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@bds_metastore_configuration_group.command(name=cli_util.override('bds.list_bds_metastore_configurations.command_name', 'list'), help=u"""Returns a list of metastore configurations ssociated with this Big Data Service cluster. \n[Command Reference](listBdsMetastoreConfigurations)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--metastore-type', type=custom_types.CliCaseInsensitiveChoice(["LOCAL", "EXTERNAL"]), help=u"""The type of the metastore in the metastore configuration""")
@cli_util.option('--metastore-id', help=u"""The OCID of the Data Catalog metastore in the metastore configuration""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVATING", "ACTIVE", "INACTIVE", "UPDATING", "FAILED", "DELETING", "DELETED"]), help=u"""The lifecycle state of the metastore in the metastore configuration""")
@cli_util.option('--bds-api-key-id', help=u"""The ID of the API key that is associated with the external metastore in the metastore configuration""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'list[BdsMetastoreConfigurationSummary]'})
@cli_util.wrap_exceptions
def list_bds_metastore_configurations(ctx, from_json, all_pages, page_size, bds_instance_id, metastore_type, metastore_id, lifecycle_state, bds_api_key_id, page, limit, sort_by, sort_order, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if metastore_type is not None:
        kwargs['metastore_type'] = metastore_type
    if metastore_id is not None:
        kwargs['metastore_id'] = metastore_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if bds_api_key_id is not None:
        kwargs['bds_api_key_id'] = bds_api_key_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_bds_metastore_configurations,
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_bds_metastore_configurations,
            limit,
            page_size,
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    else:
        result = client.list_bds_metastore_configurations(
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@bds_instance_group.command(name=cli_util.override('bds.list_patch_histories.command_name', 'list-patch-histories'), help=u"""List the patch history of this cluster. \n[Command Reference](listPatchHistories)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["INSTALLING", "INSTALLED", "FAILED"]), help=u"""The status of the patch.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--patch-version', help=u"""The version of the patch""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'list[PatchHistorySummary]'})
@cli_util.wrap_exceptions
def list_patch_histories(ctx, from_json, all_pages, page_size, bds_instance_id, lifecycle_state, sort_by, patch_version, sort_order, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if patch_version is not None:
        kwargs['patch_version'] = patch_version
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_patch_histories,
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_patch_histories,
            limit,
            page_size,
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    else:
        result = client.list_patch_histories(
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@bds_instance_group.command(name=cli_util.override('bds.list_patches.command_name', 'list-patches'), help=u"""List all the available patches for this cluster. \n[Command Reference](listPatches)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'list[PatchSummary]'})
@cli_util.wrap_exceptions
def list_patches(ctx, from_json, all_pages, page_size, bds_instance_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_patches,
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_patches,
            limit,
            page_size,
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    else:
        result = client.list_patches(
            bds_instance_id=bds_instance_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('bds.list_work_request_errors.command_name', 'list'), help=u"""Returns a paginated list of errors for a work request identified by the given ID. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
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


@work_request_log_entry_group.command(name=cli_util.override('bds.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Returns a paginated list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
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


@work_request_group.command(name=cli_util.override('bds.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--resource-id', help=u"""The OCID of the resource.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bds', 'class': 'list[WorkRequest]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, resource_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bds', 'bds', ctx)
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


@bds_instance_group.command(name=cli_util.override('bds.remove_auto_scaling_configuration.command_name', 'remove'), help=u"""Deletes an autoscale configuration. \n[Command Reference](removeAutoScalingConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""Unique Oracle-assigned identifier of the autoscale configuration.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def remove_auto_scaling_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, auto_scaling_configuration_id, cluster_admin_password, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['clusterAdminPassword'] = cluster_admin_password

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.remove_auto_scaling_configuration(
        bds_instance_id=bds_instance_id,
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        remove_auto_scaling_configuration_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.remove_cloud_sql.command_name', 'remove'), help=u"""Removes Cloud SQL from the cluster. \n[Command Reference](removeCloudSql)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def remove_cloud_sql(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, cluster_admin_password, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['clusterAdminPassword'] = cluster_admin_password

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.remove_cloud_sql(
        bds_instance_id=bds_instance_id,
        remove_cloud_sql_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.remove_node.command_name', 'remove'), help=u"""Remove a single node of a Big Data Service cluster \n[Command Reference](removeNode)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--node-id', required=True, help=u"""OCID of the node to be removed.""")
@cli_util.option('--is-force-remove-enabled', type=click.BOOL, help=u"""Boolean flag specifying whether or not to force remove node if graceful removal fails.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def remove_node(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, cluster_admin_password, node_id, is_force_remove_enabled, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['clusterAdminPassword'] = cluster_admin_password
    _details['nodeId'] = node_id

    if is_force_remove_enabled is not None:
        _details['isForceRemoveEnabled'] = is_force_remove_enabled

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.remove_node(
        bds_instance_id=bds_instance_id,
        remove_node_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.restart_node.command_name', 'restart-node'), help=u"""Restarts a single node of a Big Data Service cluster \n[Command Reference](restartNode)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--node-id', required=True, help=u"""OCID of the node to be restarted.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def restart_node(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, node_id, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['nodeId'] = node_id

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.restart_node(
        bds_instance_id=bds_instance_id,
        restart_node_details=_details,
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


@bds_metastore_configuration_group.command(name=cli_util.override('bds.test_bds_metastore_configuration.command_name', 'test'), help=u"""Test specified metastore configuration. \n[Command Reference](testBdsMetastoreConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--metastore-config-id', required=True, help=u"""The metastore configuration ID""")
@cli_util.option('--cluster-admin-password', required=True, help=u"""Base-64 encoded password for the cluster admin user.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def test_bds_metastore_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, metastore_config_id, cluster_admin_password, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(metastore_config_id, six.string_types) and len(metastore_config_id.strip()) == 0:
        raise click.UsageError('Parameter --metastore-config-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['clusterAdminPassword'] = cluster_admin_password

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.test_bds_metastore_configuration(
        bds_instance_id=bds_instance_id,
        metastore_config_id=metastore_config_id,
        test_bds_metastore_configuration_details=_details,
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


@bds_api_key_group.command(name=cli_util.override('bds.test_bds_object_storage_connection.command_name', 'test-bds-object-storage-connection'), help=u"""Test access to specified Object Storage bucket using the API key. \n[Command Reference](testBdsObjectStorageConnection)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--api-key-id', required=True, help=u"""The API key identifier.""")
@cli_util.option('--object-storage-uri', required=True, help=u"""An Oracle Cloud Infrastructure URI to which this connection must be attempted. See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.""")
@cli_util.option('--passphrase', required=True, help=u"""Base64 passphrase used to secure the private key which will be created on user behalf.""")
@cli_util.option('--object-storage-region', help=u"""The name of the region to establish the Object Storage endpoint. Example us-phoenix-1 .""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def test_bds_object_storage_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, api_key_id, object_storage_uri, passphrase, object_storage_region):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(api_key_id, six.string_types) and len(api_key_id.strip()) == 0:
        raise click.UsageError('Parameter --api-key-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['objectStorageUri'] = object_storage_uri
    _details['passphrase'] = passphrase

    if object_storage_region is not None:
        _details['objectStorageRegion'] = object_storage_region

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.test_bds_object_storage_connection(
        bds_instance_id=bds_instance_id,
        api_key_id=api_key_id,
        test_bds_object_storage_connection_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.update_auto_scaling_configuration.command_name', 'update-auto-scaling-configuration'), help=u"""Updates fields on an autoscale configuration, including the name, the threshold value, and whether the autoscale configuration is enabled. \n[Command Reference](updateAutoScalingConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""Unique Oracle-assigned identifier of the autoscale configuration.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscale configuration is enabled.""")
@cli_util.option('--cluster-admin-password', help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--policy-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details': {'module': 'bds', 'class': 'UpdateAutoScalePolicyDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details': {'module': 'bds', 'class': 'UpdateAutoScalePolicyDetails'}})
@cli_util.wrap_exceptions
def update_auto_scaling_configuration(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, auto_scaling_configuration_id, display_name, is_enabled, cluster_admin_password, policy, policy_details, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')
    if not force:
        if policy or policy_details:
            if not click.confirm("WARNING: Updates to policy and policy-details will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if cluster_admin_password is not None:
        _details['clusterAdminPassword'] = cluster_admin_password

    if policy is not None:
        _details['policy'] = cli_util.parse_json_parameter("policy", policy)

    if policy_details is not None:
        _details['policyDetails'] = cli_util.parse_json_parameter("policy_details", policy_details)

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.update_auto_scaling_configuration(
        bds_instance_id=bds_instance_id,
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        update_auto_scaling_configuration_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.update_auto_scaling_configuration_update_schedule_based_horizontal_scaling_policy_details.command_name', 'update-auto-scaling-configuration-update-schedule-based-horizontal-scaling-policy-details'), help=u"""Updates fields on an autoscale configuration, including the name, the threshold value, and whether the autoscale configuration is enabled. \n[Command Reference](updateAutoScalingConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""Unique Oracle-assigned identifier of the autoscale configuration.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscale configuration is enabled.""")
@cli_util.option('--cluster-admin-password', help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--policy-details-timezone', help=u"""The time zone of the execution schedule, in IANA time zone database name format""")
@cli_util.option('--policy-details-schedule-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type HorizontalScalingScheduleDetails.  For documentation on HorizontalScalingScheduleDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/bds/20190531/datatypes/HorizontalScalingScheduleDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-schedule-details': {'module': 'bds', 'class': 'list[HorizontalScalingScheduleDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-schedule-details': {'module': 'bds', 'class': 'list[HorizontalScalingScheduleDetails]'}})
@cli_util.wrap_exceptions
def update_auto_scaling_configuration_update_schedule_based_horizontal_scaling_policy_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, auto_scaling_configuration_id, display_name, is_enabled, cluster_admin_password, policy, if_match, policy_details_timezone, policy_details_schedule_details):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')
    if not force:
        if policy:
            if not click.confirm("WARNING: Updates to policy will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['policyDetails'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if cluster_admin_password is not None:
        _details['clusterAdminPassword'] = cluster_admin_password

    if policy is not None:
        _details['policy'] = cli_util.parse_json_parameter("policy", policy)

    if policy_details_timezone is not None:
        _details['policyDetails']['timezone'] = policy_details_timezone

    if policy_details_schedule_details is not None:
        _details['policyDetails']['scheduleDetails'] = cli_util.parse_json_parameter("policy_details_schedule_details", policy_details_schedule_details)

    _details['policyDetails']['policyType'] = 'SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY'

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.update_auto_scaling_configuration(
        bds_instance_id=bds_instance_id,
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        update_auto_scaling_configuration_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.update_auto_scaling_configuration_update_metric_based_vertical_scaling_policy_details.command_name', 'update-auto-scaling-configuration-update-metric-based-vertical-scaling-policy-details'), help=u"""Updates fields on an autoscale configuration, including the name, the threshold value, and whether the autoscale configuration is enabled. \n[Command Reference](updateAutoScalingConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""Unique Oracle-assigned identifier of the autoscale configuration.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscale configuration is enabled.""")
@cli_util.option('--cluster-admin-password', help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--policy-details-scale-up-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--policy-details-scale-down-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-scale-up-config': {'module': 'bds', 'class': 'MetricBasedVerticalScaleUpConfig'}, 'policy-details-scale-down-config': {'module': 'bds', 'class': 'MetricBasedVerticalScaleDownConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-scale-up-config': {'module': 'bds', 'class': 'MetricBasedVerticalScaleUpConfig'}, 'policy-details-scale-down-config': {'module': 'bds', 'class': 'MetricBasedVerticalScaleDownConfig'}})
@cli_util.wrap_exceptions
def update_auto_scaling_configuration_update_metric_based_vertical_scaling_policy_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, auto_scaling_configuration_id, display_name, is_enabled, cluster_admin_password, policy, if_match, policy_details_scale_up_config, policy_details_scale_down_config):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')
    if not force:
        if policy:
            if not click.confirm("WARNING: Updates to policy will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['policyDetails'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if cluster_admin_password is not None:
        _details['clusterAdminPassword'] = cluster_admin_password

    if policy is not None:
        _details['policy'] = cli_util.parse_json_parameter("policy", policy)

    if policy_details_scale_up_config is not None:
        _details['policyDetails']['scaleUpConfig'] = cli_util.parse_json_parameter("policy_details_scale_up_config", policy_details_scale_up_config)

    if policy_details_scale_down_config is not None:
        _details['policyDetails']['scaleDownConfig'] = cli_util.parse_json_parameter("policy_details_scale_down_config", policy_details_scale_down_config)

    _details['policyDetails']['policyType'] = 'METRIC_BASED_VERTICAL_SCALING_POLICY'

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.update_auto_scaling_configuration(
        bds_instance_id=bds_instance_id,
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        update_auto_scaling_configuration_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.update_auto_scaling_configuration_update_metric_based_horizontal_scaling_policy_details.command_name', 'update-auto-scaling-configuration-update-metric-based-horizontal-scaling-policy-details'), help=u"""Updates fields on an autoscale configuration, including the name, the threshold value, and whether the autoscale configuration is enabled. \n[Command Reference](updateAutoScalingConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""Unique Oracle-assigned identifier of the autoscale configuration.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscale configuration is enabled.""")
@cli_util.option('--cluster-admin-password', help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--policy-details-scale-out-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--policy-details-scale-in-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-scale-out-config': {'module': 'bds', 'class': 'MetricBasedHorizontalScaleOutConfig'}, 'policy-details-scale-in-config': {'module': 'bds', 'class': 'MetricBasedHorizontalScaleInConfig'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-scale-out-config': {'module': 'bds', 'class': 'MetricBasedHorizontalScaleOutConfig'}, 'policy-details-scale-in-config': {'module': 'bds', 'class': 'MetricBasedHorizontalScaleInConfig'}})
@cli_util.wrap_exceptions
def update_auto_scaling_configuration_update_metric_based_horizontal_scaling_policy_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, auto_scaling_configuration_id, display_name, is_enabled, cluster_admin_password, policy, if_match, policy_details_scale_out_config, policy_details_scale_in_config):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')
    if not force:
        if policy:
            if not click.confirm("WARNING: Updates to policy will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['policyDetails'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if cluster_admin_password is not None:
        _details['clusterAdminPassword'] = cluster_admin_password

    if policy is not None:
        _details['policy'] = cli_util.parse_json_parameter("policy", policy)

    if policy_details_scale_out_config is not None:
        _details['policyDetails']['scaleOutConfig'] = cli_util.parse_json_parameter("policy_details_scale_out_config", policy_details_scale_out_config)

    if policy_details_scale_in_config is not None:
        _details['policyDetails']['scaleInConfig'] = cli_util.parse_json_parameter("policy_details_scale_in_config", policy_details_scale_in_config)

    _details['policyDetails']['policyType'] = 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.update_auto_scaling_configuration(
        bds_instance_id=bds_instance_id,
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        update_auto_scaling_configuration_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.update_auto_scaling_configuration_update_schedule_based_vertical_scaling_policy_details.command_name', 'update-auto-scaling-configuration-update-schedule-based-vertical-scaling-policy-details'), help=u"""Updates fields on an autoscale configuration, including the name, the threshold value, and whether the autoscale configuration is enabled. \n[Command Reference](updateAutoScalingConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--auto-scaling-configuration-id', required=True, help=u"""Unique Oracle-assigned identifier of the autoscale configuration.""")
@cli_util.option('--display-name', help=u"""A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.""")
@cli_util.option('--is-enabled', type=click.BOOL, help=u"""Whether the autoscale configuration is enabled.""")
@cli_util.option('--cluster-admin-password', help=u"""Base-64 encoded password for the cluster (and Cloudera Manager) admin user.""")
@cli_util.option('--policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--policy-details-timezone', help=u"""The time zone of the execution schedule, in IANA time zone database name format""")
@cli_util.option('--policy-details-schedule-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type VerticalScalingScheduleDetails.  For documentation on VerticalScalingScheduleDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/bds/20190531/datatypes/VerticalScalingScheduleDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-schedule-details': {'module': 'bds', 'class': 'list[VerticalScalingScheduleDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'policy': {'module': 'bds', 'class': 'AutoScalePolicy'}, 'policy-details-schedule-details': {'module': 'bds', 'class': 'list[VerticalScalingScheduleDetails]'}})
@cli_util.wrap_exceptions
def update_auto_scaling_configuration_update_schedule_based_vertical_scaling_policy_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, auto_scaling_configuration_id, display_name, is_enabled, cluster_admin_password, policy, if_match, policy_details_timezone, policy_details_schedule_details):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(auto_scaling_configuration_id, six.string_types) and len(auto_scaling_configuration_id.strip()) == 0:
        raise click.UsageError('Parameter --auto-scaling-configuration-id cannot be whitespace or empty string')
    if not force:
        if policy:
            if not click.confirm("WARNING: Updates to policy will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['policyDetails'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if is_enabled is not None:
        _details['isEnabled'] = is_enabled

    if cluster_admin_password is not None:
        _details['clusterAdminPassword'] = cluster_admin_password

    if policy is not None:
        _details['policy'] = cli_util.parse_json_parameter("policy", policy)

    if policy_details_timezone is not None:
        _details['policyDetails']['timezone'] = policy_details_timezone

    if policy_details_schedule_details is not None:
        _details['policyDetails']['scheduleDetails'] = cli_util.parse_json_parameter("policy_details_schedule_details", policy_details_schedule_details)

    _details['policyDetails']['policyType'] = 'SCHEDULE_BASED_VERTICAL_SCALING_POLICY'

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.update_auto_scaling_configuration(
        bds_instance_id=bds_instance_id,
        auto_scaling_configuration_id=auto_scaling_configuration_id,
        update_auto_scaling_configuration_details=_details,
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


@bds_instance_group.command(name=cli_util.override('bds.update_bds_instance.command_name', 'update'), help=u"""Updates the Big Data Service cluster identified by the given ID. \n[Command Reference](updateBdsInstance)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--display-name', help=u"""Name of the cluster.""")
@cli_util.option('--bootstrap-script-url', help=u"""Pre-authenticated URL of the bootstrap script in Object Store that can be downloaded and executed..""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. For example, `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For example, `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'bds', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'bds', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'bds', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'bds', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_bds_instance(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, display_name, bootstrap_script_url, freeform_tags, defined_tags, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')
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

    if bootstrap_script_url is not None:
        _details['bootstrapScriptUrl'] = bootstrap_script_url

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.update_bds_instance(
        bds_instance_id=bds_instance_id,
        update_bds_instance_details=_details,
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


@bds_metastore_configuration_group.command(name=cli_util.override('bds.update_bds_metastore_configuration.command_name', 'update'), help=u"""Update the BDS metastore configuration represented by the provided ID. \n[Command Reference](updateBdsMetastoreConfiguration)""")
@cli_util.option('--bds-instance-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--metastore-config-id', required=True, help=u"""The metastore configuration ID""")
@cli_util.option('--display-name', help=u"""The display name of the metastore configuration.""")
@cli_util.option('--bds-api-key-id', help=u"""The ID of BDS Api Key used for Data Catalog metastore integration. Set only if metastore's type is EXTERNAL.""")
@cli_util.option('--bds-api-key-passphrase', help=u"""Base-64 encoded passphrase of the BDS Api Key.""")
@cli_util.option('--cluster-admin-password', help=u"""Base-64 encoded password for the cluster admin user.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_bds_metastore_configuration(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bds_instance_id, metastore_config_id, display_name, bds_api_key_id, bds_api_key_passphrase, cluster_admin_password, if_match):

    if isinstance(bds_instance_id, six.string_types) and len(bds_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --bds-instance-id cannot be whitespace or empty string')

    if isinstance(metastore_config_id, six.string_types) and len(metastore_config_id.strip()) == 0:
        raise click.UsageError('Parameter --metastore-config-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if bds_api_key_id is not None:
        _details['bdsApiKeyId'] = bds_api_key_id

    if bds_api_key_passphrase is not None:
        _details['bdsApiKeyPassphrase'] = bds_api_key_passphrase

    if cluster_admin_password is not None:
        _details['clusterAdminPassword'] = cluster_admin_password

    client = cli_util.build_client('bds', 'bds', ctx)
    result = client.update_bds_metastore_configuration(
        bds_instance_id=bds_instance_id,
        metastore_config_id=metastore_config_id,
        update_bds_metastore_configuration_details=_details,
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
