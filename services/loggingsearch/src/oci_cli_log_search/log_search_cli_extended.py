# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.loggingsearch.src.oci_cli_log_search.generated import logsearch_cli

# oci loggingsearch search-result search-logs -> oci loggingsearch search-logs
logsearch_cli.logging_search_root_group.commands.pop(logsearch_cli.search_result_group.name)
logsearch_cli.logging_search_root_group.add_command(logsearch_cli.search_logs)
