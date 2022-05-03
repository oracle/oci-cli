# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click
from oci_cli import cli_util, json_skeleton_utils

from services.rover.src.oci_cli_rover.generated import rover_service_cli
from services.rover.src.oci_cli_rover.rover_utils import setup_master_key_policy, \
    validate_policy_parameters


@rover_service_cli.rover_service_group.command(name="create-master-key-policy",
                                               help=u"""Create Policy for Master key""")
@cli_util.option('--master-key-id', required=True, help=u"""Unique RoverStandalone Cluster identifier""")
@cli_util.option('--policy-compartment-id', help=u"""Compartment ID where the policy should be created""")
@cli_util.option('--policy-name', help=u"""Display name for the policy to be created""")
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'rover', 'class': 'RoverCluster'})
@cli_util.wrap_exceptions
def create_master_key_policy_extended(ctx, **kwargs):
    validate_policy_parameters(**kwargs)
    result = setup_master_key_policy(ctx, **kwargs)
    cli_util.render_response(result, ctx)
