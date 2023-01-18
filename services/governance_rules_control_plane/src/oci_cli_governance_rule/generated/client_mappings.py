# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.governance_rules_control_plane import GovernanceRuleClient

MODULE_TO_TYPE_MAPPINGS["governance_rules_control_plane"] = oci.governance_rules_control_plane.models.governance_rules_control_plane_type_mapping
if CLIENT_MAP.get("governance_rules_control_plane") is None:
    CLIENT_MAP["governance_rules_control_plane"] = {}
CLIENT_MAP["governance_rules_control_plane"]["governance_rule"] = GovernanceRuleClient
