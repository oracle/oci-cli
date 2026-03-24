# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.generative_ai_data.src.oci_cli_generate_enrichment_job.generated import generateenrichmentjob_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Remove generate-enrichment-job-delta-refresh-enrichment-job-configuration from oci generative-ai-data generate-enrichment-job enrichment-job
generateenrichmentjob_cli.enrichment_job_group.commands.pop(generateenrichmentjob_cli.generate_enrichment_job_delta_refresh_enrichment_job_configuration.name)


# Remove generate-enrichment-job-full-build-enrichment-job-configuration from oci generative-ai-data generate-enrichment-job enrichment-job
generateenrichmentjob_cli.enrichment_job_group.commands.pop(generateenrichmentjob_cli.generate_enrichment_job_full_build_enrichment_job_configuration.name)


# Remove generate-enrichment-job-partial-build-enrichment-job-configuration from oci generative-ai-data generate-enrichment-job enrichment-job
generateenrichmentjob_cli.enrichment_job_group.commands.pop(generateenrichmentjob_cli.generate_enrichment_job_partial_build_enrichment_job_configuration.name)
