# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from services.tenant_manager_control_plane.src.oci_cli_link.generated import link_cli

link_cli.link_root_group.commands.pop(link_cli.link_group.name)
link_cli.link_root_group.add_command(link_cli.get_link)
link_cli.link_root_group.add_command(link_cli.list_links)
link_cli.link_root_group.add_command(link_cli.delete_link)
