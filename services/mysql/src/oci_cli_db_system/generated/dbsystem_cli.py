# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.mysql.src.oci_cli_mysql.generated import mysql_service_cli


@click.command(cli_util.override('db_system.db_system_root_group.command_name', 'db-system'), cls=CommandGroupWithAlias, help=cli_util.override('db_system.db_system_root_group.help', """The API for the MySQL Database Service"""), short_help=cli_util.override('db_system.db_system_root_group.short_help', """MySQL Database Service API"""))
@cli_util.help_option_group
def db_system_root_group():
    pass


@click.command(cli_util.override('db_system.db_system_group.command_name', 'db-system'), cls=CommandGroupWithAlias, help="""A DB System is the core logical unit of MySQL Database Service.""")
@cli_util.help_option_group
def db_system_group():
    pass


mysql_service_cli.mysql_service_group.add_command(db_system_root_group)
db_system_root_group.add_command(db_system_group)


@db_system_group.command(name=cli_util.override('db_system.create_db_system.command_name', 'create'), help=u"""Creates and launches a DB System.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--configuration-id', required=True, help=u"""The OCID of the Configuration to be used for this DB System.""")
@cli_util.option('--shape-name', required=True, help=u"""The name of the shape. The shape determines the resources allocated - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. To get a list of shapes, use the [ListShapes] operation.""")
@cli_util.option('--subnet-id', required=True, help=u"""The OCID of the subnet the DB System is associated with.""")
@cli_util.option('--admin-username', required=True, help=u"""The username for the administrative user.""")
@cli_util.option('--admin-password', required=True, help=u"""The password for the administrative user. The password must be between 8 and 32 characters long, and must contain at least 1 numeric character, 1 lowercase character, 1 uppercase character, and 1 special (nonalphanumeric) character.""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the DB System. It does not have to be unique.""")
@cli_util.option('--description', help=u"""User-provided data about the DB System.""")
@cli_util.option('--availability-domain', help=u"""The Availability Domain where the primary instance should be located.""")
@cli_util.option('--fault-domain', help=u"""The name of the Fault Domain the DB System is located in.""")
@cli_util.option('--mysql-version', help=u"""The specific MySQL version identifier.""")
@cli_util.option('--data-storage-size-in-gbs', type=click.INT, help=u"""Initial size of the data volume in GBs that will be created and attached. Keep in mind that this only specifies the size of the database data volume, the log volume for the database will be scaled appropriately with its shape.""")
@cli_util.option('--hostname-label', help=u"""The hostname for the primary endpoint of the DB System. Used for DNS.

The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\").

Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.""")
@cli_util.option('--ip-address', help=u"""The IP address the DB System is configured to listen on. A private IP address of your choice to assign to the primary endpoint of the DB System. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. This should be a \"dotted-quad\" style IPv4 address.""")
@cli_util.option('--port', type=click.INT, help=u"""The port for primary endpoint of the DB System to listen on.""")
@cli_util.option('--port-x', type=click.INT, help=u"""The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.""")
@cli_util.option('--backup-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--source', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--maintenance', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'backup-policy': {'module': 'mysql', 'class': 'CreateBackupPolicyDetails'}, 'source': {'module': 'mysql', 'class': 'CreateDbSystemSourceDetails'}, 'maintenance': {'module': 'mysql', 'class': 'CreateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-policy': {'module': 'mysql', 'class': 'CreateBackupPolicyDetails'}, 'source': {'module': 'mysql', 'class': 'CreateDbSystemSourceDetails'}, 'maintenance': {'module': 'mysql', 'class': 'CreateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'mysql', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def create_db_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, configuration_id, shape_name, subnet_id, admin_username, admin_password, display_name, description, availability_domain, fault_domain, mysql_version, data_storage_size_in_gbs, hostname_label, ip_address, port, port_x, backup_policy, source, maintenance, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['configurationId'] = configuration_id
    _details['shapeName'] = shape_name
    _details['subnetId'] = subnet_id
    _details['adminUsername'] = admin_username
    _details['adminPassword'] = admin_password

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if availability_domain is not None:
        _details['availabilityDomain'] = availability_domain

    if fault_domain is not None:
        _details['faultDomain'] = fault_domain

    if mysql_version is not None:
        _details['mysqlVersion'] = mysql_version

    if data_storage_size_in_gbs is not None:
        _details['dataStorageSizeInGBs'] = data_storage_size_in_gbs

    if hostname_label is not None:
        _details['hostnameLabel'] = hostname_label

    if ip_address is not None:
        _details['ipAddress'] = ip_address

    if port is not None:
        _details['port'] = port

    if port_x is not None:
        _details['portX'] = port_x

    if backup_policy is not None:
        _details['backupPolicy'] = cli_util.parse_json_parameter("backup_policy", backup_policy)

    if source is not None:
        _details['source'] = cli_util.parse_json_parameter("source", source)

    if maintenance is not None:
        _details['maintenance'] = cli_util.parse_json_parameter("maintenance", maintenance)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('mysql', 'db_system', ctx)
    result = client.create_db_system(
        create_db_system_details=_details,
        **kwargs
    )
    if wait_for_state:

        client = cli_util.build_client('mysql', 'work_requests', ctx)

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db_system.create_db_system_create_db_system_source_from_backup_details.command_name', 'create-db-system-create-db-system-source-from-backup-details'), help=u"""Creates and launches a DB System.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--configuration-id', required=True, help=u"""The OCID of the Configuration to be used for this DB System.""")
@cli_util.option('--shape-name', required=True, help=u"""The name of the shape. The shape determines the resources allocated - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. To get a list of shapes, use the [ListShapes] operation.""")
@cli_util.option('--subnet-id', required=True, help=u"""The OCID of the subnet the DB System is associated with.""")
@cli_util.option('--admin-username', required=True, help=u"""The username for the administrative user.""")
@cli_util.option('--admin-password', required=True, help=u"""The password for the administrative user. The password must be between 8 and 32 characters long, and must contain at least 1 numeric character, 1 lowercase character, 1 uppercase character, and 1 special (nonalphanumeric) character.""")
@cli_util.option('--source-backup-id', required=True, help=u"""The OCID of the backup to be used as the source for the new DB System.""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the DB System. It does not have to be unique.""")
@cli_util.option('--description', help=u"""User-provided data about the DB System.""")
@cli_util.option('--availability-domain', help=u"""The Availability Domain where the primary instance should be located.""")
@cli_util.option('--fault-domain', help=u"""The name of the Fault Domain the DB System is located in.""")
@cli_util.option('--mysql-version', help=u"""The specific MySQL version identifier.""")
@cli_util.option('--data-storage-size-in-gbs', type=click.INT, help=u"""Initial size of the data volume in GBs that will be created and attached. Keep in mind that this only specifies the size of the database data volume, the log volume for the database will be scaled appropriately with its shape.""")
@cli_util.option('--hostname-label', help=u"""The hostname for the primary endpoint of the DB System. Used for DNS.

The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\").

Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.""")
@cli_util.option('--ip-address', help=u"""The IP address the DB System is configured to listen on. A private IP address of your choice to assign to the primary endpoint of the DB System. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. This should be a \"dotted-quad\" style IPv4 address.""")
@cli_util.option('--port', type=click.INT, help=u"""The port for primary endpoint of the DB System to listen on.""")
@cli_util.option('--port-x', type=click.INT, help=u"""The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.""")
@cli_util.option('--backup-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--maintenance', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'backup-policy': {'module': 'mysql', 'class': 'CreateBackupPolicyDetails'}, 'maintenance': {'module': 'mysql', 'class': 'CreateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-policy': {'module': 'mysql', 'class': 'CreateBackupPolicyDetails'}, 'maintenance': {'module': 'mysql', 'class': 'CreateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'mysql', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def create_db_system_create_db_system_source_from_backup_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, configuration_id, shape_name, subnet_id, admin_username, admin_password, source_backup_id, display_name, description, availability_domain, fault_domain, mysql_version, data_storage_size_in_gbs, hostname_label, ip_address, port, port_x, backup_policy, maintenance, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['source'] = {}
    _details['compartmentId'] = compartment_id
    _details['configurationId'] = configuration_id
    _details['shapeName'] = shape_name
    _details['subnetId'] = subnet_id
    _details['adminUsername'] = admin_username
    _details['adminPassword'] = admin_password
    _details['source']['backupId'] = source_backup_id

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if availability_domain is not None:
        _details['availabilityDomain'] = availability_domain

    if fault_domain is not None:
        _details['faultDomain'] = fault_domain

    if mysql_version is not None:
        _details['mysqlVersion'] = mysql_version

    if data_storage_size_in_gbs is not None:
        _details['dataStorageSizeInGBs'] = data_storage_size_in_gbs

    if hostname_label is not None:
        _details['hostnameLabel'] = hostname_label

    if ip_address is not None:
        _details['ipAddress'] = ip_address

    if port is not None:
        _details['port'] = port

    if port_x is not None:
        _details['portX'] = port_x

    if backup_policy is not None:
        _details['backupPolicy'] = cli_util.parse_json_parameter("backup_policy", backup_policy)

    if maintenance is not None:
        _details['maintenance'] = cli_util.parse_json_parameter("maintenance", maintenance)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['source']['sourceType'] = 'BACKUP'

    client = cli_util.build_client('mysql', 'db_system', ctx)
    result = client.create_db_system(
        create_db_system_details=_details,
        **kwargs
    )
    if wait_for_state:

        client = cli_util.build_client('mysql', 'work_requests', ctx)

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db_system.create_db_system_create_db_system_source_import_from_url_details.command_name', 'create-db-system-create-db-system-source-import-from-url-details'), help=u"""Creates and launches a DB System.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--configuration-id', required=True, help=u"""The OCID of the Configuration to be used for this DB System.""")
@cli_util.option('--shape-name', required=True, help=u"""The name of the shape. The shape determines the resources allocated - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. To get a list of shapes, use the [ListShapes] operation.""")
@cli_util.option('--subnet-id', required=True, help=u"""The OCID of the subnet the DB System is associated with.""")
@cli_util.option('--admin-username', required=True, help=u"""The username for the administrative user.""")
@cli_util.option('--admin-password', required=True, help=u"""The password for the administrative user. The password must be between 8 and 32 characters long, and must contain at least 1 numeric character, 1 lowercase character, 1 uppercase character, and 1 special (nonalphanumeric) character.""")
@cli_util.option('--source-source-url', required=True, help=u"""The Pre-Authenticated Request (PAR) URL of the file you want to import from Object Storage.""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the DB System. It does not have to be unique.""")
@cli_util.option('--description', help=u"""User-provided data about the DB System.""")
@cli_util.option('--availability-domain', help=u"""The Availability Domain where the primary instance should be located.""")
@cli_util.option('--fault-domain', help=u"""The name of the Fault Domain the DB System is located in.""")
@cli_util.option('--mysql-version', help=u"""The specific MySQL version identifier.""")
@cli_util.option('--data-storage-size-in-gbs', type=click.INT, help=u"""Initial size of the data volume in GBs that will be created and attached. Keep in mind that this only specifies the size of the database data volume, the log volume for the database will be scaled appropriately with its shape.""")
@cli_util.option('--hostname-label', help=u"""The hostname for the primary endpoint of the DB System. Used for DNS.

The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\").

Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.""")
@cli_util.option('--ip-address', help=u"""The IP address the DB System is configured to listen on. A private IP address of your choice to assign to the primary endpoint of the DB System. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. This should be a \"dotted-quad\" style IPv4 address.""")
@cli_util.option('--port', type=click.INT, help=u"""The port for primary endpoint of the DB System to listen on.""")
@cli_util.option('--port-x', type=click.INT, help=u"""The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.""")
@cli_util.option('--backup-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--maintenance', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'backup-policy': {'module': 'mysql', 'class': 'CreateBackupPolicyDetails'}, 'maintenance': {'module': 'mysql', 'class': 'CreateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-policy': {'module': 'mysql', 'class': 'CreateBackupPolicyDetails'}, 'maintenance': {'module': 'mysql', 'class': 'CreateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'mysql', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def create_db_system_create_db_system_source_import_from_url_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, configuration_id, shape_name, subnet_id, admin_username, admin_password, source_source_url, display_name, description, availability_domain, fault_domain, mysql_version, data_storage_size_in_gbs, hostname_label, ip_address, port, port_x, backup_policy, maintenance, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['source'] = {}
    _details['compartmentId'] = compartment_id
    _details['configurationId'] = configuration_id
    _details['shapeName'] = shape_name
    _details['subnetId'] = subnet_id
    _details['adminUsername'] = admin_username
    _details['adminPassword'] = admin_password
    _details['source']['sourceUrl'] = source_source_url

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if availability_domain is not None:
        _details['availabilityDomain'] = availability_domain

    if fault_domain is not None:
        _details['faultDomain'] = fault_domain

    if mysql_version is not None:
        _details['mysqlVersion'] = mysql_version

    if data_storage_size_in_gbs is not None:
        _details['dataStorageSizeInGBs'] = data_storage_size_in_gbs

    if hostname_label is not None:
        _details['hostnameLabel'] = hostname_label

    if ip_address is not None:
        _details['ipAddress'] = ip_address

    if port is not None:
        _details['port'] = port

    if port_x is not None:
        _details['portX'] = port_x

    if backup_policy is not None:
        _details['backupPolicy'] = cli_util.parse_json_parameter("backup_policy", backup_policy)

    if maintenance is not None:
        _details['maintenance'] = cli_util.parse_json_parameter("maintenance", maintenance)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    _details['source']['sourceType'] = 'IMPORTURL'

    client = cli_util.build_client('mysql', 'db_system', ctx)
    result = client.create_db_system(
        create_db_system_details=_details,
        **kwargs
    )
    if wait_for_state:

        client = cli_util.build_client('mysql', 'work_requests', ctx)

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db_system.delete_db_system.command_name', 'delete'), help=u"""Delete a DB System, including terminating, detaching, removing, finalizing and otherwise deleting all related resources.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB System [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_db_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, if_match):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('mysql', 'db_system', ctx)
    result = client.delete_db_system(
        db_system_id=db_system_id,
        **kwargs
    )
    if wait_for_state:

        client = cli_util.build_client('mysql', 'work_requests', ctx)

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db_system.get_db_system.command_name', 'get'), help=u"""Get information about the specified DB System.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB System [OCID].""")
@cli_util.option('--if-none-match', help=u"""For conditional requests. In the GET call for a resource, set the `If-None-Match` header to the value of the ETag from a previous GET (or POST or PUT) response for that resource. The server will return with either a 304 Not Modified response if the resource has not changed, or a 200 OK response with the updated representation.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'mysql', 'class': 'DbSystem'})
@cli_util.wrap_exceptions
def get_db_system(ctx, from_json, db_system_id, if_none_match):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    kwargs = {}
    if if_none_match is not None:
        kwargs['if_none_match'] = if_none_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('mysql', 'db_system', ctx)
    result = client.get_db_system(
        db_system_id=db_system_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db_system.list_db_systems.command_name', 'list'), help=u"""Get a list of DB Systems in the specified compartment. The default sort order is by timeUpdated, descending.""")
@cli_util.option('--compartment-id', required=True, help=u"""The compartment [OCID].""")
@cli_util.option('--db-system-id', help=u"""The DB System [OCID].""")
@cli_util.option('--display-name', help=u"""A filter to return only the resource matching the given display name exactly.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]), help=u"""DbSystem Lifecycle State""")
@cli_util.option('--configuration-id', help=u"""The requested Configuration instance.""")
@cli_util.option('--is-up-to-date', type=click.BOOL, help=u"""Filter instances if they are using the latest revision of the Configuration they are associated with.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["displayName", "timeCreated"]), help=u"""The field to sort by. Only one sort order may be provided. Time fields are default ordered as descending. Display name is default ordered as ascending.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use (ASC or DESC).""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated list call. For information about pagination, see [List Pagination].""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` or `opc-prev-page` response header from the previous list call. For information about pagination, see [List Pagination].""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'mysql', 'class': 'list[DbSystemSummary]'})
@cli_util.wrap_exceptions
def list_db_systems(ctx, from_json, all_pages, page_size, compartment_id, db_system_id, display_name, lifecycle_state, configuration_id, is_up_to_date, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if db_system_id is not None:
        kwargs['db_system_id'] = db_system_id
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if configuration_id is not None:
        kwargs['configuration_id'] = configuration_id
    if is_up_to_date is not None:
        kwargs['is_up_to_date'] = is_up_to_date
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('mysql', 'db_system', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_systems,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_systems,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_db_systems(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db_system.restart_db_system.command_name', 'restart'), help=u"""Restarts the specified DB System.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB System [OCID].""")
@cli_util.option('--shutdown-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["IMMEDIATE", "FAST", "SLOW"]), help=u"""The InnoDB shutdown mode to use, following the option \"[innodb_fast_shutdown]\".""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def restart_db_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, shutdown_type, if_match):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['shutdownType'] = shutdown_type

    client = cli_util.build_client('mysql', 'db_system', ctx)
    result = client.restart_db_system(
        db_system_id=db_system_id,
        restart_db_system_details=_details,
        **kwargs
    )
    if wait_for_state:

        client = cli_util.build_client('mysql', 'work_requests', ctx)

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db_system.start_db_system.command_name', 'start'), help=u"""Start the specified DB System.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB System [OCID].""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def start_db_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, if_match):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('mysql', 'db_system', ctx)
    result = client.start_db_system(
        db_system_id=db_system_id,
        **kwargs
    )
    if wait_for_state:

        client = cli_util.build_client('mysql', 'work_requests', ctx)

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db_system.stop_db_system.command_name', 'stop'), help=u"""Stops the specified DB System.

A stopped DB System is not billed.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB System [OCID].""")
@cli_util.option('--shutdown-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["IMMEDIATE", "FAST", "SLOW"]), help=u"""The InnoDB shutdown mode to use, following the option \"[innodb_fast_shutdown]\".""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def stop_db_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, shutdown_type, if_match):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['shutdownType'] = shutdown_type

    client = cli_util.build_client('mysql', 'db_system', ctx)
    result = client.stop_db_system(
        db_system_id=db_system_id,
        stop_db_system_details=_details,
        **kwargs
    )
    if wait_for_state:

        client = cli_util.build_client('mysql', 'work_requests', ctx)

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@db_system_group.command(name=cli_util.override('db_system.update_db_system.command_name', 'update'), help=u"""Update the configuration of a DB System.

Updating different fields in the DB System will have different results on the uptime of the DB System. For example, changing the displayName of a DB System will take effect immediately, but changing the shape of a DB System is an asynchronous operation that involves provisioning new Compute resources, pausing the DB System and migrating storage before making the DB System available again.""")
@cli_util.option('--db-system-id', required=True, help=u"""The DB System [OCID].""")
@cli_util.option('--display-name', help=u"""The user-friendly name for the DB System. It does not have to be unique.""")
@cli_util.option('--description', help=u"""User-provided data about the DB System.""")
@cli_util.option('--subnet-id', help=u"""The OCID of the subnet the DB System is associated with.""")
@cli_util.option('--availability-domain', help=u"""The Availability Domain where the primary instance should be located.""")
@cli_util.option('--fault-domain', help=u"""The name of the Fault Domain the DB System is located in.""")
@cli_util.option('--shape-name', help=u"""The shape of the DB System. The shape determines resources allocated to the DB System - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes. To get a list of shapes, use the [ListShapes] operation.

Changes in Shape will result in a downtime as the MySQL DB System is migrated to the new Compute instance.""")
@cli_util.option('--mysql-version', help=u"""The specific MySQL version identifier.""")
@cli_util.option('--configuration-id', help=u"""The OCID of the Configuration to be used for Instances in this DB System.""")
@cli_util.option('--admin-username', help=u"""The username for the administrative user for the MySQL Instance.""")
@cli_util.option('--admin-password', help=u"""The password for the administrative user. The password must be between 8 and 32 characters long, and must contain at least 1 numeric character, 1 lowercase character, 1 uppercase character, and 1 special (nonalphanumeric) character.""")
@cli_util.option('--data-storage-size-in-gbs', type=click.INT, help=u"""New size of the data volume in GBs that will be created and attached.

Increases in data storage size will happen asynchronously and will require DB System downtime.

Decreases in data storage size are not supported.""")
@cli_util.option('--hostname-label', help=u"""The hostname for the primary endpoint of the DB System. Used for DNS. The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN) (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\"). Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.""")
@cli_util.option('--ip-address', help=u"""The IP address the DB System should be configured to listen on the provided subnet. It must be a free private IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet. This should be a \"dotted-quad\" style IPv4 address.""")
@cli_util.option('--port', type=click.INT, help=u"""The port for primary endpoint of the DB System to listen on.""")
@cli_util.option('--port-x', type=click.INT, help=u"""The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.""")
@cli_util.option('--backup-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--maintenance', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `If-Match` header to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'backup-policy': {'module': 'mysql', 'class': 'UpdateBackupPolicyDetails'}, 'maintenance': {'module': 'mysql', 'class': 'UpdateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'backup-policy': {'module': 'mysql', 'class': 'UpdateBackupPolicyDetails'}, 'maintenance': {'module': 'mysql', 'class': 'UpdateMaintenanceDetails'}, 'freeform-tags': {'module': 'mysql', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'mysql', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_db_system(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, db_system_id, display_name, description, subnet_id, availability_domain, fault_domain, shape_name, mysql_version, configuration_id, admin_username, admin_password, data_storage_size_in_gbs, hostname_label, ip_address, port, port_x, backup_policy, maintenance, freeform_tags, defined_tags, if_match):

    if isinstance(db_system_id, six.string_types) and len(db_system_id.strip()) == 0:
        raise click.UsageError('Parameter --db-system-id cannot be whitespace or empty string')
    if not force:
        if backup_policy or maintenance or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to backup-policy and maintenance and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
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

    if subnet_id is not None:
        _details['subnetId'] = subnet_id

    if availability_domain is not None:
        _details['availabilityDomain'] = availability_domain

    if fault_domain is not None:
        _details['faultDomain'] = fault_domain

    if shape_name is not None:
        _details['shapeName'] = shape_name

    if mysql_version is not None:
        _details['mysqlVersion'] = mysql_version

    if configuration_id is not None:
        _details['configurationId'] = configuration_id

    if admin_username is not None:
        _details['adminUsername'] = admin_username

    if admin_password is not None:
        _details['adminPassword'] = admin_password

    if data_storage_size_in_gbs is not None:
        _details['dataStorageSizeInGBs'] = data_storage_size_in_gbs

    if hostname_label is not None:
        _details['hostnameLabel'] = hostname_label

    if ip_address is not None:
        _details['ipAddress'] = ip_address

    if port is not None:
        _details['port'] = port

    if port_x is not None:
        _details['portX'] = port_x

    if backup_policy is not None:
        _details['backupPolicy'] = cli_util.parse_json_parameter("backup_policy", backup_policy)

    if maintenance is not None:
        _details['maintenance'] = cli_util.parse_json_parameter("maintenance", maintenance)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('mysql', 'db_system', ctx)
    result = client.update_db_system(
        db_system_id=db_system_id,
        update_db_system_details=_details,
        **kwargs
    )
    if wait_for_state:

        client = cli_util.build_client('mysql', 'work_requests', ctx)

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
