# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

import click
from .generated import bastion_cli

from oci_cli import cli_util
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils
import json

cli_util.rename_command(bastion_cli, bastion_cli.session_group,
                        bastion_cli.create_session_create_managed_ssh_session_target_resource_details,
                        "create-managed-ssh")
cli_util.rename_command(bastion_cli, bastion_cli.session_group,
                        bastion_cli.create_session_create_port_forwarding_session_target_resource_details,
                        "create-port-forwarding")


@cli_util.copy_params_from_generated_command(bastion_cli.create_bastion,
                                             params_to_exclude=['max_session_ttl_in_seconds', 'static_jump_host_ip_addresses', 'client_cidr_block_allow_list'])
@bastion_cli.bastion_group.command(name='create', help=bastion_cli.create_bastion.help)
@cli_util.option('--max-session-ttl', type=click.INT, help="""Max TTL of the sessions on the bastion in seconds.""")
@cli_util.option('--jump-host-ips', type=custom_types.CLI_COMPLEX_TYPE, help=u"""the ip addresses of the hosts that the bastion has access to.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--client-cidr-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""the ip ranges that the bastion has access to.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'jump-host-ips': {'module': 'bastion', 'class': 'list[string]'}, 'client-cidr-list': {'module': 'bastion', 'class': 'list[string]'}, 'freeform-tags': {'module': 'bastion', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'bastion', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'bastion', 'class': 'Bastion'})
@cli_util.wrap_exceptions
def create_bastion(ctx, **kwargs):
    if 'max_session_ttl' in kwargs:
        kwargs['max_session_ttl_in_seconds'] = kwargs['max_session_ttl']
        kwargs.pop('max_session_ttl')
    if 'client_cidr_list' in kwargs:
        kwargs['client_cidr_block_allow_list'] = kwargs['client_cidr_list']
        kwargs.pop('client_cidr_list')
    if 'jump_host_ips' in kwargs:
        kwargs['static_jump_host_ip_addresses'] = kwargs['jump_host_ips']
        kwargs.pop('jump_host_ips')
    # Invoke base method "create_bastion"
    ctx.invoke(bastion_cli.create_bastion, **kwargs)


@cli_util.copy_params_from_generated_command(bastion_cli.update_bastion,
                                             params_to_exclude=['max_session_ttl_in_seconds', 'static_jump_host_ip_addresses', 'client_cidr_block_allow_list'])
@bastion_cli.bastion_group.command(name='update', help=bastion_cli.update_bastion.help)
@cli_util.option('--max-session-ttl', type=click.INT, help="""Max TTL in seconds of the sessions on the bastion.""")
@cli_util.option('--jump-host-ips', type=custom_types.CLI_COMPLEX_TYPE, help=u"""the ip addresses of the hosts that the bastion has access to.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--client-cidr-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""the ip ranges that the bastion has access to.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'jump-host-ips': {'module': 'bastion', 'class': 'list[string]'}, 'client-cidr-list': {'module': 'bastion', 'class': 'list[string]'}, 'freeform-tags': {'module': 'bastion', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'bastion', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_bastion(ctx, **kwargs):
    if 'max_session_ttl' in kwargs:
        kwargs['max_session_ttl_in_seconds'] = kwargs['max_session_ttl']
        kwargs.pop('max_session_ttl')
    if 'client_cidr_list' in kwargs:
        kwargs['client_cidr_block_allow_list'] = kwargs['client_cidr_list']
        kwargs.pop('client_cidr_list')
    if 'jump_host_ips' in kwargs:
        kwargs['static_jump_host_ip_addresses'] = kwargs['jump_host_ips']
        kwargs.pop('jump_host_ips')
    # Invoke base method "update_bastion"
    ctx.invoke(bastion_cli.update_bastion, **kwargs)


@cli_util.copy_params_from_generated_command(bastion_cli.create_session, params_to_exclude=['key_details'])
@bastion_cli.session_group.command(name='create', help=bastion_cli.create_session.help)
@cli_util.option('--ssh-public-key-file', type=click.File('r'), help="""A file containing ssh public key content for ssh connection.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'target-resource-details': {'module': 'bastion', 'class': 'CreateSessionTargetResourceDetails'}, 'key-details': {'module': 'bastion', 'class': 'PublicKeyDetails'}, 'freeform-tags': {'module': 'bastion', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'bastion', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'bastion', 'class': 'Session'})
@cli_util.wrap_exceptions
def create_session(ctx, **kwargs):
    key_details = {}

    if 'ssh_public_key_file' in kwargs and kwargs['ssh_public_key_file'] is not None:
        key_details['publicKeyContent'] = kwargs['ssh_public_key_file'].read()
        kwargs.pop('ssh_public_key_file')

    if len(key_details) > 0:
        kwargs['key_details'] = json.dumps(key_details)
    # Invoke base method "create_bastion"
    ctx.invoke(bastion_cli.create_session, **kwargs)


@cli_util.copy_params_from_generated_command(
    bastion_cli.create_session_create_managed_ssh_session_target_resource_details,
    params_to_exclude=['key_details',
                       'session_ttl_in_seconds',
                       'target_resource_details_target_resource_id',
                       'target_resource_details_target_resource_operating_system_user_name',
                       'target_resource_details_target_resource_port',
                       'target_resource_details_target_resource_private_ip_address'])
@bastion_cli.session_group.command(name='create-managed-ssh',
                                   help=bastion_cli.create_session_create_managed_ssh_session_target_resource_details.help)
@cli_util.option('--ssh-public-key-file', type=click.File('r'), help="""A file containing ssh public key content for ssh connection.""")
@cli_util.option('--session-ttl', help="""TTL of the session in seconds.""")
@cli_util.option('--target-resource-id', help="""The OCID of the target resource to connect to.""")
@cli_util.option('--target-os-username', help="""Name of the user to use on target resource operating system.""")
@cli_util.option('--target-port', help="""Target resource port to use.""")
@cli_util.option('--target-private-ip', help="""Target resource private ip address.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'bastion', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'bastion', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'bastion', 'class': 'Session'})
@cli_util.wrap_exceptions
def create_managed_ssh(ctx, **kwargs):
    if 'session_ttl' in kwargs:
        kwargs['session_ttl_in_seconds'] = kwargs['session_ttl']
        kwargs.pop('session_ttl')

    if 'target_resource_id' in kwargs:
        kwargs['target_resource_details_target_resource_id'] = kwargs['target_resource_id']
        kwargs.pop('target_resource_id')

    if 'target_os_username' in kwargs:
        kwargs['target_resource_details_target_resource_operating_system_user_name'] = kwargs['target_os_username']
        kwargs.pop('target_os_username')

    if 'target_port' in kwargs:
        kwargs['target_resource_details_target_resource_port'] = kwargs['target_port']
        kwargs.pop('target_port')

    if 'target_private_ip' in kwargs:
        kwargs['target_resource_details_target_resource_private_ip_address'] = kwargs['target_private_ip']
        kwargs.pop('target_private_ip')

    key_details = {}

    if 'ssh_public_key_file' in kwargs and kwargs['ssh_public_key_file'] is not None:
        key_details['publicKeyContent'] = kwargs['ssh_public_key_file'].read()
        kwargs.pop('ssh_public_key_file')

    if len(key_details) > 0:
        kwargs['key_details'] = json.dumps(key_details)

    # Invoke base method
    ctx.invoke(bastion_cli.create_session_create_managed_ssh_session_target_resource_details, **kwargs)


@cli_util.copy_params_from_generated_command(
    bastion_cli.create_session_create_port_forwarding_session_target_resource_details,
    params_to_exclude=['key_details',
                       'session_ttl_in_seconds',
                       'target_resource_details_target_resource_id',
                       'target_resource_details_target_resource_port',
                       'target_resource_details_target_resource_private_ip_address'])
@bastion_cli.session_group.command(name='create-port-forwarding',
                                   help=bastion_cli.create_session_create_port_forwarding_session_target_resource_details.help)
@cli_util.option('--ssh-public-key-file', type=click.File('r'), help="""A file containing ssh public key content for ssh connection.""")
@cli_util.option('--session-ttl', help="""TTL of the session in seconds.""")
@cli_util.option('--target-resource-id', help="""The OCID of the target resource to connect to.""")
@cli_util.option('--target-port', help="""Target resource port to use.""")
@cli_util.option('--target-private-ip', help="""Target resource private ip address.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'bastion', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'bastion', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'bastion', 'class': 'Session'})
@cli_util.wrap_exceptions
def create_port_forwarding(ctx, **kwargs):
    if 'session_ttl' in kwargs:
        kwargs['session_ttl_in_seconds'] = kwargs['session_ttl']
        kwargs.pop('session_ttl')

    if 'target_resource_id' in kwargs:
        kwargs['target_resource_details_target_resource_id'] = kwargs['target_resource_id']
        kwargs.pop('target_resource_id')

    if 'target_port' in kwargs:
        kwargs['target_resource_details_target_resource_port'] = kwargs['target_port']
        kwargs.pop('target_port')

    if 'target_private_ip' in kwargs:
        kwargs['target_resource_details_target_resource_private_ip_address'] = kwargs['target_private_ip']
        kwargs.pop('target_private_ip')

    key_details = {}

    if 'ssh_public_key_file' in kwargs and kwargs['ssh_public_key_file'] is not None:
        key_details['publicKeyContent'] = kwargs['ssh_public_key_file'].read()
        kwargs.pop('ssh_public_key_file')

    if len(key_details) > 0:
        kwargs['key_details'] = json.dumps(key_details)

    # Invoke base method
    ctx.invoke(bastion_cli.create_session_create_port_forwarding_session_target_resource_details, **kwargs)
