# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import click
import json

from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from services.analytics.src.oci_cli_analytics.generated import analytics_cli

#
# Customizations for:
#     oci analytics analytics-instance create
#
# --idcs-access-token replaced by --idcs-access-token-file file paramenter.
# --capacity complex type replaced by --capacity-type and --capacity-value
#


@cli_util.copy_params_from_generated_command(analytics_cli.create_analytics_instance, params_to_exclude=['capacity', 'idcs_access_token'])
@analytics_cli.analytics_instance_group.command(name='create', help=analytics_cli.create_analytics_instance.help)
@cli_util.option('--idcs-access-token-file', type=click.File('r'), help=u"""A file containing the IDCS access token identifying a stripe and service administrator user.""")
@cli_util.option('--capacity-type', required=True, help=u"""The capacity model to use.""")
@cli_util.option('--capacity-value', type=click.INT, required=True, help=u"""The capacity value selected (OLPU count, number of users, ...etc...). This parameter affects the number of CPUs, amount of memory or other resources allocated to the instance.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'defined-tags': {'module': 'analytics', 'class': 'dict(str, dict(str, object))'}, 'freeform-tags': {'module': 'analytics', 'class': 'dict(str, string)'}}, output_type={'module': 'analytics', 'class': 'AnalyticsInstance'})
@cli_util.wrap_exceptions
def create_analytics_instance_extended(ctx, **kwargs):

    # "capcity" complex type.
    capacity = {}

    # Add "capacityType" parameter.
    if 'capacity_type' in kwargs and kwargs['capacity_type']:
        capacity['capacityType'] = kwargs['capacity_type']

    # Add "capacityValue" parameter.
    if 'capacity_value' in kwargs and kwargs['capacity_value']:
        capacity['capacityValue'] = kwargs['capacity_value']

    # Set "--idcs-access-token" to the content of file "--idcs-access-token-file"
    if 'idcs_access_token_file' in kwargs and kwargs['idcs_access_token_file']:
        content = [line.rstrip('\n') for line in kwargs['idcs_access_token_file']]
        kwargs['idcs_access_token'] = ''.join(content).strip()

    # Set "--capacity" complex type from the values collected above.
    kwargs['capacity'] = json.dumps(capacity)

    # Remove the extram parameters not expected on base method "create_analytics_instance".
    del kwargs['capacity_type']
    del kwargs['capacity_value']
    del kwargs['idcs_access_token_file']

    # Invoke base method "create_analytics_instance"
    ctx.invoke(analytics_cli.create_analytics_instance, **kwargs)
