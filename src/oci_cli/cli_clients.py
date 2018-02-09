# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import oci
from oci.audit import AuditClient
from oci.core import BlockstorageClient
from oci.core import ComputeClient
from oci.core import VirtualNetworkClient
from oci.database import DatabaseClient
from oci.dns import DnsClient
from oci.identity import IdentityClient
from oci.load_balancer import LoadBalancerClient
from oci.object_storage import ObjectStorageClient

CLIENT_MAP = {
    "audit": AuditClient,
    "blockstorage": BlockstorageClient,
    "compute": ComputeClient,
    "database": DatabaseClient,
    "dns": DnsClient,
    "identity": IdentityClient,
    "load_balancer": LoadBalancerClient,
    "object_storage": ObjectStorageClient,
    "virtual_network": VirtualNetworkClient
}

MODULE_TO_TYPE_MAPPINGS = {
    "audit": oci.audit.models.audit_type_mapping,
    "core": oci.core.models.core_type_mapping,
    "database": oci.database.models.database_type_mapping,
    "dns": oci.dns.models.dns_type_mapping,
    "identity": oci.identity.models.identity_type_mapping,
    "load_balancer": oci.load_balancer.models.load_balancer_type_mapping,
    "object_storage": oci.object_storage.models.object_storage_type_mapping
}
