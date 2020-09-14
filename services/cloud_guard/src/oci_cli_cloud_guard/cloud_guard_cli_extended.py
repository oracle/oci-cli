# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from services.cloud_guard.src.oci_cli_cloud_guard.generated import cloudguard_cli


@cli_util.copy_params_from_generated_command(cloudguard_cli.list_problems, params_to_exclude=['region_parameterconflict'])
@cloudguard_cli.problem_group.command(name=cli_util.override('cloud_guard.list_problems.command_name', 'list'), help=cloudguard_cli.list_problems.help)
@cli_util.option('--problem-region', help=u"""OCI Monitoring region.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'detector-rule-id-list': {'module': 'cloud_guard', 'class': 'list[string]'}}, output_type={'module': 'cloud_guard', 'class': 'list[ProblemSummary]'})
@cli_util.wrap_exceptions
def list_problems_extended(ctx, **kwargs):
    if 'problem_region' in kwargs:
        kwargs['region_parameterconflict'] = kwargs['problem_region']
        kwargs.pop('problem_region')
    ctx.invoke(cloudguard_cli.list_problems, **kwargs)
