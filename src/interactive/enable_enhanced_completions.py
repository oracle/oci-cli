# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates. All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
Enable enhanced completions with caching in the OCI CLI.

This module patches the existing completion system to add caching support.
"""

import os
from pathlib import Path

def enable_enhanced_completions():
    """
    Enable enhanced completions by modifying the existing completion imports.

    This function should be called early in the CLI initialization.
    """
    try:
        # Import both modules
        import interactive.oci_resources_completions as orig_module
        from interactive.enhanced_completions import get_enhanced_oci_resources

        # Save original function if not already saved
        if not hasattr(orig_module, '_original_get_oci_resources'):
            orig_module._original_get_oci_resources = orig_module.get_oci_resources

        # Replace with enhanced version
        orig_module.get_oci_resources = get_enhanced_oci_resources

        # Set environment variable to indicate enhanced completions are enabled
        os.environ['OCI_CLI_ENHANCED_COMPLETIONS'] = '1'

        return True
    except ImportError:
        return False


def is_enhanced_completions_enabled():
    """Check if enhanced completions are enabled."""
    return os.environ.get('OCI_CLI_ENHANCED_COMPLETIONS') == '1'