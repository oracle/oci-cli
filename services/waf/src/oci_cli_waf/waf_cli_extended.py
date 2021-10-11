# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.waf.src.oci_cli_waf.generated import waf_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci waf work-request-log-entry list-work-request-logs -> oci waf work-request-log-entry list
cli_util.rename_command(waf_cli, waf_cli.work_request_log_entry_group, waf_cli.list_work_request_logs, "list")


# oci waf work-request-log-entry -> oci waf work-request-log
cli_util.rename_command(waf_cli, waf_cli.waf_root_group, waf_cli.work_request_log_entry_group, "work-request-log")


# oci waf network-address-list create-network-address-list-create-network-address-list-addresses-details -> oci waf network-address-list create-addresses-list
cli_util.rename_command(waf_cli, waf_cli.network_address_list_group, waf_cli.create_network_address_list_create_network_address_list_addresses_details, "create-addresses-list")


# oci waf network-address-list update-network-address-list-update-network-address-list-addresses-details -> oci waf network-address-list update-addresses-list
cli_util.rename_command(waf_cli, waf_cli.network_address_list_group, waf_cli.update_network_address_list_update_network_address_list_addresses_details, "update-addresses-list")


# oci waf network-address-list create-network-address-list-create-network-address-list-vcn-addresses-details -> oci waf network-address-list create-vcn-addresses-list
cli_util.rename_command(waf_cli, waf_cli.network_address_list_group, waf_cli.create_network_address_list_create_network_address_list_vcn_addresses_details, "create-vcn-addresses-list")


# oci waf network-address-list update-network-address-list-update-network-address-list-vcn-addresses-details -> oci waf network-address-list update-vcn-addresses-list
cli_util.rename_command(waf_cli, waf_cli.network_address_list_group, waf_cli.update_network_address_list_update_network_address_list_vcn_addresses_details, "update-vcn-addresses-list")


# oci waf web-app-firewall create-web-app-firewall-create-web-app-firewall-load-balancer-details -> oci waf web-app-firewall create-for-load-balancer
cli_util.rename_command(waf_cli, waf_cli.web_app_firewall_group, waf_cli.create_web_app_firewall_create_web_app_firewall_load_balancer_details, "create-for-load-balancer")


# oci waf web-app-firewall update -> oci waf web-app-firewall update-for-load-balancer
cli_util.rename_command(waf_cli, waf_cli.web_app_firewall_group, waf_cli.update_web_app_firewall, "update-for-load-balancer")


# Remove create from oci waf network-address-list
waf_cli.network_address_list_group.commands.pop(waf_cli.create_network_address_list.name)


# Remove update from oci waf network-address-list
waf_cli.network_address_list_group.commands.pop(waf_cli.update_network_address_list.name)


# Remove create from oci waf web-app-firewall
waf_cli.web_app_firewall_group.commands.pop(waf_cli.create_web_app_firewall.name)
