# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from services.application_migration.src.oci_cli_application_migration.generated import applicationmigration_cli

'''
Drop following commands:
oci application-migration migration create-migration-ics-discovery-details --application-name, --compartment-id, --discovery-details-service-instance-password, --discovery-details-service-instance-user, --source-id, --application-config, --defined-tags, --description, --display-name, --freeform-tags, --is-automatic-migration, --is-new-service-required, --service-config
oci application-migration migration create-migration-jcs-discovery-details --application-name, --compartment-id, --discovery-details-weblogic-password, --discovery-details-weblogic-user, --source-id, --application-config, --defined-tags, --description, --display-name, --freeform-tags, --is-automatic-migration, --is-new-service-required, --service-config
oci application-migration migration create-migration-oac-discovery-details --application-name, --compartment-id, --discovery-details-service-instance-password, --discovery-details-service-instance-user, --source-id, --application-config, --defined-tags, --description, --display-name, --freeform-tags, --is-automatic-migration, --is-new-service-required, --service-config
oci application-migration migration create-migration-oic-discovery-details --application-name, --compartment-id, --discovery-details-service-instance-password, --discovery-details-service-instance-user, --source-id, --application-config, --defined-tags, --description, --display-name, --freeform-tags, --is-automatic-migration, --is-new-service-required, --service-config
oci application-migration migration create-migration-pcs-discovery-details --application-name, --compartment-id, --discovery-details-service-instance-password, --discovery-details-service-instance-user, --source-id, --application-config, --defined-tags, --description, --display-name, --freeform-tags, --is-automatic-migration, --is-new-service-required, --service-config
oci application-migration migration create-migration-soacs-discovery-details --application-name, --compartment-id, --discovery-details-weblogic-password, --discovery-details-weblogic-user, --source-id, --application-config, --defined-tags, --description, --display-name, --freeform-tags, --is-automatic-migration, --is-new-service-required, --service-config

oci application-migration migration update-migration-ics-discovery-details --discovery-details-service-instance-password, --discovery-details-service-instance-user, --migration-id, --application-config, --defined-tags, --description, --display-name, --force, --freeform-tags, --is-automatic-migration, --is-new-service-required, --service-config
oci application-migration migration update-migration-jcs-discovery-details --discovery-details-weblogic-password, --discovery-details-weblogic-user, --migration-id, --application-config, --defined-tags, --description, --display-name, --force, --freeform-tags, --is-automatic-migration, --is-new-service-required, --service-config
oci application-migration migration update-migration-oac-discovery-details --discovery-details-service-instance-password, --discovery-details-service-instance-user, --migration-id, --application-config, --defined-tags, --description, --display-name, --force, --freeform-tags, --is-automatic-migration, --is-new-service-required, --service-config
oci application-migration migration update-migration-oic-discovery-details --discovery-details-service-instance-password, --discovery-details-service-instance-user, --migration-id, --application-config, --defined-tags, --description, --display-name, --force, --freeform-tags, --is-automatic-migration, --is-new-service-required, --service-config
oci application-migration migration update-migration-pcs-discovery-details --discovery-details-service-instance-password, --discovery-details-service-instance-user, --migration-id, --application-config, --defined-tags, --description, --display-name, --force, --freeform-tags, --is-automatic-migration, --is-new-service-required, --service-config
oci application-migration migration update-migration-soacs-discovery-details --discovery-details-weblogic-password, --discovery-details-weblogic-user, --migration-id, --application-config, --defined-tags, --description, --display-name, --force, --freeform-tags, --is-automatic-migration, --is-new-service-required, --service-config

oci application-migration source create-source-ocic-authorization-details --authorization-details-password, --authorization-details-username, --compartment-id, --source-details, --defined-tags, --description, --display-name, --freeform-tags
oci application-migration source create-source-ocic-source-details --compartment-id, --source-details-compute-account, --source-details-region, --authorization-details, --defined-tags, --description, --display-name, --freeform-tags

oci application-migration source update-source-ocic-authorization-details --authorization-details-password, --authorization-details-username, --source-id, --defined-tags, --description, --display-name, --force, --freeform-tags, --source-details
oci application-migration source update-source-ocic-source-details --source-details-compute-account, --source-details-region, --source-id, --authorization-details, --defined-tags, --description, --display-name, --force, --freeform-tags

oci application-migration source-application get --source-application-name, --source-id
'''

applicationmigration_cli.migration_group.commands.pop(applicationmigration_cli.create_migration_ics_discovery_details.name)
applicationmigration_cli.migration_group.commands.pop(applicationmigration_cli.create_migration_jcs_discovery_details.name)
applicationmigration_cli.migration_group.commands.pop(applicationmigration_cli.create_migration_oac_discovery_details.name)
applicationmigration_cli.migration_group.commands.pop(applicationmigration_cli.create_migration_oic_discovery_details.name)
applicationmigration_cli.migration_group.commands.pop(applicationmigration_cli.create_migration_pcs_discovery_details.name)
applicationmigration_cli.migration_group.commands.pop(applicationmigration_cli.create_migration_soacs_discovery_details.name)

applicationmigration_cli.migration_group.commands.pop(applicationmigration_cli.update_migration_ics_discovery_details.name)
applicationmigration_cli.migration_group.commands.pop(applicationmigration_cli.update_migration_jcs_discovery_details.name)
applicationmigration_cli.migration_group.commands.pop(applicationmigration_cli.update_migration_oac_discovery_details.name)
applicationmigration_cli.migration_group.commands.pop(applicationmigration_cli.update_migration_oic_discovery_details.name)
applicationmigration_cli.migration_group.commands.pop(applicationmigration_cli.update_migration_pcs_discovery_details.name)
applicationmigration_cli.migration_group.commands.pop(applicationmigration_cli.update_migration_soacs_discovery_details.name)

applicationmigration_cli.source_group.commands.pop(applicationmigration_cli.create_source_internal_authorization_details.name)
applicationmigration_cli.source_group.commands.pop(applicationmigration_cli.create_source_internal_source_details.name)
applicationmigration_cli.source_group.commands.pop(applicationmigration_cli.create_source_ocic_authorization_details.name)
applicationmigration_cli.source_group.commands.pop(applicationmigration_cli.create_source_ocic_source_details.name)

applicationmigration_cli.source_group.commands.pop(applicationmigration_cli.update_source_internal_authorization_details.name)
applicationmigration_cli.source_group.commands.pop(applicationmigration_cli.update_source_internal_source_details.name)
applicationmigration_cli.source_group.commands.pop(applicationmigration_cli.update_source_ocic_authorization_details.name)
applicationmigration_cli.source_group.commands.pop(applicationmigration_cli.update_source_ocic_source_details.name)
