# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.tenant_manager_control_plane.src.oci_cli_link.generated import link_cli

link_cli.link_root_group.commands.pop(link_cli.link_group.name)
link_cli.link_root_group.add_command(link_cli.get_link)
link_cli.link_root_group.add_command(link_cli.list_links)
link_cli.link_root_group.add_command(link_cli.delete_link)
