# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.application import get_app

SHORT_CUTS_TEXT = "[Tab/Enter] Autocomplete/Execute command   [Ctrl + D] Quit"


class BottomToolbar:
    """
    This class is for designing the bottom toolbar of the CLI Interactive.
    the method show_toolbar() is being called from the prompt toolkit whenever the user presses any key.
    The method set_toolbar_text() is being called whenever the caller needs to show a message in the bottom toolbar,
    this message can be error message, success message or any other message. if error message, then the parameter
    is_error need to be set to True this way the color of the text will indicate that this is an error message
    """

    def __init__(self):
        self._toolbar_text = ""
        self._is_error = False
        self.size = 3

    def _add_toolbar_message_window(self):
        """
        This function adds the message above the horizontal line in the bottom toolbar

        :return: (string, string)
        """
        if self._is_error:
            return "class:bottom-toolbar.error.text", self._toolbar_text
        else:
            return "class:bottom-toolbar.text", self._toolbar_text

    def _add_line_before_shortcuts(self) -> str:
        """
        This function adds a horizontal line in the bottom toolbar above shortcuts

        :return: string
        """
        return get_app().output.get_size().columns * '-'

    def _reset_toolbar_message(self):
        self._toolbar_text = ""
        self._is_error = False

    def set_toolbar_text(self, toolbar_text, is_error=False):
        self._toolbar_text = toolbar_text
        self._is_error = is_error

    def show_toolbar(self) -> FormattedText:
        """
        This function defines toolbar display

        :return: FormattedText
        """
        toolbar_style, toolbar_msg = self._add_toolbar_message_window()  # This shows the message above the line
        dash_line = self._add_line_before_shortcuts()  # This draws the line between the message and the shortcuts
        self._reset_toolbar_message()  # reset the message so the error can disappear in the next completions

        message = FormattedText([
            (toolbar_style, toolbar_msg + '\n'),
            ('', dash_line + '\n'),
            ('', SHORT_CUTS_TEXT)
        ])
        return message  # This returns the shortcuts which prompt toolkit show in the bottom toolbar
