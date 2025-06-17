# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.wlms.src.oci_cli_wlms.generated import wlms_service_cli
from services.wlms.src.oci_cli_weblogic_management_service_configuration.generated import weblogicmanagementserviceconfiguration_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Remove weblogic-management-service-configuration from oci wlms
wlms_service_cli.wlms_service_group.commands.pop(weblogicmanagementserviceconfiguration_cli.weblogic_management_service_configuration_root_group.name)


# Move commands under 'oci wlms weblogic-management-service-configuration' -> 'oci wlms'
wlms_service_cli.wlms_service_group.add_command(weblogicmanagementserviceconfiguration_cli.configuration_group)
