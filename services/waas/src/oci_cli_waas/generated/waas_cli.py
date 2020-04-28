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
from services.waas.src.oci_cli_waas.generated import waas_service_cli


@click.command(cli_util.override('waas.waas_root_group.command_name', 'waas'), cls=CommandGroupWithAlias, help=cli_util.override('waas.waas_root_group.help', """OCI Web Application Acceleration and Security Services"""), short_help=cli_util.override('waas.waas_root_group.short_help', """Web Application Acceleration and Security Services API"""))
@cli_util.help_option_group
def waas_root_group():
    pass


@click.command(cli_util.override('waas.waas_policy_group.command_name', 'waas-policy'), cls=CommandGroupWithAlias, help="""The details of a Web Application Acceleration and Security (WAAS) policy. A policy describes how the WAAS service should operate for the configured web application.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def waas_policy_group():
    pass


@click.command(cli_util.override('waas.access_rule_group.command_name', 'access-rule'), cls=CommandGroupWithAlias, help="""A content access rule. An access rule specifies an action to take if a set of criteria is matched by a request.""")
@cli_util.help_option_group
def access_rule_group():
    pass


@click.command(cli_util.override('waas.good_bot_group.command_name', 'good-bot'), cls=CommandGroupWithAlias, help="""The good bot settings. Good bots provides a list of bots which are managed by known providers.""")
@cli_util.help_option_group
def good_bot_group():
    pass


@click.command(cli_util.override('waas.threat_feed_group.command_name', 'threat-feed'), cls=CommandGroupWithAlias, help="""The settings of the threat intelligence feed. You can block requests from IP addresses based on their reputations with various commercial and open source threat feeds.""")
@cli_util.help_option_group
def threat_feed_group():
    pass


@click.command(cli_util.override('waas.waf_traffic_datum_group.command_name', 'waf-traffic-datum'), cls=CommandGroupWithAlias, help="""A time series of traffic data for the  Web Application Firewall configured for a policy.""")
@cli_util.help_option_group
def waf_traffic_datum_group():
    pass


@click.command(cli_util.override('waas.certificate_group.command_name', 'certificate'), cls=CommandGroupWithAlias, help="""The details of the SSL certificate. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def certificate_group():
    pass


@click.command(cli_util.override('waas.edge_subnet_group.command_name', 'edge-subnet'), cls=CommandGroupWithAlias, help="""The details about an edge node subnet.""")
@cli_util.help_option_group
def edge_subnet_group():
    pass


@click.command(cli_util.override('waas.recommendation_group.command_name', 'recommendation'), cls=CommandGroupWithAlias, help="""A recommended protection rule for a web application. This recommendation can be accepted to apply it to the Web Application Firewall configuration for this policy.

Use the `POST /waasPolicies/{waasPolicyId}/actions/acceptWafConfigRecommendations` method to accept recommended protection rules.""")
@cli_util.help_option_group
def recommendation_group():
    pass


@click.command(cli_util.override('waas.js_challenge_group.command_name', 'js-challenge'), cls=CommandGroupWithAlias, help="""The JavaScript challenge settings. JavaScript Challenge is the function to filter abnormal or malicious bots and allow access to real clients.""")
@cli_util.help_option_group
def js_challenge_group():
    pass


@click.command(cli_util.override('waas.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""Many of the API requests you use to create and configure WAAS policies do not take effect immediately. In these cases, the request spawns an asynchronous work flow to fulfill the request. `WorkRequest` objects provide visibility for in-progress work flows. For more information about work requests, see [Viewing the State of a Work Request].""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('waas.custom_protection_rule_group.command_name', 'custom-protection-rule'), cls=CommandGroupWithAlias, help="""The details of a custom protection rule.""")
@cli_util.help_option_group
def custom_protection_rule_group():
    pass


@click.command(cli_util.override('waas.address_rate_limiting_group.command_name', 'address-rate-limiting'), cls=CommandGroupWithAlias, help="""The IP rate limiting configuration. Defines the amount of allowed requests from a unique IP address and the resulting block response code when that threshold is exceeded.""")
@cli_util.help_option_group
def address_rate_limiting_group():
    pass


@click.command(cli_util.override('waas.captcha_group.command_name', 'captcha'), cls=CommandGroupWithAlias, help="""The settings of the CAPTCHA challenge. If a specific URL should be accessed only by a human, a CAPTCHA challenge can be placed at the URL to protect the web application from bots.

*Warning:* Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def captcha_group():
    pass


@click.command(cli_util.override('waas.waf_blocked_request_group.command_name', 'waf-blocked-request'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def waf_blocked_request_group():
    pass


@click.command(cli_util.override('waas.policy_config_group.command_name', 'policy-config'), cls=CommandGroupWithAlias, help="""The configuration details for the WAAS policy.""")
@cli_util.help_option_group
def policy_config_group():
    pass


@click.command(cli_util.override('waas.waf_request_group.command_name', 'waf-request'), cls=CommandGroupWithAlias, help="""A time series of request counts handled by the Web Application Firewall, including blocked requests.""")
@cli_util.help_option_group
def waf_request_group():
    pass


@click.command(cli_util.override('waas.protection_rule_group.command_name', 'protection-rule'), cls=CommandGroupWithAlias, help="""The protection rule settings. Protection rules can allow, block, or trigger an alert if a request meets the parameters of an applied rule.""")
@cli_util.help_option_group
def protection_rule_group():
    pass


@click.command(cli_util.override('waas.whitelist_group.command_name', 'whitelist'), cls=CommandGroupWithAlias, help="""An array of IP addresses that bypass the Web Application Firewall. Supports both single IP addresses or subnet masks (CIDR notation).""")
@cli_util.help_option_group
def whitelist_group():
    pass


@click.command(cli_util.override('waas.purge_cache_group.command_name', 'purge-cache'), cls=CommandGroupWithAlias, help="""The list of cached resources to purge. If a resource is not specified, the purge targets all rules in a policy.""")
@cli_util.help_option_group
def purge_cache_group():
    pass


@click.command(cli_util.override('waas.human_interaction_challenge_group.command_name', 'human-interaction-challenge'), cls=CommandGroupWithAlias, help="""The human interaction challenge settings. The human interaction challenge checks various event listeners in the user's browser to determine if there is a human user making a request.""")
@cli_util.help_option_group
def human_interaction_challenge_group():
    pass


@click.command(cli_util.override('waas.device_fingerprint_challenge_group.command_name', 'device-fingerprint-challenge'), cls=CommandGroupWithAlias, help="""The device fingerprint challenge settings. The device fingerprint challenge generates hashed signatures of both virtual and real browsers to identify and block malicious bots.""")
@cli_util.help_option_group
def device_fingerprint_challenge_group():
    pass


@click.command(cli_util.override('waas.address_list_group.command_name', 'address-list'), cls=CommandGroupWithAlias, help="""The details of the address list.""")
@cli_util.help_option_group
def address_list_group():
    pass


@click.command(cli_util.override('waas.waf_log_group.command_name', 'waf-log'), cls=CommandGroupWithAlias, help="""A list of Web Application Firewall log entries. Each entry is a JSON object, including a timestamp property and other fields varying based on log type. Logs record what rules and countermeasures are triggered by requests and are used as a basis to move request handling into block mode. For more information about WAF logs, see [Logs].""")
@cli_util.help_option_group
def waf_log_group():
    pass


@click.command(cli_util.override('waas.caching_rule_group.command_name', 'caching-rule'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def caching_rule_group():
    pass


@click.command(cli_util.override('waas.protection_settings_group.command_name', 'protection-settings'), cls=CommandGroupWithAlias, help="""The settings used for protection rules.""")
@cli_util.help_option_group
def protection_settings_group():
    pass


@click.command(cli_util.override('waas.waf_config_group.command_name', 'waf-config'), cls=CommandGroupWithAlias, help="""The Web Application Firewall configuration for the WAAS policy.""")
@cli_util.help_option_group
def waf_config_group():
    pass


waas_service_cli.waas_service_group.add_command(waas_root_group)
waas_root_group.add_command(waas_policy_group)
waas_root_group.add_command(access_rule_group)
waas_root_group.add_command(good_bot_group)
waas_root_group.add_command(threat_feed_group)
waas_root_group.add_command(waf_traffic_datum_group)
waas_root_group.add_command(certificate_group)
waas_root_group.add_command(edge_subnet_group)
waas_root_group.add_command(recommendation_group)
waas_root_group.add_command(js_challenge_group)
waas_root_group.add_command(work_request_group)
waas_root_group.add_command(custom_protection_rule_group)
waas_root_group.add_command(address_rate_limiting_group)
waas_root_group.add_command(captcha_group)
waas_root_group.add_command(waf_blocked_request_group)
waas_root_group.add_command(policy_config_group)
waas_root_group.add_command(waf_request_group)
waas_root_group.add_command(protection_rule_group)
waas_root_group.add_command(whitelist_group)
waas_root_group.add_command(purge_cache_group)
waas_root_group.add_command(human_interaction_challenge_group)
waas_root_group.add_command(device_fingerprint_challenge_group)
waas_root_group.add_command(address_list_group)
waas_root_group.add_command(waf_log_group)
waas_root_group.add_command(caching_rule_group)
waas_root_group.add_command(protection_settings_group)
waas_root_group.add_command(waf_config_group)
# oci waas waas --> oci waas
waas_service_cli.waas_service_group.commands.pop(waas_root_group.name)
waas_service_cli.waas_service_group.add_command(waas_policy_group)
waas_service_cli.waas_service_group.add_command(access_rule_group)
waas_service_cli.waas_service_group.add_command(good_bot_group)
waas_service_cli.waas_service_group.add_command(threat_feed_group)
waas_service_cli.waas_service_group.add_command(waf_traffic_datum_group)
waas_service_cli.waas_service_group.add_command(certificate_group)
waas_service_cli.waas_service_group.add_command(edge_subnet_group)
waas_service_cli.waas_service_group.add_command(recommendation_group)
waas_service_cli.waas_service_group.add_command(js_challenge_group)
waas_service_cli.waas_service_group.add_command(work_request_group)
waas_service_cli.waas_service_group.add_command(custom_protection_rule_group)
waas_service_cli.waas_service_group.add_command(address_rate_limiting_group)
waas_service_cli.waas_service_group.add_command(captcha_group)
waas_service_cli.waas_service_group.add_command(waf_blocked_request_group)
waas_service_cli.waas_service_group.add_command(policy_config_group)
waas_service_cli.waas_service_group.add_command(waf_request_group)
waas_service_cli.waas_service_group.add_command(protection_rule_group)
waas_service_cli.waas_service_group.add_command(whitelist_group)
waas_service_cli.waas_service_group.add_command(purge_cache_group)
waas_service_cli.waas_service_group.add_command(human_interaction_challenge_group)
waas_service_cli.waas_service_group.add_command(device_fingerprint_challenge_group)
waas_service_cli.waas_service_group.add_command(address_list_group)
waas_service_cli.waas_service_group.add_command(waf_log_group)
waas_service_cli.waas_service_group.add_command(caching_rule_group)
waas_service_cli.waas_service_group.add_command(protection_settings_group)
waas_service_cli.waas_service_group.add_command(waf_config_group)


@recommendation_group.command(name=cli_util.override('waas.accept_recommendations.command_name', 'accept'), help=u"""Accepts a list of recommended Web Application Firewall protection rules. Web Application Firewall protection rule recommendations are sets of rules generated by observed traffic patterns through the Web Application Firewall and are meant to optimize the Web Application Firewall's security profile. Only the rules specified in the request body will be updated; all other rules will remain unchanged.

Use the `GET /waasPolicies/{waasPolicyId}/wafConfig/recommendations` method to view a list of recommended Web Application Firewall protection rules. For more information, see [WAF Protection Rules].""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--protection-rule-keys', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'protection-rule-keys': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'protection-rule-keys': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def accept_recommendations(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, protection_rule_keys, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.accept_recommendations(
        waas_policy_id=waas_policy_id,
        protection_rule_keys=cli_util.parse_json_parameter("protection_rule_keys", protection_rule_keys),
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


@work_request_group.command(name=cli_util.override('waas.cancel_work_request.command_name', 'cancel'), help=u"""Cancels a specified work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request. This number is generated when work request is created.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_work_request(ctx, from_json, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@address_list_group.command(name=cli_util.override('waas.change_address_list_compartment.command_name', 'change-compartment'), help=u"""Moves address list into a different compartment. When provided, If-Match is checked against ETag values of the address list. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].""")
@cli_util.option('--address-list-id', required=True, help=u"""The [OCID] of the address list. This number is generated when the address list is added to the compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_address_list_compartment(ctx, from_json, address_list_id, compartment_id, if_match):

    if isinstance(address_list_id, six.string_types) and len(address_list_id.strip()) == 0:
        raise click.UsageError('Parameter --address-list-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.change_address_list_compartment(
        address_list_id=address_list_id,
        change_address_list_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('waas.change_certificate_compartment.command_name', 'change-compartment'), help=u"""Moves certificate into a different compartment. When provided, If-Match is checked against ETag values of the certificate. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].""")
@cli_util.option('--certificate-id', required=True, help=u"""The [OCID] of the SSL certificate used in the WAAS policy. This number is generated when the certificate is added to the policy.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_certificate_compartment(ctx, from_json, certificate_id, compartment_id, if_match):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.change_certificate_compartment(
        certificate_id=certificate_id,
        change_certificate_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@custom_protection_rule_group.command(name=cli_util.override('waas.change_custom_protection_rule_compartment.command_name', 'change-compartment'), help=u"""Moves a custom protection rule into a different compartment within the same tenancy. When provided, If-Match is checked against ETag values of the custom protection rule. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].""")
@cli_util.option('--custom-protection-rule-id', required=True, help=u"""The [OCID] of the custom protection rule. This number is generated when the custom protection rule is added to the compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_custom_protection_rule_compartment(ctx, from_json, custom_protection_rule_id, compartment_id, if_match):

    if isinstance(custom_protection_rule_id, six.string_types) and len(custom_protection_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --custom-protection-rule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.change_custom_protection_rule_compartment(
        custom_protection_rule_id=custom_protection_rule_id,
        change_custom_protection_rule_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@waas_policy_group.command(name=cli_util.override('waas.change_waas_policy_compartment.command_name', 'change-compartment'), help=u"""Moves WAAS policy into a different compartment. When provided, If-Match is checked against ETag values of the WAAS policy. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved. For information about moving resources between compartments, see [Moving Resources to a Different Compartment].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_waas_policy_compartment(ctx, from_json, waas_policy_id, compartment_id, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.change_waas_policy_compartment(
        waas_policy_id=waas_policy_id,
        change_waas_policy_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@address_list_group.command(name=cli_util.override('waas.create_address_list.command_name', 'create'), help=u"""Creates an address list in a set compartment and allows it to be used in a WAAS policy and referenced by access rules. Addresses can be IP addresses and CIDR notations.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to create the address list.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name for the address list.""")
@cli_util.option('--addresses', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of IP addresses or CIDR notations.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'addresses': {'module': 'waas', 'class': 'list[string]'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'addresses': {'module': 'waas', 'class': 'list[string]'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'waas', 'class': 'AddressList'})
@cli_util.wrap_exceptions
def create_address_list(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, addresses, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['addresses'] = cli_util.parse_json_parameter("addresses", addresses)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.create_address_list(
        create_address_list_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_address_list') and callable(getattr(client, 'get_address_list')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_address_list(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@certificate_group.command(name=cli_util.override('waas.create_certificate.command_name', 'create'), help=u"""Allows an SSL certificate to be added to a WAAS policy. The Web Application Firewall terminates SSL connections to inspect requests in runtime, and then re-encrypts requests before sending them to the origin for fulfillment.

For more information, see [WAF Settings].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to create the SSL certificate.""")
@cli_util.option('--certificate-data', required=True, help=u"""The data of the SSL certificate.

 **Note:** Many SSL certificate providers require an intermediate certificate chain to ensure a trusted status. If your SSL certificate requires an intermediate certificate chain, please append the intermediate certificate key in the `certificateData` field after the leaf certificate issued by the SSL certificate provider. If you are unsure if your certificate requires an intermediate certificate chain, see your certificate provider's documentation.

 The example below shows an intermediate certificate appended to a leaf certificate.""")
@cli_util.option('--private-key-data', required=True, help=u"""The private key of the SSL certificate.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the SSL certificate. The name can be changed and does not need to be unique.""")
@cli_util.option('--is-trust-verification-disabled', type=click.BOOL, help=u"""Set to `true` if the SSL certificate is self-signed.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'waas', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def create_certificate(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, certificate_data, private_key_data, display_name, is_trust_verification_disabled, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['certificateData'] = certificate_data
    _details['privateKeyData'] = private_key_data

    if display_name is not None:
        _details['displayName'] = display_name

    if is_trust_verification_disabled is not None:
        _details['isTrustVerificationDisabled'] = is_trust_verification_disabled

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.create_certificate(
        create_certificate_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate') and callable(getattr(client, 'get_certificate')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@custom_protection_rule_group.command(name=cli_util.override('waas.create_custom_protection_rule.command_name', 'create'), help=u"""Creates a new custom protection rule in the specified compartment.

Custom protection rules allow you to create rules in addition to the rulesets provided by the Web Application Firewall service, including rules from [ModSecurity]. The syntax for custom rules is based on the ModSecurity syntax. For more information about custom protection rules, see [Custom Protection Rules].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to create the custom protection rule.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name for the custom protection rule.""")
@cli_util.option('--template', required=True, help=u"""The template text of the custom protection rule. All custom protection rules are expressed in ModSecurity Rule Language.

Additionally, each rule must include two placeholder variables that are updated by the WAF service upon publication of the rule.

`id: {{id_1}}` - This field is populated with a unique rule ID generated by the WAF service which identifies a `SecRule`. More than one `SecRule` can be defined in the `template` field of a CreateCustomSecurityRule call. The value of the first `SecRule` must be `id: {{id_1}}` and the `id` field of each subsequent `SecRule` should increase by one, as shown in the example.

`ctl:ruleEngine={{mode}}` - The action to be taken when the criteria of the `SecRule` are met, either `OFF`, `DETECT` or `BLOCK`. This field is automatically populated with the corresponding value of the `action` field of the `CustomProtectionRuleSetting` schema when the `WafConfig` is updated.

*Example:*   ```   SecRule REQUEST_COOKIES \"regex matching SQL injection - part 1/2\" \\           \"phase:2,                                                 \\           msg:'Detects chained SQL injection attempts 1/2.',        \\           id: {{id_1}},                                             \\           ctl:ruleEngine={{mode}},                                  \\           deny\"   SecRule REQUEST_COOKIES \"regex matching SQL injection - part 2/2\" \\           \"phase:2,                                                 \\           msg:'Detects chained SQL injection attempts 2/2.',        \\           id: {{id_2}},                                             \\           ctl:ruleEngine={{mode}},                                  \\           deny\"   ```

 The example contains two `SecRules` each having distinct regex expression to match the `Cookie` header value during the second input analysis phase.

For more information about custom protection rules, see [Custom Protection Rules].

For more information about ModSecurity syntax, see [Making Rules: The Basic Syntax].

For more information about ModSecurity's open source WAF rules, see [Mod Security's OWASP Core Rule Set documentation].""")
@cli_util.option('--description', help=u"""A description for the Custom Protection rule.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'waas', 'class': 'CustomProtectionRule'})
@cli_util.wrap_exceptions
def create_custom_protection_rule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, template, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['template'] = template

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.create_custom_protection_rule(
        create_custom_protection_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_custom_protection_rule') and callable(getattr(client, 'get_custom_protection_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_custom_protection_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@waas_policy_group.command(name=cli_util.override('waas.create_waas_policy.command_name', 'create'), help=u"""Creates a new Web Application Acceleration and Security (WAAS) policy in the specified compartment. A WAAS policy must be established before creating Web Application Firewall (WAF) rules. To use WAF rules, your web application's origin servers must defined in the `WaasPolicy` schema.

A domain name must be specified when creating a WAAS policy. The domain name should be different from the origins specified in your `WaasPolicy`. Once domain name is entered and stored, it is unchangeable.

Use the record data returned in the `cname` field of the `WaasPolicy` object to create a CNAME record in your DNS configuration that will direct your domain's traffic through the WAF.

For the purposes of access control, you must provide the OCID of the compartment where you want the service to reside. For information about access control and compartments, see [Overview of the IAM Service].

You must specify a display name and domain for the WAAS policy. The display name does not have to be unique and can be changed. The domain name should be different from every origin specified in `WaasPolicy`.

All Oracle Cloud Infrastructure resources, including WAAS policies, receive a unique, Oracle-assigned ID called an Oracle Cloud Identifier (OCID). When a resource is created, you can find its OCID in the response. You can also retrieve a resource's OCID by using a list API operation for that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers].

**Note:** After sending the POST request, the new object's state will temporarily be `CREATING`. Ensure that the resource's state has changed to `ACTIVE` before use.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to create the WAAS policy.""")
@cli_util.option('--domain', required=True, help=u"""The web application domain that the WAAS policy protects.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the WAAS policy. The name can be changed and does not need to be unique.""")
@cli_util.option('--additional-domains', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of additional domains for the specified web application.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--origins', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.

This option is a JSON dictionary of type dict(str, Origin).  For documentation on Origin please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/Origin.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--origin-groups', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests. To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.

This option is a JSON dictionary of type dict(str, OriginGroup).  For documentation on OriginGroup please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/OriginGroup.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--policy-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--waf-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'additional-domains': {'module': 'waas', 'class': 'list[string]'}, 'origins': {'module': 'waas', 'class': 'dict(str, Origin)'}, 'origin-groups': {'module': 'waas', 'class': 'dict(str, OriginGroup)'}, 'policy-config': {'module': 'waas', 'class': 'PolicyConfig'}, 'waf-config': {'module': 'waas', 'class': 'WafConfigDetails'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'additional-domains': {'module': 'waas', 'class': 'list[string]'}, 'origins': {'module': 'waas', 'class': 'dict(str, Origin)'}, 'origin-groups': {'module': 'waas', 'class': 'dict(str, OriginGroup)'}, 'policy-config': {'module': 'waas', 'class': 'PolicyConfig'}, 'waf-config': {'module': 'waas', 'class': 'WafConfigDetails'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_waas_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, domain, display_name, additional_domains, origins, origin_groups, policy_config, waf_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['domain'] = domain

    if display_name is not None:
        _details['displayName'] = display_name

    if additional_domains is not None:
        _details['additionalDomains'] = cli_util.parse_json_parameter("additional_domains", additional_domains)

    if origins is not None:
        _details['origins'] = cli_util.parse_json_parameter("origins", origins)

    if origin_groups is not None:
        _details['originGroups'] = cli_util.parse_json_parameter("origin_groups", origin_groups)

    if policy_config is not None:
        _details['policyConfig'] = cli_util.parse_json_parameter("policy_config", policy_config)

    if waf_config is not None:
        _details['wafConfig'] = cli_util.parse_json_parameter("waf_config", waf_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.create_waas_policy(
        create_waas_policy_details=_details,
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


@address_list_group.command(name=cli_util.override('waas.delete_address_list.command_name', 'delete'), help=u"""Deletes the address list from the compartment if it is not used.""")
@cli_util.option('--address-list-id', required=True, help=u"""The [OCID] of the address list. This number is generated when the address list is added to the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_address_list(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, address_list_id, if_match):

    if isinstance(address_list_id, six.string_types) and len(address_list_id.strip()) == 0:
        raise click.UsageError('Parameter --address-list-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.delete_address_list(
        address_list_id=address_list_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_address_list') and callable(getattr(client, 'get_address_list')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_address_list(address_list_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@certificate_group.command(name=cli_util.override('waas.delete_certificate.command_name', 'delete'), help=u"""Deletes an SSL certificate from the WAAS service.""")
@cli_util.option('--certificate-id', required=True, help=u"""The [OCID] of the SSL certificate used in the WAAS policy. This number is generated when the certificate is added to the policy.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_certificate(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, certificate_id, if_match):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.delete_certificate(
        certificate_id=certificate_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate') and callable(getattr(client, 'get_certificate')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_certificate(certificate_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@custom_protection_rule_group.command(name=cli_util.override('waas.delete_custom_protection_rule.command_name', 'delete'), help=u"""Deletes a Custom Protection rule.""")
@cli_util.option('--custom-protection-rule-id', required=True, help=u"""The [OCID] of the custom protection rule. This number is generated when the custom protection rule is added to the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_custom_protection_rule(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, custom_protection_rule_id, if_match):

    if isinstance(custom_protection_rule_id, six.string_types) and len(custom_protection_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --custom-protection-rule-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.delete_custom_protection_rule(
        custom_protection_rule_id=custom_protection_rule_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_custom_protection_rule') and callable(getattr(client, 'get_custom_protection_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_custom_protection_rule(custom_protection_rule_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@waas_policy_group.command(name=cli_util.override('waas.delete_waas_policy.command_name', 'delete'), help=u"""Deletes a policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_waas_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.delete_waas_policy(
        waas_policy_id=waas_policy_id,
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


@address_list_group.command(name=cli_util.override('waas.get_address_list.command_name', 'get'), help=u"""Gets the details of an address list.""")
@cli_util.option('--address-list-id', required=True, help=u"""The [OCID] of the address list. This number is generated when the address list is added to the compartment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'AddressList'})
@cli_util.wrap_exceptions
def get_address_list(ctx, from_json, address_list_id):

    if isinstance(address_list_id, six.string_types) and len(address_list_id.strip()) == 0:
        raise click.UsageError('Parameter --address-list-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.get_address_list(
        address_list_id=address_list_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('waas.get_certificate.command_name', 'get'), help=u"""Gets the details of an SSL certificate.""")
@cli_util.option('--certificate-id', required=True, help=u"""The [OCID] of the SSL certificate used in the WAAS policy. This number is generated when the certificate is added to the policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def get_certificate(ctx, from_json, certificate_id):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.get_certificate(
        certificate_id=certificate_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@custom_protection_rule_group.command(name=cli_util.override('waas.get_custom_protection_rule.command_name', 'get'), help=u"""Gets the details of a custom protection rule.""")
@cli_util.option('--custom-protection-rule-id', required=True, help=u"""The [OCID] of the custom protection rule. This number is generated when the custom protection rule is added to the compartment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'CustomProtectionRule'})
@cli_util.wrap_exceptions
def get_custom_protection_rule(ctx, from_json, custom_protection_rule_id):

    if isinstance(custom_protection_rule_id, six.string_types) and len(custom_protection_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --custom-protection-rule-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.get_custom_protection_rule(
        custom_protection_rule_id=custom_protection_rule_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@device_fingerprint_challenge_group.command(name=cli_util.override('waas.get_device_fingerprint_challenge.command_name', 'get'), help=u"""Gets the device fingerprint challenge settings in the Web Application Firewall configuration for a WAAS policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'DeviceFingerprintChallenge'})
@cli_util.wrap_exceptions
def get_device_fingerprint_challenge(ctx, from_json, waas_policy_id):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.get_device_fingerprint_challenge(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@human_interaction_challenge_group.command(name=cli_util.override('waas.get_human_interaction_challenge.command_name', 'get'), help=u"""Gets the human interaction challenge settings in the Web Application Firewall configuration for a WAAS policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'HumanInteractionChallenge'})
@cli_util.wrap_exceptions
def get_human_interaction_challenge(ctx, from_json, waas_policy_id):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.get_human_interaction_challenge(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@js_challenge_group.command(name=cli_util.override('waas.get_js_challenge.command_name', 'get'), help=u"""Gets the JavaScript challenge settings in the Web Application Firewall configuration for a WAAS policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'JsChallenge'})
@cli_util.wrap_exceptions
def get_js_challenge(ctx, from_json, waas_policy_id):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.get_js_challenge(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@policy_config_group.command(name=cli_util.override('waas.get_policy_config.command_name', 'get'), help=u"""Gets the configuration of a WAAS policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'PolicyConfig'})
@cli_util.wrap_exceptions
def get_policy_config(ctx, from_json, waas_policy_id):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.get_policy_config(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@protection_rule_group.command(name=cli_util.override('waas.get_protection_rule.command_name', 'get'), help=u"""Gets the details of a protection rule in the Web Application Firewall configuration for a WAAS policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--protection-rule-key', required=True, help=u"""The protection rule key.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'ProtectionRule'})
@cli_util.wrap_exceptions
def get_protection_rule(ctx, from_json, waas_policy_id, protection_rule_key):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    if isinstance(protection_rule_key, six.string_types) and len(protection_rule_key.strip()) == 0:
        raise click.UsageError('Parameter --protection-rule-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.get_protection_rule(
        waas_policy_id=waas_policy_id,
        protection_rule_key=protection_rule_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@protection_settings_group.command(name=cli_util.override('waas.get_protection_settings.command_name', 'get'), help=u"""Gets the protection settings in the Web Application Firewall configuration for a WAAS policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'ProtectionSettings'})
@cli_util.wrap_exceptions
def get_protection_settings(ctx, from_json, waas_policy_id):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.get_protection_settings(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@waas_policy_group.command(name=cli_util.override('waas.get_waas_policy.command_name', 'get'), help=u"""Gets the details of a WAAS policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'WaasPolicy'})
@cli_util.wrap_exceptions
def get_waas_policy(ctx, from_json, waas_policy_id):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.get_waas_policy(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@address_rate_limiting_group.command(name=cli_util.override('waas.get_waf_address_rate_limiting.command_name', 'get-waf'), help=u"""Gets the address rate limiting settings of the Web Application Firewall configuration for a WAAS policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'AddressRateLimiting'})
@cli_util.wrap_exceptions
def get_waf_address_rate_limiting(ctx, from_json, waas_policy_id):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.get_waf_address_rate_limiting(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@waf_config_group.command(name=cli_util.override('waas.get_waf_config.command_name', 'get'), help=u"""Gets the Web Application Firewall configuration details for a WAAS policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'WafConfig'})
@cli_util.wrap_exceptions
def get_waf_config(ctx, from_json, waas_policy_id):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.get_waf_config(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('waas.get_work_request.command_name', 'get'), help=u"""Gets the details of a specified work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The [OCID] of the work request. This number is generated when work request is created.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@access_rule_group.command(name=cli_util.override('waas.list_access_rules.command_name', 'list'), help=u"""Gets the currently configured access rules for the Web Application Firewall configuration of a specified WAAS policy. The order of the access rules is important. The rules will be checked in the order they are specified and the first matching rule will be used.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[AccessRule]'})
@cli_util.wrap_exceptions
def list_access_rules(ctx, from_json, all_pages, page_size, waas_policy_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_access_rules,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_access_rules,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    else:
        result = client.list_access_rules(
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@address_list_group.command(name=cli_util.override('waas.list_address_lists.command_name', 'list'), help=u"""Gets a list of address lists that can be used in a WAAS policy.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment. This number is generated when the compartment is created.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "name", "timeCreated"]), help=u"""The value by which address lists are sorted in a paginated 'List' call. If unspecified, defaults to `timeCreated`.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.""")
@cli_util.option('--id', multiple=True, help=u"""Filter address lists using a list of address lists OCIDs.""")
@cli_util.option('--name', multiple=True, help=u"""Filter address lists using a list of names.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help=u"""Filter address lists using a list of lifecycle states.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that matches address lists created on or after the specified date-time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that matches address lists created before the specified date-time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'waas', 'class': 'list[string]'}, 'name': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'waas', 'class': 'list[string]'}, 'name': {'module': 'waas', 'class': 'list[string]'}}, output_type={'module': 'waas', 'class': 'list[AddressListSummary]'})
@cli_util.wrap_exceptions
def list_address_lists(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, id, name, lifecycle_state, time_created_greater_than_or_equal_to, time_created_less_than):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if name is not None and len(name) > 0:
        kwargs['name'] = name
    if lifecycle_state is not None and len(lifecycle_state) > 0:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if time_created_less_than is not None:
        kwargs['time_created_less_than'] = time_created_less_than
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_address_lists,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_address_lists,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_address_lists(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@caching_rule_group.command(name=cli_util.override('waas.list_caching_rules.command_name', 'list'), help=u"""Gets the currently configured caching rules for the Web Application Firewall configuration of a specified WAAS policy. The rules are processed in the order they are specified in and the first matching rule will be used when processing a request.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[CachingRuleSummary]'})
@cli_util.wrap_exceptions
def list_caching_rules(ctx, from_json, all_pages, page_size, waas_policy_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_caching_rules,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_caching_rules,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    else:
        result = client.list_caching_rules(
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@captcha_group.command(name=cli_util.override('waas.list_captchas.command_name', 'list'), help=u"""Gets the list of currently configured CAPTCHA challenges in the Web Application Firewall configuration of a WAAS policy.

The order of the CAPTCHA challenges is important. The URL for each CAPTCHA will be checked in the order they are created.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[Captcha]'})
@cli_util.wrap_exceptions
def list_captchas(ctx, from_json, all_pages, page_size, waas_policy_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_captchas,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_captchas,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    else:
        result = client.list_captchas(
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('waas.list_certificates.command_name', 'list'), help=u"""Gets a list of SSL certificates that can be used in a WAAS policy.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment. This number is generated when the compartment is created.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "compartmentId", "displayName", "notValidAfter", "timeCreated"]), help=u"""The value by which certificate summaries are sorted in a paginated 'List' call. If unspecified, defaults to `timeCreated`.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.""")
@cli_util.option('--id', multiple=True, help=u"""Filter certificates using a list of certificates OCIDs.""")
@cli_util.option('--display-name', multiple=True, help=u"""Filter certificates using a list of display names.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help=u"""Filter certificates using a list of lifecycle states.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that matches certificates created on or after the specified date-time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that matches certificates created before the specified date-time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'waas', 'class': 'list[string]'}, 'display-name': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'waas', 'class': 'list[string]'}, 'display-name': {'module': 'waas', 'class': 'list[string]'}}, output_type={'module': 'waas', 'class': 'list[CertificateSummary]'})
@cli_util.wrap_exceptions
def list_certificates(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, id, display_name, lifecycle_state, time_created_greater_than_or_equal_to, time_created_less_than):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if display_name is not None and len(display_name) > 0:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None and len(lifecycle_state) > 0:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if time_created_less_than is not None:
        kwargs['time_created_less_than'] = time_created_less_than
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_certificates,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_certificates,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_certificates(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@custom_protection_rule_group.command(name=cli_util.override('waas.list_custom_protection_rules.command_name', 'list'), help=u"""Gets a list of custom protection rules for the specified Web Application Firewall.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment. This number is generated when the compartment is created.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "compartmentId", "displayName", "modSecurityRuleId", "timeCreated"]), help=u"""The value by which custom protection rules are sorted in a paginated 'List' call. If unspecified, defaults to `timeCreated`.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.""")
@cli_util.option('--id', multiple=True, help=u"""Filter custom protection rules using a list of custom protection rule OCIDs.""")
@cli_util.option('--display-name', multiple=True, help=u"""Filter custom protection rules using a list of display names.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help=u"""Filter Custom Protection rules using a list of lifecycle states.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that matches Custom Protection rules created on or after the specified date-time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that matches custom protection rules created before the specified date-time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'waas', 'class': 'list[string]'}, 'display-name': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'waas', 'class': 'list[string]'}, 'display-name': {'module': 'waas', 'class': 'list[string]'}}, output_type={'module': 'waas', 'class': 'list[CustomProtectionRuleSummary]'})
@cli_util.wrap_exceptions
def list_custom_protection_rules(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, id, display_name, lifecycle_state, time_created_greater_than_or_equal_to, time_created_less_than):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if display_name is not None and len(display_name) > 0:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None and len(lifecycle_state) > 0:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if time_created_less_than is not None:
        kwargs['time_created_less_than'] = time_created_less_than
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_custom_protection_rules,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_custom_protection_rules,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_custom_protection_rules(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@edge_subnet_group.command(name=cli_util.override('waas.list_edge_subnets.command_name', 'list'), help=u"""Return the list of the tenant's edge node subnets. Use these CIDR blocks to restrict incoming traffic to your origin. These subnets are owned by OCI and forward traffic to customer origins. They are not associated with specific regions or compartments.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["cidr", "region", "timeModified"]), help=u"""The value by which edge node subnets are sorted in a paginated 'List' call. If unspecified, defaults to `timeModified`.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[EdgeSubnet]'})
@cli_util.wrap_exceptions
def list_edge_subnets(ctx, from_json, all_pages, page_size, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_edge_subnets,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_edge_subnets,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_edge_subnets(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@good_bot_group.command(name=cli_util.override('waas.list_good_bots.command_name', 'list'), help=u"""Gets the list of good bots defined in the Web Application Firewall configuration for a WAAS policy.

The list is sorted by `key`, in ascending order.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[GoodBot]'})
@cli_util.wrap_exceptions
def list_good_bots(ctx, from_json, all_pages, page_size, waas_policy_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_good_bots,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_good_bots,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    else:
        result = client.list_good_bots(
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@protection_rule_group.command(name=cli_util.override('waas.list_protection_rules.command_name', 'list'), help=u"""Gets the list of available protection rules for a WAAS policy. Use the `GetWafConfig` operation to view a list of currently configured protection rules for the Web Application Firewall, or use the `ListRecommendations` operation to get a list of recommended protection rules for the Web Application Firewall. The list is sorted by `key`, in ascending order.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--mod-security-rule-id', multiple=True, help=u"""Filter rules using a list of ModSecurity rule IDs.""")
@cli_util.option('--action', type=custom_types.CliCaseInsensitiveChoice(["OFF", "DETECT", "BLOCK"]), multiple=True, help=u"""Filter rules using a list of actions.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'mod-security-rule-id': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'mod-security-rule-id': {'module': 'waas', 'class': 'list[string]'}}, output_type={'module': 'waas', 'class': 'list[ProtectionRule]'})
@cli_util.wrap_exceptions
def list_protection_rules(ctx, from_json, all_pages, page_size, waas_policy_id, limit, page, mod_security_rule_id, action):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if mod_security_rule_id is not None and len(mod_security_rule_id) > 0:
        kwargs['mod_security_rule_id'] = mod_security_rule_id
    if action is not None and len(action) > 0:
        kwargs['action'] = action
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_protection_rules,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_protection_rules,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    else:
        result = client.list_protection_rules(
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@recommendation_group.command(name=cli_util.override('waas.list_recommendations.command_name', 'list'), help=u"""Gets the list of recommended Web Application Firewall protection rules.

Use the `POST /waasPolicies/{waasPolicyId}/actions/acceptWafConfigRecommendations` method to accept recommended Web Application Firewall protection rules. For more information, see [WAF Protection Rules]. The list is sorted by `key`, in ascending order.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--recommended-action', type=custom_types.CliCaseInsensitiveChoice(["DETECT", "BLOCK"]), help=u"""A filter that matches recommended protection rules based on the selected action. If unspecified, rules with any action type are returned.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[Recommendation]'})
@cli_util.wrap_exceptions
def list_recommendations(ctx, from_json, all_pages, page_size, waas_policy_id, recommended_action, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if recommended_action is not None:
        kwargs['recommended_action'] = recommended_action
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_recommendations,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_recommendations,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    else:
        result = client.list_recommendations(
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@threat_feed_group.command(name=cli_util.override('waas.list_threat_feeds.command_name', 'list'), help=u"""Gets the list of available web application threat intelligence feeds and the actions set for each feed. The list is sorted by `key`, in ascending order.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[ThreatFeed]'})
@cli_util.wrap_exceptions
def list_threat_feeds(ctx, from_json, all_pages, page_size, waas_policy_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_threat_feeds,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_threat_feeds,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    else:
        result = client.list_threat_feeds(
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@waas_policy_group.command(name=cli_util.override('waas.list_waas_policies.command_name', 'list'), help=u"""Gets a list of WAAS policies.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment. This number is generated when the compartment is created.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "displayName", "timeCreated"]), help=u"""The value by which policies are sorted in a paginated 'List' call.  If unspecified, defaults to `timeCreated`.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.""")
@cli_util.option('--id', multiple=True, help=u"""Filter policies using a list of policy OCIDs.""")
@cli_util.option('--display-name', multiple=True, help=u"""Filter policies using a list of display names.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help=u"""Filter policies using a list of lifecycle states.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that matches policies created on or after the specified date and time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that matches policies created before the specified date-time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'id': {'module': 'waas', 'class': 'list[string]'}, 'display-name': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'id': {'module': 'waas', 'class': 'list[string]'}, 'display-name': {'module': 'waas', 'class': 'list[string]'}}, output_type={'module': 'waas', 'class': 'list[WaasPolicySummary]'})
@cli_util.wrap_exceptions
def list_waas_policies(ctx, from_json, all_pages, page_size, compartment_id, limit, page, sort_by, sort_order, id, display_name, lifecycle_state, time_created_greater_than_or_equal_to, time_created_less_than):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if id is not None and len(id) > 0:
        kwargs['id'] = id
    if display_name is not None and len(display_name) > 0:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None and len(lifecycle_state) > 0:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if time_created_less_than is not None:
        kwargs['time_created_less_than'] = time_created_less_than
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_waas_policies,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_waas_policies,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_waas_policies(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@custom_protection_rule_group.command(name=cli_util.override('waas.list_waas_policy_custom_protection_rules.command_name', 'list-waas-policy'), help=u"""Gets the list of currently configured custom protection rules for a WAAS policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--mod-security-rule-id', multiple=True, help=u"""Filter rules using a list of ModSecurity rule IDs.""")
@cli_util.option('--action', type=custom_types.CliCaseInsensitiveChoice(["DETECT", "BLOCK"]), multiple=True, help=u"""Filter rules using a list of actions.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'mod-security-rule-id': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'mod-security-rule-id': {'module': 'waas', 'class': 'list[string]'}}, output_type={'module': 'waas', 'class': 'list[WaasPolicyCustomProtectionRuleSummary]'})
@cli_util.wrap_exceptions
def list_waas_policy_custom_protection_rules(ctx, from_json, all_pages, page_size, waas_policy_id, limit, page, mod_security_rule_id, action):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if mod_security_rule_id is not None and len(mod_security_rule_id) > 0:
        kwargs['mod_security_rule_id'] = mod_security_rule_id
    if action is not None and len(action) > 0:
        kwargs['action'] = action
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_waas_policy_custom_protection_rules,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_waas_policy_custom_protection_rules,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    else:
        result = client.list_waas_policy_custom_protection_rules(
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@waf_blocked_request_group.command(name=cli_util.override('waas.list_waf_blocked_requests.command_name', 'list'), help=u"""Gets the number of blocked requests by a Web Application Firewall feature in five minute blocks, sorted by `timeObserved` in ascending order (starting from oldest data).""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--time-observed-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that limits returned events to those occurring on or after a date and time, specified in RFC 3339 format. If unspecified, defaults to 30 minutes before receipt of the request.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-observed-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that limits returned events to those occurring before a date and time, specified in RFC 3339 format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--waf-feature', type=custom_types.CliCaseInsensitiveChoice(["PROTECTION_RULES", "JS_CHALLENGE", "ACCESS_RULES", "THREAT_FEEDS", "HUMAN_INTERACTION_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "CAPTCHA", "ADDRESS_RATE_LIMITING"]), multiple=True, help=u"""Filter stats by the Web Application Firewall feature that triggered the block action. If unspecified, data for all WAF features will be returned.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[WafBlockedRequest]'})
@cli_util.wrap_exceptions
def list_waf_blocked_requests(ctx, from_json, all_pages, page_size, waas_policy_id, time_observed_greater_than_or_equal_to, time_observed_less_than, limit, page, waf_feature):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if time_observed_greater_than_or_equal_to is not None:
        kwargs['time_observed_greater_than_or_equal_to'] = time_observed_greater_than_or_equal_to
    if time_observed_less_than is not None:
        kwargs['time_observed_less_than'] = time_observed_less_than
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if waf_feature is not None and len(waf_feature) > 0:
        kwargs['waf_feature'] = waf_feature
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_waf_blocked_requests,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_waf_blocked_requests,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    else:
        result = client.list_waf_blocked_requests(
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@waf_log_group.command(name=cli_util.override('waas.list_waf_logs.command_name', 'list'), help=u"""Gets structured Web Application Firewall event logs for a WAAS policy. Sorted by the `timeObserved` in ascending order (starting from the oldest recorded event).""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `20`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--time-observed-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that matches log entries where the observed event occurred on or after a date and time specified in RFC 3339 format. If unspecified, defaults to two hours before receipt of the request.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-observed-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that matches log entries where the observed event occurred before a date and time, specified in RFC 3339 format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--text-contains', help=u"""A full text search for logs.""")
@cli_util.option('--access-rule-key', multiple=True, help=u"""Filters logs by access rule key.""")
@cli_util.option('--action', type=custom_types.CliCaseInsensitiveChoice(["BLOCK", "DETECT", "BYPASS", "LOG", "REDIRECTED"]), multiple=True, help=u"""Filters logs by Web Application Firewall action.""")
@cli_util.option('--client-address', multiple=True, help=u"""Filters logs by client IP address.""")
@cli_util.option('--country-code', multiple=True, help=u"""Filters logs by country code. Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see [ISO's website].""")
@cli_util.option('--country-name', multiple=True, help=u"""Filter logs by country name.""")
@cli_util.option('--fingerprint', multiple=True, help=u"""Filter logs by device fingerprint.""")
@cli_util.option('--http-method', type=custom_types.CliCaseInsensitiveChoice(["OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT"]), multiple=True, help=u"""Filter logs by HTTP method.""")
@cli_util.option('--incident-key', multiple=True, help=u"""Filter logs by incident key.""")
@cli_util.option('--log-type', type=custom_types.CliCaseInsensitiveChoice(["ACCESS", "PROTECTION_RULES", "JS_CHALLENGE", "CAPTCHA", "ACCESS_RULES", "THREAT_FEEDS", "HUMAN_INTERACTION_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "ADDRESS_RATE_LIMITING"]), multiple=True, help=u"""Filter by log type. For more information about WAF logs, see [Logs].""")
@cli_util.option('--origin-address', multiple=True, help=u"""Filter by origin IP address.""")
@cli_util.option('--referrer', multiple=True, help=u"""Filter by referrer.""")
@cli_util.option('--request-url', multiple=True, help=u"""Filter by request URL.""")
@cli_util.option('--response-code', multiple=True, help=u"""Filter by response code.""")
@cli_util.option('--threat-feed-key', multiple=True, help=u"""Filter by threat feed key.""")
@cli_util.option('--user-agent', multiple=True, help=u"""Filter by user agent.""")
@cli_util.option('--protection-rule-key', multiple=True, help=u"""Filter by protection rule key.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({'access-rule-key': {'module': 'waas', 'class': 'list[string]'}, 'client-address': {'module': 'waas', 'class': 'list[string]'}, 'country-code': {'module': 'waas', 'class': 'list[string]'}, 'country-name': {'module': 'waas', 'class': 'list[string]'}, 'fingerprint': {'module': 'waas', 'class': 'list[string]'}, 'incident-key': {'module': 'waas', 'class': 'list[string]'}, 'origin-address': {'module': 'waas', 'class': 'list[string]'}, 'referrer': {'module': 'waas', 'class': 'list[string]'}, 'request-url': {'module': 'waas', 'class': 'list[string]'}, 'response-code': {'module': 'waas', 'class': 'list[integer]'}, 'threat-feed-key': {'module': 'waas', 'class': 'list[string]'}, 'user-agent': {'module': 'waas', 'class': 'list[string]'}, 'protection-rule-key': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'access-rule-key': {'module': 'waas', 'class': 'list[string]'}, 'client-address': {'module': 'waas', 'class': 'list[string]'}, 'country-code': {'module': 'waas', 'class': 'list[string]'}, 'country-name': {'module': 'waas', 'class': 'list[string]'}, 'fingerprint': {'module': 'waas', 'class': 'list[string]'}, 'incident-key': {'module': 'waas', 'class': 'list[string]'}, 'origin-address': {'module': 'waas', 'class': 'list[string]'}, 'referrer': {'module': 'waas', 'class': 'list[string]'}, 'request-url': {'module': 'waas', 'class': 'list[string]'}, 'response-code': {'module': 'waas', 'class': 'list[integer]'}, 'threat-feed-key': {'module': 'waas', 'class': 'list[string]'}, 'user-agent': {'module': 'waas', 'class': 'list[string]'}, 'protection-rule-key': {'module': 'waas', 'class': 'list[string]'}}, output_type={'module': 'waas', 'class': 'list[WafLog]'})
@cli_util.wrap_exceptions
def list_waf_logs(ctx, from_json, all_pages, page_size, waas_policy_id, limit, page, time_observed_greater_than_or_equal_to, time_observed_less_than, text_contains, access_rule_key, action, client_address, country_code, country_name, fingerprint, http_method, incident_key, log_type, origin_address, referrer, request_url, response_code, threat_feed_key, user_agent, protection_rule_key):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if time_observed_greater_than_or_equal_to is not None:
        kwargs['time_observed_greater_than_or_equal_to'] = time_observed_greater_than_or_equal_to
    if time_observed_less_than is not None:
        kwargs['time_observed_less_than'] = time_observed_less_than
    if text_contains is not None:
        kwargs['text_contains'] = text_contains
    if access_rule_key is not None and len(access_rule_key) > 0:
        kwargs['access_rule_key'] = access_rule_key
    if action is not None and len(action) > 0:
        kwargs['action'] = action
    if client_address is not None and len(client_address) > 0:
        kwargs['client_address'] = client_address
    if country_code is not None and len(country_code) > 0:
        kwargs['country_code'] = country_code
    if country_name is not None and len(country_name) > 0:
        kwargs['country_name'] = country_name
    if fingerprint is not None and len(fingerprint) > 0:
        kwargs['fingerprint'] = fingerprint
    if http_method is not None and len(http_method) > 0:
        kwargs['http_method'] = http_method
    if incident_key is not None and len(incident_key) > 0:
        kwargs['incident_key'] = incident_key
    if log_type is not None and len(log_type) > 0:
        kwargs['log_type'] = log_type
    if origin_address is not None and len(origin_address) > 0:
        kwargs['origin_address'] = origin_address
    if referrer is not None and len(referrer) > 0:
        kwargs['referrer'] = referrer
    if request_url is not None and len(request_url) > 0:
        kwargs['request_url'] = request_url
    if response_code is not None and len(response_code) > 0:
        kwargs['response_code'] = response_code
    if threat_feed_key is not None and len(threat_feed_key) > 0:
        kwargs['threat_feed_key'] = threat_feed_key
    if user_agent is not None and len(user_agent) > 0:
        kwargs['user_agent'] = user_agent
    if protection_rule_key is not None and len(protection_rule_key) > 0:
        kwargs['protection_rule_key'] = protection_rule_key
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_waf_logs,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_waf_logs,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    else:
        result = client.list_waf_logs(
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@waf_request_group.command(name=cli_util.override('waas.list_waf_requests.command_name', 'list'), help=u"""Gets the number of requests managed by a Web Application Firewall over a specified period of time, including blocked requests. Sorted by `timeObserved` in ascending order (starting from oldest requests).""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--time-observed-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that limits returned events to those occurring on or after a date and time, specified in RFC 3339 format. If unspecified, defaults to 30 minutes before receipt of the request.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-observed-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that limits returned events to those occurring before a date and time, specified in RFC 3339 format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[WafRequest]'})
@cli_util.wrap_exceptions
def list_waf_requests(ctx, from_json, all_pages, page_size, waas_policy_id, time_observed_greater_than_or_equal_to, time_observed_less_than, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if time_observed_greater_than_or_equal_to is not None:
        kwargs['time_observed_greater_than_or_equal_to'] = time_observed_greater_than_or_equal_to
    if time_observed_less_than is not None:
        kwargs['time_observed_less_than'] = time_observed_less_than
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_waf_requests,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_waf_requests,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    else:
        result = client.list_waf_requests(
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@waf_traffic_datum_group.command(name=cli_util.override('waas.list_waf_traffic.command_name', 'list-waf-traffic'), help=u"""Gets the Web Application Firewall traffic data for a WAAS policy. Sorted by `timeObserved` in ascending order (starting from oldest data).""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--time-observed-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that limits returned events to those occurring on or after a date and time, specified in RFC 3339 format. If unspecified, defaults to 30 minutes before receipt of the request.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-observed-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that limits returned events to those occurring before a date and time, specified in RFC 3339 format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[WafTrafficDatum]'})
@cli_util.wrap_exceptions
def list_waf_traffic(ctx, from_json, all_pages, page_size, waas_policy_id, time_observed_greater_than_or_equal_to, time_observed_less_than, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if time_observed_greater_than_or_equal_to is not None:
        kwargs['time_observed_greater_than_or_equal_to'] = time_observed_greater_than_or_equal_to
    if time_observed_less_than is not None:
        kwargs['time_observed_less_than'] = time_observed_less_than
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_waf_traffic,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_waf_traffic,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    else:
        result = client.list_waf_traffic(
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@whitelist_group.command(name=cli_util.override('waas.list_whitelists.command_name', 'list'), help=u"""Gets the list of whitelists defined in the Web Application Firewall configuration for a WAAS policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[Whitelist]'})
@cli_util.wrap_exceptions
def list_whitelists(ctx, from_json, all_pages, page_size, waas_policy_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_whitelists,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_whitelists,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    else:
        result = client.list_whitelists(
            waas_policy_id=waas_policy_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('waas.list_work_requests.command_name', 'list'), help=u"""Gets a list of subnets (CIDR notation) from which the WAAS EDGE may make requests. The subnets are owned by OCI and forward traffic to your origins. Allow traffic from these subnets to your origins. They are not associated with specific regions or compartments.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the policy.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment. This number is generated when the compartment is created.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "status", "timeAccepted", "timeStarted", "timeFinished", "operationType"]), help=u"""The value by which work requests are sorted in a paginated 'List' call. If unspecified, defaults to `timeAccepted`.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, waas_policy_id, compartment_id, limit, page, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            waas_policy_id=waas_policy_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            waas_policy_id=waas_policy_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            waas_policy_id=waas_policy_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@purge_cache_group.command(name=cli_util.override('waas.purge_cache.command_name', 'purge-cache'), help=u"""Performs a purge of the cache for each specified resource. If no resources are passed, the cache for the entire Web Application Firewall will be purged. For more information, see [Caching Rules].""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--resources', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A resource to purge, specified by either a hostless absolute path starting with a single slash (Example: `/path/to/resource`) or by a relative path in which the first component will be interpreted as a domain protected by the WAAS policy (Example: `example.com/path/to/resource`).""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'resources': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'resources': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def purge_cache(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, if_match, resources):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if resources is not None:
        _details['resources'] = cli_util.parse_json_parameter("resources", resources)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.purge_cache(
        waas_policy_id=waas_policy_id,
        purge_cache=_details,
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


@access_rule_group.command(name=cli_util.override('waas.update_access_rules.command_name', 'update'), help=u"""Updates the list of access rules in the Web Application Firewall configuration for a specified WAAS policy. Access rules allow explicit actions to be defined and executed for requests that meet various conditions. A rule action can be set to allow, detect, or block requests. The detect setting allows the request to pass through the Web Application Firewall and is tagged with a `DETECT` flag in the Web Application Firewall's log.

This operation can create, delete, update, and/or reorder access rules depending on the structure of the request body.

Access rules can be updated by changing the properties of the access rule object with the rule's key specified in the key field. Access rules can be reordered by changing the order of the access rules in the list when updating.

Access rules can be created by adding a new access rule object to the list without a `key` property specified. A `key` will be generated for the new access rule upon update.

Any existing access rules that are not specified with a `key` in the list of access rules will be deleted upon update.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--access-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'access-rules': {'module': 'waas', 'class': 'list[AccessRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'access-rules': {'module': 'waas', 'class': 'list[AccessRule]'}})
@cli_util.wrap_exceptions
def update_access_rules(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, access_rules, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_access_rules(
        waas_policy_id=waas_policy_id,
        access_rules=cli_util.parse_json_parameter("access_rules", access_rules),
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


@address_list_group.command(name=cli_util.override('waas.update_address_list.command_name', 'update'), help=u"""Updates the details of an address list. Only the fields specified in the request body will be updated; all other properties will remain unchanged.""")
@cli_util.option('--address-list-id', required=True, help=u"""The [OCID] of the address list. This number is generated when the address list is added to the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the address list.""")
@cli_util.option('--addresses', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of IP addresses or CIDR notations.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'addresses': {'module': 'waas', 'class': 'list[string]'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'addresses': {'module': 'waas', 'class': 'list[string]'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'waas', 'class': 'AddressList'})
@cli_util.wrap_exceptions
def update_address_list(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, address_list_id, if_match, display_name, addresses, freeform_tags, defined_tags):

    if isinstance(address_list_id, six.string_types) and len(address_list_id.strip()) == 0:
        raise click.UsageError('Parameter --address-list-id cannot be whitespace or empty string')
    if not force:
        if addresses or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to addresses and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if addresses is not None:
        _details['addresses'] = cli_util.parse_json_parameter("addresses", addresses)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_address_list(
        address_list_id=address_list_id,
        update_address_list_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_address_list') and callable(getattr(client, 'get_address_list')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_address_list(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@caching_rule_group.command(name=cli_util.override('waas.update_caching_rules.command_name', 'update'), help=u"""Updates the configuration for each specified caching rule.

Caching rules WAF policies allow you to selectively cache content on Oracle Cloud Infrastructure's edge servers, such as webpages or certain file types. For more information about caching rules, see [Caching Rules].

This operation can create, delete, update, and/or reorder caching rules depending on the structure of the request body. Caching rules can be updated by changing the properties of the caching rule object with the rule's key specified in the key field. Any existing caching rules that are not specified with a key in the list of access rules will be deleted upon update.

The order the caching rules are specified in is important. The rules are processed in the order they are specified and the first matching rule will be used when processing a request. Use `ListCachingRules` to view a list of all available caching rules in a compartment.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--caching-rules-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'caching-rules-details': {'module': 'waas', 'class': 'list[CachingRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'caching-rules-details': {'module': 'waas', 'class': 'list[CachingRule]'}})
@cli_util.wrap_exceptions
def update_caching_rules(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, caching_rules_details, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_caching_rules(
        waas_policy_id=waas_policy_id,
        caching_rules_details=cli_util.parse_json_parameter("caching_rules_details", caching_rules_details),
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


@captcha_group.command(name=cli_util.override('waas.update_captchas.command_name', 'update'), help=u"""Updates the list of CAPTCHA challenges in the Web Application Firewall configuration for a WAAS policy. This operation can create, update, or delete CAPTCHAs depending on the structure of the request body. CAPTCHA challenges can be updated by changing the properties of the CAPTCHA object with the rule's key specified in the key field. CAPTCHA challenges can be reordered by changing the order of the CAPTCHA challenges in the list when updating.

CAPTCHA challenges can be created by adding a new access rule object to the list without a `key` property specified. A `key` will be generated for the new CAPTCHA challenges upon update.

Any existing CAPTCHA challenges that are not specified with a `key` in the list of CAPTCHA challenges will be deleted upon update.

Query parameters are allowed in CAPTCHA URL.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--captchas', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of CAPTCHA details.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'captchas': {'module': 'waas', 'class': 'list[Captcha]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'captchas': {'module': 'waas', 'class': 'list[Captcha]'}})
@cli_util.wrap_exceptions
def update_captchas(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, captchas, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_captchas(
        waas_policy_id=waas_policy_id,
        captchas=cli_util.parse_json_parameter("captchas", captchas),
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


@certificate_group.command(name=cli_util.override('waas.update_certificate.command_name', 'update'), help=u"""It is not possible to update a certificate, only create and delete. Therefore, this operation can only update the display name, freeform tags, and defined tags of a certificate.""")
@cli_util.option('--certificate-id', required=True, help=u"""The [OCID] of the SSL certificate used in the WAAS policy. This number is generated when the certificate is added to the policy.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the SSL certificate. The name can be changed and does not need to be unique.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'waas', 'class': 'Certificate'})
@cli_util.wrap_exceptions
def update_certificate(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, certificate_id, if_match, display_name, freeform_tags, defined_tags):

    if isinstance(certificate_id, six.string_types) and len(certificate_id.strip()) == 0:
        raise click.UsageError('Parameter --certificate-id cannot be whitespace or empty string')
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

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_certificate(
        certificate_id=certificate_id,
        update_certificate_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_certificate') and callable(getattr(client, 'get_certificate')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_certificate(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@custom_protection_rule_group.command(name=cli_util.override('waas.update_custom_protection_rule.command_name', 'update'), help=u"""Updates the configuration of a custom protection rule. Only the fields specified in the request body will be updated; all other properties will remain unchanged.""")
@cli_util.option('--custom-protection-rule-id', required=True, help=u"""The [OCID] of the custom protection rule. This number is generated when the custom protection rule is added to the compartment.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the custom protection rule.""")
@cli_util.option('--description', help=u"""A description for the custom protection rule.""")
@cli_util.option('--template', help=u"""The template text of the custom protection rule. All custom protection rules are expressed in ModSecurity Rule Language.

Additionally, each rule must include two placeholder variables that are updated by the WAF service upon publication of the rule.

`id: {{id_1}}` - This field is populated with a unique rule ID generated by the WAF service which identifies a `SecRule`. More than one `SecRule` can be defined in the `template` field of a CreateCustomSecurityRule call. The value of the first `SecRule` must be `id: {{id_1}}` and the `id` field of each subsequent `SecRule` should increase by one, as shown in the example.

`ctl:ruleEngine={{mode}}` - The action to be taken when the criteria of the `SecRule` are met, either `OFF`, `DETECT` or `BLOCK`. This field is automatically populated with the corresponding value of the `action` field of the `CustomProtectionRuleSetting` schema when the `WafConfig` is updated.

*Example:*   ```   SecRule REQUEST_COOKIES \"regex matching SQL injection - part 1/2\" \\           \"phase:2,                                                 \\           msg:'Detects chained SQL injection attempts 1/2.',        \\           id: {{id_1}},                                             \\           ctl:ruleEngine={{mode}},                                  \\           deny\"   SecRule REQUEST_COOKIES \"regex matching SQL injection - part 2/2\" \\           \"phase:2,                                                 \\           msg:'Detects chained SQL injection attempts 2/2.',        \\           id: {{id_2}},                                             \\           ctl:ruleEngine={{mode}},                                  \\           deny\"   ```

 The example contains two `SecRules` each having distinct regex expression to match the `Cookie` header value during the second input analysis phase.

For more information about custom protection rules, see [Custom Protection Rules].

For more information about ModSecurity syntax, see [Making Rules: The Basic Syntax].

For more information about ModSecurity's open source WAF rules, see [Mod Security's OWASP Core Rule Set documentation].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'waas', 'class': 'CustomProtectionRule'})
@cli_util.wrap_exceptions
def update_custom_protection_rule(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, custom_protection_rule_id, display_name, description, template, freeform_tags, defined_tags, if_match):

    if isinstance(custom_protection_rule_id, six.string_types) and len(custom_protection_rule_id.strip()) == 0:
        raise click.UsageError('Parameter --custom-protection-rule-id cannot be whitespace or empty string')
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

    if template is not None:
        _details['template'] = template

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_custom_protection_rule(
        custom_protection_rule_id=custom_protection_rule_id,
        update_custom_protection_rule_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_custom_protection_rule') and callable(getattr(client, 'get_custom_protection_rule')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_custom_protection_rule(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@device_fingerprint_challenge_group.command(name=cli_util.override('waas.update_device_fingerprint_challenge.command_name', 'update'), help=u"""Updates the Device Fingerprint Challenge (DFC) settings in the Web Application Firewall configuration for a policy. The DFC generates a hashed signature of both virtual and real browsers based on 50+ attributes. These proprietary signatures are then leveraged for real-time correlation to identify and block malicious bots.

The signature is based on a library of attributes detected via JavaScript listeners; the attributes include OS, screen resolution, fonts, UserAgent, IP address, etc. We are constantly making improvements and considering new libraries to include in our DFC build. We can also exclude attributes from the signature as needed.

DFC collects attributes to generate a hashed signature about a client - if a fingerprint is not possible, then it will result in a block or alert action. Actions can be enforced across multiple devices if they share they have the same fingerprint.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Enables or disables the device fingerprint challenge Web Application Firewall feature.""")
@cli_util.option('--action', type=custom_types.CliCaseInsensitiveChoice(["DETECT", "BLOCK"]), help=u"""The action to take on requests from detected bots. If unspecified, defaults to `DETECT`.""")
@cli_util.option('--failure-threshold', type=click.INT, help=u"""The number of failed requests allowed before taking action. If unspecified, defaults to `10`.""")
@cli_util.option('--action-expiration-in-seconds', type=click.INT, help=u"""The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.""")
@cli_util.option('--failure-threshold-expiration-in-seconds', type=click.INT, help=u"""The number of seconds before the failure threshold resets. If unspecified, defaults to `60`.""")
@cli_util.option('--max-address-count', type=click.INT, help=u"""The maximum number of IP addresses permitted with the same device fingerprint. If unspecified, defaults to `20`.""")
@cli_util.option('--max-address-count-expiration-in-seconds', type=click.INT, help=u"""The number of seconds before the maximum addresses count resets. If unspecified, defaults to `60`.""")
@cli_util.option('--challenge-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'challenge-settings': {'module': 'waas', 'class': 'BlockChallengeSettings'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'challenge-settings': {'module': 'waas', 'class': 'BlockChallengeSettings'}})
@cli_util.wrap_exceptions
def update_device_fingerprint_challenge(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, is_enabled, action, failure_threshold, action_expiration_in_seconds, failure_threshold_expiration_in_seconds, max_address_count, max_address_count_expiration_in_seconds, challenge_settings, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')
    if not force:
        if challenge_settings:
            if not click.confirm("WARNING: Updates to challenge-settings will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['isEnabled'] = is_enabled

    if action is not None:
        _details['action'] = action

    if failure_threshold is not None:
        _details['failureThreshold'] = failure_threshold

    if action_expiration_in_seconds is not None:
        _details['actionExpirationInSeconds'] = action_expiration_in_seconds

    if failure_threshold_expiration_in_seconds is not None:
        _details['failureThresholdExpirationInSeconds'] = failure_threshold_expiration_in_seconds

    if max_address_count is not None:
        _details['maxAddressCount'] = max_address_count

    if max_address_count_expiration_in_seconds is not None:
        _details['maxAddressCountExpirationInSeconds'] = max_address_count_expiration_in_seconds

    if challenge_settings is not None:
        _details['challengeSettings'] = cli_util.parse_json_parameter("challenge_settings", challenge_settings)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_device_fingerprint_challenge(
        waas_policy_id=waas_policy_id,
        update_device_fingerprint_challenge_details=_details,
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


@good_bot_group.command(name=cli_util.override('waas.update_good_bots.command_name', 'update'), help=u"""Updates the list of good bots in the Web Application Firewall configuration for a policy. Only the fields specified in the request body will be updated, all other configuration properties will remain unchanged.

Good bots allows you to manage access for bots from known providers, such as Google or Baidu. For more information about good bots, see [Bot Management].""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--good-bots', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'good-bots': {'module': 'waas', 'class': 'list[GoodBot]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'good-bots': {'module': 'waas', 'class': 'list[GoodBot]'}})
@cli_util.wrap_exceptions
def update_good_bots(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, good_bots, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_good_bots(
        waas_policy_id=waas_policy_id,
        good_bots=cli_util.parse_json_parameter("good_bots", good_bots),
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


@human_interaction_challenge_group.command(name=cli_util.override('waas.update_human_interaction_challenge.command_name', 'update'), help=u"""Updates the Human Interaction Challenge (HIC) settings in the Web Application Firewall configuration for a WAAS policy. HIC is a countermeasure that allows the proxy to check the user's browser for various behaviors that distinguish a human presence from a bot.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Enables or disables the human interaction challenge Web Application Firewall feature.""")
@cli_util.option('--action', type=custom_types.CliCaseInsensitiveChoice(["DETECT", "BLOCK"]), help=u"""The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.""")
@cli_util.option('--failure-threshold', type=click.INT, help=u"""The number of failed requests before taking action. If unspecified, defaults to `10`.""")
@cli_util.option('--action-expiration-in-seconds', type=click.INT, help=u"""The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.""")
@cli_util.option('--failure-threshold-expiration-in-seconds', type=click.INT, help=u"""The number of seconds before the failure threshold resets. If unspecified, defaults to  `60`.""")
@cli_util.option('--interaction-threshold', type=click.INT, help=u"""The number of interactions required to pass the challenge. If unspecified, defaults to `3`.""")
@cli_util.option('--recording-period-in-seconds', type=click.INT, help=u"""The number of seconds to record the interactions from the user. If unspecified, defaults to `15`.""")
@cli_util.option('--set-http-header', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set to `DETECT`.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--challenge-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-nat-enabled', type=click.BOOL, help=u"""When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking visitors with shared IP addresses.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'set-http-header': {'module': 'waas', 'class': 'Header'}, 'challenge-settings': {'module': 'waas', 'class': 'BlockChallengeSettings'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'set-http-header': {'module': 'waas', 'class': 'Header'}, 'challenge-settings': {'module': 'waas', 'class': 'BlockChallengeSettings'}})
@cli_util.wrap_exceptions
def update_human_interaction_challenge(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, is_enabled, action, failure_threshold, action_expiration_in_seconds, failure_threshold_expiration_in_seconds, interaction_threshold, recording_period_in_seconds, set_http_header, challenge_settings, is_nat_enabled, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')
    if not force:
        if set_http_header or challenge_settings:
            if not click.confirm("WARNING: Updates to set-http-header and challenge-settings will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['isEnabled'] = is_enabled

    if action is not None:
        _details['action'] = action

    if failure_threshold is not None:
        _details['failureThreshold'] = failure_threshold

    if action_expiration_in_seconds is not None:
        _details['actionExpirationInSeconds'] = action_expiration_in_seconds

    if failure_threshold_expiration_in_seconds is not None:
        _details['failureThresholdExpirationInSeconds'] = failure_threshold_expiration_in_seconds

    if interaction_threshold is not None:
        _details['interactionThreshold'] = interaction_threshold

    if recording_period_in_seconds is not None:
        _details['recordingPeriodInSeconds'] = recording_period_in_seconds

    if set_http_header is not None:
        _details['setHttpHeader'] = cli_util.parse_json_parameter("set_http_header", set_http_header)

    if challenge_settings is not None:
        _details['challengeSettings'] = cli_util.parse_json_parameter("challenge_settings", challenge_settings)

    if is_nat_enabled is not None:
        _details['isNatEnabled'] = is_nat_enabled

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_human_interaction_challenge(
        waas_policy_id=waas_policy_id,
        update_human_interaction_challenge_details=_details,
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


@js_challenge_group.command(name=cli_util.override('waas.update_js_challenge.command_name', 'update'), help=u"""Updates the JavaScript challenge settings in the Web Application Firewall configuration for a WAAS policy. JavaScript Challenge validates that the client can accept JavaScript with a binary decision. For more information, see [Bot Management].""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Enables or disables the JavaScript challenge Web Application Firewall feature.""")
@cli_util.option('--action', type=custom_types.CliCaseInsensitiveChoice(["DETECT", "BLOCK"]), help=u"""The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.""")
@cli_util.option('--failure-threshold', type=click.INT, help=u"""The number of failed requests before taking action. If unspecified, defaults to `10`.""")
@cli_util.option('--action-expiration-in-seconds', type=click.INT, help=u"""The number of seconds between challenges from the same IP address. If unspecified, defaults to `60`.""")
@cli_util.option('--set-http-header', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set to `DETECT`.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--challenge-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--are-redirects-challenged', type=click.BOOL, help=u"""When enabled, redirect responses from the origin will also be challenged. This will change HTTP 301/302 responses from origin to HTTP 200 with an HTML body containing JavaScript page redirection.""")
@cli_util.option('--criteria', type=custom_types.CLI_COMPLEX_TYPE, help=u"""When defined, the JavaScript Challenge would be applied only for the requests that matched all the listed conditions.

This option is a JSON list with items of type AccessRuleCriteria.  For documentation on AccessRuleCriteria please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/AccessRuleCriteria.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-nat-enabled', type=click.BOOL, help=u"""When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking visitors with shared IP addresses.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'set-http-header': {'module': 'waas', 'class': 'Header'}, 'challenge-settings': {'module': 'waas', 'class': 'BlockChallengeSettings'}, 'criteria': {'module': 'waas', 'class': 'list[AccessRuleCriteria]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'set-http-header': {'module': 'waas', 'class': 'Header'}, 'challenge-settings': {'module': 'waas', 'class': 'BlockChallengeSettings'}, 'criteria': {'module': 'waas', 'class': 'list[AccessRuleCriteria]'}})
@cli_util.wrap_exceptions
def update_js_challenge(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, is_enabled, action, failure_threshold, action_expiration_in_seconds, set_http_header, challenge_settings, are_redirects_challenged, criteria, is_nat_enabled, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')
    if not force:
        if set_http_header or challenge_settings or criteria:
            if not click.confirm("WARNING: Updates to set-http-header and challenge-settings and criteria will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['isEnabled'] = is_enabled

    if action is not None:
        _details['action'] = action

    if failure_threshold is not None:
        _details['failureThreshold'] = failure_threshold

    if action_expiration_in_seconds is not None:
        _details['actionExpirationInSeconds'] = action_expiration_in_seconds

    if set_http_header is not None:
        _details['setHttpHeader'] = cli_util.parse_json_parameter("set_http_header", set_http_header)

    if challenge_settings is not None:
        _details['challengeSettings'] = cli_util.parse_json_parameter("challenge_settings", challenge_settings)

    if are_redirects_challenged is not None:
        _details['areRedirectsChallenged'] = are_redirects_challenged

    if criteria is not None:
        _details['criteria'] = cli_util.parse_json_parameter("criteria", criteria)

    if is_nat_enabled is not None:
        _details['isNatEnabled'] = is_nat_enabled

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_js_challenge(
        waas_policy_id=waas_policy_id,
        update_js_challenge_details=_details,
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


@policy_config_group.command(name=cli_util.override('waas.update_policy_config.command_name', 'update'), help=u"""Updates the configuration for a WAAS policy. Only the fields specified in the request body will be updated; all other properties will remain unchanged.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--certificate-id', help=u"""The OCID of the SSL certificate to use if HTTPS is supported.""")
@cli_util.option('--is-https-enabled', type=click.BOOL, help=u"""Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.""")
@cli_util.option('--is-https-forced', type=click.BOOL, help=u"""Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.""")
@cli_util.option('--tls-protocols', type=custom_types.CliCaseInsensitiveChoice(["TLS_V1", "TLS_V1_1", "TLS_V1_2", "TLS_V1_3"]), help=u"""A list of allowed TLS protocols. Only applicable when HTTPS support is enabled. The TLS protocol is negotiated while the request is connecting and the most recent protocol supported by both the edge node and client browser will be selected. If no such version exists, the connection will be aborted. - **TLS_V1:** corresponds to TLS 1.0 specification.

- **TLS_V1_1:** corresponds to TLS 1.1 specification.

- **TLS_V1_2:** corresponds to TLS 1.2 specification.

- **TLS_V1_3:** corresponds to TLS 1.3 specification.

Enabled TLS protocols must go in a row. For example if `TLS_v1_1` and `TLS_V1_3` are enabled, `TLS_V1_2` must be enabled too.""")
@cli_util.option('--is-origin-compression-enabled', type=click.BOOL, help=u"""Enable or disable GZIP compression of origin responses. If enabled, the header `Accept-Encoding: gzip` is sent to origin, otherwise, the empty `Accept-Encoding:` header is used.""")
@cli_util.option('--is-behind-cdn', type=click.BOOL, help=u"""Enabling `isBehindCdn` allows for the collection of IP addresses from client requests if the WAF is connected to a CDN.""")
@cli_util.option('--client-address-header', type=custom_types.CliCaseInsensitiveChoice(["X_FORWARDED_FOR", "X_CLIENT_IP", "X_REAL_IP", "CLIENT_IP", "TRUE_CLIENT_IP"]), help=u"""Specifies an HTTP header name which is treated as the connecting client's IP address. Applicable only if `isBehindCdn` is enabled.

The edge node reads this header and its value and sets the client IP address as specified. It does not create the header if the header is not present in the request. If the header is not present, the connecting IP address will be used as the client's true IP address. It uses the last IP address in the header's value as the true IP address.

Example: `X-Client-Ip: 11.1.1.1, 13.3.3.3`

In the case of multiple headers with the same name, only the first header will be used. It is assumed that CDN sets the correct client IP address to prevent spoofing.

- **X_FORWARDED_FOR:** Corresponds to `X-Forwarded-For` header name.

- **X_CLIENT_IP:** Corresponds to `X-Client-Ip` header name.

- **X_REAL_IP:** Corresponds to `X-Real-Ip` header name.

- **CLIENT_IP:** Corresponds to `Client-Ip` header name.

- **TRUE_CLIENT_IP:** Corresponds to `True-Client-Ip` header name.""")
@cli_util.option('--is-cache-control-respected', type=click.BOOL, help=u"""Enable or disable automatic content caching based on the response `cache-control` header. This feature enables the origin to act as a proxy cache. Caching is usually defined using `cache-control` header. For example `cache-control: max-age=120` means that the returned resource is valid for 120 seconds. Caching rules will overwrite this setting.""")
@cli_util.option('--is-response-buffering-enabled', type=click.BOOL, help=u"""Enable or disable buffering of responses from the origin. Buffering improves overall stability in case of network issues, but slightly increases Time To First Byte.""")
@cli_util.option('--cipher-group', type=custom_types.CliCaseInsensitiveChoice(["DEFAULT"]), help=u"""The set cipher group for the configured TLS protocol. This sets the configuration for the TLS connections between clients and edge nodes only. - **DEFAULT:** Cipher group supports TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 protocols. It has the following ciphers enabled: `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:!DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA`""")
@cli_util.option('--load-balancing-method', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An object that represents a load balancing method and its properties.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--websocket-path-prefixes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""ModSecurity is not capable to inspect WebSockets. Therefore paths specified here have WAF disabled if Connection request header from the client has the value Upgrade (case insensitive matching) and Upgrade request header has the value websocket (case insensitive matching). Paths matches if the concatenation of request URL path and query starts with the contents of the one of `websocketPathPrefixes` array value. In All other cases challenges, like JSC, HIC and etc., remain active.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-sni-enabled', type=click.BOOL, help=u"""SNI stands for Server Name Indication and is an extension of the TLS protocol. It indicates which hostname is being contacted by the browser at the beginning of the 'handshake'-process. This allows a server to connect multiple SSL Certificates to one IP address and port.""")
@cli_util.option('--health-checks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'load-balancing-method': {'module': 'waas', 'class': 'LoadBalancingMethod'}, 'websocket-path-prefixes': {'module': 'waas', 'class': 'list[string]'}, 'health-checks': {'module': 'waas', 'class': 'HealthCheck'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'load-balancing-method': {'module': 'waas', 'class': 'LoadBalancingMethod'}, 'websocket-path-prefixes': {'module': 'waas', 'class': 'list[string]'}, 'health-checks': {'module': 'waas', 'class': 'HealthCheck'}})
@cli_util.wrap_exceptions
def update_policy_config(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, certificate_id, is_https_enabled, is_https_forced, tls_protocols, is_origin_compression_enabled, is_behind_cdn, client_address_header, is_cache_control_respected, is_response_buffering_enabled, cipher_group, load_balancing_method, websocket_path_prefixes, is_sni_enabled, health_checks, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')
    if not force:
        if tls_protocols or load_balancing_method or websocket_path_prefixes or health_checks:
            if not click.confirm("WARNING: Updates to tls-protocols and load-balancing-method and websocket-path-prefixes and health-checks will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if certificate_id is not None:
        _details['certificateId'] = certificate_id

    if is_https_enabled is not None:
        _details['isHttpsEnabled'] = is_https_enabled

    if is_https_forced is not None:
        _details['isHttpsForced'] = is_https_forced

    if tls_protocols is not None:
        _details['tlsProtocols'] = cli_util.parse_json_parameter("tls_protocols", tls_protocols)

    if is_origin_compression_enabled is not None:
        _details['isOriginCompressionEnabled'] = is_origin_compression_enabled

    if is_behind_cdn is not None:
        _details['isBehindCdn'] = is_behind_cdn

    if client_address_header is not None:
        _details['clientAddressHeader'] = client_address_header

    if is_cache_control_respected is not None:
        _details['isCacheControlRespected'] = is_cache_control_respected

    if is_response_buffering_enabled is not None:
        _details['isResponseBufferingEnabled'] = is_response_buffering_enabled

    if cipher_group is not None:
        _details['cipherGroup'] = cipher_group

    if load_balancing_method is not None:
        _details['loadBalancingMethod'] = cli_util.parse_json_parameter("load_balancing_method", load_balancing_method)

    if websocket_path_prefixes is not None:
        _details['websocketPathPrefixes'] = cli_util.parse_json_parameter("websocket_path_prefixes", websocket_path_prefixes)

    if is_sni_enabled is not None:
        _details['isSniEnabled'] = is_sni_enabled

    if health_checks is not None:
        _details['healthChecks'] = cli_util.parse_json_parameter("health_checks", health_checks)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_policy_config(
        waas_policy_id=waas_policy_id,
        update_policy_config_details=_details,
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


@policy_config_group.command(name=cli_util.override('waas.update_policy_config_round_robin_load_balancing_method.command_name', 'update-policy-config-round-robin-load-balancing-method'), help=u"""Updates the configuration for a WAAS policy. Only the fields specified in the request body will be updated; all other properties will remain unchanged.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--certificate-id', help=u"""The OCID of the SSL certificate to use if HTTPS is supported.""")
@cli_util.option('--is-https-enabled', type=click.BOOL, help=u"""Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.""")
@cli_util.option('--is-https-forced', type=click.BOOL, help=u"""Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.""")
@cli_util.option('--tls-protocols', type=custom_types.CliCaseInsensitiveChoice(["TLS_V1", "TLS_V1_1", "TLS_V1_2", "TLS_V1_3"]), help=u"""A list of allowed TLS protocols. Only applicable when HTTPS support is enabled. The TLS protocol is negotiated while the request is connecting and the most recent protocol supported by both the edge node and client browser will be selected. If no such version exists, the connection will be aborted. - **TLS_V1:** corresponds to TLS 1.0 specification.

- **TLS_V1_1:** corresponds to TLS 1.1 specification.

- **TLS_V1_2:** corresponds to TLS 1.2 specification.

- **TLS_V1_3:** corresponds to TLS 1.3 specification.

Enabled TLS protocols must go in a row. For example if `TLS_v1_1` and `TLS_V1_3` are enabled, `TLS_V1_2` must be enabled too.""")
@cli_util.option('--is-origin-compression-enabled', type=click.BOOL, help=u"""Enable or disable GZIP compression of origin responses. If enabled, the header `Accept-Encoding: gzip` is sent to origin, otherwise, the empty `Accept-Encoding:` header is used.""")
@cli_util.option('--is-behind-cdn', type=click.BOOL, help=u"""Enabling `isBehindCdn` allows for the collection of IP addresses from client requests if the WAF is connected to a CDN.""")
@cli_util.option('--client-address-header', type=custom_types.CliCaseInsensitiveChoice(["X_FORWARDED_FOR", "X_CLIENT_IP", "X_REAL_IP", "CLIENT_IP", "TRUE_CLIENT_IP"]), help=u"""Specifies an HTTP header name which is treated as the connecting client's IP address. Applicable only if `isBehindCdn` is enabled.

The edge node reads this header and its value and sets the client IP address as specified. It does not create the header if the header is not present in the request. If the header is not present, the connecting IP address will be used as the client's true IP address. It uses the last IP address in the header's value as the true IP address.

Example: `X-Client-Ip: 11.1.1.1, 13.3.3.3`

In the case of multiple headers with the same name, only the first header will be used. It is assumed that CDN sets the correct client IP address to prevent spoofing.

- **X_FORWARDED_FOR:** Corresponds to `X-Forwarded-For` header name.

- **X_CLIENT_IP:** Corresponds to `X-Client-Ip` header name.

- **X_REAL_IP:** Corresponds to `X-Real-Ip` header name.

- **CLIENT_IP:** Corresponds to `Client-Ip` header name.

- **TRUE_CLIENT_IP:** Corresponds to `True-Client-Ip` header name.""")
@cli_util.option('--is-cache-control-respected', type=click.BOOL, help=u"""Enable or disable automatic content caching based on the response `cache-control` header. This feature enables the origin to act as a proxy cache. Caching is usually defined using `cache-control` header. For example `cache-control: max-age=120` means that the returned resource is valid for 120 seconds. Caching rules will overwrite this setting.""")
@cli_util.option('--is-response-buffering-enabled', type=click.BOOL, help=u"""Enable or disable buffering of responses from the origin. Buffering improves overall stability in case of network issues, but slightly increases Time To First Byte.""")
@cli_util.option('--cipher-group', type=custom_types.CliCaseInsensitiveChoice(["DEFAULT"]), help=u"""The set cipher group for the configured TLS protocol. This sets the configuration for the TLS connections between clients and edge nodes only. - **DEFAULT:** Cipher group supports TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 protocols. It has the following ciphers enabled: `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:!DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA`""")
@cli_util.option('--websocket-path-prefixes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""ModSecurity is not capable to inspect WebSockets. Therefore paths specified here have WAF disabled if Connection request header from the client has the value Upgrade (case insensitive matching) and Upgrade request header has the value websocket (case insensitive matching). Paths matches if the concatenation of request URL path and query starts with the contents of the one of `websocketPathPrefixes` array value. In All other cases challenges, like JSC, HIC and etc., remain active.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-sni-enabled', type=click.BOOL, help=u"""SNI stands for Server Name Indication and is an extension of the TLS protocol. It indicates which hostname is being contacted by the browser at the beginning of the 'handshake'-process. This allows a server to connect multiple SSL Certificates to one IP address and port.""")
@cli_util.option('--health-checks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'websocket-path-prefixes': {'module': 'waas', 'class': 'list[string]'}, 'health-checks': {'module': 'waas', 'class': 'HealthCheck'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'websocket-path-prefixes': {'module': 'waas', 'class': 'list[string]'}, 'health-checks': {'module': 'waas', 'class': 'HealthCheck'}})
@cli_util.wrap_exceptions
def update_policy_config_round_robin_load_balancing_method(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, certificate_id, is_https_enabled, is_https_forced, tls_protocols, is_origin_compression_enabled, is_behind_cdn, client_address_header, is_cache_control_respected, is_response_buffering_enabled, cipher_group, websocket_path_prefixes, is_sni_enabled, health_checks, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')
    if not force:
        if tls_protocols or websocket_path_prefixes or health_checks:
            if not click.confirm("WARNING: Updates to tls-protocols and websocket-path-prefixes and health-checks will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['loadBalancingMethod'] = {}

    if certificate_id is not None:
        _details['certificateId'] = certificate_id

    if is_https_enabled is not None:
        _details['isHttpsEnabled'] = is_https_enabled

    if is_https_forced is not None:
        _details['isHttpsForced'] = is_https_forced

    if tls_protocols is not None:
        _details['tlsProtocols'] = cli_util.parse_json_parameter("tls_protocols", tls_protocols)

    if is_origin_compression_enabled is not None:
        _details['isOriginCompressionEnabled'] = is_origin_compression_enabled

    if is_behind_cdn is not None:
        _details['isBehindCdn'] = is_behind_cdn

    if client_address_header is not None:
        _details['clientAddressHeader'] = client_address_header

    if is_cache_control_respected is not None:
        _details['isCacheControlRespected'] = is_cache_control_respected

    if is_response_buffering_enabled is not None:
        _details['isResponseBufferingEnabled'] = is_response_buffering_enabled

    if cipher_group is not None:
        _details['cipherGroup'] = cipher_group

    if websocket_path_prefixes is not None:
        _details['websocketPathPrefixes'] = cli_util.parse_json_parameter("websocket_path_prefixes", websocket_path_prefixes)

    if is_sni_enabled is not None:
        _details['isSniEnabled'] = is_sni_enabled

    if health_checks is not None:
        _details['healthChecks'] = cli_util.parse_json_parameter("health_checks", health_checks)

    _details['loadBalancingMethod']['method'] = 'ROUND_ROBIN'

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_policy_config(
        waas_policy_id=waas_policy_id,
        update_policy_config_details=_details,
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


@policy_config_group.command(name=cli_util.override('waas.update_policy_config_sticky_cookie_load_balancing_method.command_name', 'update-policy-config-sticky-cookie-load-balancing-method'), help=u"""Updates the configuration for a WAAS policy. Only the fields specified in the request body will be updated; all other properties will remain unchanged.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--certificate-id', help=u"""The OCID of the SSL certificate to use if HTTPS is supported.""")
@cli_util.option('--is-https-enabled', type=click.BOOL, help=u"""Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.""")
@cli_util.option('--is-https-forced', type=click.BOOL, help=u"""Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.""")
@cli_util.option('--tls-protocols', type=custom_types.CliCaseInsensitiveChoice(["TLS_V1", "TLS_V1_1", "TLS_V1_2", "TLS_V1_3"]), help=u"""A list of allowed TLS protocols. Only applicable when HTTPS support is enabled. The TLS protocol is negotiated while the request is connecting and the most recent protocol supported by both the edge node and client browser will be selected. If no such version exists, the connection will be aborted. - **TLS_V1:** corresponds to TLS 1.0 specification.

- **TLS_V1_1:** corresponds to TLS 1.1 specification.

- **TLS_V1_2:** corresponds to TLS 1.2 specification.

- **TLS_V1_3:** corresponds to TLS 1.3 specification.

Enabled TLS protocols must go in a row. For example if `TLS_v1_1` and `TLS_V1_3` are enabled, `TLS_V1_2` must be enabled too.""")
@cli_util.option('--is-origin-compression-enabled', type=click.BOOL, help=u"""Enable or disable GZIP compression of origin responses. If enabled, the header `Accept-Encoding: gzip` is sent to origin, otherwise, the empty `Accept-Encoding:` header is used.""")
@cli_util.option('--is-behind-cdn', type=click.BOOL, help=u"""Enabling `isBehindCdn` allows for the collection of IP addresses from client requests if the WAF is connected to a CDN.""")
@cli_util.option('--client-address-header', type=custom_types.CliCaseInsensitiveChoice(["X_FORWARDED_FOR", "X_CLIENT_IP", "X_REAL_IP", "CLIENT_IP", "TRUE_CLIENT_IP"]), help=u"""Specifies an HTTP header name which is treated as the connecting client's IP address. Applicable only if `isBehindCdn` is enabled.

The edge node reads this header and its value and sets the client IP address as specified. It does not create the header if the header is not present in the request. If the header is not present, the connecting IP address will be used as the client's true IP address. It uses the last IP address in the header's value as the true IP address.

Example: `X-Client-Ip: 11.1.1.1, 13.3.3.3`

In the case of multiple headers with the same name, only the first header will be used. It is assumed that CDN sets the correct client IP address to prevent spoofing.

- **X_FORWARDED_FOR:** Corresponds to `X-Forwarded-For` header name.

- **X_CLIENT_IP:** Corresponds to `X-Client-Ip` header name.

- **X_REAL_IP:** Corresponds to `X-Real-Ip` header name.

- **CLIENT_IP:** Corresponds to `Client-Ip` header name.

- **TRUE_CLIENT_IP:** Corresponds to `True-Client-Ip` header name.""")
@cli_util.option('--is-cache-control-respected', type=click.BOOL, help=u"""Enable or disable automatic content caching based on the response `cache-control` header. This feature enables the origin to act as a proxy cache. Caching is usually defined using `cache-control` header. For example `cache-control: max-age=120` means that the returned resource is valid for 120 seconds. Caching rules will overwrite this setting.""")
@cli_util.option('--is-response-buffering-enabled', type=click.BOOL, help=u"""Enable or disable buffering of responses from the origin. Buffering improves overall stability in case of network issues, but slightly increases Time To First Byte.""")
@cli_util.option('--cipher-group', type=custom_types.CliCaseInsensitiveChoice(["DEFAULT"]), help=u"""The set cipher group for the configured TLS protocol. This sets the configuration for the TLS connections between clients and edge nodes only. - **DEFAULT:** Cipher group supports TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 protocols. It has the following ciphers enabled: `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:!DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA`""")
@cli_util.option('--websocket-path-prefixes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""ModSecurity is not capable to inspect WebSockets. Therefore paths specified here have WAF disabled if Connection request header from the client has the value Upgrade (case insensitive matching) and Upgrade request header has the value websocket (case insensitive matching). Paths matches if the concatenation of request URL path and query starts with the contents of the one of `websocketPathPrefixes` array value. In All other cases challenges, like JSC, HIC and etc., remain active.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-sni-enabled', type=click.BOOL, help=u"""SNI stands for Server Name Indication and is an extension of the TLS protocol. It indicates which hostname is being contacted by the browser at the beginning of the 'handshake'-process. This allows a server to connect multiple SSL Certificates to one IP address and port.""")
@cli_util.option('--health-checks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--load-balancing-method-name', help=u"""The name of the cookie used to track the persistence. Can contain any US-ASCII character except separator or control character.""")
@cli_util.option('--load-balancing-method-domain', help=u"""The domain for which the cookie is set, defaults to WAAS policy domain.""")
@cli_util.option('--load-balancing-method-expiration-time-in-seconds', type=click.INT, help=u"""The time for which a browser should keep the cookie in seconds. Empty value will cause the cookie to expire at the end of a browser session.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'websocket-path-prefixes': {'module': 'waas', 'class': 'list[string]'}, 'health-checks': {'module': 'waas', 'class': 'HealthCheck'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'websocket-path-prefixes': {'module': 'waas', 'class': 'list[string]'}, 'health-checks': {'module': 'waas', 'class': 'HealthCheck'}})
@cli_util.wrap_exceptions
def update_policy_config_sticky_cookie_load_balancing_method(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, certificate_id, is_https_enabled, is_https_forced, tls_protocols, is_origin_compression_enabled, is_behind_cdn, client_address_header, is_cache_control_respected, is_response_buffering_enabled, cipher_group, websocket_path_prefixes, is_sni_enabled, health_checks, if_match, load_balancing_method_name, load_balancing_method_domain, load_balancing_method_expiration_time_in_seconds):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')
    if not force:
        if tls_protocols or websocket_path_prefixes or health_checks:
            if not click.confirm("WARNING: Updates to tls-protocols and websocket-path-prefixes and health-checks will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['loadBalancingMethod'] = {}

    if certificate_id is not None:
        _details['certificateId'] = certificate_id

    if is_https_enabled is not None:
        _details['isHttpsEnabled'] = is_https_enabled

    if is_https_forced is not None:
        _details['isHttpsForced'] = is_https_forced

    if tls_protocols is not None:
        _details['tlsProtocols'] = cli_util.parse_json_parameter("tls_protocols", tls_protocols)

    if is_origin_compression_enabled is not None:
        _details['isOriginCompressionEnabled'] = is_origin_compression_enabled

    if is_behind_cdn is not None:
        _details['isBehindCdn'] = is_behind_cdn

    if client_address_header is not None:
        _details['clientAddressHeader'] = client_address_header

    if is_cache_control_respected is not None:
        _details['isCacheControlRespected'] = is_cache_control_respected

    if is_response_buffering_enabled is not None:
        _details['isResponseBufferingEnabled'] = is_response_buffering_enabled

    if cipher_group is not None:
        _details['cipherGroup'] = cipher_group

    if websocket_path_prefixes is not None:
        _details['websocketPathPrefixes'] = cli_util.parse_json_parameter("websocket_path_prefixes", websocket_path_prefixes)

    if is_sni_enabled is not None:
        _details['isSniEnabled'] = is_sni_enabled

    if health_checks is not None:
        _details['healthChecks'] = cli_util.parse_json_parameter("health_checks", health_checks)

    if load_balancing_method_name is not None:
        _details['loadBalancingMethod']['name'] = load_balancing_method_name

    if load_balancing_method_domain is not None:
        _details['loadBalancingMethod']['domain'] = load_balancing_method_domain

    if load_balancing_method_expiration_time_in_seconds is not None:
        _details['loadBalancingMethod']['expirationTimeInSeconds'] = load_balancing_method_expiration_time_in_seconds

    _details['loadBalancingMethod']['method'] = 'STICKY_COOKIE'

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_policy_config(
        waas_policy_id=waas_policy_id,
        update_policy_config_details=_details,
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


@policy_config_group.command(name=cli_util.override('waas.update_policy_config_ip_hash_load_balancing_method.command_name', 'update-policy-config-ip-hash-load-balancing-method'), help=u"""Updates the configuration for a WAAS policy. Only the fields specified in the request body will be updated; all other properties will remain unchanged.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--certificate-id', help=u"""The OCID of the SSL certificate to use if HTTPS is supported.""")
@cli_util.option('--is-https-enabled', type=click.BOOL, help=u"""Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.""")
@cli_util.option('--is-https-forced', type=click.BOOL, help=u"""Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.""")
@cli_util.option('--tls-protocols', type=custom_types.CliCaseInsensitiveChoice(["TLS_V1", "TLS_V1_1", "TLS_V1_2", "TLS_V1_3"]), help=u"""A list of allowed TLS protocols. Only applicable when HTTPS support is enabled. The TLS protocol is negotiated while the request is connecting and the most recent protocol supported by both the edge node and client browser will be selected. If no such version exists, the connection will be aborted. - **TLS_V1:** corresponds to TLS 1.0 specification.

- **TLS_V1_1:** corresponds to TLS 1.1 specification.

- **TLS_V1_2:** corresponds to TLS 1.2 specification.

- **TLS_V1_3:** corresponds to TLS 1.3 specification.

Enabled TLS protocols must go in a row. For example if `TLS_v1_1` and `TLS_V1_3` are enabled, `TLS_V1_2` must be enabled too.""")
@cli_util.option('--is-origin-compression-enabled', type=click.BOOL, help=u"""Enable or disable GZIP compression of origin responses. If enabled, the header `Accept-Encoding: gzip` is sent to origin, otherwise, the empty `Accept-Encoding:` header is used.""")
@cli_util.option('--is-behind-cdn', type=click.BOOL, help=u"""Enabling `isBehindCdn` allows for the collection of IP addresses from client requests if the WAF is connected to a CDN.""")
@cli_util.option('--client-address-header', type=custom_types.CliCaseInsensitiveChoice(["X_FORWARDED_FOR", "X_CLIENT_IP", "X_REAL_IP", "CLIENT_IP", "TRUE_CLIENT_IP"]), help=u"""Specifies an HTTP header name which is treated as the connecting client's IP address. Applicable only if `isBehindCdn` is enabled.

The edge node reads this header and its value and sets the client IP address as specified. It does not create the header if the header is not present in the request. If the header is not present, the connecting IP address will be used as the client's true IP address. It uses the last IP address in the header's value as the true IP address.

Example: `X-Client-Ip: 11.1.1.1, 13.3.3.3`

In the case of multiple headers with the same name, only the first header will be used. It is assumed that CDN sets the correct client IP address to prevent spoofing.

- **X_FORWARDED_FOR:** Corresponds to `X-Forwarded-For` header name.

- **X_CLIENT_IP:** Corresponds to `X-Client-Ip` header name.

- **X_REAL_IP:** Corresponds to `X-Real-Ip` header name.

- **CLIENT_IP:** Corresponds to `Client-Ip` header name.

- **TRUE_CLIENT_IP:** Corresponds to `True-Client-Ip` header name.""")
@cli_util.option('--is-cache-control-respected', type=click.BOOL, help=u"""Enable or disable automatic content caching based on the response `cache-control` header. This feature enables the origin to act as a proxy cache. Caching is usually defined using `cache-control` header. For example `cache-control: max-age=120` means that the returned resource is valid for 120 seconds. Caching rules will overwrite this setting.""")
@cli_util.option('--is-response-buffering-enabled', type=click.BOOL, help=u"""Enable or disable buffering of responses from the origin. Buffering improves overall stability in case of network issues, but slightly increases Time To First Byte.""")
@cli_util.option('--cipher-group', type=custom_types.CliCaseInsensitiveChoice(["DEFAULT"]), help=u"""The set cipher group for the configured TLS protocol. This sets the configuration for the TLS connections between clients and edge nodes only. - **DEFAULT:** Cipher group supports TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 protocols. It has the following ciphers enabled: `ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:!DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA`""")
@cli_util.option('--websocket-path-prefixes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""ModSecurity is not capable to inspect WebSockets. Therefore paths specified here have WAF disabled if Connection request header from the client has the value Upgrade (case insensitive matching) and Upgrade request header has the value websocket (case insensitive matching). Paths matches if the concatenation of request URL path and query starts with the contents of the one of `websocketPathPrefixes` array value. In All other cases challenges, like JSC, HIC and etc., remain active.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-sni-enabled', type=click.BOOL, help=u"""SNI stands for Server Name Indication and is an extension of the TLS protocol. It indicates which hostname is being contacted by the browser at the beginning of the 'handshake'-process. This allows a server to connect multiple SSL Certificates to one IP address and port.""")
@cli_util.option('--health-checks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'websocket-path-prefixes': {'module': 'waas', 'class': 'list[string]'}, 'health-checks': {'module': 'waas', 'class': 'HealthCheck'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'websocket-path-prefixes': {'module': 'waas', 'class': 'list[string]'}, 'health-checks': {'module': 'waas', 'class': 'HealthCheck'}})
@cli_util.wrap_exceptions
def update_policy_config_ip_hash_load_balancing_method(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, certificate_id, is_https_enabled, is_https_forced, tls_protocols, is_origin_compression_enabled, is_behind_cdn, client_address_header, is_cache_control_respected, is_response_buffering_enabled, cipher_group, websocket_path_prefixes, is_sni_enabled, health_checks, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')
    if not force:
        if tls_protocols or websocket_path_prefixes or health_checks:
            if not click.confirm("WARNING: Updates to tls-protocols and websocket-path-prefixes and health-checks will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['loadBalancingMethod'] = {}

    if certificate_id is not None:
        _details['certificateId'] = certificate_id

    if is_https_enabled is not None:
        _details['isHttpsEnabled'] = is_https_enabled

    if is_https_forced is not None:
        _details['isHttpsForced'] = is_https_forced

    if tls_protocols is not None:
        _details['tlsProtocols'] = cli_util.parse_json_parameter("tls_protocols", tls_protocols)

    if is_origin_compression_enabled is not None:
        _details['isOriginCompressionEnabled'] = is_origin_compression_enabled

    if is_behind_cdn is not None:
        _details['isBehindCdn'] = is_behind_cdn

    if client_address_header is not None:
        _details['clientAddressHeader'] = client_address_header

    if is_cache_control_respected is not None:
        _details['isCacheControlRespected'] = is_cache_control_respected

    if is_response_buffering_enabled is not None:
        _details['isResponseBufferingEnabled'] = is_response_buffering_enabled

    if cipher_group is not None:
        _details['cipherGroup'] = cipher_group

    if websocket_path_prefixes is not None:
        _details['websocketPathPrefixes'] = cli_util.parse_json_parameter("websocket_path_prefixes", websocket_path_prefixes)

    if is_sni_enabled is not None:
        _details['isSniEnabled'] = is_sni_enabled

    if health_checks is not None:
        _details['healthChecks'] = cli_util.parse_json_parameter("health_checks", health_checks)

    _details['loadBalancingMethod']['method'] = 'IP_HASH'

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_policy_config(
        waas_policy_id=waas_policy_id,
        update_policy_config_details=_details,
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


@protection_rule_group.command(name=cli_util.override('waas.update_protection_rules.command_name', 'update'), help=u"""Updates the action for each specified protection rule. Requests can either be allowed, blocked, or trigger an alert if they meet the parameters of an applied rule. For more information on protection rules, see [WAF Protection Rules]. This operation can update or disable protection rules depending on the structure of the request body. Protection rules can be updated by changing the properties of the protection rule object with the rule's key specified in the key field.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--protection-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'protection-rules': {'module': 'waas', 'class': 'list[ProtectionRuleAction]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'protection-rules': {'module': 'waas', 'class': 'list[ProtectionRuleAction]'}})
@cli_util.wrap_exceptions
def update_protection_rules(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, protection_rules, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_protection_rules(
        waas_policy_id=waas_policy_id,
        protection_rules=cli_util.parse_json_parameter("protection_rules", protection_rules),
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


@protection_settings_group.command(name=cli_util.override('waas.update_protection_settings.command_name', 'update'), help=u"""Updates the protection settings in the Web Application Firewall configuration for a WAAS policy. Protection settings allow you define what action is taken when a request is blocked by the Web Application Firewall, such as returning a response code or block page. Only the fields specified in the request body will be updated; all other fields will remain unchanged.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--block-action', type=custom_types.CliCaseInsensitiveChoice(["SHOW_ERROR_PAGE", "SET_RESPONSE_CODE"]), help=u"""If `action` is set to `BLOCK`, this specifies how the traffic is blocked when detected as malicious by a protection rule. If unspecified, defaults to `SET_RESPONSE_CODE`.""")
@cli_util.option('--block-response-code', type=click.INT, help=u"""The response code returned when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`. The list of available response codes: `400`, `401`, `403`, `405`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `500`, `501`, `502`, `503`, `504`, `507`.""")
@cli_util.option('--block-error-page-message', help=u"""The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to 'Access to the website is blocked.'""")
@cli_util.option('--block-error-page-code', help=u"""The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`.""")
@cli_util.option('--block-error-page-description', help=u"""The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `Access blocked by website owner. Please contact support.`""")
@cli_util.option('--max-argument-count', type=click.INT, help=u"""The maximum number of arguments allowed to be passed to your application before an action is taken. Arguements are query parameters or body parameters in a PUT or POST request. If unspecified, defaults to `255`. This setting only applies if a corresponding protection rule is enabled, such as the \"Number of Arguments Limits\" rule (key: 960335).

Example: If `maxArgumentCount` to `2` for the Max Number of Arguments protection rule (key: 960335), the following requests would be blocked: `GET /myapp/path?query=one&query=two&query=three` `POST /myapp/path` with Body `{\"argument1\":\"one\",\"argument2\":\"two\",\"argument3\":\"three\"}`""")
@cli_util.option('--max-name-length-per-argument', type=click.INT, help=u"""The maximum length allowed for each argument name, in characters. Arguements are query parameters or body parameters in a PUT or POST request. If unspecified, defaults to `400`. This setting only applies if a corresponding protection rule is enabled, such as the \"Values Limits\" rule (key: 960208).""")
@cli_util.option('--max-total-name-length-of-arguments', type=click.INT, help=u"""The maximum length allowed for the sum of the argument name and value, in characters. Arguements are query parameters or body parameters in a PUT or POST request. If unspecified, defaults to `64000`. This setting only applies if a corresponding protection rule is enabled, such as the \"Total Arguments Limits\" rule (key: 960341).""")
@cli_util.option('--recommendations-period-in-days', type=click.INT, help=u"""The length of time to analyze traffic traffic, in days. After the analysis period, `WafRecommendations` will be populated. If unspecified, defaults to `10`.

Use `GET /waasPolicies/{waasPolicyId}/wafRecommendations` to view WAF recommendations.""")
@cli_util.option('--is-response-inspected', type=click.BOOL, help=u"""Inspects the response body of origin responses. Can be used to detect leakage of sensitive data. If unspecified, defaults to `false`.

**Note:** Only origin responses with a Content-Type matching a value in `mediaTypes` will be inspected.""")
@cli_util.option('--max-response-size-in-ki-b', type=click.INT, help=u"""The maximum response size to be fully inspected, in binary kilobytes (KiB). Anything over this limit will be partially inspected. If unspecified, defaults to `1024`.""")
@cli_util.option('--allowed-http-methods', type=custom_types.CliCaseInsensitiveChoice(["OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT", "PATCH", "PROPFIND"]), help=u"""The list of allowed HTTP methods. If unspecified, default to `[OPTIONS, GET, HEAD, POST]`. This setting only applies if a corresponding protection rule is enabled, such as the \"Restrict HTTP Request Methods\" rule (key: 911100).""")
@cli_util.option('--media-types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of media types to allow for inspection, if `isResponseInspected` is enabled. Only responses with MIME types in this list will be inspected. If unspecified, defaults to `[\"text/html\", \"text/plain\", \"text/xml\"]`.

    Supported MIME types include:

    - text/html     - text/plain     - text/asp     - text/css     - text/x-script     - application/json     - text/webviewhtml     - text/x-java-source     - application/x-javascript     - application/javascript     - application/ecmascript     - text/javascript     - text/ecmascript     - text/x-script.perl     - text/x-script.phyton     - application/plain     - application/xml     - text/xml""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'media-types': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'media-types': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_protection_settings(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, block_action, block_response_code, block_error_page_message, block_error_page_code, block_error_page_description, max_argument_count, max_name_length_per_argument, max_total_name_length_of_arguments, recommendations_period_in_days, is_response_inspected, max_response_size_in_ki_b, allowed_http_methods, media_types, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')
    if not force:
        if allowed_http_methods or media_types:
            if not click.confirm("WARNING: Updates to allowed-http-methods and media-types will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if block_action is not None:
        _details['blockAction'] = block_action

    if block_response_code is not None:
        _details['blockResponseCode'] = block_response_code

    if block_error_page_message is not None:
        _details['blockErrorPageMessage'] = block_error_page_message

    if block_error_page_code is not None:
        _details['blockErrorPageCode'] = block_error_page_code

    if block_error_page_description is not None:
        _details['blockErrorPageDescription'] = block_error_page_description

    if max_argument_count is not None:
        _details['maxArgumentCount'] = max_argument_count

    if max_name_length_per_argument is not None:
        _details['maxNameLengthPerArgument'] = max_name_length_per_argument

    if max_total_name_length_of_arguments is not None:
        _details['maxTotalNameLengthOfArguments'] = max_total_name_length_of_arguments

    if recommendations_period_in_days is not None:
        _details['recommendationsPeriodInDays'] = recommendations_period_in_days

    if is_response_inspected is not None:
        _details['isResponseInspected'] = is_response_inspected

    if max_response_size_in_ki_b is not None:
        _details['maxResponseSizeInKiB'] = max_response_size_in_ki_b

    if allowed_http_methods is not None:
        _details['allowedHttpMethods'] = cli_util.parse_json_parameter("allowed_http_methods", allowed_http_methods)

    if media_types is not None:
        _details['mediaTypes'] = cli_util.parse_json_parameter("media_types", media_types)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_protection_settings(
        waas_policy_id=waas_policy_id,
        update_protection_settings_details=_details,
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


@threat_feed_group.command(name=cli_util.override('waas.update_threat_feeds.command_name', 'update'), help=u"""Updates the action to take when a request's IP address matches an address in the specified threat intelligence feed. Threat intelligence feeds are compiled lists of IP addresses with malicious reputations based on internet intelligence. Only the threat feeds specified in the request body will be updated; all other threat feeds will remain unchanged.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--threat-feeds', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of threat feeds for which to update the actions.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'threat-feeds': {'module': 'waas', 'class': 'list[ThreatFeedAction]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'threat-feeds': {'module': 'waas', 'class': 'list[ThreatFeedAction]'}})
@cli_util.wrap_exceptions
def update_threat_feeds(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, threat_feeds, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_threat_feeds(
        waas_policy_id=waas_policy_id,
        threat_feeds=cli_util.parse_json_parameter("threat_feeds", threat_feeds),
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


@waas_policy_group.command(name=cli_util.override('waas.update_waas_policy.command_name', 'update'), help=u"""Updates the details of a WAAS policy, including origins and tags. Only the fields specified in the request body will be updated; all other properties will remain unchanged. To update platform provided resources such as `GoodBots`, `ProtectionRules`, and `ThreatFeeds`, first retrieve the list of available resources with the related list operation such as `GetThreatFeeds` or `GetProtectionRules`. The returned list will contain objects with `key` properties that can be used to update the resource during the `UpdateWaasPolicy` request.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the WAAS policy. The name can be changed and does not need to be unique.""")
@cli_util.option('--additional-domains', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of additional domains protected by this WAAS policy.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--origins', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.

This option is a JSON dictionary of type dict(str, Origin).  For documentation on Origin please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/Origin.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--origin-groups', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests. To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.

This option is a JSON dictionary of type dict(str, OriginGroup).  For documentation on OriginGroup please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/OriginGroup.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--policy-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--waf-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'additional-domains': {'module': 'waas', 'class': 'list[string]'}, 'origins': {'module': 'waas', 'class': 'dict(str, Origin)'}, 'origin-groups': {'module': 'waas', 'class': 'dict(str, OriginGroup)'}, 'policy-config': {'module': 'waas', 'class': 'PolicyConfig'}, 'waf-config': {'module': 'waas', 'class': 'WafConfig'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'additional-domains': {'module': 'waas', 'class': 'list[string]'}, 'origins': {'module': 'waas', 'class': 'dict(str, Origin)'}, 'origin-groups': {'module': 'waas', 'class': 'dict(str, OriginGroup)'}, 'policy-config': {'module': 'waas', 'class': 'PolicyConfig'}, 'waf-config': {'module': 'waas', 'class': 'WafConfig'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_waas_policy(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, display_name, additional_domains, origins, origin_groups, policy_config, waf_config, freeform_tags, defined_tags, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')
    if not force:
        if additional_domains or origins or origin_groups or policy_config or waf_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to additional-domains and origins and origin-groups and policy-config and waf-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if additional_domains is not None:
        _details['additionalDomains'] = cli_util.parse_json_parameter("additional_domains", additional_domains)

    if origins is not None:
        _details['origins'] = cli_util.parse_json_parameter("origins", origins)

    if origin_groups is not None:
        _details['originGroups'] = cli_util.parse_json_parameter("origin_groups", origin_groups)

    if policy_config is not None:
        _details['policyConfig'] = cli_util.parse_json_parameter("policy_config", policy_config)

    if waf_config is not None:
        _details['wafConfig'] = cli_util.parse_json_parameter("waf_config", waf_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_waas_policy(
        waas_policy_id=waas_policy_id,
        update_waas_policy_details=_details,
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


@custom_protection_rule_group.command(name=cli_util.override('waas.update_waas_policy_custom_protection_rules.command_name', 'update-waas-policy'), help=u"""Updates the action for each specified custom protection rule. Only the `DETECT` and `BLOCK` actions can be set. Disabled rules should not be included in the list. For more information on protection rules, see [WAF Protection Rules].""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--update-custom-protection-rules-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'update-custom-protection-rules-details': {'module': 'waas', 'class': 'list[CustomProtectionRuleSetting]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'update-custom-protection-rules-details': {'module': 'waas', 'class': 'list[CustomProtectionRuleSetting]'}})
@cli_util.wrap_exceptions
def update_waas_policy_custom_protection_rules(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, update_custom_protection_rules_details, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_waas_policy_custom_protection_rules(
        waas_policy_id=waas_policy_id,
        update_custom_protection_rules_details=cli_util.parse_json_parameter("update_custom_protection_rules_details", update_custom_protection_rules_details),
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


@address_rate_limiting_group.command(name=cli_util.override('waas.update_waf_address_rate_limiting.command_name', 'update-waf'), help=u"""Updates the address rate limiting settings in the Web Application Firewall configuration for a policy. Rate limiting allows you to configure a threshold for the number of requests from a unique IP address for the given period. You can also define the response code for the requests from the same address that exceed the threshold.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Enables or disables the address rate limiting Web Application Firewall feature.""")
@cli_util.option('--allowed-rate-per-address', type=click.INT, help=u"""The number of allowed requests per second from one IP address. If unspecified, defaults to `1`.""")
@cli_util.option('--max-delayed-count-per-address', type=click.INT, help=u"""The maximum number of requests allowed to be queued before subsequent requests are dropped. If unspecified, defaults to `10`.""")
@cli_util.option('--block-response-code', type=click.INT, help=u"""The response status code returned when a request is blocked. If unspecified, defaults to `503`. The list of available response codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `499`, `500`, `501`, `502`, `503`, `504`, `507`.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_waf_address_rate_limiting(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, is_enabled, allowed_rate_per_address, max_delayed_count_per_address, block_response_code, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['isEnabled'] = is_enabled

    if allowed_rate_per_address is not None:
        _details['allowedRatePerAddress'] = allowed_rate_per_address

    if max_delayed_count_per_address is not None:
        _details['maxDelayedCountPerAddress'] = max_delayed_count_per_address

    if block_response_code is not None:
        _details['blockResponseCode'] = block_response_code

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_waf_address_rate_limiting(
        waas_policy_id=waas_policy_id,
        update_waf_address_rate_limiting_details=_details,
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


@waf_config_group.command(name=cli_util.override('waas.update_waf_config.command_name', 'update'), help=u"""Updates the Web Application Firewall configuration for a specified WAAS policy.

To update platform provided resources such as `GoodBots`, `ProtectionRules`, and `ThreatFeeds`, first retrieve the list of available resources with the related list operation, such as `GetThreatFeeds` or `GetProtectionRules`.

The returned list will contain objects with `key` properties that can be used to update the resource during the `UpdateWafConfig` request.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--access-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The access rules applied to the Web Application Firewall. Used for defining custom access policies with the combination of `ALLOW`, `DETECT`, and `BLOCK` rules, based on different criteria.

This option is a JSON list with items of type AccessRule.  For documentation on AccessRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/AccessRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--address-rate-limiting', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The IP address rate limiting settings used to limit the number of requests from an address.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--captchas', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of CAPTCHA challenge settings. These are used to challenge requests with a CAPTCHA to block bots.

This option is a JSON list with items of type Captcha.  For documentation on Captcha please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/Captcha.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--device-fingerprint-challenge', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The device fingerprint challenge settings. Used to detect unique devices based on the device fingerprint information collected in order to block bots.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--good-bots', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of bots allowed to access the web application.

This option is a JSON list with items of type GoodBot.  For documentation on GoodBot please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/GoodBot.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--human-interaction-challenge', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The human interaction challenge settings. Used to look for natural human interactions such as mouse movements, time on site, and page scrolling to identify bots.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--js-challenge', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The JavaScript challenge settings. Used to challenge requests with a JavaScript challenge and take the action if a browser has no JavaScript support in order to block bots.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--origin', help=u"""The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in `Origins`. Required when creating the `WafConfig` resource, but not on update.""")
@cli_util.option('--caching-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of caching rules applied to the web application.

This option is a JSON list with items of type CachingRule.  For documentation on CachingRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/CachingRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--custom-protection-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the custom protection rule OCIDs and their actions.

This option is a JSON list with items of type CustomProtectionRuleSetting.  For documentation on CustomProtectionRuleSetting please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/CustomProtectionRuleSetting.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--origin-groups', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests. To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--protection-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the protection rules and their details.

This option is a JSON list with items of type ProtectionRule.  For documentation on ProtectionRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/ProtectionRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--protection-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The settings to apply to protection rules.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--threat-feeds', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of threat intelligence feeds and the actions to apply to known malicious traffic based on internet intelligence.

This option is a JSON list with items of type ThreatFeed.  For documentation on ThreatFeed please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/ThreatFeed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--whitelists', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of IP addresses that bypass the Web Application Firewall.

This option is a JSON list with items of type Whitelist.  For documentation on Whitelist please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/Whitelist.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'access-rules': {'module': 'waas', 'class': 'list[AccessRule]'}, 'address-rate-limiting': {'module': 'waas', 'class': 'AddressRateLimiting'}, 'captchas': {'module': 'waas', 'class': 'list[Captcha]'}, 'device-fingerprint-challenge': {'module': 'waas', 'class': 'DeviceFingerprintChallenge'}, 'good-bots': {'module': 'waas', 'class': 'list[GoodBot]'}, 'human-interaction-challenge': {'module': 'waas', 'class': 'HumanInteractionChallenge'}, 'js-challenge': {'module': 'waas', 'class': 'JsChallenge'}, 'caching-rules': {'module': 'waas', 'class': 'list[CachingRule]'}, 'custom-protection-rules': {'module': 'waas', 'class': 'list[CustomProtectionRuleSetting]'}, 'origin-groups': {'module': 'waas', 'class': 'list[string]'}, 'protection-rules': {'module': 'waas', 'class': 'list[ProtectionRule]'}, 'protection-settings': {'module': 'waas', 'class': 'ProtectionSettings'}, 'threat-feeds': {'module': 'waas', 'class': 'list[ThreatFeed]'}, 'whitelists': {'module': 'waas', 'class': 'list[Whitelist]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'access-rules': {'module': 'waas', 'class': 'list[AccessRule]'}, 'address-rate-limiting': {'module': 'waas', 'class': 'AddressRateLimiting'}, 'captchas': {'module': 'waas', 'class': 'list[Captcha]'}, 'device-fingerprint-challenge': {'module': 'waas', 'class': 'DeviceFingerprintChallenge'}, 'good-bots': {'module': 'waas', 'class': 'list[GoodBot]'}, 'human-interaction-challenge': {'module': 'waas', 'class': 'HumanInteractionChallenge'}, 'js-challenge': {'module': 'waas', 'class': 'JsChallenge'}, 'caching-rules': {'module': 'waas', 'class': 'list[CachingRule]'}, 'custom-protection-rules': {'module': 'waas', 'class': 'list[CustomProtectionRuleSetting]'}, 'origin-groups': {'module': 'waas', 'class': 'list[string]'}, 'protection-rules': {'module': 'waas', 'class': 'list[ProtectionRule]'}, 'protection-settings': {'module': 'waas', 'class': 'ProtectionSettings'}, 'threat-feeds': {'module': 'waas', 'class': 'list[ThreatFeed]'}, 'whitelists': {'module': 'waas', 'class': 'list[Whitelist]'}})
@cli_util.wrap_exceptions
def update_waf_config(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, access_rules, address_rate_limiting, captchas, device_fingerprint_challenge, good_bots, human_interaction_challenge, js_challenge, origin, caching_rules, custom_protection_rules, origin_groups, protection_rules, protection_settings, threat_feeds, whitelists, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')
    if not force:
        if access_rules or address_rate_limiting or captchas or device_fingerprint_challenge or good_bots or human_interaction_challenge or js_challenge or caching_rules or custom_protection_rules or origin_groups or protection_rules or protection_settings or threat_feeds or whitelists:
            if not click.confirm("WARNING: Updates to access-rules and address-rate-limiting and captchas and device-fingerprint-challenge and good-bots and human-interaction-challenge and js-challenge and caching-rules and custom-protection-rules and origin-groups and protection-rules and protection-settings and threat-feeds and whitelists will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if access_rules is not None:
        _details['accessRules'] = cli_util.parse_json_parameter("access_rules", access_rules)

    if address_rate_limiting is not None:
        _details['addressRateLimiting'] = cli_util.parse_json_parameter("address_rate_limiting", address_rate_limiting)

    if captchas is not None:
        _details['captchas'] = cli_util.parse_json_parameter("captchas", captchas)

    if device_fingerprint_challenge is not None:
        _details['deviceFingerprintChallenge'] = cli_util.parse_json_parameter("device_fingerprint_challenge", device_fingerprint_challenge)

    if good_bots is not None:
        _details['goodBots'] = cli_util.parse_json_parameter("good_bots", good_bots)

    if human_interaction_challenge is not None:
        _details['humanInteractionChallenge'] = cli_util.parse_json_parameter("human_interaction_challenge", human_interaction_challenge)

    if js_challenge is not None:
        _details['jsChallenge'] = cli_util.parse_json_parameter("js_challenge", js_challenge)

    if origin is not None:
        _details['origin'] = origin

    if caching_rules is not None:
        _details['cachingRules'] = cli_util.parse_json_parameter("caching_rules", caching_rules)

    if custom_protection_rules is not None:
        _details['customProtectionRules'] = cli_util.parse_json_parameter("custom_protection_rules", custom_protection_rules)

    if origin_groups is not None:
        _details['originGroups'] = cli_util.parse_json_parameter("origin_groups", origin_groups)

    if protection_rules is not None:
        _details['protectionRules'] = cli_util.parse_json_parameter("protection_rules", protection_rules)

    if protection_settings is not None:
        _details['protectionSettings'] = cli_util.parse_json_parameter("protection_settings", protection_settings)

    if threat_feeds is not None:
        _details['threatFeeds'] = cli_util.parse_json_parameter("threat_feeds", threat_feeds)

    if whitelists is not None:
        _details['whitelists'] = cli_util.parse_json_parameter("whitelists", whitelists)

    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_waf_config(
        waas_policy_id=waas_policy_id,
        update_waf_config_details=_details,
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


@whitelist_group.command(name=cli_util.override('waas.update_whitelists.command_name', 'update'), help=u"""Updates the list of IP addresses that bypass the Web Application Firewall for a WAAS policy. Supports single IP addresses, subnet masks (CIDR notation) and Address Lists.

This operation can create, delete, update, and/or reorder whitelists depending on the structure of the request body.

Whitelists can be updated by changing the properties of the whitelist object with the rule's key specified in the `key` field. Whitelists can be reordered by changing the order of the whitelists in the list of objects when updating.

Whitelists can be created by adding a new whitelist object to the list without a `key` property specified. A `key` will be generated for the new whitelist upon update.

Whitelists can be deleted by removing the existing whitelist object from the list. Any existing whitelists that are not specified with a `key` in the list of access rules will be deleted upon update.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--whitelists', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'whitelists': {'module': 'waas', 'class': 'list[Whitelist]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'whitelists': {'module': 'waas', 'class': 'list[Whitelist]'}})
@cli_util.wrap_exceptions
def update_whitelists(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, whitelists, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', 'waas', ctx)
    result = client.update_whitelists(
        waas_policy_id=waas_policy_id,
        whitelists=cli_util.parse_json_parameter("whitelists", whitelists),
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
