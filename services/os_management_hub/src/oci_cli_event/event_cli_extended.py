# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.os_management_hub.src.oci_cli_os_management_hub.generated import os_management_hub_service_cli
from services.os_management_hub.src.oci_cli_event.generated import event_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


@cli_util.copy_params_from_generated_command(event_cli.list_events, params_to_exclude=['time_created_less_than', 'time_created_greater_than_or_equal_to', 'is_managed_by_autonomous_linux'])
@event_cli.event_group.command(name=cli_util.override('event.list_events.command_name', 'list'), help=event_cli.list_events.help)
@cli_util.option('--time-created-lt', type=custom_types.CLI_DATETIME, help=u"""A filter that returns events that occurred on or before the date provided. Example: `2016-08-25T21:10:29.600Z`

The following datetime formats are supported:

UTC with microseconds
***********************
Format: YYYY-MM-DDTHH:mm:ss.ssssssTZD
Example: 2017-09-15T20:30:00.123456Z

UTC with milliseconds
***********************
Format: YYYY-MM-DDTHH:mm:ss.sssTZD
Example: 2017-09-15T20:30:00.123Z

UTC without milliseconds
**************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example: 2017-09-15T20:30:00Z

UTC with minute precision
**************************
Format: YYYY-MM-DDTHH:mmTZD
Example: 2017-09-15T20:30Z

Timezone with microseconds
***************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00.456789-08:00,
2017-09-15T12:30:00.456789-0800

Timezone with milliseconds
***************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00.456-08:00,
2017-09-15T12:30:00.456-0800

Timezone without milliseconds
*******************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00-08:00,
2017-09-15T12:30:00-0800

Timezone with minute precision
*******************************
Format: YYYY-MM-DDTHH:mmTZD
Example:
2017-09-15T12:30-08:00,
2017-09-15T12:30-0800

Short date and time
********************
The timezone for this date and time will be taken as UTC (Needs to be surrounded by single or double quotes)
Format: 'YYYY-MM-DD HH:mm' or "YYYY-MM-DD HH:mm"
Example: '2017-09-15 17:25'

Date Only
*********
This date will be taken as midnight UTC of that day
Format: YYYY-MM-DD
Example: 2017-09-15

Epoch seconds
**************
Example: 1412195400
    """)
@cli_util.option('--time-created-gte', type=custom_types.CLI_DATETIME, help=u"""A filter that returns events that occurred on or after the date provided. Example: `2016-08-25T21:10:29.600Z`

The following datetime formats are supported:

UTC with microseconds
***********************
Format: YYYY-MM-DDTHH:mm:ss.ssssssTZD
Example: 2017-09-15T20:30:00.123456Z

UTC with milliseconds
***********************
Format: YYYY-MM-DDTHH:mm:ss.sssTZD
Example: 2017-09-15T20:30:00.123Z

UTC without milliseconds
**************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example: 2017-09-15T20:30:00Z

UTC with minute precision
**************************
Format: YYYY-MM-DDTHH:mmTZD
Example: 2017-09-15T20:30Z

Timezone with microseconds
***************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00.456789-08:00,
2017-09-15T12:30:00.456789-0800

Timezone with milliseconds
***************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00.456-08:00,
2017-09-15T12:30:00.456-0800

Timezone without milliseconds
*******************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00-08:00,
2017-09-15T12:30:00-0800

Timezone with minute precision
*******************************
Format: YYYY-MM-DDTHH:mmTZD
Example:
2017-09-15T12:30-08:00,
2017-09-15T12:30-0800

Short date and time
********************
The timezone for this date and time will be taken as UTC (Needs to be surrounded by single or double quotes)
Format: 'YYYY-MM-DD HH:mm' or "YYYY-MM-DD HH:mm"
Example: '2017-09-15 17:25'

Date Only
*********
This date will be taken as midnight UTC of that day
Format: YYYY-MM-DD
Example: 2017-09-15

Epoch seconds
**************
Example: 1412195400
    """)
@cli_util.option('--is-managed-by-alx', type=click.BOOL, help=u"""Indicates whether to list only resources managed by the Autonomous Linux service.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management_hub', 'class': 'EventCollection'})
@cli_util.wrap_exceptions
def list_events_extended(ctx, **kwargs):

    if 'time_created_lt' in kwargs:
        kwargs['time_created_less_than'] = kwargs['time_created_lt']
        kwargs.pop('time_created_lt')

    if 'time_created_gte' in kwargs:
        kwargs['time_created_greater_than_or_equal_to'] = kwargs['time_created_gte']
        kwargs.pop('time_created_gte')

    if 'is_managed_by_alx' in kwargs:
        kwargs['is_managed_by_autonomous_linux'] = kwargs['is_managed_by_alx']
        kwargs.pop('is_managed_by_alx')

    ctx.invoke(event_cli.list_events, **kwargs)


# Move commands under 'oci os-management-hub event event' -> 'oci os-management-hub event'
event_cli.event_root_group.commands.pop(event_cli.event_group.name)
os_management_hub_service_cli.os_management_hub_service_group.commands.pop(event_cli.event_root_group.name)
os_management_hub_service_cli.os_management_hub_service_group.add_command(event_cli.event_group)

# Move commands under 'oci os-management-hub event event-collection' -> 'oci os-management-hub event'
event_cli.event_root_group.commands.pop(event_cli.event_collection_group.name)
# this is the same annotating the extended method with @event_cli.event_group.command
event_cli.event_group.add_command(list_events_extended)

# oci os-management-hub event get-event-content -> oci os-management-hub event get-event-content
cli_util.rename_command(event_cli, event_cli.event_group, event_cli.get_event_content, "get-event-content")

# oci os-management-hub event delete-event-content -> oci os-management-hub event delete-event-content
cli_util.rename_command(event_cli, event_cli.event_group, event_cli.delete_event_content, "delete-event-content")
