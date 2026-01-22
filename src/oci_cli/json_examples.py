# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates. All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

"""
Module to provide realistic JSON examples for complex parameters in OCI CLI.
This enhances the --generate-param-json-input functionality with better examples.
"""

import random

# Cached example OCIDs for realistic examples
CACHED_OCIDS = {
    "compartment": "ocid1.compartment.oc1..aaaaaaaaq3loyafnlhij4knz3jvbqycxya6nfkfq7tczzoakdnye3wnzpqeq",
    "instance": "ocid1.instance.oc1.iad.anuwcljtniwq6syc7g6n7ywrya3avzcctnw7qbbaqn72f2tqhqcbhxiq",
    "vcn": "ocid1.vcn.oc1.iad.amaaaaaanlc5nbyaknrwfkzv7oqv4kxfytaglazuaeruocuyvdrbcg2bqda",
    "subnet": "ocid1.subnet.oc1.iad.aaaaaaaawngpvr7vhqvq65vqp2z4bkxhvxl5wqkmpvd3xjmi7rxyogddng4a",
    "image": "ocid1.image.oc1.iad.aaaaaaaaiu73xa6afjzskjwvt3j5shpmftnbkiwindolgp7c2yxvjpyqhbza",
    "boot_volume": "ocid1.bootvolume.oc1.iad.abuwcljr5bhtqkplnlaxfzvmvntnigpmzpdo3kmyocoaen6fqhilcixugk7q",
    "block_volume": "ocid1.volume.oc1.iad.abuwcljrbffbqz2z2e3h7zjlz2nsanx56yt4b6lufnopcgnxk4zgrncdkxeq",
    "dedicated_vm_host": "ocid1.dedicatedvmhost.oc1.iad.anuwcljtniwq6syc5btw2bzqulj5fp2xdhqcd3r3eltsm4pq4xiq",
    "capacity_reservation": "ocid1.capacityreservation.oc1.iad.anuwcljrniwq6syc5btw2bzlkj5fp2xdhycd3r3eltpb4pq7xiq"
}

# Minimal shape configuration examples - prefer 1.0 OCPU for minimal setup
SHAPE_CONFIG_EXAMPLES = [
    {
        "_comment": "Absolute minimal flexible VM",
        "ocpus": 1.0,
        "memoryInGBs": 1.0
    },
    {
        "_comment": "Burstable instance (cost-optimized)",
        "ocpus": 1.0,
        "memoryInGBs": 2.0,
        "baselineOcpuUtilization": "BASELINE_1_2"
    },
    {
        "_comment": "Minimal with baseline control",
        "ocpus": 1.0,
        "memoryInGBs": 1.0,
        "baselineOcpuUtilization": "BASELINE_1_1"
    }
]

# Map of parameter names to example generators
PARAMETER_EXAMPLES = {
    "shape-config": lambda: random.choice(SHAPE_CONFIG_EXAMPLES),
    "shapeConfig": lambda: random.choice(SHAPE_CONFIG_EXAMPLES),

    # Minimal parameter examples
    "agent-config": lambda: {
        "_comment": "Minimal agent configuration",
        "isMonitoringDisabled": False,
        "isManagementDisabled": False
    },

    "availability-config": lambda: {
        "_comment": "Minimal availability configuration",
        "recoveryAction": "RESTORE_INSTANCE"
    },

    "launch-options": lambda: {
        "_comment": "Minimal launch options",
        "bootVolumeType": "PARAVIRTUALIZED",
        "firmware": "UEFI_64",
        "networkType": "PARAVIRTUALIZED"
    },

    "instance-options": lambda: {
        "_comment": "Minimal instance options",
        "areLegacyImdsEndpointsDisabled": False
    },

    "platform-config": lambda: {
        "_comment": "Minimal platform configuration",
        "type": "AMD_MILAN_BM"
    },

    # Source details for instance launch/update
    "source-details": lambda: random.choice([
        {
            "_comment": "Boot from image",
            "sourceType": "image",
            "imageId": CACHED_OCIDS["image"]
        },
        {
            "_comment": "Boot from existing boot volume",
            "sourceType": "bootVolume",
            "bootVolumeId": CACHED_OCIDS["boot_volume"]
        }
    ]),

    # Volume attachments
    "launch-volume-attachments": lambda: [
        {
            "attachmentType": "paravirtualized",
            "device": "/dev/sdb",
            "displayName": "data-volume",
            "volumeId": CACHED_OCIDS["block_volume"]
        }
    ],

    # Metadata for cloud-init
    "metadata": lambda: {
        "ssh_authorized_keys": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC... user@host",
        "user_data": "IyEvYmluL2Jhc2gKZWNobyAiSGVsbG8gV29ybGQi"  # base64 encoded
    },

    # Extended metadata
    "extended-metadata": lambda: {
        "app_version": "1.0.0",
        "environment": "development"
    },

    # Preemptible instance config
    "preemptible-instance-config": lambda: {
        "preemptionAction": {
            "type": "TERMINATE",
            "preserveBootVolume": False
        }
    },

    # Examples with OCIDs for reference parameters
    "capacity-reservation-id": lambda: CACHED_OCIDS["capacity_reservation"],
    "dedicated-vm-host-id": lambda: CACHED_OCIDS["dedicated_vm_host"],
    "instance-id": lambda: CACHED_OCIDS["instance"],
    "compartment-id": lambda: CACHED_OCIDS["compartment"],
    "image-id": lambda: CACHED_OCIDS["image"],
    "subnet-id": lambda: CACHED_OCIDS["subnet"],
    "vcn-id": lambda: CACHED_OCIDS["vcn"]
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
# Shape config examples (truly minimal configurations):
# - Absolute minimal: 1 OCPU, 1GB RAM
# - Burstable minimal: 1 OCPU, 2GB RAM, 50% baseline
# - Minimal with full baseline: 1 OCPU, 1GB RAM, 100% baseline
# baselineOcpuUtilization: BASELINE_1_1 (100%), BASELINE_1_2 (50%), BASELINE_1_8 (12.5%)
""",
        "agent-config": "# Minimal agent configuration example",
        "availability-config": "# Minimal availability configuration example",
        "launch-options": "# Minimal launch options example",
        "instance-options": "# Minimal instance options example",
        "platform-config": "# Minimal platform configuration example",
        "source-details": "# Examples: boot from image or boot volume",
        "launch-volume-attachments": "# Example: attach block volume as /dev/sdb",
        "metadata": "# Example: SSH keys and cloud-init user_data (base64)",
        "extended-metadata": "# Example: custom key-value pairs",
        "preemptible-instance-config": "# Example: preemptible instance with termination action"
    }

    return descriptions.get(param_name, "")