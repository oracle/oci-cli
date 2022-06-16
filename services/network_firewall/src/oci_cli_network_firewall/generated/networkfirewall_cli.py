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


@cli.command(cli_util.override('network_firewall.network_firewall_root_group.command_name', 'network-firewall'), cls=CommandGroupWithAlias, help=cli_util.override('network_firewall.network_firewall_root_group.help', """Use the Network Firewall API to create network firewalls and configure policies that regulates network traffic in and across VCNs."""), short_help=cli_util.override('network_firewall.network_firewall_root_group.short_help', """Network Firewall API"""))
@cli_util.help_option_group
def network_firewall_root_group():
    pass


@click.command(cli_util.override('network_firewall.network_firewall_group.command_name', 'network-firewall'), cls=CommandGroupWithAlias, help="""Description of Network Firewall.""")
@cli_util.help_option_group
def network_firewall_group():
    pass


@click.command(cli_util.override('network_firewall.network_firewall_policy_group.command_name', 'network-firewall-policy'), cls=CommandGroupWithAlias, help="""Description of NetworkFirewall Policy.""")
@cli_util.help_option_group
def network_firewall_policy_group():
    pass


@click.command(cli_util.override('network_firewall.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('network_firewall.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('network_firewall.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status""")
@cli_util.help_option_group
def work_request_group():
    pass


network_firewall_root_group.add_command(network_firewall_group)
network_firewall_root_group.add_command(network_firewall_policy_group)
network_firewall_root_group.add_command(work_request_error_group)
network_firewall_root_group.add_command(work_request_log_entry_group)
network_firewall_root_group.add_command(work_request_group)


@work_request_group.command(name=cli_util.override('network_firewall.cancel_work_request.command_name', 'cancel'), help=u"""Cancel work request with the given ID. \n[Command Reference](cancelWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
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
    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@network_firewall_group.command(name=cli_util.override('network_firewall.change_network_firewall_compartment.command_name', 'change-compartment'), help=u"""Moves a NetworkFirewall resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeNetworkFirewallCompartment)""")
@cli_util.option('--network-firewall-id', required=True, help=u"""The [OCID] of the Network Firewall resource.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the Network Firewalll resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_network_firewall_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_firewall_id, compartment_id, if_match):

    if isinstance(network_firewall_id, six.string_types) and len(network_firewall_id.strip()) == 0:
        raise click.UsageError('Parameter --network-firewall-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    result = client.change_network_firewall_compartment(
        network_firewall_id=network_firewall_id,
        change_network_firewall_compartment_details=_details,
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


@network_firewall_policy_group.command(name=cli_util.override('network_firewall.change_network_firewall_policy_compartment.command_name', 'change-compartment'), help=u"""Moves a NetworkFirewallPolicy resource from one compartment identifier to another. When provided, If-Match is checked against ETag values of the resource. \n[Command Reference](changeNetworkFirewallPolicyCompartment)""")
@cli_util.option('--network-firewall-policy-id', required=True, help=u"""Unique Network Firewall Policy identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_network_firewall_policy_compartment(ctx, from_json, network_firewall_policy_id, compartment_id, if_match):

    if isinstance(network_firewall_policy_id, six.string_types) and len(network_firewall_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --network-firewall-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    result = client.change_network_firewall_policy_compartment(
        network_firewall_policy_id=network_firewall_policy_id,
        change_network_firewall_policy_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@network_firewall_group.command(name=cli_util.override('network_firewall.create_network_firewall.command_name', 'create'), help=u"""Creates a new NetworkFirewall. \n[Command Reference](createNetworkFirewall)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the Network Firewall.""")
@cli_util.option('--subnet-id', required=True, help=u"""The [OCID] of the subnet associated with the Network Firewall.""")
@cli_util.option('--network-firewall-policy-id', required=True, help=u"""The [OCID] of the Network Firewall Policy.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--availability-domain', help=u"""Availability Domain where Network Firewall instance is created. To get a list of availability domains for a tenancy, use [ListAvailabilityDomains] operation. Example: `kIdk:PHX-AD-1`""")
@cli_util.option('--ipv4-address', help=u"""IPv4 address for the Network Firewall.""")
@cli_util.option('--ipv6-address', help=u"""IPv6 address for the Network Firewall.""")
@cli_util.option('--network-security-group-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of network security groups [OCID] associated with the Network Firewall.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-security-group-ids': {'module': 'network_firewall', 'class': 'list[string]'}, 'freeform-tags': {'module': 'network_firewall', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'network_firewall', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-security-group-ids': {'module': 'network_firewall', 'class': 'list[string]'}, 'freeform-tags': {'module': 'network_firewall', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'network_firewall', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'network_firewall', 'class': 'NetworkFirewall'})
@cli_util.wrap_exceptions
def create_network_firewall(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, subnet_id, network_firewall_policy_id, display_name, availability_domain, ipv4_address, ipv6_address, network_security_group_ids, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['subnetId'] = subnet_id
    _details['networkFirewallPolicyId'] = network_firewall_policy_id

    if display_name is not None:
        _details['displayName'] = display_name

    if availability_domain is not None:
        _details['availabilityDomain'] = availability_domain

    if ipv4_address is not None:
        _details['ipv4Address'] = ipv4_address

    if ipv6_address is not None:
        _details['ipv6Address'] = ipv6_address

    if network_security_group_ids is not None:
        _details['networkSecurityGroupIds'] = cli_util.parse_json_parameter("network_security_group_ids", network_security_group_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    result = client.create_network_firewall(
        create_network_firewall_details=_details,
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


@network_firewall_policy_group.command(name=cli_util.override('network_firewall.create_network_firewall_policy.command_name', 'create'), help=u"""Creates a new Network Firewall Policy. \n[Command Reference](createNetworkFirewallPolicy)""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment containing the NetworkFirewall Policy.""")
@cli_util.option('--display-name', help=u"""A user-friendly optional name for the firewall policy. Avoid entering confidential information.""")
@cli_util.option('--mapped-secrets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map defining secrets of the policy. The value of an entry is a \"mapped secret\" consisting of a purpose and source. The associated key is the identifier by which the mapped secret is referenced.

This option is a JSON dictionary of type dict(str, MappedSecret).  For documentation on MappedSecret please see our API reference: https://docs.cloud.oracle.com/api/#/en/networkfirewall/20211001/datatypes/MappedSecret.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-lists', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map defining application lists of the policy. The value of an entry is a list of \"applications\", each consisting of a protocol identifier (such as TCP, UDP, or ICMP) and protocol-specific parameters (such as a port range). The associated key is the identifier by which the application list is referenced.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--url-lists', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map defining URL pattern lists of the policy. The value of an entry is a list of URL patterns. The associated key is the identifier by which the URL pattern list is referenced.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ip-address-lists', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map defining IP address lists of the policy. The value of an entry is a list of IP addresses or prefixes in CIDR notation. The associated key is the identifier by which the IP address list is referenced.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--security-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Security Rules defining the behavior of the policy. The first rule with a matching condition determines the action taken upon network traffic.

This option is a JSON list with items of type SecurityRule.  For documentation on SecurityRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/networkfirewall/20211001/datatypes/SecurityRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--decryption-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Decryption Rules defining the behavior of the policy. The first rule with a matching condition determines the action taken upon network traffic.

This option is a JSON list with items of type DecryptionRule.  For documentation on DecryptionRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/networkfirewall/20211001/datatypes/DecryptionRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--decryption-profiles', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map defining decryption profiles of the policy. The value of an entry is a decryption profile. The associated key is the identifier by which the decryption profile is referenced.

This option is a JSON dictionary of type dict(str, DecryptionProfile).  For documentation on DecryptionProfile please see our API reference: https://docs.cloud.oracle.com/api/#/en/networkfirewall/20211001/datatypes/DecryptionProfile.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'mapped-secrets': {'module': 'network_firewall', 'class': 'dict(str, MappedSecret)'}, 'application-lists': {'module': 'network_firewall', 'class': 'dict(str, list[Application])'}, 'url-lists': {'module': 'network_firewall', 'class': 'dict(str, list[UrlPattern])'}, 'ip-address-lists': {'module': 'network_firewall', 'class': 'dict(str, list[string])'}, 'security-rules': {'module': 'network_firewall', 'class': 'list[SecurityRule]'}, 'decryption-rules': {'module': 'network_firewall', 'class': 'list[DecryptionRule]'}, 'decryption-profiles': {'module': 'network_firewall', 'class': 'dict(str, DecryptionProfile)'}, 'freeform-tags': {'module': 'network_firewall', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'network_firewall', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'mapped-secrets': {'module': 'network_firewall', 'class': 'dict(str, MappedSecret)'}, 'application-lists': {'module': 'network_firewall', 'class': 'dict(str, list[Application])'}, 'url-lists': {'module': 'network_firewall', 'class': 'dict(str, list[UrlPattern])'}, 'ip-address-lists': {'module': 'network_firewall', 'class': 'dict(str, list[string])'}, 'security-rules': {'module': 'network_firewall', 'class': 'list[SecurityRule]'}, 'decryption-rules': {'module': 'network_firewall', 'class': 'list[DecryptionRule]'}, 'decryption-profiles': {'module': 'network_firewall', 'class': 'dict(str, DecryptionProfile)'}, 'freeform-tags': {'module': 'network_firewall', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'network_firewall', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'network_firewall', 'class': 'NetworkFirewallPolicy'})
@cli_util.wrap_exceptions
def create_network_firewall_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, mapped_secrets, application_lists, url_lists, ip_address_lists, security_rules, decryption_rules, decryption_profiles, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if mapped_secrets is not None:
        _details['mappedSecrets'] = cli_util.parse_json_parameter("mapped_secrets", mapped_secrets)

    if application_lists is not None:
        _details['applicationLists'] = cli_util.parse_json_parameter("application_lists", application_lists)

    if url_lists is not None:
        _details['urlLists'] = cli_util.parse_json_parameter("url_lists", url_lists)

    if ip_address_lists is not None:
        _details['ipAddressLists'] = cli_util.parse_json_parameter("ip_address_lists", ip_address_lists)

    if security_rules is not None:
        _details['securityRules'] = cli_util.parse_json_parameter("security_rules", security_rules)

    if decryption_rules is not None:
        _details['decryptionRules'] = cli_util.parse_json_parameter("decryption_rules", decryption_rules)

    if decryption_profiles is not None:
        _details['decryptionProfiles'] = cli_util.parse_json_parameter("decryption_profiles", decryption_profiles)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    result = client.create_network_firewall_policy(
        create_network_firewall_policy_details=_details,
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


@network_firewall_group.command(name=cli_util.override('network_firewall.delete_network_firewall.command_name', 'delete'), help=u"""Deletes a NetworkFirewall resource by identifier \n[Command Reference](deleteNetworkFirewall)""")
@cli_util.option('--network-firewall-id', required=True, help=u"""The [OCID] of the Network Firewall resource.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_network_firewall(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_firewall_id, if_match):

    if isinstance(network_firewall_id, six.string_types) and len(network_firewall_id.strip()) == 0:
        raise click.UsageError('Parameter --network-firewall-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    result = client.delete_network_firewall(
        network_firewall_id=network_firewall_id,
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


@network_firewall_policy_group.command(name=cli_util.override('network_firewall.delete_network_firewall_policy.command_name', 'delete'), help=u"""Deletes a NetworkFirewallPolicy resource with the given identifier. \n[Command Reference](deleteNetworkFirewallPolicy)""")
@cli_util.option('--network-firewall-policy-id', required=True, help=u"""Unique Network Firewall Policy identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_network_firewall_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, network_firewall_policy_id, if_match):

    if isinstance(network_firewall_policy_id, six.string_types) and len(network_firewall_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --network-firewall-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    result = client.delete_network_firewall_policy(
        network_firewall_policy_id=network_firewall_policy_id,
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


@network_firewall_group.command(name=cli_util.override('network_firewall.get_network_firewall.command_name', 'get'), help=u"""Gets a NetworkFirewall by identifier \n[Command Reference](getNetworkFirewall)""")
@cli_util.option('--network-firewall-id', required=True, help=u"""The [OCID] of the Network Firewall resource.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_firewall', 'class': 'NetworkFirewall'})
@cli_util.wrap_exceptions
def get_network_firewall(ctx, from_json, network_firewall_id):

    if isinstance(network_firewall_id, six.string_types) and len(network_firewall_id.strip()) == 0:
        raise click.UsageError('Parameter --network-firewall-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    result = client.get_network_firewall(
        network_firewall_id=network_firewall_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@network_firewall_policy_group.command(name=cli_util.override('network_firewall.get_network_firewall_policy.command_name', 'get'), help=u"""Gets a NetworkFirewallPolicy given the network firewall policy identifier. \n[Command Reference](getNetworkFirewallPolicy)""")
@cli_util.option('--network-firewall-policy-id', required=True, help=u"""Unique Network Firewall Policy identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_firewall', 'class': 'NetworkFirewallPolicy'})
@cli_util.wrap_exceptions
def get_network_firewall_policy(ctx, from_json, network_firewall_policy_id):

    if isinstance(network_firewall_policy_id, six.string_types) and len(network_firewall_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --network-firewall-policy-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    result = client.get_network_firewall_policy(
        network_firewall_policy_id=network_firewall_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('network_firewall.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_firewall', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@network_firewall_policy_group.command(name=cli_util.override('network_firewall.list_network_firewall_policies.command_name', 'list'), help=u"""Returns a list of Network Firewall Policies. \n[Command Reference](listNetworkFirewallPolicies)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""Unique Network Firewall Policy identifier""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources with a lifecycleState matching the given value.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_firewall', 'class': 'NetworkFirewallPolicySummaryCollection'})
@cli_util.wrap_exceptions
def list_network_firewall_policies(ctx, from_json, all_pages, page_size, compartment_id, display_name, id, limit, page, lifecycle_state, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
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
    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_network_firewall_policies,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_network_firewall_policies,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_network_firewall_policies(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@network_firewall_group.command(name=cli_util.override('network_firewall.list_network_firewalls.command_name', 'list'), help=u"""Returns a list of NetworkFirewalls. \n[Command Reference](listNetworkFirewalls)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--network-firewall-policy-id', help=u"""A filter to return only resources that match the entire networkFirewallPolicyId given.""")
@cli_util.option('--id', help=u"""The [OCID] of the Network Firewall resource.""")
@cli_util.option('--availability-domain', help=u"""A filter to return only resources that are present within the specified availability domain. To get a list of availability domains for a tenancy, use [ListAvailabilityDomains] operation. Example: `kIdk:PHX-AD-1`""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources with a lifecycleState matching the given value.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_firewall', 'class': 'NetworkFirewallCollection'})
@cli_util.wrap_exceptions
def list_network_firewalls(ctx, from_json, all_pages, page_size, compartment_id, display_name, network_firewall_policy_id, id, availability_domain, limit, page, lifecycle_state, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if network_firewall_policy_id is not None:
        kwargs['network_firewall_policy_id'] = network_firewall_policy_id
    if id is not None:
        kwargs['id'] = id
    if availability_domain is not None:
        kwargs['availability_domain'] = availability_domain
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
    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_network_firewalls,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_network_firewalls,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_network_firewalls(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('network_firewall.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_firewall', 'class': 'WorkRequestErrorCollection'})
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
    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
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


@work_request_log_entry_group.command(name=cli_util.override('network_firewall.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The ID of the asynchronous request.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_firewall', 'class': 'WorkRequestLogEntryCollection'})
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
    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
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


@work_request_group.command(name=cli_util.override('network_firewall.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--work-request-id', help=u"""The ID of the asynchronous work request.""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help=u"""A filter to return only resources their lifecycleState matches the given OperationStatus.""")
@cli_util.option('--resource-id', help=u"""The ID of the resource affected by the work request.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` or `opc-prev-page` header field of a previous response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeAccepted"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeAccepted is descending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'network_firewall', 'class': 'WorkRequestSummaryCollection'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, work_request_id, status, resource_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if work_request_id is not None:
        kwargs['work_request_id'] = work_request_id
    if status is not None:
        kwargs['status'] = status
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
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


@network_firewall_group.command(name=cli_util.override('network_firewall.update_network_firewall.command_name', 'update'), help=u"""Updates the NetworkFirewall \n[Command Reference](updateNetworkFirewall)""")
@cli_util.option('--network-firewall-id', required=True, help=u"""The [OCID] of the Network Firewall resource.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the Network Firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--network-firewall-policy-id', help=u"""The [OCID] of the Network Firewall Policy.""")
@cli_util.option('--network-security-group-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of network security groups [OCID] associated with the Network Firewall.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'network-security-group-ids': {'module': 'network_firewall', 'class': 'list[string]'}, 'freeform-tags': {'module': 'network_firewall', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'network_firewall', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'network-security-group-ids': {'module': 'network_firewall', 'class': 'list[string]'}, 'freeform-tags': {'module': 'network_firewall', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'network_firewall', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_network_firewall(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, network_firewall_id, display_name, network_firewall_policy_id, network_security_group_ids, freeform_tags, defined_tags, if_match):

    if isinstance(network_firewall_id, six.string_types) and len(network_firewall_id.strip()) == 0:
        raise click.UsageError('Parameter --network-firewall-id cannot be whitespace or empty string')
    if not force:
        if network_security_group_ids or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to network-security-group-ids and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if network_firewall_policy_id is not None:
        _details['networkFirewallPolicyId'] = network_firewall_policy_id

    if network_security_group_ids is not None:
        _details['networkSecurityGroupIds'] = cli_util.parse_json_parameter("network_security_group_ids", network_security_group_ids)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    result = client.update_network_firewall(
        network_firewall_id=network_firewall_id,
        update_network_firewall_details=_details,
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


@network_firewall_policy_group.command(name=cli_util.override('network_firewall.update_network_firewall_policy.command_name', 'update'), help=u"""Updates the NetworkFirewallPolicy \n[Command Reference](updateNetworkFirewallPolicy)""")
@cli_util.option('--network-firewall-policy-id', required=True, help=u"""Unique Network Firewall Policy identifier""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the firewall. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--mapped-secrets', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map defining secrets of the policy. The value of an entry is a \"mapped secret\" consisting of a purpose and source. The associated key is the identifier by which the mapped secret is referenced.

This option is a JSON dictionary of type dict(str, MappedSecret).  For documentation on MappedSecret please see our API reference: https://docs.cloud.oracle.com/api/#/en/networkfirewall/20211001/datatypes/MappedSecret.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-lists', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map defining application lists of the policy. The value of an entry is a list of \"applications\", each consisting of a protocol identifier (such as TCP, UDP, or ICMP) and protocol-specific parameters (such as a port range). The associated key is the identifier by which the application list is referenced.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--url-lists', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map defining URL pattern lists of the policy. The value of an entry is a list of URL patterns. The associated key is the identifier by which the URL pattern list is referenced.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ip-address-lists', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map defining IP address lists of the policy. The value of an entry is a list of IP addresses or prefixes in CIDR notation. The associated key is the identifier by which the IP address list is referenced.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--security-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Security Rules defining the behavior of the policy. The first rule with a matching condition determines the action taken upon network traffic.

This option is a JSON list with items of type SecurityRule.  For documentation on SecurityRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/networkfirewall/20211001/datatypes/SecurityRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--decryption-rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of Decryption Rules defining the behavior of the policy. The first rule with a matching condition determines the action taken upon network traffic.

This option is a JSON list with items of type DecryptionRule.  For documentation on DecryptionRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/networkfirewall/20211001/datatypes/DecryptionRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--decryption-profiles', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Map defining decryption profiles of the policy. The value of an entry is a decryption profile. The associated key is the identifier by which the decryption profile is referenced.

This option is a JSON dictionary of type dict(str, DecryptionProfile).  For documentation on DecryptionProfile please see our API reference: https://docs.cloud.oracle.com/api/#/en/networkfirewall/20211001/datatypes/DecryptionProfile.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "WAITING", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'mapped-secrets': {'module': 'network_firewall', 'class': 'dict(str, MappedSecret)'}, 'application-lists': {'module': 'network_firewall', 'class': 'dict(str, list[Application])'}, 'url-lists': {'module': 'network_firewall', 'class': 'dict(str, list[UrlPattern])'}, 'ip-address-lists': {'module': 'network_firewall', 'class': 'dict(str, list[string])'}, 'security-rules': {'module': 'network_firewall', 'class': 'list[SecurityRule]'}, 'decryption-rules': {'module': 'network_firewall', 'class': 'list[DecryptionRule]'}, 'decryption-profiles': {'module': 'network_firewall', 'class': 'dict(str, DecryptionProfile)'}, 'freeform-tags': {'module': 'network_firewall', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'network_firewall', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'mapped-secrets': {'module': 'network_firewall', 'class': 'dict(str, MappedSecret)'}, 'application-lists': {'module': 'network_firewall', 'class': 'dict(str, list[Application])'}, 'url-lists': {'module': 'network_firewall', 'class': 'dict(str, list[UrlPattern])'}, 'ip-address-lists': {'module': 'network_firewall', 'class': 'dict(str, list[string])'}, 'security-rules': {'module': 'network_firewall', 'class': 'list[SecurityRule]'}, 'decryption-rules': {'module': 'network_firewall', 'class': 'list[DecryptionRule]'}, 'decryption-profiles': {'module': 'network_firewall', 'class': 'dict(str, DecryptionProfile)'}, 'freeform-tags': {'module': 'network_firewall', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'network_firewall', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_network_firewall_policy(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, network_firewall_policy_id, display_name, mapped_secrets, application_lists, url_lists, ip_address_lists, security_rules, decryption_rules, decryption_profiles, freeform_tags, defined_tags, if_match):

    if isinstance(network_firewall_policy_id, six.string_types) and len(network_firewall_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --network-firewall-policy-id cannot be whitespace or empty string')
    if not force:
        if mapped_secrets or application_lists or url_lists or ip_address_lists or security_rules or decryption_rules or decryption_profiles or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to mapped-secrets and application-lists and url-lists and ip-address-lists and security-rules and decryption-rules and decryption-profiles and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if mapped_secrets is not None:
        _details['mappedSecrets'] = cli_util.parse_json_parameter("mapped_secrets", mapped_secrets)

    if application_lists is not None:
        _details['applicationLists'] = cli_util.parse_json_parameter("application_lists", application_lists)

    if url_lists is not None:
        _details['urlLists'] = cli_util.parse_json_parameter("url_lists", url_lists)

    if ip_address_lists is not None:
        _details['ipAddressLists'] = cli_util.parse_json_parameter("ip_address_lists", ip_address_lists)

    if security_rules is not None:
        _details['securityRules'] = cli_util.parse_json_parameter("security_rules", security_rules)

    if decryption_rules is not None:
        _details['decryptionRules'] = cli_util.parse_json_parameter("decryption_rules", decryption_rules)

    if decryption_profiles is not None:
        _details['decryptionProfiles'] = cli_util.parse_json_parameter("decryption_profiles", decryption_profiles)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('network_firewall', 'network_firewall', ctx)
    result = client.update_network_firewall_policy(
        network_firewall_policy_id=network_firewall_policy_id,
        update_network_firewall_policy_details=_details,
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
