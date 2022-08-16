# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.constants import MESH_CRD_DICT


def get_resource_type_from_ocid(ocid: str):
    return MESH_CRD_DICT[ocid.split(".")[1]]


class MeshTaskException(Exception):
    pass
