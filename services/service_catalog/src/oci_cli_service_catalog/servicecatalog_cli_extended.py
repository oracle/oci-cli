# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.service_catalog.src.oci_cli_service_catalog.generated import servicecatalog_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci service-catalog private-application create-private-application-create-private-application-stack-package -> oci service-catalog private-application create-with-stack-package
cli_util.rename_command(servicecatalog_cli, servicecatalog_cli.private_application_group, servicecatalog_cli.create_private_application_create_private_application_stack_package, "create-with-stack-package")


# oci service-catalog private-application get-private-application-action-download-logo -> oci service-catalog private-application download-logo
cli_util.rename_command(servicecatalog_cli, servicecatalog_cli.private_application_group, servicecatalog_cli.get_private_application_action_download_logo, "download-logo")


# oci service-catalog private-application-package get-private-application-package-action-download-config -> oci service-catalog private-application-package download-config
cli_util.rename_command(servicecatalog_cli, servicecatalog_cli.private_application_package_group, servicecatalog_cli.get_private_application_package_action_download_config, "download-config")


@cli_util.copy_params_from_generated_command(servicecatalog_cli.delete_service_catalog_association, params_to_exclude=['service_catalog_association_id'])
@servicecatalog_cli.service_catalog_association_group.command(name=servicecatalog_cli.delete_service_catalog_association.name, help=servicecatalog_cli.delete_service_catalog_association.help)
@cli_util.option('--association-id', required=True, help=u"""The unique identifier of the service catalog association. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_service_catalog_association_extended(ctx, **kwargs):
    if 'association_id' in kwargs:
        kwargs['service_catalog_association_id'] = kwargs['association_id']
        kwargs.pop('association_id')

    ctx.invoke(servicecatalog_cli.delete_service_catalog_association, **kwargs)


@cli_util.copy_params_from_generated_command(servicecatalog_cli.get_service_catalog_association, params_to_exclude=['service_catalog_association_id'])
@servicecatalog_cli.service_catalog_association_group.command(name=servicecatalog_cli.get_service_catalog_association.name, help=servicecatalog_cli.get_service_catalog_association.help)
@cli_util.option('--association-id', required=True, help=u"""The unique identifier of the service catalog association. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'ServiceCatalogAssociation'})
@cli_util.wrap_exceptions
def get_service_catalog_association_extended(ctx, **kwargs):
    if 'association_id' in kwargs:
        kwargs['service_catalog_association_id'] = kwargs['association_id']
        kwargs.pop('association_id')

    ctx.invoke(servicecatalog_cli.get_service_catalog_association, **kwargs)


@cli_util.copy_params_from_generated_command(servicecatalog_cli.list_service_catalog_associations, params_to_exclude=['service_catalog_association_id'])
@servicecatalog_cli.service_catalog_association_group.command(name=servicecatalog_cli.list_service_catalog_associations.name, help=servicecatalog_cli.list_service_catalog_associations.help)
@cli_util.option('--association-id', help=u"""The unique identifier for the service catalog association.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'ServiceCatalogAssociationCollection'})
@cli_util.wrap_exceptions
def list_service_catalog_associations_extended(ctx, **kwargs):
    if 'association_id' in kwargs:
        kwargs['service_catalog_association_id'] = kwargs['association_id']
        kwargs.pop('association_id')

    ctx.invoke(servicecatalog_cli.list_service_catalog_associations, **kwargs)


@cli_util.copy_params_from_generated_command(servicecatalog_cli.get_private_application_package, params_to_exclude=['private_application_package_id'])
@servicecatalog_cli.private_application_package_group.command(name=servicecatalog_cli.get_private_application_package.name, help=servicecatalog_cli.get_private_application_package.help)
@cli_util.option('--package-id', required=True, help=u"""The unique identifier for the private application package. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'PrivateApplicationPackage'})
@cli_util.wrap_exceptions
def get_private_application_package_extended(ctx, **kwargs):
    if 'package_id' in kwargs:
        kwargs['private_application_package_id'] = kwargs['package_id']
        kwargs.pop('package_id')

    ctx.invoke(servicecatalog_cli.get_private_application_package, **kwargs)


@cli_util.copy_params_from_generated_command(servicecatalog_cli.get_private_application_package_action_download_config, params_to_exclude=['private_application_package_id'])
@servicecatalog_cli.private_application_package_group.command(name=servicecatalog_cli.get_private_application_package_action_download_config.name, help=servicecatalog_cli.get_private_application_package_action_download_config.help)
@cli_util.option('--package-id', required=True, help=u"""The unique identifier for the private application package. [required]""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_private_application_package_action_download_config_extended(ctx, **kwargs):
    if 'package_id' in kwargs:
        kwargs['private_application_package_id'] = kwargs['package_id']
        kwargs.pop('package_id')

    ctx.invoke(servicecatalog_cli.get_private_application_package_action_download_config, **kwargs)


@cli_util.copy_params_from_generated_command(servicecatalog_cli.list_private_application_packages, params_to_exclude=['private_application_package_id'])
@servicecatalog_cli.private_application_package_group.command(name=servicecatalog_cli.list_private_application_packages.name, help=servicecatalog_cli.list_private_application_packages.help)
@cli_util.option('--package-id', help=u"""The unique identifier for the private application package.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'service_catalog', 'class': 'PrivateApplicationPackageCollection'})
@cli_util.wrap_exceptions
def list_private_application_packages_extended(ctx, **kwargs):
    if 'package_id' in kwargs:
        kwargs['private_application_package_id'] = kwargs['package_id']
        kwargs.pop('package_id')

    ctx.invoke(servicecatalog_cli.list_private_application_packages, **kwargs)
