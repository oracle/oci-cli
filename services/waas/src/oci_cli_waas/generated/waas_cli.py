# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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


@cli.command(cli_util.override('waas_root_group.command_name', 'waas'), cls=CommandGroupWithAlias, help=cli_util.override('waas_root_group.help', """OCI Web Application Acceleration and Security Services"""), short_help=cli_util.override('waas_root_group.short_help', """Web Application Acceleration and Security Services API"""))
@cli_util.help_option_group
def waas_root_group():
    pass


@click.command(cli_util.override('waas_policy_group.command_name', 'waas-policy'), cls=CommandGroupWithAlias, help="""The details of a Web Application Acceleration and Security (WAAS) policy. A policy describes how the WAAS service should operate for the configured web application.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def waas_policy_group():
    pass


@click.command(cli_util.override('access_rule_group.command_name', 'access-rule'), cls=CommandGroupWithAlias, help="""A content access rule. An access rule specifies an action to take if a set of criteria is matched by a request.""")
@cli_util.help_option_group
def access_rule_group():
    pass


@click.command(cli_util.override('good_bot_group.command_name', 'good-bot'), cls=CommandGroupWithAlias, help="""The good bot settings. Good bots provides a list of bots which are managed by known providers.""")
@cli_util.help_option_group
def good_bot_group():
    pass


@click.command(cli_util.override('threat_feed_group.command_name', 'threat-feed'), cls=CommandGroupWithAlias, help="""The settings of the threat intelligence feed. You can block requests from IP addresses based on their reputations with various commercial and open source threat feeds.""")
@cli_util.help_option_group
def threat_feed_group():
    pass


@click.command(cli_util.override('waf_traffic_datum_group.command_name', 'waf-traffic-datum'), cls=CommandGroupWithAlias, help="""A time series of traffic data for the  Web Application Firewall configured for a policy.""")
@cli_util.help_option_group
def waf_traffic_datum_group():
    pass


@click.command(cli_util.override('policy_config_group.command_name', 'policy-config'), cls=CommandGroupWithAlias, help="""The configuration details for the WAAS policy.""")
@cli_util.help_option_group
def policy_config_group():
    pass


@click.command(cli_util.override('certificate_group.command_name', 'certificate'), cls=CommandGroupWithAlias, help="""The details of the SSL certificate. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def certificate_group():
    pass


@click.command(cli_util.override('edge_subnet_group.command_name', 'edge-subnet'), cls=CommandGroupWithAlias, help="""The details about an edge node subnet.""")
@cli_util.help_option_group
def edge_subnet_group():
    pass


@click.command(cli_util.override('recommendation_group.command_name', 'recommendation'), cls=CommandGroupWithAlias, help="""A recommended protection rule for a web application. This recommendation can be accepted to apply it to the Web Application Firewall configuration for this policy.

Use the `POST /waasPolicies/{waasPolicyId}/actions/acceptWafConfigRecommendations` method to accept recommended protection rules.""")
@cli_util.help_option_group
def recommendation_group():
    pass


@click.command(cli_util.override('waf_request_group.command_name', 'waf-request'), cls=CommandGroupWithAlias, help="""A time series of request counts handled by the Web Application Firewall, including blocked requests.""")
@cli_util.help_option_group
def waf_request_group():
    pass


@click.command(cli_util.override('js_challenge_group.command_name', 'js-challenge'), cls=CommandGroupWithAlias, help="""The JavaScript challenge settings. Javascript Challenge is the function to filter abnormal or malicious bots and allow access to real clients.""")
@cli_util.help_option_group
def js_challenge_group():
    pass


@click.command(cli_util.override('protection_rule_group.command_name', 'protection-rule'), cls=CommandGroupWithAlias, help="""The protection rule settings. Protection rules can allow, block, or trigger an alert if a request meets the parameters of an applied rule.""")
@cli_util.help_option_group
def protection_rule_group():
    pass


@click.command(cli_util.override('whitelist_group.command_name', 'whitelist'), cls=CommandGroupWithAlias, help="""An array of IP addresses that bypass the Web Application Firewall. Supports both single IP addresses or subnet masks (CIDR notation).""")
@cli_util.help_option_group
def whitelist_group():
    pass


@click.command(cli_util.override('work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""Many of the API requests you use to create and configure WAAS policies do not take effect immediately. In these cases, the request spawns an asynchronous work flow to fulfill the request. `WorkRequest` objects provide visibility for in-progress work flows. For more information about work requests, see [Viewing the State of a Work Request].""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('human_interaction_challenge_group.command_name', 'human-interaction-challenge'), cls=CommandGroupWithAlias, help="""The human interaction challenge settings. The human interaction challenge checks various event listeners in the user's browser to determine if there is a human user making a request.""")
@cli_util.help_option_group
def human_interaction_challenge_group():
    pass


@click.command(cli_util.override('device_fingerprint_challenge_group.command_name', 'device-fingerprint-challenge'), cls=CommandGroupWithAlias, help="""The device fingerprint challenge settings. The device fingerprint challenge generates hashed signatures of both virtual and real browsers to identify and block malicious bots.""")
@cli_util.help_option_group
def device_fingerprint_challenge_group():
    pass


@click.command(cli_util.override('address_rate_limiting_group.command_name', 'address-rate-limiting'), cls=CommandGroupWithAlias, help="""The IP rate limiting configuration. Defines the amount of allowed requests from a unique IP address and the resulting block response code when that threshold is exceeded.""")
@cli_util.help_option_group
def address_rate_limiting_group():
    pass


@click.command(cli_util.override('waf_log_group.command_name', 'waf-log'), cls=CommandGroupWithAlias, help="""A list of Web Application Firewall log entries. Each entry is a JSON object whose fields vary based on log type. Logs record what rules and countermeasures are triggered by requests and are used as a basis to move request handling into block mode.""")
@cli_util.help_option_group
def waf_log_group():
    pass


@click.command(cli_util.override('captcha_group.command_name', 'captcha'), cls=CommandGroupWithAlias, help="""The settings of the CAPTCHA challenge. If a specific URL should be accessed only by a human, a CAPTCHA challenge can be placed at the URL to protect the web application from bots.

*Warning:* Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def captcha_group():
    pass


@click.command(cli_util.override('protection_settings_group.command_name', 'protection-settings'), cls=CommandGroupWithAlias, help="""The settings used for protection rules.""")
@cli_util.help_option_group
def protection_settings_group():
    pass


@click.command(cli_util.override('waf_config_group.command_name', 'waf-config'), cls=CommandGroupWithAlias, help="""The Web Application Firewall configuration for the WAAS policy.""")
@cli_util.help_option_group
def waf_config_group():
    pass


@click.command(cli_util.override('waf_blocked_request_group.command_name', 'waf-blocked-request'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def waf_blocked_request_group():
    pass


waas_root_group.add_command(waas_policy_group)
waas_root_group.add_command(access_rule_group)
waas_root_group.add_command(good_bot_group)
waas_root_group.add_command(threat_feed_group)
waas_root_group.add_command(waf_traffic_datum_group)
waas_root_group.add_command(policy_config_group)
waas_root_group.add_command(certificate_group)
waas_root_group.add_command(edge_subnet_group)
waas_root_group.add_command(recommendation_group)
waas_root_group.add_command(waf_request_group)
waas_root_group.add_command(js_challenge_group)
waas_root_group.add_command(protection_rule_group)
waas_root_group.add_command(whitelist_group)
waas_root_group.add_command(work_request_group)
waas_root_group.add_command(human_interaction_challenge_group)
waas_root_group.add_command(device_fingerprint_challenge_group)
waas_root_group.add_command(address_rate_limiting_group)
waas_root_group.add_command(waf_log_group)
waas_root_group.add_command(captcha_group)
waas_root_group.add_command(protection_settings_group)
waas_root_group.add_command(waf_config_group)
waas_root_group.add_command(waf_blocked_request_group)


@recommendation_group.command(name=cli_util.override('accept_recommendations.command_name', 'accept'), help=u"""Accepts a list of recommended Web Application Firewall protection rules. Web Application Firewall protection rule recommendations are sets of rules generated by observed traffic patterns through the Web Application Firewall and are meant to optimize the Web Application Firewall's security profile. Only the rules specified in the request body will be updated; all other rules will remain unchanged.

Use the `GET /waasPolicies/{waasPolicyId}/wafConfig/recommendations` method to view a list of recommended Web Application Firewall protection rules. For more information, see [WAF Protection Rules].""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--protection-rule-keys', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def accept_recommendations(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, protection_rule_keys, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', ctx)
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


@work_request_group.command(name=cli_util.override('cancel_work_request.command_name', 'cancel'), help=u"""Cancels a specified work request.""")
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
    client = cli_util.build_client('waas', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@certificate_group.command(name=cli_util.override('create_certificate.command_name', 'create'), help=u"""Allows an SSL certificate to be added to a WAAS policy. The Web Application Firewall terminates SSL connections to inspect requests in runtime, and then re-encrypts requests before sending them to the origin for fulfillment.

For more information, see [WAF Settings].""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to create the SSL certificate.""")
@cli_util.option('--certificate-data', required=True, help=u"""The data of the SSL certificate.""")
@cli_util.option('--private-key-data', required=True, help=u"""The private key of the SSL certificate.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the SSL certificate. The name can be changed and does not need to be unique.""")
@cli_util.option('--is-trust-verification-disabled', type=click.BOOL, help=u"""Set to true if the SSL certificate is self-signed.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair without any defined schema.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A key-value pair with a defined schema that restricts the values of tags. These predefined keys are scoped to namespaces.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    details = {}
    details['compartmentId'] = compartment_id
    details['certificateData'] = certificate_data
    details['privateKeyData'] = private_key_data

    if display_name is not None:
        details['displayName'] = display_name

    if is_trust_verification_disabled is not None:
        details['isTrustVerificationDisabled'] = is_trust_verification_disabled

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', ctx)
    result = client.create_certificate(
        create_certificate_details=details,
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


@waas_policy_group.command(name=cli_util.override('create_waas_policy.command_name', 'create'), help=u"""Creates a new Web Application Acceleration and Security (WAAS) policy in the specified compartment. A WAAS policy must be established before creating Web Application Firewall (WAF) rules. To use WAF rules, your web application's origin servers must defined in the `WaasPolicy` schema.

A domain name must be specified when creating a WAAS policy. The domain name should be different from the origins specified in your `WaasPolicy`. Once domain name is entered and stored, it is unchangeable.

Use the record data returned in the `cname` field of the `WaasPolicy` object to create a CNAME record in your DNS configuration that will direct your domain's traffic through the WAF.

For the purposes of access control, you must provide the OCID of the compartment where you want the service to reside. For information about access control and compartments, see [Overview of the IAM Service].

You must specify a display name and domain for the WAAS policy. The display name does not have to be unique and can be changed. The domain name should be different from every origin specified in `WaasPolicy`.

All Oracle Cloud Infrastructure resources, including WAAS policies, receive a unique, Oracle-assigned ID called an Oracle Cloud Identifier (OCID). When a resource is created, you can find its OCID in the response. You can also retrieve a resource's OCID by using a list API operation for that resource type, or by viewing the resource in the Console. Fore more information, see [Resource Identifiers].

**Note:** After sending the POST request, the new object's state will temporarily be `CREATING`. Ensure that the resource's state has changed to `ACTIVE` before use.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment in which to create the WAAS policy.""")
@cli_util.option('--domain', required=True, help=u"""The web application domain that the WAAS policy protects.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the WAAS policy. The name is can be changed and does not need to be unique.""")
@cli_util.option('--additional-domains', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of additional domains for the specified web application.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--origins', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.

This option is a JSON dictionary of type dict(str, Origin).  For documentation on Origin please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/Origin.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--policy-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--waf-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair without any defined schema.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A key-value pair with a defined schema that restricts the values of tags. These predefined keys are scoped to namespaces.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'additional-domains': {'module': 'waas', 'class': 'list[string]'}, 'origins': {'module': 'waas', 'class': 'dict(str, Origin)'}, 'policy-config': {'module': 'waas', 'class': 'PolicyConfig'}, 'waf-config': {'module': 'waas', 'class': 'WafConfigDetails'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'additional-domains': {'module': 'waas', 'class': 'list[string]'}, 'origins': {'module': 'waas', 'class': 'dict(str, Origin)'}, 'policy-config': {'module': 'waas', 'class': 'PolicyConfig'}, 'waf-config': {'module': 'waas', 'class': 'WafConfigDetails'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_waas_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, domain, display_name, additional_domains, origins, policy_config, waf_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id
    details['domain'] = domain

    if display_name is not None:
        details['displayName'] = display_name

    if additional_domains is not None:
        details['additionalDomains'] = cli_util.parse_json_parameter("additional_domains", additional_domains)

    if origins is not None:
        details['origins'] = cli_util.parse_json_parameter("origins", origins)

    if policy_config is not None:
        details['policyConfig'] = cli_util.parse_json_parameter("policy_config", policy_config)

    if waf_config is not None:
        details['wafConfig'] = cli_util.parse_json_parameter("waf_config", waf_config)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', ctx)
    result = client.create_waas_policy(
        create_waas_policy_details=details,
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


@certificate_group.command(name=cli_util.override('delete_certificate.command_name', 'delete'), help=u"""Deletes an SSL certificate from the WAAS service.""")
@cli_util.option('--certificate-id', required=True, help=u"""The [OCID] of the SSL certificate used in the WAAS policy. This number is generated when the certificate is added to the policy.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('waas', ctx)
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


@waas_policy_group.command(name=cli_util.override('delete_waas_policy.command_name', 'delete'), help=u"""Deletes a policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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
    client = cli_util.build_client('waas', ctx)
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


@certificate_group.command(name=cli_util.override('get_certificate.command_name', 'get'), help=u"""Gets the details of an SSL certificate.""")
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
    client = cli_util.build_client('waas', ctx)
    result = client.get_certificate(
        certificate_id=certificate_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@device_fingerprint_challenge_group.command(name=cli_util.override('get_device_fingerprint_challenge.command_name', 'get'), help=u"""Gets the device fingerprint challenge settings in the Web Application Firewall configuration for a WAAS policy.""")
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
    client = cli_util.build_client('waas', ctx)
    result = client.get_device_fingerprint_challenge(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@human_interaction_challenge_group.command(name=cli_util.override('get_human_interaction_challenge.command_name', 'get'), help=u"""Gets the human interaction challenge settings in the Web Application Firewall configuration for a WAAS policy.""")
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
    client = cli_util.build_client('waas', ctx)
    result = client.get_human_interaction_challenge(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@js_challenge_group.command(name=cli_util.override('get_js_challenge.command_name', 'get'), help=u"""Gets the JavaScript challenge settings in the Web Application Firewall configuration for a WAAS policy.""")
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
    client = cli_util.build_client('waas', ctx)
    result = client.get_js_challenge(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@policy_config_group.command(name=cli_util.override('get_policy_config.command_name', 'get'), help=u"""Gets the configuration of a WAAS policy.""")
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
    client = cli_util.build_client('waas', ctx)
    result = client.get_policy_config(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@protection_rule_group.command(name=cli_util.override('get_protection_rule.command_name', 'get'), help=u"""Gets the details of a protection rule in the Web Application Firewall configuration for a WAAS policy.""")
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
    client = cli_util.build_client('waas', ctx)
    result = client.get_protection_rule(
        waas_policy_id=waas_policy_id,
        protection_rule_key=protection_rule_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@protection_settings_group.command(name=cli_util.override('get_protection_settings.command_name', 'get'), help=u"""Gets the protection settings in the Web Application Firewall configuration for a WAAS policy.""")
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
    client = cli_util.build_client('waas', ctx)
    result = client.get_protection_settings(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@waas_policy_group.command(name=cli_util.override('get_waas_policy.command_name', 'get'), help=u"""Gets the details of a WAAS policy.""")
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
    client = cli_util.build_client('waas', ctx)
    result = client.get_waas_policy(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@address_rate_limiting_group.command(name=cli_util.override('get_waf_address_rate_limiting.command_name', 'get-waf'), help=u"""Gets the address rate limiting settings of the Web Application Firewall configuration for a WAAS policy.""")
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
    client = cli_util.build_client('waas', ctx)
    result = client.get_waf_address_rate_limiting(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@waf_config_group.command(name=cli_util.override('get_waf_config.command_name', 'get'), help=u"""Gets the Web Application Firewall configuration details for a WAAS policy.""")
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
    client = cli_util.build_client('waas', ctx)
    result = client.get_waf_config(
        waas_policy_id=waas_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('get_work_request.command_name', 'get'), help=u"""Gets the details of a specified work request.""")
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
    client = cli_util.build_client('waas', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@access_rule_group.command(name=cli_util.override('list_access_rules.command_name', 'list'), help=u"""Gets the currently configured access rules for the Web Application Firewall configration of a specified WAAS policy. The order of the access rules is important. The rules will be checked in the order they are specified and the first matching rule will be used.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
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
    client = cli_util.build_client('waas', ctx)
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


@captcha_group.command(name=cli_util.override('list_captchas.command_name', 'list'), help=u"""Gets the list of currently configured CAPTCHA challenges in the Web Application Firewall configuration of a WAAS policy.

The order of the CAPTCHA challenges is important. The URL for each CAPTCHA will be checked in the order they are created.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
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
    client = cli_util.build_client('waas', ctx)
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


@certificate_group.command(name=cli_util.override('list_certificates.command_name', 'list'), help=u"""Gets a list of SSL certificates that can be used in a WAAS policy.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment. This number is generated when the compartment is created.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "compartmentId", "displayName", "notValidAfter", "timeCreated"]), help=u"""The value by which certificate summaries are sorted in a paginated 'List' call. If unspecified, defaults to `timeCreated`.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.""")
@cli_util.option('--id', help=u"""Filter certificates using a list of certificates OCIDs.""")
@cli_util.option('--display-name', help=u"""Filter certificates using a list of display names.""")
@cli_util.option('--lifecycle-state', help=u"""Filter certificates using a list of lifecycle states.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that matches certificates created on or after the specified date-time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that matches certificates created before the specified date-time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[CertificateSummary]'})
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
    client = cli_util.build_client('waas', ctx)
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


@edge_subnet_group.command(name=cli_util.override('list_edge_subnets.command_name', 'list'), help=u"""Return the list of the tenant's edge node subnets. Use these CIDR blocks to restrict incoming traffic to your origin. These subnets are owned by OCI and forward traffic to customer origins. They are not associated with specific regions or compartments.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
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
    client = cli_util.build_client('waas', ctx)
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


@good_bot_group.command(name=cli_util.override('list_good_bots.command_name', 'list'), help=u"""Gets the list of good bots defined in the Web Application Firewall configuration for a WAAS policy.

The list is sorted ascending by `key`.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
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
    client = cli_util.build_client('waas', ctx)
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


@protection_rule_group.command(name=cli_util.override('list_protection_rules.command_name', 'list'), help=u"""Gets the list of protection rules in the Web Application Firewall configuration for a WAAS policy, including currently defined rules and recommended rules. The list is sorted ascending by `key`.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--mod-security-rule-id', help=u"""Filter rules using a list of ModSecurity rule IDs.""")
@cli_util.option('--action', type=custom_types.CliCaseInsensitiveChoice(["OFF", "DETECT", "BLOCK"]), multiple=True, help=u"""Filter rules using a list of actions.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[ProtectionRule]'})
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
    client = cli_util.build_client('waas', ctx)
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


@recommendation_group.command(name=cli_util.override('list_recommendations.command_name', 'list'), help=u"""Gets the list of recommended Web Application Firewall protection rules.

Use the `POST /waasPolicies/{waasPolicyId}/actions/acceptWafConfigRecommendations` method to accept recommended Web Application Firewall protection rules. For more information, see [WAF Protection Rules]. The list is sorted ascending by `key`.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--recommended-action', type=custom_types.CliCaseInsensitiveChoice(["DETECT", "BLOCK"]), help=u"""A filter that matches recommended protection rules based on the selected action. If unspecified, rules with any action type are returned.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
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
    client = cli_util.build_client('waas', ctx)
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


@threat_feed_group.command(name=cli_util.override('list_threat_feeds.command_name', 'list'), help=u"""Gets the list of available web application threat intelligence feeds and the actions set for each feed. The list is sorted ascending by `key`.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
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
    client = cli_util.build_client('waas', ctx)
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


@waas_policy_group.command(name=cli_util.override('list_waas_policies.command_name', 'list'), help=u"""Gets a list of WAAS policies.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment. This number is generated when the compartment is created.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["id", "displayName", "timeCreated"]), help=u"""The value by which policies are sorted in a paginated 'List' call.  If unspecified, defaults to `timeCreated`.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.""")
@cli_util.option('--id', help=u"""Filter policies using a list of policy OCIDs.""")
@cli_util.option('--display-name', help=u"""Filter policies using a list of display names.""")
@cli_util.option('--lifecycle-state', help=u"""Filter policies using a list of lifecycle states.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that matches policies created on or after the specified date and time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that matches policies created before the specified date-time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[WaasPolicySummary]'})
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
    client = cli_util.build_client('waas', ctx)
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


@waf_blocked_request_group.command(name=cli_util.override('list_waf_blocked_requests.command_name', 'list'), help=u"""Gets the number of blocked requests by a Web Application Firewall feature in five minute blocks, in ascending order by `timeObserved`.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--time-observed-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that limits returned events to those occurring on or after a date and time, specified in RFC 3339 format. If unspecified, defaults to 30 minutes before receipt of the request.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-observed-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that limits returned events to those occurring before a date and time, specified in RFC 3339 format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
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
    client = cli_util.build_client('waas', ctx)
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


@waf_log_group.command(name=cli_util.override('list_waf_logs.command_name', 'list'), help=u"""Gets structured Web Application Firewall event logs for a WAAS policy. The list is sorted by the `timeObserved` starting from the oldest recorded event (ascending).""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `20`.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous paginated call.""")
@cli_util.option('--time-observed-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that matches log entries where the observed event occurred on or after a date and time specified in RFC 3339 format. If unspecified, defaults to two hours before receipt of the request.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-observed-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that matches log entries where the observed event occurred before a date and time, specified in RFC 3339 format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--text-contains', help=u"""A full text search for logs.""")
@cli_util.option('--access-rule-key', help=u"""Filters logs by access rule key.""")
@cli_util.option('--action', type=custom_types.CliCaseInsensitiveChoice(["BLOCK", "DETECT", "BYPASS", "LOG", "REDIRECTED"]), multiple=True, help=u"""Filters logs by Web Application Firewall action.""")
@cli_util.option('--client-address', help=u"""Filters logs by client IP address.""")
@cli_util.option('--country-code', help=u"""Filters logs by country code. Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see [ISO's website].""")
@cli_util.option('--country-name', help=u"""Filter logs by country name.""")
@cli_util.option('--fingerprint', help=u"""Filter logs by device fingerprint.""")
@cli_util.option('--http-method', type=custom_types.CliCaseInsensitiveChoice(["OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT"]), multiple=True, help=u"""Filter logs by HTTP method.""")
@cli_util.option('--incident-key', help=u"""Filter logs by incident key.""")
@cli_util.option('--log-type', type=custom_types.CliCaseInsensitiveChoice(["ACCESS", "PROTECTION_RULES", "JS_CHALLENGE", "CAPTCHA", "ACCESS_RULES", "THREAT_FEEDS", "HUMAN_INTERACTION_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "ADDRESS_RATE_LIMITING"]), multiple=True, help=u"""Filter by log type.""")
@cli_util.option('--origin-address', help=u"""Filter by origin IP address.""")
@cli_util.option('--referrer', help=u"""Filter by referrer.""")
@cli_util.option('--request-url', help=u"""Filter by request URL.""")
@cli_util.option('--response-code', help=u"""Filter by response code.""")
@cli_util.option('--threat-feed-key', help=u"""Filter by threat feed key.""")
@cli_util.option('--user-agent', help=u"""Filter by user agent.""")
@cli_util.option('--protection-rule-key', help=u"""Filter by protection rule key.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'waas', 'class': 'list[WafLog]'})
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
    client = cli_util.build_client('waas', ctx)
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


@waf_request_group.command(name=cli_util.override('list_waf_requests.command_name', 'list'), help=u"""Gets the number of requests managed by a Web Application Firewall over a specified period of time, including blocked requests. Sorted by `timeObserved` with oldest requests first (ascending).""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--time-observed-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that limits returned events to those occurring on or after a date and time, specified in RFC 3339 format. If unspecified, defaults to 30 minutes before receipt of the request.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-observed-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that limits returned events to those occurring before a date and time, specified in RFC 3339 format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
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
    client = cli_util.build_client('waas', ctx)
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


@waf_traffic_datum_group.command(name=cli_util.override('list_waf_traffic.command_name', 'list-waf-traffic'), help=u"""Gets the Web Application Firewall traffic data for a WAAS policy. Sorted by `timeObserved` with oldest data points first (ascending).""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--time-observed-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""A filter that limits returned events to those occurring on or after a date and time, specified in RFC 3339 format. If unspecified, defaults to 30 minutes before receipt of the request.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-observed-less-than', type=custom_types.CLI_DATETIME, help=u"""A filter that limits returned events to those occurring before a date and time, specified in RFC 3339 format.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
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
    client = cli_util.build_client('waas', ctx)
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


@whitelist_group.command(name=cli_util.override('list_whitelists.command_name', 'list'), help=u"""Gets the list of whitelists defined in the Web Application Firewall configuration for a WAAS policy.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
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
    client = cli_util.build_client('waas', ctx)
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


@work_request_group.command(name=cli_util.override('list_work_requests.command_name', 'list'), help=u"""Gets a list of subnets (CIDR notation) from which the WAAS EDGE may make requests. The subnets are owned by OCI and forward traffic to your origins. Allow traffic from these subnets to your origins. They are not associated with specific regions or compartments.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the policy.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment. This number is generated when the compartment is created.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated call. In unspecified, defaults to `10`.""")
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
    client = cli_util.build_client('waas', ctx)
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


@access_rule_group.command(name=cli_util.override('update_access_rules.command_name', 'update'), help=u"""Updates the list of access rules in the Web Application Firewall configuration for a specified WAAS policy. Access rules allow explicit actions to be defined and executed for requests that meet various conditions. A rule action can be set to allow, detect, or block requests. The detect setting allows the request to pass through the Web Application Firewall and is tagged with a `DETECT` flag in the Web Application Firewall's log. This operation can create, delete, update, and/or reorder access rules depending on the structure of the request body. Updating an existing access rule can be accomplished by changing the properties of the access rule object with a non-empty `key` property in the list. Reordering of access rules can be accomplished by changing the order of the access rules in the list when updating. Creating an access rule can be accomplished by adding a new access rule object to the list without a `key` property. A `key` will be generated for the new access rule upon update. Deleting an access rule can be accomplished by removing the existing access rule object from the list. Any existing access rule with a `key` that is not present in the list of access rules sent in the request will be deleted.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--access-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_access_rules(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, access_rules, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', ctx)
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


@captcha_group.command(name=cli_util.override('update_captchas.command_name', 'update'), help=u"""Updates the list of CAPTCHA challenges in the Web Application Firewall configuration for a WAAS policy. This operation can create, update, or delete CAPTCHAs depending on the structure of the request body. Updating an existing CAPTCHA can be accomplished by changing the properties of the CAPTCHA object with a non-empty `key` property in the list. Creating a CAPTCHA can be accomplished by adding a new CAPTCHA object to the list without a `key` property. A `key` will be generated for the new CAPTCHA upon update. Deleting a CAPTCHA can be accomplished by removing the existing CAPTCHA object from the list. Any existing CAPTCHA with a `key` that is not present in the list of CAPTCHAs sent in the request will be deleted.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--captchas', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of CAPTCHA details.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_captchas(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, captchas, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', ctx)
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


@certificate_group.command(name=cli_util.override('update_certificate.command_name', 'update'), help=u"""It is not possible to update a certificate, only create and delete. Therefore, this operation can only update the display name, freeform tags, and defined tags of a certificate.""")
@cli_util.option('--certificate-id', required=True, help=u"""The [OCID] of the SSL certificate used in the WAAS policy. This number is generated when the certificate is added to the policy.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the SSL certificate. The name can be changed and does not need to be unique.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair without any defined schema.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A key-value pair with a defined schema that restricts the values of tags. These predefined keys are scoped to namespaces.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', ctx)
    result = client.update_certificate(
        certificate_id=certificate_id,
        update_certificate_details=details,
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


@device_fingerprint_challenge_group.command(name=cli_util.override('update_device_fingerprint_challenge.command_name', 'update'), help=u"""Updates the Device Fingerprint Challenge (DFC) settings in the Web Application Firewall configuration for a policy. The DFC generates a hashed signature of both virtual and real browsers based on 50+ attributes. These proprietary signatures are then leveraged for real-time correlation to identify and block malicious bots.

The signature is based on a library of attributes detected via JavaScript listeners; the attributes include OS, screen resolution, fonts, UserAgent, IP address, etc. We are constantly making improvements and considering new libraries to include in our DFC build. We can also exclude attributes from the signature as needed.

DFC collects attributes to generate a hashed signature about a client \u2013 if a fingerprint is not possible, then it will result in a block or alert action. Actions can be enforced across multiple devices if they share they have the same fingerprint.""")
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
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    details = {}
    details['isEnabled'] = is_enabled

    if action is not None:
        details['action'] = action

    if failure_threshold is not None:
        details['failureThreshold'] = failure_threshold

    if action_expiration_in_seconds is not None:
        details['actionExpirationInSeconds'] = action_expiration_in_seconds

    if failure_threshold_expiration_in_seconds is not None:
        details['failureThresholdExpirationInSeconds'] = failure_threshold_expiration_in_seconds

    if max_address_count is not None:
        details['maxAddressCount'] = max_address_count

    if max_address_count_expiration_in_seconds is not None:
        details['maxAddressCountExpirationInSeconds'] = max_address_count_expiration_in_seconds

    if challenge_settings is not None:
        details['challengeSettings'] = cli_util.parse_json_parameter("challenge_settings", challenge_settings)

    client = cli_util.build_client('waas', ctx)
    result = client.update_device_fingerprint_challenge(
        waas_policy_id=waas_policy_id,
        update_device_fingerprint_challenge_details=details,
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


@good_bot_group.command(name=cli_util.override('update_good_bots.command_name', 'update'), help=u"""Updates the list of good bots in the Web Application Firewall configuration for a policy. Only the fields specified in the request body will be updated, all other configuration properties will remain unchanged.

Good bots allows you to manage access for bots from known providers, such as Google or Baidu. For more information about good bots, please see [Bot Management].""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--good-bots', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_good_bots(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, good_bots, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', ctx)
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


@human_interaction_challenge_group.command(name=cli_util.override('update_human_interaction_challenge.command_name', 'update'), help=u"""Updates the Human Interaction Challenge (HIC) settings in the Web Application Firewall configuration for a WAAS policy. HIC is a countermeasure that allows the proxy to check the user's browser for various behaviors that distinguish a human presence from a bot.""")
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
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'set-http-header': {'module': 'waas', 'class': 'Header'}, 'challenge-settings': {'module': 'waas', 'class': 'BlockChallengeSettings'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'set-http-header': {'module': 'waas', 'class': 'Header'}, 'challenge-settings': {'module': 'waas', 'class': 'BlockChallengeSettings'}})
@cli_util.wrap_exceptions
def update_human_interaction_challenge(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, is_enabled, action, failure_threshold, action_expiration_in_seconds, failure_threshold_expiration_in_seconds, interaction_threshold, recording_period_in_seconds, set_http_header, challenge_settings, if_match):

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

    details = {}
    details['isEnabled'] = is_enabled

    if action is not None:
        details['action'] = action

    if failure_threshold is not None:
        details['failureThreshold'] = failure_threshold

    if action_expiration_in_seconds is not None:
        details['actionExpirationInSeconds'] = action_expiration_in_seconds

    if failure_threshold_expiration_in_seconds is not None:
        details['failureThresholdExpirationInSeconds'] = failure_threshold_expiration_in_seconds

    if interaction_threshold is not None:
        details['interactionThreshold'] = interaction_threshold

    if recording_period_in_seconds is not None:
        details['recordingPeriodInSeconds'] = recording_period_in_seconds

    if set_http_header is not None:
        details['setHttpHeader'] = cli_util.parse_json_parameter("set_http_header", set_http_header)

    if challenge_settings is not None:
        details['challengeSettings'] = cli_util.parse_json_parameter("challenge_settings", challenge_settings)

    client = cli_util.build_client('waas', ctx)
    result = client.update_human_interaction_challenge(
        waas_policy_id=waas_policy_id,
        update_human_interaction_challenge_details=details,
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


@js_challenge_group.command(name=cli_util.override('update_js_challenge.command_name', 'update'), help=u"""Updates the JavaScript challenge settings in the Web Application Firewall configuration for a WAAS policy. JavaScript Challenge validates that the client can accept JavaScript with a binary decision. For more information, see [Bot Management].""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Enables or disables the JavaScript challenge Web Application Firewall feature.""")
@cli_util.option('--action', type=custom_types.CliCaseInsensitiveChoice(["DETECT", "BLOCK"]), help=u"""The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.""")
@cli_util.option('--failure-threshold', type=click.INT, help=u"""The number of failed requests before taking action. If unspecified, defaults to `10`.""")
@cli_util.option('--action-expiration-in-seconds', type=click.INT, help=u"""The number of seconds between challenges from the same IP address. If unspecified, defaults to `60`.""")
@cli_util.option('--set-http-header', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the `action` is set to `DETECT`.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--challenge-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'set-http-header': {'module': 'waas', 'class': 'Header'}, 'challenge-settings': {'module': 'waas', 'class': 'BlockChallengeSettings'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'set-http-header': {'module': 'waas', 'class': 'Header'}, 'challenge-settings': {'module': 'waas', 'class': 'BlockChallengeSettings'}})
@cli_util.wrap_exceptions
def update_js_challenge(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, is_enabled, action, failure_threshold, action_expiration_in_seconds, set_http_header, challenge_settings, if_match):

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

    details = {}
    details['isEnabled'] = is_enabled

    if action is not None:
        details['action'] = action

    if failure_threshold is not None:
        details['failureThreshold'] = failure_threshold

    if action_expiration_in_seconds is not None:
        details['actionExpirationInSeconds'] = action_expiration_in_seconds

    if set_http_header is not None:
        details['setHttpHeader'] = cli_util.parse_json_parameter("set_http_header", set_http_header)

    if challenge_settings is not None:
        details['challengeSettings'] = cli_util.parse_json_parameter("challenge_settings", challenge_settings)

    client = cli_util.build_client('waas', ctx)
    result = client.update_js_challenge(
        waas_policy_id=waas_policy_id,
        update_js_challenge_details=details,
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


@policy_config_group.command(name=cli_util.override('update_policy_config.command_name', 'update'), help=u"""Updates the configuration for a WAAS policy. Only the fields specified in the request body will be updated; all other properties will remain unchanged.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--certificate-id', help=u"""The OCID of the SSL certificate to use if HTTPS is supported.""")
@cli_util.option('--is-https-enabled', type=click.BOOL, help=u"""Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.""")
@cli_util.option('--is-https-forced', type=click.BOOL, help=u"""Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_policy_config(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, certificate_id, is_https_enabled, is_https_forced, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

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

    client = cli_util.build_client('waas', ctx)
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


@protection_rule_group.command(name=cli_util.override('update_protection_rules.command_name', 'update'), help=u"""Updates the action for each specified protection rule. Requests can either be allowed, blocked, or trigger an alert if they meet the parameters of an applied rule. For more information on protection rules, see [WAF Protection Rules]. This operation can update or disable protection rules depending on the structure of the request body. Updating an existing protection rule can be accomplished by changing the properties of the protection rule object with a non-empty `key` property in the list.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--protection-rules', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_protection_rules(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, protection_rules, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', ctx)
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


@protection_settings_group.command(name=cli_util.override('update_protection_settings.command_name', 'update'), help=u"""Updates the protection settings in the Web Application Firewall configuration for a WAAS policy. Protection settings allow you define what action is taken when a request is blocked by the Web Application Firewall, such as returning a response code or block page. Only the fields specified in the request body will be updated; all other fields will remain unchanged.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--block-action', type=custom_types.CliCaseInsensitiveChoice(["SHOW_ERROR_PAGE", "SET_RESPONSE_CODE"]), help=u"""If `action` is set to `BLOCK`, this specifies how the traffic is blocked when detected as malicious by a protection rule. If unspecified, defaults to `SET_RESPONSE_CODE`.""")
@cli_util.option('--block-response-code', type=click.INT, help=u"""The response code returned when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`.""")
@cli_util.option('--block-error-page-message', help=u"""The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to 'Access to the website is blocked.'""")
@cli_util.option('--block-error-page-code', help=u"""The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`.""")
@cli_util.option('--block-error-page-description', help=u"""The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic is detected as malicious by a protection rule. If unspecified, defaults to `Access blocked by website owner. Please contact support.`""")
@cli_util.option('--max-argument-count', type=click.INT, help=u"""The maximum number of arguments allowed to be passed to your application before an action is taken. If unspecified, defaults to `255`.""")
@cli_util.option('--max-name-length-per-argument', type=click.INT, help=u"""The maximum length allowed for each argument name, in characters. If unspecified, defaults to `400`.""")
@cli_util.option('--max-total-name-length-of-arguments', type=click.INT, help=u"""The maximum length allowed for the sum of all argument names, in characters. If unspecified, defaults to `64000`.""")
@cli_util.option('--recommendations-period-in-days', type=click.INT, help=u"""The length of time to analyze traffic traffic, in days. After the analysis period, `WafRecommendations` will be populated. If unspecified, defaults to `10`.

Use `GET /waasPolicies/{waasPolicyId}/wafRecommendations` to view WAF recommendations.""")
@cli_util.option('--is-response-inspected', type=click.BOOL, help=u"""Inspects the response body of origin responses. Can be used to detect leakage of sensitive data. If unspecified, defaults to `false`.

**Note:** Only origin responses with a Content-Type matching a value in `mediaTypes` will be inspected.""")
@cli_util.option('--max-response-size-in-ki-b', type=click.INT, help=u"""The maximum response size to be fully inspected, in binary kilobytes (KiB). Anything over this limit will be partially inspected. If unspecified, defaults to `1024`.""")
@cli_util.option('--allowed-http-methods', type=custom_types.CliCaseInsensitiveChoice(["OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT", "PATCH", "PROPFIND"]), help=u"""The list of allowed HTTP methods. If unspecified, default to `[OPTIONS, GET, HEAD, POST]`.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--media-types', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of media types to allow for inspection, if `isResponseInspected` is enabled. Only responses with MIME types in this list will be inspected. If unspecified, defaults to `[`text/html`, `text/plain`, `text/xml`]`.

    Supported MIME types include:

    - text/html     - text/plain     - text/asp     - text/css     - text/x-script     - application/json     - text/webviewhtml     - text/x-java-source     - application/x-javascript     - application/javascript     - application/ecmascript     - text/javascript     - text/ecmascript     - text/x-script.perl     - text/x-script.phyton     - application/plain     - application/xml     - text/xml""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'allowed-http-methods': {'module': 'waas', 'class': 'list[string]'}, 'media-types': {'module': 'waas', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'allowed-http-methods': {'module': 'waas', 'class': 'list[string]'}, 'media-types': {'module': 'waas', 'class': 'list[string]'}})
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

    details = {}

    if block_action is not None:
        details['blockAction'] = block_action

    if block_response_code is not None:
        details['blockResponseCode'] = block_response_code

    if block_error_page_message is not None:
        details['blockErrorPageMessage'] = block_error_page_message

    if block_error_page_code is not None:
        details['blockErrorPageCode'] = block_error_page_code

    if block_error_page_description is not None:
        details['blockErrorPageDescription'] = block_error_page_description

    if max_argument_count is not None:
        details['maxArgumentCount'] = max_argument_count

    if max_name_length_per_argument is not None:
        details['maxNameLengthPerArgument'] = max_name_length_per_argument

    if max_total_name_length_of_arguments is not None:
        details['maxTotalNameLengthOfArguments'] = max_total_name_length_of_arguments

    if recommendations_period_in_days is not None:
        details['recommendationsPeriodInDays'] = recommendations_period_in_days

    if is_response_inspected is not None:
        details['isResponseInspected'] = is_response_inspected

    if max_response_size_in_ki_b is not None:
        details['maxResponseSizeInKiB'] = max_response_size_in_ki_b

    if allowed_http_methods is not None:
        details['allowedHttpMethods'] = cli_util.parse_json_parameter("allowed_http_methods", allowed_http_methods)

    if media_types is not None:
        details['mediaTypes'] = cli_util.parse_json_parameter("media_types", media_types)

    client = cli_util.build_client('waas', ctx)
    result = client.update_protection_settings(
        waas_policy_id=waas_policy_id,
        update_protection_settings_details=details,
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


@threat_feed_group.command(name=cli_util.override('update_threat_feeds.command_name', 'update'), help=u"""Updates the action to take when a request's IP address matches an address in the specified threat intelligence feed. Threat intelligence feeds are compiled lists of IP addresses with malicious reputations based on internet intelligence. Only the threat feeds specified in the request body will be updated; all other threat feeds will remain unchanged.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--threat-feeds', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of threat feeds for which to update the actions.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_threat_feeds(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, threat_feeds, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', ctx)
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


@waas_policy_group.command(name=cli_util.override('update_waas_policy.command_name', 'update'), help=u"""Updates the details of a WAAS policy, including origins and tags. Only the fields specified in the request body will be updated; all other properties will remain unchanged. To update platform provided resources such as `GoodBots`, `ProtectionRules`, and `ThreatFeeds` first retrieve the list of available resources with the related list operation such as `GetThreatFeeds` or `GetProtectionRules`. The returned list will contain objects with `key` properties that can be used to update the resource during the `UpdateWaasPolicy` request.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the WAAS policy. The name is can be changed and does not need to be unique.""")
@cli_util.option('--additional-domains', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of additional domains protected by this WAAS policy.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--origins', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.

This option is a JSON dictionary of type dict(str, Origin).  For documentation on Origin please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/Origin.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--policy-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--waf-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A simple key-value pair without any defined schema.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'additional-domains': {'module': 'waas', 'class': 'list[string]'}, 'origins': {'module': 'waas', 'class': 'dict(str, Origin)'}, 'policy-config': {'module': 'waas', 'class': 'PolicyConfig'}, 'waf-config': {'module': 'waas', 'class': 'WafConfig'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'additional-domains': {'module': 'waas', 'class': 'list[string]'}, 'origins': {'module': 'waas', 'class': 'dict(str, Origin)'}, 'policy-config': {'module': 'waas', 'class': 'PolicyConfig'}, 'waf-config': {'module': 'waas', 'class': 'WafConfig'}, 'freeform-tags': {'module': 'waas', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'waas', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_waas_policy(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, display_name, additional_domains, origins, policy_config, waf_config, freeform_tags, defined_tags, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')
    if not force:
        if additional_domains or origins or policy_config or waf_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to additional-domains and origins and policy-config and waf-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if additional_domains is not None:
        details['additionalDomains'] = cli_util.parse_json_parameter("additional_domains", additional_domains)

    if origins is not None:
        details['origins'] = cli_util.parse_json_parameter("origins", origins)

    if policy_config is not None:
        details['policyConfig'] = cli_util.parse_json_parameter("policy_config", policy_config)

    if waf_config is not None:
        details['wafConfig'] = cli_util.parse_json_parameter("waf_config", waf_config)

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('waas', ctx)
    result = client.update_waas_policy(
        waas_policy_id=waas_policy_id,
        update_waas_policy_details=details,
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


@address_rate_limiting_group.command(name=cli_util.override('update_waf_address_rate_limiting.command_name', 'update-waf'), help=u"""Updates the address rate limiting settings in the Web Application Firewall configuration for a policy. Rate limiting allows you to configure a threshold for the number of requests from a unique IP address for the given period. You can also define the response code for the requests from the same address that exceed the threshold.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--is-enabled', required=True, type=click.BOOL, help=u"""Enables or disables the address rate limiting Web Application Firewall feature.""")
@cli_util.option('--allowed-rate-per-address', type=click.INT, help=u"""The number of allowed requests per second from one IP address. If unspecified, defaults to `1`.""")
@cli_util.option('--max-delayed-count-per-address', type=click.INT, help=u"""The maximum number of requests allowed to be queued before subsequent requests are dropped. If unspecified, defaults to `10`.""")
@cli_util.option('--block-response-code', type=click.INT, help=u"""The response status code returned when a request is blocked. If unspecified, defaults to `503`.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
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

    details = {}
    details['isEnabled'] = is_enabled

    if allowed_rate_per_address is not None:
        details['allowedRatePerAddress'] = allowed_rate_per_address

    if max_delayed_count_per_address is not None:
        details['maxDelayedCountPerAddress'] = max_delayed_count_per_address

    if block_response_code is not None:
        details['blockResponseCode'] = block_response_code

    client = cli_util.build_client('waas', ctx)
    result = client.update_waf_address_rate_limiting(
        waas_policy_id=waas_policy_id,
        update_waf_address_rate_limiting_details=details,
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


@waf_config_group.command(name=cli_util.override('update_waf_config.command_name', 'update'), help=u"""Updates the Web Application Firewall configuration for a specified WAAS policy.

To update platform provided resources such as `GoodBots`, `ProtectionRules`, and `ThreatFeeds` first retrieve the list of available resources with the related list operation such as `GetThreatFeeds` or `GetProtectionRules`.

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
@cli_util.option('--protection-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of the protection rules and their details.

This option is a JSON list with items of type ProtectionRule.  For documentation on ProtectionRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/ProtectionRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--protection-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The settings to apply to protection rules.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--threat-feeds', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of threat intelligence feeds and the actions to apply to known malicious traffic based on internet intelligence.

This option is a JSON list with items of type ThreatFeed.  For documentation on ThreatFeed please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/ThreatFeed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--whitelists', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of IP addresses that bypass the Web Application Firewall.

This option is a JSON list with items of type Whitelist.  For documentation on Whitelist please see our API reference: https://docs.cloud.oracle.com/api/#/en/waas/20181116/datatypes/Whitelist.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'access-rules': {'module': 'waas', 'class': 'list[AccessRule]'}, 'address-rate-limiting': {'module': 'waas', 'class': 'AddressRateLimiting'}, 'captchas': {'module': 'waas', 'class': 'list[Captcha]'}, 'device-fingerprint-challenge': {'module': 'waas', 'class': 'DeviceFingerprintChallenge'}, 'good-bots': {'module': 'waas', 'class': 'list[GoodBot]'}, 'human-interaction-challenge': {'module': 'waas', 'class': 'HumanInteractionChallenge'}, 'js-challenge': {'module': 'waas', 'class': 'JsChallenge'}, 'protection-rules': {'module': 'waas', 'class': 'list[ProtectionRule]'}, 'protection-settings': {'module': 'waas', 'class': 'ProtectionSettings'}, 'threat-feeds': {'module': 'waas', 'class': 'list[ThreatFeed]'}, 'whitelists': {'module': 'waas', 'class': 'list[Whitelist]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'access-rules': {'module': 'waas', 'class': 'list[AccessRule]'}, 'address-rate-limiting': {'module': 'waas', 'class': 'AddressRateLimiting'}, 'captchas': {'module': 'waas', 'class': 'list[Captcha]'}, 'device-fingerprint-challenge': {'module': 'waas', 'class': 'DeviceFingerprintChallenge'}, 'good-bots': {'module': 'waas', 'class': 'list[GoodBot]'}, 'human-interaction-challenge': {'module': 'waas', 'class': 'HumanInteractionChallenge'}, 'js-challenge': {'module': 'waas', 'class': 'JsChallenge'}, 'protection-rules': {'module': 'waas', 'class': 'list[ProtectionRule]'}, 'protection-settings': {'module': 'waas', 'class': 'ProtectionSettings'}, 'threat-feeds': {'module': 'waas', 'class': 'list[ThreatFeed]'}, 'whitelists': {'module': 'waas', 'class': 'list[Whitelist]'}})
@cli_util.wrap_exceptions
def update_waf_config(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, access_rules, address_rate_limiting, captchas, device_fingerprint_challenge, good_bots, human_interaction_challenge, js_challenge, origin, protection_rules, protection_settings, threat_feeds, whitelists, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')
    if not force:
        if access_rules or address_rate_limiting or captchas or device_fingerprint_challenge or good_bots or human_interaction_challenge or js_challenge or protection_rules or protection_settings or threat_feeds or whitelists:
            if not click.confirm("WARNING: Updates to access-rules and address-rate-limiting and captchas and device-fingerprint-challenge and good-bots and human-interaction-challenge and js-challenge and protection-rules and protection-settings and threat-feeds and whitelists will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if access_rules is not None:
        details['accessRules'] = cli_util.parse_json_parameter("access_rules", access_rules)

    if address_rate_limiting is not None:
        details['addressRateLimiting'] = cli_util.parse_json_parameter("address_rate_limiting", address_rate_limiting)

    if captchas is not None:
        details['captchas'] = cli_util.parse_json_parameter("captchas", captchas)

    if device_fingerprint_challenge is not None:
        details['deviceFingerprintChallenge'] = cli_util.parse_json_parameter("device_fingerprint_challenge", device_fingerprint_challenge)

    if good_bots is not None:
        details['goodBots'] = cli_util.parse_json_parameter("good_bots", good_bots)

    if human_interaction_challenge is not None:
        details['humanInteractionChallenge'] = cli_util.parse_json_parameter("human_interaction_challenge", human_interaction_challenge)

    if js_challenge is not None:
        details['jsChallenge'] = cli_util.parse_json_parameter("js_challenge", js_challenge)

    if origin is not None:
        details['origin'] = origin

    if protection_rules is not None:
        details['protectionRules'] = cli_util.parse_json_parameter("protection_rules", protection_rules)

    if protection_settings is not None:
        details['protectionSettings'] = cli_util.parse_json_parameter("protection_settings", protection_settings)

    if threat_feeds is not None:
        details['threatFeeds'] = cli_util.parse_json_parameter("threat_feeds", threat_feeds)

    if whitelists is not None:
        details['whitelists'] = cli_util.parse_json_parameter("whitelists", whitelists)

    client = cli_util.build_client('waas', ctx)
    result = client.update_waf_config(
        waas_policy_id=waas_policy_id,
        update_waf_config_details=details,
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


@whitelist_group.command(name=cli_util.override('update_whitelists.command_name', 'update'), help=u"""Updates the list of IP addresses that bypass the Web Application Firewall for a WAAS policy. Supports both single IP addresses or subnet masks (CIDR notation). This operation can create, delete, update, and/or reorder whitelists depending on the structure of the request body. Updating an existing whitelist can be accomplished by changing the properties of the whitelist object with a non-empty `key` property in the list. Reordering of whitelists can be accomplished by changing the order of the whitelists in the list when updating. Creating a whitelist can be accomplished by adding a new whitelist object to the list without a `key` property. A `key` will be generated for the new whitelist upon update. Deleting a whitelist can be accomplished by removing the existing whitelist object from the list. Any existing whitelist with a `key` that is not present in the list of whitelists sent in the request will be deleted.""")
@cli_util.option('--waas-policy-id', required=True, help=u"""The [OCID] of the WAAS policy.""")
@cli_util.option('--whitelists', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_whitelists(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, waas_policy_id, whitelists, if_match):

    if isinstance(waas_policy_id, six.string_types) and len(waas_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --waas-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('waas', ctx)
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
