# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.tenant_manager_control_plane.src.oci_cli_domain_governance.generated import domaingovernance_cli

domaingovernance_cli.domain_governance_root_group.commands.pop(domaingovernance_cli.domain_governance_group.name)
domaingovernance_cli.domain_governance_root_group.add_command(domaingovernance_cli.get_domain_governance)
domaingovernance_cli.domain_governance_root_group.add_command(domaingovernance_cli.create_domain_governance)
domaingovernance_cli.domain_governance_root_group.add_command(domaingovernance_cli.update_domain_governance)
domaingovernance_cli.domain_governance_root_group.add_command(domaingovernance_cli.list_domain_governances)
domaingovernance_cli.domain_governance_root_group.add_command(domaingovernance_cli.delete_domain_governance)
