# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates. All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://apache.org/licenses/LICENSE-2.0. You may choose either license.

import re

import click


_LIST_ITEM = re.compile(r'^[ \t]*(?:[-*+]|\d+[.)])[ \t]+')


def _split_at_list_boundaries(text):
    if '\b' in text or '\n' not in text:
        return [text]

    lines = text.split('\n')
    sections = []
    current_section = [lines[0]]

    for index in range(1, len(lines)):
        previous_line = lines[index - 1]
        next_line = lines[index]
        is_part_of_newline_sequence = (
            (index > 1 and previous_line == '')
            or (index < len(lines) - 1 and next_line == ''))

        if (
                not is_part_of_newline_sequence
                and (
                    _LIST_ITEM.match(previous_line)
                    or _LIST_ITEM.match(next_line))):
            sections.append('\n'.join(current_section))
            current_section = [next_line]
        else:
            current_section.append(next_line)

    sections.append('\n'.join(current_section))
    return sections


class OciHelpFormatter(click.HelpFormatter):
    """Click help formatter that retains newlines around list items."""

    def write_text(self, text):
        for section in _split_at_list_boundaries(text):
            super().write_text(section)

    def write_dl(self, rows, col_max=30, col_spacing=2):
        rows = list(rows)
        if any(len(row) != 2 for row in rows):
            return super().write_dl(
                rows, col_max=col_max, col_spacing=col_spacing
            )

        expanded_rows = []
        contains_list_boundary = False
        for first, second in rows:
            sections = _split_at_list_boundaries(second)
            expanded_rows.append((first, sections[0]))
            if len(sections) > 1:
                contains_list_boundary = True
                expanded_rows.extend(
                    ('', section) for section in sections[1:]
                )

        if not contains_list_boundary:
            expanded_rows = rows

        return super().write_dl(
            expanded_rows, col_max=col_max, col_spacing=col_spacing
        )


class OciHelpContext(click.Context):
    """Click context that creates OCI CLI help formatters."""

    formatter_class = OciHelpFormatter


class OciCommand(click.Command):
    """Click command that uses OCI CLI help formatting."""

    context_class = OciHelpContext


class OciGroup(click.Group):
    """Click group that creates formatter-aware commands and groups."""

    context_class = OciHelpContext
    command_class = OciCommand
    # Click treats ``type`` as a sentinel for ``type(self)`` so nested groups
    # retain the formatter-aware class, including for OciGroup subclasses.
    group_class = type
