# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
from enum import Enum

GROUP = 'servicemesh.oci.oracle.com'
VERSION = 'v1beta1'

VDB_ANNOTATION = 'servicemesh.oci.oracle.com/virtual-deployment-binding-ref'
IGD_LABEL = 'servicemesh.oci.oracle.com/ingress-gateway-deployment'

MESH_PLURAL = 'meshes'
VS_PLURAL = 'virtualservices'
VD_PLURAL = 'virtualdeployments'
VDB_PLURAL = 'virtualdeploymentbindings'
IG_PLURAL = 'ingressgateways'
IGD_PLURAL = 'ingressgatewaydeployments'
AP_PLURAL = 'accesspolicies'
VSRT_PLURAL = 'virtualserviceroutetables'
IGRT_PLURAL = 'ingressgatewayroutetables'
OVERVIEW = 'overview'

CONDITION_TYPES = ['ServiceMeshActive', 'ServiceMeshConfigured', 'ServiceMeshDependenciesActive']

OCI_SM_PROXY = 'oci-sm-proxy'

# TODO: This will be replaced by API
OLM_VERSION = "v0.20.0"


class IssueType(Enum):
    CSV_STATUS_NOT_SUCCEEDED = 'Status of Csv did not succeed'
    MULTIPLE_SIDECAR_VERSIONS = 'Multiple versions are used for proxy sidecar'
    SETUP_OBSERVABILITY = 'Observability setup is not complete'
    MISSING_MESH_WEBHOOKS = 'All Mesh webhooks are not installed'
    MISSING_OPERATOR_SERVICES = 'All Operator Services are not installed'
    MISSING_MESH_CRDS = 'All Mesh Crds are not installed'
    INCOMPATIBLE_VERSIONS = 'Incompatible software versions are used in installation'
    INCOMPATIBLE_OLM_VERSION = 'OLM Version is not compatible'

    def describe(self):
        return self.value


TROUBLESHOOT_DICT = {
    IssueType.CSV_STATUS_NOT_SUCCEEDED: "Refer - https://docs.oracle.com/en-us/iaas/Content/service-mesh/tbl-troubleshoot-osok.htm",
    IssueType.MISSING_MESH_WEBHOOKS: "Refer - https://docs.oracle.com/en-us/iaas/Content/service-mesh/tbl-troubleshoot-osok.htm",
    IssueType.MISSING_MESH_CRDS: "Refer - https://docs.oracle.com/en-us/iaas/Content/service-mesh/tbl-troubleshoot-osok.htm",
    IssueType.INCOMPATIBLE_VERSIONS: "Contact Oracle Support for assistance.",
    IssueType.SETUP_OBSERVABILITY: "Suggestions to setup Observability",
    IssueType.MULTIPLE_SIDECAR_VERSIONS: "Refer - https://docs.oracle.com/en-us/iaas/Content/service-mesh/tbl-troubleshoot-osok.htm",
    IssueType.MISSING_OPERATOR_SERVICES: "Refer - https://docs.oracle.com/en-us/iaas/Content/service-mesh/tbl-troubleshoot-osok.htm",
    IssueType.INCOMPATIBLE_OLM_VERSION: "Refer - https://docs.oracle.com/en-us/iaas/Content/service-mesh/tbl-troubleshoot-osok.htm",

}

MESH_CUSTOM_RESOURCE_DICT = {
    'mesh': 'meshId',
    'meshvirtualservice': 'virtualServiceId',
    'meshvirtualdeployment': 'virtualDeploymentId',
    'meshingressgateway': 'ingressGatewayId',
    'meshaccesspolicy': 'accessPolicyId',
    'meshvirtualserviceroutetable': 'virtualServiceRouteTableId',
    'meshingressgatewayroutetable': 'ingressGatewayRouteTableId',
}

MESH_CRD_DICT = {
    'mesh': MESH_PLURAL,
    'meshvirtualservice': VS_PLURAL,
    'meshvirtualdeployment': VD_PLURAL,
    'meshingressgateway': IG_PLURAL,
    'meshaccesspolicy': AP_PLURAL,
    'meshvirtualserviceroutetable': VSRT_PLURAL,
    'meshingressgatewayroutetable': IGRT_PLURAL,
    'meshvirtualdeploymentbinding': VDB_PLURAL,
    'meshingressgatewaydeployment': IGD_PLURAL,
}

VALID_CRDS_LIST = ['accesspolicies.servicemesh.oci.oracle.com',
                   'ingressgatewaydeployments.servicemesh.oci.oracle.com',
                   'ingressgatewayroutetables.servicemesh.oci.oracle.com',
                   'ingressgateways.servicemesh.oci.oracle.com',
                   'meshes.servicemesh.oci.oracle.com',
                   'virtualdeploymentbindings.servicemesh.oci.oracle.com',
                   'virtualdeployments.servicemesh.oci.oracle.com',
                   'virtualserviceroutetables.servicemesh.oci.oracle.com',
                   'virtualservices.servicemesh.oci.oracle.com']

WEBHOOKS_LIST = ["ap-validator.servicemesh.oci.oracle.cloud.com",
                 "ig-validator.servicemesh.oci.oracle.cloud.com",
                 "igd-validator.servicemesh.oci.oracle.cloud.com",
                 "igrt-validator.servicemesh.oci.oracle.cloud.com",
                 "mesh-validator.servicemesh.oci.oracle.cloud.com",
                 "vd-validator.servicemesh.oci.oracle.cloud.com",
                 "vdb-validator.servicemesh.oci.oracle.cloud.com",
                 "vs-validator.servicemesh.oci.oracle.cloud.com",
                 "vsrt-validator.servicemesh.oci.oracle.cloud.com",
                 "proxy-injector.servicemesh.oci.oracle.com"]

OPERATOR_SERVICES_LIST = [
    "oci-service-operator-controller-manager-service",
    "oci-service-operator-webhook-service"
]

OPERATOR_ANNOTATION = 'oci-service-operator-controller-manager-*'
CERT_MANAGER_LABEL = 'app.kubernetes.io/name=cert-manager'
METRICS_SERVER_LABEL = 'k8s-app=metrics-server'
OLM_LABEL = 'app=olm-operator'
CATALOG_OPERATOR_LABEL = 'app=catalog-operator'

SIDECAR_INJECTION_LABEL = 'servicemesh.oci.oracle.com/sidecar-injection'
SIDECAR_INJECTION_LABEL_ENABLED = 'servicemesh.oci.oracle.com/sidecar-injection=enabled'

ITEMS = 'items'
METADATA = 'metadata'
ANNOTATIONS = 'annotations'
LABELS = 'labels'
SPEC = 'spec'
ENV = 'env'
POD_UPGRADE_ENABLED = 'podUpgradeEnabled'
STATUS = 'status'
NAME = 'name'
NAMESPACE = 'namespace'
CONTAINERS = 'containers'
CONTAINER_STATUSES = 'containerStatuses'
IMAGE = 'image'
STATE = 'state'
MESH_ID = 'meshId'
VIRTUAL_SERVICE_ID = 'virtualServiceId'
VIRTUAL_DEPLOYMENT_ID = 'virtualDeploymentId'
INGRESS_GATEWAY_ID = 'ingressGatewayId'
PHASE = 'phase'
PROXY_VERSION = 'proxy_version'
DYNAMIC_VERSION = 'dynamic_config_version'
CSV = 'csv'
REPORT = 'report'
PENDING = 'Pending'
SUCCEEDED = 'Succeeded'
OLM = 'olm'
