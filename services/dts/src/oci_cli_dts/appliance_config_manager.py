# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
import configparser
from oci import exceptions
import os
import shutil
import stat
from services.dts.src.oci_cli_dts.appliance_constants import APPLIANCE_ACCESS_TOKEN_KEY, APPLIANCE_CONFIG_FILE_NAME, APPLIANCE_ENDPOINT_KEY, \
    APPLIANCE_SERIAL_ID_KEY, DEFAULT_PROFILE

from services.dts.src.oci_cli_dts.appliance_config import ApplianceConfig


class ApplianceConfigManager:
    def __init__(self, appliance_configs_base_dir):
        self.appliance_configs_base_dir = appliance_configs_base_dir

    def get_base_dir(self):
        """
        Returns the base directory as a String
        :return: The base directory that was configured for this object
        """
        return self.appliance_configs_base_dir

    def get_config_dir(self, appliance_profile):
        """
        Returns the path of the appliance config directory if present
        :param appliance_profile: The appliance profile name
        :return: The full path to the appliance profile's directory
        """
        return '%s/%s' % (self.appliance_configs_base_dir, appliance_profile)

    def get_config_file(self, appliance_profile):
        """
        Returns the appliance profile path
        :param appliance_profile: The appliance profile name
        :return: The full path to the appliance profile's config file
        """
        return '%s/%s' % (self.get_config_dir(appliance_profile), APPLIANCE_CONFIG_FILE_NAME)

    def create_config_dir(self, appliance_profile):
        """
        Creates the config directory for the appliance profile. The config directory resides under the
        applaince_configs_base_dir and is named appliance_profile
        :param appliance_profile: The appliance profile name
        :return: None
        """
        appliance_config_dir = self.get_config_dir(appliance_profile)
        if not os.path.exists(appliance_config_dir):
            os.makedirs(appliance_config_dir)

    def create_config(self, appliance_config_spec):
        """
        Creates the config folder for the appliance and adds details tot he config
        :param appliance_config_spec: The ApplianceConfigSpec object
        :return: None
        """
        appliance_endpoint = appliance_config_spec.get_endpoint()
        if appliance_endpoint[1] == 443:
            appliance_url = 'https://%s' % appliance_endpoint[0]
        else:
            appliance_url = 'https://%s:%d' % (appliance_endpoint[0], appliance_endpoint[1])

        self.create_config_dir(appliance_config_spec.get_profile())
        config_file = open(self.get_config_file(appliance_config_spec.get_profile()), "w")
        config = configparser.ConfigParser(default_section=DEFAULT_PROFILE)
        config.set(DEFAULT_PROFILE, APPLIANCE_ENDPOINT_KEY, appliance_url)
        config.set(DEFAULT_PROFILE, APPLIANCE_ACCESS_TOKEN_KEY, appliance_config_spec.get_access_token())
        config.set(DEFAULT_PROFILE, APPLIANCE_SERIAL_ID_KEY, appliance_config_spec.get_serial_id())
        config.write(config_file)
        config_file.close()
        # Set read and write permissions only for the owner
        os.chmod(self.get_config_file(appliance_config_spec.get_profile()), stat.S_IRUSR | stat.S_IWUSR)

    def is_config_present(self, appliance_profile):
        """
        Verifies if the appliance_profile exists
        :param appliance_profile: The appliance profile name
        :return: True if the profile exists, False otherwise
        """
        return os.path.exists(self.get_config_file(appliance_profile))

    def validate_config_present(self, appliance_profile):
        """
        Raises an exception if the config is not present
        :param appliance_profile: The appliance profile name
        :return: None
        """
        if not self.is_config_present(appliance_profile):
            if DEFAULT_PROFILE == appliance_profile:
                raise exceptions.InvalidConfig('Cannot find appliance config. Appliance not initialized')
            else:
                raise exceptions.InvalidConfig(
                    'Cannot find appliance config for profile %s since it was not initialized' % appliance_profile)

    def get_config(self, appliance_profile):
        """
        Creates an ApplianceConfig object out of the config file
        :param appliance_profile: The appliance profile name
        :return: The ApplianceConfig object
        """
        self.validate_config_present(appliance_profile)
        appliance_config_file = self.get_config_file(appliance_profile)
        try:
            config = configparser.ConfigParser()
            config.read(appliance_config_file)
            appliance_url = config.get(DEFAULT_PROFILE, APPLIANCE_ENDPOINT_KEY)
            access_token = config.get(DEFAULT_PROFILE, APPLIANCE_ACCESS_TOKEN_KEY)
            serial_id = config.get(DEFAULT_PROFILE, APPLIANCE_SERIAL_ID_KEY)
            return ApplianceConfig(appliance_url, access_token, serial_id)
        except IOError as e:
            click.FileError('Unable to parse the appliance config file %s: %s' % (appliance_config_file, e))

    def list_configs(self):
        """
        Returns all the appliances that have been configured on the host
        :return: A dictionary having the key as the appliance_profile and the value as the ApplianceConfig object
        """
        config_profile_dict = {}
        # Loop through all the children of the base folder. Only directories will be profiles
        for child in os.listdir(self.appliance_configs_base_dir):
            if os.path.isdir('{}/{}'.format(self.appliance_configs_base_dir, child)):
                appliance_profile = child.split('/')[-1]
                if self.is_config_present(appliance_profile):
                    config_profile_dict[appliance_profile] = self.get_config(appliance_profile)
        return config_profile_dict

    def delete_config(self, appliance_profile):
        """
        Deletes the appliance profile
        :param appliance_profile: The appliance profile name
        :return: None
        """
        if not self.is_config_present(appliance_profile):
            raise exceptions.InvalidConfig('The profile {} does not exist'.format(appliance_profile))
        try:
            shutil.rmtree(self.get_config_dir(appliance_profile))
        except IOError as e:
            click.FileError('Failed to delete appliance config for profile {}. '
                            'Make sure the permissions are set correctly for this path...'
                            .format(appliance_profile))
            raise e
