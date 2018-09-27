# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .. import cli_util
from ..cli_util import option
from ..generated import email_cli
from .. import json_skeleton_utils
import click


# create sender update compartment_id and email_address to be required
@cli_util.copy_params_from_generated_command(email_cli.create_sender, params_to_exclude=['compartment_id', 'email_address'])
@email_cli.sender_group.command(name='create', help="""Creates a sender for a tenancy in a given compartment.""")
@option('--compartment-id', required=True, help="""The OCID of the compartment that contains the sender.""")
@option('--email-address', required=True, help="""The email address of the sender.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'email', 'class': 'Sender'})
@cli_util.wrap_exceptions
def create_sender(ctx, **kwargs):
    ctx.invoke(email_cli.create_sender, **kwargs)


# create suppression update compartment_id and email_address to be required
@cli_util.copy_params_from_generated_command(email_cli.create_suppression, params_to_exclude=['compartment_id', 'email_address'])
@email_cli.suppression_group.command(name=cli_util.override('create_suppression.command_name', 'create'), help="""Adds recipient email addresses to the suppression list for a tenancy.""")
@option('--compartment-id', required=True, help="""The OCID of the compartment to contain the suppression. Since suppressions are at the customer level, this must be the tenancy OCID.""")
@option('--email-address', required=True, help="""The recipient email address of the suppression.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'email', 'class': 'Suppression'})
@cli_util.wrap_exceptions
def create_suppression(ctx, **kwargs):
    ctx.invoke(email_cli.create_suppression, **kwargs)
