# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.vn_monitoring.src.oci_cli_vn_monitoring.generated import vnmonitoring_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci vn-monitoring path-analysis-work-request-result -> oci vn-monitoring path-analysis
cli_util.rename_command(vnmonitoring_cli, vnmonitoring_cli.vn_monitoring_root_group, vnmonitoring_cli.path_analysis_work_request_result_group, "path-analysis")


# oci vn-monitoring work-request-log-entry -> oci vn-monitoring work-request-log
cli_util.rename_command(vnmonitoring_cli, vnmonitoring_cli.vn_monitoring_root_group, vnmonitoring_cli.work_request_log_entry_group, "work-request-log")


# oci vn-monitoring path-analysis-work-request-result get-path-analysis-adhoc-get-path-analysis-details -> oci vn-monitoring path-analysis-work-request-result get-path-analysis-adhoc
cli_util.rename_command(vnmonitoring_cli, vnmonitoring_cli.path_analysis_work_request_result_group, vnmonitoring_cli.get_path_analysis_adhoc_get_path_analysis_details, "get-path-analysis-adhoc")


# oci vn-monitoring path-analysis-work-request-result get-path-analysis-persisted-get-path-analysis-details -> oci vn-monitoring path-analysis-work-request-result get-path-analysis-persisted
cli_util.rename_command(vnmonitoring_cli, vnmonitoring_cli.path_analysis_work_request_result_group, vnmonitoring_cli.get_path_analysis_persisted_get_path_analysis_details, "get-path-analysis-persisted")


# oci vn-monitoring work-request-log-entry list-work-request-logs -> oci vn-monitoring work-request-log-entry list
cli_util.rename_command(vnmonitoring_cli, vnmonitoring_cli.work_request_log_entry_group, vnmonitoring_cli.list_work_request_logs, "list")


# oci vn-monitoring path-analyzer-test-collection list-path-analyzer-tests -> oci vn-monitoring path-analyzer-test-collection list
cli_util.rename_command(vnmonitoring_cli, vnmonitoring_cli.path_analyzer_test_collection_group, vnmonitoring_cli.list_path_analyzer_tests, "list")


# Remove get-path-analysis from oci vn-monitoring path-analysis-work-request-result
vnmonitoring_cli.path_analysis_work_request_result_group.commands.pop(vnmonitoring_cli.get_path_analysis.name)


# Move commands under 'oci vn-monitoring path-analyzer-test-collection' -> 'oci vn-monitoring path-analyzer-test'
vnmonitoring_cli.vn_monitoring_root_group.commands.pop(vnmonitoring_cli.path_analyzer_test_collection_group.name)
vnmonitoring_cli.path_analyzer_test_group.add_command(vnmonitoring_cli.list_path_analyzer_tests)
