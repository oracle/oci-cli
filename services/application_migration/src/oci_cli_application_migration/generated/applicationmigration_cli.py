# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('application_migration.application_migration_root_group.command_name', 'application-migration'), cls=CommandGroupWithAlias, help=cli_util.override('application_migration.application_migration_root_group.help', """API for the Application Migration service. Use this API to migrate applications from Oracle Cloud Infrastructure - Classic to Oracle Cloud Infrastructure."""), short_help=cli_util.override('application_migration.application_migration_root_group.short_help', """Application Migration Service API"""))
@cli_util.help_option_group
def application_migration_root_group():
    pass


@click.command(cli_util.override('application_migration.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing an operation that is tracked by a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('application_migration.migration_group.command_name', 'migration'), cls=CommandGroupWithAlias, help="""An application being migrated from a source environment to OCI.""")
@cli_util.help_option_group
def migration_group():
    pass


@click.command(cli_util.override('application_migration.source_application_group.command_name', 'source-application'), cls=CommandGroupWithAlias, help="""An application running in the source environment that is available for export.""")
@cli_util.help_option_group
def source_application_group():
    pass


@click.command(cli_util.override('application_migration.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from executing an operation that is tracked by a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('application_migration.source_group.command_name', 'source'), cls=CommandGroupWithAlias, help="""The Source object. Sources represent external locations from which applications may be imported into an OCI tenancy.""")
@cli_util.help_option_group
def source_group():
    pass


@click.command(cli_util.override('application_migration.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""An asynchronous work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


application_migration_root_group.add_command(work_request_error_group)
application_migration_root_group.add_command(migration_group)
application_migration_root_group.add_command(source_application_group)
application_migration_root_group.add_command(work_request_log_entry_group)
application_migration_root_group.add_command(source_group)
application_migration_root_group.add_command(work_request_group)


@work_request_group.command(name=cli_util.override('application_migration.cancel_work_request.command_name', 'cancel'), help=u"""Cancels the specified work request""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cancel_work_request(ctx, from_json, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.cancel_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.change_migration_compartment.command_name', 'change-compartment'), help=u"""Moves a Migration into a different compartment.""")
@cli_util.option('--migration-id', required=True, help=u"""The application OCID""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_migration_compartment(ctx, from_json, migration_id, compartment_id, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.change_migration_compartment(
        migration_id=migration_id,
        change_migration_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.change_source_compartment.command_name', 'change-compartment'), help=u"""Moves a Source into a different compartment.""")
@cli_util.option('--source-id', required=True, help=u"""The source OCID""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the compartment into which the resource should be moved.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_source_compartment(ctx, from_json, source_id, compartment_id, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.change_source_compartment(
        source_id=source_id,
        change_source_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.create_migration.command_name', 'create'), help=u"""Creates an application migration in the specified compartment. Specify the compartment using the compartment ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique idenfifier (OCID) for the compartment where the Source is located.""")
@cli_util.option('--source-id', required=True, help=u"""Unique identifier (OCID) of the application source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application being migrated from the source.""")
@cli_util.option('--discovery-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Human-readable name of the application.""")
@cli_util.option('--description', help=u"""Description of the application.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'discovery-details': {'module': 'application_migration', 'class': 'DiscoveryDetails'}, 'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'discovery-details': {'module': 'application_migration', 'class': 'DiscoveryDetails'}, 'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration(ctx, from_json, compartment_id, source_id, application_name, discovery_details, display_name, description, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails'] = cli_util.parse_json_parameter("discovery_details", discovery_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_migration(
        create_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.create_migration_oic_discovery_details.command_name', 'create-migration-oic-discovery-details'), help=u"""Creates an application migration in the specified compartment. Specify the compartment using the compartment ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique idenfifier (OCID) for the compartment where the Source is located.""")
@cli_util.option('--source-id', required=True, help=u"""Unique identifier (OCID) of the application source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application being migrated from the source.""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""The OIC instance admin user""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""The OIC instance admin password""")
@cli_util.option('--display-name', help=u"""Human-readable name of the application.""")
@cli_util.option('--description', help=u"""Description of the application.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration_oic_discovery_details(ctx, from_json, compartment_id, source_id, application_name, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'OIC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_migration(
        create_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.create_migration_pcs_discovery_details.command_name', 'create-migration-pcs-discovery-details'), help=u"""Creates an application migration in the specified compartment. Specify the compartment using the compartment ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique idenfifier (OCID) for the compartment where the Source is located.""")
@cli_util.option('--source-id', required=True, help=u"""Unique identifier (OCID) of the application source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application being migrated from the source.""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""The PCS instance admin user""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""The PCS instance admin password""")
@cli_util.option('--display-name', help=u"""Human-readable name of the application.""")
@cli_util.option('--description', help=u"""Description of the application.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration_pcs_discovery_details(ctx, from_json, compartment_id, source_id, application_name, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'PCS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_migration(
        create_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.create_migration_ics_discovery_details.command_name', 'create-migration-ics-discovery-details'), help=u"""Creates an application migration in the specified compartment. Specify the compartment using the compartment ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique idenfifier (OCID) for the compartment where the Source is located.""")
@cli_util.option('--source-id', required=True, help=u"""Unique identifier (OCID) of the application source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application being migrated from the source.""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""The ICS instance admin user""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""The ICS instance admin password""")
@cli_util.option('--display-name', help=u"""Human-readable name of the application.""")
@cli_util.option('--description', help=u"""Description of the application.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration_ics_discovery_details(ctx, from_json, compartment_id, source_id, application_name, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'ICS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_migration(
        create_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.create_migration_oac_discovery_details.command_name', 'create-migration-oac-discovery-details'), help=u"""Creates an application migration in the specified compartment. Specify the compartment using the compartment ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique idenfifier (OCID) for the compartment where the Source is located.""")
@cli_util.option('--source-id', required=True, help=u"""Unique identifier (OCID) of the application source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application being migrated from the source.""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""The OAC instance admin user""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""The OAC instance admin password""")
@cli_util.option('--display-name', help=u"""Human-readable name of the application.""")
@cli_util.option('--description', help=u"""Description of the application.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration_oac_discovery_details(ctx, from_json, compartment_id, source_id, application_name, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'OAC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_migration(
        create_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.create_migration_jcs_discovery_details.command_name', 'create-migration-jcs-discovery-details'), help=u"""Creates an application migration in the specified compartment. Specify the compartment using the compartment ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique idenfifier (OCID) for the compartment where the Source is located.""")
@cli_util.option('--source-id', required=True, help=u"""Unique identifier (OCID) of the application source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application being migrated from the source.""")
@cli_util.option('--discovery-details-weblogic-user', required=True, help=u"""The JCS instance weblogic admin user""")
@cli_util.option('--discovery-details-weblogic-password', required=True, help=u"""The JCS instance weblogic admin password""")
@cli_util.option('--display-name', help=u"""Human-readable name of the application.""")
@cli_util.option('--description', help=u"""Description of the application.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration_jcs_discovery_details(ctx, from_json, compartment_id, source_id, application_name, discovery_details_weblogic_user, discovery_details_weblogic_password, display_name, description, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails']['weblogicUser'] = discovery_details_weblogic_user
    _details['discoveryDetails']['weblogicPassword'] = discovery_details_weblogic_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'JCS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_migration(
        create_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.create_migration_soacs_discovery_details.command_name', 'create-migration-soacs-discovery-details'), help=u"""Creates an application migration in the specified compartment. Specify the compartment using the compartment ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique idenfifier (OCID) for the compartment where the Source is located.""")
@cli_util.option('--source-id', required=True, help=u"""Unique identifier (OCID) of the application source.""")
@cli_util.option('--application-name', required=True, help=u"""Name of the application being migrated from the source.""")
@cli_util.option('--discovery-details-weblogic-user', required=True, help=u"""The SOACS instance weblogic admin user""")
@cli_util.option('--discovery-details-weblogic-password', required=True, help=u"""The SOACS instance weblogic admin password""")
@cli_util.option('--display-name', help=u"""Human-readable name of the application.""")
@cli_util.option('--description', help=u"""Description of the application.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def create_migration_soacs_discovery_details(ctx, from_json, compartment_id, source_id, application_name, discovery_details_weblogic_user, discovery_details_weblogic_password, display_name, description, service_config, application_config, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceId'] = source_id
    _details['applicationName'] = application_name
    _details['discoveryDetails']['weblogicUser'] = discovery_details_weblogic_user
    _details['discoveryDetails']['weblogicPassword'] = discovery_details_weblogic_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'SOACS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_migration(
        create_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.create_source.command_name', 'create'), help=u"""Creates a migration source in the specified compartment. Specify the compartment using the compartment ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique idenfifier (OCID) for the compartment where the Source is located.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Human-readable name of the source.""")
@cli_util.option('--description', help=u"""Description of the source.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source(ctx, from_json, compartment_id, source_details, display_name, description, authorization_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.create_source_internal_source_details.command_name', 'create-source-internal-source-details'), help=u"""Creates a migration source in the specified compartment. Specify the compartment using the compartment ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique idenfifier (OCID) for the compartment where the Source is located.""")
@cli_util.option('--source-details-account-name', required=True, help=u"""The tradition cloud account name""")
@cli_util.option('--display-name', help=u"""Human-readable name of the source.""")
@cli_util.option('--description', help=u"""Description of the source.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source_internal_source_details(ctx, from_json, compartment_id, source_details_account_name, display_name, description, authorization_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['accountName'] = source_details_account_name

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['sourceDetails']['type'] = 'INTERNAL_COMPUTE'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.create_source_ocic_source_details.command_name', 'create-source-ocic-source-details'), help=u"""Creates a migration source in the specified compartment. Specify the compartment using the compartment ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique idenfifier (OCID) for the compartment where the Source is located.""")
@cli_util.option('--source-details-region', required=True, help=u"""The Oracle Cloud Infrastructure - Classic region name (e.g. us2-z11 or uscom-central-1)""")
@cli_util.option('--source-details-compute-account', required=True, help=u"""The compute account id""")
@cli_util.option('--display-name', help=u"""Human-readable name of the source.""")
@cli_util.option('--description', help=u"""Description of the source.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source_ocic_source_details(ctx, from_json, compartment_id, source_details_region, source_details_compute_account, display_name, description, authorization_details, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails']['region'] = source_details_region
    _details['sourceDetails']['computeAccount'] = source_details_compute_account

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['sourceDetails']['type'] = 'OCIC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.create_source_internal_authorization_details.command_name', 'create-source-internal-authorization-details'), help=u"""Creates a migration source in the specified compartment. Specify the compartment using the compartment ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique idenfifier (OCID) for the compartment where the Source is located.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--authorization-details-username', required=True, help=u"""User with Compute Operations role in Oracle Cloud Infrastructure - Classic.""")
@cli_util.option('--authorization-details-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the source.""")
@cli_util.option('--description', help=u"""Description of the source.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source_internal_authorization_details(ctx, from_json, compartment_id, source_details, authorization_details_username, authorization_details_password, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['authorizationDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)
    _details['authorizationDetails']['username'] = authorization_details_username
    _details['authorizationDetails']['password'] = authorization_details_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['authorizationDetails']['type'] = 'INTERNAL_COMPUTE'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.create_source_ocic_authorization_details.command_name', 'create-source-ocic-authorization-details'), help=u"""Creates a migration source in the specified compartment. Specify the compartment using the compartment ID.""")
@cli_util.option('--compartment-id', required=True, help=u"""Unique idenfifier (OCID) for the compartment where the Source is located.""")
@cli_util.option('--source-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--authorization-details-username', required=True, help=u"""User with Compute Operations role in Oracle Cloud Infrastructure - Classic.""")
@cli_util.option('--authorization-details-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the source.""")
@cli_util.option('--description', help=u"""Description of the source.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def create_source_ocic_authorization_details(ctx, from_json, compartment_id, source_details, authorization_details_username, authorization_details_password, display_name, description, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['authorizationDetails'] = {}
    _details['compartmentId'] = compartment_id
    _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)
    _details['authorizationDetails']['username'] = authorization_details_username
    _details['authorizationDetails']['password'] = authorization_details_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['authorizationDetails']['type'] = 'OCIC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.create_source(
        create_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.delete_migration.command_name', 'delete'), help=u"""Deletes the specified Application object.""")
@cli_util.option('--migration-id', required=True, help=u"""The application OCID""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_migration(ctx, from_json, migration_id, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.delete_migration(
        migration_id=migration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.delete_source.command_name', 'delete'), help=u"""Deletes the specified Source object.""")
@cli_util.option('--source-id', required=True, help=u"""The source OCID""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_source(ctx, from_json, source_id, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.delete_source(
        source_id=source_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.get_migration.command_name', 'get'), help=u"""Gets an application migration using the ID.""")
@cli_util.option('--migration-id', required=True, help=u"""The application OCID""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'Migration'})
@cli_util.wrap_exceptions
def get_migration(ctx, from_json, migration_id):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.get_migration(
        migration_id=migration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.get_source.command_name', 'get'), help=u"""Gets a migration source using the source ID.""")
@cli_util.option('--source-id', required=True, help=u"""The source OCID""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'Source'})
@cli_util.wrap_exceptions
def get_source(ctx, from_json, source_id):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.get_source(
        source_id=source_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('application_migration.get_work_request.command_name', 'get'), help=u"""Gets the details of a work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.list_migrations.command_name', 'list'), help=u"""Returns a list of migrations in a given compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment OCID on which to filter.""")
@cli_util.option('--id', help=u"""The OCID on which to query for an application.""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""Specifies the field on which to sort. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.""")
@cli_util.option('--display-name', help=u"""Display name on which to query.""")
@cli_util.option('--lifecycle-state', help=u"""The lifecycle state on which to filter.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[MigrationSummary]'})
@cli_util.wrap_exceptions
def list_migrations(ctx, from_json, all_pages, page_size, compartment_id, id, limit, page, sort_order, sort_by, display_name, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_migrations,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_migrations,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_migrations(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@source_application_group.command(name=cli_util.override('application_migration.list_source_applications.command_name', 'list'), help=u"""Returns a list of applications running in the source environment. This list is generated dynamically by interrogating the source and changes as applications are started or stopped in that environment.""")
@cli_util.option('--source-id', required=True, help=u"""The source OCID""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment OCID on which to filter.""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""Specifies the field on which to sort. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.""")
@cli_util.option('--display-name', help=u"""Resource name on which to query.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[SourceApplicationSummary]'})
@cli_util.wrap_exceptions
def list_source_applications(ctx, from_json, all_pages, page_size, source_id, compartment_id, limit, page, sort_order, sort_by, display_name):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if display_name is not None:
        kwargs['display_name'] = display_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_source_applications,
            source_id=source_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_source_applications,
            limit,
            page_size,
            source_id=source_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_source_applications(
            source_id=source_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.list_sources.command_name', 'list'), help=u"""Returns a list of migration sources in a specified compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment OCID on which to filter.""")
@cli_util.option('--id', help=u"""The OCID on which to query for a source.""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""Specifies the field on which to sort. By default, `TIMECREATED` is ordered descending. By default, `DISPLAYNAME` is ordered ascending. Note that you can sort only on one field.""")
@cli_util.option('--display-name', help=u"""Display name on which to query.""")
@cli_util.option('--lifecycle-state', help=u"""The lifecycle state on which to filter.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[SourceSummary]'})
@cli_util.wrap_exceptions
def list_sources(ctx, from_json, all_pages, page_size, compartment_id, id, limit, page, sort_order, sort_by, display_name, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if id is not None:
        kwargs['id'] = id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_sources,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_sources,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_sources(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('application_migration.list_work_request_errors.command_name', 'list'), help=u"""Gets the errors for a work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('application_migration.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Gets the logs for a work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order, either `ASC` (ascending) or `DESC` (descending).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('application_migration.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment or for a specified resource.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment OCID on which to filter.""")
@cli_util.option('--resource-id', help=u"""The OCID of the resource.""")
@cli_util.option('--limit', type=click.INT, help=u"""The number of items returned in a paginated `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the preceding `List` call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'application_migration', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, resource_id, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.migrate_application.command_name', 'migrate-application'), help=u"""Validates target configuration and migrates a PaaS application running in a Source environment into the customers Oracle Cloud Infrastructure tenancy. This an optional action and only required if automatic start of migration was not selected when creating the migration.""")
@cli_util.option('--migration-id', required=True, help=u"""The application OCID""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def migrate_application(ctx, from_json, migration_id):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.migrate_application(
        migration_id=migration_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.update_migration.command_name', 'update'), help=u"""Update the configuration for an application migration.""")
@cli_util.option('--migration-id', required=True, help=u"""The application OCID""")
@cli_util.option('--display-name', help=u"""Human-readable name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--discovery-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'discovery-details': {'module': 'application_migration', 'class': 'DiscoveryDetails'}, 'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'discovery-details': {'module': 'application_migration', 'class': 'DiscoveryDetails'}, 'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration(ctx, from_json, force, migration_id, display_name, description, discovery_details, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if discovery_details or service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to discovery-details and service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if discovery_details is not None:
        _details['discoveryDetails'] = cli_util.parse_json_parameter("discovery_details", discovery_details)

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_migration(
        migration_id=migration_id,
        update_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.update_migration_oic_discovery_details.command_name', 'update-migration-oic-discovery-details'), help=u"""Update the configuration for an application migration.""")
@cli_util.option('--migration-id', required=True, help=u"""The application OCID""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""The OIC instance admin user""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""The OIC instance admin password""")
@cli_util.option('--display-name', help=u"""Human-readable name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration_oic_discovery_details(ctx, from_json, force, migration_id, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'OIC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_migration(
        migration_id=migration_id,
        update_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.update_migration_pcs_discovery_details.command_name', 'update-migration-pcs-discovery-details'), help=u"""Update the configuration for an application migration.""")
@cli_util.option('--migration-id', required=True, help=u"""The application OCID""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""The PCS instance admin user""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""The PCS instance admin password""")
@cli_util.option('--display-name', help=u"""Human-readable name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration_pcs_discovery_details(ctx, from_json, force, migration_id, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'PCS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_migration(
        migration_id=migration_id,
        update_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.update_migration_ics_discovery_details.command_name', 'update-migration-ics-discovery-details'), help=u"""Update the configuration for an application migration.""")
@cli_util.option('--migration-id', required=True, help=u"""The application OCID""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""The ICS instance admin user""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""The ICS instance admin password""")
@cli_util.option('--display-name', help=u"""Human-readable name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration_ics_discovery_details(ctx, from_json, force, migration_id, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'ICS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_migration(
        migration_id=migration_id,
        update_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.update_migration_oac_discovery_details.command_name', 'update-migration-oac-discovery-details'), help=u"""Update the configuration for an application migration.""")
@cli_util.option('--migration-id', required=True, help=u"""The application OCID""")
@cli_util.option('--discovery-details-service-instance-user', required=True, help=u"""The OAC instance admin user""")
@cli_util.option('--discovery-details-service-instance-password', required=True, help=u"""The OAC instance admin password""")
@cli_util.option('--display-name', help=u"""Human-readable name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration_oac_discovery_details(ctx, from_json, force, migration_id, discovery_details_service_instance_user, discovery_details_service_instance_password, display_name, description, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['discoveryDetails']['serviceInstanceUser'] = discovery_details_service_instance_user
    _details['discoveryDetails']['serviceInstancePassword'] = discovery_details_service_instance_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'OAC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_migration(
        migration_id=migration_id,
        update_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.update_migration_jcs_discovery_details.command_name', 'update-migration-jcs-discovery-details'), help=u"""Update the configuration for an application migration.""")
@cli_util.option('--migration-id', required=True, help=u"""The application OCID""")
@cli_util.option('--discovery-details-weblogic-user', required=True, help=u"""The JCS instance weblogic admin user""")
@cli_util.option('--discovery-details-weblogic-password', required=True, help=u"""The JCS instance weblogic admin password""")
@cli_util.option('--display-name', help=u"""Human-readable name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration_jcs_discovery_details(ctx, from_json, force, migration_id, discovery_details_weblogic_user, discovery_details_weblogic_password, display_name, description, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['discoveryDetails']['weblogicUser'] = discovery_details_weblogic_user
    _details['discoveryDetails']['weblogicPassword'] = discovery_details_weblogic_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'JCS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_migration(
        migration_id=migration_id,
        update_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@migration_group.command(name=cli_util.override('application_migration.update_migration_soacs_discovery_details.command_name', 'update-migration-soacs-discovery-details'), help=u"""Update the configuration for an application migration.""")
@cli_util.option('--migration-id', required=True, help=u"""The application OCID""")
@cli_util.option('--discovery-details-weblogic-user', required=True, help=u"""The SOACS instance weblogic admin user""")
@cli_util.option('--discovery-details-weblogic-password', required=True, help=u"""The SOACS instance weblogic admin password""")
@cli_util.option('--display-name', help=u"""Human-readable name of the migration.""")
@cli_util.option('--description', help=u"""Description of the migration.""")
@cli_util.option('--service-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--application-config', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Configuration required to migrate the application. In addition to the key and value, additional fields are provided to describe type type and purpose of each field. Only the value for each key is required when passing configuration to the CreateMigration operation.

This option is a JSON dictionary of type dict(str, ConfigurationField).  For documentation on ConfigurationField please see our API reference: https://docs.cloud.oracle.com/api/#/en/applicationmigration/20191031/datatypes/ConfigurationField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'application-config': {'module': 'application_migration', 'class': 'dict(str, ConfigurationField)'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_migration_soacs_discovery_details(ctx, from_json, force, migration_id, discovery_details_weblogic_user, discovery_details_weblogic_password, display_name, description, service_config, application_config, freeform_tags, defined_tags, if_match):

    if isinstance(migration_id, six.string_types) and len(migration_id.strip()) == 0:
        raise click.UsageError('Parameter --migration-id cannot be whitespace or empty string')
    if not force:
        if service_config or application_config or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to service-config and application-config and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['discoveryDetails'] = {}
    _details['discoveryDetails']['weblogicUser'] = discovery_details_weblogic_user
    _details['discoveryDetails']['weblogicPassword'] = discovery_details_weblogic_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if service_config is not None:
        _details['serviceConfig'] = cli_util.parse_json_parameter("service_config", service_config)

    if application_config is not None:
        _details['applicationConfig'] = cli_util.parse_json_parameter("application_config", application_config)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['discoveryDetails']['type'] = 'SOACS'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_migration(
        migration_id=migration_id,
        update_migration_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.update_source.command_name', 'update'), help=u"""Update source details.""")
@cli_util.option('--source-id', required=True, help=u"""The source OCID""")
@cli_util.option('--display-name', help=u"""Human-readable name of the source.""")
@cli_util.option('--description', help=u"""Description of the source.""")
@cli_util.option('--source-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_source(ctx, from_json, force, source_id, display_name, description, source_details, authorization_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if source_details or authorization_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source-details and authorization-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if source_details is not None:
        _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.update_source_internal_source_details.command_name', 'update-source-internal-source-details'), help=u"""Update source details.""")
@cli_util.option('--source-id', required=True, help=u"""The source OCID""")
@cli_util.option('--source-details-account-name', required=True, help=u"""The tradition cloud account name""")
@cli_util.option('--display-name', help=u"""Human-readable name of the source.""")
@cli_util.option('--description', help=u"""Description of the source.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_source_internal_source_details(ctx, from_json, force, source_id, source_details_account_name, display_name, description, authorization_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if authorization_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to authorization-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDetails'] = {}
    _details['sourceDetails']['accountName'] = source_details_account_name

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['sourceDetails']['type'] = 'INTERNAL_COMPUTE'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.update_source_ocic_source_details.command_name', 'update-source-ocic-source-details'), help=u"""Update source details.""")
@cli_util.option('--source-id', required=True, help=u"""The source OCID""")
@cli_util.option('--source-details-region', required=True, help=u"""The Oracle Cloud Infrastructure - Classic region name (e.g. us2-z11 or uscom-central-1)""")
@cli_util.option('--source-details-compute-account', required=True, help=u"""The compute account id""")
@cli_util.option('--display-name', help=u"""Human-readable name of the source.""")
@cli_util.option('--description', help=u"""Description of the source.""")
@cli_util.option('--authorization-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'authorization-details': {'module': 'application_migration', 'class': 'AuthorizationDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_source_ocic_source_details(ctx, from_json, force, source_id, source_details_region, source_details_compute_account, display_name, description, authorization_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if authorization_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to authorization-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['sourceDetails'] = {}
    _details['sourceDetails']['region'] = source_details_region
    _details['sourceDetails']['computeAccount'] = source_details_compute_account

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if authorization_details is not None:
        _details['authorizationDetails'] = cli_util.parse_json_parameter("authorization_details", authorization_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['sourceDetails']['type'] = 'OCIC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.update_source_internal_authorization_details.command_name', 'update-source-internal-authorization-details'), help=u"""Update source details.""")
@cli_util.option('--source-id', required=True, help=u"""The source OCID""")
@cli_util.option('--authorization-details-username', required=True, help=u"""User with Compute Operations role in Oracle Cloud Infrastructure - Classic.""")
@cli_util.option('--authorization-details-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the source.""")
@cli_util.option('--description', help=u"""Description of the source.""")
@cli_util.option('--source-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_source_internal_authorization_details(ctx, from_json, force, source_id, authorization_details_username, authorization_details_password, display_name, description, source_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if source_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['authorizationDetails'] = {}
    _details['authorizationDetails']['username'] = authorization_details_username
    _details['authorizationDetails']['password'] = authorization_details_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if source_details is not None:
        _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['authorizationDetails']['type'] = 'INTERNAL_COMPUTE'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@source_group.command(name=cli_util.override('application_migration.update_source_ocic_authorization_details.command_name', 'update-source-ocic-authorization-details'), help=u"""Update source details.""")
@cli_util.option('--source-id', required=True, help=u"""The source OCID""")
@cli_util.option('--authorization-details-username', required=True, help=u"""User with Compute Operations role in Oracle Cloud Infrastructure - Classic.""")
@cli_util.option('--authorization-details-password', required=True, help=u"""Password for this user.""")
@cli_util.option('--display-name', help=u"""Human-readable name of the source.""")
@cli_util.option('--description', help=u"""Description of the source.""")
@cli_util.option('--source-details', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'source-details': {'module': 'application_migration', 'class': 'SourceDetails'}, 'freeform-tags': {'module': 'application_migration', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'application_migration', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_source_ocic_authorization_details(ctx, from_json, force, source_id, authorization_details_username, authorization_details_password, display_name, description, source_details, freeform_tags, defined_tags, if_match):

    if isinstance(source_id, six.string_types) and len(source_id.strip()) == 0:
        raise click.UsageError('Parameter --source-id cannot be whitespace or empty string')
    if not force:
        if source_details or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to source-details and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['authorizationDetails'] = {}
    _details['authorizationDetails']['username'] = authorization_details_username
    _details['authorizationDetails']['password'] = authorization_details_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if source_details is not None:
        _details['sourceDetails'] = cli_util.parse_json_parameter("source_details", source_details)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['authorizationDetails']['type'] = 'OCIC'

    client = cli_util.build_client('application_migration', 'application_migration', ctx)
    result = client.update_source(
        source_id=source_id,
        update_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
