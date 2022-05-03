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


@cli.command(cli_util.override('apm_synthetics.apm_synthetics_root_group.command_name', 'apm-synthetics'), cls=CommandGroupWithAlias, help=cli_util.override('apm_synthetics.apm_synthetics_root_group.help', """Use the Application Performance Monitoring Synthetic Monitoring API to query synthetic scripts and monitors. For more information, see [Application Performance Monitoring]."""), short_help=cli_util.override('apm_synthetics.apm_synthetics_root_group.short_help', """Application Performance Monitoring Synthetic Monitoring API"""))
@cli_util.help_option_group
def apm_synthetics_root_group():
    pass


@click.command(cli_util.override('apm_synthetics.dedicated_vantage_point_group.command_name', 'dedicated-vantage-point'), cls=CommandGroupWithAlias, help="""The information about a dedicated vantage point.""")
@cli_util.help_option_group
def dedicated_vantage_point_group():
    pass


@click.command(cli_util.override('apm_synthetics.script_collection_group.command_name', 'script-collection'), cls=CommandGroupWithAlias, help="""The results of a script search, which contains both ScriptSummary items and other data in an APM domain.""")
@cli_util.help_option_group
def script_collection_group():
    pass


@click.command(cli_util.override('apm_synthetics.monitor_group.command_name', 'monitor'), cls=CommandGroupWithAlias, help="""The information about a monitor.""")
@cli_util.help_option_group
def monitor_group():
    pass


@click.command(cli_util.override('apm_synthetics.monitor_result_group.command_name', 'monitor-result'), cls=CommandGroupWithAlias, help="""The monitor result for a specific execution.""")
@cli_util.help_option_group
def monitor_result_group():
    pass


@click.command(cli_util.override('apm_synthetics.monitor_collection_group.command_name', 'monitor-collection'), cls=CommandGroupWithAlias, help="""The results of a monitor search, which contains both MonitorSummary items and other data in an APM domain.""")
@cli_util.help_option_group
def monitor_collection_group():
    pass


@click.command(cli_util.override('apm_synthetics.dedicated_vantage_point_collection_group.command_name', 'dedicated-vantage-point-collection'), cls=CommandGroupWithAlias, help="""The results of a dedicated vantage point search, which contains DedicatedVantagePointSummary items and other data in an APM domain.""")
@cli_util.help_option_group
def dedicated_vantage_point_collection_group():
    pass


@click.command(cli_util.override('apm_synthetics.public_vantage_point_collection_group.command_name', 'public-vantage-point-collection'), cls=CommandGroupWithAlias, help="""The results of a public vantage point search, which contains PublicVantagePointSummary items and other data in an APM domain.""")
@cli_util.help_option_group
def public_vantage_point_collection_group():
    pass


@click.command(cli_util.override('apm_synthetics.script_group.command_name', 'script'), cls=CommandGroupWithAlias, help="""The information about the script.""")
@cli_util.help_option_group
def script_group():
    pass


apm_synthetics_root_group.add_command(dedicated_vantage_point_group)
apm_synthetics_root_group.add_command(script_collection_group)
apm_synthetics_root_group.add_command(monitor_group)
apm_synthetics_root_group.add_command(monitor_result_group)
apm_synthetics_root_group.add_command(monitor_collection_group)
apm_synthetics_root_group.add_command(dedicated_vantage_point_collection_group)
apm_synthetics_root_group.add_command(public_vantage_point_collection_group)
apm_synthetics_root_group.add_command(script_group)


@dedicated_vantage_point_group.command(name=cli_util.override('apm_synthetics.create_dedicated_vantage_point.command_name', 'create'), help=u"""Registers a new dedicated vantage point. \n[Command Reference](createDedicatedVantagePoint)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--display-name', required=True, help=u"""Unique dedicated vantage point name that cannot be edited. The name should not contain any confidential information.""")
@cli_util.option('--dvp-stack-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--region-parameterconflict', required=True, help=u"""Name of the region.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED"]), help=u"""Status of the dedicated vantage point.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'dvp-stack-details': {'module': 'apm_synthetics', 'class': 'DvpStackDetails'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dvp-stack-details': {'module': 'apm_synthetics', 'class': 'DvpStackDetails'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'DedicatedVantagePoint'})
@cli_util.wrap_exceptions
def create_dedicated_vantage_point(ctx, from_json, apm_domain_id, display_name, dvp_stack_details, region_parameterconflict, status, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['dvpStackDetails'] = cli_util.parse_json_parameter("dvp_stack_details", dvp_stack_details)
    _details['region'] = region_parameterconflict

    if status is not None:
        _details['status'] = status

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.create_dedicated_vantage_point(
        apm_domain_id=apm_domain_id,
        create_dedicated_vantage_point_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dedicated_vantage_point_group.command(name=cli_util.override('apm_synthetics.create_dedicated_vantage_point_oracle_rm_stack.command_name', 'create-dedicated-vantage-point-oracle-rm-stack'), help=u"""Registers a new dedicated vantage point. \n[Command Reference](createDedicatedVantagePoint)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--display-name', required=True, help=u"""Unique dedicated vantage point name that cannot be edited. The name should not contain any confidential information.""")
@cli_util.option('--region-parameterconflict', required=True, help=u"""Name of the region.""")
@cli_util.option('--dvp-stack-details-dvp-version', required=True, help=u"""Version of DVP.""")
@cli_util.option('--dvp-stack-details-dvp-stack-id', required=True, help=u"""Stack [OCID] of DVP RM stack.""")
@cli_util.option('--dvp-stack-details-dvp-stream-id', required=True, help=u"""Stream [OCID] of DVP RM stack.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED"]), help=u"""Status of the dedicated vantage point.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'DedicatedVantagePoint'})
@cli_util.wrap_exceptions
def create_dedicated_vantage_point_oracle_rm_stack(ctx, from_json, apm_domain_id, display_name, region_parameterconflict, dvp_stack_details_dvp_version, dvp_stack_details_dvp_stack_id, dvp_stack_details_dvp_stream_id, status, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dvpStackDetails'] = {}
    _details['displayName'] = display_name
    _details['region'] = region_parameterconflict
    _details['dvpStackDetails']['dvpVersion'] = dvp_stack_details_dvp_version
    _details['dvpStackDetails']['dvpStackId'] = dvp_stack_details_dvp_stack_id
    _details['dvpStackDetails']['dvpStreamId'] = dvp_stack_details_dvp_stream_id

    if status is not None:
        _details['status'] = status

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['dvpStackDetails']['dvpStackType'] = 'ORACLE_RM_STACK'

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.create_dedicated_vantage_point(
        apm_domain_id=apm_domain_id,
        create_dedicated_vantage_point_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitor_group.command(name=cli_util.override('apm_synthetics.create_monitor.command_name', 'create'), help=u"""Creates a new monitor. \n[Command Reference](createMonitor)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--display-name', required=True, help=u"""Unique name that can be edited. The name should not contain any confidential information.""")
@cli_util.option('--monitor-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SCRIPTED_BROWSER", "BROWSER", "SCRIPTED_REST", "REST"]), help=u"""Type of monitor.""")
@cli_util.option('--vantage-points', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of public and dedicated vantage points from which to execute the monitor. Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--repeat-interval-in-seconds', required=True, type=click.INT, help=u"""Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.""")
@cli_util.option('--script-id', help=u"""The [OCID] of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED", "INVALID"]), help=u"""Enables or disables the monitor.""")
@cli_util.option('--is-run-once', type=click.BOOL, help=u"""If runOnce is enabled, then the monitor will run once.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.""")
@cli_util.option('--target', help=u"""Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.""")
@cli_util.option('--script-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of script parameters in the monitor. This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`

This option is a JSON list with items of type MonitorScriptParameter.  For documentation on MonitorScriptParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/MonitorScriptParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'configuration': {'module': 'apm_synthetics', 'class': 'MonitorConfiguration'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'configuration': {'module': 'apm_synthetics', 'class': 'MonitorConfiguration'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor(ctx, from_json, apm_domain_id, display_name, monitor_type, vantage_points, repeat_interval_in_seconds, script_id, status, is_run_once, timeout_in_seconds, target, script_parameters, configuration, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['monitorType'] = monitor_type
    _details['vantagePoints'] = cli_util.parse_json_parameter("vantage_points", vantage_points)
    _details['repeatIntervalInSeconds'] = repeat_interval_in_seconds

    if script_id is not None:
        _details['scriptId'] = script_id

    if status is not None:
        _details['status'] = status

    if is_run_once is not None:
        _details['isRunOnce'] = is_run_once

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if target is not None:
        _details['target'] = target

    if script_parameters is not None:
        _details['scriptParameters'] = cli_util.parse_json_parameter("script_parameters", script_parameters)

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.create_monitor(
        apm_domain_id=apm_domain_id,
        create_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitor_group.command(name=cli_util.override('apm_synthetics.create_monitor_scripted_rest_monitor_configuration.command_name', 'create-monitor-scripted-rest-monitor-configuration'), help=u"""Creates a new monitor. \n[Command Reference](createMonitor)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--display-name', required=True, help=u"""Unique name that can be edited. The name should not contain any confidential information.""")
@cli_util.option('--monitor-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SCRIPTED_BROWSER", "BROWSER", "SCRIPTED_REST", "REST"]), help=u"""Type of monitor.""")
@cli_util.option('--vantage-points', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of public and dedicated vantage points from which to execute the monitor. Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--repeat-interval-in-seconds', required=True, type=click.INT, help=u"""Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.""")
@cli_util.option('--script-id', help=u"""The [OCID] of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED", "INVALID"]), help=u"""Enables or disables the monitor.""")
@cli_util.option('--is-run-once', type=click.BOOL, help=u"""If runOnce is enabled, then the monitor will run once.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.""")
@cli_util.option('--target', help=u"""Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.""")
@cli_util.option('--script-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of script parameters in the monitor. This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`

This option is a JSON list with items of type MonitorScriptParameter.  For documentation on MonitorScriptParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/MonitorScriptParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--configuration-network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_scripted_rest_monitor_configuration(ctx, from_json, apm_domain_id, display_name, monitor_type, vantage_points, repeat_interval_in_seconds, script_id, status, is_run_once, timeout_in_seconds, target, script_parameters, freeform_tags, defined_tags, configuration_is_failure_retried, configuration_network_configuration):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configuration'] = {}
    _details['displayName'] = display_name
    _details['monitorType'] = monitor_type
    _details['vantagePoints'] = cli_util.parse_json_parameter("vantage_points", vantage_points)
    _details['repeatIntervalInSeconds'] = repeat_interval_in_seconds

    if script_id is not None:
        _details['scriptId'] = script_id

    if status is not None:
        _details['status'] = status

    if is_run_once is not None:
        _details['isRunOnce'] = is_run_once

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if target is not None:
        _details['target'] = target

    if script_parameters is not None:
        _details['scriptParameters'] = cli_util.parse_json_parameter("script_parameters", script_parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if configuration_is_failure_retried is not None:
        _details['configuration']['isFailureRetried'] = configuration_is_failure_retried

    if configuration_network_configuration is not None:
        _details['configuration']['networkConfiguration'] = cli_util.parse_json_parameter("configuration_network_configuration", configuration_network_configuration)

    _details['configuration']['configType'] = 'SCRIPTED_REST_CONFIG'

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.create_monitor(
        apm_domain_id=apm_domain_id,
        create_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitor_group.command(name=cli_util.override('apm_synthetics.create_monitor_scripted_browser_monitor_configuration.command_name', 'create-monitor-scripted-browser-monitor-configuration'), help=u"""Creates a new monitor. \n[Command Reference](createMonitor)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--display-name', required=True, help=u"""Unique name that can be edited. The name should not contain any confidential information.""")
@cli_util.option('--monitor-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SCRIPTED_BROWSER", "BROWSER", "SCRIPTED_REST", "REST"]), help=u"""Type of monitor.""")
@cli_util.option('--vantage-points', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of public and dedicated vantage points from which to execute the monitor. Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--repeat-interval-in-seconds', required=True, type=click.INT, help=u"""Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.""")
@cli_util.option('--script-id', help=u"""The [OCID] of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED", "INVALID"]), help=u"""Enables or disables the monitor.""")
@cli_util.option('--is-run-once', type=click.BOOL, help=u"""If runOnce is enabled, then the monitor will run once.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.""")
@cli_util.option('--target', help=u"""Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.""")
@cli_util.option('--script-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of script parameters in the monitor. This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`

This option is a JSON list with items of type MonitorScriptParameter.  For documentation on MonitorScriptParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/MonitorScriptParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--configuration-is-certificate-validation-enabled', type=click.BOOL, help=u"""If certificate validation is enabled, then the call will fail in case of certification errors.""")
@cli_util.option('--configuration-network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_scripted_browser_monitor_configuration(ctx, from_json, apm_domain_id, display_name, monitor_type, vantage_points, repeat_interval_in_seconds, script_id, status, is_run_once, timeout_in_seconds, target, script_parameters, freeform_tags, defined_tags, configuration_is_failure_retried, configuration_is_certificate_validation_enabled, configuration_network_configuration):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configuration'] = {}
    _details['displayName'] = display_name
    _details['monitorType'] = monitor_type
    _details['vantagePoints'] = cli_util.parse_json_parameter("vantage_points", vantage_points)
    _details['repeatIntervalInSeconds'] = repeat_interval_in_seconds

    if script_id is not None:
        _details['scriptId'] = script_id

    if status is not None:
        _details['status'] = status

    if is_run_once is not None:
        _details['isRunOnce'] = is_run_once

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if target is not None:
        _details['target'] = target

    if script_parameters is not None:
        _details['scriptParameters'] = cli_util.parse_json_parameter("script_parameters", script_parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if configuration_is_failure_retried is not None:
        _details['configuration']['isFailureRetried'] = configuration_is_failure_retried

    if configuration_is_certificate_validation_enabled is not None:
        _details['configuration']['isCertificateValidationEnabled'] = configuration_is_certificate_validation_enabled

    if configuration_network_configuration is not None:
        _details['configuration']['networkConfiguration'] = cli_util.parse_json_parameter("configuration_network_configuration", configuration_network_configuration)

    _details['configuration']['configType'] = 'SCRIPTED_BROWSER_CONFIG'

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.create_monitor(
        apm_domain_id=apm_domain_id,
        create_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitor_group.command(name=cli_util.override('apm_synthetics.create_monitor_rest_monitor_configuration.command_name', 'create-monitor-rest-monitor-configuration'), help=u"""Creates a new monitor. \n[Command Reference](createMonitor)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--display-name', required=True, help=u"""Unique name that can be edited. The name should not contain any confidential information.""")
@cli_util.option('--monitor-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SCRIPTED_BROWSER", "BROWSER", "SCRIPTED_REST", "REST"]), help=u"""Type of monitor.""")
@cli_util.option('--vantage-points', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of public and dedicated vantage points from which to execute the monitor. Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--repeat-interval-in-seconds', required=True, type=click.INT, help=u"""Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.""")
@cli_util.option('--script-id', help=u"""The [OCID] of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED", "INVALID"]), help=u"""Enables or disables the monitor.""")
@cli_util.option('--is-run-once', type=click.BOOL, help=u"""If runOnce is enabled, then the monitor will run once.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.""")
@cli_util.option('--target', help=u"""Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.""")
@cli_util.option('--script-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of script parameters in the monitor. This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`

This option is a JSON list with items of type MonitorScriptParameter.  For documentation on MonitorScriptParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/MonitorScriptParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--configuration-is-redirection-enabled', type=click.BOOL, help=u"""If redirection enabled, then redirects will be allowed while accessing target URL.""")
@cli_util.option('--configuration-is-certificate-validation-enabled', type=click.BOOL, help=u"""If certificate validation enabled, then call will fail for certificate errors.""")
@cli_util.option('--configuration-request-method', type=custom_types.CliCaseInsensitiveChoice(["GET", "POST"]), help=u"""Request HTTP method.""")
@cli_util.option('--configuration-req-authentication-scheme', type=custom_types.CliCaseInsensitiveChoice(["OAUTH", "NONE", "BASIC", "BEARER"]), help=u"""Request http authentication scheme.""")
@cli_util.option('--configuration-req-authentication-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-request-headers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of request headers. Example: `[{\"headerName\": \"content-type\", \"headerValue\":\"json\"}]`

This option is a JSON list with items of type Header.  For documentation on Header please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/Header.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-request-query-params', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of request query params. Example: `[{\"paramName\": \"sortOrder\", \"paramValue\": \"asc\"}]`

This option is a JSON list with items of type RequestQueryParam.  For documentation on RequestQueryParam please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/RequestQueryParam.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-request-post-body', help=u"""Request post body content.""")
@cli_util.option('--configuration-verify-response-content', help=u"""Verify response content against regular expression based string. If response content does not match the verifyResponseContent value, then it will be considered a failure.""")
@cli_util.option('--configuration-verify-response-codes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Expected HTTP response codes. For status code range, set values such as 2xx, 3xx.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-req-authentication-details': {'module': 'apm_synthetics', 'class': 'RequestAuthenticationDetails'}, 'configuration-request-headers': {'module': 'apm_synthetics', 'class': 'list[Header]'}, 'configuration-request-query-params': {'module': 'apm_synthetics', 'class': 'list[RequestQueryParam]'}, 'configuration-verify-response-codes': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-req-authentication-details': {'module': 'apm_synthetics', 'class': 'RequestAuthenticationDetails'}, 'configuration-request-headers': {'module': 'apm_synthetics', 'class': 'list[Header]'}, 'configuration-request-query-params': {'module': 'apm_synthetics', 'class': 'list[RequestQueryParam]'}, 'configuration-verify-response-codes': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_rest_monitor_configuration(ctx, from_json, apm_domain_id, display_name, monitor_type, vantage_points, repeat_interval_in_seconds, script_id, status, is_run_once, timeout_in_seconds, target, script_parameters, freeform_tags, defined_tags, configuration_is_failure_retried, configuration_is_redirection_enabled, configuration_is_certificate_validation_enabled, configuration_request_method, configuration_req_authentication_scheme, configuration_req_authentication_details, configuration_request_headers, configuration_request_query_params, configuration_request_post_body, configuration_verify_response_content, configuration_verify_response_codes, configuration_network_configuration):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configuration'] = {}
    _details['displayName'] = display_name
    _details['monitorType'] = monitor_type
    _details['vantagePoints'] = cli_util.parse_json_parameter("vantage_points", vantage_points)
    _details['repeatIntervalInSeconds'] = repeat_interval_in_seconds

    if script_id is not None:
        _details['scriptId'] = script_id

    if status is not None:
        _details['status'] = status

    if is_run_once is not None:
        _details['isRunOnce'] = is_run_once

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if target is not None:
        _details['target'] = target

    if script_parameters is not None:
        _details['scriptParameters'] = cli_util.parse_json_parameter("script_parameters", script_parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if configuration_is_failure_retried is not None:
        _details['configuration']['isFailureRetried'] = configuration_is_failure_retried

    if configuration_is_redirection_enabled is not None:
        _details['configuration']['isRedirectionEnabled'] = configuration_is_redirection_enabled

    if configuration_is_certificate_validation_enabled is not None:
        _details['configuration']['isCertificateValidationEnabled'] = configuration_is_certificate_validation_enabled

    if configuration_request_method is not None:
        _details['configuration']['requestMethod'] = configuration_request_method

    if configuration_req_authentication_scheme is not None:
        _details['configuration']['reqAuthenticationScheme'] = configuration_req_authentication_scheme

    if configuration_req_authentication_details is not None:
        _details['configuration']['reqAuthenticationDetails'] = cli_util.parse_json_parameter("configuration_req_authentication_details", configuration_req_authentication_details)

    if configuration_request_headers is not None:
        _details['configuration']['requestHeaders'] = cli_util.parse_json_parameter("configuration_request_headers", configuration_request_headers)

    if configuration_request_query_params is not None:
        _details['configuration']['requestQueryParams'] = cli_util.parse_json_parameter("configuration_request_query_params", configuration_request_query_params)

    if configuration_request_post_body is not None:
        _details['configuration']['requestPostBody'] = configuration_request_post_body

    if configuration_verify_response_content is not None:
        _details['configuration']['verifyResponseContent'] = configuration_verify_response_content

    if configuration_verify_response_codes is not None:
        _details['configuration']['verifyResponseCodes'] = cli_util.parse_json_parameter("configuration_verify_response_codes", configuration_verify_response_codes)

    if configuration_network_configuration is not None:
        _details['configuration']['networkConfiguration'] = cli_util.parse_json_parameter("configuration_network_configuration", configuration_network_configuration)

    _details['configuration']['configType'] = 'REST_CONFIG'

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.create_monitor(
        apm_domain_id=apm_domain_id,
        create_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitor_group.command(name=cli_util.override('apm_synthetics.create_monitor_browser_monitor_configuration.command_name', 'create-monitor-browser-monitor-configuration'), help=u"""Creates a new monitor. \n[Command Reference](createMonitor)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--display-name', required=True, help=u"""Unique name that can be edited. The name should not contain any confidential information.""")
@cli_util.option('--monitor-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SCRIPTED_BROWSER", "BROWSER", "SCRIPTED_REST", "REST"]), help=u"""Type of monitor.""")
@cli_util.option('--vantage-points', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of public and dedicated vantage points from which to execute the monitor. Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--repeat-interval-in-seconds', required=True, type=click.INT, help=u"""Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.""")
@cli_util.option('--script-id', help=u"""The [OCID] of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED", "INVALID"]), help=u"""Enables or disables the monitor.""")
@cli_util.option('--is-run-once', type=click.BOOL, help=u"""If runOnce is enabled, then the monitor will run once.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.""")
@cli_util.option('--target', help=u"""Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.""")
@cli_util.option('--script-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of script parameters in the monitor. This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`

This option is a JSON list with items of type MonitorScriptParameter.  For documentation on MonitorScriptParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/MonitorScriptParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--configuration-is-certificate-validation-enabled', type=click.BOOL, help=u"""If certificate validation is enabled, then the call will fail in case of certification errors.""")
@cli_util.option('--configuration-verify-texts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Verifies all the search strings present in the response. If any search string is not present in the response, then it will be considered as a failure.

This option is a JSON list with items of type VerifyText.  For documentation on VerifyText please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/VerifyText.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-verify-texts': {'module': 'apm_synthetics', 'class': 'list[VerifyText]'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-verify-texts': {'module': 'apm_synthetics', 'class': 'list[VerifyText]'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def create_monitor_browser_monitor_configuration(ctx, from_json, apm_domain_id, display_name, monitor_type, vantage_points, repeat_interval_in_seconds, script_id, status, is_run_once, timeout_in_seconds, target, script_parameters, freeform_tags, defined_tags, configuration_is_failure_retried, configuration_is_certificate_validation_enabled, configuration_verify_texts, configuration_network_configuration):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configuration'] = {}
    _details['displayName'] = display_name
    _details['monitorType'] = monitor_type
    _details['vantagePoints'] = cli_util.parse_json_parameter("vantage_points", vantage_points)
    _details['repeatIntervalInSeconds'] = repeat_interval_in_seconds

    if script_id is not None:
        _details['scriptId'] = script_id

    if status is not None:
        _details['status'] = status

    if is_run_once is not None:
        _details['isRunOnce'] = is_run_once

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if target is not None:
        _details['target'] = target

    if script_parameters is not None:
        _details['scriptParameters'] = cli_util.parse_json_parameter("script_parameters", script_parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if configuration_is_failure_retried is not None:
        _details['configuration']['isFailureRetried'] = configuration_is_failure_retried

    if configuration_is_certificate_validation_enabled is not None:
        _details['configuration']['isCertificateValidationEnabled'] = configuration_is_certificate_validation_enabled

    if configuration_verify_texts is not None:
        _details['configuration']['verifyTexts'] = cli_util.parse_json_parameter("configuration_verify_texts", configuration_verify_texts)

    if configuration_network_configuration is not None:
        _details['configuration']['networkConfiguration'] = cli_util.parse_json_parameter("configuration_network_configuration", configuration_network_configuration)

    _details['configuration']['configType'] = 'BROWSER_CONFIG'

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.create_monitor(
        apm_domain_id=apm_domain_id,
        create_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@script_group.command(name=cli_util.override('apm_synthetics.create_script.command_name', 'create'), help=u"""Creates a new script. \n[Command Reference](createScript)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--display-name', required=True, help=u"""Unique name that can be edited. The name should not contain any confidential information.""")
@cli_util.option('--content-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["SIDE", "JS"]), help=u"""Content type of script.""")
@cli_util.option('--content', required=True, help=u"""The content of the script. It may contain custom-defined tags that can be used for setting dynamic parameters. The format to set dynamic parameters is: `<ORAP><ON>param name</ON><OV>param value</OV><OS>isParamValueSecret(true/false)</OS></ORAP>`. Param value and isParamValueSecret are optional, the default value for isParamValueSecret is false. Examples: With mandatory param name : `<ORAP><ON>param name</ON></ORAP>` With parameter name and value : `<ORAP><ON>param name</ON><OV>param value</OV></ORAP>` Note that the content is valid if it matches the given content type. For example, if the content type is SIDE, then the content should be in Side script format. If the content type is JS, then the content should be in JavaScript format.""")
@cli_util.option('--content-file-name', help=u"""File name of uploaded script content.""")
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of script parameters. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\", \"isSecret\": false}]`

This option is a JSON list with items of type ScriptParameter.  For documentation on ScriptParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/ScriptParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'parameters': {'module': 'apm_synthetics', 'class': 'list[ScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parameters': {'module': 'apm_synthetics', 'class': 'list[ScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'Script'})
@cli_util.wrap_exceptions
def create_script(ctx, from_json, apm_domain_id, display_name, content_type, content, content_file_name, parameters, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['contentType'] = content_type
    _details['content'] = content

    if content_file_name is not None:
        _details['contentFileName'] = content_file_name

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.create_script(
        apm_domain_id=apm_domain_id,
        create_script_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dedicated_vantage_point_group.command(name=cli_util.override('apm_synthetics.delete_dedicated_vantage_point.command_name', 'delete'), help=u"""Deregisters the specified dedicated vantage point. \n[Command Reference](deleteDedicatedVantagePoint)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--dedicated-vantage-point-id', required=True, help=u"""The OCID of the dedicated vantage point.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_dedicated_vantage_point(ctx, from_json, apm_domain_id, dedicated_vantage_point_id, if_match):

    if isinstance(dedicated_vantage_point_id, six.string_types) and len(dedicated_vantage_point_id.strip()) == 0:
        raise click.UsageError('Parameter --dedicated-vantage-point-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.delete_dedicated_vantage_point(
        apm_domain_id=apm_domain_id,
        dedicated_vantage_point_id=dedicated_vantage_point_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitor_group.command(name=cli_util.override('apm_synthetics.delete_monitor.command_name', 'delete'), help=u"""Deletes the specified monitor. \n[Command Reference](deleteMonitor)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of the monitor.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_monitor(ctx, from_json, apm_domain_id, monitor_id, if_match):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.delete_monitor(
        apm_domain_id=apm_domain_id,
        monitor_id=monitor_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@script_group.command(name=cli_util.override('apm_synthetics.delete_script.command_name', 'delete'), help=u"""Deletes the specified script. \n[Command Reference](deleteScript)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--script-id', required=True, help=u"""The OCID of the script.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_script(ctx, from_json, apm_domain_id, script_id, if_match):

    if isinstance(script_id, six.string_types) and len(script_id.strip()) == 0:
        raise click.UsageError('Parameter --script-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.delete_script(
        apm_domain_id=apm_domain_id,
        script_id=script_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dedicated_vantage_point_group.command(name=cli_util.override('apm_synthetics.get_dedicated_vantage_point.command_name', 'get'), help=u"""Gets the details of the dedicated vantage point identified by the OCID. \n[Command Reference](getDedicatedVantagePoint)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--dedicated-vantage-point-id', required=True, help=u"""The OCID of the dedicated vantage point.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_synthetics', 'class': 'DedicatedVantagePoint'})
@cli_util.wrap_exceptions
def get_dedicated_vantage_point(ctx, from_json, apm_domain_id, dedicated_vantage_point_id):

    if isinstance(dedicated_vantage_point_id, six.string_types) and len(dedicated_vantage_point_id.strip()) == 0:
        raise click.UsageError('Parameter --dedicated-vantage-point-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.get_dedicated_vantage_point(
        apm_domain_id=apm_domain_id,
        dedicated_vantage_point_id=dedicated_vantage_point_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitor_group.command(name=cli_util.override('apm_synthetics.get_monitor.command_name', 'get'), help=u"""Gets the configuration of the monitor identified by the OCID. \n[Command Reference](getMonitor)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of the monitor.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def get_monitor(ctx, from_json, apm_domain_id, monitor_id):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.get_monitor(
        apm_domain_id=apm_domain_id,
        monitor_id=monitor_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitor_result_group.command(name=cli_util.override('apm_synthetics.get_monitor_result.command_name', 'get'), help=u"""Gets the results for a specific execution of a monitor identified by OCID. The results are in a HAR file, Screenshot, Console Log or Network details. \n[Command Reference](getMonitorResult)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of the monitor.""")
@cli_util.option('--vantage-point', required=True, help=u"""The vantagePoint name.""")
@cli_util.option('--result-type', required=True, help=u"""The result type: har, screenshot, log, or network.""")
@cli_util.option('--result-content-type', required=True, help=u"""The result content type: zip or raw.""")
@cli_util.option('--execution-time', required=True, help=u"""The time the object was posted.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_synthetics', 'class': 'MonitorResult'})
@cli_util.wrap_exceptions
def get_monitor_result(ctx, from_json, apm_domain_id, monitor_id, vantage_point, result_type, result_content_type, execution_time):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')

    if isinstance(execution_time, six.string_types) and len(execution_time.strip()) == 0:
        raise click.UsageError('Parameter --execution-time cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.get_monitor_result(
        apm_domain_id=apm_domain_id,
        monitor_id=monitor_id,
        vantage_point=vantage_point,
        result_type=result_type,
        result_content_type=result_content_type,
        execution_time=execution_time,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@script_group.command(name=cli_util.override('apm_synthetics.get_script.command_name', 'get'), help=u"""Gets the configuration of the script identified by the OCID. \n[Command Reference](getScript)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--script-id', required=True, help=u"""The OCID of the script.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_synthetics', 'class': 'Script'})
@cli_util.wrap_exceptions
def get_script(ctx, from_json, apm_domain_id, script_id):

    if isinstance(script_id, six.string_types) and len(script_id.strip()) == 0:
        raise click.UsageError('Parameter --script-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.get_script(
        apm_domain_id=apm_domain_id,
        script_id=script_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dedicated_vantage_point_collection_group.command(name=cli_util.override('apm_synthetics.list_dedicated_vantage_points.command_name', 'list-dedicated-vantage-points'), help=u"""Returns a list of dedicated vantage points. \n[Command Reference](listDedicatedVantagePoints)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "name", "timeCreated", "timeUpdated", "status"]), help=u"""The field to sort by. Only one sort order may be provided. Default order of displayName is ascending. Default order of timeCreated and timeUpdated is descending. The displayName sort by is case sensitive.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire display name.""")
@cli_util.option('--name', help=u"""A filter to return only the resources that match the entire name.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED"]), help=u"""A filter to return only the dedicated vantage points that match a given status.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_synthetics', 'class': 'DedicatedVantagePointCollection'})
@cli_util.wrap_exceptions
def list_dedicated_vantage_points(ctx, from_json, all_pages, page_size, apm_domain_id, limit, page, sort_order, sort_by, display_name, name, status):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if display_name is not None:
        kwargs['display_name'] = display_name
    if name is not None:
        kwargs['name'] = name
    if status is not None:
        kwargs['status'] = status
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dedicated_vantage_points,
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dedicated_vantage_points,
            limit,
            page_size,
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    else:
        result = client.list_dedicated_vantage_points(
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@monitor_collection_group.command(name=cli_util.override('apm_synthetics.list_monitors.command_name', 'list-monitors'), help=u"""Returns a list of monitors. \n[Command Reference](listMonitors)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire display name.""")
@cli_util.option('--script-id', help=u"""A filter to return only monitors using scriptId.""")
@cli_util.option('--vantage-point', help=u"""The name of the public or dedicated vantage point.""")
@cli_util.option('--monitor-type', help=u"""A filter to return only monitors that match the given monitor type. Supported values are SCRIPTED_BROWSER, BROWSER, SCRIPTED_REST and REST.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED", "INVALID"]), help=u"""A filter to return only monitors that match the status given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "timeCreated", "timeUpdated", "status", "monitorType"]), help=u"""The field to sort by. Only one sort order may be provided. Default order of displayName is ascending. Default order of timeCreated and timeUpdated is descending. The displayName sort by is case insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_synthetics', 'class': 'MonitorCollection'})
@cli_util.wrap_exceptions
def list_monitors(ctx, from_json, all_pages, page_size, apm_domain_id, display_name, script_id, vantage_point, monitor_type, status, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if script_id is not None:
        kwargs['script_id'] = script_id
    if vantage_point is not None:
        kwargs['vantage_point'] = vantage_point
    if monitor_type is not None:
        kwargs['monitor_type'] = monitor_type
    if status is not None:
        kwargs['status'] = status
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_monitors,
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_monitors,
            limit,
            page_size,
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    else:
        result = client.list_monitors(
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@public_vantage_point_collection_group.command(name=cli_util.override('apm_synthetics.list_public_vantage_points.command_name', 'list-public-vantage-points'), help=u"""Returns a list of public vantage points. \n[Command Reference](listPublicVantagePoints)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "displayName"]), help=u"""The field to sort by. You can provide one sort by (`sortBy`). Default order for displayName or name is ascending. The displayName or name sort by is case insensitive.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire display name.""")
@cli_util.option('--name', help=u"""A filter to return only the resources that match the entire name.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_synthetics', 'class': 'PublicVantagePointCollection'})
@cli_util.wrap_exceptions
def list_public_vantage_points(ctx, from_json, all_pages, page_size, apm_domain_id, limit, page, sort_order, sort_by, display_name, name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if display_name is not None:
        kwargs['display_name'] = display_name
    if name is not None:
        kwargs['name'] = name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_public_vantage_points,
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_public_vantage_points,
            limit,
            page_size,
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    else:
        result = client.list_public_vantage_points(
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@script_collection_group.command(name=cli_util.override('apm_synthetics.list_scripts.command_name', 'list-scripts'), help=u"""Returns a list of scripts. \n[Command Reference](listScripts)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--display-name', help=u"""A filter to return only the resources that match the entire display name.""")
@cli_util.option('--content-type', help=u"""A filter to return only resources that match the content type given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].

Example: `50`""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "timeCreated", "timeUpdated", "contentType"]), help=u"""The field to sort by. Only one sort order may be provided. Default order of displayName and contentType is ascending. Default order of timeCreated and timeUpdated is descending. The displayName sort by is case insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'apm_synthetics', 'class': 'ScriptCollection'})
@cli_util.wrap_exceptions
def list_scripts(ctx, from_json, all_pages, page_size, apm_domain_id, display_name, content_type, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if content_type is not None:
        kwargs['content_type'] = content_type
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_scripts,
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_scripts,
            limit,
            page_size,
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    else:
        result = client.list_scripts(
            apm_domain_id=apm_domain_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@dedicated_vantage_point_group.command(name=cli_util.override('apm_synthetics.update_dedicated_vantage_point.command_name', 'update'), help=u"""Updates the dedicated vantage point. \n[Command Reference](updateDedicatedVantagePoint)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--dedicated-vantage-point-id', required=True, help=u"""The OCID of the dedicated vantage point.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED"]), help=u"""Status of the dedicated vantage point.""")
@cli_util.option('--dvp-stack-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--region-parameterconflict', help=u"""Name of the region.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'dvp-stack-details': {'module': 'apm_synthetics', 'class': 'DvpStackDetails'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dvp-stack-details': {'module': 'apm_synthetics', 'class': 'DvpStackDetails'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'DedicatedVantagePoint'})
@cli_util.wrap_exceptions
def update_dedicated_vantage_point(ctx, from_json, force, apm_domain_id, dedicated_vantage_point_id, status, dvp_stack_details, region_parameterconflict, freeform_tags, defined_tags, if_match):

    if isinstance(dedicated_vantage_point_id, six.string_types) and len(dedicated_vantage_point_id.strip()) == 0:
        raise click.UsageError('Parameter --dedicated-vantage-point-id cannot be whitespace or empty string')
    if not force:
        if dvp_stack_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to dvp-stack-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if status is not None:
        _details['status'] = status

    if dvp_stack_details is not None:
        _details['dvpStackDetails'] = cli_util.parse_json_parameter("dvp_stack_details", dvp_stack_details)

    if region_parameterconflict is not None:
        _details['region'] = region_parameterconflict

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.update_dedicated_vantage_point(
        apm_domain_id=apm_domain_id,
        dedicated_vantage_point_id=dedicated_vantage_point_id,
        update_dedicated_vantage_point_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dedicated_vantage_point_group.command(name=cli_util.override('apm_synthetics.update_dedicated_vantage_point_oracle_rm_stack.command_name', 'update-dedicated-vantage-point-oracle-rm-stack'), help=u"""Updates the dedicated vantage point. \n[Command Reference](updateDedicatedVantagePoint)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--dedicated-vantage-point-id', required=True, help=u"""The OCID of the dedicated vantage point.""")
@cli_util.option('--dvp-stack-details-dvp-version', required=True, help=u"""Version of DVP.""")
@cli_util.option('--dvp-stack-details-dvp-stack-id', required=True, help=u"""Stack [OCID] of DVP RM stack.""")
@cli_util.option('--dvp-stack-details-dvp-stream-id', required=True, help=u"""Stream [OCID] of DVP RM stack.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED"]), help=u"""Status of the dedicated vantage point.""")
@cli_util.option('--region-parameterconflict', help=u"""Name of the region.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'DedicatedVantagePoint'})
@cli_util.wrap_exceptions
def update_dedicated_vantage_point_oracle_rm_stack(ctx, from_json, force, apm_domain_id, dedicated_vantage_point_id, dvp_stack_details_dvp_version, dvp_stack_details_dvp_stack_id, dvp_stack_details_dvp_stream_id, status, region_parameterconflict, freeform_tags, defined_tags, if_match):

    if isinstance(dedicated_vantage_point_id, six.string_types) and len(dedicated_vantage_point_id.strip()) == 0:
        raise click.UsageError('Parameter --dedicated-vantage-point-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dvpStackDetails'] = {}
    _details['dvpStackDetails']['dvpVersion'] = dvp_stack_details_dvp_version
    _details['dvpStackDetails']['dvpStackId'] = dvp_stack_details_dvp_stack_id
    _details['dvpStackDetails']['dvpStreamId'] = dvp_stack_details_dvp_stream_id

    if status is not None:
        _details['status'] = status

    if region_parameterconflict is not None:
        _details['region'] = region_parameterconflict

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['dvpStackDetails']['dvpStackType'] = 'ORACLE_RM_STACK'

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.update_dedicated_vantage_point(
        apm_domain_id=apm_domain_id,
        dedicated_vantage_point_id=dedicated_vantage_point_id,
        update_dedicated_vantage_point_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitor_group.command(name=cli_util.override('apm_synthetics.update_monitor.command_name', 'update'), help=u"""Updates the monitor. \n[Command Reference](updateMonitor)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of the monitor.""")
@cli_util.option('--display-name', help=u"""Unique name that can be edited. The name should not contain any confidential information.""")
@cli_util.option('--vantage-points', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of public and dedicated vantage points from which to execute the monitor. Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--script-id', help=u"""The [OCID] of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED", "INVALID"]), help=u"""Enables or disables the monitor.""")
@cli_util.option('--repeat-interval-in-seconds', type=click.INT, help=u"""Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.""")
@cli_util.option('--is-run-once', type=click.BOOL, help=u"""If runOnce is enabled, then the monitor will run once.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.""")
@cli_util.option('--target', help=u"""Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.""")
@cli_util.option('--script-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of script parameters in the monitor. This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`

This option is a JSON list with items of type MonitorScriptParameter.  For documentation on MonitorScriptParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/MonitorScriptParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'configuration': {'module': 'apm_synthetics', 'class': 'MonitorConfiguration'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'configuration': {'module': 'apm_synthetics', 'class': 'MonitorConfiguration'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor(ctx, from_json, force, apm_domain_id, monitor_id, display_name, vantage_points, script_id, status, repeat_interval_in_seconds, is_run_once, timeout_in_seconds, target, script_parameters, configuration, freeform_tags, defined_tags, if_match):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')
    if not force:
        if vantage_points or script_parameters or configuration or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to vantage-points and script-parameters and configuration and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if vantage_points is not None:
        _details['vantagePoints'] = cli_util.parse_json_parameter("vantage_points", vantage_points)

    if script_id is not None:
        _details['scriptId'] = script_id

    if status is not None:
        _details['status'] = status

    if repeat_interval_in_seconds is not None:
        _details['repeatIntervalInSeconds'] = repeat_interval_in_seconds

    if is_run_once is not None:
        _details['isRunOnce'] = is_run_once

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if target is not None:
        _details['target'] = target

    if script_parameters is not None:
        _details['scriptParameters'] = cli_util.parse_json_parameter("script_parameters", script_parameters)

    if configuration is not None:
        _details['configuration'] = cli_util.parse_json_parameter("configuration", configuration)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.update_monitor(
        apm_domain_id=apm_domain_id,
        monitor_id=monitor_id,
        update_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitor_group.command(name=cli_util.override('apm_synthetics.update_monitor_scripted_rest_monitor_configuration.command_name', 'update-monitor-scripted-rest-monitor-configuration'), help=u"""Updates the monitor. \n[Command Reference](updateMonitor)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of the monitor.""")
@cli_util.option('--display-name', help=u"""Unique name that can be edited. The name should not contain any confidential information.""")
@cli_util.option('--vantage-points', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of public and dedicated vantage points from which to execute the monitor. Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--script-id', help=u"""The [OCID] of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED", "INVALID"]), help=u"""Enables or disables the monitor.""")
@cli_util.option('--repeat-interval-in-seconds', type=click.INT, help=u"""Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.""")
@cli_util.option('--is-run-once', type=click.BOOL, help=u"""If runOnce is enabled, then the monitor will run once.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.""")
@cli_util.option('--target', help=u"""Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.""")
@cli_util.option('--script-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of script parameters in the monitor. This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`

This option is a JSON list with items of type MonitorScriptParameter.  For documentation on MonitorScriptParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/MonitorScriptParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--configuration-is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--configuration-network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_scripted_rest_monitor_configuration(ctx, from_json, force, apm_domain_id, monitor_id, display_name, vantage_points, script_id, status, repeat_interval_in_seconds, is_run_once, timeout_in_seconds, target, script_parameters, freeform_tags, defined_tags, if_match, configuration_is_failure_retried, configuration_network_configuration):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')
    if not force:
        if vantage_points or script_parameters or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to vantage-points and script-parameters and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configuration'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if vantage_points is not None:
        _details['vantagePoints'] = cli_util.parse_json_parameter("vantage_points", vantage_points)

    if script_id is not None:
        _details['scriptId'] = script_id

    if status is not None:
        _details['status'] = status

    if repeat_interval_in_seconds is not None:
        _details['repeatIntervalInSeconds'] = repeat_interval_in_seconds

    if is_run_once is not None:
        _details['isRunOnce'] = is_run_once

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if target is not None:
        _details['target'] = target

    if script_parameters is not None:
        _details['scriptParameters'] = cli_util.parse_json_parameter("script_parameters", script_parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if configuration_is_failure_retried is not None:
        _details['configuration']['isFailureRetried'] = configuration_is_failure_retried

    if configuration_network_configuration is not None:
        _details['configuration']['networkConfiguration'] = cli_util.parse_json_parameter("configuration_network_configuration", configuration_network_configuration)

    _details['configuration']['configType'] = 'SCRIPTED_REST_CONFIG'

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.update_monitor(
        apm_domain_id=apm_domain_id,
        monitor_id=monitor_id,
        update_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitor_group.command(name=cli_util.override('apm_synthetics.update_monitor_scripted_browser_monitor_configuration.command_name', 'update-monitor-scripted-browser-monitor-configuration'), help=u"""Updates the monitor. \n[Command Reference](updateMonitor)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of the monitor.""")
@cli_util.option('--display-name', help=u"""Unique name that can be edited. The name should not contain any confidential information.""")
@cli_util.option('--vantage-points', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of public and dedicated vantage points from which to execute the monitor. Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--script-id', help=u"""The [OCID] of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED", "INVALID"]), help=u"""Enables or disables the monitor.""")
@cli_util.option('--repeat-interval-in-seconds', type=click.INT, help=u"""Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.""")
@cli_util.option('--is-run-once', type=click.BOOL, help=u"""If runOnce is enabled, then the monitor will run once.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.""")
@cli_util.option('--target', help=u"""Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.""")
@cli_util.option('--script-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of script parameters in the monitor. This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`

This option is a JSON list with items of type MonitorScriptParameter.  For documentation on MonitorScriptParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/MonitorScriptParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--configuration-is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--configuration-is-certificate-validation-enabled', type=click.BOOL, help=u"""If certificate validation is enabled, then the call will fail in case of certification errors.""")
@cli_util.option('--configuration-network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_scripted_browser_monitor_configuration(ctx, from_json, force, apm_domain_id, monitor_id, display_name, vantage_points, script_id, status, repeat_interval_in_seconds, is_run_once, timeout_in_seconds, target, script_parameters, freeform_tags, defined_tags, if_match, configuration_is_failure_retried, configuration_is_certificate_validation_enabled, configuration_network_configuration):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')
    if not force:
        if vantage_points or script_parameters or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to vantage-points and script-parameters and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configuration'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if vantage_points is not None:
        _details['vantagePoints'] = cli_util.parse_json_parameter("vantage_points", vantage_points)

    if script_id is not None:
        _details['scriptId'] = script_id

    if status is not None:
        _details['status'] = status

    if repeat_interval_in_seconds is not None:
        _details['repeatIntervalInSeconds'] = repeat_interval_in_seconds

    if is_run_once is not None:
        _details['isRunOnce'] = is_run_once

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if target is not None:
        _details['target'] = target

    if script_parameters is not None:
        _details['scriptParameters'] = cli_util.parse_json_parameter("script_parameters", script_parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if configuration_is_failure_retried is not None:
        _details['configuration']['isFailureRetried'] = configuration_is_failure_retried

    if configuration_is_certificate_validation_enabled is not None:
        _details['configuration']['isCertificateValidationEnabled'] = configuration_is_certificate_validation_enabled

    if configuration_network_configuration is not None:
        _details['configuration']['networkConfiguration'] = cli_util.parse_json_parameter("configuration_network_configuration", configuration_network_configuration)

    _details['configuration']['configType'] = 'SCRIPTED_BROWSER_CONFIG'

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.update_monitor(
        apm_domain_id=apm_domain_id,
        monitor_id=monitor_id,
        update_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitor_group.command(name=cli_util.override('apm_synthetics.update_monitor_rest_monitor_configuration.command_name', 'update-monitor-rest-monitor-configuration'), help=u"""Updates the monitor. \n[Command Reference](updateMonitor)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of the monitor.""")
@cli_util.option('--display-name', help=u"""Unique name that can be edited. The name should not contain any confidential information.""")
@cli_util.option('--vantage-points', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of public and dedicated vantage points from which to execute the monitor. Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--script-id', help=u"""The [OCID] of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED", "INVALID"]), help=u"""Enables or disables the monitor.""")
@cli_util.option('--repeat-interval-in-seconds', type=click.INT, help=u"""Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.""")
@cli_util.option('--is-run-once', type=click.BOOL, help=u"""If runOnce is enabled, then the monitor will run once.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.""")
@cli_util.option('--target', help=u"""Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.""")
@cli_util.option('--script-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of script parameters in the monitor. This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`

This option is a JSON list with items of type MonitorScriptParameter.  For documentation on MonitorScriptParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/MonitorScriptParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--configuration-is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--configuration-is-redirection-enabled', type=click.BOOL, help=u"""If redirection enabled, then redirects will be allowed while accessing target URL.""")
@cli_util.option('--configuration-is-certificate-validation-enabled', type=click.BOOL, help=u"""If certificate validation enabled, then call will fail for certificate errors.""")
@cli_util.option('--configuration-request-method', type=custom_types.CliCaseInsensitiveChoice(["GET", "POST"]), help=u"""Request HTTP method.""")
@cli_util.option('--configuration-req-authentication-scheme', type=custom_types.CliCaseInsensitiveChoice(["OAUTH", "NONE", "BASIC", "BEARER"]), help=u"""Request http authentication scheme.""")
@cli_util.option('--configuration-req-authentication-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-request-headers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of request headers. Example: `[{\"headerName\": \"content-type\", \"headerValue\":\"json\"}]`

This option is a JSON list with items of type Header.  For documentation on Header please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/Header.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-request-query-params', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of request query params. Example: `[{\"paramName\": \"sortOrder\", \"paramValue\": \"asc\"}]`

This option is a JSON list with items of type RequestQueryParam.  For documentation on RequestQueryParam please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/RequestQueryParam.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-request-post-body', help=u"""Request post body content.""")
@cli_util.option('--configuration-verify-response-content', help=u"""Verify response content against regular expression based string. If response content does not match the verifyResponseContent value, then it will be considered a failure.""")
@cli_util.option('--configuration-verify-response-codes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Expected HTTP response codes. For status code range, set values such as 2xx, 3xx.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-req-authentication-details': {'module': 'apm_synthetics', 'class': 'RequestAuthenticationDetails'}, 'configuration-request-headers': {'module': 'apm_synthetics', 'class': 'list[Header]'}, 'configuration-request-query-params': {'module': 'apm_synthetics', 'class': 'list[RequestQueryParam]'}, 'configuration-verify-response-codes': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-req-authentication-details': {'module': 'apm_synthetics', 'class': 'RequestAuthenticationDetails'}, 'configuration-request-headers': {'module': 'apm_synthetics', 'class': 'list[Header]'}, 'configuration-request-query-params': {'module': 'apm_synthetics', 'class': 'list[RequestQueryParam]'}, 'configuration-verify-response-codes': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_rest_monitor_configuration(ctx, from_json, force, apm_domain_id, monitor_id, display_name, vantage_points, script_id, status, repeat_interval_in_seconds, is_run_once, timeout_in_seconds, target, script_parameters, freeform_tags, defined_tags, if_match, configuration_is_failure_retried, configuration_is_redirection_enabled, configuration_is_certificate_validation_enabled, configuration_request_method, configuration_req_authentication_scheme, configuration_req_authentication_details, configuration_request_headers, configuration_request_query_params, configuration_request_post_body, configuration_verify_response_content, configuration_verify_response_codes, configuration_network_configuration):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')
    if not force:
        if vantage_points or script_parameters or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to vantage-points and script-parameters and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configuration'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if vantage_points is not None:
        _details['vantagePoints'] = cli_util.parse_json_parameter("vantage_points", vantage_points)

    if script_id is not None:
        _details['scriptId'] = script_id

    if status is not None:
        _details['status'] = status

    if repeat_interval_in_seconds is not None:
        _details['repeatIntervalInSeconds'] = repeat_interval_in_seconds

    if is_run_once is not None:
        _details['isRunOnce'] = is_run_once

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if target is not None:
        _details['target'] = target

    if script_parameters is not None:
        _details['scriptParameters'] = cli_util.parse_json_parameter("script_parameters", script_parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if configuration_is_failure_retried is not None:
        _details['configuration']['isFailureRetried'] = configuration_is_failure_retried

    if configuration_is_redirection_enabled is not None:
        _details['configuration']['isRedirectionEnabled'] = configuration_is_redirection_enabled

    if configuration_is_certificate_validation_enabled is not None:
        _details['configuration']['isCertificateValidationEnabled'] = configuration_is_certificate_validation_enabled

    if configuration_request_method is not None:
        _details['configuration']['requestMethod'] = configuration_request_method

    if configuration_req_authentication_scheme is not None:
        _details['configuration']['reqAuthenticationScheme'] = configuration_req_authentication_scheme

    if configuration_req_authentication_details is not None:
        _details['configuration']['reqAuthenticationDetails'] = cli_util.parse_json_parameter("configuration_req_authentication_details", configuration_req_authentication_details)

    if configuration_request_headers is not None:
        _details['configuration']['requestHeaders'] = cli_util.parse_json_parameter("configuration_request_headers", configuration_request_headers)

    if configuration_request_query_params is not None:
        _details['configuration']['requestQueryParams'] = cli_util.parse_json_parameter("configuration_request_query_params", configuration_request_query_params)

    if configuration_request_post_body is not None:
        _details['configuration']['requestPostBody'] = configuration_request_post_body

    if configuration_verify_response_content is not None:
        _details['configuration']['verifyResponseContent'] = configuration_verify_response_content

    if configuration_verify_response_codes is not None:
        _details['configuration']['verifyResponseCodes'] = cli_util.parse_json_parameter("configuration_verify_response_codes", configuration_verify_response_codes)

    if configuration_network_configuration is not None:
        _details['configuration']['networkConfiguration'] = cli_util.parse_json_parameter("configuration_network_configuration", configuration_network_configuration)

    _details['configuration']['configType'] = 'REST_CONFIG'

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.update_monitor(
        apm_domain_id=apm_domain_id,
        monitor_id=monitor_id,
        update_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@monitor_group.command(name=cli_util.override('apm_synthetics.update_monitor_browser_monitor_configuration.command_name', 'update-monitor-browser-monitor-configuration'), help=u"""Updates the monitor. \n[Command Reference](updateMonitor)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--monitor-id', required=True, help=u"""The OCID of the monitor.""")
@cli_util.option('--display-name', help=u"""Unique name that can be edited. The name should not contain any confidential information.""")
@cli_util.option('--vantage-points', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of public and dedicated vantage points from which to execute the monitor. Use /publicVantagePoints to fetch public vantage points, and /dedicatedVantagePoints to fetch dedicated vantage points.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--script-id', help=u"""The [OCID] of the script. scriptId is mandatory for creation of SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ENABLED", "DISABLED", "INVALID"]), help=u"""Enables or disables the monitor.""")
@cli_util.option('--repeat-interval-in-seconds', type=click.INT, help=u"""Interval in seconds after the start time when the job should be repeated. Minimum repeatIntervalInSeconds should be 300 seconds for Scripted REST, Scripted Browser and Browser monitors, and 60 seconds for REST monitor.""")
@cli_util.option('--is-run-once', type=click.BOOL, help=u"""If runOnce is enabled, then the monitor will run once.""")
@cli_util.option('--timeout-in-seconds', type=click.INT, help=u"""Timeout in seconds. Timeout cannot be more than 30% of repeatIntervalInSeconds time for monitors. Also, timeoutInSeconds should be a multiple of 60 for Scripted REST, Scripted Browser and Browser monitors. Monitor will be allowed to run only for timeoutInSeconds time. It would be terminated after that.""")
@cli_util.option('--target', help=u"""Specify the endpoint on which to run the monitor. For BROWSER and REST monitor types, target is mandatory. If target is specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script (specified by scriptId in monitor) against the specified target endpoint. If target is not specified in the SCRIPTED_BROWSER monitor type, then the monitor will run the selected script as it is.""")
@cli_util.option('--script-parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of script parameters in the monitor. This is valid only for SCRIPTED_BROWSER and SCRIPTED_REST monitor types. For other monitor types, it should be set to null. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\"}]`

This option is a JSON list with items of type MonitorScriptParameter.  For documentation on MonitorScriptParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/MonitorScriptParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--configuration-is-failure-retried', type=click.BOOL, help=u"""If isFailureRetried is enabled, then a failed call will be retried.""")
@cli_util.option('--configuration-is-certificate-validation-enabled', type=click.BOOL, help=u"""If certificate validation is enabled, then the call will fail in case of certification errors.""")
@cli_util.option('--configuration-verify-texts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Verifies all the search strings present in the response. If any search string is not present in the response, then it will be considered as a failure.

This option is a JSON list with items of type VerifyText.  For documentation on VerifyText please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/VerifyText.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--configuration-network-configuration', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-verify-texts': {'module': 'apm_synthetics', 'class': 'list[VerifyText]'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'vantage-points': {'module': 'apm_synthetics', 'class': 'list[string]'}, 'script-parameters': {'module': 'apm_synthetics', 'class': 'list[MonitorScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}, 'configuration-verify-texts': {'module': 'apm_synthetics', 'class': 'list[VerifyText]'}, 'configuration-network-configuration': {'module': 'apm_synthetics', 'class': 'NetworkConfiguration'}}, output_type={'module': 'apm_synthetics', 'class': 'Monitor'})
@cli_util.wrap_exceptions
def update_monitor_browser_monitor_configuration(ctx, from_json, force, apm_domain_id, monitor_id, display_name, vantage_points, script_id, status, repeat_interval_in_seconds, is_run_once, timeout_in_seconds, target, script_parameters, freeform_tags, defined_tags, if_match, configuration_is_failure_retried, configuration_is_certificate_validation_enabled, configuration_verify_texts, configuration_network_configuration):

    if isinstance(monitor_id, six.string_types) and len(monitor_id.strip()) == 0:
        raise click.UsageError('Parameter --monitor-id cannot be whitespace or empty string')
    if not force:
        if vantage_points or script_parameters or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to vantage-points and script-parameters and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['configuration'] = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if vantage_points is not None:
        _details['vantagePoints'] = cli_util.parse_json_parameter("vantage_points", vantage_points)

    if script_id is not None:
        _details['scriptId'] = script_id

    if status is not None:
        _details['status'] = status

    if repeat_interval_in_seconds is not None:
        _details['repeatIntervalInSeconds'] = repeat_interval_in_seconds

    if is_run_once is not None:
        _details['isRunOnce'] = is_run_once

    if timeout_in_seconds is not None:
        _details['timeoutInSeconds'] = timeout_in_seconds

    if target is not None:
        _details['target'] = target

    if script_parameters is not None:
        _details['scriptParameters'] = cli_util.parse_json_parameter("script_parameters", script_parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if configuration_is_failure_retried is not None:
        _details['configuration']['isFailureRetried'] = configuration_is_failure_retried

    if configuration_is_certificate_validation_enabled is not None:
        _details['configuration']['isCertificateValidationEnabled'] = configuration_is_certificate_validation_enabled

    if configuration_verify_texts is not None:
        _details['configuration']['verifyTexts'] = cli_util.parse_json_parameter("configuration_verify_texts", configuration_verify_texts)

    if configuration_network_configuration is not None:
        _details['configuration']['networkConfiguration'] = cli_util.parse_json_parameter("configuration_network_configuration", configuration_network_configuration)

    _details['configuration']['configType'] = 'BROWSER_CONFIG'

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.update_monitor(
        apm_domain_id=apm_domain_id,
        monitor_id=monitor_id,
        update_monitor_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@script_group.command(name=cli_util.override('apm_synthetics.update_script.command_name', 'update'), help=u"""Updates the script. \n[Command Reference](updateScript)""")
@cli_util.option('--apm-domain-id', required=True, help=u"""The APM domain ID the request is intended for.""")
@cli_util.option('--script-id', required=True, help=u"""The OCID of the script.""")
@cli_util.option('--display-name', help=u"""Unique name that can be edited. The name should not contain any confidential information.""")
@cli_util.option('--content-type', type=custom_types.CliCaseInsensitiveChoice(["SIDE", "JS"]), help=u"""Content type of script.""")
@cli_util.option('--content', help=u"""The content of the script. It may contain custom-defined tags that can be used for setting dynamic parameters. The format to set dynamic parameters is: `<ORAP><ON>param name</ON><OV>param value</OV><OS>isParamValueSecret(true/false)</OS></ORAP>`. Param value and isParamValueSecret are optional, the default value for isParamValueSecret is false. Examples: With mandatory param name : `<ORAP><ON>param name</ON></ORAP>` With parameter name and value : `<ORAP><ON>param name</ON><OV>param value</OV></ORAP>` Note that the content is valid if it matches the given content type. For example, if the content type is SIDE, then the content should be in Side script format. If the content type is JS, then the content should be in JavaScript format.""")
@cli_util.option('--content-file-name', help=u"""File name of uploaded script content.""")
@cli_util.option('--parameters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of script parameters. Example: `[{\"paramName\": \"userid\", \"paramValue\":\"testuser\", \"isSecret\": false}]`

This option is a JSON list with items of type ScriptParameter.  For documentation on ScriptParameter please see our API reference: https://docs.cloud.oracle.com/api/#/en/apmsynthetic/20200630/datatypes/ScriptParameter.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'parameters': {'module': 'apm_synthetics', 'class': 'list[ScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'parameters': {'module': 'apm_synthetics', 'class': 'list[ScriptParameter]'}, 'freeform-tags': {'module': 'apm_synthetics', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'apm_synthetics', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'apm_synthetics', 'class': 'Script'})
@cli_util.wrap_exceptions
def update_script(ctx, from_json, force, apm_domain_id, script_id, display_name, content_type, content, content_file_name, parameters, freeform_tags, defined_tags, if_match):

    if isinstance(script_id, six.string_types) and len(script_id.strip()) == 0:
        raise click.UsageError('Parameter --script-id cannot be whitespace or empty string')
    if not force:
        if parameters or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to parameters and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if content_type is not None:
        _details['contentType'] = content_type

    if content is not None:
        _details['content'] = content

    if content_file_name is not None:
        _details['contentFileName'] = content_file_name

    if parameters is not None:
        _details['parameters'] = cli_util.parse_json_parameter("parameters", parameters)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('apm_synthetics', 'apm_synthetic', ctx)
    result = client.update_script(
        apm_domain_id=apm_domain_id,
        script_id=script_id,
        update_script_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
