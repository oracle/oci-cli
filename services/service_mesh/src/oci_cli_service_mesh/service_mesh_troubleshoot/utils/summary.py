# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.constants import CONDITION_TYPES


class BasicPodSummary:
    def __init__(self, name=None, namespace=None, version=None, labels=[], status=None):
        self.name = name
        self.namespace = namespace
        self.labels = labels
        self.version = version
        self.status = status


class MeshData:
    def __init__(self,
                 mesh_id=None,
                 vs_id=None,
                 vd_id=None,
                 vdb_key=None,
                 vsrt_id=None,
                 ig_id=None,
                 igd_key=None,
                 igrt_id=None,
                 ap_id=None):
        self.mesh_id = mesh_id
        self.vs_id = vs_id
        self.vd_id = vd_id
        self.vdb_key = vdb_key
        self.vsrt_id = vsrt_id
        self.ig_id = ig_id
        self.igd_key = igd_key
        self.igrt_id = igrt_id
        self.ap_id = ap_id

    def get_hierarchy_as_dict(self):
        hierarchy = {self.mesh_id: None}
        if self.ap_id is not None:
            hierarchy[self.ap_id] = self.mesh_id
        if self.vs_id is not None:
            hierarchy[self.vs_id] = self.mesh_id
        if self.ig_id is not None:
            hierarchy[self.ig_id] = self.mesh_id
        if self.ap_id is not None:
            hierarchy[self.ap_id] = self.mesh_id
        if self.vd_id is not None:
            hierarchy[self.vd_id] = self.vs_id
        if self.igd_key is not None:
            hierarchy[self.igd_key] = self.ig_id
        if self.vdb_key is not None:
            hierarchy[self.vdb_key] = self.vd_id
        return hierarchy

    def get_mesh_hierarchy(self):
        return 'mesh_' + self.mesh_id

    def get_virtual_service_hierarchy(self):
        return 'mesh_' + self.mesh_id + '/vs_' + self.vs_id

    def get_virtual_deployment_hierarchy(self):
        return 'mesh_' + self.mesh_id + '/vs_' + self.vs_id + '/vd_' + self.vd_id

    def get_virtual_deployment_binding_hierarchy(self):
        return 'mesh_' + self.mesh_id + '/vs_' + self.vs_id + '/vd_' + self.vd_id + '/vdb_' + self.vdb_key

    def get_virtual_service_route_table_hierarchy(self):
        return 'mesh_' + self.mesh_id + '/vs_' + self.vs_id + '/vd_' + self.vd_id + '/vsrt_' + self.vsrt_id

    def get_ingress_gateway_hierarchy(self):
        return 'mesh_' + self.mesh_id + '/ig_' + self.ig_id

    def get_ingress_gateway_deployment_hierarchy(self):
        return 'mesh_' + self.mesh_id + '/ig_' + self.ig_id + '/igd_' + self.igd_key

    def get_ingress_gateway_route_table_hierarchy(self):
        return 'mesh_' + self.mesh_id + '/ig_' + self.ig_id + '/igrt_' + self.igrt_id

    def get_access_policy_hierarchy(self):
        return 'mesh_' + self.mesh_id + '/ap_' + self.ap_id


class PodSummary:
    def __init__(self,
                 proxy_version=None,
                 proxy_status=None,
                 basic_pod_summary: BasicPodSummary = None,
                 mesh_data: MeshData = None,
                 pod_json=None,
                 dynamic_config_version=None):
        self.proxy_version = proxy_version
        self.dynamic_config_version = dynamic_config_version
        self.proxy_status = proxy_status
        self.basic_pod_summary = basic_pod_summary
        self.mesh_data = mesh_data
        self.pod_json = pod_json

    def to_dict(self, mesh_data):
        data = {}
        if mesh_data.mesh_id is not None:
            data['mesh_id'] = mesh_data.mesh_id
        if mesh_data.vs_id is not None:
            data['vs_id'] = mesh_data.vs_id
        if mesh_data.vd_id is not None:
            data['vd_id'] = mesh_data.vd_id
        if mesh_data.ig_id is not None:
            data['ig_id'] = mesh_data.ig_id
        if mesh_data.vdb_key is not None:
            data['vdb_key'] = mesh_data.vdb_key
        if mesh_data.igd_key is not None:
            data['igd_key'] = mesh_data.igd_key
        if self.basic_pod_summary.name is not None:
            data['name'] = self.basic_pod_summary.name
        if self.basic_pod_summary.namespace is not None:
            data['namespace'] = self.basic_pod_summary.namespace
        if self.proxy_status is not None:
            data['proxy_status'] = self.proxy_status
        if self.proxy_version is not None:
            data['proxy_version'] = self.proxy_version
        if self.dynamic_config_version is not None:
            data['dynamic_config_version'] = self.dynamic_config_version
        if self.basic_pod_summary.labels is not None:
            data['labels'] = self.basic_pod_summary.labels

        return data


class CustomResourceSummary:
    def __init__(self, custom_resource_json):
        self.custom_resource_json = custom_resource_json

    def get_name(self):
        return self.custom_resource_json['metadata']['name']

    def get_namespace(self):
        return self.custom_resource_json['metadata']['namespace']

    def get_kind(self):
        return self.custom_resource_json['kind']

    def get_qualified_name(self):
        return self.get_namespace() + '_' + self.get_name()

    def is_inactive_resource(self):
        for condition in self.custom_resource_json['status']['conditions']:
            if condition['type'] in CONDITION_TYPES and condition['status'] != 'True':
                return True
        return False

    def get_relative_path(self, mesh_id=None):
        if self.custom_resource_json['kind'] == 'Mesh':
            return 'mesh_' + self.custom_resource_json['status']['meshId']
        elif self.custom_resource_json['kind'] == 'VirtualService':
            return 'mesh_' + self.custom_resource_json['status']['meshId'] + \
                   '/vs_' + self.custom_resource_json['status']['virtualServiceId']
        elif self.custom_resource_json['kind'] == 'VirtualDeployment':
            return 'mesh_' + self.custom_resource_json['status']['meshId'] + \
                   '/vs_' + self.custom_resource_json['status']['virtualServiceId'] + \
                   '/vd_' + self.custom_resource_json['status']['virtualDeploymentId']
        elif self.custom_resource_json['kind'] == 'VirtualDeploymentBinding':
            return 'mesh_' + self.custom_resource_json['status']['meshId'] + \
                   '/vs_' + self.custom_resource_json['status']['virtualServiceId'] + \
                   '/vd_' + self.custom_resource_json['status']['virtualDeploymentId'] + \
                   '/vdb_' + self.get_qualified_name()
        elif self.custom_resource_json['kind'] == 'VirtualServiceRouteTable':
            return 'mesh_' + mesh_id + \
                   '/vs_' + self.custom_resource_json['status']['virtualServiceId'] + \
                   '/vsrt_' + self.custom_resource_json['status']['virtualServiceRouteTableId']
        elif self.custom_resource_json['kind'] == 'IngressGateway':
            return 'mesh_' + self.custom_resource_json['status']['meshId'] + \
                   '/ig_' + self.custom_resource_json['status']['ingressGatewayId']
        elif self.custom_resource_json['kind'] == 'IngressGatewayDeployment':
            return 'mesh_' + self.custom_resource_json['status']['meshId'] + \
                   '/ig_' + self.custom_resource_json['status']['ingressGatewayId'] + \
                   '/igd_' + self.get_qualified_name()
        elif self.custom_resource_json['kind'] == 'IngressGatewayRouteTable':
            return 'mesh_' + mesh_id + \
                   '/ig_' + self.custom_resource_json['status']['ingressGatewayId'] + \
                   '/igrt_' + self.custom_resource_json['status']['ingressGatewayRouteTableId']
        elif self.custom_resource_json['kind'] == 'AccessPolicy':
            return 'mesh_' + self.custom_resource_json['status']['meshId'] + \
                   '/ap_' + self.custom_resource_json['status']['accessPolicyId']


class MeshResources:
    def __init__(self,
                 mesh_dict=None,
                 vs_dict=None,
                 vd_dict=None,
                 vdb_dict=None,
                 vsrt_dict=None,
                 ig_dict=None,
                 igd_dict=None,
                 igrt_dict=None,
                 ap_dict=None):
        if ap_dict is None:
            ap_dict = {}
        if igrt_dict is None:
            igrt_dict = {}
        if igd_dict is None:
            igd_dict = {}
        if ig_dict is None:
            ig_dict = {}
        if vsrt_dict is None:
            vsrt_dict = {}
        if vdb_dict is None:
            vdb_dict = {}
        if vd_dict is None:
            vd_dict = {}
        if vs_dict is None:
            vs_dict = {}
        if mesh_dict is None:
            mesh_dict = {}
        self.mesh_dict = mesh_dict
        self.vs_dict = vs_dict
        self.vd_dict = vd_dict
        self.vdb_dict = vdb_dict
        self.vsrt_dict = vsrt_dict
        self.ig_dict = ig_dict
        self.igd_dict = igd_dict
        self.igrt_dict = igrt_dict
        self.ap_dict = ap_dict
