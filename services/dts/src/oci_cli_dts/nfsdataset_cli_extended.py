# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function

import click
import time

from oci import exceptions
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias

from services.dts.src.oci_cli_dts.generated import dts_service_cli
from services.dts.src.oci_cli_dts.nfs_dataset_client_proxy import NfsDatasetClientProxy
from services.dts.src.oci_cli_dts.physical_appliance_control_plane.client.models.nfs_dataset_info import NfsDatasetInfo


"""
nfs-dataset command
This is a local command set and not generated from spec, but created here.
These commands help setup the nfs-datasets on the appliance.
"""


@click.command('nfs-dataset', cls=CommandGroupWithAlias, help="""NFS Dataset Operations""")
@cli_util.help_option_group
def nfs_dataset_group():
    pass


dts_service_cli.dts_service_group.add_command(nfs_dataset_group)


@nfs_dataset_group.command('show', help=u"""Shows the NFS Dataset details""")
@cli_util.option('--name', required=True, help=u"""Dataset Name""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Transfer Appliance profile""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'NFSDataset'})
@cli_util.wrap_exceptions
def nfs_dataset_show(ctx, from_json, name, appliance_profile):
    nfs_dataset_client = create_nfs_dataset_client(ctx, appliance_profile)
    nfs_dataset_info = nfs_dataset_client.get_nfs_dataset(name)
    cli_util.render_response(nfs_dataset_info, ctx)


@nfs_dataset_group.command('list', help=u"""Lists all of the NFS datasets""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Transfer Appliance profile""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'NFSDataset'})
@cli_util.wrap_exceptions
def nfs_dataset_list(ctx, from_json, appliance_profile):
    click.echo("Listing NFS datasets")
    nfs_dataset_client = create_nfs_dataset_client(ctx, appliance_profile)
    nfs_datasets = nfs_dataset_client.list_nfs_datasets()
    cli_util.render_response(nfs_datasets, ctx)


@nfs_dataset_group.command('create', help=u"""Creates, sets exports on an NFS Dataset""")
@cli_util.option('--rw', type=click.BOOL, help=u"""Read/Write option on export""")
@cli_util.option('--world', type=click.BOOL, help=u"""World option on export""")
@cli_util.option('--ip', help=u"""IP address to export to""")
@cli_util.option('--subnet-mask-length', type=click.INT, help=u"""Subnet mask length for the IP address""")
@cli_util.option('--name', required=True, help=u"""Dataset Name""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Transfer Appliance profile""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'NFSDataset'})
@cli_util.wrap_exceptions
def nfs_dataset_create(ctx, from_json, rw, world, ip, subnet_mask_length, name, appliance_profile):
    result = _create_nfs_dataset_helper(
        create_nfs_dataset_client(ctx, appliance_profile), rw, world, ip, subnet_mask_length, name)
    cli_util.render_response(result, ctx)


def _create_nfs_dataset_helper(nfs_dataset_client, rw, world, ip, subnet_mask_length, name):
    click.echo("Creating dataset with NFS export details {}".format(name))
    if (rw is None and world is not None) or (rw is not None and world is None):
        raise exceptions.ClientError("--rw and --world have to be passed together. You cannot set only one of them")
    export_configs = [{
        'readWrite': rw,
        'world': world,
        'ipAddress': ip,
        'subnetMaskLength': subnet_mask_length,
        'hostname': None
    }] if rw is not None and world is not None else None
    details = {
        'name': name,
        'nfsExportDetails': {
            'exportConfigs': export_configs
        }
    }
    return nfs_dataset_client.create_nfs_dataset(details)


@nfs_dataset_group.command('set-export', help=u"""Add an NFS export configuration for the dataset""")
@cli_util.option('--rw', required=True, type=click.BOOL, help=u"""Read/Write option on export""")
@cli_util.option('--world', required=True, type=click.BOOL, help=u"""World option on export""")
@cli_util.option('--ip', help=u"""IP address to export to""")
@cli_util.option('--subnet-mask-length', type=click.INT, help=u"""Subnet mask length for the IP address""")
@cli_util.option('--name', required=True, help=u"""Dataset Name""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Transfer Appliance profile""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'NFSDataset'})
@cli_util.wrap_exceptions
def nfs_dataset_set_export(ctx, from_json, rw, world, ip, subnet_mask_length, name, appliance_profile):
    click.echo("Settings NFS exports to dataset {}".format(name))
    nfs_dataset_client = create_nfs_dataset_client(ctx, appliance_profile)
    body = {
        'name': name,
        'nfsExportDetails': {
            'exportConfigs': [
                {
                    'readWrite': rw,
                    'world': world,
                    'ipAddress': ip,
                    'subnetMaskLength': subnet_mask_length,
                    'hostname': None
                }
            ]
        }
    }
    nfs_dataset_info = nfs_dataset_client.update_nfs_dataset(name, body)
    cli_util.render_response(nfs_dataset_info, ctx)


@nfs_dataset_group.command('activate', help=u"""Creates, sets exports and Activates the NFS dataset""")
@cli_util.option('--rw', type=click.BOOL, help=u"""Read/Write option on export""")
@cli_util.option('--world', type=click.BOOL, help=u"""World option on export""")
@cli_util.option('--ip', help=u"""IP address to export to""")
@cli_util.option('--subnet-mask-length', type=click.INT, help=u"""Subnet mask length for the IP address""")
@cli_util.option('--name', required=True, help=u"""Dataset Name""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Transfer Appliance profile""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'NFSDataset'})
@cli_util.wrap_exceptions
def nfs_dataset_activate(ctx, from_json, rw, world, ip, subnet_mask_length, name, appliance_profile):
    """
    1. Get all the datasets
    2. Check if the dataset name provided exists in the received datasets
        1. If it exists, check if it is sealed
            1. If sealed, reopen and activate the dataset
            2. If not sealed, just activate the dataset
        2. If it doesn't exist, create the dataset with exports followed by activating it
    """
    nfs_dataset_client = create_nfs_dataset_client(ctx, appliance_profile)
    click.echo("Fetching all the datasets")
    nfs_datasets = nfs_dataset_client.list_nfs_datasets().data
    nfs_dataset = next((item for item in nfs_datasets if item['name'] == name), None)
    if nfs_dataset is not None:
        if nfs_dataset['state'] == NfsDatasetInfo.STATE_SEALED:
            click.echo("Reopening the dataset {} because it was sealed".format(name))
            nfs_dataset_client.reopen_nfs_dataset(name)
    else:
        result = _create_nfs_dataset_helper(nfs_dataset_client, rw, world, ip, subnet_mask_length, name)
        cli_util.render_response(result, ctx)
    click.echo("Activating dataset {}".format(name))
    nfs_dataset_client.activate_nfs_dataset(name)
    click.echo("Dataset {} activated".format(name))


@nfs_dataset_group.command('deactivate', help=u"""Deactivates the NFS dataset""")
@cli_util.option('--name', required=True, help=u"""Dataset Name""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Transfer Appliance profile""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'NFSDataset'})
@cli_util.wrap_exceptions
def nfs_dataset_deactivate(ctx, from_json, name, appliance_profile):
    nfs_dataset_client = create_nfs_dataset_client(ctx, appliance_profile)
    click.echo("Deactivating dataset {}".format(name))
    nfs_dataset_info = nfs_dataset_client.deactivate_nfs_dataset(name)
    cli_util.render_response(nfs_dataset_info, ctx)


@nfs_dataset_group.command('seal', help=u"""Seals the NFS dataset and deactivates it if it is active""")
@cli_util.option('--wait', is_flag=True, help=u"""Waits until seal is complete""")
@cli_util.option('--name', help=u"""Dataset Name""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Transfer Appliance profile""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'NFSDataset'})
@cli_util.wrap_exceptions
def nfs_dataset_seal(ctx, from_json, wait, name, appliance_profile):
    """
    1. Get the datasets. Since there is only one dataset, deactivate it if present, else throw a not found error
    2. If the dataset is ACTIVE, deactivate it
    3. Seal the dataset
    """
    nfs_dataset_client = create_nfs_dataset_client(ctx, appliance_profile)

    click.echo("Initiating Seal .... \n(Track progress using 'oci dts nfs-dataset seal-status' command)")
    click.echo("Fetching all the datasets ...\n")
    nfs_datasets = nfs_dataset_client.list_nfs_datasets().data
    if len(nfs_datasets) < 1:
        raise exceptions.ClientError("No datasets exist. Create a Dataset first")
    nfs_dataset = nfs_datasets[0]
    if name is not None:
        if name != nfs_dataset['name']:
            raise exceptions.ClientError("The dataset {} does not exist".format(name))
    name = nfs_dataset['name']
    if nfs_dataset['state'] == NfsDatasetInfo.STATE_ACTIVE:
        click.echo("Deactivating the dataset {}".format(name))
        nfs_dataset_client.deactivate_nfs_dataset(name)

    click.echo("Triggering seal on dataset {}".format(name))
    click.echo("This performs a pre-walk of the file system to check for invalid files before walking again "
               "to do the actual seal. This process can be time consuming depending on the size and number of files. "
               "Progress will be displayed once the pre-walk is done.")
    nfs_dataset_client.initiate_seal_on_nfs_dataset(name)
    seal_status = nfs_dataset_client.get_nfs_dataset_seal_status(name).data
    if wait:
        _seal_progress_display(seal_status)
        while seal_status['completed'] is None or not seal_status['completed']:
            time.sleep(0.5)
            seal_status = nfs_dataset_client.get_nfs_dataset_seal_status(name).data
            _seal_progress_display(seal_status)
        cli_util.render(seal_status, None, ctx)


def _seal_progress_display(seal_status):
    if seal_status['bytesToProcess'] > 0 and seal_status['numFilesToProcess'] > 0:
        click.echo("\nFiles processed: {} / {}".format(seal_status['numFilesProcessed'], seal_status['numFilesToProcess']))
        click.echo("\nBytes processed: {} / {}".format(seal_status['bytesProcessed'], seal_status['bytesToProcess']))


@nfs_dataset_group.command('delete', help=u"""Deletes the NFS dataset""")
@cli_util.option('--name', required=True, help=u"""Dataset Name""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Transfer Appliance profile""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'NFSDataset'})
@cli_util.wrap_exceptions
def nfs_dataset_delete(ctx, from_json, name, appliance_profile):
    nfs_dataset_client = create_nfs_dataset_client(ctx, appliance_profile)
    click.echo("Deleting dataset {}".format(name))
    nfs_dataset_client.delete_nfs_dataset(name)
    click.echo("Successfully deleted the dataset {}".format(name))


@nfs_dataset_group.command('seal-status', help=u"""Retrieves the NFS dataset's seal status""")
@cli_util.option('--name', required=True, help=u"""Dataset Name""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Transfer Appliance profile""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'NFSDataset'})
@cli_util.wrap_exceptions
def nfs_dataset_get_seal_status(ctx, from_json, name, appliance_profile):
    nfs_dataset_client = create_nfs_dataset_client(ctx, appliance_profile)
    click.echo("Getting the seal status of the dataset {}".format(name))
    seal_status = nfs_dataset_client.get_nfs_dataset_seal_status(name)
    cli_util.render_response(seal_status, ctx)


@nfs_dataset_group.command('get-seal-manifest', help=u"""Retrieves the NFS dataset's seal manifest""")
@cli_util.option('--output-file', required=True, help=u"""File path where the manifest has to be written""")
@cli_util.option('--name', required=True, help=u"""Dataset Name""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Transfer Appliance profile""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'NFSDataset'})
@cli_util.wrap_exceptions
def nfs_dataset_get_seal_manifest(ctx, from_json, output_file, name, appliance_profile):
    nfs_dataset_client = create_nfs_dataset_client(ctx, appliance_profile)
    click.echo("Retrieving the seal manifest from the transfer appliance and writing it to {}. "
               "Duration of this operation depends on the size of the manifest which in turn is "
               "dependent on the number of files in the dataset".format(output_file))
    stream = nfs_dataset_client.get_nfs_dataset_seal_manifest(name).data
    write_to_file(output_file, stream)
    click.echo("Dataset seal manifest written to {}".format(output_file))


def write_to_file(output_file, stream):
    with open(output_file, 'wb') as f:
        f.write(stream)


@nfs_dataset_group.command('reopen', help=u"""Reopens a sealed NFS dataset""")
@cli_util.option('--name', required=True, help=u"""Dataset Name""")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help=u"""Transfer Appliance profile""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={},
                                                      output_type={'module': 'dts', 'class': 'NFSDataset'})
@cli_util.wrap_exceptions
def nfs_dataset_reopen(ctx, from_json, name, appliance_profile):
    nfs_dataset_client = create_nfs_dataset_client(ctx, appliance_profile)
    click.echo("Re-opening the dataset {}".format(name))
    nfs_dataset_info = nfs_dataset_client.reopen_nfs_dataset(name)
    cli_util.render_response(nfs_dataset_info, ctx)


def create_nfs_dataset_client(ctx, appliance_profile):
    return NfsDatasetClientProxy(ctx, appliance_profile)


def nfs_dataset_deactivate_helper(ctx, **nfs_deactivate_kwargs):
    ctx.invoke(nfs_dataset_deactivate, **nfs_deactivate_kwargs)


def deactivate_nfs_dataset(ctx, appliance_profile, **nfs_dataset):
    '''
    This method checks the state of NFS_dataset and deactivates if the state is active
    :param ctx
    :param appliance_profile: str
    :param nfs_dataset: dict {'name': <dataset_name>, 'state':<state of dataset>}
    :return:
    '''
    nfs_deactivate_kwargs = {
        'name': nfs_dataset['name'],
        'appliance_profile': appliance_profile
    }
    if nfs_dataset['state'] == NfsDatasetInfo.STATE_ACTIVE:
        click.echo("Deactivating the dataset {}".format(nfs_dataset['name']))
        nfs_dataset_deactivate_helper(ctx, **nfs_deactivate_kwargs)
    else:
        click.echo("NFS-Dataset: {} is in NOT_ACTIVE state".format(nfs_dataset['name']))
