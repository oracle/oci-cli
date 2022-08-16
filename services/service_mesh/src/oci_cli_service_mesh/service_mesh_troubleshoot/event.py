# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
from enum import Enum
from typing import Set, Dict


class EventType(Enum):
    OCI_CLI_VERSION = 'OCI_CLI_VERSION'
    CSV_STATUS = 'CSV_STATUS'
    INSTALL_PLAN_STATUS = 'INSTALL_PLAN_STATUS'
    OSOK = 'OCI_SERVICE_OPERATOR_FOR_KUBERNETES'
    OLM = 'OLM'
    METRICS_SERVER = 'METRICS_SERVER'
    SIDECAR_INJECTION_ENABLED_NAMESPACES = 'SIDECAR_INJECTION_ENABLED_NAMESPACES'
    POD_SUMMARY = 'POD_SUMMARY'
    CATALOG_OPERATOR = 'CATALOG_OPERATOR'  # catalog operator
    SERVICE_MESH_CRDS = 'SERVICE_MESH_CRDS'
    SERVICE_MESH_WEBHOOKS = 'SERVICE_MESH_WEBHOOKS'
    PROMETHEUS_VERSION = 'PROMETHEUS_VERSION'
    GRAFANA_VERSION = 'GRAFANA_VERSION'
    OPERATOR_SERVICES = 'OPERATOR_SERVICES'


class OperationType(Enum):
    ACCUMULATE = 'ACCUMULATE'
    STORE_SINGLE_EVENT = 'STORE_SINGLE_EVENT'
    STORE_MULTI_EVENT = 'STORE_MULTI_EVENT'


# Identifications are set of string to Apply operation, meshId, virtualServiceId .. etc.
class Event:
    def __init__(self,
                 event_type: EventType,
                 operations: Set[OperationType],
                 data: Dict,
                 identifications: Dict,
                 store: Set[str]):
        self.event_type = event_type
        self.operations = operations
        self.data = data
        self.identifications = identifications
        self.store = store
