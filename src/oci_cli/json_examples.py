# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates. All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
Module to provide realistic JSON examples for complex parameters in OCI CLI.
This enhances the --generate-param-json-input functionality with better examples.
"""

import random

# Shape configuration examples for different use cases
SHAPE_CONFIG_EXAMPLES = [
    {
        "_comment": "Flexible VM with 2 OCPUs and 16GB RAM (standard configuration)",
        "ocpus": 2.0,
        "memoryInGBs": 16.0,
        "baselineOcpuUtilization": "BASELINE_1_1"
    },
    {
        "_comment": "Burstable instance with 50% baseline (cost-optimized)",
        "ocpus": 1.0,
        "memoryInGBs": 8.0,
        "baselineOcpuUtilization": "BASELINE_1_2"
    },
    {
        "_comment": "High performance with NVMe drives",
        "ocpus": 4.0,
        "memoryInGBs": 32.0,
        "nvmes": 2,
        "baselineOcpuUtilization": "BASELINE_1_1"
    },
    {
        "_comment": "Minimal configuration for development",
        "ocpus": 1.0,
        "memoryInGBs": 4.0,
        "baselineOcpuUtilization": "BASELINE_1_8"
    }
]

# Map of parameter names to example generators
PARAMETER_EXAMPLES = {
    "shape-config": lambda: random.choice(SHAPE_CONFIG_EXAMPLES),
    "shapeConfig": lambda: random.choice(SHAPE_CONFIG_EXAMPLES),

    # Add more parameter examples here as needed
    "agent-config": lambda: {
        "_comment": "Agent configuration for monitoring and management",
        "isMonitoringDisabled": False,
        "isManagementDisabled": False,
        "areAllPluginsDisabled": False,
        "pluginsConfig": [
            {
                "name": "OS Management Service Agent",
                "desiredState": "ENABLED"
            }
        ]
    },

    "availability-config": lambda: {
        "_comment": "Availability configuration for instance recovery",
        "recoveryAction": "RESTORE_INSTANCE",
        "isLiveMigrationPreferred": True
    },

    "launch-options": lambda: {
        "_comment": "Launch options for boot configuration",
        "bootVolumeType": "PARAVIRTUALIZED",
        "firmware": "UEFI_64",
        "networkType": "PARAVIRTUALIZED",
        "remoteDataVolumeType": "PARAVIRTUALIZED",
        "isPvEncryptionInTransitEnabled": True,
        "isConsistentVolumeNamingEnabled": True
    },

    "instance-options": lambda: {
        "_comment": "Instance options for security configuration",
        "areLegacyImdsEndpointsDisabled": True
    },

    "platform-config": lambda: {
        "_comment": "Platform configuration for performance tuning",
        "type": "AMD_MILAN_BM_GPU",
        "numaNodesPerSocket": "NPS1",
        "isSymmetricMultiThreadingEnabled": True,
        "isAccessControlServiceEnabled": True,
        "areVirtualInstructionsEnabled": True,
        "isInputOutputMemoryManagementUnitEnabled": True
    }
}


def get_example_json_for_parameter(param_name):
    """
    Get a realistic JSON example for a given parameter.

    Args:
        param_name (str): The parameter name (e.g., "shape-config")

    Returns:
        dict or None: Example JSON object or None if no example is available
    """
    if param_name in PARAMETER_EXAMPLES:
        example = PARAMETER_EXAMPLES[param_name]()
        # Remove the _comment field for the actual output
        if "_comment" in example:
            del example["_comment"]
        return example
    return None


def enhance_json_skeleton_with_examples(original_skeleton, param_name=None):
    """
    Enhance a JSON skeleton with realistic examples where available.

    Args:
        original_skeleton: The original JSON skeleton
        param_name: Optional parameter name to get specific example for

    Returns:
        Enhanced JSON skeleton with better examples
    """
    if param_name:
        example = get_example_json_for_parameter(param_name)
        if example:
            return example

    # If no specific example, return the original
    return original_skeleton


def get_example_description_for_parameter(param_name):
    """
    Get a description of available examples for a parameter.

    Args:
        param_name (str): The parameter name

    Returns:
        str: Description of available examples
    """
    descriptions = {
        "shape-config": """
Available shape-config examples:
1. Standard flexible VM (2 OCPUs, 16GB RAM)
2. Burstable instance with 50% baseline (cost-optimized)
3. High performance with NVMe drives
4. Minimal development configuration

The baselineOcpuUtilization options are:
- BASELINE_1_1: 100% baseline (no burstable performance)
- BASELINE_1_2: 50% baseline
- BASELINE_1_8: 12.5% baseline (most cost-effective)
""",
        "agent-config": "Agent configuration for monitoring and management services",
        "availability-config": "Availability configuration for instance recovery behavior",
        "launch-options": "Launch options for boot and network configuration",
        "instance-options": "Instance options for security configuration",
        "platform-config": "Platform configuration for performance tuning"
    }

    return descriptions.get(param_name, "")