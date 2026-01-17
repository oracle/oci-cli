# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates. All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
Enhanced completion module for OCI CLI with caching support for compartments and OCIDs.

This module provides:
1. Caching of compartment listings from 'oci iam compartment list'
2. Smart completion for --compartment-id parameters
3. Persistent cache storage for frequently used OCIDs
4. Time-based cache invalidation
"""

import json
import os
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from prompt_toolkit.completion import Completion
from oci_cli import cli_util
from interactive.error_messages import get_error_message
import hashlib


class OCIDCache:
    """
    Manages a persistent cache for OCIDs to speed up autocompletion.
    """

    CACHE_DIR = os.path.join(os.path.expanduser("~"), ".oci", "completion_cache")
    CACHE_TTL_HOURS = 24  # Default cache validity period

    def __init__(self, cache_ttl_hours: int = 24):
        """
        Initialize the OCID cache.

        Args:
            cache_ttl_hours: Number of hours before cache expires
        """
        self.cache_dir = Path(self.CACHE_DIR)
        self.cache_ttl = timedelta(hours=cache_ttl_hours)
        self._ensure_cache_dir()

    def _ensure_cache_dir(self):
        """Create cache directory if it doesn't exist."""
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_cache_file(self, cache_key: str) -> Path:
        """Get the cache file path for a given key."""
        # Use hash to ensure valid filename
        hashed_key = hashlib.md5(cache_key.encode()).hexdigest()
        return self.cache_dir / f"{hashed_key}.json"

    def _is_cache_valid(self, cache_file: Path) -> bool:
        """Check if cache file is still valid based on TTL."""
        if not cache_file.exists():
            return False

        modified_time = datetime.fromtimestamp(cache_file.stat().st_mtime)
        return datetime.now() - modified_time < self.cache_ttl

    def get(self, cache_key: str) -> Optional[List[Dict[str, Any]]]:
        """
        Retrieve cached data if available and valid.

        Args:
            cache_key: Unique identifier for the cached data

        Returns:
            Cached data if valid, None otherwise
        """
        cache_file = self._get_cache_file(cache_key)

        if not self._is_cache_valid(cache_file):
            return None

        try:
            with open(cache_file, 'r') as f:
                data = json.load(f)
                return data.get('items', [])
        except (json.JSONDecodeError, IOError):
            # Invalid cache file, remove it
            cache_file.unlink(missing_ok=True)
            return None

    def set(self, cache_key: str, items: List[Dict[str, Any]]):
        """
        Store data in cache.

        Args:
            cache_key: Unique identifier for the cached data
            items: List of items to cache
        """
        cache_file = self._get_cache_file(cache_key)

        try:
            cache_data = {
                'timestamp': datetime.now().isoformat(),
                'items': items
            }
            with open(cache_file, 'w') as f:
                json.dump(cache_data, f, indent=2)
        except IOError:
            # Silently fail if we can't write cache
            pass

    def clear(self):
        """Clear all cached data."""
        for cache_file in self.cache_dir.glob("*.json"):
            cache_file.unlink(missing_ok=True)

    def clear_expired(self):
        """Remove only expired cache files."""
        for cache_file in self.cache_dir.glob("*.json"):
            if not self._is_cache_valid(cache_file):
                cache_file.unlink(missing_ok=True)


class CompartmentCompleter:
    """
    Provides compartment-aware completion for OCI CLI.
    """

    def __init__(self, ctx, cache_ttl_hours: int = 24):
        """
        Initialize the compartment completer.

        Args:
            ctx: Click context object
            cache_ttl_hours: Hours before cache expires
        """
        self.ctx = ctx
        self.cache = OCIDCache(cache_ttl_hours)

    def _get_profile_key(self) -> str:
        """Generate a unique key based on the current OCI profile."""
        profile = self.ctx.obj.get('profile', 'DEFAULT')
        region = self.ctx.obj.get('region', 'us-phoenix-1')
        return f"profile_{profile}_region_{region}"

    def _fetch_compartments(self) -> List[Dict[str, Any]]:
        """
        Fetch compartments from OCI API.

        Returns:
            List of compartment dictionaries
        """
        try:
            identity_client = cli_util.build_client("identity", "identity", self.ctx)
            tenancy_id = cli_util.get_tenancy_from_config(self.ctx)

            # Get all compartments in tenancy
            compartments = []

            # Add root compartment (tenancy)
            root_compartment = identity_client.get_compartment(compartment_id=tenancy_id)
            compartments.append({
                'id': root_compartment.data.id,
                'name': root_compartment.data.name,
                'description': root_compartment.data.description or "Root compartment",
                'lifecycle_state': root_compartment.data.lifecycle_state,
                'is_root': True
            })

            # List all child compartments
            response = identity_client.list_compartments(
                compartment_id=tenancy_id,
                compartment_id_in_subtree=True,
                lifecycle_state='ACTIVE',
                limit=1000
            )

            for compartment in response.data:
                compartments.append({
                    'id': compartment.id,
                    'name': compartment.name,
                    'description': compartment.description or "",
                    'lifecycle_state': compartment.lifecycle_state,
                    'is_root': False
                })

            return compartments
        except Exception as e:
            # Log error but don't crash
            print(f"Warning: Could not fetch compartments: {e}")
            return []

    def get_compartment_completions(
        self,
        word_before_cursor: str,
        bottom_toolbar=None,
        sub_string: str = ""
    ) -> List[Completion]:
        """
        Get compartment completions with caching support.

        Args:
            word_before_cursor: Current partial input
            bottom_toolbar: Optional toolbar for error messages
            sub_string: Substring to filter compartments

        Returns:
            List of Completion objects
        """
        cache_key = f"compartments_{self._get_profile_key()}"

        # Try to get from cache first
        compartments = self.cache.get(cache_key)

        if compartments is None:
            # Cache miss, fetch from API
            if bottom_toolbar:
                bottom_toolbar.set_toolbar_text("Fetching compartments...", is_error=False)

            compartments = self._fetch_compartments()

            if compartments:
                # Store in cache
                self.cache.set(cache_key, compartments)
            elif bottom_toolbar:
                bottom_toolbar.set_toolbar_text(
                    get_error_message("no_items_found"),
                    is_error=True
                )
                return []

        # Filter and create completions
        completions = []
        for compartment in compartments:
            # Filter by substring if provided
            if sub_string and sub_string.lower() not in compartment['name'].lower():
                continue

            # Create display text with additional info
            display_text = compartment['name']
            if compartment.get('is_root'):
                display_text += " (root)"
            if compartment.get('description'):
                display_text += f" - {compartment['description'][:50]}"

            completions.append(
                Completion(
                    compartment['id'],
                    -len(word_before_cursor),
                    display=display_text
                )
            )

        return completions


def get_enhanced_oci_resources(
    ctx,
    param_name: str,
    word_before_cursor: str,
    bottom_toolbar=None,
    sub_string: str = ""
) -> List[Completion]:
    """
    Enhanced resource completion with caching support.

    This function extends the existing get_oci_resources with:
    1. Compartment caching for --compartment-id
    2. Smarter filtering and sorting
    3. Better error handling

    Args:
        ctx: Click context
        param_name: Parameter name (e.g., '--compartment-id')
        word_before_cursor: Current partial input
        bottom_toolbar: Optional toolbar for status messages
        sub_string: Substring filter

    Returns:
        List of Completion objects
    """
    # Handle compartment-id specially with caching
    if param_name in ['--compartment-id', '-c']:
        completer = CompartmentCompleter(ctx)
        return completer.get_compartment_completions(
            word_before_cursor,
            bottom_toolbar,
            sub_string
        )

    # For other resources, fall back to the original implementation
    # Import here to avoid circular dependency
    from interactive.oci_resources_completions import get_oci_resources
    return get_oci_resources(ctx, param_name, word_before_cursor, bottom_toolbar, sub_string)


def clear_completion_cache():
    """
    Clear all cached completion data.

    This can be called when the user wants to force a refresh.
    """
    cache = OCIDCache()
    cache.clear()
    print("Completion cache cleared successfully.")


def clear_expired_cache():
    """
    Clear only expired cache entries.

    This should be called periodically to clean up old data.
    """
    cache = OCIDCache()
    cache.clear_expired()


# Additional helper functions for integration with existing CLI

def setup_enhanced_completions():
    """
    Setup enhanced completions by patching the existing completion system.

    This function should be called during CLI initialization.
    """
    # Import and patch the existing module
    import interactive.oci_resources_completions as orig_module

    # Save original function
    if not hasattr(orig_module, '_original_get_oci_resources'):
        orig_module._original_get_oci_resources = orig_module.get_oci_resources

    # Replace with enhanced version
    orig_module.get_oci_resources = get_enhanced_oci_resources

    print("Enhanced completions with caching enabled.")


def get_cache_info() -> Dict[str, Any]:
    """
    Get information about the current cache state.

    Returns:
        Dictionary with cache statistics
    """
    cache = OCIDCache()
    cache_files = list(cache.cache_dir.glob("*.json"))

    total_size = sum(f.stat().st_size for f in cache_files)
    valid_count = sum(1 for f in cache_files if cache._is_cache_valid(f))

    return {
        'cache_directory': str(cache.cache_dir),
        'total_files': len(cache_files),
        'valid_files': valid_count,
        'expired_files': len(cache_files) - valid_count,
        'total_size_bytes': total_size,
        'ttl_hours': cache.cache_ttl.total_seconds() / 3600
    }