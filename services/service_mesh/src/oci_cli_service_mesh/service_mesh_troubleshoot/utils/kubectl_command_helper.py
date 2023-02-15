# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import concurrent.futures
import json
import os
import re
import subprocess
from io import StringIO

import click
import sys
import time

from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.constants import \
    MESH_CUSTOM_RESOURCE_DICT, OCI_SM_PROXY, IGD_LABEL, MESH_CRD_DICT, ITEMS, METADATA, NAME, NAMESPACE, SPEC, \
    CONTAINERS, IMAGE, STATUS, CONTAINER_STATUSES, STATE, SIDECAR_INJECTION_LABEL_ENABLED, MESH_ID, VIRTUAL_SERVICE_ID, \
    INGRESS_GATEWAY_ID, VIRTUAL_DEPLOYMENT_ID, LABELS, ANNOTATIONS
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.messages import Messages
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.summary import BasicPodSummary, \
    PodSummary
from services.service_mesh.src.oci_cli_service_mesh.service_mesh_troubleshoot.utils.summary import \
    CustomResourceSummary, MeshResources


def construct_empty_pod_summary():
    name = 'Unavailable'
    namespace = 'Unavailable'
    labels = {}
    version = 'Unavailable'
    status = 'Unavailable'
    return BasicPodSummary(name=name,
                           namespace=namespace,
                           status=status,
                           version=version,
                           labels=labels)


def get_name_namespace_labels_from_pod_json(pod):
    name, namespace, labels = None, None, None
    if pod is not None and METADATA in pod:
        if NAME in pod[METADATA]:
            name = pod[METADATA][NAME]
        if NAMESPACE in pod[METADATA]:
            namespace = pod[METADATA][NAMESPACE]
        if LABELS in pod[METADATA]:
            labels = pod[METADATA][LABELS]
    return name, namespace, labels


def get_proxy_details_from_pod_json(pod):
    status, proxy_status, proxy_version = None, None, None
    if STATUS in pod:
        status = pod[STATUS]
        if CONTAINER_STATUSES in pod[STATUS] and len(pod[STATUS][CONTAINER_STATUSES]) > 0:
            for container_status in pod[STATUS][CONTAINER_STATUSES]:
                if NAME in container_status:
                    if container_status[NAME] == OCI_SM_PROXY:
                        if STATE in container_status:
                            proxy_status = container_status[STATE]
                        if IMAGE in container_status:
                            proxy_version = container_status[IMAGE].split(':')[1]
    return status, proxy_status, proxy_version


class KubeCommandHelper:

    def __init__(self, k8s_context=None):
        self.k8s_config, self.use_context = k8s_context

    def get_resource_filter_type_id(self, ocid):
        return MESH_CUSTOM_RESOURCE_DICT[ocid.split(".")[1]]

    def print_command(self, args):
        command_string = ' '.join([str(argument) for argument in args])
        print('\nExecuting: {}'.format(command_string))

    # Run the given command as a subprocess
    def run_command_as_subprocess(self, args, append_context_to_args=True, print_output=False):

        if append_context_to_args and self.k8s_config is not None:
            args.append('--kubeconfig')
            args.append(self.k8s_config)
        if append_context_to_args and self.use_context is not None:
            args.append('--context')
            args.append(self.use_context)

        if print_output:
            self.print_command(args)
        start_time = time.time()
        try:
            output = subprocess.run(args, capture_output=True, timeout=300)
            kubectl_command_summary = KubectlCommandSummary(output.returncode,
                                                            output.stdout.decode('utf-8'),
                                                            output.stderr.decode('utf-8'))
        except Exception as error:
            kubectl_command_summary = KubectlCommandSummary(-1, '', error)

        if kubectl_command_summary.return_code != 0:
            click.echo(format(args))
            click.echo('\nReturn Code: {}, Error: {}'.format(kubectl_command_summary.return_code,
                                                             kubectl_command_summary.stderr))
        if print_output:
            click.echo('Time taken: {}'.format(time.time() - start_time))

        return kubectl_command_summary

    # Filter pod by label selector
    def get_pod_details_by_label_selector(self, label_selector):
        get_pods_by_filter_args = ['kubectl', 'get', 'pods', '--all-namespaces', '-l', label_selector, '-o', 'json']
        kubectl_command_summary = self.run_command_as_subprocess(get_pods_by_filter_args)
        pod_summary = construct_empty_pod_summary()
        if kubectl_command_summary.return_code == 0:
            pod_json = json.loads(kubectl_command_summary.stdout)
            if pod_json is not None and ITEMS in pod_json and len(pod_json[ITEMS]) > 0:
                pod = pod_json[ITEMS][0]
                if METADATA in pod and LABELS in pod[METADATA]:
                    pod_summary.labels = pod[METADATA][LABELS]
                if METADATA in pod and NAME in pod[METADATA] and NAMESPACE in pod[METADATA]:
                    pod_summary.name = pod[METADATA][NAME]
                    pod_summary.namespace = pod[METADATA][NAMESPACE]
                if SPEC in pod and CONTAINERS in pod[SPEC] \
                        and len(pod[SPEC][CONTAINERS]) > 0 and IMAGE in pod[SPEC][CONTAINERS][0]:
                    pod_summary.version = pod[SPEC][CONTAINERS][0][IMAGE].split(':')[1]
                if STATUS in pod and CONTAINER_STATUSES in pod[STATUS] \
                        and len(pod[STATUS][CONTAINER_STATUSES]) > 0 \
                        and STATE in pod[STATUS][CONTAINER_STATUSES][0]:
                    pod_summary.status = pod[STATUS][CONTAINER_STATUSES][0][STATE]
            return pod_summary
        else:
            return pod_summary

    # Filter operator pod
    def get_operator_pod_details(self, search_string):
        kubectl_get_pods_args = [
            'kubectl', 'get', 'pods', '--no-headers', '--all-namespaces', '--template',
            '{{range .items}}{{.metadata.name}}{{" "}}{{.metadata.namespace}}{{"\\n"}}{{end}}']
        if self.k8s_config is not None:
            kubectl_get_pods_args.append('--kubeconfig')
            kubectl_get_pods_args.append(self.k8s_config)
        basic_pod_summary = construct_empty_pod_summary()
        try:
            kubectl_command_summary = self.run_command_as_subprocess(kubectl_get_pods_args)
            if kubectl_command_summary.return_code != 0:
                return basic_pod_summary
            pods_list = kubectl_command_summary.stdout.split('\n')
            operator_search_string = "oci-service-operator-controller-manager"
            operator_pod = [pod for pod in pods_list if operator_search_string in pod]
            if len(operator_pod) < 1:
                return basic_pod_summary
            operator_pod = operator_pod[0].strip("\'")
            pod_tokens = operator_pod.split(" ")

            if pod_tokens is None or len(pod_tokens) < 2:
                return basic_pod_summary
            name, namespace = pod_tokens[0].strip(), pod_tokens[1].strip()
            get_operator_pod_args = ['kubectl', 'get', 'pod', name, '-n', namespace, '-o', 'json']
            kubectl_command_summary = self.run_command_as_subprocess(get_operator_pod_args)
            if kubectl_command_summary.return_code == 0:
                pod_json = json.loads(kubectl_command_summary.stdout)
                if pod_json is not None:
                    if METADATA in pod_json and LABELS in pod_json[METADATA]:
                        basic_pod_summary.labels = pod_json[METADATA][LABELS]
                    if METADATA in pod_json and NAME in pod_json[METADATA] and NAMESPACE in pod_json[METADATA]:
                        basic_pod_summary.name = pod_json[METADATA][NAME]
                        basic_pod_summary.namespace = pod_json[METADATA][NAMESPACE]
                    if STATUS in pod_json:
                        basic_pod_summary.status = pod_json[STATUS]
                    if SPEC in pod_json and CONTAINERS in pod_json[SPEC] and len(pod_json[SPEC][CONTAINERS]) > 0:
                        container = pod_json[SPEC][CONTAINERS][0]
                        if IMAGE in container:
                            basic_pod_summary.version = container[IMAGE].split(":")[1]
                return basic_pod_summary
        except Exception as error:
            click.echo(Messages.some_exception.format('fetching operator details', error), file=sys.stderr)
        return basic_pod_summary

    def get_csv(self, namespace):
        get_status_of_csv_args = ['kubectl', 'get', 'csv', '-n', namespace, '-o', 'json']
        kubectl_command_summary = self.run_command_as_subprocess(get_status_of_csv_args)
        csv = 'Unavailable'
        if kubectl_command_summary.return_code == 0:
            csv = json.loads(kubectl_command_summary.stdout)
        return csv

    def get_install_plan(self, namespace):
        get_status_of_installplan_args = ['kubectl', 'get', 'installplan', '-n', namespace, '-o', 'json']
        kubectl_command_summary = self.run_command_as_subprocess(get_status_of_installplan_args)
        install_plan = 'Unavailable'
        if kubectl_command_summary.return_code == 0:
            install_plan = json.loads(kubectl_command_summary.stdout)

        return install_plan

    def get_subscription(self, namespace):
        get_status_of_subscription_args = ['kubectl', 'get', 'subscription', '-n', namespace, '-o', 'json']
        kubectl_command_summary = self.run_command_as_subprocess(get_status_of_subscription_args)
        subscription = 'Unavailable'

        if kubectl_command_summary.return_code == 0:
            subscription = json.loads(kubectl_command_summary.stdout)

        return subscription

    def get_catalog_source(self, namespace):
        get_status_of_catalog_source_args = ['kubectl', 'get', 'catalogsource', '-n', namespace, '-o', 'json']
        kubectl_command_summary = self.run_command_as_subprocess(get_status_of_catalog_source_args)
        catalog_source = 'Unavailable'

        if kubectl_command_summary.return_code == 0:
            catalog_source = json.loads(kubectl_command_summary.stdout)

        return catalog_source

    # Get installed crds validated
    def get_crds_validated(self):
        get_crds_validated_args = ['kubectl', 'get', 'crds']
        kubectl_command_summary = self.run_command_as_subprocess(get_crds_validated_args)
        validated_crds_list = []
        if kubectl_command_summary.return_code == 0:
            crd_installed = kubectl_command_summary.stdout
            validated_crds_list = re.findall(r".*.servicemesh.*.com", crd_installed)
        return validated_crds_list

    # Get installed webhooks validated
    def get_webhooks_validated(self):
        get_webhooks_validated_args = ['kubectl', 'get', 'ValidatingWebhookConfiguration']
        kubectl_command_summary = self.run_command_as_subprocess(get_webhooks_validated_args)
        webhooks_list = []
        if kubectl_command_summary.return_code == 0:
            webhook_installed = kubectl_command_summary.stdout
            webhooks_list = re.findall(r".*.servicemesh.*.com", webhook_installed)

        get_mutating_webhook_args = ['kubectl', 'get', 'MutatingWebhookConfiguration']
        kubectl_command_summary = self.run_command_as_subprocess(get_mutating_webhook_args)
        mutating_webhooks_list = []
        if kubectl_command_summary.return_code == 0:
            mutating_webhooks = kubectl_command_summary.stdout
            mutating_webhooks_list = re.findall(r".*.servicemesh.*.com", mutating_webhooks)

        return webhooks_list + mutating_webhooks_list

    def get_operator_services(self):
        get_services_args = ['kubectl', 'get', 'services', '--all-namespaces']
        kubectl_command_summary = self.run_command_as_subprocess(get_services_args)
        services = ['oci-service-operator-controller-manager-service', 'oci-service-operator-webhook-service']
        service_list = []
        if kubectl_command_summary.return_code == 0:
            services_list = kubectl_command_summary.stdout
            for service in services:
                if re.search(service, services_list):
                    service_list.append(service)

        return service_list

    # Get pod logs
    def get_pod_logs(self, name, namespace):
        log_command_args = ['kubectl', 'logs', name, '-n', namespace]
        kubectl_command_summary = self.run_command_as_subprocess(log_command_args)
        logs = None
        if kubectl_command_summary.return_code == 0:
            logs = kubectl_command_summary.stdout
        return logs

    # Get proxy logs
    def get_proxy_logs(self, name, namespace):
        pod_logs_args = ['kubectl', 'logs', name, '-n', namespace, '-c', OCI_SM_PROXY]
        kubectl_command_summary = self.run_command_as_subprocess(pod_logs_args)
        proxy_logs = None
        if kubectl_command_summary.return_code == 0:
            proxy_logs = kubectl_command_summary.stdout
        return proxy_logs

    # Get config dump
    def get_config_dump(self, name, namespace):
        if self.k8s_config is not None:
            config_dump_args = ['kubectl', 'exec', name, '-n', namespace, '-c', OCI_SM_PROXY, '--kubeconfig',
                                self.k8s_config, '--', 'curl', '-s', 'localhost:9901/config_dump']
        else:
            config_dump_args = ['kubectl', 'exec', name, '-n', namespace, '-c', OCI_SM_PROXY,
                                '--', 'curl', '-s', 'localhost:9901/config_dump']
        kubectl_command_summary = self.run_command_as_subprocess(args=config_dump_args, append_context_to_args=False)
        config_dump = None
        if kubectl_command_summary.return_code == 0:
            config_dump = json.loads(kubectl_command_summary.stdout)
        return config_dump

    # Get Proxy Stats
    def get_proxy_stats(self, name, namespace):
        if self.k8s_config is not None:
            proxy_stats_args = ['kubectl', 'exec', name, '-n', namespace, '-c', OCI_SM_PROXY, '--kubeconfig',
                                self.k8s_config, '--', 'curl', '-s', 'localhost:9901/stats?format=json']
        else:
            proxy_stats_args = ['kubectl', 'exec', name, '-n', namespace, '-c', OCI_SM_PROXY,
                                '--', 'curl', '-s', 'localhost:9901/stats?format=json']
        kubectl_command_summary = self.run_command_as_subprocess(args=proxy_stats_args, append_context_to_args=False)
        proxy_stats = None
        if kubectl_command_summary.return_code == 0:
            proxy_stats = json.loads(kubectl_command_summary.stdout)
        return proxy_stats

    # Filter namespaces with sidecar injection enabled
    def get_namespaces_with_sidecar_injection_enabled(self):
        get_namespace_args = ['kubectl', 'get', 'namespaces', '-l', SIDECAR_INJECTION_LABEL_ENABLED, '-o', 'json']
        kubectl_command_summary = self.run_command_as_subprocess(get_namespace_args)
        namespaces = []
        if kubectl_command_summary.return_code == 0:
            namespaces_json = json.loads(kubectl_command_summary.stdout)
            if namespaces_json is not None and ITEMS in namespaces_json:
                for item in namespaces_json[ITEMS]:
                    if METADATA in item and NAME in item[METADATA]:
                        namespaces.append(item[METADATA][NAME])
        return namespaces

    # Filter required vdbs
    def filter_vdbs_by_ocid(self, ocid):
        mesh_vdb_dict = {}
        filter_type = self.get_resource_filter_type_id(ocid)
        get_vdbs_args = ['kubectl', 'get', 'virtualdeploymentbindings', '--all-namespaces', '-o', 'json']
        kubectl_command_summary = self.run_command_as_subprocess(get_vdbs_args)

        if kubectl_command_summary.return_code != 0:
            return mesh_vdb_dict

        vdbs_string = kubectl_command_summary.stdout
        vdbs = json.loads(vdbs_string)
        if vdbs is not None and ITEMS in vdbs and len(vdbs[ITEMS]) > 0:
            for item in vdbs[ITEMS]:
                name, namespace = None, None
                mesh_id, vs_id, vd_id = None, None, None
                if STATUS not in item or filter_type not in item[STATUS] or \
                        item[STATUS][filter_type] != ocid:
                    continue
                if METADATA in item:
                    if NAME in item[METADATA]:
                        name = item[METADATA][NAME]
                    if NAMESPACE in item[METADATA]:
                        namespace = item[METADATA][NAMESPACE]
                if STATUS in item:
                    if MESH_ID in item[STATUS]:
                        mesh_id = item[STATUS][MESH_ID]
                    if VIRTUAL_SERVICE_ID in item[STATUS]:
                        vs_id = item[STATUS][VIRTUAL_SERVICE_ID]
                    if MESH_ID in item[STATUS]:
                        vd_id = item[STATUS][VIRTUAL_DEPLOYMENT_ID]
                vs_dict = mesh_vdb_dict.get(mesh_id, {})
                vd_dict = vs_dict.get(vs_id, {})
                vdb_list = vd_dict.get(vd_id, [])
                vdb_list.append(namespace + "/" + name)
                vd_dict[vd_id] = vdb_list
                vs_dict[vs_id] = vd_dict
                mesh_vdb_dict[mesh_id] = vs_dict
        return mesh_vdb_dict

    def get_all_services(self):
        services_dict = {}
        all_services_args = ['kubectl', 'get', 'services', '--all-namespaces', '-o', 'json']
        kubectl_command_summary = self.run_command_as_subprocess(all_services_args)
        if kubectl_command_summary.return_code != 0:
            return services_dict

        services_string = kubectl_command_summary.stdout
        services = json.loads(services_string)
        if services is not None and ITEMS in services:
            for service in services[ITEMS]:
                services_dict[service[NAME]] = service[LABELS]
        return services_dict

    # Filter all pods with VDB annotation
    def filter_all_pods_related_to_vdbs(self):
        pod_dict = {}
        filter_pods_by_vdbs_args = ['kubectl', 'get', 'pods', '--all-namespaces', '-o', 'json']
        kubectl_command_summary = self.run_command_as_subprocess(filter_pods_by_vdbs_args)

        if kubectl_command_summary.return_code != 0:
            return pod_dict

        pods_string = kubectl_command_summary.stdout
        pods = json.loads(pods_string)
        vdb_ref_key = 'servicemesh.oci.oracle.com/virtual-deployment-binding-ref'

        if pods is not None and ITEMS in pods:
            for pod in pods[ITEMS]:

                # Capture vdb_key
                vdb_key = None
                if METADATA in pod:
                    if ANNOTATIONS in pod[METADATA]:
                        if vdb_ref_key not in pod[METADATA][ANNOTATIONS]:
                            continue
                        vdb_key = pod[METADATA][ANNOTATIONS][vdb_ref_key]

                if vdb_key is None:
                    continue

                # Capture name, namespace, labels
                name, namespace, labels = get_name_namespace_labels_from_pod_json(pod)

                # Capture status, proxy_status, proxy_version
                status, proxy_status, proxy_version = get_proxy_details_from_pod_json(pod)

                # VDB can have multiple pods
                vdb_pod_list = pod_dict.get(vdb_key, [])
                basic_pod_summary = BasicPodSummary(name=name,
                                                    namespace=namespace,
                                                    status=status,
                                                    labels=labels)
                new_pod_summary = PodSummary(proxy_status=proxy_status,
                                             proxy_version=proxy_version,
                                             basic_pod_summary=basic_pod_summary,
                                             pod_json=pod)

                vdb_pod_list.append(new_pod_summary)
                pod_dict[vdb_key] = vdb_pod_list

        return pod_dict

    # Filter all pods related to IGDs
    def filter_all_pods_related_to_igds(self):
        pod_dict = {}
        filter_pods_by_igds_args = ['kubectl', 'get', 'pods', '--all-namespaces', '-l', IGD_LABEL, '-o', 'json']
        kubectl_command_summary = self.run_command_as_subprocess(filter_pods_by_igds_args)

        if kubectl_command_summary.return_code != 0:
            return pod_dict

        pods_string = kubectl_command_summary.stdout
        pods_json = json.loads(pods_string)
        if pods_json is not None and ITEMS in pods_json:
            for pod in pods_json[ITEMS]:

                # Capture name, namespace, labels
                name, namespace, labels = get_name_namespace_labels_from_pod_json(pod)

                # Capture igd_key
                igd_key = None
                if METADATA in pod and namespace is not None:
                    if LABELS in pod[METADATA] and IGD_LABEL in pod[METADATA][LABELS]:
                        igd_key = namespace + '/' + pod[METADATA][LABELS][IGD_LABEL]

                if igd_key is None:
                    continue

                # Capture status, proxy_status, proxy_version
                status, proxy_status, proxy_version = get_proxy_details_from_pod_json(pod)

                # IGD can have multiple pods
                igd_pod_list = pod_dict.get(igd_key, [])
                basic_pod_summary = BasicPodSummary(name=name,
                                                    namespace=namespace,
                                                    status=status,
                                                    labels=labels)
                new_pod_summary = PodSummary(proxy_status=proxy_status,
                                             proxy_version=proxy_version,
                                             basic_pod_summary=basic_pod_summary,
                                             pod_json=pod)
                igd_pod_list.append(new_pod_summary)
                pod_dict[igd_key] = igd_pod_list

        return pod_dict

    # Filter IGDs by OCID
    def filter_igds_by_ocid(self, ocid):
        mesh_igd_dict = {}
        filter_type = self.get_resource_filter_type_id(ocid)
        get_igds_args = ['kubectl', 'get', 'ingressgatewaydeployments', '--all-namespaces', '-o', 'json']
        kubectl_command_summary = self.run_command_as_subprocess(get_igds_args)

        if kubectl_command_summary.return_code != 0:
            return mesh_igd_dict

        igds_string = kubectl_command_summary.stdout
        igds = json.loads(igds_string)
        if igds is not None and ITEMS in igds:
            for item in igds[ITEMS]:
                name, namespace = None, None
                mesh_id, ig_id = None, None
                if STATUS not in item or filter_type not in item[STATUS] or \
                        item[STATUS][filter_type] != ocid:
                    continue
                if METADATA in item:
                    if NAME in item[METADATA]:
                        name = item[METADATA][NAME]
                    if NAMESPACE in item[METADATA]:
                        namespace = item[METADATA][NAMESPACE]
                if STATUS in item:
                    if MESH_ID in item[STATUS]:
                        mesh_id = item[STATUS][MESH_ID]
                    if INGRESS_GATEWAY_ID in item[STATUS]:
                        ig_id = item[STATUS][INGRESS_GATEWAY_ID]
                ig_dict = mesh_igd_dict.get(mesh_id, {})
                igd_list = ig_dict.get(ig_id, [])
                igd_list.append(namespace + "/" + name)
                ig_dict[ig_id] = igd_list
                mesh_igd_dict[mesh_id] = ig_dict
        return mesh_igd_dict

    # Filters vdb, igd, vsrt, igrt
    def filter_mesh_resources_helper_by_filtered_list(self, crd, filter_dict):
        filter_list = filter_dict.keys()
        crd_dict = {}
        get_all_crd_args = ['kubectl', 'get', MESH_CRD_DICT[crd], '--all-namespaces', '-o', 'json']
        kubectl_command_summary = self.run_command_as_subprocess(get_all_crd_args)
        if kubectl_command_summary.return_code != 0:
            return crd_dict
        resources_string = kubectl_command_summary.stdout
        resources = json.loads(resources_string)
        if resources is not None and ITEMS in resources:
            for resource in resources[ITEMS]:
                if STATUS in resource:
                    ocid = None
                    if crd in ['meshvirtualserviceroutetable', 'meshvirtualdeploymentbinding'] and \
                            VIRTUAL_SERVICE_ID in resource[STATUS]:
                        ocid = resource[STATUS][VIRTUAL_SERVICE_ID]
                    elif crd in ['meshingressgatewayroutetable', 'meshingressgatewaydeployment'] and \
                            INGRESS_GATEWAY_ID in resource[STATUS]:
                        ocid = resource[STATUS][INGRESS_GATEWAY_ID]
                    if ocid is not None and ocid in filter_list:
                        custom_resource_summary = CustomResourceSummary(resource)
                        crd_list = crd_dict.get(ocid, [])
                        crd_list.append(custom_resource_summary)
                        crd_dict[ocid] = crd_list
        return crd_dict

    # Filters mesh, vs, vd, ig, ap related to mesh_id
    def filter_mesh_resources_helper(self, mesh_id, crd):
        crd_dict = {}
        get_all_crd_args = ['kubectl', 'get', MESH_CRD_DICT[crd], '--all-namespaces', '-o', 'json']
        kubectl_command_summary = self.run_command_as_subprocess(get_all_crd_args)
        if kubectl_command_summary.return_code != 0:
            return crd_dict
        resources_string = kubectl_command_summary.stdout
        resources = json.loads(resources_string)
        if resources is not None and ITEMS in resources:
            for resource in resources[ITEMS]:
                if STATUS not in resource or MESH_CUSTOM_RESOURCE_DICT[crd] not in resource[STATUS]:
                    continue
                ocid = resource[STATUS][MESH_CUSTOM_RESOURCE_DICT[crd]]
                if MESH_ID in resource[STATUS] and mesh_id == resource[STATUS][MESH_ID]:
                    custom_resource_summary = CustomResourceSummary(resource)
                    crd_list = crd_dict.get(ocid, [])
                    crd_list.append(custom_resource_summary)
                    crd_dict[ocid] = crd_list
        return crd_dict

    # Parallel filter mesh resources related to mesh_id
    def parallel_filter_mesh_resources(self, mesh_id):
        with concurrent.futures.ProcessPoolExecutor() as independent_executor:
            mesh_process = independent_executor.submit(self.filter_mesh_resources_helper, mesh_id, 'mesh')
            vs_process = independent_executor.submit(self.filter_mesh_resources_helper, mesh_id, 'meshvirtualservice')
            vd_process = independent_executor.submit(self.filter_mesh_resources_helper, mesh_id,
                                                     'meshvirtualdeployment')
            ap_process = independent_executor.submit(self.filter_mesh_resources_helper, mesh_id, 'meshaccesspolicy')
            ig_process = independent_executor.submit(self.filter_mesh_resources_helper, mesh_id, 'meshingressgateway')

        vd_dict = vd_process.result()
        ig_dict = ig_process.result()

        with concurrent.futures.ProcessPoolExecutor() as dependent_executor:
            vdb_process = dependent_executor.submit(self.filter_mesh_resources_helper_by_filtered_list,
                                                    'meshvirtualdeploymentbinding', vd_dict)
            vsrt_process = dependent_executor.submit(self.filter_mesh_resources_helper_by_filtered_list,
                                                     'meshvirtualserviceroutetable', vd_dict)
            igd_process = dependent_executor.submit(self.filter_mesh_resources_helper_by_filtered_list,
                                                    'meshingressgatewaydeployment', ig_dict)
            igrt_process = dependent_executor.submit(self.filter_mesh_resources_helper_by_filtered_list,
                                                     'meshingressgatewayroutetable', ig_dict)

        mesh_dict = mesh_process.result()
        vs_dict = vs_process.result()
        ap_dict = ap_process.result()
        vdb_dict = vdb_process.result()
        vsrt_dict = vsrt_process.result()
        igd_dict = igd_process.result()
        igrt_dict = igrt_process.result()

        return MeshResources(mesh_dict, vs_dict, vd_dict, vdb_dict, vsrt_dict, ig_dict, igd_dict, igrt_dict, ap_dict)

    # Calculate time difference
    def calculate_time(self, start_time, message):
        click.echo('\nTime taken for {} is: {}s'.format(message, time.time() - start_time))

    # Returns kubectl version if installed
    def get_kubectl_version(self):
        # Check if kubectl client is present
        kubectl_version_args = ['kubectl', 'version', '--short']
        return self.run_command_as_subprocess(kubectl_version_args)

    # Checks for kubectl installation
    def is_kubectl_installed(self):
        # Check if kubectl client is present
        return self.get_kubectl_version()

    # Gets all the contexts present in the given config file
    def get_command_context(self, kube_config_path=None, context_name=None):
        if context_name is None:
            context_args = ['kubectl', 'config', 'current-context']
        else:
            context_args = ['kubectl', 'config', 'get-contexts', '-o', 'name', context_name]

        if kube_config_path is not None:
            context_args.append('--kubeconfig')
            context_args.append(kube_config_path)

        return self.run_command_as_subprocess(context_args)

    def check_context(self, k8s_context):
        kube_config_path, use_context = k8s_context
        if kube_config_path is None:
            kube_command_summary = self.get_command_context(context_name=use_context)
            if kube_command_summary.return_code != 0:
                error = Messages.context_not_available + kube_command_summary.stderr
                return KubectlCommandSummary(return_code=1, stderr=error)
            else:
                click.echo(Messages.using_context.format(kube_command_summary.stdout),
                           file=sys.stdout)
                return kube_command_summary
        else:
            if not os.path.exists(kube_config_path):
                error = 'Invalid path: {} provided for k8s_context. Please check if the path points to a valid config.' \
                    .format(kube_config_path)
                return KubectlCommandSummary(return_code=1, stderr=error)
            else:
                kube_command_summary = self.get_command_context(kube_config_path=kube_config_path,
                                                                context_name=use_context)
                if kube_command_summary.return_code != 0:
                    error = 'Unable to load context from the provided k8s_context. ' + kube_command_summary.stderr
                    return KubectlCommandSummary(return_code=1, stderr=error)
                else:
                    click.echo(Messages.using_context.format(kube_command_summary.stdout), file=sys.stdout)
                    return kube_command_summary


class KubectlCommandSummary:

    def __init__(self, return_code, stdout=None, stderr=None):
        self.return_code = return_code
        self.stdout = stdout
        self.stderr = stderr

    def __str__(self):
        contents = StringIO()
        contents.write('\nReturn Code: {}'.format(self.return_code))
        contents.write('\nstdout: \n{}'.format(self.stdout))
        contents.write('\nstderr: \n{}'.format(self.stderr))
        return contents.getvalue()
