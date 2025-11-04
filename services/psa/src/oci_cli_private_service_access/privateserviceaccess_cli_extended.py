# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.psa.src.oci_cli_private_service_access.generated import privateserviceaccess_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


# Adding a new group psa-services under Root group "psa"
@click.command('psa-services', cls=CommandGroupWithAlias, help="""Results of a privateServiceAccess search. Contains both
  PrivateServiceAccessSummary items and other information, such as metadata.""")
@cli_util.help_option_group
def psa_services_group():
    pass


# Adding a new group under the root group
# oci psa psa-services
privateserviceaccess_cli.psa_root_group.add_command(psa_services_group)

# oci psa work-request-log-entry -> oci psa private-service-access
privateserviceaccess_cli.psa_root_group.commands.pop(privateserviceaccess_cli.work_request_log_entry_group.name)

# Rename commands
# oci psa psa-services list-private-service-accesses -> oci psa psa-services list
cli_util.rename_command(privateserviceaccess_cli.private_service_access_group, privateserviceaccess_cli.private_service_access_collection_group, privateserviceaccess_cli.list_psa_services, "list")

# oci psa private-service-access list-private-service-accesses -> oci psa private-service-access list
cli_util.rename_command(privateserviceaccess_cli, privateserviceaccess_cli.private_service_access_group, privateserviceaccess_cli.list_private_service_accesses, "list")

# oci psa private-service-access work-request list-psa  -> oci psa work-request list
cli_util.rename_command(privateserviceaccess_cli.private_service_access_group, privateserviceaccess_cli.work_request_group, privateserviceaccess_cli.list_psa_work_requests, "list")

# oci psa private-service-access work-request get-psa  -> oci psa work-request get
cli_util.rename_command(privateserviceaccess_cli.private_service_access_group, privateserviceaccess_cli.work_request_group, privateserviceaccess_cli.get_psa_work_request, "get")

# oci psa private-service-access work-request get-psa  -> oci psa work-request get
cli_util.rename_command(privateserviceaccess_cli.private_service_access_group, privateserviceaccess_cli.work_request_group, privateserviceaccess_cli.cancel_psa_work_request, "cancel")

# oci psa private-service-access work-request-error list-psa  -> oci psa work-request-error list
cli_util.rename_command(privateserviceaccess_cli.private_service_access_group, privateserviceaccess_cli.work_request_error_group, privateserviceaccess_cli.list_psa_work_request_errors, "list")

# oci psa private-service-access work-request-log-entry list-psa-work-request-logs  -> oci psa work-request-log-entry list
cli_util.rename_command(privateserviceaccess_cli.private_service_access_group, privateserviceaccess_cli.work_request_log_entry_group, privateserviceaccess_cli.list_psa_work_request_logs, "list")

# oci psa work-request-log-entry list -> oci psa work-request-log list
cli_util.rename_command(privateserviceaccess_cli, privateserviceaccess_cli.private_service_access_group, privateserviceaccess_cli.work_request_log_entry_group, "work-request-log")

# Adding psa-services group under psa group
# oci psa -> oci psa psa-services
psa_services_group.add_command(privateserviceaccess_cli.list_psa_services)

# oci psa private-service-access work-request -> oci psa work-request
privateserviceaccess_cli.psa_root_group.add_command(privateserviceaccess_cli.work_request_group)

# oci psa private-service-access work-request-error -> oci psa work-request-error
privateserviceaccess_cli.psa_root_group.add_command(privateserviceaccess_cli.work_request_error_group)

# oci psa private-service-access work-request-log-entry -> oci psa work-request-log-entry
privateserviceaccess_cli.psa_root_group.add_command(privateserviceaccess_cli.work_request_log_entry_group)

# oci psa private-service-access private-service-access-collection list-private-service-accesses -> oci psa private-service-access list
privateserviceaccess_cli.private_service_access_group.add_command(privateserviceaccess_cli.list_private_service_accesses)

# oci psa private-service-access private-service-access create -> oci psa private-service-access create
privateserviceaccess_cli.private_service_access_group.add_command(privateserviceaccess_cli.create_private_service_access)

# oci psa private-service-access private-service-access get -> oci psa private-service-access get
privateserviceaccess_cli.private_service_access_group.add_command(privateserviceaccess_cli.get_private_service_access)

# oci psa private-service-access private-service-access delete -> oci psa private-service-access delete
privateserviceaccess_cli.private_service_access_group.add_command(privateserviceaccess_cli.delete_private_service_access)

# oci psa private-service-access private-service-access update -> oci psa private-service-access update
privateserviceaccess_cli.private_service_access_group.add_command(privateserviceaccess_cli.update_private_service_access)

# oci psa private-service-access private-service-access change-compartment -> oci psa private-service-access change-compartment
privateserviceaccess_cli.private_service_access_group.add_command(privateserviceaccess_cli.change_private_service_access_compartment)

# oci psa private-service-access psa-service-collection -> oci psa private-service-access
privateserviceaccess_cli.psa_root_group.commands.pop(privateserviceaccess_cli.psa_service_collection_group.name)

# oci psa private-service-access work-request-log-entry -> oci psa private-service-access
privateserviceaccess_cli.private_service_access_group.commands.pop(privateserviceaccess_cli.work_request_log_entry_group.name)

# oci psa private-service-access private-service-access-collection -> oci psa private-service-access
privateserviceaccess_cli.psa_root_group.commands.pop(privateserviceaccess_cli.private_service_access_collection_group.name)
