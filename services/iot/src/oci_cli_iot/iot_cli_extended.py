# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
import oci
import sys
from services.iot.src.oci_cli_iot.generated import iot_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci iot iot-domain-group configure-iot-domain-group-data-access -> oci iot iot-domain-group configure-data-access
cli_util.rename_command(iot_cli, iot_cli.iot_domain_group_group, iot_cli.configure_iot_domain_group_data_access, "configure-data-access")


# oci iot iot-domain change-iot-domain-data-retention-period -> oci iot iot-domain change-data-retention-period
cli_util.rename_command(iot_cli, iot_cli.iot_domain_group, iot_cli.change_iot_domain_data_retention_period, "change-data-retention-period")


# oci iot iot-domain configure-iot-domain-data-access-apex-data-access-details -> oci iot iot-domain configure-apex-data-access
cli_util.rename_command(iot_cli, iot_cli.iot_domain_group, iot_cli.configure_iot_domain_data_access_apex_data_access_details, "configure-apex-data-access")


# oci iot iot-domain configure-iot-domain-data-access-direct-data-access-details -> oci iot iot-domain configure-direct-data-access
cli_util.rename_command(iot_cli, iot_cli.iot_domain_group, iot_cli.configure_iot_domain_data_access_direct_data_access_details, "configure-direct-data-access")


# oci iot iot-domain configure-iot-domain-data-access-ords-data-access-details -> oci iot iot-domain configure-ords-data-access
cli_util.rename_command(iot_cli, iot_cli.iot_domain_group, iot_cli.configure_iot_domain_data_access_ords_data_access_details, "configure-ords-data-access")


# oci iot digital-twin-instance invoke-raw-command-invoke-raw-binary-command-details -> oci iot digital-twin-instance invoke-raw-binary-command
cli_util.rename_command(iot_cli, iot_cli.digital_twin_instance_group, iot_cli.invoke_raw_command_invoke_raw_binary_command_details, "invoke-raw-binary-command")


# oci iot digital-twin-instance invoke-raw-command-invoke-raw-json-command-details -> oci iot digital-twin-instance invoke-raw-json-command
cli_util.rename_command(iot_cli, iot_cli.digital_twin_instance_group, iot_cli.invoke_raw_command_invoke_raw_json_command_details, "invoke-raw-json-command")


# oci iot digital-twin-instance invoke-raw-command-invoke-raw-text-command-details -> oci iot digital-twin-instance invoke-raw-text-command
cli_util.rename_command(iot_cli, iot_cli.digital_twin_instance_group, iot_cli.invoke_raw_command_invoke_raw_text_command_details, "invoke-raw-text-command")


# oci iot digital-twin-model get-digital-twin-model-spec -> oci iot digital-twin-model get-spec
cli_util.rename_command(iot_cli, iot_cli.digital_twin_model_group, iot_cli.get_digital_twin_model_spec, "get-spec")


# oci iot digital-twin-instance get-digital-twin-instance-content -> oci iot digital-twin-instance get-content
cli_util.rename_command(iot_cli, iot_cli.digital_twin_instance_group, iot_cli.get_digital_twin_instance_content, "get-content")


# oci iot work-request list-work-request-errors -> oci iot work-request list-errors
cli_util.rename_command(iot_cli, iot_cli.work_request_group, iot_cli.list_work_request_errors, "list-errors")


# oci iot work-request list-work-request-logs -> oci iot work-request list-logs
cli_util.rename_command(iot_cli, iot_cli.work_request_group, iot_cli.list_work_request_logs, "list-logs")


# oci iot iot-domain -> oci iot domain
cli_util.rename_command(iot_cli, iot_cli.iot_root_group, iot_cli.iot_domain_group, "domain")


# oci iot iot-domain-group -> oci iot domain-group
cli_util.rename_command(iot_cli, iot_cli.iot_root_group, iot_cli.iot_domain_group_group, "domain-group")


# Remove configure-iot-domain-data-access from oci iot iot-domain
iot_cli.iot_domain_group.commands.pop(iot_cli.configure_iot_domain_data_access.name)


# Remove invoke-raw-command from oci iot digital-twin-instance
iot_cli.digital_twin_instance_group.commands.pop(iot_cli.invoke_raw_command.name)

# oci iot iot-flow-runtime -> oci iot flow-runtime
cli_util.rename_command(iot_cli, iot_cli.iot_root_group, iot_cli.iot_flow_runtime_group, "flow-runtime")


# oci iot flow-runtime deploy-iot-flow-runtime-flows -> oci iot flow-runtime update-flows
cli_util.rename_command(iot_cli, iot_cli.iot_flow_runtime_group, iot_cli.update_iot_flow_runtime_flows, "update-flows")


# oci iot flow-runtime get-iot-flow-runtime-flows -> oci iot flow-runtime get-flows
cli_util.rename_command(iot_cli, iot_cli.iot_flow_runtime_group, iot_cli.get_iot_flow_runtime_flows, "get-flows")


class NullableAuthId(click.types.StringParamType):

    def convert(self, value, param, ctx):
        value = super(NullableAuthId, self).convert(value, param, ctx)
        if isinstance(value, str) and value.lower() == 'null':
            return None
        return value


@cli_util.copy_params_from_generated_command(
    iot_cli.update_digital_twin_instance, params_to_exclude=['auth_id'])
@iot_cli.digital_twin_instance_group.command(
    name=iot_cli.update_digital_twin_instance.name,
    help=iot_cli.update_digital_twin_instance.help)
@cli_util.option(
    '--auth-id',
    type=NullableAuthId(),
    help='The OCID of the authentication resource. Specify null to clear the value.')
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={
        'gateways': {'module': 'iot', 'class': 'list[string]'},
        'freeform-tags': {'module': 'iot', 'class': 'dict(str, string)'},
        'defined-tags': {'module': 'iot', 'class': 'dict(str, dict(str, object))'}},
    output_type={'module': 'iot', 'class': 'DigitalTwinInstance'})
@cli_util.wrap_exceptions
def update_digital_twin_instance_extended(ctx, **kwargs):
    digital_twin_instance_id = kwargs['digital_twin_instance_id']
    if isinstance(digital_twin_instance_id, str) and not digital_twin_instance_id.strip():
        raise click.UsageError('Parameter --digital-twin-instance-id cannot be whitespace or empty string')

    if not kwargs['force'] and any(
            kwargs[name] for name in ('gateways', 'freeform_tags', 'defined_tags')):
        if not click.confirm(
                'WARNING: Updates to gateways and freeform-tags and defined-tags will replace any '
                'existing values. Are you sure you want to continue?'):
            ctx.abort()

    request_kwargs = {'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])}
    if kwargs['if_match'] is not None:
        request_kwargs['if_match'] = kwargs['if_match']

    details = {}
    scalar_fields = {
        'connectivity_type': 'connectivityType',
        'external_key': 'externalKey',
        'display_name': 'displayName',
        'description': 'description',
        'digital_twin_adapter_id': 'digitalTwinAdapterId',
        'digital_twin_model_id': 'digitalTwinModelId',
        'digital_twin_model_spec_uri': 'digitalTwinModelSpecUri'}
    for parameter_name, payload_name in scalar_fields.items():
        if kwargs[parameter_name] is not None:
            details[payload_name] = kwargs[parameter_name]

    # Preserve an explicitly supplied null (from --auth-id null or --from-json) while leaving an
    # omitted authId unchanged. This enables an atomic DIRECT -> INDIRECT transition.
    if ctx.get_parameter_source('auth_id') is not click.core.ParameterSource.DEFAULT:
        details['authId'] = kwargs['auth_id']

    for parameter_name, payload_name in (
            ('gateways', 'gateways'),
            ('freeform_tags', 'freeformTags'),
            ('defined_tags', 'definedTags')):
        if kwargs[parameter_name] is not None:
            details[payload_name] = cli_util.parse_json_parameter(parameter_name, kwargs[parameter_name])

    client = cli_util.build_client('iot', 'iot', ctx)
    result = client.update_digital_twin_instance(
        digital_twin_instance_id=digital_twin_instance_id,
        update_digital_twin_instance_details=details,
        **request_kwargs)

    if kwargs['wait_for_state']:
        if hasattr(client, 'get_digital_twin_instance') and callable(
                getattr(client, 'get_digital_twin_instance')):
            try:
                wait_period_kwargs = {}
                if kwargs['max_wait_seconds'] is not None:
                    wait_period_kwargs['max_wait_seconds'] = kwargs['max_wait_seconds']
                if kwargs['wait_interval_seconds'] is not None:
                    wait_period_kwargs['max_interval_seconds'] = kwargs['wait_interval_seconds']
                click.echo(
                    'Action completed. Waiting until the resource has entered state: {}'.format(
                        kwargs['wait_for_state']),
                    file=sys.stderr)
                result = oci.wait_until(
                    client,
                    client.get_digital_twin_instance(result.data.id),
                    'lifecycle_state',
                    kwargs['wait_for_state'],
                    **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded:
                click.echo(
                    'Failed to wait until the resource entered the specified state. '
                    'Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo(
                    'Encountered error while waiting for resource to enter the specified state. '
                    'Outputting last known resource state',
                    file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)

    cli_util.render_response(result, ctx)
