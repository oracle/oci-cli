# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


"""
NOTE: This class should always comply to the API definition of NfsDatasetClient present in
services/dts/src/oci_cli_dts/physical_appliance_control_plane/client/nfs_dataset_client.py
"""

from oci_cli import cli_util

from services.dts.src.oci_cli_dts.appliance_config_manager import ApplianceConfigManager
from services.dts.src.oci_cli_dts.appliance_constants import APPLIANCE_CONFIGS_BASE_DIR, APPLIANCE_AUTH_USER, \
    APPLIANCE_CERT_FILE_NAME
from services.dts.src.oci_cli_dts.physical_appliance_control_plane.client.nfs_dataset_client import NfsDatasetClient


class NfsDatasetClientProxy:
    def __init__(self, ctx, appliance_profile):
        config_manager = ApplianceConfigManager(APPLIANCE_CONFIGS_BASE_DIR)
        appliance_config = config_manager.get_config(appliance_profile)
        self.auth_value = "{}:{}".format(APPLIANCE_AUTH_USER, appliance_config.get_access_token())
        self.serial_id = appliance_config.get_appliance_serial_id()

        config = cli_util.build_config(ctx.obj)
        host_name = appliance_config.get_appliance_url()
        self_signed_cert = "{}/{}".format(config_manager.get_config_dir(appliance_profile), APPLIANCE_CERT_FILE_NAME)
        self.nfs_dataset_client = NfsDatasetClient(
            config=config, service_endpoint=host_name, self_signed_cert=self_signed_cert)

    def activate_nfs_dataset(self, dataset_name, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.nfs_dataset_client.activate_nfs_dataset(dataset_name, **kwargs)

    def create_nfs_dataset(self, details, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.nfs_dataset_client.create_nfs_dataset(details, **kwargs)

    def deactivate_nfs_dataset(self, dataset_name, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.nfs_dataset_client.deactivate_nfs_dataset(dataset_name, **kwargs)

    def delete_nfs_dataset(self, dataset_name, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.nfs_dataset_client.delete_nfs_dataset(dataset_name, **kwargs)

    def get_nfs_dataset(self, dataset_name, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.nfs_dataset_client.get_nfs_dataset(dataset_name, **kwargs)

    def get_nfs_dataset_seal_manifest(self, dataset_name, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.nfs_dataset_client.get_nfs_dataset_seal_manifest(dataset_name, **kwargs)

    def get_nfs_dataset_seal_status(self, dataset_name, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.nfs_dataset_client.get_nfs_dataset_seal_status(dataset_name, **kwargs)

    def initiate_seal_on_nfs_dataset(self, dataset_name, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.nfs_dataset_client.initiate_seal_on_nfs_dataset(dataset_name, **kwargs)

    def list_nfs_datasets(self, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.nfs_dataset_client.list_nfs_datasets(**kwargs)

    def reopen_nfs_dataset(self, dataset_name, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.nfs_dataset_client.reopen_nfs_dataset(dataset_name, **kwargs)

    def update_nfs_dataset(self, dataset_name, body, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.nfs_dataset_client.update_nfs_dataset(dataset_name, body, **kwargs)
