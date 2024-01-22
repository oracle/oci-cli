# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.generative_ai_inference.src.oci_cli_generative_ai_inference.generated import generativeaiinference_cli


# generativeaiinference_cli.generate_text_result_group.commands.pop(generativeaiinference_cli.generate_text_llama_llm_inference_request.name)
# generativeaiinference_cli.generate_text_result_group.commands.pop(generativeaiinference_cli.generate_text_cohere_llm_inference_request.name)
# Remove oci generative-ai-inference generate-text-result
generativeaiinference_cli.generative_ai_inference_root_group.commands.pop(generativeaiinference_cli.generate_text_result_group.name)
