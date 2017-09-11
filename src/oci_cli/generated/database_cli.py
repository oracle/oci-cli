# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
from ..cli_root import cli
from .. import cli_util


@cli.group(cli_util.override('db_group.command_name', 'db'), help=cli_util.override('db_group.help', """The API for the Database Service."""))
@cli_util.help_option_group
def db_group():
    pass


@click.group(cli_util.override('db_version_group.command_name', 'db-version'), help="""The Oracle database software version.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def db_version_group():
    pass


@click.group(cli_util.override('database_group.command_name', 'database'), help="""An Oracle database on a DB System. For more information, see [Managing Oracle Databases].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def database_group():
    pass


@click.group(cli_util.override('db_system_shape_group.command_name', 'db-system-shape'), help="""The shape of the DB System. The shape determines the CPU cores, storage, and memory allocated to the DB System.
For a description of shapes, see [DB System Launch Options].
To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator.
If you're an administrator who needs to write policies to give users access,
see [Getting Started with Policies].""")
@cli_util.help_option_group
def db_system_shape_group():
    pass


@click.group(cli_util.override('db_home_group.command_name', 'db-home'), help="""A directory where Oracle database software is installed. Each DB System can have multiple database homes,
and each database home can have multiple databases within it. All the databases within a single database home
must be the same database version, but different database homes can run different versions. For more information,
see [Managing Oracle Databases].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an
administrator. If you're an administrator who needs to write policies to give users access,
see [Getting Started with Policies].""")
@cli_util.help_option_group
def db_home_group():
    pass


@click.group(cli_util.override('db_system_group.command_name', 'db-system'), help="""The Database Service supports several types of DB Systems, ranging in size, price, and performance. For details about each type of system, see:

- [Exadata DB Systems]
- [Bare Metal DB Systems]

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].

For information about access control and compartments, see
[Overview of the Identity Service].

For information about Availability Domains, see
[Regions and Availability Domains].

To get a list of Availability Domains, use the `ListAvailabilityDomains` operation
in the Identity Service API.""")
@cli_util.help_option_group
def db_system_group():
    pass


@click.group(cli_util.override('db_node_group.command_name', 'db-node'), help="""A server where Oracle database software is running.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def db_node_group():
    pass


@db_home_group.command(name=cli_util.override('create_db_home.command_name', 'create'), help="""Creates a new DB Home in the specified DB System based on the request parameters you provide.""")
@click.option('--database', required=True, help="""""")
@click.option('--db-system-id', required=True, help="""The OCID of the DB System.""")
@click.option('--db-version', required=True, help="""A valid Oracle database version. To get a list of supported versions, use the [ListDbVersions] operation.""")
@click.option('--display-name', help="""The user-provided name of the database home.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def create_db_home(ctx, database, db_system_id, db_version, display_name):
    kwargs = {}

    details = {}
    details['database'] = cli_util.parse_json_parameter("database", database)
    details['dbSystemId'] = db_system_id
    details['dbVersion'] = db_version

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('database', ctx)
    result = client.create_db_home(
        create_db_home_with_db_system_id_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@db_node_group.command(name=cli_util.override('db_node_action.command_name', 'db-node-action'), help="""Performs an action, such as one of the power actions (start, stop, softreset, or reset), on the specified DB Node.

**start** - power on

**stop** - power off

**softreset** - ACPI shutdown and power on

**reset** - power off and power on

Note that the **stop** state has no effect on the resources you consume. Billing continues for DB Nodes that you stop, and related resources continue to apply against any relevant quotas. You must terminate the DB System ([TerminateDbSystem]) to remove its resources from billing and quotas.""")
@click.option('--db-node-id', required=True, help="""The database node OCID.""")
@click.option('--action', required=True, help="""The action to perform on the DB Node.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def db_node_action(ctx, db_node_id, action, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.db_node_action(
        db_node_id=db_node_id,
        action=action,
        **kwargs
    )
    cli_util.render_response(result)


@db_home_group.command(name=cli_util.override('delete_db_home.command_name', 'delete'), help="""Deletes a DB Home. The DB Home and its database data are local to the DB System and will be lost when it is deleted. Oracle recommends that you back up any data in the DB System prior to deleting it.""")
@click.option('--db-home-id', required=True, help="""The database home OCID.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def delete_db_home(ctx, db_home_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.delete_db_home(
        db_home_id=db_home_id,
        **kwargs
    )
    cli_util.render_response(result)


@database_group.command(name=cli_util.override('get_database.command_name', 'get'), help="""Gets information about a specific database.""")
@click.option('--database-id', required=True, help="""The database OCID.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_database(ctx, database_id):
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_database(
        database_id=database_id,
        **kwargs
    )
    cli_util.render_response(result)


@db_home_group.command(name=cli_util.override('get_db_home.command_name', 'get'), help="""Gets information about the specified database home.""")
@click.option('--db-home-id', required=True, help="""The database home OCID.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_db_home(ctx, db_home_id):
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_home(
        db_home_id=db_home_id,
        **kwargs
    )
    cli_util.render_response(result)


@db_node_group.command(name=cli_util.override('get_db_node.command_name', 'get'), help="""Gets information about the specified database node.""")
@click.option('--db-node-id', required=True, help="""The database node OCID.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_db_node(ctx, db_node_id):
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_node(
        db_node_id=db_node_id,
        **kwargs
    )
    cli_util.render_response(result)


@db_system_group.command(name=cli_util.override('get_db_system.command_name', 'get'), help="""Gets information about the specified DB System.""")
@click.option('--db-system-id', required=True, help="""The DB System OCID.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def get_db_system(ctx, db_system_id):
    kwargs = {}
    client = cli_util.build_client('database', ctx)
    result = client.get_db_system(
        db_system_id=db_system_id,
        **kwargs
    )
    cli_util.render_response(result)


@db_system_group.command(name=cli_util.override('launch_db_system.command_name', 'launch'), help="""Launches a new DB System in the specified compartment and Availability Domain. You'll specify a single Oracle Database Edition that applies to all the databases on that DB System. The selected edition cannot be changed.

An initial database is created on the DB System based on the request parameters you provide and some default options. For more information, see [Default Options for the Initial Database].

The DB System will include a command line interface (CLI) that you can use to create additional databases and manage existing databases. For more information, see the [Oracle Database CLI Reference].""")
@click.option('--availability-domain', required=True, help="""The Availability Domain where the DB System is located.""")
@click.option('--compartment-id', required=True, help="""The Oracle Cloud ID (OCID) of the compartment the DB System  belongs in.""")
@click.option('--cpu-core-count', required=True, help="""The number of CPU cores to enable. The valid values depend on the specified shape:

- BM.DenseIO1.36 and BM.HighIO1.36 - Specify a multiple of 2, from 2 to 36. - BM.RACLocalStorage1.72 - Specify a multiple of 4, from 4 to 72. - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84. - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168. - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336.""")
@click.option('--database-edition', required=True, help="""The Oracle Database Edition that applies to all the databases on the DB System.

Exadata DB Systems and 2-node RAC DB Systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.""")
@click.option('--db-home', required=True, help="""""")
@click.option('--hostname', required=True, help="""The host name for the DB System. The host name must begin with an alphabetic character and can contain a maximum of 30 alphanumeric characters, including hyphens (-).

The maximum length of the combined hostname and domain is 63 characters.

**Note:** The hostname must be unique within the subnet. If it is not unique, the DB System will fail to provision.""")
@click.option('--shape', required=True, help="""The shape of the DB System. The shape determines the CPU cores, storage, and memory allocated to the DB System. To get a list of shapes, use the [ListDbSystemShapes] operation.""")
@click.option('--ssh-public-keys', required=True, help="""The public key portion of the key pair to use for SSH access to the DB System. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.""")
@click.option('--subnet-id', required=True, help="""The OCID of the subnet the DB System is associated with.

**Subnet Restrictions:** - For 1- and 2-node RAC DB Systems, do not use a subnet that overlaps with 192.168.16.16/28 - For Exadata DB Systems, do not use a subnet that overlaps with 192.168.128.0/20

These subnets are used by the Oracle Clusterware private interconnect on the database instance. Specifying an overlapping subnet will cause the private interconnect to malfunction. This restriction applies to both the client subnet and backup subnet.""")
@click.option('--backup-subnet-id', help="""The OCID of the backup network subnet the DB System is associated with. Applicable only to Exadata.

**Subnet Restrictions:** See above subnetId's **Subnet Restriction**.""")
@click.option('--cluster-name', help="""Cluster name for Exadata and 2-node RAC DB Systems. The cluster name must begin with an an alphabetic character, and may contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.""")
@click.option('--data-storage-percentage', help="""The percentage assigned to DATA storage (user data and database files). The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Specify 80 or 40. The default is 80 percent assigned to DATA storage.""")
@click.option('--disk-redundancy', help="""The type of redundancy configured for the DB System. Normal is 2-way redundancy, recommended for test and development systems. High is 3-way redundancy, recommended for production systems.""")
@click.option('--display-name', help="""The user-friendly name for the DB System. It does not have to be unique.""")
@click.option('--domain', help="""A domain name used for the DB System. If the Oracle-provided Internet and VCN Resolver is enabled for the specified subnet, the domain name for the subnet is used (don't provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def launch_db_system(ctx, availability_domain, compartment_id, cpu_core_count, database_edition, db_home, hostname, shape, ssh_public_keys, subnet_id, backup_subnet_id, cluster_name, data_storage_percentage, disk_redundancy, display_name, domain):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id
    details['cpuCoreCount'] = cpu_core_count
    details['databaseEdition'] = database_edition
    details['dbHome'] = cli_util.parse_json_parameter("db_home", db_home)
    details['hostname'] = hostname
    details['shape'] = shape
    details['sshPublicKeys'] = cli_util.parse_json_parameter("ssh_public_keys", ssh_public_keys)
    details['subnetId'] = subnet_id

    if backup_subnet_id is not None:
        details['backupSubnetId'] = backup_subnet_id

    if cluster_name is not None:
        details['clusterName'] = cluster_name

    if data_storage_percentage is not None:
        details['dataStoragePercentage'] = data_storage_percentage

    if disk_redundancy is not None:
        details['diskRedundancy'] = disk_redundancy

    if display_name is not None:
        details['displayName'] = display_name

    if domain is not None:
        details['domain'] = domain

    client = cli_util.build_client('database', ctx)
    result = client.launch_db_system(
        launch_db_system_details=details,
        **kwargs
    )
    cli_util.render_response(result)


@database_group.command(name=cli_util.override('list_databases.command_name', 'list'), help="""Gets a list of the databases in the specified database home.""")
@click.option('--compartment-id', required=True, help="""The compartment OCID.""")
@click.option('--db-home-id', required=True, help="""A database home OCID.""")
@click.option('--limit', help="""The maximum number of items to return.""")
@click.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_databases(ctx, compartment_id, db_home_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    result = client.list_databases(
        compartment_id=compartment_id,
        db_home_id=db_home_id,
        **kwargs
    )
    cli_util.render_response(result)


@db_home_group.command(name=cli_util.override('list_db_homes.command_name', 'list'), help="""Gets a list of database homes in the specified DB System and compartment. A database home is a directory where Oracle database software is installed.""")
@click.option('--compartment-id', required=True, help="""The compartment OCID.""")
@click.option('--db-system-id', required=True, help="""The OCID of the DB System.""")
@click.option('--limit', help="""The maximum number of items to return.""")
@click.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_db_homes(ctx, compartment_id, db_system_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    result = client.list_db_homes(
        compartment_id=compartment_id,
        db_system_id=db_system_id,
        **kwargs
    )
    cli_util.render_response(result)


@db_node_group.command(name=cli_util.override('list_db_nodes.command_name', 'list'), help="""Gets a list of database nodes in the specified DB System and compartment. A database node is a server running database software.""")
@click.option('--compartment-id', required=True, help="""The compartment OCID.""")
@click.option('--db-system-id', required=True, help="""The OCID of the DB System.""")
@click.option('--limit', help="""The maximum number of items to return.""")
@click.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_db_nodes(ctx, compartment_id, db_system_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    result = client.list_db_nodes(
        compartment_id=compartment_id,
        db_system_id=db_system_id,
        **kwargs
    )
    cli_util.render_response(result)


@db_system_shape_group.command(name=cli_util.override('list_db_system_shapes.command_name', 'list'), help="""Gets a list of the shapes that can be used to launch a new DB System. The shape determines the CPU cores, storage, and memory allocated to the DB System.""")
@click.option('--availability-domain', required=True, help="""The name of the Availability Domain.""")
@click.option('--compartment-id', required=True, help="""The compartment OCID.""")
@click.option('--limit', help="""The maximum number of items to return.""")
@click.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_db_system_shapes(ctx, availability_domain, compartment_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    result = client.list_db_system_shapes(
        availability_domain=availability_domain,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@db_system_group.command(name=cli_util.override('list_db_systems.command_name', 'list'), help="""Gets a list of the DB Systems in the specified compartment.""")
@click.option('--compartment-id', required=True, help="""The compartment OCID.""")
@click.option('--limit', help="""The maximum number of items to return.""")
@click.option('--page', help="""The pagination token to continue listing from.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_db_systems(ctx, compartment_id, limit, page):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    client = cli_util.build_client('database', ctx)
    result = client.list_db_systems(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@db_version_group.command(name=cli_util.override('list_db_versions.command_name', 'list'), help="""Gets a list of supported Oracle database versions.""")
@click.option('--compartment-id', required=True, help="""The compartment OCID.""")
@click.option('--limit', help="""The maximum number of items to return.""")
@click.option('--page', help="""The pagination token to continue listing from.""")
@click.option('--db-system-shape', help="""If provided, filters the results to the set of database versions which are supported for the given shape.""")
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def list_db_versions(ctx, compartment_id, limit, page, db_system_shape):
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if db_system_shape is not None:
        kwargs['db_system_shape'] = db_system_shape
    client = cli_util.build_client('database', ctx)
    result = client.list_db_versions(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result)


@db_system_group.command(name=cli_util.override('terminate_db_system.command_name', 'terminate'), help="""Terminates a DB System and permanently deletes it and any databases running on it. The database data is local to the DB System and will be lost when the system is terminated. Oracle recommends that you back up any data in the DB System prior to terminating it.""")
@click.option('--db-system-id', required=True, help="""The DB System OCID.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def terminate_db_system(ctx, db_system_id, if_match):
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('database', ctx)
    result = client.terminate_db_system(
        db_system_id=db_system_id,
        **kwargs
    )
    cli_util.render_response(result)


@db_system_group.command(name=cli_util.override('update_db_system.command_name', 'update'), help="""Updates the properties of a DB System, such as the CPU core count.""")
@click.option('--db-system-id', required=True, help="""The DB System OCID.""")
@click.option('--cpu-core-count', help="""The number of CPU Cores to be set on the DB System""")
@click.option('--ssh-public-keys', help="""The public key portion of the key pair to use for SSH access to the DB System. Multiple public keys can be provided. The length of the combined keys cannot exceed 10,000 characters.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def update_db_system(ctx, force, db_system_id, cpu_core_count, ssh_public_keys, if_match):
    if not force:
        if ssh_public_keys:
            if not click.confirm("WARNING: Updates to ssh-public-keys will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if cpu_core_count is not None:
        details['cpuCoreCount'] = cpu_core_count

    if ssh_public_keys is not None:
        details['sshPublicKeys'] = cli_util.parse_json_parameter("ssh_public_keys", ssh_public_keys)

    client = cli_util.build_client('database', ctx)
    result = client.update_db_system(
        db_system_id=db_system_id,
        update_db_system_details=details,
        **kwargs
    )
    cli_util.render_response(result)
