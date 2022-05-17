# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.application import get_app
from prompt_toolkit.layout.containers import ConditionalContainer, Window
from prompt_toolkit.layout.dimension import Dimension
from prompt_toolkit.filters import (
    is_done,
    renderer_height_is_known,
)
from prompt_toolkit.layout.controls import FormattedTextControl

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
        self._line_drawn = False  # The line between all the windows and the bottom toolbar needs to be drawn one time in the session
        self._toolbar_index = -1

    def _create_message_container(self):
        toolbar_message_container = ConditionalContainer(
            Window(
                FormattedTextControl(
                    self._toolbar_text,
                    style="class:bottom-toolbar.text"
                    if not self._is_error
                    else "class:bottom-toolbar.error.text",
                ),
                style="class:bottom-toolbar",
                dont_extend_height=True,
                height=Dimension(min=1),
            ),
            filter=~is_done & renderer_height_is_known,
        )
        return toolbar_message_container

    def _initialize_toolbar_message(self):
        """
        Since we add a new window for the message above the horizontal line in the bottom toolbar, this function needs
        to be called only once in the session, then after that we don't need to add a new window for the message,
        instead we update the existing window using the variable self._toolbar_index
        """
        h_split_children = get_app().layout.container.children
        toolbar_message_container = self._create_message_container()
        self._toolbar_index = len(h_split_children) - 1
        h_split_children.insert(self._toolbar_index, toolbar_message_container)

    def _add_toolbar_message_window(self):
        """
        This function adds the message above the horizontal line in the bottom toolbar

        :return:
        """
        if self._toolbar_index == -1:
            self._initialize_toolbar_message()
        message_container = self._create_message_container()
        get_app().layout.container.children[self._toolbar_index] = message_container

    def _add_line_before_shortcuts(self):
        if self._line_drawn:
            return
        """
        The terminal window has an object called HSplit (horizontal split), the is object contains multiple horizontal
        windows, the last window is the bottom toolbar, so in this function we read the list of windows and add one
        extra window which is the line before the toolbar.
        for example, the list of windows might have 5 windows, so add the new window just before the bottom toolbar
        window which makes the lenght of the list 6.
        """
        h_split_children = get_app().layout.container.children
        toolbar_line = ConditionalContainer(
            Window(char="-", style="class:bottom-toolbar.text", height=1),
            filter=~is_done,
        )
        toolbar_index = len(h_split_children) - 1
        h_split_children.insert(toolbar_index, toolbar_line)

        self._line_drawn = True

    def set_toolbar_text(self, toolbar_text, is_error=False):
        self._toolbar_text = toolbar_text
        self._is_error = is_error

    def show_toolbar(self):
        self._add_toolbar_message_window()  # This shows the message above the line
        self._add_line_before_shortcuts()  # This draws the line between the message and the shortcuts
        self._reset_toolbar_message()  # reset the message so the error can disappear in the next completions
        return HTML(
            SHORT_CUTS_TEXT
        )  # This returns the shortcuts which prompt toolkit show in the bottom toolbar

    def _reset_toolbar_message(self):
        self._is_error = False
        self._toolbar_text = ""
