# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates. All rights reserved.

import click
import json  # noqa: F401
import oci  # noqa: F401
from services.golden_gate.src.oci_cli_golden_gate.generated import goldengate_cli

from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import custom_types  # noqa: F401
from oci_cli import cli_exceptions  # noqa: F401
from oci_cli import json_skeleton_utils

# Fixup deployment start to use default start
cli_util.rename_command(goldengate_cli,
                        goldengate_cli.deployment_group,
                        goldengate_cli.start_deployment_default_start_deployment_details,
                        goldengate_cli.start_deployment.name)

# Fixup deployment stop to use default stop
cli_util.rename_command(goldengate_cli,
                        goldengate_cli.deployment_group,
                        goldengate_cli.stop_deployment_default_stop_deployment_details,
                        goldengate_cli.stop_deployment.name)

# Fixup deployment upgrade to use current release upgrade
cli_util.rename_command(goldengate_cli,
                        goldengate_cli.deployment_group,
                        goldengate_cli.upgrade_deployment_upgrade_deployment_current_release_details,
                        goldengate_cli.upgrade_deployment.name)

# Fixup deployment-backup restore to use default restore
cli_util.rename_command(goldengate_cli,
                        goldengate_cli.deployment_backup_group,
                        goldengate_cli.restore_deployment_default_restore_deployment_details,
                        goldengate_cli.restore_deployment.name)

# Fixup list-work-request-logs to use list
cli_util.rename_command(goldengate_cli,
                        goldengate_cli.work_request_log_entry_group,
                        goldengate_cli.list_work_request_logs,
                        'list')

# from oci goldengate deployment create <blah> -ogg-data <json>
# to   oci goldengate deployment create <blah>
#                 --deployment-name <text>
#                 --admin-username <text>
#                 [--admin-password <text>]
#                 --certificate-file <file>
#                 --private-key-file <file>


@cli_util.copy_params_from_generated_command(goldengate_cli.create_deployment,
                                             params_to_exclude=['deployment_type', 'ogg_data'],
                                             copy_from_json=False)
@goldengate_cli.deployment_group.command(name='create', help=goldengate_cli.create_deployment.help)
@cli_util.option('--deployment-name', help=u"""The name given to the GoldenGate service deployment.
The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter.""")
@cli_util.option('--admin-username', help=u"""The GoldenGate deployment console username.""")
@cli_util.option('--admin-password', help=u"""The password associated with the GoldenGate deployment console username.
The password must be 8 to 30 characters long and must contain at least 1 uppercase, 1 lowercase, 1 numeric,
and 1 special character. Special characters such as ‘$’, ‘^’, or ‘?’ are not allowed.""")
@cli_util.option('--certificate-file', type=click.File('r'), help=u"""The SSL certificate for this deployment in PEM format.""")
@cli_util.option('--private-key-file', type=click.File('r'), help=u"""The private key for your certificate in PEM format.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}}, output_type={'module': 'golden_gate', 'class': 'Deployment'})
@cli_util.wrap_exceptions
def create_deployment_extended(ctx, **kwargs):
    if kwargs.get('deployment_type') is None:
        kwargs['deployment_type'] = "OGG"

    if kwargs.get('ogg_data') is None:
        _ogg_details = {}
        _missing_params = []
        if kwargs.get('deployment_name') is None:
            _missing_params.append("deployment-name")
        else:
            _ogg_details['deploymentName'] = kwargs.get('deployment_name')
        del kwargs['deployment_name']

        if kwargs.get('admin_username') is None:
            _missing_params.append("admin-username")
        else:
            _ogg_details['adminUsername'] = kwargs.get('admin_username')
        del kwargs['admin_username']

        if len(_missing_params) != 0:
            raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Missing option(s) --{}.'
                                                                           .format(', --'.join(_missing_params)))

        if kwargs.get('admin_password') is None:
            _ogg_details['adminPassword'] = click.prompt(text='Enter admin password', default='',
                                                         hide_input=True, show_default=False, confirmation_prompt=True)
            if not _ogg_details['adminPassword']:
                raise click.UsageError('Password cannot be whitespace or empty string')
        else:
            _ogg_details['adminPassword'] = kwargs.get('admin_password')
        del kwargs['admin_password']

        if kwargs.get('certificate_file') is not None:
            _ogg_details['certificate'] = kwargs.get('certificate_file').read()
        del kwargs['certificate_file']

        if kwargs.get('private_key_file') is not None:
            _ogg_details['key'] = kwargs.get('private_key_file').read()
        del kwargs['private_key_file']

        kwargs['ogg_data'] = json.dumps(_ogg_details)

    ctx.invoke(goldengate_cli.create_deployment, **kwargs)


# from oci goldengate deployment update <blah> -ogg-data <json>
# to   oci goldengate deployment update <blah>
#                 --admin-username <text>
#                 [--admin-password <text>]
#                 --certificate-file <file>
#                 --private-key-file <file>

@cli_util.copy_params_from_generated_command(goldengate_cli.update_deployment,
                                             params_to_exclude=['ogg_data'],
                                             copy_from_json=False)
@goldengate_cli.deployment_group.command(name='update', help=goldengate_cli.update_deployment.help)
@cli_util.option('--admin-username', help=u"""The GoldenGate deployment console username.""")
@cli_util.option('--admin-password', help=u"""The password associated with the GoldenGate deployment console username.
The password must be 8 to 30 characters long and must contain at least 1 uppercase, 1 lowercase, 1 numeric,
and 1 special character. Special characters such as ‘$’, ‘^’, or ‘?’ are not allowed.""")
@cli_util.option('--certificate-file', type=click.File('r'), help=u"""The SSL certificate for this deployment in PEM format.""")
@cli_util.option('--private-key-file', type=click.File('r'), help=u"""The private key for your certificate in PEM format.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'golden_gate', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'golden_gate', 'class': 'dict(str, dict(str, object))'}, 'nsg-ids': {'module': 'golden_gate', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_deployment_extended(ctx, **kwargs):
    if kwargs.get('ogg_data') is None:
        _ogg_details = {}

        if kwargs.get('admin_username') is not None:
            _ogg_details['adminUsername'] = kwargs.get('admin_username')
            if kwargs.get('admin_password') is None:
                _ogg_details['adminPassword'] = click.prompt(text='Enter admin password', default='',
                                                             hide_input=True, show_default=False,
                                                             confirmation_prompt=True)
                if not _ogg_details['adminPassword']:
                    raise click.UsageError('Password cannot be whitespace or empty string')
            else:
                _ogg_details['adminPassword'] = kwargs.get('admin_password')
            del kwargs['admin_password']
        del kwargs['admin_username']

        if 'admin_password' in kwargs:
            if kwargs.get('admin_password') is not None:
                raise cli_exceptions.RequiredValueNotInDefaultOrUserInputError('Missing option(s) --admin-username.')
            del kwargs['admin_password']

        if kwargs.get('certificate_file') is not None:
            _ogg_details['certificate'] = kwargs.get('certificate_file').read()
        del kwargs['certificate_file']

        if kwargs.get('private_key_file') is not None:
            _ogg_details['key'] = kwargs.get('private_key_file').read()
        del kwargs['private_key_file']

        kwargs['ogg_data'] = json.dumps(_ogg_details)

    ctx.invoke(goldengate_cli.update_deployment, **kwargs)
