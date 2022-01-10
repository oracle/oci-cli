# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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
from services.cims.src.oci_cli_cims.generated import support_service_cli


@click.command(cli_util.override('incident.incident_root_group.command_name', 'incident'), cls=CommandGroupWithAlias, help=cli_util.override('incident.incident_root_group.help', """Use the Support Management API to manage support requests. For more information, see [Getting Help and Contacting Support]. **Note**: Before you can create service requests with this API, you need to have an Oracle Single Sign On (SSO) account, and you need to register your Customer Support Identifier (CSI) with My Oracle Support."""), short_help=cli_util.override('incident.incident_root_group.short_help', """Support Management API"""))
@cli_util.help_option_group
def incident_root_group():
    pass


@click.command(cli_util.override('incident.update_incident_group.command_name', 'update-incident'), cls=CommandGroupWithAlias, help="""Details about the support ticket being updated.""")
@cli_util.help_option_group
def update_incident_group():
    pass


@click.command(cli_util.override('incident.incident_resource_type_group.command_name', 'incident-resource-type'), cls=CommandGroupWithAlias, help="""Details about the resource associated with the support request.""")
@cli_util.help_option_group
def incident_resource_type_group():
    pass


@click.command(cli_util.override('incident.validation_response_group.command_name', 'validation-response'), cls=CommandGroupWithAlias, help="""The validation response returned when checking whether the requested user is valid.""")
@cli_util.help_option_group
def validation_response_group():
    pass


@click.command(cli_util.override('incident.incident_group.command_name', 'incident'), cls=CommandGroupWithAlias, help="""Details of about the incident object.""")
@cli_util.help_option_group
def incident_group():
    pass


@click.command(cli_util.override('incident.status_group.command_name', 'status'), cls=CommandGroupWithAlias, help="""Details about the status of the support ticket.""")
@cli_util.help_option_group
def status_group():
    pass


support_service_cli.support_service_group.add_command(incident_root_group)
incident_root_group.add_command(update_incident_group)
incident_root_group.add_command(incident_resource_type_group)
incident_root_group.add_command(validation_response_group)
incident_root_group.add_command(incident_group)
incident_root_group.add_command(status_group)


@incident_group.command(name=cli_util.override('incident.create_incident.command_name', 'create'), help=u"""Enables the customer to create an support ticket. \n[Command Reference](createIncident)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy.""")
@cli_util.option('--ticket', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--problem-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["LIMIT", "LEGACY_LIMIT", "TECH", "ACCOUNT"]), help=u"""The kind of support ticket, such as a technical issue request.""")
@cli_util.option('--ocid', required=True, help=u"""User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.""")
@cli_util.option('--csi', help=u"""The Customer Support Identifier number for the support account.""")
@cli_util.option('--contacts', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of contacts.

This option is a JSON list with items of type Contact.  For documentation on Contact please see our API reference: https://docs.cloud.oracle.com/api/#/en/incident/20181231/datatypes/Contact.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--referrer', help=u"""The incident referrer. This value is often the URL that the customer used when creating the support ticket.""")
@cli_util.option('--homeregion', help=u"""The region of the tenancy.""")
@json_skeleton_utils.get_cli_json_input_option({'ticket': {'module': 'cims', 'class': 'CreateTicketDetails'}, 'contacts': {'module': 'cims', 'class': 'list[Contact]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ticket': {'module': 'cims', 'class': 'CreateTicketDetails'}, 'contacts': {'module': 'cims', 'class': 'list[Contact]'}}, output_type={'module': 'cims', 'class': 'Incident'})
@cli_util.wrap_exceptions
def create_incident(ctx, from_json, compartment_id, ticket, problem_type, ocid, csi, contacts, referrer, homeregion):

    kwargs = {}
    if homeregion is not None:
        kwargs['homeregion'] = homeregion
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


@incident_group.command(name=cli_util.override('incident.get_incident.command_name', 'get'), help=u"""Gets the details of the support ticket. \n[Command Reference](getIncident)""")
@cli_util.option('--incident-key', required=True, help=u"""Unique identifier for the support ticket.""")
@cli_util.option('--csi', required=True, help=u"""The Customer Support Identifier associated with the support account.""")
@cli_util.option('--ocid', required=True, help=u"""User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.""")
@cli_util.option('--homeregion', help=u"""The region of the tenancy.""")
@cli_util.option('--problem-type', help=u"""The kind of support request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cims', 'class': 'Incident'})
@cli_util.wrap_exceptions
def get_incident(ctx, from_json, incident_key, csi, ocid, homeregion, problem_type):

    if isinstance(incident_key, six.string_types) and len(incident_key.strip()) == 0:
        raise click.UsageError('Parameter --incident-key cannot be whitespace or empty string')

    kwargs = {}
    if homeregion is not None:
        kwargs['homeregion'] = homeregion
    if problem_type is not None:
        kwargs['problem_type'] = problem_type
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cims', 'incident', ctx)
    result = client.get_incident(
        incident_key=incident_key,
        csi=csi,
        ocid=ocid,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@status_group.command(name=cli_util.override('incident.get_status.command_name', 'get'), help=u"""Gets the status of the service. \n[Command Reference](getStatus)""")
@cli_util.option('--source', required=True, help=u"""The system that generated the support ticket, such as My Oracle Support.""")
@cli_util.option('--ocid', required=True, help=u"""User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.""")
@cli_util.option('--homeregion', help=u"""The region of the tenancy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cims', 'class': 'Status'})
@cli_util.wrap_exceptions
def get_status(ctx, from_json, source, ocid, homeregion):

    if isinstance(source, six.string_types) and len(source.strip()) == 0:
        raise click.UsageError('Parameter --source cannot be whitespace or empty string')

    kwargs = {}
    if homeregion is not None:
        kwargs['homeregion'] = homeregion
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cims', 'incident', ctx)
    result = client.get_status(
        source=source,
        ocid=ocid,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@incident_resource_type_group.command(name=cli_util.override('incident.list_incident_resource_types.command_name', 'list'), help=u"""During support ticket creation, returns the list of all possible products that Oracle Cloud Infrastructure supports. \n[Command Reference](listIncidentResourceTypes)""")
@cli_util.option('--problem-type', required=True, help=u"""The kind of support request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy.""")
@cli_util.option('--csi', required=True, help=u"""The Customer Support Identifier associated with the support account.""")
@cli_util.option('--ocid', required=True, help=u"""User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["dateUpdated", "severity"]), help=u"""The key to use to sort the returned items.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order to sort the results in.""")
@cli_util.option('--name', help=u"""The user-friendly name of the incident type.""")
@cli_util.option('--homeregion', help=u"""The region of the tenancy.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cims', 'class': 'list[IncidentResourceType]'})
@cli_util.wrap_exceptions
def list_incident_resource_types(ctx, from_json, all_pages, page_size, problem_type, compartment_id, csi, ocid, limit, page, sort_by, sort_order, name, homeregion):

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
    if homeregion is not None:
        kwargs['homeregion'] = homeregion
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


@incident_group.command(name=cli_util.override('incident.list_incidents.command_name', 'list'), help=u"""Returns the list of support tickets raised by the tenancy. \n[Command Reference](listIncidents)""")
@cli_util.option('--csi', required=True, help=u"""The Customer Support Identifier associated with the support account.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy.""")
@cli_util.option('--ocid', required=True, help=u"""User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["dateUpdated", "severity"]), help=u"""The key to use to sort the returned items.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The order to sort the results in.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "CLOSED"]), help=u"""The current state of the ticket.""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--homeregion', help=u"""The region of the tenancy.""")
@cli_util.option('--problem-type', help=u"""The kind of support request.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cims', 'class': 'list[IncidentSummary]'})
@cli_util.wrap_exceptions
def list_incidents(ctx, from_json, all_pages, page_size, csi, compartment_id, ocid, limit, sort_by, sort_order, lifecycle_state, page, homeregion, problem_type):

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
    if homeregion is not None:
        kwargs['homeregion'] = homeregion
    if problem_type is not None:
        kwargs['problem_type'] = problem_type
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


@update_incident_group.command(name=cli_util.override('incident.update_incident.command_name', 'update-incident'), help=u"""Updates the specified support ticket's information. \n[Command Reference](updateIncident)""")
@cli_util.option('--incident-key', required=True, help=u"""Unique identifier for the support ticket.""")
@cli_util.option('--csi', required=True, help=u"""The Customer Support Identifier associated with the support account.""")
@cli_util.option('--ticket', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ocid', required=True, help=u"""User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--homeregion', help=u"""The region of the tenancy.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'ticket': {'module': 'cims', 'class': 'UpdateTicketDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'ticket': {'module': 'cims', 'class': 'UpdateTicketDetails'}}, output_type={'module': 'cims', 'class': 'Incident'})
@cli_util.wrap_exceptions
def update_incident(ctx, from_json, force, incident_key, csi, ticket, ocid, if_match, homeregion):

    if isinstance(incident_key, six.string_types) and len(incident_key.strip()) == 0:
        raise click.UsageError('Parameter --incident-key cannot be whitespace or empty string')
    if not force:
        if ticket:
            if not click.confirm("WARNING: Updates to ticket will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if homeregion is not None:
        kwargs['homeregion'] = homeregion
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


@validation_response_group.command(name=cli_util.override('incident.validate_user.command_name', 'validate-user'), help=u"""Checks whether the requested user is valid. \n[Command Reference](validateUser)""")
@cli_util.option('--csi', required=True, help=u"""The Customer Support Identifier number for the support account.""")
@cli_util.option('--ocid', required=True, help=u"""User OCID for Oracle Identity Cloud Service (IDCS) users who also have a federated Oracle Cloud Infrastructure account.""")
@cli_util.option('--problem-type', help=u"""The kind of support request.""")
@cli_util.option('--homeregion', help=u"""The region of the tenancy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'cims', 'class': 'ValidationResponse'})
@cli_util.wrap_exceptions
def validate_user(ctx, from_json, csi, ocid, problem_type, homeregion):

    kwargs = {}
    if problem_type is not None:
        kwargs['problem_type'] = problem_type
    if homeregion is not None:
        kwargs['homeregion'] = homeregion
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('cims', 'incident', ctx)
    result = client.validate_user(
        csi=csi,
        ocid=ocid,
        **kwargs
    )
    cli_util.render_response(result, ctx)
