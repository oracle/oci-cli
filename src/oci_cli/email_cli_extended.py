# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from . import cli_util
from .generated import email_cli

# create sender update compartment_id and email_address to be required
cli_util.update_param_help(email_cli.create_sender, 'compartment_id', ' [required]', append=True)
cli_util.get_param(email_cli.create_sender, 'compartment_id').callback = cli_util.handle_required_param

cli_util.update_param_help(email_cli.create_sender, 'email_address', ' [required]', append=True)
cli_util.get_param(email_cli.create_sender, 'email_address').callback = cli_util.handle_required_param

# create suppression update compartment_id and email_address to be required
cli_util.update_param_help(email_cli.create_suppression, 'compartment_id', ' [required]', append=True)
cli_util.get_param(email_cli.create_suppression, 'compartment_id').callback = cli_util.handle_required_param

cli_util.update_param_help(email_cli.create_suppression, 'email_address', ' [required]', append=True)
cli_util.get_param(email_cli.create_suppression, 'email_address').callback = cli_util.handle_required_param
