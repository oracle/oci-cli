# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import click
import sys


class CommandGroupWithAlias(click.Group):
    def get_command(self, ctx, cmd_name):
        command_chain = self.get_command_chain(ctx)

        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            if cmd_name in ctx.obj['global_command_alias']:
                # An alias existed with this cmd_name but it matched a pre-defined name exactly, so we discard the alias
                click.echo(
                    click.style(
                        "Could not use '{}' as an alias for '{}' as it belongs to an existing command under '{}'".format(cmd_name, ctx.obj['global_command_alias'][cmd_name], command_chain),
                        fg='red'
                    ),
                    file=sys.stderr
                )
            elif command_chain in ctx.obj['command_sequence_alias']:
                if cmd_name in ctx.obj['command_sequence_alias'][command_chain]:
                    # An alias existed with this cmd_name in this command chain, but it matched a pre-defined name exactly, so we discard the alias
                    click.echo(
                        click.style(
                            "Could not use '{}' as an alias for '{}' as it belongs to an existing command under '{}'".format(cmd_name, ctx.obj['command_sequence_alias'][command_chain][cmd_name], command_chain),
                            fg='red'
                        ),
                        file=sys.stderr
                    )

            return rv

        if command_chain in ctx.obj['command_sequence_alias']:
            if cmd_name in ctx.obj['command_sequence_alias'][command_chain]:
                rv = click.Group.get_command(self, ctx, ctx.obj['command_sequence_alias'][command_chain][cmd_name])
                if rv is not None:
                    return rv

        if cmd_name in ctx.obj['global_command_alias']:
            rv = click.Group.get_command(self, ctx, ctx.obj['global_command_alias'][cmd_name])
            if rv is not None:
                return rv

        return None

    def get_command_chain(self, ctx):
        ordered_command_chain = []

        parent = ctx.parent
        while parent is not None:
            if parent.parent is not None:
                ordered_command_chain.append(parent.command.name)

            parent = parent.parent

        # This gives us a path from the child up to the parent, so reverse it to go parent to child as
        # we key that way (i.e. 'compute image export' rather than 'export image compute')
        ordered_command_chain.reverse()
        ordered_command_chain.append(ctx.command.name)

        return ' '.join(ordered_command_chain)
