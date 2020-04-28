# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
from services.waas.src.oci_cli_waas.generated import waas_cli
from .generated import waas_service_cli
from oci_cli import cli_util
from oci_cli import custom_types  # noqa: F401
import sys  # noqa: F401
import six  # noqa: F401
import oci  # noqa: F401
from oci_cli import json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias

# oci waas purge-cache purge-cache --waas-policy-id, --resources
# to
# oci waas purge-cache --waas-policy-id, --resources
waas_service_cli.waas_service_group.commands.pop(waas_cli.purge_cache_group.name)
waas_service_cli.waas_service_group.add_command(waas_cli.purge_cache)

# oci waas custom-protection-rule update-waas-policy --update-custom-protection-rules-details, --waas-policy-id
# to
# oci waas custom-protection-rule update-setting --custom-protection-rules-details, --waas-policy-id
# waas_cli.waas_root_group.commands.pop(waas_cli.custom_protection_rule_setting_group.name)

waas_cli.custom_protection_rule_group.commands.pop(waas_cli.update_waas_policy_custom_protection_rules.name)

# removing oci waas policy-config update-policy-config-sticky-cookie-load-balancing-method, update-policy-config-round-robin-load-balancing-method, policy-config update-policy-config-ip-hash-load-balancing-method
waas_cli.policy_config_group.commands.pop(waas_cli.update_policy_config_sticky_cookie_load_balancing_method.name)
waas_cli.policy_config_group.commands.pop(waas_cli.update_policy_config_round_robin_load_balancing_method.name)
waas_cli.policy_config_group.commands.pop(waas_cli.update_policy_config_ip_hash_load_balancing_method.name)


@cli_util.copy_params_from_generated_command(waas_cli.update_waas_policy_custom_protection_rules, params_to_exclude=['update_custom_protection_rules_details'])
@waas_cli.custom_protection_rule_group.command(name=cli_util.override('update_waas_policy_custom_protection_rules.command_name', 'update-setting'), help=waas_cli.update_waas_policy_custom_protection_rules.help)
@cli_util.option('--custom-protection-rules-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-protection-rules-details': {'module': 'waas', 'class': 'list[CustomProtectionRuleSetting]'}})
@cli_util.wrap_exceptions
def update_waas_policy_custom_protection_rules_extended(ctx, **kwargs):
    if 'custom_protection_rules_details' in kwargs:
        kwargs['update_custom_protection_rules_details'] = kwargs['custom_protection_rules_details']
        kwargs.pop('custom_protection_rules_details')
    ctx.invoke(waas_cli.update_waas_policy_custom_protection_rules, **kwargs)


# Adds commands to support Backward incompatible changes introduced by DEXREQ-829
# Update oci waas custom-protection-rule list-waas-policy to
# oci waas waas-policy custom-protection-rule list
@click.command(cli_util.override('waas.waas_policy_custom_protection_rule_group.command_name', 'waas-policy-custom-protection-rule'), cls=CommandGroupWithAlias, help="""Summary information about a Custom Protection rule.""")
@cli_util.help_option_group
# Create Dummy group
def waas_policy_custom_protection_rule_group():
    pass


waas_cli.custom_protection_rule_group.commands.pop(waas_cli.list_waas_policy_custom_protection_rules.name)
waas_policy_custom_protection_rule_group.add_command(waas_cli.list_waas_policy_custom_protection_rules)
cli_util.rename_command(waas_cli, waas_policy_custom_protection_rule_group, waas_cli.list_waas_policy_custom_protection_rules, 'list')
waas_cli.waas_policy_group.add_command(waas_policy_custom_protection_rule_group)
cli_util.rename_command(waas_cli, waas_cli.waas_policy_group, waas_policy_custom_protection_rule_group, "custom-protection-rule")


# Add update-address-list to certificate group
# This is to address backward in-compatible changes introduced by DEXREQ-829
@cli_util.copy_params_from_generated_command(waas_cli.update_address_list)
@waas_cli.certificate_group.command(name=cli_util.override('waas.certificate_group.update_address_list.command_name', 'update-address-list'), help="**Deprecated**, use oci waas address-list update command " + waas_cli.update_address_list.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'addresses': {'module': 'waas', 'class': 'list[string]'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'waas', 'class': 'AddressList'})
@cli_util.wrap_exceptions
def update_address_list_extended(ctx, **kwargs):
    ctx.invoke(waas_cli.update_address_list, **kwargs)


@cli_util.copy_params_from_generated_command(waas_cli.update_policy_config, params_to_exclude=['tls_protocols'])
@waas_cli.policy_config_group.command(name=cli_util.override('waas.update_policy_config.command_name', 'update'), help=waas_cli.update_policy_config.help)
@cli_util.option('--tls-protocols', type=custom_types.CliCaseInsensitiveChoice(["TLS_V1", "TLS_V1_1", "TLS_V1_2", "TLS_V1_3"]), multiple=True, help=u"""A list of allowed TLS protocols. Only applicable when HTTPS support is enabled. The TLS protocol is negotiated while the request is connecting and the most recent protocol supported by both the edge node and client browser will be selected. If no such version exists, the connection will be aborted. - **TLS_V1:** corresponds to TLS 1.0 specification.

- **TLS_V1_1:** corresponds to TLS 1.1 specification.

- **TLS_V1_2:** corresponds to TLS 1.2 specification.

- **TLS_V1_3:** corresponds to TLS 1.3 specification.

Enabled TLS protocols must go in a row. For example if `TLS_v1_1` and `TLS_V1_3` are enabled, `TLS_V1_2` must be enabled too.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'load-balancing-method': {'module': 'waas', 'class': 'LoadBalancingMethod'}, 'websocket-path-prefixes': {'module': 'waas', 'class': 'list[string]'}, 'health-checks': {'module': 'waas', 'class': 'HealthCheck'}})
@cli_util.wrap_exceptions
def update_policy_config(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, certificate_id, is_https_enabled, is_https_forced, tls_protocols, is_origin_compression_enabled, is_behind_cdn, client_address_header, is_cache_control_respected, is_response_buffering_enabled, cipher_group, load_balancing_method, websocket_path_prefixes, is_sni_enabled, health_checks, if_match):
    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')
    if not force:
        if tls_protocols or load_balancing_method or websocket_path_prefixes or health_checks:
            if not click.confirm("WARNING: Updates to tls-protocols, load-balancing-method, websocket-path-prefixes and health-checks will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if certificate_id is not None:
        details['certificateId'] = certificate_id

    if is_https_enabled is not None:
        details['isHttpsEnabled'] = is_https_enabled

    if is_https_forced is not None:
        details['isHttpsForced'] = is_https_forced

    if tls_protocols is not None and len(tls_protocols) > 0:
        print(tls_protocols)
        details['tlsProtocols'] = tls_protocols

    if is_origin_compression_enabled is not None:
        details['isOriginCompressionEnabled'] = is_origin_compression_enabled

    if is_behind_cdn is not None:
        details['isBehindCdn'] = is_behind_cdn

    if client_address_header is not None:
        details['clientAddressHeader'] = client_address_header

    if is_cache_control_respected is not None:
        details['isCacheControlRespected'] = is_cache_control_respected

    if is_response_buffering_enabled is not None:
        details['isResponseBufferingEnabled'] = is_response_buffering_enabled

    if cipher_group is not None:
        details['cipherGroup'] = cipher_group

    if load_balancing_method is not None:
        details['loadBalancingMethod'] = cli_util.parse_json_parameter("load_balancing_method", load_balancing_method)

    if websocket_path_prefixes is not None:
        details['websocketPathPrefixes'] = cli_util.parse_json_parameter("websocket_path_prefixes",
                                                                         websocket_path_prefixes)

    if is_sni_enabled is not None:
        details['isSniEnabled'] = is_sni_enabled

    if health_checks is not None:
        details['healthChecks'] = cli_util.parse_json_parameter("health_checks", health_checks)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_policy_config(
        waas_policy_id=waas_policy_id,
        update_policy_config_details=details,
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
