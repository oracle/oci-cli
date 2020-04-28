# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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


@cli.command(cli_util.override('support.support_root_group.command_name', 'support'), cls=CommandGroupWithAlias, help=cli_util.override('support.support_root_group.help', """Use the Support Management API to manage support requests. For more information, see [Getting Help and Contacting Support]. **Note**: Before you can create service requests with this API, you need to have an Oracle Single Sign On (SSO) account, and you need to register your Customer Support Identifier (CSI) with My Oracle Support."""), short_help=cli_util.override('support.support_root_group.short_help', """Support Management API"""))
@cli_util.help_option_group
def support_root_group():
    pass


@click.command(cli_util.override('support.update_incident_group.command_name', 'update-incident'), cls=CommandGroupWithAlias, help="""Details of Resource Item to be updated""")
@cli_util.help_option_group
def update_incident_group():
    pass


@click.command(cli_util.override('support.incident_resource_type_group.command_name', 'incident-resource-type'), cls=CommandGroupWithAlias, help="""Details of incident type""")
@cli_util.help_option_group
def incident_resource_type_group():
    pass


@click.command(cli_util.override('support.validation_response_group.command_name', 'validation-response'), cls=CommandGroupWithAlias, help="""Validation Response""")
@cli_util.help_option_group
def validation_response_group():
    pass


@click.command(cli_util.override('support.incident_group.command_name', 'incident'), cls=CommandGroupWithAlias, help="""Details of Incident""")
@cli_util.help_option_group
def incident_group():
    pass


@click.command(cli_util.override('support.status_group.command_name', 'status'), cls=CommandGroupWithAlias, help="""Details of Ticket Status""")
@cli_util.help_option_group
def status_group():
    pass


support_root_group.add_command(update_incident_group)
support_root_group.add_command(incident_resource_type_group)
support_root_group.add_command(validation_response_group)
support_root_group.add_command(incident_group)
support_root_group.add_command(status_group)


@incident_group.command(name=cli_util.override('support.create_incident.command_name', 'create'), help=u"""This API enables the customer to Create an Incident""")
@cli_util.option('--compartment-id', required=True, help=u"""Tenancy Ocid""")
@cli_util.option('--ticket', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--problem-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT"]), help=u"""States type of incident. eg: LIMIT, TECH""")
@cli_util.option('--ocid', required=True, help=u"""User OCID for IDCS users that have a shadow in OCI""")
@cli_util.option('--csi', help=u"""Customer Support Identifier of the support account""")
@cli_util.option('--contacts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of contacts

This option is a JSON list with items of type Contact.  For documentation on Contact please see our API reference: https://docs.cloud.oracle.com/api/#/en/incident/20181231/datatypes/Contact.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--referrer', help=u"""Referrer of the incident., its usually the URL for where the customer logged the incident""")
@json_skeleton_utils.get_cli_json_input_option({'ticket': {'module': 'cims', 'class': 'CreateTicketDetails'}, 'contacts': {'module': 'cims', 'class': 'list[Contact]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ticket': {'module': 'cims', 'class': 'CreateTicketDetails'}, 'contacts': {'module': 'cims', 'class': 'list[Contact]'}}, output_type={'module': 'cims', 'class': 'Incident'})
@cli_util.wrap_exceptions
def create_incident(ctx, from_json, compartment_id, ticket, problem_type, ocid, csi, contacts, referrer):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['ticket'] = cli_util.parse_json_parameter("ticket", ticket)
    _details['problemType'] = problem_type

    if csi is not None:
        _details['csi'] = csi

    if contacts is not None:
        _details['contacts'] = cli_util.parse_json_parameter("contacts", contacts)

    if referrer is not None:
        _details['referrer'] = referrer

    client = cli_util.build_client('cims', 'incident', ctx)
    result = client.create_incident(
        ocid=ocid,
        create_incident_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@incident_group.command(name=cli_util.override('support.get_incident.command_name', 'get'), help=u"""This API fetches the details of a requested Incident""")
@cli_util.option('--incident-key', required=True, help=u"""Unique ID that identifies an incident""")
@cli_util.option('--csi', required=True, help=u"""Customer Support Identifier of the support account""")
@cli_util.option('--ocid', required=True, help=u"""User OCID for IDCS users that have a shadow in OCI""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cims', 'class': 'Incident'})
@cli_util.wrap_exceptions
def get_incident(ctx, from_json, incident_key, csi, ocid):

    if isinstance(incident_key, six.string_types) and len(incident_key.strip()) == 0:
        raise click.UsageError('Parameter --incident-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cims', 'incident', ctx)
    result = client.get_incident(
        incident_key=incident_key,
        csi=csi,
        ocid=ocid,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@status_group.command(name=cli_util.override('support.get_status.command_name', 'get'), help=u"""GetStatus of the Service""")
@cli_util.option('--source', required=True, help=u"""Source is a downstream system. Eg: JIRA or MOS or any other source in future.""")
@cli_util.option('--ocid', required=True, help=u"""User OCID for IDCS users that have a shadow in OCI""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cims', 'class': 'Status'})
@cli_util.wrap_exceptions
def get_status(ctx, from_json, source, ocid):

    if isinstance(source, six.string_types) and len(source.strip()) == 0:
        raise click.UsageError('Parameter --source cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cims', 'incident', ctx)
    result = client.get_status(
        source=source,
        ocid=ocid,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@incident_resource_type_group.command(name=cli_util.override('support.list_incident_resource_types.command_name', 'list'), help=u"""This API returns the list of all possible product that OCI supports, while creating an incident""")
@cli_util.option('--problem-type', required=True, help=u"""Problem Type of Taxonomy - tech/limit""")
@cli_util.option('--compartment-id', required=True, help=u"""Tenancy Ocid""")
@cli_util.option('--csi', required=True, help=u"""Customer Support Identifier of the support account""")
@cli_util.option('--ocid', required=True, help=u"""User OCID for IDCS users that have a shadow in OCI""")
@cli_util.option('--limit', type=click.INT, help=u"""Limit query for number of returned results""")
@cli_util.option('--page', help=u"""Pagination for Incident list""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["dateUpdated", "severity"]), help=u"""The key to sort the returned items by""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order in which to sort the results""")
@cli_util.option('--name', help=u"""Name of Incident Type. eg: Limit Increase""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cims', 'class': 'list[IncidentResourceType]'})
@cli_util.wrap_exceptions
def list_incident_resource_types(ctx, from_json, all_pages, page_size, problem_type, compartment_id, csi, ocid, limit, page, sort_by, sort_order, name):

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
    if name is not None:
        kwargs['name'] = name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cims', 'incident', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_incident_resource_types,
            problem_type=problem_type,
            compartment_id=compartment_id,
            csi=csi,
            ocid=ocid,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_incident_resource_types,
            limit,
            page_size,
            problem_type=problem_type,
            compartment_id=compartment_id,
            csi=csi,
            ocid=ocid,
            **kwargs
        )
    else:
        result = client.list_incident_resource_types(
            problem_type=problem_type,
            compartment_id=compartment_id,
            csi=csi,
            ocid=ocid,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@incident_group.command(name=cli_util.override('support.list_incidents.command_name', 'list'), help=u"""This API returns the list of incidents raised by the tenant""")
@cli_util.option('--csi', required=True, help=u"""Customer Support Identifier of the support account""")
@cli_util.option('--compartment-id', required=True, help=u"""Tenancy Ocid""")
@cli_util.option('--ocid', required=True, help=u"""User OCID for IDCS users that have a shadow in OCI""")
@cli_util.option('--limit', type=click.INT, help=u"""Limit query for number of returned results""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["dateUpdated", "severity"]), help=u"""The key to sort the returned items by""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order in which to sort the results""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CLOSED"]), help=u"""The order in which to sort the results""")
@cli_util.option('--page', help=u"""Pagination for Incident list""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cims', 'class': 'list[IncidentSummary]'})
@cli_util.wrap_exceptions
def list_incidents(ctx, from_json, all_pages, page_size, csi, compartment_id, ocid, limit, sort_by, sort_order, lifecycle_state, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cims', 'incident', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_incidents,
            csi=csi,
            compartment_id=compartment_id,
            ocid=ocid,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_incidents,
            limit,
            page_size,
            csi=csi,
            compartment_id=compartment_id,
            ocid=ocid,
            **kwargs
        )
    else:
        result = client.list_incidents(
            csi=csi,
            compartment_id=compartment_id,
            ocid=ocid,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@update_incident_group.command(name=cli_util.override('support.update_incident.command_name', 'update-incident'), help=u"""This API updates an existing incident""")
@cli_util.option('--incident-key', required=True, help=u"""Unique ID that identifies an incident""")
@cli_util.option('--csi', required=True, help=u"""Customer Support Identifier of the support account""")
@cli_util.option('--ticket', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ocid', required=True, help=u"""User OCID for IDCS users that have a shadow in OCI""")
@cli_util.option('--if-match', help=u"""if-match check""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'ticket': {'module': 'cims', 'class': 'UpdateTicketDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ticket': {'module': 'cims', 'class': 'UpdateTicketDetails'}}, output_type={'module': 'cims', 'class': 'Incident'})
@cli_util.wrap_exceptions
def update_incident(ctx, from_json, force, incident_key, csi, ticket, ocid, if_match):

    if isinstance(incident_key, six.string_types) and len(incident_key.strip()) == 0:
        raise click.UsageError('Parameter --incident-key cannot be whitespace or empty string')
    if not force:
        if ticket:
            if not click.confirm("WARNING: Updates to ticket will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['ticket'] = cli_util.parse_json_parameter("ticket", ticket)

    client = cli_util.build_client('cims', 'incident', ctx)
    result = client.update_incident(
        incident_key=incident_key,
        csi=csi,
        ocid=ocid,
        update_incident_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@validation_response_group.command(name=cli_util.override('support.validate_user.command_name', 'validate-user'), help=u"""ValidateUser""")
@cli_util.option('--csi', required=True, help=u"""Customer support identifier of the support account""")
@cli_util.option('--ocid', required=True, help=u"""User OCID for IDCS users that have a shadow in OCI""")
@cli_util.option('--problem-type', help=u"""Problem Type of Taxonomy - tech/limit""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cims', 'class': 'ValidationResponse'})
@cli_util.wrap_exceptions
def validate_user(ctx, from_json, csi, ocid, problem_type):

    kwargs = {}
    if problem_type is not None:
        kwargs['problem_type'] = problem_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cims', 'incident', ctx)
    result = client.validate_user(
        csi=csi,
        ocid=ocid,
        **kwargs
    )
    cli_util.render_response(result, ctx)
