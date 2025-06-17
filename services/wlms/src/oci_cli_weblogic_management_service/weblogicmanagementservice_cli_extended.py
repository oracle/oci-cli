# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.wlms.src.oci_cli_wlms.generated import wlms_service_cli
from services.wlms.src.oci_cli_weblogic_management_service.generated import weblogicmanagementservice_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci wlms weblogic-management-service managed-instance list-managed-instance-scan-results -> oci wlms weblogic-management-service managed-instance list-scan-results
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.managed_instance_group, weblogicmanagementservice_cli.list_managed_instance_scan_results, "list-scan-results")


# oci wlms weblogic-management-service managed-instance list-managed-instance-servers -> oci wlms weblogic-management-service managed-instance list-servers
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.managed_instance_group, weblogicmanagementservice_cli.list_managed_instance_servers, "list-servers")


# oci wlms weblogic-management-service wls-domain list-wls-domain-credentials -> oci wlms weblogic-management-service wls-domain list-credentials
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.wls_domain_group, weblogicmanagementservice_cli.list_wls_domain_credentials, "list-credentials")


# oci wlms weblogic-management-service wls-domain get-wls-domain-credential -> oci wlms weblogic-management-service wls-domain get-credential
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.wls_domain_group, weblogicmanagementservice_cli.get_wls_domain_credential, "get-credential")


# oci wlms weblogic-management-service wls-domain update-wls-domain-credential -> oci wlms weblogic-management-service wls-domain update-credential
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.wls_domain_group, weblogicmanagementservice_cli.update_wls_domain_credential, "update-credential")


# oci wlms weblogic-management-service wls-domain list-wls-domain-scan-results -> oci wlms weblogic-management-service wls-domain list-scan-results
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.wls_domain_group, weblogicmanagementservice_cli.list_wls_domain_scan_results, "list-scan-results")


# oci wlms weblogic-management-service wls-domain list-wls-domain-servers -> oci wlms weblogic-management-service wls-domain list-servers
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.wls_domain_group, weblogicmanagementservice_cli.list_wls_domain_servers, "list-servers")


# Remove list-wls-domains-sharing-middlewares from oci wlms weblogic-management-service wls-domain
weblogicmanagementservice_cli.wls_domain_group.commands.pop(weblogicmanagementservice_cli.list_wls_domains_sharing_middlewares.name)


# Remove weblogic-management-service from oci wlms
wlms_service_cli.wlms_service_group.commands.pop(weblogicmanagementservice_cli.weblogic_management_service_root_group.name)


# Move commands under 'oci wlms weblogic-management-service' -> 'oci wlms'
wlms_service_cli.wlms_service_group.add_command(weblogicmanagementservice_cli.resource_inventory_group)
wlms_service_cli.wlms_service_group.add_command(weblogicmanagementservice_cli.agreement_group)
wlms_service_cli.wlms_service_group.add_command(weblogicmanagementservice_cli.managed_instance_group)
wlms_service_cli.wlms_service_group.add_command(weblogicmanagementservice_cli.wls_domain_group)
wlms_service_cli.wlms_service_group.add_command(weblogicmanagementservice_cli.required_policy_collection_group)
wlms_service_cli.wlms_service_group.add_command(weblogicmanagementservice_cli.work_request_group)


# oci wlms managed-instance get-managed-instance-server -> oci wlms managed-instance get-server
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.managed_instance_group, weblogicmanagementservice_cli.get_managed_instance_server, "get-server")


# oci wlms managed-instance list-managed-instance-server-installed-patches -> oci wlms managed-instance list-server-installed-patches
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.managed_instance_group, weblogicmanagementservice_cli.list_managed_instance_server_installed_patches, "list-server-installed-patches")


# oci wlms wls-domain get-wls-domain-server -> oci wlms wls-domain get-server
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.wls_domain_group, weblogicmanagementservice_cli.get_wls_domain_server, "get-server")


# oci wlms wls-domain get-wls-domain-server-backup -> oci wlms wls-domain get-server-backup
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.wls_domain_group, weblogicmanagementservice_cli.get_wls_domain_server_backup, "get-server-backup")


# oci wlms wls-domain get-wls-domain-server-backup-content -> oci wlms wls-domain get-server-backup-content
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.wls_domain_group, weblogicmanagementservice_cli.get_wls_domain_server_backup_content, "get-server-backup-content")


# oci wlms wls-domain list-wls-domain-server-backups -> oci wlms wls-domain list-server-backups
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.wls_domain_group, weblogicmanagementservice_cli.list_wls_domain_server_backups, "list-server-backups")


# oci wlms wls-domain list-wls-domain-server-installed-patches -> oci wlms wls-domain list-server-installed-patches
cli_util.rename_command(weblogicmanagementservice_cli, weblogicmanagementservice_cli.wls_domain_group, weblogicmanagementservice_cli.list_wls_domain_server_installed_patches, "list-server-installed-patches")
