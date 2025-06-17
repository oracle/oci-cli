# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.apiaccesscontrol.src.oci_cli_privileged_api_requests.generated import privilegedapirequests_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Move commands under 'oci apiaccesscontrol privileged-api-requests privileged-api-request' -> 'oci apiaccesscontrol privileged-api-requests'
privilegedapirequests_cli.privileged_api_requests_root_group.commands.pop(privilegedapirequests_cli.privileged_api_request_group.name)
privilegedapirequests_cli.privileged_api_requests_root_group.add_command(privilegedapirequests_cli.approve_privileged_api_request)
privilegedapirequests_cli.privileged_api_requests_root_group.add_command(privilegedapirequests_cli.close_privileged_api_request)
privilegedapirequests_cli.privileged_api_requests_root_group.add_command(privilegedapirequests_cli.create_privileged_api_request)
privilegedapirequests_cli.privileged_api_requests_root_group.add_command(privilegedapirequests_cli.get_privileged_api_request)
privilegedapirequests_cli.privileged_api_requests_root_group.add_command(privilegedapirequests_cli.reject_privileged_api_request)
privilegedapirequests_cli.privileged_api_requests_root_group.add_command(privilegedapirequests_cli.revoke_privileged_api_request)


# Move commands under 'oci apiaccesscontrol privileged-api-requests privileged-api-request-collection' -> 'oci apiaccesscontrol privileged-api-requests'
privilegedapirequests_cli.privileged_api_requests_root_group.commands.pop(privilegedapirequests_cli.privileged_api_request_collection_group.name)
privilegedapirequests_cli.privileged_api_requests_root_group.add_command(privilegedapirequests_cli.list_privileged_api_requests)
