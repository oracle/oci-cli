# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function

from services.dts.src.oci_cli_dts.generated import dts_service_cli
from services.dts.src.oci_cli_transfer_job.generated import transferjob_cli
from services.dts.src.oci_cli_transfer_appliance.generated import transferappliance_cli
from services.dts.src.oci_cli_transfer_appliance_entitlement.generated import transferapplianceentitlement_cli
from services.dts.src.oci_cli_transfer_device.generated import transferdevice_cli
from services.dts.src.oci_cli_transfer_package.generated import transferpackage_cli
from services.dts.src.oci_cli_shipping_vendors.generated import shippingvendors_cli

from services.dts.src.oci_cli_dts.dts_transform import DTS_Transform

# COMMAND HELP OVERRIDES ####
command_help_override_list = [
    # Job
    {"command": transferjob_cli.create_transfer_job,
        "help_text": "Creates a new transfer disk or appliance job."},
    {"command": transferjob_cli.get_transfer_job,
        "help_text": "Shows the transfer disk or appliance job details."},
    {"command": transferjob_cli.update_transfer_job,
        "help_text": "Updates the transfer disk or appliance job details."},
    {"command": transferjob_cli.delete_transfer_job,
        "help_text": "Deletes the transfer disk or appliance job."},
    {"command": transferjob_cli.list_transfer_jobs,
        "help_text": "Lists all transfer disk or appliance jobs."},
]
#

# GROUP HELP STRING OVERRIDES #####
group_help_override_list = [
    {"group": dts_service_cli.dts_service_group,
        "help_text": "Transfer disk or appliance job operations",
        "short_help_text": "Data Transfer Service"},

    {"group": transferjob_cli.transfer_job_root_group,
        "help_text": "Transfer disk or appliance job operations",
        "short_help_text": "Transfer disk or appliance job operations"},

    {"group": transferappliance_cli.transfer_appliance_root_group,
        "help_text": "Transfer appliance operations",
        "short_help_text": "Transfer appliance operations"},


]
#


# RENAME COMMANDS #####
rename_command_list = [
    {"group": dts_service_cli.dts_service_group, "old": transferjob_cli.transfer_job_root_group, "new": "job"},

    {"group": transferjob_cli.transfer_job_root_group, "old": transferjob_cli.get_transfer_job, "new": "show"},

    {"group": transferapplianceentitlement_cli.transfer_appliance_entitlement_root_group, "old": transferapplianceentitlement_cli.create_transfer_appliance_entitlement, "new": "request-entitlement"},
    {"group": transferapplianceentitlement_cli.transfer_appliance_entitlement_root_group, "old": transferapplianceentitlement_cli.get_transfer_appliance_entitlement, "new": "show-entitlement"},

]
#


# RELOCATE COMMANDS ####
relocate_command_list = [
    # dts job commands
    {"group": transferjob_cli.transfer_job_root_group, "command": transferjob_cli.create_transfer_job},
    {"group": transferjob_cli.transfer_job_root_group, "command": transferjob_cli.delete_transfer_job},
    {"group": transferjob_cli.transfer_job_root_group, "command": transferjob_cli.get_transfer_job},
    {"group": transferjob_cli.transfer_job_root_group, "command": transferjob_cli.list_transfer_jobs},
    {"group": transferjob_cli.transfer_job_root_group, "command": transferjob_cli.update_transfer_job},

]
#

# POP COMMANDS #######
pop_command_list = [
    # dts
    {"group": dts_service_cli.dts_service_group, "command": transferdevice_cli.transfer_device_group.name},
    {"group": dts_service_cli.dts_service_group, "command": transferpackage_cli.transfer_package_group.name},
    {"group": dts_service_cli.dts_service_group, "command": shippingvendors_cli.shipping_vendors_group.name},
    {"group": dts_service_cli.dts_service_group, "command": transferapplianceentitlement_cli.transfer_appliance_entitlement_root_group.name},

    # dts job
    {"group": transferjob_cli.transfer_job_root_group, "command": transferjob_cli.transfer_job_group.name},

]
####

DTS_Transform.transform(command_help_override_list=command_help_override_list,
                        group_help_override_list=group_help_override_list,
                        rename_command_list=rename_command_list,
                        relocate_command_list=relocate_command_list,
                        pop_command_list=pop_command_list)
