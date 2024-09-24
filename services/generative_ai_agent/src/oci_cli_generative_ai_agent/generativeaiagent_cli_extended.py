# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.generative_ai_agent.src.oci_cli_generative_ai_agent.generated import generativeaiagent_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# oci generative-ai-agent data-ingestion-job get-data-ingestion-job-log-content -> oci generative-ai-agent data-ingestion-job get-log-content
cli_util.rename_command(generativeaiagent_cli, generativeaiagent_cli.data_ingestion_job_group, generativeaiagent_cli.get_data_ingestion_job_log_content, "get-log-content")


# oci generative-ai-agent data-source create-data-source-oci-object-storage-data-source-config -> oci generative-ai-agent data-source create-object-storage-ds
cli_util.rename_command(generativeaiagent_cli, generativeaiagent_cli.data_source_group, generativeaiagent_cli.create_data_source_oci_object_storage_data_source_config, "create-object-storage-ds")


# oci generative-ai-agent data-source update-data-source-oci-object-storage-data-source-config -> oci generative-ai-agent data-source update-object-storage-ds
cli_util.rename_command(generativeaiagent_cli, generativeaiagent_cli.data_source_group, generativeaiagent_cli.update_data_source_oci_object_storage_data_source_config, "update-object-storage-ds")


# oci generative-ai-agent knowledge-base create-knowledge-base-default-index-config -> oci generative-ai-agent knowledge-base create-default-kb
cli_util.rename_command(generativeaiagent_cli, generativeaiagent_cli.knowledge_base_group, generativeaiagent_cli.create_knowledge_base_default_index_config, "create-default-kb")


# oci generative-ai-agent knowledge-base create-knowledge-base-oci-database-config -> oci generative-ai-agent knowledge-base create-oci-database-kb
cli_util.rename_command(generativeaiagent_cli, generativeaiagent_cli.knowledge_base_group, generativeaiagent_cli.create_knowledge_base_oci_database_config, "create-oci-database-kb")


# oci generative-ai-agent knowledge-base create-knowledge-base-oci-open-search-index-config -> oci generative-ai-agent knowledge-base create-oci-open-search-kb
cli_util.rename_command(generativeaiagent_cli, generativeaiagent_cli.knowledge_base_group, generativeaiagent_cli.create_knowledge_base_oci_open_search_index_config, "create-oci-open-search-kb")


# oci generative-ai-agent knowledge-base update-knowledge-base-oci-database-config -> oci generative-ai-agent knowledge-base update-oci-database-kb
cli_util.rename_command(generativeaiagent_cli, generativeaiagent_cli.knowledge_base_group, generativeaiagent_cli.update_knowledge_base_oci_database_config, "update-oci-database-kb")


# oci generative-ai-agent knowledge-base update-knowledge-base-oci-open-search-index-config -> oci generative-ai-agent knowledge-base update-oci-open-search-kb
cli_util.rename_command(generativeaiagent_cli, generativeaiagent_cli.knowledge_base_group, generativeaiagent_cli.update_knowledge_base_oci_open_search_index_config, "update-oci-open-search-kb")


# oci generative-ai-agent work-request-log-entry list-work-request-logs -> oci generative-ai-agent work-request-log-entry list-logs
cli_util.rename_command(generativeaiagent_cli, generativeaiagent_cli.work_request_log_entry_group, generativeaiagent_cli.list_work_request_logs, "list-logs")


# Remove update_knowledge_base_default_index_config from oci generative-ai-agent knowledge-base
generativeaiagent_cli.knowledge_base_group.commands.pop(generativeaiagent_cli.update_knowledge_base_default_index_config.name)
