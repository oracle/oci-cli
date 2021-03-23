# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.network_load_balancer.src.oci_cli_network_load_balancer.generated import networkloadbalancer_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci nlb backend-summary list-backends -> oci nlb backend-summary list
cli_util.rename_command(networkloadbalancer_cli, networkloadbalancer_cli.backend_summary_group, networkloadbalancer_cli.list_backends, "list")


# oci nlb backend-set-summary list-backend-sets -> oci nlb backend-set-summary list
cli_util.rename_command(networkloadbalancer_cli, networkloadbalancer_cli.backend_set_summary_group, networkloadbalancer_cli.list_backend_sets, "list")


# oci nlb listener-summary list-listeners -> oci nlb listener-summary list
cli_util.rename_command(networkloadbalancer_cli, networkloadbalancer_cli.listener_summary_group, networkloadbalancer_cli.list_listeners, "list")


# oci nlb listener-protocols list-network-load-balancers-protocols -> oci nlb listener-protocols list
cli_util.rename_command(networkloadbalancer_cli, networkloadbalancer_cli.listener_protocols_group, networkloadbalancer_cli.list_network_load_balancers_protocols, "list")


# oci nlb network-load-balancing-policy list-network-load-balancers-policies -> oci nlb network-load-balancing-policy list
cli_util.rename_command(networkloadbalancer_cli, networkloadbalancer_cli.network_load_balancing_policy_group, networkloadbalancer_cli.list_network_load_balancers_policies, "list")


# oci nlb work-request-log-entry list-work-request-logs -> oci nlb work-request-log-entry list
cli_util.rename_command(networkloadbalancer_cli, networkloadbalancer_cli.work_request_log_entry_group, networkloadbalancer_cli.list_work_request_logs, "list")


# Move commands under 'oci nlb backend-summary' -> 'oci nlb backend'
networkloadbalancer_cli.nlb_root_group.commands.pop(networkloadbalancer_cli.backend_summary_group.name)
networkloadbalancer_cli.backend_group.add_command(networkloadbalancer_cli.list_backends)


# Move commands under 'oci nlb backend-set-summary' -> 'oci nlb backend-set'
networkloadbalancer_cli.nlb_root_group.commands.pop(networkloadbalancer_cli.backend_set_summary_group.name)
networkloadbalancer_cli.backend_set_group.add_command(networkloadbalancer_cli.list_backend_sets)


# Move commands under 'oci nlb listener-summary' -> 'oci nlb listener'
networkloadbalancer_cli.nlb_root_group.commands.pop(networkloadbalancer_cli.listener_summary_group.name)
networkloadbalancer_cli.listener_group.add_command(networkloadbalancer_cli.list_listeners)
