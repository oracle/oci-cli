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


@cli.command(cli_util.override('dns_root_group.command_name', 'dns'), cls=CommandGroupWithAlias, help=cli_util.override('dns_root_group.help', """API for the DNS service. Use this API to manage DNS zones, records, and other DNS resources.
For more information, see [Overview of the DNS Service](/iaas/Content/DNS/Concepts/dnszonemanagement.htm).
"""), short_help=cli_util.override('dns_root_group.short_help', """DNS API"""))
@cli_util.help_option_group
def dns_root_group():
    pass


@click.command(cli_util.override('steering_policy_attachment_group.command_name', 'steering-policy-attachment'), cls=CommandGroupWithAlias, help="""An attachment between a steering policy and a domain. An attachment constructs DNS responses using its steering policy instead of the records at its defined domain. Only records of the policy's covered rtype are blocked at the domain. A domain can have a maximum of one attachment covering any given rtype.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def steering_policy_attachment_group():
    pass


@click.command(cli_util.override('zone_group.command_name', 'zone'), cls=CommandGroupWithAlias, help="""A DNS zone.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def zone_group():
    pass


@click.command(cli_util.override('rr_set_group.command_name', 'rr-set'), cls=CommandGroupWithAlias, help="""A collection of DNS records of the same domain and type. For more information about record types, see [Resource Record (RR) TYPEs].""")
@cli_util.help_option_group
def rr_set_group():
    pass


@click.command(cli_util.override('record_collection_group.command_name', 'record-collection'), cls=CommandGroupWithAlias, help="""A collection of DNS resource records.""")
@cli_util.help_option_group
def record_collection_group():
    pass


@click.command(cli_util.override('steering_policy_group.command_name', 'steering-policy'), cls=CommandGroupWithAlias, help="""A DNS steering policy.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def steering_policy_group():
    pass


@click.command(cli_util.override('records_group.command_name', 'records'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def records_group():
    pass


@click.command(cli_util.override('zones_group.command_name', 'zones'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def zones_group():
    pass


dns_root_group.add_command(steering_policy_attachment_group)
dns_root_group.add_command(zone_group)
dns_root_group.add_command(rr_set_group)
dns_root_group.add_command(record_collection_group)
dns_root_group.add_command(steering_policy_group)
dns_root_group.add_command(records_group)
dns_root_group.add_command(zones_group)


@steering_policy_group.command(name=cli_util.override('create_steering_policy.command_name', 'create'), help=u"""Creates a new steering policy in the specified compartment. For more information on creating policies with templates, see [Traffic Management API Guide].""")
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
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'answers': {'module': 'dns', 'class': 'list[SteeringPolicyAnswer]'}, 'rules': {'module': 'dns', 'class': 'list[SteeringPolicyRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'answers': {'module': 'dns', 'class': 'list[SteeringPolicyAnswer]'}, 'rules': {'module': 'dns', 'class': 'list[SteeringPolicyRule]'}}, output_type={'module': 'dns', 'class': 'SteeringPolicy'})
@cli_util.wrap_exceptions
def create_steering_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, template, ttl, health_check_monitor_id, freeform_tags, defined_tags, answers, rules):

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['displayName'] = display_name
    details['template'] = template

    if ttl is not None:
        details['ttl'] = ttl

    if health_check_monitor_id is not None:
        details['healthCheckMonitorId'] = health_check_monitor_id

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if answers is not None:
        details['answers'] = cli_util.parse_json_parameter("answers", answers)

    if rules is not None:
        details['rules'] = cli_util.parse_json_parameter("rules", rules)

    client = cli_util.build_client('dns', ctx)
    result = client.create_steering_policy(
        create_steering_policy_details=details,
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


@steering_policy_attachment_group.command(name=cli_util.override('create_steering_policy_attachment.command_name', 'create'), help=u"""Creates a new attachment between a steering policy and a domain, giving the policy permission to answer queries for the specified domain. A steering policy must be attached to a domain for the policy to answer DNS queries for that domain.

For the purposes of access control, the attachment is automatically placed into the same compartment as the domain's zone.""")
@cli_util.option('--steering-policy-id', required=True, help=u"""The OCID of the attached steering policy.""")
@cli_util.option('--zone-id', required=True, help=u"""The OCID of the attached zone.""")
@cli_util.option('--domain-name', required=True, help=u"""The attached domain within the attached zone.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'SteeringPolicyAttachment'})
@cli_util.wrap_exceptions
def create_steering_policy_attachment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, steering_policy_id, zone_id, domain_name, display_name):

    kwargs = {}

    details = {}
    details['steeringPolicyId'] = steering_policy_id
    details['zoneId'] = zone_id
    details['domainName'] = domain_name

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('dns', ctx)
    result = client.create_steering_policy_attachment(
        create_steering_policy_attachment_details=details,
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


@zone_group.command(name=cli_util.override('create_zone.command_name', 'create'), help=u"""Creates a new zone in the specified compartment. The `compartmentId` query parameter is required if the `Content-Type` header for the request is `text/dns`.""")
@cli_util.option('--name', required=True, help=u"""The name of the zone.""")
@cli_util.option('--zone-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["PRIMARY", "SECONDARY"]), help=u"""The type of the zone. Must be either `PRIMARY` or `SECONDARY`.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

 **Example:** `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

 **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--external-masters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""External master servers for the zone. `externalMasters` becomes a required parameter when the `zoneType` value is `SECONDARY`.

This option is a JSON list with items of type ExternalMaster.  For documentation on ExternalMaster please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/ExternalMaster.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'external-masters': {'module': 'dns', 'class': 'list[ExternalMaster]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'external-masters': {'module': 'dns', 'class': 'list[ExternalMaster]'}}, output_type={'module': 'dns', 'class': 'Zone'})
@cli_util.wrap_exceptions
def create_zone(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, zone_type, freeform_tags, defined_tags, external_masters, compartment_id):

    kwargs = {}
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id

    details = {}
    details['name'] = name
    details['zoneType'] = zone_type
    details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if external_masters is not None:
        details['externalMasters'] = cli_util.parse_json_parameter("external_masters", external_masters)

    client = cli_util.build_client('dns', ctx)
    result = client.create_zone(
        create_zone_details=details,
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


@records_group.command(name=cli_util.override('delete_domain_records.command_name', 'delete-domain'), help=u"""Deletes all records at the specified zone and domain.""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_domain_records(ctx, from_json, zone_name_or_id, domain, if_match, if_unmodified_since, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    if isinstance(domain, six.string_types) and len(domain.strip()) == 0:
        raise click.UsageError('Parameter --domain cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    client = cli_util.build_client('dns', ctx)
    result = client.delete_domain_records(
        zone_name_or_id=zone_name_or_id,
        domain=domain,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rr_set_group.command(name=cli_util.override('delete_rr_set.command_name', 'delete'), help=u"""Deletes all records in the specified RRSet.""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--rtype', required=True, help=u"""The type of the target RRSet within the target zone.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_rr_set(ctx, from_json, zone_name_or_id, domain, rtype, if_match, if_unmodified_since, compartment_id):

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
    client = cli_util.build_client('dns', ctx)
    result = client.delete_rr_set(
        zone_name_or_id=zone_name_or_id,
        domain=domain,
        rtype=rtype,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@steering_policy_group.command(name=cli_util.override('delete_steering_policy.command_name', 'delete'), help=u"""Deletes the specified steering policy. A `204` response indicates that the delete has been successful. Deletion will fail if the policy is attached to any zones. To detach a policy from a zone, see `DeleteSteeringPolicyAttachment`.""")
@cli_util.option('--steering-policy-id', required=True, help=u"""The OCID of the target steering policy.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_steering_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, steering_policy_id, if_match, if_unmodified_since):

    if isinstance(steering_policy_id, six.string_types) and len(steering_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --steering-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    client = cli_util.build_client('dns', ctx)
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


@steering_policy_attachment_group.command(name=cli_util.override('delete_steering_policy_attachment.command_name', 'delete'), help=u"""Deletes the specified steering policy attachment. A `204` response indicates that the delete has been successful.""")
@cli_util.option('--steering-policy-attachment-id', required=True, help=u"""The OCID of the target steering policy attachment.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_steering_policy_attachment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, steering_policy_attachment_id, if_match, if_unmodified_since):

    if isinstance(steering_policy_attachment_id, six.string_types) and len(steering_policy_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --steering-policy-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    client = cli_util.build_client('dns', ctx)
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


@zone_group.command(name=cli_util.override('delete_zone.command_name', 'delete'), help=u"""Deletes the specified zone and all its steering policy attachments. A `204` response indicates that zone has been successfully deleted.""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_zone(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, zone_name_or_id, if_match, if_unmodified_since, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    client = cli_util.build_client('dns', ctx)
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


@records_group.command(name=cli_util.override('get_domain_records.command_name', 'get-domain'), help=u"""Gets a list of all records at the specified zone and domain. The results are sorted by `rtype` in alphabetical order by default. You can optionally filter and/or sort the results using the listed parameters.""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a page of the collection.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--zone-version', help=u"""The version of the zone for which data is requested.""")
@cli_util.option('--rtype', help=u"""Search by record type. Will match any record whose [type] (case-insensitive) equals the provided value.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["rtype", "ttl"]), help=u"""The field by which to sort records.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order to sort the resources.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def get_domain_records(ctx, from_json, all_pages, page_size, zone_name_or_id, domain, if_none_match, if_modified_since, limit, page, zone_version, rtype, sort_by, sort_order, compartment_id):

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
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    client = cli_util.build_client('dns', ctx)
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


@rr_set_group.command(name=cli_util.override('get_rr_set.command_name', 'get'), help=u"""Gets a list of all records in the specified RRSet. The results are sorted by `recordHash` by default.""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--rtype', required=True, help=u"""The type of the target RRSet within the target zone.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a page of the collection.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--zone-version', help=u"""The version of the zone for which data is requested.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'RRSet'})
@cli_util.wrap_exceptions
def get_rr_set(ctx, from_json, all_pages, page_size, zone_name_or_id, domain, rtype, if_none_match, if_modified_since, limit, page, zone_version, compartment_id):

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
    client = cli_util.build_client('dns', ctx)
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


@steering_policy_group.command(name=cli_util.override('get_steering_policy.command_name', 'get'), help=u"""Gets information about the specified steering policy.""")
@cli_util.option('--steering-policy-id', required=True, help=u"""The OCID of the target steering policy.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'SteeringPolicy'})
@cli_util.wrap_exceptions
def get_steering_policy(ctx, from_json, steering_policy_id, if_none_match, if_modified_since):

    if isinstance(steering_policy_id, six.string_types) and len(steering_policy_id.strip()) == 0:
        raise click.UsageError('Parameter --steering-policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    client = cli_util.build_client('dns', ctx)
    result = client.get_steering_policy(
        steering_policy_id=steering_policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@steering_policy_attachment_group.command(name=cli_util.override('get_steering_policy_attachment.command_name', 'get'), help=u"""Gets information about the specified steering policy attachment.""")
@cli_util.option('--steering-policy-attachment-id', required=True, help=u"""The OCID of the target steering policy attachment.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'SteeringPolicyAttachment'})
@cli_util.wrap_exceptions
def get_steering_policy_attachment(ctx, from_json, steering_policy_attachment_id, if_none_match, if_modified_since):

    if isinstance(steering_policy_attachment_id, six.string_types) and len(steering_policy_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --steering-policy-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    client = cli_util.build_client('dns', ctx)
    result = client.get_steering_policy_attachment(
        steering_policy_attachment_id=steering_policy_attachment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@zones_group.command(name=cli_util.override('get_zone.command_name', 'get'), help=u"""Gets information about the specified zone, including its creation date, zone type, and serial.""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--if-none-match', help=u"""The `If-None-Match` header field makes the request method conditional on the absence of any current representation of the target resource, when the field-value is `*`, or having a selected representation with an entity-tag that does not match any of those listed in the field-value.""")
@cli_util.option('--if-modified-since', help=u"""The `If-Modified-Since` header field makes a GET or HEAD request method conditional on the selected representation's modification date being more recent than the date provided in the field-value.  Transfer of the selected representation's data is avoided if that data has not changed.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'Zone'})
@cli_util.wrap_exceptions
def get_zone(ctx, from_json, zone_name_or_id, if_none_match, if_modified_since, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    if if_modified_since is not None:
        kwargs['if_modified_since'] = if_modified_since
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    client = cli_util.build_client('dns', ctx)
    result = client.get_zone(
        zone_name_or_id=zone_name_or_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@records_group.command(name=cli_util.override('get_zone_records.command_name', 'get-zone'), help=u"""Gets all records in the specified zone. The results are sorted by `domain` in alphabetical order by default. For more information about records, see [Resource Record (RR) TYPEs].""")
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
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def get_zone_records(ctx, from_json, all_pages, page_size, zone_name_or_id, if_none_match, if_modified_since, limit, page, zone_version, domain, domain_contains, rtype, sort_by, sort_order, compartment_id):

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
    client = cli_util.build_client('dns', ctx)
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


@steering_policy_group.command(name=cli_util.override('list_steering_policies.command_name', 'list'), help=u"""Gets a list of all steering policies in the specified compartment.""")
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
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'list[SteeringPolicySummary]'})
@cli_util.wrap_exceptions
def list_steering_policies(ctx, from_json, all_pages, page_size, compartment_id, limit, page, id, display_name, display_name_contains, health_check_monitor_id, time_created_greater_than_or_equal_to, time_created_less_than, template, lifecycle_state, sort_by, sort_order):

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
    client = cli_util.build_client('dns', ctx)
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


@steering_policy_attachment_group.command(name=cli_util.override('list_steering_policy_attachments.command_name', 'list'), help=u"""Lists the steering policy attachments in the specified compartment.""")
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
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'list[SteeringPolicyAttachmentSummary]'})
@cli_util.wrap_exceptions
def list_steering_policy_attachments(ctx, from_json, all_pages, page_size, compartment_id, limit, page, id, display_name, steering_policy_id, zone_id, domain, domain_contains, time_created_greater_than_or_equal_to, time_created_less_than, lifecycle_state, sort_by, sort_order):

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
    client = cli_util.build_client('dns', ctx)
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


@zones_group.command(name=cli_util.override('list_zones.command_name', 'list'), help=u"""Gets a list of all zones in the specified compartment. The collection can be filtered by name, time created, and zone type.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a page of the collection.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--name', help=u"""A case-sensitive filter for zone names. Will match any zone with a name that equals the provided value.""")
@cli_util.option('--name-contains', help=u"""Search by zone name. Will match any zone whose name (case-insensitive) contains the provided value.""")
@cli_util.option('--zone-type', type=custom_types.CliCaseInsensitiveChoice(["PRIMARY", "SECONDARY"]), help=u"""Search by zone type, `PRIMARY` or `SECONDARY`. Will match any zone whose type equals the provided value.""")
@cli_util.option('--time-created-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""An [RFC 3339] timestamp that states all returned resources were created on or after the indicated time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-created-less-than', type=custom_types.CLI_DATETIME, help=u"""An [RFC 3339] timestamp that states all returned resources were created before the indicated time.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), help=u"""The state of a resource.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["name", "zoneType", "timeCreated"]), help=u"""The field by which to sort zones.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order to sort the resources.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'list[ZoneSummary]'})
@cli_util.wrap_exceptions
def list_zones(ctx, from_json, all_pages, page_size, compartment_id, limit, page, name, name_contains, zone_type, time_created_greater_than_or_equal_to, time_created_less_than, lifecycle_state, sort_by, sort_order):

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
    client = cli_util.build_client('dns', ctx)
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


@records_group.command(name=cli_util.override('patch_domain_records.command_name', 'patch-domain'), help=u"""Updates records in the specified zone at a domain. You can update one record or all records for the specified zone depending on the changes provided in the request body. You can also add or remove records using this function.""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type RecordOperation.  For documentation on RecordOperation please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/RecordOperation.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'dns', 'class': 'list[RecordOperation]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'dns', 'class': 'list[RecordOperation]'}}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def patch_domain_records(ctx, from_json, zone_name_or_id, domain, items, if_match, if_unmodified_since, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    if isinstance(domain, six.string_types) and len(domain.strip()) == 0:
        raise click.UsageError('Parameter --domain cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id

    details = {}

    if items is not None:
        details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('dns', ctx)
    result = client.patch_domain_records(
        zone_name_or_id=zone_name_or_id,
        domain=domain,
        patch_domain_records_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@rr_set_group.command(name=cli_util.override('patch_rr_set.command_name', 'patch'), help=u"""Updates records in the specified RRSet.""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--rtype', required=True, help=u"""The type of the target RRSet within the target zone.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type RecordOperation.  For documentation on RecordOperation please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/RecordOperation.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'dns', 'class': 'list[RecordOperation]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'dns', 'class': 'list[RecordOperation]'}}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def patch_rr_set(ctx, from_json, zone_name_or_id, domain, rtype, items, if_match, if_unmodified_since, compartment_id):

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

    details = {}

    if items is not None:
        details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('dns', ctx)
    result = client.patch_rr_set(
        zone_name_or_id=zone_name_or_id,
        domain=domain,
        rtype=rtype,
        patch_rr_set_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@records_group.command(name=cli_util.override('patch_zone_records.command_name', 'patch-zone'), help=u"""Updates a collection of records in the specified zone. You can update one record or all records for the specified zone depending on the changes provided in the request body. You can also add or remove records using this function.""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type RecordOperation.  For documentation on RecordOperation please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/RecordOperation.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'dns', 'class': 'list[RecordOperation]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'dns', 'class': 'list[RecordOperation]'}}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def patch_zone_records(ctx, from_json, zone_name_or_id, items, if_match, if_unmodified_since, compartment_id):

    if isinstance(zone_name_or_id, six.string_types) and len(zone_name_or_id.strip()) == 0:
        raise click.UsageError('Parameter --zone-name-or-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id

    details = {}

    if items is not None:
        details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('dns', ctx)
    result = client.patch_zone_records(
        zone_name_or_id=zone_name_or_id,
        patch_zone_records_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@records_group.command(name=cli_util.override('update_domain_records.command_name', 'update-domain'), help=u"""Replaces records in the specified zone at a domain with the records specified in the request body. If a specified record does not exist, it will be created. If the record exists, then it will be updated to represent the record in the body of the request. If a record in the zone does not exist in the request body, the record will be removed from the zone.""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type RecordDetails.  For documentation on RecordDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/RecordDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'dns', 'class': 'list[RecordDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'dns', 'class': 'list[RecordDetails]'}}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def update_domain_records(ctx, from_json, force, zone_name_or_id, domain, items, if_match, if_unmodified_since, compartment_id):

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
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id

    details = {}

    if items is not None:
        details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('dns', ctx)
    result = client.update_domain_records(
        zone_name_or_id=zone_name_or_id,
        domain=domain,
        update_domain_records_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@record_collection_group.command(name=cli_util.override('update_rr_set.command_name', 'update-rr-set'), help=u"""Replaces records in the specified RRSet.""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--domain', required=True, help=u"""The target fully-qualified domain name (FQDN) within the target zone.""")
@cli_util.option('--rtype', required=True, help=u"""The type of the target RRSet within the target zone.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type RecordDetails.  For documentation on RecordDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/RecordDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'dns', 'class': 'list[RecordDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'dns', 'class': 'list[RecordDetails]'}}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def update_rr_set(ctx, from_json, force, zone_name_or_id, domain, rtype, items, if_match, if_unmodified_since, compartment_id):

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
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id

    details = {}

    if items is not None:
        details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('dns', ctx)
    result = client.update_rr_set(
        zone_name_or_id=zone_name_or_id,
        domain=domain,
        rtype=rtype,
        update_rr_set_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@steering_policy_group.command(name=cli_util.override('update_steering_policy.command_name', 'update'), help=u"""Updates the configuration of the specified steering policy.""")
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
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'answers': {'module': 'dns', 'class': 'list[SteeringPolicyAnswer]'}, 'rules': {'module': 'dns', 'class': 'list[SteeringPolicyRule]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'answers': {'module': 'dns', 'class': 'list[SteeringPolicyAnswer]'}, 'rules': {'module': 'dns', 'class': 'list[SteeringPolicyRule]'}}, output_type={'module': 'dns', 'class': 'SteeringPolicy'})
@cli_util.wrap_exceptions
def update_steering_policy(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, steering_policy_id, display_name, ttl, health_check_monitor_id, template, freeform_tags, defined_tags, answers, rules, if_match, if_unmodified_since):

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

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if ttl is not None:
        details['ttl'] = ttl

    if health_check_monitor_id is not None:
        details['healthCheckMonitorId'] = health_check_monitor_id

    if template is not None:
        details['template'] = template

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if answers is not None:
        details['answers'] = cli_util.parse_json_parameter("answers", answers)

    if rules is not None:
        details['rules'] = cli_util.parse_json_parameter("rules", rules)

    client = cli_util.build_client('dns', ctx)
    result = client.update_steering_policy(
        steering_policy_id=steering_policy_id,
        update_steering_policy_details=details,
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


@steering_policy_attachment_group.command(name=cli_util.override('update_steering_policy_attachment.command_name', 'update'), help=u"""Updates the specified steering policy attachment with your new information.""")
@cli_util.option('--steering-policy-attachment-id', required=True, help=u"""The OCID of the target steering policy attachment.""")
@cli_util.option('--display-name', help=u"""A user-friendly name for the steering policy attachment. Does not have to be unique and can be changed. Avoid entering confidential information.""")
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'dns', 'class': 'SteeringPolicyAttachment'})
@cli_util.wrap_exceptions
def update_steering_policy_attachment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, steering_policy_attachment_id, display_name, if_match, if_unmodified_since):

    if isinstance(steering_policy_attachment_id, six.string_types) and len(steering_policy_attachment_id.strip()) == 0:
        raise click.UsageError('Parameter --steering-policy-attachment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if if_unmodified_since is not None:
        kwargs['if_unmodified_since'] = if_unmodified_since

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('dns', ctx)
    result = client.update_steering_policy_attachment(
        steering_policy_attachment_id=steering_policy_attachment_id,
        update_steering_policy_attachment_details=details,
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


@zone_group.command(name=cli_util.override('update_zone.command_name', 'update'), help=u"""Updates the specified secondary zone with your new external master server information. For more information about secondary zone, see [Manage DNS Service Zone].""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

 **Example:** `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

 **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--external-masters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""External master servers for the zone. `externalMasters` becomes a required parameter when the `zoneType` value is `SECONDARY`.

This option is a JSON list with items of type ExternalMaster.  For documentation on ExternalMaster please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/ExternalMaster.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]), help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'external-masters': {'module': 'dns', 'class': 'list[ExternalMaster]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'dns', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dns', 'class': 'dict(str, dict(str, object))'}, 'external-masters': {'module': 'dns', 'class': 'list[ExternalMaster]'}}, output_type={'module': 'dns', 'class': 'Zone'})
@cli_util.wrap_exceptions
def update_zone(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, zone_name_or_id, freeform_tags, defined_tags, external_masters, if_match, if_unmodified_since, compartment_id):

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
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id

    details = {}

    if freeform_tags is not None:
        details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if external_masters is not None:
        details['externalMasters'] = cli_util.parse_json_parameter("external_masters", external_masters)

    client = cli_util.build_client('dns', ctx)
    result = client.update_zone(
        zone_name_or_id=zone_name_or_id,
        update_zone_details=details,
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


@records_group.command(name=cli_util.override('update_zone_records.command_name', 'update-zone'), help=u"""Replaces records in the specified zone with the records specified in the request body. If a specified record does not exist, it will be created. If the record exists, then it will be updated to represent the record in the body of the request. If a record in the zone does not exist in the request body, the record will be removed from the zone.""")
@cli_util.option('--zone-name-or-id', required=True, help=u"""The name or OCID of the target zone.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""

This option is a JSON list with items of type RecordDetails.  For documentation on RecordDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/dns/20180115/datatypes/RecordDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""The `If-Match` header field makes the request method conditional on the existence of at least one current representation of the target resource, when the field-value is `*`, or having a current representation of the target resource that has an entity-tag matching a member of the list of entity-tags provided in the field-value.""")
@cli_util.option('--if-unmodified-since', help=u"""The `If-Unmodified-Since` header field makes the request method conditional on the selected representation's last modification date being earlier than or equal to the date provided in the field-value.  This field accomplishes the same purpose as If-Match for cases where the user agent does not have an entity-tag for the representation.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment the resource belongs to.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'dns', 'class': 'list[RecordDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'dns', 'class': 'list[RecordDetails]'}}, output_type={'module': 'dns', 'class': 'RecordCollection'})
@cli_util.wrap_exceptions
def update_zone_records(ctx, from_json, force, zone_name_or_id, items, if_match, if_unmodified_since, compartment_id):

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
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id

    details = {}

    if items is not None:
        details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('dns', ctx)
    result = client.update_zone_records(
        zone_name_or_id=zone_name_or_id,
        update_zone_records_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
