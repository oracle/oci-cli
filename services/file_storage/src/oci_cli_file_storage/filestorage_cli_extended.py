# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci_cli import cli_util
from services.file_storage.src.oci_cli_file_storage.generated import filestorage_cli
from services.file_storage.src.oci_cli_file_storage.generated.filestorage_cli import outbound_connector_group


# Remove auto-generated parent create command from the CLI and
# rename command "create-outbound-connector-create-ldap-bind-account-details".
filestorage_cli.outbound_connector_group.commands.pop(filestorage_cli.create_outbound_connector.name)

cli_util.rename_command(filestorage_cli, outbound_connector_group, filestorage_cli.create_outbound_connector_create_ldap_bind_account_details, "create_ldap_bind_connector")
