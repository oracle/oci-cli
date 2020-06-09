# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from subprocess import Popen, PIPE

import contextlib
import os
import os.path
import signal
import sys


def render_help_text(ctx, command_chain=[]):
    if not command_chain:
        command_chain = _get_command_chain(ctx)

    if sys.platform == 'win32':
        _render_help_windows(ctx, command_chain)

    # We need groff to format our man page text, so if it doesn't exist then fall back to click help
    if _exists_on_path('groff'):
        _render_help_posix_with_groff(ctx, command_chain)


def _render_help_windows(ctx, command_chain):
    current_file = os.path.realpath(__file__)
    current_dir = os.path.dirname(current_file)

    man_page_folder = os.path.join(current_dir, 'data_files', 'text', 'cmdref')
    command_chain[-1] = '{}.txt'.format(command_chain[-1])

    target_man_page = os.path.join(man_page_folder, *command_chain)
    if os.path.exists(target_man_page):
        p = Popen(['more'], stdin=PIPE, shell=True)
        with open(target_man_page, 'rb') as f:
            man_page_content = f.read()
        p.communicate(input=man_page_content)

        ctx.exit()


def _render_help_posix_with_groff(ctx, command_chain):
    current_file = os.path.realpath(__file__)
    current_dir = os.path.dirname(current_file)

    man_page_folder = os.path.join(current_dir, 'data_files', 'man')
    target_man_page = os.path.join(man_page_folder, '{}.1'.format('_'.join(command_chain)))

    if os.path.exists(target_man_page):
        groff_converter_cmd = ['groff', '-m', 'man', '-T', 'ascii', '-rHY=0']

        p3 = Popen(groff_converter_cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        with open(target_man_page, 'rb') as f:
            groff_output = p3.communicate(input=f.read())[0]

        if not _exists_on_path('less'):
            ctx.echo(groff_output)
        else:
            # We need to ignore the keyboard interrupt so we don't kill less and render the user's terminal unusable
            with _ignore_ctrl_c():
                p = Popen(['less', '-R'], stdin=PIPE)
                p.communicate(input=groff_output)

        ctx.exit()


def _get_command_chain(ctx):
    # This will eventually hold the call chain like: ['compute', 'image', 'export', 'to-object']
    ordered_command_chain = []

    parent = ctx.parent
    while parent is not None:
        if parent.parent is not None:
            ordered_command_chain.append(parent.info_name)

        parent = parent.parent

    # At this point we have the chain (without the command that was actually invoked) but in the reverse
    # order like: ['export', 'image', 'compute'] so we want to reverse it and then put in the
    # name of the command which was actually invoked to give us the chain in the right order. We also
    # need to append the command name
    ordered_command_chain.reverse()
    ordered_command_chain.append(ctx.info_name)

    return ordered_command_chain


def _exists_on_path(name):
    return any([os.path.exists(os.path.join(p, name)) for p in os.environ.get('PATH', '').split(os.pathsep)])


@contextlib.contextmanager
def _ignore_ctrl_c():
    original = signal.signal(signal.SIGINT, signal.SIG_IGN)
    try:
        yield
    finally:
        signal.signal(signal.SIGINT, original)
