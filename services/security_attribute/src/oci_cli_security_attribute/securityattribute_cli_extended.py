# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.security_attribute.src.oci_cli_security_attribute.generated import securityattribute_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci security-attribute security-attribute-namespace cascading-delete -> oci security-attribute security-attribute-namespace cascade-delete
cli_util.rename_command(securityattribute_cli, securityattribute_cli.security_attribute_namespace_group, securityattribute_cli.cascading_delete_security_attribute_namespace, "cascade-delete")


# oci security-attribute security-attribute-work-request -> oci security-attribute work-request
cli_util.rename_command(securityattribute_cli, securityattribute_cli.security_attribute_root_group, securityattribute_cli.security_attribute_work_request_group, "work-request")


# oci security-attribute security-attribute-work-request-error list -> oci security-attribute work-request list-errors
cli_util.rename_command(securityattribute_cli, securityattribute_cli.security_attribute_work_request_error_group, securityattribute_cli.list_security_attribute_work_request_errors, "list-errors")
securityattribute_cli.security_attribute_work_request_error_group.commands.pop(securityattribute_cli.list_security_attribute_work_request_errors.name)
securityattribute_cli.security_attribute_work_request_group.add_command(securityattribute_cli.list_security_attribute_work_request_errors)
securityattribute_cli.security_attribute_root_group.commands.pop(securityattribute_cli.security_attribute_work_request_error_group.name)


# oci security-attribute security-attribute-work-request-log list -> oci security-attribute work-request list-logs
cli_util.rename_command(securityattribute_cli, securityattribute_cli.security_attribute_work_request_log_group, securityattribute_cli.list_security_attribute_work_request_logs, "list-logs")
securityattribute_cli.security_attribute_work_request_log_group.commands.pop(securityattribute_cli.list_security_attribute_work_request_logs.name)
securityattribute_cli.security_attribute_work_request_group.add_command(securityattribute_cli.list_security_attribute_work_request_logs)
securityattribute_cli.security_attribute_root_group.commands.pop(securityattribute_cli.security_attribute_work_request_log_group.name)


# Remove create-security-attribute-default-security-attribute-validator from oci security-attribute security-attribute
securityattribute_cli.security_attribute_group.commands.pop(securityattribute_cli.create_security_attribute_default_security_attribute_validator.name)


# Remove create-security-attribute-enum-security-attribute-validator from oci security-attribute security-attribute
securityattribute_cli.security_attribute_group.commands.pop(securityattribute_cli.create_security_attribute_enum_security_attribute_validator.name)


# Remove update-security-attribute-default-security-attribute-validator from oci security-attribute security-attribute
securityattribute_cli.security_attribute_group.commands.pop(securityattribute_cli.update_security_attribute_default_security_attribute_validator.name)


# Remove update-security-attribute-enum-security-attribute-validator from oci security-attribute security-attribute
securityattribute_cli.security_attribute_group.commands.pop(securityattribute_cli.update_security_attribute_enum_security_attribute_validator.name)
