# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


import click

from services.dts.src.oci_cli_dts.appliance_constants import APPLIANCE_CERT_FILE_NAME


class ApplianceAuthManager:
    def __init__(self, appliance_config_spec, expected_cert_fingerprint, config_manager, cert_manager):
        """
        This class is responsible for getting the certificates from an appliance and validating them
        :param appliance_config_spec: The ApplianceConfigSpec object containing the appliance's details
        :param expected_cert_fingerprint: The certificate's fingerprint that is passed in by the user. This is used
        later to be able to compare against the fingerprint of the certificate that was received
        :param config_manager: The ApplianceConfigManager object that handles the directory structure of the appliance
        configs
        :param cert_manager: The ApplianceCertManager object that actually implements the individual operations related
        to the fetching and storing of certificates
        """
        self.appliance_config_spec = appliance_config_spec
        self.expected_cert_fingerprint = expected_cert_fingerprint
        self.config_manager = config_manager
        self.cert_manager = cert_manager

    def initialize_auth(self):
        """
        The wrapper for the initialization of auth for the appliance on the host. This essentially makes calls to the
        cert manager
        :return: None
        """
        try:
            self.config_manager.create_config(self.appliance_config_spec)
        except Exception as e:
            click.echo("Error while creating the config at {}. Attempting to delete the config..."
                       .format(self.appliance_config_spec.get_profile()))
            self.config_manager.delete_config(self.appliance_config_spec.get_profile())
            raise e

        cert_file = "{}/{}".format(self.config_manager.get_config_dir(self.appliance_config_spec.get_profile()),
                                   APPLIANCE_CERT_FILE_NAME)

        try:
            self.cert_manager.fetch_cert(cert_file)
        except Exception as e:
            click.echo("Error while fetching the certificate from the appliance. Attempting to delete the config...")
            click.echo(e)
            self.config_manager.delete_config(self.appliance_config_spec.get_profile())
            raise e

        try:
            self.cert_manager.validate_cert(cert_file, self.expected_cert_fingerprint)
        except Exception as e:
            click.echo(e)
            click.echo("Error while validating cert fingerprint. Attempting to delete the config...")
            self.config_manager.delete_config(self.appliance_config_spec.get_profile())
            raise e
