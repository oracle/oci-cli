# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import io
import os.path

import click
import json
from services.cims.src.oci_cli_incident.generated import incident_cli
from oci_cli import cli_util
from services.cims.src.oci_cli_incident.generated.incident_cli import incident_group
from oci_cli import custom_types
from oci_cli import json_skeleton_utils

from oci_cli import cli_exceptions

# remove update-incident stand-alone command
# incident_cli.incident_root_group.commands.pop(incident_cli.update_incident_group.name)
# incident_cli.incident_root_group.commands.pop(incident_cli.status_group.name)


# add command to incident group
incident_cli.incident_group.add_command(incident_cli.update_incident)


# rename update-incident to just update
cli_util.rename_command(incident_cli, incident_group, incident_cli.update_incident, "update")


# modify csi parameter to be required for incident create, and flatten JSON parameter for ticket to be required params.
@cli_util.copy_params_from_generated_command(incident_cli.create_incident, params_to_exclude=['csi', 'ticket'])
@incident_cli.incident_group.command(name=cli_util.override('support.create_incident.command_name', 'create'),
                                     help=u"""This API enables the customer to Create an Incident""")
@cli_util.option('--csi', required=True, help=u'''Customer Support Identifier''')
@cli_util.option('--severity', required=True,
                 type=custom_types.CliCaseInsensitiveChoice(["LOW", "MEDIUM", "HGIH", "HIGHEST"]),
                 help=u"""States severity level of incident. Acceptable values are LOW, MEDIUM, HIGH, HIGHEST.  Please note for HIGHEST: Oracle Support requires a 24x7 contact be provided so additional information can be requested as needed 24x7.)""")
@cli_util.option('--title', required=True,
                 help=u"""Title for the SR.  Should be a high level description of issue.  eg:  Cannot connect to instance""")
@cli_util.option('--description', required=True,
                 help=u"""This should be the description of the SR with a more granular level of detail as to what the problem you are facing is.  eg: I cannot connect to my compute instance.  I have tried ssh, ping, traceroute, and provide the results of those.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={'ticket': {'module': 'cims', 'class': 'CreateTicketDetails'},
                                   'contacts': {'module': 'cims', 'class': 'list[Contact]'}},
    output_type={'module': 'cims', 'class': 'Incident'})
@cli_util.wrap_exceptions
def create_incident_extended(ctx, **kwargs):
    ticket = {}
    if 'severity' in kwargs:
        ticket['severity'] = kwargs['severity']
        kwargs.pop('severity')

    if 'title' in kwargs:
        ticket['title'] = kwargs['title']
        kwargs.pop('title')

    if 'description' in kwargs:
        ticket['description'] = kwargs['description']
        kwargs.pop('description')

    if len(ticket) > 0:
        kwargs['ticket'] = json.dumps(ticket)

    ctx.invoke(incident_cli.create_incident, **kwargs)


# modify update incident to flatten ticket parameter to required params.
@cli_util.copy_params_from_generated_command(incident_cli.update_incident, params_to_exclude=['ticket', 'comments'])
@incident_cli.incident_group.command(name=cli_util.override('support.update_incident.command_name', 'update'),
                                     help=u"""This API enables the customer to Update an Incident""")
@cli_util.option('--activity-type', required=True,
                 help=u"""This is the action to be taken on the ticket.  Acceptable values are (CASE SENSITIVE) NOTES, EMAIL_OUTBOUND, EMAIL_INBOUND, CLOSE, UPDATE, PROBLEM_DESCRIPTION, ADD_CONTACT""")
@cli_util.option('--type', required=True,
                 help=u"""Valid types are activity and contact. To add additional contact to the Service Request, use contact as type.""")
@cli_util.option('--comments', required=False,
                 help=u"""String text field with the comment you wish to add to the ticket. comments field is mandatory when --type is activity. Must put the string in quotes.""")
@cli_util.option('--contact', required=False,
                 help=u"""Email of the additional contact to be added to a Service request. contact field is mandatory when --type is contact.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={'ticket': {'module': 'cims', 'class': 'UpdateTicketDetails'}},
    output_type={'module': 'cims', 'class': 'Incident'})
@cli_util.wrap_exceptions
def update_incident_extended(ctx, **kwargs):

    if kwargs['comments'] and kwargs['contact']:
        raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Cannot specify both --comments and --contact')

    if not kwargs['comments'] and not kwargs['contact']:
        raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Must specify either --comments or --contacts')

    ticket = {}

    if 'activity_type' in kwargs:
        ticket['acitivityType'] = kwargs['activity_type']

    if 'comments' in kwargs:
        ticket['comments'] = kwargs['comments']

    if 'type' in kwargs:
        ticket['type'] = kwargs['type']

    if 'contact' in kwargs:
        ticket['contact'] = kwargs['contact']

    if kwargs['type'] == 'contact':
        ticket = {'resource': {
            'item': {'activityType': kwargs['activity_type'], 'contact': kwargs['contact'], 'type': kwargs['type']}}}
    elif kwargs['type'] == 'activity':
        ticket = {'resource': {
            'item': {'activityType': kwargs['activity_type'], 'comments': kwargs['comments'], 'type': kwargs['type']}}}
    else:
        raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('--type must be either activity or contact')

    kwargs['ticket'] = json.dumps(ticket)

    kwargs.pop('activity_type')
    kwargs.pop('type')
    kwargs.pop('comments')
    kwargs.pop('contact')

    ctx.invoke(incident_cli.update_incident, **kwargs)


@cli_util.copy_params_from_generated_command(incident_cli.put_attachment, params_to_exclude=['attachment_name', 'put_attachment_details'])
@incident_group.command(name=cli_util.override('support.put_attachment.command_name', 'put-attachment'), help=u"""Uploads the file and attaches it to the support request. \n[Command Reference](putAttachment)""")
@cli_util.option('--file', required=True, type=click.File('rb'),
                 help=u"""File to be uploaded as attachment to the Service Request.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'cims', 'class': 'Incident'})
@cli_util.wrap_exceptions
def put_attachment_extended(ctx, **kwargs):
    if 'file' in kwargs:
        attachment_file_path = kwargs['file']
        kwargs['attachment_name'] = os.path.basename(attachment_file_path.name)
        file_content = bytearray(attachment_file_path.read())
        kwargs['put_attachment_details'] = io.BytesIO(file_content)

    kwargs.pop('file')
    ctx.invoke(incident_cli.put_attachment, **kwargs)
