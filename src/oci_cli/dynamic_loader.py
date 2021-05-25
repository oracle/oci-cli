# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import sys
from inspect import getsourcefile
from os import listdir, path
from .service_mapping import service_mapping
from .final_command_processor import process

ALL_SERVICES_DIR = "services"

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


def load_service_from_command(command):
    for arg in command:
        if arg in service_mapping:
            load_service(arg)
            break


def load_service(service):
    if service in service_mapping:
        load_modules(path.join(services_dir, service_mapping[service][0]), service_mapping[service][0])
        process()


def load_all_services():
    for service in [dir for dir in listdir(services_dir) if path.isdir(path.join(services_dir, dir))]:
        load_modules(path.join(services_dir, service), service)
    process()


def load_modules(service_dir, service):
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
