# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.load_balancer import LoadBalancerClient

MODULE_TO_TYPE_MAPPINGS["load_balancer"] = oci.load_balancer.models.load_balancer_type_mapping
CLIENT_MAP["load_balancer"] = LoadBalancerClient
