# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


"""
NOTE: This class should always comply to the API definition of PhysicalTransferApplianceClient present in
services/dts/src/oci_cli_dts/physical_appliance_control_plane/client/physical_transfer_appliance_client.py
"""

from oci_cli import cli_util

from services.dts.src.oci_cli_dts.appliance_config_manager import ApplianceConfigManager
from services.dts.src.oci_cli_dts.appliance_constants import APPLIANCE_CONFIGS_BASE_DIR, APPLIANCE_AUTH_USER, \
    APPLIANCE_CERT_FILE_NAME
from services.dts.src.oci_cli_dts.physical_appliance_control_plane.client.physical_transfer_appliance_client import \
    PhysicalTransferApplianceClient


class ApplianceClientProxy:
    def __init__(self, ctx, appliance_profile):
        config_manager = ApplianceConfigManager(APPLIANCE_CONFIGS_BASE_DIR)
        appliance_config = config_manager.get_config(appliance_profile)
        self.auth_value = "{}:{}".format(APPLIANCE_AUTH_USER, appliance_config.get_access_token())
        self.serial_id = appliance_config.get_appliance_serial_id()

        config = cli_util.build_config(ctx.obj)
        host_name = appliance_config.get_appliance_url()
        self_signed_cert = "{}/{}".format(config_manager.get_config_dir(appliance_profile), APPLIANCE_CERT_FILE_NAME)
        self.appliance_client = PhysicalTransferApplianceClient(config=config,
                                                                service_endpoint=host_name,
                                                                self_signed_cert=self_signed_cert)

    def configure_encryption(self, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.appliance_client.configure_encryption(**kwargs)

    def finalize_appliance(self, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.appliance_client.finalize_appliance(**kwargs)

    def get_physical_transfer_appliance(self, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.appliance_client.get_physical_transfer_appliance(**kwargs)

    def set_object_storage_upload_config(self, upload_config, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.appliance_client.set_object_storage_upload_config(upload_config, **kwargs)

    def unlock_appliance(self, **kwargs):
        kwargs['auth_value'] = self.auth_value
        kwargs['serial_id'] = self.serial_id
        return self.appliance_client.unlock_appliance(**kwargs)
