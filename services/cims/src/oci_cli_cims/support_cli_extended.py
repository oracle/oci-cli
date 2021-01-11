# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.cims.src.oci_cli_cims.generated import support_service_cli
from services.cims.src.oci_cli_incident.generated import incident_cli
from services.cims.src.oci_cli_user.generated import user_cli


# Remove duplicate incident resource `oci support incident incident`
support_service_cli.support_service_group.commands.pop(incident_cli.incident_root_group.name)
support_service_cli.support_service_group.add_command(incident_cli.incident_resource_type_group)
support_service_cli.support_service_group.add_command(incident_cli.validation_response_group)
support_service_cli.support_service_group.add_command(incident_cli.incident_group)

# Remove duplicate user resource `oci support user user`
support_service_cli.support_service_group.commands.pop(user_cli.user_root_group.name)
support_service_cli.support_service_group.add_command(user_cli.user_group)

# Remove `oci support user`
support_service_cli.support_service_group.commands.pop(user_cli.user_group.name)
