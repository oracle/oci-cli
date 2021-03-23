# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.tenant_manager_control_plane.src.oci_cli_domain.generated import domain_cli

domain_cli.domain_root_group.commands.pop(domain_cli.domain_group.name)
domain_cli.domain_root_group.add_command(domain_cli.get_domain)
domain_cli.domain_root_group.add_command(domain_cli.create_domain)
domain_cli.domain_root_group.add_command(domain_cli.update_domain)
domain_cli.domain_root_group.add_command(domain_cli.list_domains)
domain_cli.domain_root_group.add_command(domain_cli.delete_domain)
