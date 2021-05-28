# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import sys
from inspect import getsourcefile
from os import listdir, path, environ
from .service_mapping import service_mapping

ALL_SERVICES_DIR = "services"
NON_SERVICE_TOP_LEVEL_COMMANDS = ["raw-request", "session", "setup"]

# Add platformization directories to the python system path (PYTHONPATH)
# This has to be done prior to importing cli_root.
this_file_path = path.abspath(getsourcefile(lambda: 0))
if "site-packages" in this_file_path or "dist-packages" in this_file_path:
    # If the installation directory starts with oci_cli, we need to find the
    # last occurrence of oci_cli in the path.
    python_cli_root_dir = this_file_path[0:this_file_path.rindex("oci_cli")]
else:
    python_cli_root_dir = this_file_path[0:this_file_path.index("/src/oci_cli")]
sys.path.append(python_cli_root_dir + 'src')
sys.path.append(python_cli_root_dir)
services_dir = path.join(python_cli_root_dir, ALL_SERVICES_DIR)


def load_required_services_for_invocation():
    """
    Loads services required for the currently executing command.

    This includes loading the necessary services for an autocomplete
    invocation.
    """
    if "COMP_WORDS" in environ:
        cli_autocomplete()
    else:
        load_service_from_command(sys.argv)


def cli_autocomplete():
    words = environ["COMP_WORDS"].split()
    if len(words) == 1:
        # if we're completing "oci" we can short circuit click autocomplete
        # and provide the top level command options in our code
        complete_top_level_commands()
        sys.exit(1)
    elif len(words) == 2:
        # if we're completing a root parameter (e.g. "oci --" -> "oci --help")
        # we don't need to load any services
        # if we're completing a service (e.g. "oci com") use the prefix to load
        # all potentially matching services
        if not words[1].startswith("-"):
            for service in service_mapping:
                if service.startswith(words[1]):
                    load_service(service)
    elif len(words) > 2:
        # we have at least "oci {service}" so we can load the specific service
        load_service_from_command(words)


def complete_top_level_commands():
    all_top_level_commands = sorted(NON_SERVICE_TOP_LEVEL_COMMANDS + list(service_mapping.keys()))
    for command in all_top_level_commands:
        print(command)


def load_service_from_command(command):
    for arg in command:
        if arg in service_mapping:
            load_service(arg)
            break


def load_service(service):
    if service in service_mapping:
        load_service_modules(path.join(services_dir, service_mapping[service][0]), service_mapping[service][0])


def load_service_dir(service):
    load_service_modules(path.join(services_dir, service), service)


def load_all_services():
    for service in [dir for dir in listdir(services_dir) if path.isdir(path.join(services_dir, dir))]:
        load_service_modules(path.join(services_dir, service), service)


def load_service_modules(service_dir, service):
    modules = path.join(service_dir, 'src')
    if path.isdir(modules):
        for mod in [dir for dir in sorted(listdir(modules)) if 'oci_cli' in dir]:
            load_generated(path.join(modules, mod), service, mod)
            load_extended(path.join(modules, mod), service, mod)


# Only loads in the generated service files
def load_generated(mod_dir, service, mod):
    generated_dir = path.join(mod_dir, "generated")
    if path.isdir(generated_dir):
        for file in sorted(listdir(generated_dir)):
            if "__" not in file and file.endswith('.py'):
                load_module(".{service}.src.{mod}.generated.{generated_mod}".format(service=service, mod=mod, generated_mod=file[:-3]))


# Only loads in any extended/manual changes
def load_extended(mod_dir, service, mod):
    for file in sorted(listdir(mod_dir)):
        if path.isfile(path.join(mod_dir, file)) and "extended" in file and file.endswith('.py'):
            load_module(".{service}.src.{mod}.{extended_mod}".format(service=service, mod=mod, extended_mod=file[:-3]))


def load_module(mod_path):
    __import__(ALL_SERVICES_DIR + mod_path)
