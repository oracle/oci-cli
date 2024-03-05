# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401
from services.generative_ai_inference.src.oci_cli_generative_ai_inference.generated import generativeaiinference_cli

# Remove oci generative-ai-inference deprecated commands:
# GenerateText API: generate_text, generate_text_on_demand_serving_mode, generate_text_dedicated_serving_mode
generativeaiinference_cli.generate_text_result_group.commands.pop(generativeaiinference_cli.generate_text.name)
generativeaiinference_cli.generate_text_result_group.commands.pop(generativeaiinference_cli.generate_text_on_demand_serving_mode.name)
generativeaiinference_cli.generate_text_result_group.commands.pop(generativeaiinference_cli.generate_text_dedicated_serving_mode.name)
# SummarizeText API: summarize_text_on_demand_serving_mode, summarize_text_dedicated_serving_mode
generativeaiinference_cli.summarize_text_result_group.commands.pop(generativeaiinference_cli.summarize_text_on_demand_serving_mode.name)
generativeaiinference_cli.summarize_text_result_group.commands.pop(generativeaiinference_cli.summarize_text_dedicated_serving_mode.name)
# EmbedText API: embed_text_on_demand_serving_mode, embed_text_dedicated_serving_mode
generativeaiinference_cli.embed_text_result_group.commands.pop(generativeaiinference_cli.embed_text_on_demand_serving_mode.name)
generativeaiinference_cli.embed_text_result_group.commands.pop(generativeaiinference_cli.embed_text_dedicated_serving_mode.name)
