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


@cli.command(cli_util.override('dns.dns_root_group.command_name', 'dns'), cls=CommandGroupWithAlias, help=cli_util.override('dns.dns_root_group.help', """API for the DNS service. Use this API to manage DNS zones, records, and other DNS resources.
For more information, see [Overview of the DNS Service]."""), short_help=cli_util.override('dns.dns_root_group.short_help', """DNS API"""))
@cli_util.help_option_group
def dns_root_group():
    pass


@click.command(cli_util.override('dns.resolver_group.command_name', 'resolver'), cls=CommandGroupWithAlias, help="""An OCI DNS resolver. If the resolver has an attached VCN, the VCN will attempt to answer queries based on the attached views in priority order. If the query does not match any of the attached views, the query will be evaluated against the default view. If the default view does not match, the rules will be evaluated in priority order. If no rules match the query, answers come from Internet DNS. A resolver may have a maximum of 10 resolver endpoints.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def resolver_group():
    pass


@click.command(cli_util.override('dns.view_group.command_name', 'view'), cls=CommandGroupWithAlias, help="""An OCI DNS view.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def view_group():
    pass


@click.command(cli_util.override('dns.zone_transfer_server_group.command_name', 'zone-transfer-server'), cls=CommandGroupWithAlias, help="""An OCI nameserver that transfers zone data with external nameservers.""")
@cli_util.help_option_group
def zone_transfer_server_group():
    pass


@click.command(cli_util.override('dns.steering_policy_attachment_group.command_name', 'steering-policy-attachment'), cls=CommandGroupWithAlias, help="""An attachment between a steering policy and a domain. An attachment constructs DNS responses using its steering policy instead of the records at its defined domain. Only records of the policy's covered rtype are blocked at the domain. A domain can have a maximum of one attachment covering any given rtype.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def steering_policy_attachment_group():
    pass


@click.command(cli_util.override('dns.zone_group.command_name', 'zone'), cls=CommandGroupWithAlias, help="""A DNS zone.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def zone_group():
    pass


@click.command(cli_util.override('dns.tsig_key_group.command_name', 'tsig-key'), cls=CommandGroupWithAlias, help="""A TSIG key. **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def tsig_key_group():
    pass


@click.command(cli_util.override('dns.rr_set_group.command_name', 'rr-set'), cls=CommandGroupWithAlias, help="""A collection of DNS records of the same domain and type. For more information about record types, see [Resource Record (RR) TYPEs].""")
@cli_util.help_option_group
def rr_set_group():
    pass


@click.command(cli_util.override('dns.steering_policy_group.command_name', 'steering-policy'), cls=CommandGroupWithAlias, help="""A DNS steering policy.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def steering_policy_group():
    pass


@click.command(cli_util.override('dns.resolver_endpoint_group.command_name', 'resolver-endpoint'), cls=CommandGroupWithAlias, help="""An OCI DNS resolver endpoint.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def resolver_endpoint_group():
    pass


@click.command(cli_util.override('dns.records_group.command_name', 'records'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def records_group():
    pass


dns_root_group.add_command(resolver_group)
dns_root_group.add_command(view_group)
dns_root_group.add_command(zone_transfer_server_group)
dns_root_group.add_command(steering_policy_attachment_group)
dns_root_group.add_command(zone_group)
dns_root_group.add_command(tsig_key_group)
dns_root_group.add_command(rr_set_group)
dns_root_group.add_command(steering_policy_group)
dns_root_group.add_command(resolver_endpoint_group)
dns_root_group.add_command(records_group)


@resolver_group.command(name=cli_util.override('dns.change_resolver_compartment.command_name', 'change-compartment'), help=u"""Moves a resolver into a different compartment along with its protected default view and any endpoints.

Zones in the default view are not moved. VCN-dedicated resolvers are initially created in the same compartment as their corresponding VCN, but can then be moved to a different compartment. \n[Command Reference](changeResolverCompartment)""")
@cli_util.option('--resolver-id', required=True, help=u"""The OCID of the target resolver.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resolver, along with its protected default view and resolver endpoints, should be moved.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_resolver_compartment(ctx, from_json, resolver_id, compartment_id, if_match, scope):

    if isinstance(resolver_id, six.string_types) and len(resolver_id.strip()) == 0:
        raise click.UsageError('Parameter --resolver-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.change_resolver_compartment(
        resolver_id=resolver_id,
        change_resolver_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@steering_policy_group.command(name=cli_util.override('dns.change_steering_policy_compartment.command_name', 'change-compartment'), help=u"""Moves a steering policy into a different compartment. \n[Command Reference](changeSteeringPolicyCompartment)""")
@cli_util.option('--steering-policy-id', required=True, help=u"""The OCID of the target steering policy.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the steering policy should be moved.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_steering_policy_compartment(ctx, from_json, steering_policy_id, compartment_id, if_match, scope):

    if isinstance(steering_policy_id, six.string_types) and len(steering_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --steering-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.change_steering_policy_compartment(
        steering_policy_id=steering_policy_id,
        change_steering_policy_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tsig_key_group.command(name=cli_util.override('dns.change_tsig_key_compartment.command_name', 'change-compartment'), help=u"""Moves a TSIG key into a different compartment. \n[Command Reference](changeTsigKeyCompartment)""")
@cli_util.option('--tsig-key-id', required=True, help=u"""The OCID of the target TSIG key.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the TSIG key should be moved.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_tsig_key_compartment(ctx, from_json, tsig_key_id, compartment_id, if_match, scope):

    if isinstance(tsig_key_id, six.string_types) and len(tsig_key_id.strip()) == 0:
        raise click.UsageError('Parameter --tsig-key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.change_tsig_key_compartment(
        tsig_key_id=tsig_key_id,
        change_tsig_key_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@view_group.command(name=cli_util.override('dns.change_view_compartment.command_name', 'change-compartment'), help=u"""Moves a view into a different compartment.

To change the compartment of a protected view, change the compartment of its corresponding resolver. \n[Command Reference](changeViewCompartment)""")
@cli_util.option('--view-id', required=True, help=u"""The OCID of the target view.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the view should be moved.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_view_compartment(ctx, from_json, view_id, compartment_id, if_match, scope):

    if isinstance(view_id, six.string_types) and len(view_id.strip()) == 0:
        raise click.UsageError('Parameter --view-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.change_view_compartment(
        view_id=view_id,
        change_view_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@zone_group.command(name=cli_util.override('dns.change_zone_compartment.command_name', 'change-compartment'), help=u"""Moves a zone into a different compartment.

Protected zones cannot have their compartment changed. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required.

**Note:** All SteeringPolicyAttachment objects associated with this zone will also be moved into the provided compartment. \n[Command Reference](changeZoneCompartment)""")
@cli_util.option('--zone-id', required=True, help=u"""The OCID of the target zone.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the zone should be moved.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_zone_compartment(ctx, from_json, zone_id, compartment_id, if_match, scope):

    if isinstance(zone_id, six.string_types) and len(zone_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.change_zone_compartment(
        zone_id=zone_id,
        change_zone_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@resolver_endpoint_group.command(name=cli_util.override('dns.create_resolver_endpoint.command_name', 'create'), help=u"""Creates a new resolver endpoint in the same compartment as the resolver. \n[Command Reference](createResolverEndpoint)""")
@cli_util.option('--resolver-id', required=True, help=u"""The OCID of the target resolver.""")
@cli_util.option('--name', required=True, help=u"""The name of the resolver endpoint. Must be unique, case-insensitive, within the resolver.""")
@cli_util.option('--is-forwarding', required=True, type=click.BOOL, help=u"""A Boolean flag indicating whether or not the resolver endpoint is for forwarding.""")
@cli_util.option('--is-listening', required=True, type=click.BOOL, help=u"""A Boolean flag indicating whether or not the resolver endpoint is for listening.""")
@cli_util.option('--endpoint-type', type=custom_types.CliCaseInsensitiveChoice(["VNIC"]), help=u"""The type of resolver endpoint. VNIC is currently the only supported type.""")
@cli_util.option('--forwarding-address', help=u"""An IP address from which forwarded queries may be sent. For VNIC endpoints, this IP address must be part of the subnet and will be assigned by the system if unspecified when isForwarding is true.""")
@cli_util.option('--listening-address', help=u"""An IP address to listen to queries on. For VNIC endpoints this IP address must be part of the subnet and will be assigned by the system if unspecified when isListening is true.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'ResolverEndpoint'})
@cli_util.wrap_exceptions
def create_resolver_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, resolver_id, name, is_forwarding, is_listening, endpoint_type, forwarding_address, listening_address, scope):

    if isinstance(resolver_id, six.string_types) and len(resolver_id.strip()) == 0:
        raise click.UsageError('Parameter --resolver-id cannot be whitespace or empty string')

    kwargs = {}
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['isForwarding'] = is_forwarding
    _details['isListening'] = is_listening

    if endpoint_type is not None:
        _details['endpointType'] = endpoint_type

    if forwarding_address is not None:
        _details['forwardingAddress'] = forwarding_address

    if listening_address is not None:
        _details['listeningAddress'] = listening_address

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.create_resolver_endpoint(
        resolver_id=resolver_id,
        create_resolver_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_resolver_endpoint') and callable(getattr(client, 'get_resolver_endpoint')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_resolver_endpoint(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@resolver_endpoint_group.command(name=cli_util.override('dns.create_resolver_endpoint_create_resolver_vnic_endpoint_details.command_name', 'create-resolver-endpoint-create-resolver-vnic-endpoint-details'), help=u"""Creates a new resolver endpoint in the same compartment as the resolver. \n[Command Reference](createResolverEndpoint)""")
@cli_util.option('--resolver-id', required=True, help=u"""The OCID of the target resolver.""")
@cli_util.option('--name', required=True, help=u"""The name of the resolver endpoint. Must be unique, case-insensitive, within the resolver.""")
@cli_util.option('--is-forwarding', required=True, type=click.BOOL, help=u"""A Boolean flag indicating whether or not the resolver endpoint is for forwarding.""")
@cli_util.option('--is-listening', required=True, type=click.BOOL, help=u"""A Boolean flag indicating whether or not the resolver endpoint is for listening.""")
@cli_util.option('--subnet-id', required=True, help=u"""The OCID of a subnet. Must be part of the VCN that the resolver is attached to.""")
@cli_util.option('--forwarding-address', help=u"""An IP address from which forwarded queries may be sent. For VNIC endpoints, this IP address must be part of the subnet and will be assigned by the system if unspecified when isForwarding is true.""")
@cli_util.option('--listening-address', help=u"""An IP address to listen to queries on. For VNIC endpoints this IP address must be part of the subnet and will be assigned by the system if unspecified when isListening is true.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the resolver endpoint is a part of.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nsg-ids': {'module': 'dns', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'dns', 'class': 'list[string]'}}, output_type={'module': 'dns', 'class': 'ResolverEndpoint'})
@cli_util.wrap_exceptions
def create_resolver_endpoint_create_resolver_vnic_endpoint_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, resolver_id, name, is_forwarding, is_listening, subnet_id, forwarding_address, listening_address, nsg_ids, scope):

    if isinstance(resolver_id, six.string_types) and len(resolver_id.strip()) == 0:
        raise click.UsageError('Parameter --resolver-id cannot be whitespace or empty string')

    kwargs = {}
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['isForwarding'] = is_forwarding
    _details['isListening'] = is_listening
    _details['subnetId'] = subnet_id

    if forwarding_address is not None:
        _details['forwardingAddress'] = forwarding_address

    if listening_address is not None:
        _details['listeningAddress'] = listening_address

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    _details['endpointType'] = 'VNIC'

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.create_resolver_endpoint(
        resolver_id=resolver_id,
        create_resolver_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_resolver_endpoint') and callable(getattr(client, 'get_resolver_endpoint')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_resolver_endpoint(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@steering_policy_group.command(name=cli_util.override('dns.create_steering_policy.command_name', 'create'), help=u"""Creates a new steering policy in the specified compartment. For more information on creating policies with templates, see [Traffic Management API Guide]. \n[Command Reference](createSteeringPolicy)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the steering policy.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly name for the steering policy. Does not have to be unique and can be changed. Avoid entering confidential information.""")
@cli_util.option('--template', required=True, type=custom_types.CliCaseInsensitiveChoice(["FAILOVER", "LOAD_BALANCE", "ROUTE_BY_GEO", "ROUTE_BY_ASN", "ROUTE_BY_IP", "CUSTOM"]), help=u"""A set of predefined rules based on the desired purpose of the steering policy. Each template utilizes Traffic Management's rules in a different order to produce the desired results when answering DNS queries.

 **Example:** The `FAILOVER` template determines answers by filtering the policy's answers using the `FILTER` rule first, then the following rules in succession: `HEALTH`, `PRIORITY`, and `LIMIT`. This gives the domain dynamic failover capability.

 It is **strongly recommended** to use a template other than `CUSTOM` when creating a steering policy.

 All templates require the rule order to begin with an unconditional `FILTER` rule that keeps answers contingent upon `answer.isDisabled != true`, except for `CUSTOM`. A defined `HEALTH` rule must follow the `FILTER` rule if the policy references a `healthCheckMonitorId`. The last rule of a template must must be a `LIMIT` rule. For more information about templates and code examples, see [Traffic Management API Guide].

**Template Types**

* `FAILOVER` - Uses health check information on your endpoints to determine which DNS answers to serve. If an endpoint fails a health check, the answer for that endpoint will be removed from the list of available answers until the endpoint is detected as healthy.

 * `LOAD_BALANCE` - Distributes web traffic to specified endpoints based on defined weights.

 * `ROUTE_BY_GEO` - Answers DNS queries based on the query's geographic location. For a list of geographic locations to route by, see [Traffic Management Geographic Locations].

 * `ROUTE_BY_ASN` - Answers DNS queries based on the query's originating ASN.

 * `ROUTE_BY_IP` - Answers DNS queries based on the query's IP address.

 * `CUSTOM` - Allows a customized configuration of rules.""")
@cli_util.option('--ttl', type=click.INT, help=u"""The Time To Live (TTL) for responses from the steering policy, in seconds. If not specified during creation, a value of 30 seconds will be used.""")
@cli_util.option('--health-check-monitor-id', help=u"""The OCID of the health check monitor providing health data about the answers of the steering policy. A steering policy answer with `rdata` matching a monitored endpoint will use the health data of that endpoint. A steering policy answer with `rdata` not matching any monitored endpoint will be assumed healthy.

 **Note:** To use the Health Check monitoring feature in a steering policy, a monitor must be created using the Health Checks service first. For more information on how to create a monitor, please see [Managing Health Checks].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

 **Example:** `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

 **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--answers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The set of all answers that can potentially issue from the steering policy.

This option is a JSON list with items of type SteeringPolicyAnswer.  For documentation on SteeringPolicyAnswer please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/SteeringPolicyAnswer.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The series of rules that will be processed in sequence to reduce the pool of answers to a response for any given request.

 The first rule receives a shuffled list of all answers, and every other rule receives the list of answers emitted by the one preceding it. The last rule populates the response.

This option is a JSON list with items of type SteeringPolicyRule.  For documentation on SteeringPolicyRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/SteeringPolicyRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'answers': {'module': 'dns', 'class': 'list[SteeringPolicyAnswer]'}, 'rules': {'module': 'dns', 'class': 'list[SteeringPolicyRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'answers': {'module': 'dns', 'class': 'list[SteeringPolicyAnswer]'}, 'rules': {'module': 'dns', 'class': 'list[SteeringPolicyRule]'}}, output_type={'module': 'dns', 'class': 'SteeringPolicy'})
@cli_util.wrap_exceptions
def create_steering_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, template, ttl, health_check_monitor_id, freeform_tags, defined_tags, answers, rules, scope):

    kwargs = {}
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['template'] = template

    if ttl is not None:
        _details['ttl'] = ttl

    if health_check_monitor_id is not None:
        _details['healthCheckMonitorId'] = health_check_monitor_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if answers is not None:
        _details['answers'] = cli_util.parse_json_parameter("answers", answers)

    if rules is not None:
        _details['rules'] = cli_util.parse_json_parameter("rules", rules)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.create_steering_policy(
        create_steering_policy_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_steering_policy') and callable(getattr(client, 'get_steering_policy')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_steering_policy(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@steering_policy_attachment_group.command(name=cli_util.override('dns.create_steering_policy_attachment.command_name', 'create'), help=u"""Creates a new attachment between a steering policy and a domain, giving the policy permission to answer queries for the specified domain. A steering policy must be attached to a domain for the policy to answer DNS queries for that domain.

For the purposes of access control, the attachment is automatically placed into the same compartment as the domain's zone. \n[Command Reference](createSteeringPolicyAttachment)""")
@cli_util.option('--steering-policy-id', required=True, help=u"""The OCID of the attached steering policy.""")
@cli_util.option('--zone-id', required=True, help=u"""The OCID of the attached zone.""")
@cli_util.option('--domain-name', required=True, help=u"""The attached domain within the attached zone.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'SteeringPolicyAttachment'})
@cli_util.wrap_exceptions
def create_steering_policy_attachment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, steering_policy_id, zone_id, domain_name, display_name, scope):

    kwargs = {}
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['steeringPolicyId'] = steering_policy_id
    _details['zoneId'] = zone_id
    _details['domainName'] = domain_name

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.create_steering_policy_attachment(
        create_steering_policy_attachment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_steering_policy_attachment') and callable(getattr(client, 'get_steering_policy_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_steering_policy_attachment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@tsig_key_group.command(name=cli_util.override('dns.create_tsig_key.command_name', 'create'), help=u"""Creates a new TSIG key in the specified compartment. There is no `opc-retry-token` header since TSIG key names must be globally unique. \n[Command Reference](createTsigKey)""")
@cli_util.option('--algorithm', required=True, help=u"""TSIG key algorithms are encoded as domain names, but most consist of only one non-empty label, which is not required to be explicitly absolute. Applicable algorithms include: hmac-sha1, hmac-sha224, hmac-sha256, hmac-sha512. For more information on these algorithms, see [RFC 4635].""")
@cli_util.option('--name', required=True, help=u"""A globally unique domain name identifying the key for a given pair of hosts.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the TSIG key.""")
@cli_util.option('--secret', required=True, help=u"""A base64 string encoding the binary shared secret.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

 **Example:** `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

 **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dns', 'class': 'TsigKey'})
@cli_util.wrap_exceptions
def create_tsig_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, algorithm, name, compartment_id, secret, freeform_tags, defined_tags, scope):

    kwargs = {}
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['algorithm'] = algorithm
    _details['name'] = name
    _details['compartmentId'] = compartment_id
    _details['secret'] = secret

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.create_tsig_key(
        create_tsig_key_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tsig_key') and callable(getattr(client, 'get_tsig_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tsig_key(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@view_group.command(name=cli_util.override('dns.create_view.command_name', 'create'), help=u"""Creates a new view in the specified compartment. \n[Command Reference](createView)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the owning compartment.""")
@cli_util.option('--display-name', help=u"""The display name of the view.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

 **Example:** `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

 **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "DELETING", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dns', 'class': 'View'})
@cli_util.wrap_exceptions
def create_view(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, freeform_tags, defined_tags, scope):

    kwargs = {}
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.create_view(
        create_view_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_view') and callable(getattr(client, 'get_view')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_view(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@zone_group.command(name=cli_util.override('dns.create_zone.command_name', 'create'), help=u"""Creates a new zone in the specified compartment.

Private zones must have a zone type of `PRIMARY`. Creating a private zone at or under `oraclevcn.com` within the default protected view of a VCN-dedicated resolver is not permitted. \n[Command Reference](createZone)""")
@cli_util.option('--name', required=True, help=u"""The name of the zone.""")
@cli_util.option('--migration-source', type=custom_types.CliCaseInsensitiveChoice(["NONE", "DYNECT"]), help=u"""Discriminator that is used to determine whether to create a new zone (NONE) or to migrate an existing DynECT zone (DYNECT).""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

 **Example:** `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

 **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dns', 'class': 'Zone'})
@cli_util.wrap_exceptions
def create_zone(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, migration_source, freeform_tags, defined_tags, compartment_id, scope, view_id):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id

    if migration_source is not None:
        _details['migrationSource'] = migration_source

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.create_zone(
        create_zone_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_zone') and callable(getattr(client, 'get_zone')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_zone(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@zone_group.command(name=cli_util.override('dns.create_zone_create_zone_details.command_name', 'create-zone-create-zone-details'), help=u"""Creates a new zone in the specified compartment.

Private zones must have a zone type of `PRIMARY`. Creating a private zone at or under `oraclevcn.com` within the default protected view of a VCN-dedicated resolver is not permitted. \n[Command Reference](createZone)""")
@cli_util.option('--name', required=True, help=u"""The name of the zone.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

 **Example:** `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

 **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--zone-type', type=custom_types.CliCaseInsensitiveChoice(["PRIMARY", "SECONDARY"]), help=u"""The type of the zone. Must be either `PRIMARY` or `SECONDARY`. `SECONDARY` is only supported for GLOBAL zones.""")
@cli_util.option('--external-masters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""External master servers for the zone. `externalMasters` becomes a required parameter when the `zoneType` value is `SECONDARY`.

This option is a JSON list with items of type ExternalMaster.  For documentation on ExternalMaster please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/ExternalMaster.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'external-masters': {'module': 'dns', 'class': 'list[ExternalMaster]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'external-masters': {'module': 'dns', 'class': 'list[ExternalMaster]'}}, output_type={'module': 'dns', 'class': 'Zone'})
@cli_util.wrap_exceptions
def create_zone_create_zone_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, freeform_tags, defined_tags, zone_type, external_masters, compartment_id, scope, view_id):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if zone_type is not None:
        _details['zoneType'] = zone_type

    if view_id is not None:
        _details['viewId'] = view_id

    if scope is not None:
        _details['scope'] = scope

    if external_masters is not None:
        _details['externalMasters'] = cli_util.parse_json_parameter("external_masters", external_masters)

    _details['migrationSource'] = 'NONE'

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.create_zone(
        create_zone_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_zone') and callable(getattr(client, 'get_zone')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_zone(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@zone_group.command(name=cli_util.override('dns.create_zone_create_migrated_dynect_zone_details.command_name', 'create-zone-create-migrated-dynect-zone-details'), help=u"""Creates a new zone in the specified compartment.

Private zones must have a zone type of `PRIMARY`. Creating a private zone at or under `oraclevcn.com` within the default protected view of a VCN-dedicated resolver is not permitted. \n[Command Reference](createZone)""")
@cli_util.option('--name', required=True, help=u"""The name of the zone.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

 **Example:** `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

 **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dynect-migration-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'dynect-migration-details': {'module': 'dns', 'class': 'DynectMigrationDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'dynect-migration-details': {'module': 'dns', 'class': 'DynectMigrationDetails'}}, output_type={'module': 'dns', 'class': 'Zone'})
@cli_util.wrap_exceptions
def create_zone_create_migrated_dynect_zone_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, freeform_tags, defined_tags, dynect_migration_details, compartment_id, scope, view_id):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['name'] = name
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if dynect_migration_details is not None:
        _details['dynectMigrationDetails'] = cli_util.parse_json_parameter("dynect_migration_details", dynect_migration_details)

    _details['migrationSource'] = 'DYNECT'

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.create_zone(
        create_zone_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_zone') and callable(getattr(client, 'get_zone')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_zone(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@records_group.command(name=cli_util.override('dns.delete_domain_records.command_name', 'delete-domain'), help=u"""Deletes all records at the specified zone and domain.

When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](deleteDomainRecords)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_domain_records(ctx, from_json, zone_name_or_id, domain, if_match, if_unmodified_since, scope, view_id, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    if isinstance(domain, six.string_types) and len(domain.strip()) == 0:
        raise click.UsageError('Parameter --domain cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.delete_domain_records(
        zone_name_or_id=zone_name_or_id,
        domain=domain,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@resolver_endpoint_group.command(name=cli_util.override('dns.delete_resolver_endpoint.command_name', 'delete'), help=u"""Deletes the specified resolver endpoint.

Note that attempting to delete a resolver endpoint in the DELETED lifecycle state will result in a `404` response to be consistent with other operations of the API. Resolver endpoints may not be deleted if they are referenced by a resolver rule. \n[Command Reference](deleteResolverEndpoint)""")
@cli_util.option('--resolver-id', required=True, help=u"""The OCID of the target resolver.""")
@cli_util.option('--resolver-endpoint-name', required=True, help=u"""The name of the target resolver endpoint.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_resolver_endpoint(ctx, from_json, resolver_id, resolver_endpoint_name, if_match, if_unmodified_since, scope):

    if isinstance(resolver_id, six.string_types) and len(resolver_id.strip()) == 0:
        raise click.UsageError('Parameter --resolver-id cannot be whitespace or empty string')

    if isinstance(resolver_endpoint_name, six.string_types) and len(resolver_endpoint_name.strip()) == 0:
        raise click.UsageError('Parameter --resolver-endpoint-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.delete_resolver_endpoint(
        resolver_id=resolver_id,
        resolver_endpoint_name=resolver_endpoint_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rr_set_group.command(name=cli_util.override('dns.delete_rr_set.command_name', 'delete'), help=u"""Deletes all records in the specified RRSet.

When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](deleteRRSet)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--rtype', required=True, help=u"""The type of the target RRSet within the target zone.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_rr_set(ctx, from_json, zone_name_or_id, domain, rtype, if_match, if_unmodified_since, compartment_id, scope, view_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    if isinstance(domain, six.string_types) and len(domain.strip()) == 0:
        raise click.UsageError('Parameter --domain cannot be whitespace or empty string')

    if isinstance(rtype, six.string_types) and len(rtype.strip()) == 0:
        raise click.UsageError('Parameter --rtype cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.delete_rr_set(
        zone_name_or_id=zone_name_or_id,
        domain=domain,
        rtype=rtype,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@steering_policy_group.command(name=cli_util.override('dns.delete_steering_policy.command_name', 'delete'), help=u"""Deletes the specified steering policy.

A `204` response indicates that the delete has been successful. Deletion will fail if the policy is attached to any zones. To detach a policy from a zone, see `DeleteSteeringPolicyAttachment`. \n[Command Reference](deleteSteeringPolicy)""")
@cli_util.option('--steering-policy-id', required=True, help=u"""The OCID of the target steering policy.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_steering_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, steering_policy_id, if_match, if_unmodified_since, scope):

    if isinstance(steering_policy_id, six.string_types) and len(steering_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --steering-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.delete_steering_policy(
        steering_policy_id=steering_policy_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_steering_policy') and callable(getattr(client, 'get_steering_policy')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_steering_policy(steering_policy_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@steering_policy_attachment_group.command(name=cli_util.override('dns.delete_steering_policy_attachment.command_name', 'delete'), help=u"""Deletes the specified steering policy attachment. A `204` response indicates that the delete has been successful. \n[Command Reference](deleteSteeringPolicyAttachment)""")
@cli_util.option('--steering-policy-attachment-id', required=True, help=u"""The OCID of the target steering policy attachment.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_steering_policy_attachment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, steering_policy_attachment_id, if_match, if_unmodified_since, scope):

    if isinstance(steering_policy_attachment_id, six.string_types) and len(steering_policy_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --steering-policy-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.delete_steering_policy_attachment(
        steering_policy_attachment_id=steering_policy_attachment_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_steering_policy_attachment') and callable(getattr(client, 'get_steering_policy_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_steering_policy_attachment(steering_policy_attachment_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@tsig_key_group.command(name=cli_util.override('dns.delete_tsig_key.command_name', 'delete'), help=u"""Deletes the specified TSIG key. \n[Command Reference](deleteTsigKey)""")
@cli_util.option('--tsig-key-id', required=True, help=u"""The OCID of the target TSIG key.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_tsig_key(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tsig_key_id, if_match, if_unmodified_since, scope):

    if isinstance(tsig_key_id, six.string_types) and len(tsig_key_id.strip()) == 0:
        raise click.UsageError('Parameter --tsig-key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.delete_tsig_key(
        tsig_key_id=tsig_key_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tsig_key') and callable(getattr(client, 'get_tsig_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_tsig_key(tsig_key_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@view_group.command(name=cli_util.override('dns.delete_view.command_name', 'delete'), help=u"""Deletes the specified view.

Note that attempting to delete a view in the DELETED lifecycleState will result in a `404` response to be consistent with other operations of the API. Views cannot be deleted if they are referenced by non-deleted zones or resolvers. Protected views cannot be deleted. \n[Command Reference](deleteView)""")
@cli_util.option('--view-id', required=True, help=u"""The OCID of the target view.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "DELETING", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_view(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, view_id, if_match, if_unmodified_since, scope):

    if isinstance(view_id, six.string_types) and len(view_id.strip()) == 0:
        raise click.UsageError('Parameter --view-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.delete_view(
        view_id=view_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_view') and callable(getattr(client, 'get_view')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_view(view_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@zone_group.command(name=cli_util.override('dns.delete_zone.command_name', 'delete'), help=u"""Deletes the specified zone and all its steering policy attachments.

A `204` response indicates that the zone has been successfully deleted. Protected zones cannot be deleted. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](deleteZone)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_zone(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, zone_name_or_id, if_match, if_unmodified_since, scope, view_id, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.delete_zone(
        zone_name_or_id=zone_name_or_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_zone') and callable(getattr(client, 'get_zone')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_zone(zone_name_or_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
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


@records_group.command(name=cli_util.override('dns.get_domain_records.command_name', 'get-domain'), help=u"""Gets a list of all records at the specified zone and domain.

The results are sorted by `rtype` in alphabetical order by default. You can optionally filter and/or sort the results using the listed parameters. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](getDomainRecords)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a page of the collection.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--zone-version', help=u"""The version of the zone for which data is requested.""")
@cli_util.option('--rtype', help=u"""Search by record type. Will match any record whose [type] (case-insensitive) equals the provided value.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["rtype", "ttl"]), help=u"""The field by which to sort records.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order to sort the resources.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def get_domain_records(ctx, from_json, all_pages, page_size, zone_name_or_id, domain, if_none_match, if_modified_since, limit, page, zone_version, rtype, scope, view_id, sort_by, sort_order, compartment_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    if isinstance(domain, six.string_types) and len(domain.strip()) == 0:
        raise click.UsageError('Parameter --domain cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if zone_version is not None:
        kwargs['zone_version'] = zone_version
    if rtype is not None:
        kwargs['rtype'] = rtype
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.get_domain_records,
            zone_name_or_id=zone_name_or_id,
            domain=domain,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.get_domain_records,
            limit,
            page_size,
            zone_name_or_id=zone_name_or_id,
            domain=domain,
            **kwargs
        )
    else:
        result = client.get_domain_records(
            zone_name_or_id=zone_name_or_id,
            domain=domain,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@resolver_group.command(name=cli_util.override('dns.get_resolver.command_name', 'get'), help=u"""Gets information about a specific resolver.

Note that attempting to get a resolver in the DELETED lifecycleState will result in a `404` response to be consistent with other operations of the API. \n[Command Reference](getResolver)""")
@cli_util.option('--resolver-id', required=True, help=u"""The OCID of the target resolver.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'Resolver'})
@cli_util.wrap_exceptions
def get_resolver(ctx, from_json, resolver_id, if_modified_since, if_none_match, scope):

    if isinstance(resolver_id, six.string_types) and len(resolver_id.strip()) == 0:
        raise click.UsageError('Parameter --resolver-id cannot be whitespace or empty string')

    kwargs = {}
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.get_resolver(
        resolver_id=resolver_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@resolver_endpoint_group.command(name=cli_util.override('dns.get_resolver_endpoint.command_name', 'get'), help=u"""Gets information about a specific resolver endpoint.

Note that attempting to get a resolver endpoint in the DELETED lifecycle state will result in a `404` response to be consistent with other operations of the API. \n[Command Reference](getResolverEndpoint)""")
@cli_util.option('--resolver-id', required=True, help=u"""The OCID of the target resolver.""")
@cli_util.option('--resolver-endpoint-name', required=True, help=u"""The name of the target resolver endpoint.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'ResolverEndpoint'})
@cli_util.wrap_exceptions
def get_resolver_endpoint(ctx, from_json, resolver_id, resolver_endpoint_name, if_modified_since, if_none_match, scope):

    if isinstance(resolver_id, six.string_types) and len(resolver_id.strip()) == 0:
        raise click.UsageError('Parameter --resolver-id cannot be whitespace or empty string')

    if isinstance(resolver_endpoint_name, six.string_types) and len(resolver_endpoint_name.strip()) == 0:
        raise click.UsageError('Parameter --resolver-endpoint-name cannot be whitespace or empty string')

    kwargs = {}
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.get_resolver_endpoint(
        resolver_id=resolver_id,
        resolver_endpoint_name=resolver_endpoint_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rr_set_group.command(name=cli_util.override('dns.get_rr_set.command_name', 'get'), help=u"""Gets a list of all records in the specified RRSet.

The results are sorted by `recordHash` by default. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](getRRSet)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--rtype', required=True, help=u"""The type of the target RRSet within the target zone.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a page of the collection.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--zone-version', help=u"""The version of the zone for which data is requested.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'RRSet'})
@cli_util.wrap_exceptions
def get_rr_set(ctx, from_json, all_pages, page_size, zone_name_or_id, domain, rtype, if_none_match, if_modified_since, limit, page, zone_version, compartment_id, scope, view_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    if isinstance(domain, six.string_types) and len(domain.strip()) == 0:
        raise click.UsageError('Parameter --domain cannot be whitespace or empty string')

    if isinstance(rtype, six.string_types) and len(rtype.strip()) == 0:
        raise click.UsageError('Parameter --rtype cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if zone_version is not None:
        kwargs['zone_version'] = zone_version
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.get_rr_set,
            zone_name_or_id=zone_name_or_id,
            domain=domain,
            rtype=rtype,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.get_rr_set,
            limit,
            page_size,
            zone_name_or_id=zone_name_or_id,
            domain=domain,
            rtype=rtype,
            **kwargs
        )
    else:
        result = client.get_rr_set(
            zone_name_or_id=zone_name_or_id,
            domain=domain,
            rtype=rtype,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@steering_policy_group.command(name=cli_util.override('dns.get_steering_policy.command_name', 'get'), help=u"""Gets information about the specified steering policy. \n[Command Reference](getSteeringPolicy)""")
@cli_util.option('--steering-policy-id', required=True, help=u"""The OCID of the target steering policy.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'SteeringPolicy'})
@cli_util.wrap_exceptions
def get_steering_policy(ctx, from_json, steering_policy_id, if_none_match, if_modified_since, scope):

    if isinstance(steering_policy_id, six.string_types) and len(steering_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --steering-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.get_steering_policy(
        steering_policy_id=steering_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@steering_policy_attachment_group.command(name=cli_util.override('dns.get_steering_policy_attachment.command_name', 'get'), help=u"""Gets information about the specified steering policy attachment. \n[Command Reference](getSteeringPolicyAttachment)""")
@cli_util.option('--steering-policy-attachment-id', required=True, help=u"""The OCID of the target steering policy attachment.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'SteeringPolicyAttachment'})
@cli_util.wrap_exceptions
def get_steering_policy_attachment(ctx, from_json, steering_policy_attachment_id, if_none_match, if_modified_since, scope):

    if isinstance(steering_policy_attachment_id, six.string_types) and len(steering_policy_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --steering-policy-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.get_steering_policy_attachment(
        steering_policy_attachment_id=steering_policy_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tsig_key_group.command(name=cli_util.override('dns.get_tsig_key.command_name', 'get'), help=u"""Gets information about the specified TSIG key. \n[Command Reference](getTsigKey)""")
@cli_util.option('--tsig-key-id', required=True, help=u"""The OCID of the target TSIG key.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'TsigKey'})
@cli_util.wrap_exceptions
def get_tsig_key(ctx, from_json, tsig_key_id, if_none_match, if_modified_since, scope):

    if isinstance(tsig_key_id, six.string_types) and len(tsig_key_id.strip()) == 0:
        raise click.UsageError('Parameter --tsig-key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.get_tsig_key(
        tsig_key_id=tsig_key_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@view_group.command(name=cli_util.override('dns.get_view.command_name', 'get'), help=u"""Gets information about a specific view.

Note that attempting to get a view in the DELETED lifecycleState will result in a `404` response to be consistent with other operations of the API. \n[Command Reference](getView)""")
@cli_util.option('--view-id', required=True, help=u"""The OCID of the target view.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'View'})
@cli_util.wrap_exceptions
def get_view(ctx, from_json, view_id, if_modified_since, if_none_match, scope):

    if isinstance(view_id, six.string_types) and len(view_id.strip()) == 0:
        raise click.UsageError('Parameter --view-id cannot be whitespace or empty string')

    kwargs = {}
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.get_view(
        view_id=view_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@zone_group.command(name=cli_util.override('dns.get_zone.command_name', 'get'), help=u"""Gets information about the specified zone, including its creation date, zone type, and serial.

When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](getZone)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'Zone'})
@cli_util.wrap_exceptions
def get_zone(ctx, from_json, zone_name_or_id, if_none_match, if_modified_since, scope, view_id, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.get_zone(
        zone_name_or_id=zone_name_or_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@zone_group.command(name=cli_util.override('dns.get_zone_content.command_name', 'get-zone-content'), help=u"""Gets the requested zone's zone file. \n[Command Reference](getZoneContent)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_zone_content(ctx, from_json, file, zone_name_or_id, if_none_match, if_modified_since, scope, view_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.get_zone_content(
        zone_name_or_id=zone_name_or_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@records_group.command(name=cli_util.override('dns.get_zone_records.command_name', 'get-zone'), help=u"""Gets all records in the specified zone.

The results are sorted by `domain` in alphabetical order by default. For more information about records, see [Resource Record (RR) TYPEs]. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](getZoneRecords)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a page of the collection.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--zone-version', help=u"""The version of the zone for which data is requested.""")
@cli_util.option('--domain', help=u"""Search by domain. Will match any record whose domain (case-insensitive) equals the provided value.""")
@cli_util.option('--domain-contains', help=u"""Search by domain. Will match any record whose domain (case-insensitive) contains the provided value.""")
@cli_util.option('--rtype', help=u"""Search by record type. Will match any record whose [type] (case-insensitive) equals the provided value.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["domain", "rtype", "ttl"]), help=u"""The field by which to sort records.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order to sort the resources.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def get_zone_records(ctx, from_json, all_pages, page_size, zone_name_or_id, if_none_match, if_modified_since, limit, page, zone_version, domain, domain_contains, rtype, sort_by, sort_order, compartment_id, scope, view_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if zone_version is not None:
        kwargs['zone_version'] = zone_version
    if domain is not None:
        kwargs['domain'] = domain
    if domain_contains is not None:
        kwargs['domain_contains'] = domain_contains
    if rtype is not None:
        kwargs['rtype'] = rtype
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.get_zone_records,
            zone_name_or_id=zone_name_or_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.get_zone_records,
            limit,
            page_size,
            zone_name_or_id=zone_name_or_id,
            **kwargs
        )
    else:
        result = client.get_zone_records(
            zone_name_or_id=zone_name_or_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@resolver_endpoint_group.command(name=cli_util.override('dns.list_resolver_endpoints.command_name', 'list'), help=u"""Gets a list of all endpoints within a resolver. The collection can be filtered by name or lifecycle state. It can be sorted on creation time or name both in ASC or DESC order. Note that when no lifecycleState query parameter is provided, the collection does not include resolver endpoints in the DELETED lifecycle state to be consistent with other operations of the API. \n[Command Reference](listResolverEndpoints)""")
@cli_util.option('--resolver-id', required=True, help=u"""The OCID of the target resolver.""")
@cli_util.option('--name', help=u"""The name of a resource.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a page of the collection.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order to sort the resources.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "timeCreated"]), help=u"""The field by which to sort resolver endpoints.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), help=u"""The state of a resource.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'list[ResolverEndpointSummary]'})
@cli_util.wrap_exceptions
def list_resolver_endpoints(ctx, from_json, all_pages, page_size, resolver_id, name, page, limit, sort_order, sort_by, lifecycle_state, scope):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(resolver_id, six.string_types) and len(resolver_id.strip()) == 0:
        raise click.UsageError('Parameter --resolver-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_resolver_endpoints,
            resolver_id=resolver_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_resolver_endpoints,
            limit,
            page_size,
            resolver_id=resolver_id,
            **kwargs
        )
    else:
        result = client.list_resolver_endpoints(
            resolver_id=resolver_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@resolver_group.command(name=cli_util.override('dns.list_resolvers.command_name', 'list'), help=u"""Gets a list of all resolvers within a compartment.

The collection can be filtered by display name, id, or lifecycle state. It can be sorted on creation time or displayName both in ASC or DESC order. Note that when no lifecycleState query parameter is provided, the collection does not include resolvers in the DELETED lifecycleState to be consistent with other operations of the API. \n[Command Reference](listResolvers)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--display-name', help=u"""The displayName of a resource.""")
@cli_util.option('--id', help=u"""The OCID of a resource.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a page of the collection.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order to sort the resources.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "timeCreated"]), help=u"""The field by which to sort resolvers.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), help=u"""The state of a resource.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'list[ResolverSummary]'})
@cli_util.wrap_exceptions
def list_resolvers(ctx, from_json, all_pages, page_size, compartment_id, display_name, id, page, limit, sort_order, sort_by, lifecycle_state, scope):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_resolvers,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_resolvers,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_resolvers(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@steering_policy_group.command(name=cli_util.override('dns.list_steering_policies.command_name', 'list'), help=u"""Gets a list of all steering policies in the specified compartment. \n[Command Reference](listSteeringPolicies)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a page of the collection.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--id', help=u"""The OCID of a resource.""")
@cli_util.option('--display-name', help=u"""The displayName of a resource.""")
@cli_util.option('--display-name-contains', help=u"""The partial displayName of a resource. Will match any resource whose name (case-insensitive) contains the provided value.""")
@cli_util.option('--health-check-monitor-id', help=u"""Search by health check monitor OCID. Will match any resource whose health check monitor ID matches the provided value.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""An [RFC 3339] timestamp that states all returned resources were created on or after the indicated time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""An [RFC 3339] timestamp that states all returned resources were created before the indicated time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--template', help=u"""Search by steering template type. Will match any resource whose template type matches the provided value.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING"]), help=u"""The state of a resource.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "timeCreated", "template"]), help=u"""The field by which to sort steering policies. If unspecified, defaults to `timeCreated`.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order to sort the resources.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'list[SteeringPolicySummary]'})
@cli_util.wrap_exceptions
def list_steering_policies(ctx, from_json, all_pages, page_size, compartment_id, limit, page, id, display_name, display_name_contains, health_check_monitor_id, time_created_greater_than_or_equal_to, time_created_less_than, template, lifecycle_state, sort_by, sort_order, scope):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if id is not None:
        kwargs['id'] = id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if health_check_monitor_id is not None:
        kwargs['health_check_monitor_id'] = health_check_monitor_id
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if time_created_less_than is not None:
        kwargs['time_created_less_than'] = time_created_less_than
    if template is not None:
        kwargs['template'] = template
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_steering_policies,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_steering_policies,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_steering_policies(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@steering_policy_attachment_group.command(name=cli_util.override('dns.list_steering_policy_attachments.command_name', 'list'), help=u"""Lists the steering policy attachments in the specified compartment. \n[Command Reference](listSteeringPolicyAttachments)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a page of the collection.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--id', help=u"""The OCID of a resource.""")
@cli_util.option('--display-name', help=u"""The displayName of a resource.""")
@cli_util.option('--steering-policy-id', help=u"""Search by steering policy OCID. Will match any resource whose steering policy ID matches the provided value.""")
@cli_util.option('--zone-id', help=u"""Search by zone OCID. Will match any resource whose zone ID matches the provided value.""")
@cli_util.option('--domain', help=u"""Search by domain. Will match any record whose domain (case-insensitive) equals the provided value.""")
@cli_util.option('--domain-contains', help=u"""Search by domain. Will match any record whose domain (case-insensitive) contains the provided value.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""An [RFC 3339] timestamp that states all returned resources were created on or after the indicated time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""An [RFC 3339] timestamp that states all returned resources were created before the indicated time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING"]), help=u"""The state of a resource.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "timeCreated", "domainName"]), help=u"""The field by which to sort steering policy attachments. If unspecified, defaults to `timeCreated`.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order to sort the resources.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'list[SteeringPolicyAttachmentSummary]'})
@cli_util.wrap_exceptions
def list_steering_policy_attachments(ctx, from_json, all_pages, page_size, compartment_id, limit, page, id, display_name, steering_policy_id, zone_id, domain, domain_contains, time_created_greater_than_or_equal_to, time_created_less_than, lifecycle_state, sort_by, sort_order, scope):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if id is not None:
        kwargs['id'] = id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if steering_policy_id is not None:
        kwargs['steering_policy_id'] = steering_policy_id
    if zone_id is not None:
        kwargs['zone_id'] = zone_id
    if domain is not None:
        kwargs['domain'] = domain
    if domain_contains is not None:
        kwargs['domain_contains'] = domain_contains
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if time_created_less_than is not None:
        kwargs['time_created_less_than'] = time_created_less_than
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_steering_policy_attachments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_steering_policy_attachments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_steering_policy_attachments(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@tsig_key_group.command(name=cli_util.override('dns.list_tsig_keys.command_name', 'list'), help=u"""Gets a list of all TSIG keys in the specified compartment. \n[Command Reference](listTsigKeys)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a page of the collection.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--id', help=u"""The OCID of a resource.""")
@cli_util.option('--name', help=u"""The name of a resource.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), help=u"""The state of a resource.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "timeCreated"]), help=u"""The field by which to sort TSIG keys. If unspecified, defaults to `timeCreated`.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order to sort the resources.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'list[TsigKeySummary]'})
@cli_util.wrap_exceptions
def list_tsig_keys(ctx, from_json, all_pages, page_size, compartment_id, limit, page, id, name, lifecycle_state, sort_by, sort_order, scope):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if id is not None:
        kwargs['id'] = id
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_tsig_keys,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_tsig_keys,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_tsig_keys(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@view_group.command(name=cli_util.override('dns.list_views.command_name', 'list'), help=u"""Gets a list of all views within a compartment.

The collection can be filtered by display name, id, or lifecycle state. It can be sorted on creation time or displayName both in ASC or DESC order. Note that when no lifecycleState query parameter is provided, the collection does not include views in the DELETED lifecycleState to be consistent with other operations of the API. \n[Command Reference](listViews)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--display-name', help=u"""The displayName of a resource.""")
@cli_util.option('--id', help=u"""The OCID of a resource.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a page of the collection.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order to sort the resources.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "timeCreated"]), help=u"""The field by which to sort views.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "DELETING", "UPDATING"]), help=u"""The state of a resource.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'list[ViewSummary]'})
@cli_util.wrap_exceptions
def list_views(ctx, from_json, all_pages, page_size, compartment_id, display_name, id, page, limit, sort_order, sort_by, lifecycle_state, scope):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_views,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_views,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_views(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@zone_transfer_server_group.command(name=cli_util.override('dns.list_zone_transfer_servers.command_name', 'list'), help=u"""Gets a list of IP addresses of OCI nameservers for inbound and outbound transfer of zones in the specified compartment (which must be the root compartment of a tenancy) that transfer zone data with external master or downstream nameservers. \n[Command Reference](listZoneTransferServers)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'list[ZoneTransferServer]'})
@cli_util.wrap_exceptions
def list_zone_transfer_servers(ctx, from_json, all_pages, compartment_id, scope, page):

    kwargs = {}
    if scope is not None:
        kwargs['scope'] = scope
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    if all_pages:
        result = cli_util.list_call_get_all_results(
            client.list_zone_transfer_servers,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_zone_transfer_servers(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@zone_group.command(name=cli_util.override('dns.list_zones.command_name', 'list'), help=u"""Gets a list of all zones in the specified compartment.

The collection can be filtered by name, time created, scope, associated view, and zone type. Filtering by view is only supported for private zones. \n[Command Reference](listZones)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a page of the collection.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--name', help=u"""A case-sensitive filter for zone names. Will match any zone with a name that equals the provided value.""")
@cli_util.option('--name-contains', help=u"""Search by zone name. Will match any zone whose name (case-insensitive) contains the provided value.""")
@cli_util.option('--zone-type', type=custom_types.CliCaseInsensitiveChoice(["PRIMARY", "SECONDARY"]), help=u"""Search by zone type, `PRIMARY` or `SECONDARY`. Will match any zone whose type equals the provided value.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""An [RFC 3339] timestamp that states all returned resources were created on or after the indicated time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""An [RFC 3339] timestamp that states all returned resources were created before the indicated time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), help=u"""The state of a resource.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "zoneType", "timeCreated"]), help=u"""The field by which to sort zones.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order to sort the resources.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--tsig-key-id', help=u"""Search for zones that are associated with a TSIG key.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'list[ZoneSummary]'})
@cli_util.wrap_exceptions
def list_zones(ctx, from_json, all_pages, page_size, compartment_id, limit, page, name, name_contains, zone_type, time_created_greater_than_or_equal_to, time_created_less_than, lifecycle_state, sort_by, sort_order, scope, view_id, tsig_key_id):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if name is not None:
        kwargs['name'] = name
    if name_contains is not None:
        kwargs['name_contains'] = name_contains
    if zone_type is not None:
        kwargs['zone_type'] = zone_type
    if time_created_greater_than_or_equal_to is not None:
        kwargs['time_created_greater_than_or_equal_to'] = time_created_greater_than_or_equal_to
    if time_created_less_than is not None:
        kwargs['time_created_less_than'] = time_created_less_than
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    if tsig_key_id is not None:
        kwargs['tsig_key_id'] = tsig_key_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('dns', 'dns', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_zones,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_zones,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_zones(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@records_group.command(name=cli_util.override('dns.patch_domain_records.command_name', 'patch-domain'), help=u"""Updates records in the specified zone at a domain.

You can update one record or all records for the specified zone depending on the changes provided in the request body. You can also add or remove records using this function. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](patchDomainRecords)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type RecordOperation.  For documentation on RecordOperation please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/RecordOperation.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'dns', 'class': 'list[RecordOperation]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'dns', 'class': 'list[RecordOperation]'}}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def patch_domain_records(ctx, from_json, zone_name_or_id, domain, items, if_match, if_unmodified_since, scope, view_id, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    if isinstance(domain, six.string_types) and len(domain.strip()) == 0:
        raise click.UsageError('Parameter --domain cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.patch_domain_records(
        zone_name_or_id=zone_name_or_id,
        domain=domain,
        patch_domain_records_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rr_set_group.command(name=cli_util.override('dns.patch_rr_set.command_name', 'patch'), help=u"""Updates records in the specified RRSet.

When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](patchRRSet)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--rtype', required=True, help=u"""The type of the target RRSet within the target zone.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type RecordOperation.  For documentation on RecordOperation please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/RecordOperation.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'dns', 'class': 'list[RecordOperation]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'dns', 'class': 'list[RecordOperation]'}}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def patch_rr_set(ctx, from_json, zone_name_or_id, domain, rtype, items, if_match, if_unmodified_since, scope, view_id, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    if isinstance(domain, six.string_types) and len(domain.strip()) == 0:
        raise click.UsageError('Parameter --domain cannot be whitespace or empty string')

    if isinstance(rtype, six.string_types) and len(rtype.strip()) == 0:
        raise click.UsageError('Parameter --rtype cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.patch_rr_set(
        zone_name_or_id=zone_name_or_id,
        domain=domain,
        rtype=rtype,
        patch_rr_set_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@records_group.command(name=cli_util.override('dns.patch_zone_records.command_name', 'patch-zone'), help=u"""Updates a collection of records in the specified zone.

You can update one record or all records for the specified zone depending on the changes provided in the request body. You can also add or remove records using this function. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](patchZoneRecords)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type RecordOperation.  For documentation on RecordOperation please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/RecordOperation.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'dns', 'class': 'list[RecordOperation]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'dns', 'class': 'list[RecordOperation]'}}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def patch_zone_records(ctx, from_json, zone_name_or_id, items, if_match, if_unmodified_since, scope, view_id, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.patch_zone_records(
        zone_name_or_id=zone_name_or_id,
        patch_zone_records_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@records_group.command(name=cli_util.override('dns.update_domain_records.command_name', 'update-domain'), help=u"""Replaces records in the specified zone at a domain with the records specified in the request body.

If a specified record does not exist, it will be created. If the record exists, then it will be updated to represent the record in the body of the request. If a record in the zone does not exist in the request body, the record will be removed from the zone. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](updateDomainRecords)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type RecordDetails.  For documentation on RecordDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/RecordDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'dns', 'class': 'list[RecordDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'dns', 'class': 'list[RecordDetails]'}}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def update_domain_records(ctx, from_json, force, zone_name_or_id, domain, items, if_match, if_unmodified_since, scope, view_id, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    if isinstance(domain, six.string_types) and len(domain.strip()) == 0:
        raise click.UsageError('Parameter --domain cannot be whitespace or empty string')
    if not force:
        if items:
            if not click.confirm("WARNING: Updates to items will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.update_domain_records(
        zone_name_or_id=zone_name_or_id,
        domain=domain,
        update_domain_records_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@resolver_group.command(name=cli_util.override('dns.update_resolver.command_name', 'update'), help=u"""Updates the specified resolver with your new information. \n[Command Reference](updateResolver)""")
@cli_util.option('--resolver-id', required=True, help=u"""The OCID of the target resolver.""")
@cli_util.option('--display-name', help=u"""The display name of the resolver.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

 **Example:** `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

 **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--attached-views', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The attached views. Views are evaluated in order.

This option is a JSON list with items of type AttachedViewDetails.  For documentation on AttachedViewDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/AttachedViewDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Rules for the resolver. Rules are evaluated in order.

This option is a JSON list with items of type ResolverRuleDetails.  For documentation on ResolverRuleDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/ResolverRuleDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'attached-views': {'module': 'dns', 'class': 'list[AttachedViewDetails]'}, 'rules': {'module': 'dns', 'class': 'list[ResolverRuleDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'attached-views': {'module': 'dns', 'class': 'list[AttachedViewDetails]'}, 'rules': {'module': 'dns', 'class': 'list[ResolverRuleDetails]'}}, output_type={'module': 'dns', 'class': 'Resolver'})
@cli_util.wrap_exceptions
def update_resolver(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, resolver_id, display_name, freeform_tags, defined_tags, attached_views, rules, if_match, if_unmodified_since, scope):

    if isinstance(resolver_id, six.string_types) and len(resolver_id.strip()) == 0:
        raise click.UsageError('Parameter --resolver-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or attached_views or rules:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and attached-views and rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if attached_views is not None:
        _details['attachedViews'] = cli_util.parse_json_parameter("attached_views", attached_views)

    if rules is not None:
        _details['rules'] = cli_util.parse_json_parameter("rules", rules)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.update_resolver(
        resolver_id=resolver_id,
        update_resolver_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_resolver') and callable(getattr(client, 'get_resolver')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_resolver(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@resolver_endpoint_group.command(name=cli_util.override('dns.update_resolver_endpoint.command_name', 'update'), help=u"""Updates the specified resolver endpoint with your new information. \n[Command Reference](updateResolverEndpoint)""")
@cli_util.option('--resolver-id', required=True, help=u"""The OCID of the target resolver.""")
@cli_util.option('--resolver-endpoint-name', required=True, help=u"""The name of the target resolver endpoint.""")
@cli_util.option('--endpoint-type', type=custom_types.CliCaseInsensitiveChoice(["VNIC"]), help=u"""The type of resolver endpoint. VNIC is currently the only supported type.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'ResolverEndpoint'})
@cli_util.wrap_exceptions
def update_resolver_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, resolver_id, resolver_endpoint_name, endpoint_type, if_match, if_unmodified_since, scope):

    if isinstance(resolver_id, six.string_types) and len(resolver_id.strip()) == 0:
        raise click.UsageError('Parameter --resolver-id cannot be whitespace or empty string')

    if isinstance(resolver_endpoint_name, six.string_types) and len(resolver_endpoint_name.strip()) == 0:
        raise click.UsageError('Parameter --resolver-endpoint-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if endpoint_type is not None:
        _details['endpointType'] = endpoint_type

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.update_resolver_endpoint(
        resolver_id=resolver_id,
        resolver_endpoint_name=resolver_endpoint_name,
        update_resolver_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_resolver_endpoint') and callable(getattr(client, 'get_resolver_endpoint')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_resolver_endpoint(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@resolver_endpoint_group.command(name=cli_util.override('dns.update_resolver_endpoint_update_resolver_vnic_endpoint_details.command_name', 'update-resolver-endpoint-update-resolver-vnic-endpoint-details'), help=u"""Updates the specified resolver endpoint with your new information. \n[Command Reference](updateResolverEndpoint)""")
@cli_util.option('--resolver-id', required=True, help=u"""The OCID of the target resolver.""")
@cli_util.option('--resolver-endpoint-name', required=True, help=u"""The name of the target resolver endpoint.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the resolver endpoint is a part of.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'nsg-ids': {'module': 'dns', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'nsg-ids': {'module': 'dns', 'class': 'list[string]'}}, output_type={'module': 'dns', 'class': 'ResolverEndpoint'})
@cli_util.wrap_exceptions
def update_resolver_endpoint_update_resolver_vnic_endpoint_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, resolver_id, resolver_endpoint_name, nsg_ids, if_match, if_unmodified_since, scope):

    if isinstance(resolver_id, six.string_types) and len(resolver_id.strip()) == 0:
        raise click.UsageError('Parameter --resolver-id cannot be whitespace or empty string')

    if isinstance(resolver_endpoint_name, six.string_types) and len(resolver_endpoint_name.strip()) == 0:
        raise click.UsageError('Parameter --resolver-endpoint-name cannot be whitespace or empty string')
    if not force:
        if nsg_ids:
            if not click.confirm("WARNING: Updates to nsg-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if nsg_ids is not None:
        _details['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", nsg_ids)

    _details['endpointType'] = 'VNIC'

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.update_resolver_endpoint(
        resolver_id=resolver_id,
        resolver_endpoint_name=resolver_endpoint_name,
        update_resolver_endpoint_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_resolver_endpoint') and callable(getattr(client, 'get_resolver_endpoint')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_resolver_endpoint(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@rr_set_group.command(name=cli_util.override('dns.update_rr_set.command_name', 'update'), help=u"""Replaces records in the specified RRSet.

When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](updateRRSet)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--rtype', required=True, help=u"""The type of the target RRSet within the target zone.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type RecordDetails.  For documentation on RecordDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/RecordDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'dns', 'class': 'list[RecordDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'dns', 'class': 'list[RecordDetails]'}}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def update_rr_set(ctx, from_json, force, zone_name_or_id, domain, rtype, items, if_match, if_unmodified_since, scope, view_id, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    if isinstance(domain, six.string_types) and len(domain.strip()) == 0:
        raise click.UsageError('Parameter --domain cannot be whitespace or empty string')

    if isinstance(rtype, six.string_types) and len(rtype.strip()) == 0:
        raise click.UsageError('Parameter --rtype cannot be whitespace or empty string')
    if not force:
        if items:
            if not click.confirm("WARNING: Updates to items will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.update_rr_set(
        zone_name_or_id=zone_name_or_id,
        domain=domain,
        rtype=rtype,
        update_rr_set_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@steering_policy_group.command(name=cli_util.override('dns.update_steering_policy.command_name', 'update'), help=u"""Updates the configuration of the specified steering policy. \n[Command Reference](updateSteeringPolicy)""")
@cli_util.option('--steering-policy-id', required=True, help=u"""The OCID of the target steering policy.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the steering policy. Does not have to be unique and can be changed. Avoid entering confidential information.""")
@cli_util.option('--ttl', type=click.INT, help=u"""The Time To Live (TTL) for responses from the steering policy, in seconds. If not specified during creation, a value of 30 seconds will be used.""")
@cli_util.option('--health-check-monitor-id', help=u"""The OCID of the health check monitor providing health data about the answers of the steering policy. A steering policy answer with `rdata` matching a monitored endpoint will use the health data of that endpoint. A steering policy answer with `rdata` not matching any monitored endpoint will be assumed healthy.

 **Note:** To use the Health Check monitoring feature in a steering policy, a monitor must be created using the Health Checks service first. For more information on how to create a monitor, please see [Managing Health Checks].""")
@cli_util.option('--template', type=custom_types.CliCaseInsensitiveChoice(["FAILOVER", "LOAD_BALANCE", "ROUTE_BY_GEO", "ROUTE_BY_ASN", "ROUTE_BY_IP", "CUSTOM"]), help=u"""A set of predefined rules based on the desired purpose of the steering policy. Each template utilizes Traffic Management's rules in a different order to produce the desired results when answering DNS queries.

 **Example:** The `FAILOVER` template determines answers by filtering the policy's answers using the `FILTER` rule first, then the following rules in succession: `HEALTH`, `PRIORITY`, and `LIMIT`. This gives the domain dynamic failover capability.

 It is **strongly recommended** to use a template other than `CUSTOM` when creating a steering policy.

 All templates require the rule order to begin with an unconditional `FILTER` rule that keeps answers contingent upon `answer.isDisabled != true`, except for `CUSTOM`. A defined `HEALTH` rule must follow the `FILTER` rule if the policy references a `healthCheckMonitorId`. The last rule of a template must must be a `LIMIT` rule. For more information about templates and code examples, see [Traffic Management API Guide].

**Template Types**

* `FAILOVER` - Uses health check information on your endpoints to determine which DNS answers to serve. If an endpoint fails a health check, the answer for that endpoint will be removed from the list of available answers until the endpoint is detected as healthy.

 * `LOAD_BALANCE` - Distributes web traffic to specified endpoints based on defined weights.

 * `ROUTE_BY_GEO` - Answers DNS queries based on the query's geographic location. For a list of geographic locations to route by, see [Traffic Management Geographic Locations].

 * `ROUTE_BY_ASN` - Answers DNS queries based on the query's originating ASN.

 * `ROUTE_BY_IP` - Answers DNS queries based on the query's IP address.

 * `CUSTOM` - Allows a customized configuration of rules.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

 **Example:** `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

 **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--answers', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The set of all answers that can potentially issue from the steering policy.

This option is a JSON list with items of type SteeringPolicyAnswer.  For documentation on SteeringPolicyAnswer please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/SteeringPolicyAnswer.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--rules', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The series of rules that will be processed in sequence to reduce the pool of answers to a response for any given request.

 The first rule receives a shuffled list of all answers, and every other rule receives the list of answers emitted by the one preceding it. The last rule populates the response.

This option is a JSON list with items of type SteeringPolicyRule.  For documentation on SteeringPolicyRule please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/SteeringPolicyRule.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'answers': {'module': 'dns', 'class': 'list[SteeringPolicyAnswer]'}, 'rules': {'module': 'dns', 'class': 'list[SteeringPolicyRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'answers': {'module': 'dns', 'class': 'list[SteeringPolicyAnswer]'}, 'rules': {'module': 'dns', 'class': 'list[SteeringPolicyRule]'}}, output_type={'module': 'dns', 'class': 'SteeringPolicy'})
@cli_util.wrap_exceptions
def update_steering_policy(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, steering_policy_id, display_name, ttl, health_check_monitor_id, template, freeform_tags, defined_tags, answers, rules, if_match, if_unmodified_since, scope):

    if isinstance(steering_policy_id, six.string_types) and len(steering_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --steering-policy-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or answers or rules:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and answers and rules will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if ttl is not None:
        _details['ttl'] = ttl

    if health_check_monitor_id is not None:
        _details['healthCheckMonitorId'] = health_check_monitor_id

    if template is not None:
        _details['template'] = template

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if answers is not None:
        _details['answers'] = cli_util.parse_json_parameter("answers", answers)

    if rules is not None:
        _details['rules'] = cli_util.parse_json_parameter("rules", rules)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.update_steering_policy(
        steering_policy_id=steering_policy_id,
        update_steering_policy_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_steering_policy') and callable(getattr(client, 'get_steering_policy')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_steering_policy(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@steering_policy_attachment_group.command(name=cli_util.override('dns.update_steering_policy_attachment.command_name', 'update'), help=u"""Updates the specified steering policy attachment with your new information. \n[Command Reference](updateSteeringPolicyAttachment)""")
@cli_util.option('--steering-policy-attachment-id', required=True, help=u"""The OCID of the target steering policy attachment.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'SteeringPolicyAttachment'})
@cli_util.wrap_exceptions
def update_steering_policy_attachment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, steering_policy_attachment_id, display_name, if_match, if_unmodified_since, scope):

    if isinstance(steering_policy_attachment_id, six.string_types) and len(steering_policy_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --steering-policy-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.update_steering_policy_attachment(
        steering_policy_attachment_id=steering_policy_attachment_id,
        update_steering_policy_attachment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_steering_policy_attachment') and callable(getattr(client, 'get_steering_policy_attachment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_steering_policy_attachment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@tsig_key_group.command(name=cli_util.override('dns.update_tsig_key.command_name', 'update'), help=u"""Updates the specified TSIG key. \n[Command Reference](updateTsigKey)""")
@cli_util.option('--tsig-key-id', required=True, help=u"""The OCID of the target TSIG key.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

 **Example:** `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

 **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dns', 'class': 'TsigKey'})
@cli_util.wrap_exceptions
def update_tsig_key(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, tsig_key_id, freeform_tags, defined_tags, if_match, if_unmodified_since, scope):

    if isinstance(tsig_key_id, six.string_types) and len(tsig_key_id.strip()) == 0:
        raise click.UsageError('Parameter --tsig-key-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.update_tsig_key(
        tsig_key_id=tsig_key_id,
        update_tsig_key_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tsig_key') and callable(getattr(client, 'get_tsig_key')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tsig_key(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@view_group.command(name=cli_util.override('dns.update_view.command_name', 'update'), help=u"""Updates the specified view with your new information. \n[Command Reference](updateView)""")
@cli_util.option('--view-id', required=True, help=u"""The OCID of the target view.""")
@cli_util.option('--display-name', help=u"""The display name of the view.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

 **Example:** `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

 **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "DELETED", "DELETING", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dns', 'class': 'View'})
@cli_util.wrap_exceptions
def update_view(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, view_id, display_name, freeform_tags, defined_tags, if_match, if_unmodified_since, scope):

    if isinstance(view_id, six.string_types) and len(view_id.strip()) == 0:
        raise click.UsageError('Parameter --view-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.update_view(
        view_id=view_id,
        update_view_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_view') and callable(getattr(client, 'get_view')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_view(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@zone_group.command(name=cli_util.override('dns.update_zone.command_name', 'update'), help=u"""Updates the zone with the specified information.

Global secondary zones may have their external masters updated. For more information about secondary zones, see [Manage DNS Service Zone]. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](updateZone)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

 **Example:** `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

 **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--external-masters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""External master servers for the zone. `externalMasters` becomes a required parameter when the `zoneType` value is `SECONDARY`.

This option is a JSON list with items of type ExternalMaster.  For documentation on ExternalMaster please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/ExternalMaster.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED", "UPDATING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'external-masters': {'module': 'dns', 'class': 'list[ExternalMaster]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'external-masters': {'module': 'dns', 'class': 'list[ExternalMaster]'}}, output_type={'module': 'dns', 'class': 'Zone'})
@cli_util.wrap_exceptions
def update_zone(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, zone_name_or_id, freeform_tags, defined_tags, external_masters, if_match, if_unmodified_since, scope, view_id, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or external_masters:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and external-masters will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if external_masters is not None:
        _details['externalMasters'] = cli_util.parse_json_parameter("external_masters", external_masters)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.update_zone(
        zone_name_or_id=zone_name_or_id,
        update_zone_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_zone') and callable(getattr(client, 'get_zone')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_zone(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@records_group.command(name=cli_util.override('dns.update_zone_records.command_name', 'update-zone'), help=u"""Replaces records in the specified zone with the records specified in the request body.

If a specified record does not exist, it will be created. If the record exists, then it will be updated to represent the record in the body of the request. If a record in the zone does not exist in the request body, the record will be removed from the zone. When the zone name is provided as a path parameter and `PRIVATE` is used for the scope query parameter then the viewId query parameter is required. \n[Command Reference](updateZoneRecords)""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type RecordDetails.  For documentation on RecordDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/RecordDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--scope', type=custom_types.CliCaseInsensitiveChoice(["GLOBAL", "PRIVATE"]), help=u"""Specifies to operate only on resources that have a matching DNS scope.""")
@cli_util.option('--view-id', help=u"""The OCID of the view the resource is associated with.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the zone belongs to.

This parameter is deprecated and should be omitted.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'dns', 'class': 'list[RecordDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'dns', 'class': 'list[RecordDetails]'}}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def update_zone_records(ctx, from_json, force, zone_name_or_id, items, if_match, if_unmodified_since, scope, view_id, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')
    if not force:
        if items:
            if not click.confirm("WARNING: Updates to items will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if scope is not None:
        kwargs['scope'] = scope
    if view_id is not None:
        kwargs['view_id'] = view_id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('dns', 'dns', ctx)
    result = client.update_zone_records(
        zone_name_or_id=zone_name_or_id,
        update_zone_records_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
