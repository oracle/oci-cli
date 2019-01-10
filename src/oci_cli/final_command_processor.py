# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
from . import cli_root, cli_util
import six


# Map parameter variable names to shortcuts.
PARAMETER_SHORTCUT = {
    'compartment_id': '-c'
}


def add_shortcuts():
    commands = cli_util.collect_commands(cli_root.cli)
    for command in commands:
        for param in command.params:
            shortcut = PARAMETER_SHORTCUT.get(param.name)

            # "shortcut not in param.opts" is For where we use the cli_util.copy_params_from_generated_command
            # and the source command already contains the parameter shortcut, we don't want to shove it in again.
            #
            # This is used in scenarios like:
            #
            # The `import_image_from_object` command is annotated with `@cli_util.copy_params_from_generated_command`.
            # The command we copy from has --compartment-id as one of the options
            #
            # When we fall into this code for the `import_image_from_object` command, the command we copy from has
            # already had a shortcut applied to the --compartment-id option. If we do not check for the shortcut's
            # presence we would append the shortcut again so the help looks like:
            #
            #     -c, -c, -c, --compartment-id TEXT
            #
            # Instead of:
            #     -c, --compartment-id TEXT
            if shortcut and shortcut not in param.opts:
                param.opts.append(shortcut)


def remove_namespace_required_objectstorage():
    # Since almost all object storage commands require the namespace parameter and it can be obtained via an SDK
    # API call, this function goes through all the object storage commands and makes the namespace parameter as
    # Optional. It also updates the help text for the parameter
    if not cli_root.cli.commands.get('os', None):
        return
    commands = cli_util.collect_commands(cli_root.cli.commands.get('os'))
    for command in commands:
        for param in command.params:
            if param.name in ['namespace_name', 'namespace', 'ns']:
                param.required = False
                if param.help.endswith(' [required]'):
                    # Remove ' [required]'
                    param.help = ' '.join(param.help.split(' ')[:-1])
                    # Add help text
                    param.help = param.help + " If not provided, this parameter will be obtained " \
                                              "internally using a call to 'oci os ns get'"


# Many iam commands accept the compartment-id or tenany-id as a parameter.
# In most cases, except policy, we can use the tenancy from the config file as a default for the tenancy-id or
# root compartment-id.
def set_iam_default_tenancy_help():
    iam_tenancy_defaults = cli_util.get_iam_commands_that_use_tenancy_defaults()

    iam_command = cli_root.cli.commands.get('iam')
    for _, entitycommand in six.iteritems(iam_command.commands):
        if entitycommand.name in iam_tenancy_defaults.keys():
            for _, subcommand in six.iteritems(entitycommand.commands):
                for param in subcommand.params:
                    if subcommand.name in iam_tenancy_defaults[entitycommand.name]:
                        if param.name == 'compartment_id' or param.name == 'tenancy_id':
                            if param.help.endswith(' [required]'):
                                # Remove ' [required]'
                                param.help = ' '.join(param.help.split(' ')[:-1])
                                # Add help text
                                param.help = param.help + \
                                    " If not provided, this parameter will use the " + \
                                    "tenancy from the config file."


add_shortcuts()
remove_namespace_required_objectstorage()
set_iam_default_tenancy_help()
