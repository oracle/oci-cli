# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import click
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli.cli_util import get_param
from services.ocvp.src.oci_cli_esxi_host.generated import esxihost_cli
from services.ocvp.src.oci_cli_ocvp.generated import ocvs_service_cli

# Shorten parameters for create command
get_param(esxihost_cli.create_esxi_host, 'display_name').opts.extend(['--name'])

# Shorten parameters for update command
get_param(esxihost_cli.update_esxi_host, 'display_name').opts.extend(['--name'])

# Shorten parameters for list command
get_param(esxihost_cli.list_esxi_hosts, 'display_name').opts.extend(['--name'])


@cli_util.copy_params_from_generated_command(esxihost_cli.delete_esxi_host, params_to_exclude=['esxi_host_id'])
@esxihost_cli.esxi_host_group.command(name=cli_util.override('delete_esxi_host.command_name', 'delete'), help=esxihost_cli.delete_esxi_host.help)
@cli_util.option('--esxi-id', required=True, help=u"""The [OCID] of the ESXi host.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_esxi_host(ctx, **kwargs):
    if 'esxi_id' in kwargs:
        kwargs['esxi_host_id'] = kwargs['esxi_id']
        kwargs.pop('esxi_id')

    ctx.invoke(esxihost_cli.delete_esxi_host, **kwargs)


@cli_util.copy_params_from_generated_command(esxihost_cli.get_esxi_host, params_to_exclude=['esxi_host_id'])
@esxihost_cli.esxi_host_group.command(name=cli_util.override('get_esxi_host.command_name', 'get'), help=esxihost_cli.get_esxi_host.help)
@cli_util.option('--esxi-id', required=True, help=u"""The [OCID] of the ESXi host.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ocvp', 'class': 'EsxiHost'})
@cli_util.wrap_exceptions
def get_esxi_host(ctx, **kwargs):
    if 'esxi_id' in kwargs:
        kwargs['esxi_host_id'] = kwargs['esxi_id']
        kwargs.pop('esxi_id')

    ctx.invoke(esxihost_cli.get_esxi_host, **kwargs)


@cli_util.copy_params_from_generated_command(esxihost_cli.update_esxi_host, params_to_exclude=['esxi_host_id'])
@esxihost_cli.esxi_host_group.command(name=cli_util.override('update_esxi_host.command_name', 'update'), help=esxihost_cli.update_esxi_host.help)
@cli_util.option('--esxi-id', required=True, help=u"""The [OCID] of the ESXi host.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'ocvp', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'ocvp', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'ocvp', 'class': 'EsxiHost'})
@cli_util.wrap_exceptions
def update_esxi_host(ctx, **kwargs):
    if 'esxi_id' in kwargs:
        kwargs['esxi_host_id'] = kwargs['esxi_id']
        kwargs.pop('esxi_id')

    ctx.invoke(esxihost_cli.update_esxi_host, **kwargs)


@cli_util.copy_params_from_generated_command(esxihost_cli.list_esxi_hosts, params_to_exclude=['compute_instance_id'])
@esxihost_cli.esxi_host_group.command(name=cli_util.override('list_esxi_hosts.command_name', 'list'), help=esxihost_cli.list_esxi_hosts.help)
@cli_util.option('--compute-id', help=cli_util.get_param(esxihost_cli.list_esxi_hosts, 'compute_instance_id').help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'ocvp', 'class': 'EsxiHostCollection'})
@cli_util.wrap_exceptions
def list_esxi_host(ctx, **kwargs):
    if 'compute_id' in kwargs:
        kwargs['compute_instance_id'] = kwargs['compute_id']
        kwargs.pop('compute_id')

    ctx.invoke(esxihost_cli.list_esxi_hosts, **kwargs)


ocvs_service_cli.ocvs_service_group.commands.pop(esxihost_cli.esxi_host_root_group.name)
ocvs_service_cli.ocvs_service_group.add_command(esxihost_cli.esxi_host_group)
esxihost_cli.esxi_host_group.add_command(list_esxi_host)
