# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.license_manager.src.oci_cli_license_manager.generated import licensemanager_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci license-manager license-record-collection list-license-records -> oci license-manager license-record-collection list
cli_util.rename_command(licensemanager_cli, licensemanager_cli.license_record_collection_group, licensemanager_cli.list_license_records, "list")


# oci license-manager bulk-upload-license-records-details bulk-upload-license-records -> oci license-manager bulk-upload-license-records-details import-licenses
cli_util.rename_command(licensemanager_cli, licensemanager_cli.bulk_upload_license_records_details_group, licensemanager_cli.bulk_upload_license_records, "import-licenses")


# oci license-manager product-license-collection list-product-licenses -> oci license-manager product-license-collection list
cli_util.rename_command(licensemanager_cli, licensemanager_cli.product_license_collection_group, licensemanager_cli.list_product_licenses, "list")


# oci license-manager license-record-collection list-license-records -> oci license-manager license-record
licensemanager_cli.license_record_collection_group.commands.pop(licensemanager_cli.list_license_records.name)
licensemanager_cli.license_record_group.add_command(licensemanager_cli.list_license_records)


# oci license-manager bulk-upload-license-records-details bulk-upload-license-records -> oci license-manager license-record
licensemanager_cli.bulk_upload_license_records_details_group.commands.pop(licensemanager_cli.bulk_upload_license_records.name)
licensemanager_cli.license_record_group.add_command(licensemanager_cli.bulk_upload_license_records)


# oci license-manager product-license-collection list-product-licenses -> oci license-manager product-license
licensemanager_cli.product_license_collection_group.commands.pop(licensemanager_cli.list_product_licenses.name)
licensemanager_cli.product_license_group.add_command(licensemanager_cli.list_product_licenses)


# oci license-manager product-license-consumer-collection list-product-license-consumers -> oci license-manager product-license
licensemanager_cli.product_license_consumer_collection_group.commands.pop(licensemanager_cli.list_product_license_consumers.name)
licensemanager_cli.product_license_group.add_command(licensemanager_cli.list_product_license_consumers)


# oci license-manager top-utilized-product-license-collection list-top-utilized-product-licenses -> oci license-manager product-license
licensemanager_cli.top_utilized_product_license_collection_group.commands.pop(licensemanager_cli.list_top_utilized_product_licenses.name)
licensemanager_cli.product_license_group.add_command(licensemanager_cli.list_top_utilized_product_licenses)


# oci license-manager top-utilized-resource-collection list-top-utilized-resources -> oci license-manager product-license
licensemanager_cli.top_utilized_resource_collection_group.commands.pop(licensemanager_cli.list_top_utilized_resources.name)
licensemanager_cli.product_license_group.add_command(licensemanager_cli.list_top_utilized_resources)


# Remove bulk-upload-license-records-details from oci license-manager
licensemanager_cli.license_manager_root_group.commands.pop(licensemanager_cli.bulk_upload_license_records_details_group.name)


# Remove license-record-collection from oci license-manager
licensemanager_cli.license_manager_root_group.commands.pop(licensemanager_cli.license_record_collection_group.name)


# Remove product-license-collection from oci license-manager
licensemanager_cli.license_manager_root_group.commands.pop(licensemanager_cli.product_license_collection_group.name)


# Remove product-license-consumer-collection from oci license-manager
licensemanager_cli.license_manager_root_group.commands.pop(licensemanager_cli.product_license_consumer_collection_group.name)


# Remove top-utilized-product-license-collection from oci license-manager
licensemanager_cli.license_manager_root_group.commands.pop(licensemanager_cli.top_utilized_product_license_collection_group.name)


# Remove top-utilized-resource-collection from oci license-manager
licensemanager_cli.license_manager_root_group.commands.pop(licensemanager_cli.top_utilized_resource_collection_group.name)
