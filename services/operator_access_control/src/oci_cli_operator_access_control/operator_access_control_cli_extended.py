# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from services.operator_access_control.src.oci_cli_operator_access_control.generated import opctl_service_cli
from services.operator_access_control.src.oci_cli_access_requests.generated import accessrequests_cli
from services.operator_access_control.src.oci_cli_operator_control.generated import operatorcontrol_cli
from services.operator_access_control.src.oci_cli_operator_actions.generated import operatoractions_cli
from services.operator_access_control.src.oci_cli_operator_control_assignment.generated import operatorcontrolassignment_cli

# Changing from the following:
# oci operator-access-control access-requests access-request ...
# To
# oci opctl access-request ...
opctl_service_cli.opctl_service_group.commands.pop(accessrequests_cli.access_requests_root_group.name)
opctl_service_cli.opctl_service_group.add_command(accessrequests_cli.access_request_group)

# Changing from the following:
# oci operator-access-control operator-control operator-control ...
# To
# oci opctl operator-control ...
opctl_service_cli.opctl_service_group.commands.pop(operatorcontrol_cli.operator_control_root_group.name)
opctl_service_cli.opctl_service_group.add_command(operatorcontrol_cli.operator_control_group)

# Changing from the following:
# oci operator-access-control operator-actions operator-action ...
# To
# oci opctl operator-action ...
opctl_service_cli.opctl_service_group.commands.pop(operatoractions_cli.operator_actions_root_group.name)
opctl_service_cli.opctl_service_group.add_command(operatoractions_cli.operator_action_group)

# Changing from the following:
# oci operator-access-control operator-control-assignment operator-control-assignment ...
# To
# oci opctl operator-control-assignment ...
opctl_service_cli.opctl_service_group.commands.pop(operatorcontrolassignment_cli.operator_control_assignment_root_group.name)
opctl_service_cli.opctl_service_group.add_command(operatorcontrolassignment_cli.operator_control_assignment_group)
