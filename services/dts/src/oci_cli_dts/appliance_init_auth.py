# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


import sys

import click
import os
from services.dts.src.oci_cli_dts.appliance_cert_manager import ApplianceCertManager
from services.dts.src.oci_cli_dts.appliance_config_manager import ApplianceConfigManager
from services.dts.src.oci_cli_dts.appliance_config_spec import ApplianceConfigSpec
from services.dts.src.oci_cli_dts.appliance_constants import APPLIANCE_CONFIGS_BASE_DIR, DEFAULT_PROFILE

from services.dts.src.oci_cli_dts.appliance_auth_manager import ApplianceAuthManager


class InitAuth:
    def __init__(self, auth_spec):
        self.auth_spec = auth_spec

    def run(self):
        access_token = self.auth_spec.get_access_token()
        if access_token is None:
            access_token = self.get_access_token()

        config_manager = ApplianceConfigManager(APPLIANCE_CONFIGS_BASE_DIR)
        profile = self.auth_spec.get_appliance_profile()
        if config_manager.is_config_present(profile):
            prompt = 'Found an existing appliance'
            if profile != DEFAULT_PROFILE:
                prompt += ' for profile %s' % profile
            prompt += '. Is it OK to overwrite it?'
            if not click.confirm(prompt):
                click.echo('Exiting...')
                sys.exit(-1)

        appliance_ip = self.auth_spec.get_appliance_ip()
        appliance_port = self.auth_spec.get_appliance_port()
        cert_fingerprint = self.auth_spec.get_cert_fingerprint()
        serial_id = self.auth_spec.get_serial_id()

        cert_manager = ApplianceCertManager((appliance_ip, appliance_port))

        appliance_config_spec = ApplianceConfigSpec(profile=profile,
                                                    endpoint=(appliance_ip, appliance_port),
                                                    access_token=access_token,
                                                    serial_id=serial_id)

        auth_manager = ApplianceAuthManager(appliance_config_spec, cert_fingerprint, config_manager, cert_manager)

        click.echo('Registering and initializing the authentication between the CLI and the appliance')
        auth_manager.initialize_auth()

    @staticmethod
    def get_access_token():
        access_token = click.prompt('Access token', hide_input=True)
        if access_token is None:
            click.echo('No input provided. Exiting...')
            sys.exit(-1)
        return access_token

    @staticmethod
    def validate_and_get_path(env_var):
        env_var_path = os.environ.get(env_var)
        # Check if environment variable was set
        if env_var_path is None:
            raise click.UsageError('Environment variable %s has not been set. Set this and run the command' % env_var)

        # Check if path exists
        if not os.path.exists(env_var_path):
            raise click.UsageError('File %s corresponding to environment variable %s does not exist'
                                   % (env_var_path, env_var))

        # Check if the command is executable
        if not os.access(env_var_path, os.X_OK):
            raise click.UsageError('File %s corresponding to environment variable %s is not executable'
                                   % (env_var_path, env_var))

        return env_var_path
