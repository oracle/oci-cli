# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
from services.application_migration.src.oci_cli_application_migration.generated import applicationmigration_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types


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


# oci application-migration source create-source-ocic-authorization-token-details -> oci application-migration source create-source-ocic-authtoken
# oci application-migration source update-source-ocic-authorization-token-details -> oci application-migration source update-source-ocic-authtoken
cli_util.rename_command(applicationmigration_cli, applicationmigration_cli.source_group, applicationmigration_cli.update_source_ocic_authorization_token_details, 'update-source-ocic-authtoken')
cli_util.rename_command(applicationmigration_cli, applicationmigration_cli.source_group, applicationmigration_cli.create_source_ocic_authorization_token_details, 'create-source-ocic-authtoken')


# Remove create-source-occ-authorization-details from oci application-migration source
applicationmigration_cli.source_group.commands.pop(applicationmigration_cli.create_source_occ_authorization_details.name)


# Remove create-source-occ-source-details from oci application-migration source
applicationmigration_cli.source_group.commands.pop(applicationmigration_cli.create_source_occ_source_details.name)


# Remove update-source-occ-authorization-details from oci application-migration source
applicationmigration_cli.source_group.commands.pop(applicationmigration_cli.update_source_occ_authorization_details.name)


# Remove update-source-occ-source-details from oci application-migration source
applicationmigration_cli.source_group.commands.pop(applicationmigration_cli.update_source_occ_source_details.name)


@cli_util.copy_params_from_generated_command(applicationmigration_cli.list_migrations, params_to_exclude=['lifecycle_state'])
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "SUCCEEDED", "DELETING", "DELETED"]), help=u"""Filter results on lifecycleState.""")
@applicationmigration_cli.migration_group.command(name=cli_util.override('application_migration.list_migrations.command_name', 'list'), help=applicationmigration_cli.list_migrations.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[MigrationSummary]'})
@cli_util.wrap_exceptions
def list_migrations_extended(ctx, **kwargs):
    ctx.invoke(applicationmigration_cli.list_migrations, **kwargs)


@cli_util.copy_params_from_generated_command(applicationmigration_cli.list_sources, params_to_exclude=['lifecycle_state'])
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "DELETING", "UPDATING", "ACTIVE", "INACTIVE", "DELETED"]), help=u"""Filter results on lifecycleState.""")
@applicationmigration_cli.source_group.command(name=cli_util.override('application_migration.list_sources.command_name', 'list'), help=applicationmigration_cli.list_sources.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[SourceSummary]'})
@cli_util.wrap_exceptions
def list_sources_extended(ctx, **kwargs):
    ctx.invoke(applicationmigration_cli.list_sources, **kwargs)
