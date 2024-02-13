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


@cli_util.copy_params_from_generated_command(generativeaiinference_cli.generate_text_cohere_llm_inference_request, params_to_exclude=['inference_request_is_stream'])
@generativeaiinference_cli.generate_text_result_group.command(name='generate-text-cohere-llm-inference-request', help=generativeaiinference_cli.generate_text_cohere_llm_inference_request.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'serving-mode': {'module': 'generative_ai_inference', 'class': 'ServingMode'}, 'inference-request-stop-sequences': {'module': 'generative_ai_inference', 'class': 'list[string]'}}, output_type={'module': 'generative_ai_inference', 'class': 'GenerateTextResult'})
@cli_util.wrap_exceptions
def generate_text_cohere_llm_inference_request_extended(ctx, **kwargs):

    kwargs['inference_request_is_stream'] = False

    ctx.invoke(generativeaiinference_cli.generate_text_cohere_llm_inference_request, **kwargs)


@cli_util.copy_params_from_generated_command(generativeaiinference_cli.generate_text_llama_llm_inference_request, params_to_exclude=['inference_request_is_stream'])
@generativeaiinference_cli.generate_text_result_group.command(name='generate-text-llama-llm-inference-request', help=generativeaiinference_cli.generate_text_llama_llm_inference_request.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'serving-mode': {'module': 'generative_ai_inference', 'class': 'ServingMode'}, 'inference-request-stop': {'module': 'generative_ai_inference', 'class': 'list[string]'}}, output_type={'module': 'generative_ai_inference', 'class': 'GenerateTextResult'})
@cli_util.wrap_exceptions
def generate_text_llama_llm_inference_request_extended(ctx, **kwargs):

    kwargs['inference_request_is_stream'] = False

    ctx.invoke(generativeaiinference_cli.generate_text_llama_llm_inference_request, **kwargs)
