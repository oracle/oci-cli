# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.autoscaling import AutoScalingClient

MODULE_TO_TYPE_MAPPINGS["autoscaling"] = oci.autoscaling.models.autoscaling_type_mapping
CLIENT_MAP["auto_scaling"] = AutoScalingClient
