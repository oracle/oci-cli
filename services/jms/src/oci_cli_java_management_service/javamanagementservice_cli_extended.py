# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.jms.src.oci_cli_java_management_service.generated import javamanagementservice_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


@cli_util.copy_params_from_generated_command(javamanagementservice_cli.update_fleet_agent_configuration, params_to_exclude=['java_usage_tracker_processing_frequency_in_minutes', 'jre_scan_frequency_in_minutes'])
@javamanagementservice_cli.fleet_agent_configuration_group.command(name=javamanagementservice_cli.update_fleet_agent_configuration.name, help=javamanagementservice_cli.update_fleet_agent_configuration.help)
@cli_util.option('--jut-processing-frequency', type=click.INT, help=u"""The frequency (in minutes) of Java Usage Tracker processing. (That is, how often should JMS process data from the Java Usage Tracker.)""")
@cli_util.option('--jre-scan-frequency', type=click.INT, help=u"""The frequency (in minutes) of JRE scanning. (That is, how often should JMS scan for JRE installations.)""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'linux-configuration': {'module': 'jms', 'class': 'FleetAgentOsConfiguration'}, 'windows-configuration': {'module': 'jms', 'class': 'FleetAgentOsConfiguration'}})
@cli_util.wrap_exceptions
def update_fleet_agent_configuration_extended(ctx, **kwargs):
    if 'jut_processing_frequency' in kwargs:
        kwargs['java_usage_tracker_processing_frequency_in_minutes'] = kwargs['jut_processing_frequency']
        kwargs.pop('jut_processing_frequency')

    if 'jre_scan_frequency' in kwargs:
        kwargs['jre_scan_frequency_in_minutes'] = kwargs['jre_scan_frequency']
        kwargs.pop('jre_scan_frequency')

    ctx.invoke(javamanagementservice_cli.update_fleet_agent_configuration, **kwargs)
