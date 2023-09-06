# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.cims.src.oci_cli_incident.generated import incident_cli

# Remove the cli command:  oci support status
incident_cli.support_root_group.commands.pop(incident_cli.status_group.name)
# Remove the cli command:  oci support string
incident_cli.support_root_group.commands.pop(incident_cli.string_group.name)
# Remove the cli command:  oci support update-incident
incident_cli.support_root_group.commands.pop(incident_cli.update_incident_group.name)
