# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates. All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
CLI commands for managing the completion cache.

This module provides commands to:
- View cache status
- Clear the cache
- Configure cache TTL
"""

import click
import json
from interactive.enhanced_completions import (
    OCIDCache,
    clear_completion_cache,
    clear_expired_cache,
    get_cache_info
)


@click.group('completion-cache', help='Manage the OCI CLI completion cache for faster autocompletion')
@click.pass_context
def completion_cache_group(ctx):
    """Commands for managing the completion cache."""
    pass


@completion_cache_group.command('status', help='Show current cache status and statistics')
@click.pass_context
def cache_status(ctx):
    """Display information about the completion cache."""
    info = get_cache_info()

    click.echo("Completion Cache Status")
    click.echo("=" * 50)
    click.echo(f"Cache Directory: {info['cache_directory']}")
    click.echo(f"Total Cache Files: {info['total_files']}")
    click.echo(f"Valid Cache Files: {info['valid_files']}")
    click.echo(f"Expired Cache Files: {info['expired_files']}")
    click.echo(f"Total Cache Size: {info['total_size_bytes'] / 1024:.2f} KB")
    click.echo(f"Cache TTL: {info['ttl_hours']} hours")

    if info['valid_files'] > 0:
        click.echo("\nCache is active and contains valid entries.")
    else:
        click.echo("\nCache is empty or all entries are expired.")


@completion_cache_group.command('clear', help='Clear all cached completion data')
@click.option('--expired-only', is_flag=True, help='Clear only expired cache entries')
@click.option('--force', '-f', is_flag=True, help='Skip confirmation prompt')
@click.pass_context
def cache_clear(ctx, expired_only, force):
    """Clear the completion cache."""
    if expired_only:
        clear_expired_cache()
        click.echo("Expired cache entries cleared successfully.")
    else:
        if not force:
            if not click.confirm("This will clear all cached completion data. Continue?"):
                click.echo("Cache clear cancelled.")
                return

        clear_completion_cache()
        click.echo("All completion cache cleared successfully.")


@completion_cache_group.command('refresh', help='Refresh compartment cache by fetching latest data')
@click.pass_context
def cache_refresh(ctx):
    """Force refresh the compartment cache."""
    from oci_cli import cli_util

    try:
        # Clear existing compartment cache
        cache = OCIDCache()
        profile = ctx.obj.get('profile', 'DEFAULT')
        region = ctx.obj.get('region', 'us-phoenix-1')
        cache_key = f"compartments_profile_{profile}_region_{region}"

        # Clear specific cache entry
        cache_file = cache._get_cache_file(cache_key)
        if cache_file.exists():
            cache_file.unlink()

        click.echo("Fetching fresh compartment data...")

        # Import and use the compartment completer to refresh
        from interactive.enhanced_completions import CompartmentCompleter
        completer = CompartmentCompleter(ctx)
        compartments = completer._fetch_compartments()

        if compartments:
            cache.set(cache_key, compartments)
            click.echo(f"Successfully cached {len(compartments)} compartments.")
        else:
            click.echo("Warning: No compartments found or error occurred.")

    except Exception as e:
        click.echo(f"Error refreshing compartment cache: {e}")
        ctx.exit(1)


def add_cache_commands(cli):
    """Add cache management commands to the CLI."""
    cli.add_command(completion_cache_group)