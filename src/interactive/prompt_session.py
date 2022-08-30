# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from prompt_toolkit import PromptSession
from prompt_toolkit.application import get_app
from prompt_toolkit.styles import Style
from prompt_toolkit.layout import Dimension, FormattedTextControl, Window
from interactive.commands_history import CommandsHistory
from interactive.error_messages import get_error_message

from interactive.utils import (
    styles_dict,
    INTERACTIVE_COMMANDS_HISTORY_FILE_NAME,
)


def create_oci_prompt_session(colors_enabled=True, bottom_toolbar=None):
    """
    Setup resources and create Oci Prompt Session
    """

    # Setup History
    cli_interactive_history = CommandsHistory(
        INTERACTIVE_COMMANDS_HISTORY_FILE_NAME
    )

    # Setup Style
    style = Style.from_dict(styles_dict)
    cli_command = [("class:oci", "> oci ")]

    # Create Session
    session = OciPromptSession(
        message=cli_command,
        style=style if colors_enabled else None,
        complete_while_typing=True,
        dynamic_size=True,  # Turn on dynamic sizing session
        min_space=4,  # bottom toolbar uses 3 additional rows
        max_space=20,  # Autocomplete menu does not show more than 16 items
        b_toolbar=bottom_toolbar,
        history=cli_interactive_history,
    )

    return session


class OciPromptSession(PromptSession):
    def __init__(
        self,
        b_toolbar=None,
        dynamic_size=False,
        min_space=0,
        max_space=0,
        *args,
        **kwargs
    ):
        super().__init__(bottom_toolbar=b_toolbar.show_toolbar, *args, **kwargs)

        # Setup Dynamic Sizing Window Variables
        # Set to 0 or False to turn off
        self.dynamic_size = dynamic_size
        self.min_space = max(min_space, 0)
        self.max_space = max(max_space, 0)

        # Save Bottom Toolbar variables & functions
        if b_toolbar:
            self.bottom_toolbar_size = b_toolbar.size
            self.bottom_toolbar_msg = b_toolbar.set_toolbar_text
            self.reserve_space_for_menu = max(self.min_space - self.bottom_toolbar_size, 0)
        else:
            self.bottom_toolbar_size = 0
            self.bottom_toolbar_msg = None
            self.reserve_space_for_menu = self.min_space

        # Update window too small error
        self.layout.container.window_too_small = Window(
            FormattedTextControl(
                text=[("class:window-too-small", get_error_message("terminal_too_small"))]
            )
        )

    def _get_default_buffer_control_height(self) -> Dimension:
        """
        Controls the Dimension height for prompt session and window_too_small error message handling
        """
        # Run parent's checks
        dimension = super()._get_default_buffer_control_height()

        # Compute largest possible window hieght
        height = get_app().output.get_size().rows - 1
        if not self.max_space:
            max_window_size = height
        else:
            max_window_size = min(self.max_space, height)
        max_window_size = max(max_window_size - self.bottom_toolbar_size, 0)

        # Set Window Height
        if self.dynamic_size and self.completer.completer.size and dimension.min:
            dimension.min = min(self.completer.completer.size + 1, max_window_size)

        # Window is too small for autocomplete menu to display
        if self.bottom_toolbar_msg and max_window_size <= 0:
            self.bottom_toolbar_msg(
                get_error_message("terminal_too_small"),
                is_error=True,
            )

        return dimension
