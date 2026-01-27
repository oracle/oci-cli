# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates. All rights reserved.

import click

from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401

from services.dif.src.oci_cli_stack.generated import stack_cli


@cli_util.copy_params_from_generated_command(stack_cli.add_service, params_to_exclude=['services', 'stack_templates'])
@stack_cli.stack_group.command(name=cli_util.override('dif.add_service.command_name', 'add'), help=u"""Add new service or update existing service. \n[Command Reference](addService)""")
@cli_util.option('--stack-templates', required=True, multiple=True, type=custom_types.CliCaseInsensitiveChoice(["DATALAKE", "DATAPIPELINE", "AISERVICES", "DATATRANSFORMATION"]), help=u"""List of templates to be added for the stack.""")
@cli_util.option('--services', required=True, multiple=True, type=custom_types.CliCaseInsensitiveChoice(["ADB", "GGCS", "OBJECTSTORAGE", "GENAI", "DATAFLOW"]), help=u"""List of services to be added for the stack.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'adb': {'module': 'dif', 'class': 'list[AdbDetail]'}, 'ggcs': {'module': 'dif', 'class': 'list[GgcsDetail]'}, 'dataflow': {'module': 'dif', 'class': 'list[DataflowDetail]'}, 'objectstorage': {'module': 'dif', 'class': 'list[ObjectStorageDetail]'}, 'genai': {'module': 'dif', 'class': 'list[GenAiDetail]'}})
@cli_util.wrap_exceptions
def add_service_extended(ctx, **kwargs):
    ctx.invoke(stack_cli.add_service, **kwargs)


@cli_util.copy_params_from_generated_command(stack_cli.create_stack, params_to_exclude=['services', 'stack_templates'])
@stack_cli.stack_group.command(name=cli_util.override('dif.create_stack.command_name', 'create'), help=u"""Creates a Stack. \n[Command Reference](createStack)""")
@cli_util.option('--stack-templates', required=True, multiple=True, type=custom_types.CliCaseInsensitiveChoice(["DATALAKE", "DATAPIPELINE", "AISERVICES", "DATATRANSFORMATION"]), help=u"""List of templates to be onboarded for the stack.""")
@cli_util.option('--services', required=True, multiple=True, type=custom_types.CliCaseInsensitiveChoice(["ADB", "GGCS", "OBJECTSTORAGE", "GENAI", "DATAFLOW"]), help=u"""List of services to be onboarded for the stack.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'adb': {'module': 'dif', 'class': 'list[AdbDetail]'}, 'ggcs': {'module': 'dif', 'class': 'list[GgcsDetail]'}, 'dataflow': {'module': 'dif', 'class': 'list[DataflowDetail]'}, 'objectstorage': {'module': 'dif', 'class': 'list[ObjectStorageDetail]'}, 'genai': {'module': 'dif', 'class': 'list[GenAiDetail]'}, 'freeform-tags': {'module': 'dif', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dif', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'dif', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack_extended(ctx, **kwargs):
    ctx.invoke(stack_cli.create_stack, **kwargs)


@cli_util.copy_params_from_generated_command(stack_cli.deploy_artifacts, params_to_exclude=['services', 'stack_templates'])
@stack_cli.stack_group.command(name=cli_util.override('dif.deploy_artifacts.command_name', 'deploy-artifacts'), help=u"""DeployArtifacts \n[Command Reference](deployArtifacts)""")
@cli_util.option('--stack-templates', required=True, multiple=True, type=custom_types.CliCaseInsensitiveChoice(["DATALAKE", "DATAPIPELINE", "AISERVICES", "DATATRANSFORMATION"]), help=u"""List of templates to be onboarded for the stack.""")
@cli_util.option('--services', required=True, multiple=True, type=custom_types.CliCaseInsensitiveChoice(["ADB", "GGCS", "OBJECTSTORAGE", "GENAI", "DATAFLOW"]), help=u"""List of services to be onboarded for the stack.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'adb': {'module': 'dif', 'class': 'list[AdbArtifactsDetail]'}, 'ggcs': {'module': 'dif', 'class': 'list[GgcsArtifactsDetail]'}, 'dataflow': {'module': 'dif', 'class': 'list[DataflowArtifactsDetail]'}})
@cli_util.wrap_exceptions
def deploy_artifacts_extended(ctx, **kwargs):
    ctx.invoke(stack_cli.deploy_artifacts, **kwargs)


@cli_util.copy_params_from_generated_command(stack_cli.update_stack, params_to_exclude=['services', 'stack_templates'])
@stack_cli.stack_group.command(name=cli_util.override('dif.update_stack.command_name', 'update'), help=u"""Updates a Stack. \n[Command Reference](updateStack)""")
@cli_util.option('--stack-templates', multiple=True, type=custom_types.CliCaseInsensitiveChoice(["DATALAKE", "DATAPIPELINE", "AISERVICES", "DATATRANSFORMATION"]), help=u"""List of templates to be updated for the stack.""")
@cli_util.option('--services', multiple=True, type=custom_types.CliCaseInsensitiveChoice(["ADB", "GGCS", "OBJECTSTORAGE", "GENAI", "DATAFLOW"]), help=u"""List of services to be updated for the stack.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'adb': {'module': 'dif', 'class': 'list[AdbUpdateDetail]'}, 'ggcs': {'module': 'dif', 'class': 'list[GgcsUpdateDetail]'}, 'dataflow': {'module': 'dif', 'class': 'list[DataflowUpdateDetail]'}, 'objectstorage': {'module': 'dif', 'class': 'list[ObjectStorageUpdateDetail]'}, 'genai': {'module': 'dif', 'class': 'list[GenAiUpdateDetail]'}, 'freeform-tags': {'module': 'dif', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'dif', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_stack(ctx, **kwargs):
    ctx.invoke(stack_cli.update_stack, **kwargs)
