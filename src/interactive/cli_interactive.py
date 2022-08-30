# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci_cli import cli_util
from prompt_toolkit.document import Document
from prompt_toolkit.completion import ThreadedCompleter
from interactive.bottom_toolbar import BottomToolbar
from interactive.oci_shell_completer import OciShellCompleter
from interactive.utils import (
    AUTHENTICATION_PARAMS,
    AUTO_PROMPT_PARAMS,
    DEBUG_PARAMS,
    OCI_CLI_DISABLE_COLORS_ENV_VAR,
)

from interactive.key_bindings import override_key_binding
from interactive.prompt_session import create_oci_prompt_session
import os
import sys


def start_interactive_shell(ctx):

    # Getting the commands before --cli-auto-prompt, for example if the user execute oci --profile X compute instance --cli-auto-prompt,
    # then the interactive mode will begin with oci --profile X compute instance
    arguments = sys.argv[1:]

    auth_params = []
    for param in AUTHENTICATION_PARAMS:
        if param in arguments:
            param_idx = arguments.index(param)
            auth_params += arguments[param_idx: param_idx + 2]
            del arguments[param_idx: param_idx + 2]

    debug_params = []
    for param in DEBUG_PARAMS:
        if param in arguments:
            param_idx = arguments.index(param)
            debug_params += [arguments[param_idx]]
            del arguments[param_idx]

    command_before_prompt = " ".join(
        [arg for arg in arguments if arg not in AUTO_PROMPT_PARAMS]
    )

    # save the endpoint to be used for the actual command invocation
    endpoint = ctx.obj["endpoint"]
    ctx.obj["endpoint"] = None

    # Initialize the document with the initial commands typed by the user
    document = Document(command_before_prompt, len(command_before_prompt))
    # Build the config before invoking the prompt session to raise any errors due to incorrect config
    cli_util.create_config_and_signer_based_on_click_context(ctx)

    colors_enabled = True
    if OCI_CLI_DISABLE_COLORS_ENV_VAR in os.environ:
        colors_enabled = False

    # Build Prompt
    toolbar = BottomToolbar()
    session = create_oci_prompt_session(colors_enabled, toolbar)
    completer = OciShellCompleter(ctx, colors_enabled, bottom_toolbar=toolbar)
    kb = override_key_binding(completer=completer, toolbar=toolbar)
    multithread_completer = ThreadedCompleter(
        completer
    )  # This is needed for oci resources suggestion to not block the user until the result comes

    # Get Command
    text = session.prompt(
        completer=multithread_completer, default=document, key_bindings=kb
    )
    endpoint_str = " --endpoint " + endpoint if endpoint else ""
    os.environ[cli_util.OCI_CLI_IN_INTERACTIVE_MODE] = "True"  # This is needed so that the API request adds new user agent for the CLI Interactive
    command = (
        "oci "
        + " ".join(auth_params)
        + " "
        + " ".join(debug_params)
        + endpoint_str
        + " "
        + text if text else ""
    )

    # Execute Command
    os.system(command)
