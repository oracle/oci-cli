# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import click
import os
import os.path
import sys
from oci_cli_resource_manager.generated import resourcemanager_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
import oci  # noqa: F401
import base64
import zipfile

resourcemanager_cli.stack_group.commands.pop(resourcemanager_cli.create_stack.name)
resourcemanager_cli.stack_group.commands.pop(resourcemanager_cli.update_stack.name)


def create_base64encoded_zip(config_source):
    if config_source.endswith(".zip") and os.path.isfile(config_source) and zipfile.is_zipfile(config_source):
        with open(config_source, mode='rb') as zip_file:
            return base64.b64encode(zip_file.read()).decode('utf-8')


@cli_util.copy_params_from_generated_command(resourcemanager_cli.create_stack, params_to_exclude=['config_source'])
@resourcemanager_cli.stack_group.command(name=cli_util.override('create_stack.command_name', 'create'), help="""Creates a Stack""")
@cli_util.option('--config-source', required=True, help="""A Terraform configuration .zip file.""")
@cli_util.option('--working-directory', help=""" The path of the directory from which to run terraform. If not specified the root will be used.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'resource_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def create_stack_extended(ctx, config_source, working_directory, **kwargs):

    config_source = os.path.expandvars(os.path.expanduser(config_source))
    if not os.path.exists(config_source):
        click.echo('Config source does not exist', file=sys.stderr)
        ctx.abort()

    if not (config_source.endswith(".zip") and os.path.isfile(config_source) and zipfile.is_zipfile(config_source)):
        click.echo('Config source must be a .zip file.', file=sys.stderr)
        ctx.abort()

    send_value = create_base64encoded_zip(config_source)
    if not send_value:
        click.echo('Internal error: Unable to generate encoded zip', file=sys.stderr)
        ctx.abort()

    kwargs['config_source'] = {
        'configSourceType': oci.resource_manager.models.ConfigSource.CONFIG_SOURCE_TYPE_ZIP_UPLOAD,
        'zipFileBase64Encoded': send_value}

    if working_directory is not None:
        kwargs['config_source']['workingDirectory'] = working_directory

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)
    ctx.invoke(resourcemanager_cli.create_stack, **kwargs)


@cli_util.copy_params_from_generated_command(resourcemanager_cli.update_stack, params_to_exclude=['config_source'])
@resourcemanager_cli.stack_group.command(name=cli_util.override('update_stack.command_name', 'update'), help="""Update the Stack object""")
@cli_util.option('--config-source', help="""A Terraform configuration .zip file.""")
@cli_util.option('--working-directory', help=""" The path of the directory from which to run terraform. If not specified the root will be used.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'variables': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'freeform-tags': {'module': 'resource_manager', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'resource_manager', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'reseouce_manager', 'class': 'Stack'})
@cli_util.wrap_exceptions
def update_stack_extended(ctx, config_source, working_directory, **kwargs):

    if working_directory is not None or config_source is not None:
        kwargs['config_source'] = {'configSourceType': oci.resource_manager.models.ConfigSource.CONFIG_SOURCE_TYPE_ZIP_UPLOAD}

        if working_directory is not None:
            kwargs['config_source']['workingDirectory'] = working_directory

        if config_source is not None:
            config_source = os.path.expandvars(os.path.expanduser(config_source))
            if not os.path.exists(config_source):
                click.echo('Config source does not exist', file=sys.stderr)
                ctx.abort()

            if not (config_source.endswith(".zip") and os.path.isfile(config_source) and zipfile.is_zipfile(config_source)):
                click.echo('Config source must be a .zip file.', file=sys.stderr)
                ctx.abort()

            send_value = create_base64encoded_zip(config_source)
            if not send_value:
                click.echo('Internal error: Unable to generate encoded zip', file=sys.stderr)
                ctx.abort()

            kwargs['config_source']['zipFileBase64Encoded'] = send_value

    json_skeleton_utils.remove_json_skeleton_params_from_dict(kwargs)
    ctx.invoke(resourcemanager_cli.update_stack, **kwargs)
