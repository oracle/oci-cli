# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .. import cli_util
from ..generated import containerengine_cli
from .. import json_skeleton_utils
from .. import custom_types  # noqa: F401
import click


@cli_util.copy_params_from_generated_command(containerengine_cli.create_cluster, params_to_exclude=['options'],
                                             copy_from_json=False)
@containerengine_cli.cluster_group.command(name=cli_util.override('create_cluster.command_name', 'create'),
                                           help="""Create a new cluster.""")
@cli_util.option('--service-lb-subnet-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""The two subnets\
 configured to host load balancers in a Kubernetes cluster.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dashboard-enabled', type=click.BOOL, help="""Select if you want to use the Kubernetes Dashboard to\
 deploy and troubleshoot containerized applications, and to manage Kubernetes resources. Default value is true.""")
@cli_util.option('--tiller-enabled', type=click.BOOL, help="""Select if you want Tiller (the server portion of Helm)\
 to run in the Kubernetes cluster. Default value is true.""")
@cli_util.option('--pods-cidr', help="""The available group of network addresses that can be allocated to pods running\
 in the cluster, expressed as a single, contiguous IPv4 CIDR block. For example, 10.244.0.0/16.""")
@cli_util.option('--services-cidr', help="""The available group of network addresses that can be exposed as Kubernetes\
 services (ClusterIPs), expressed as a single, contiguous IPv4 CIDR block. For example, 10.96.0.0/16.""")
@json_skeleton_utils.get_cli_json_input_option({'service-lb-subnet-ids': {'module': 'container_engine', 'class': 'list[string]'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'service-lb-subnet-ids': {'module': 'container_engine', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_cluster(ctx, **kwargs):

    kwargs['options'] = {}
    if 'service_lb_subnet_ids' in kwargs and kwargs['service_lb_subnet_ids'] is not None:
        kwargs['options'] = {'serviceLbSubnetIds': cli_util.parse_json_parameter("service_lb_subnet_ids",
                                                                                 kwargs['service_lb_subnet_ids'])}
    kwargs.pop('service_lb_subnet_ids', None)

    if 'dashboard_enabled' in kwargs and kwargs['dashboard_enabled'] is not None:
        kwargs['options']['addOns'] = {}
        kwargs['options']['addOns']['isKubernetesDashboardEnabled'] = kwargs['dashboard_enabled']
    kwargs.pop('dashboard_enabled', None)

    if 'tiller_enabled' in kwargs and kwargs['tiller_enabled'] is not None:
        if 'addOns' not in kwargs['options']:
            kwargs['options']['addOns'] = {}
        kwargs['options']['addOns']['isTillerEnabled'] = kwargs['tiller_enabled']
    kwargs.pop('tiller_enabled', None)

    if 'pods_cidr' in kwargs and kwargs['pods_cidr'] is not None:
        kwargs['options']['kubernetesNetworkConfig'] = {}
        kwargs['options']['kubernetesNetworkConfig']['podsCidr'] = kwargs['pods_cidr']
    kwargs.pop('pods_cidr', None)

    if 'services_cidr' in kwargs and kwargs['services_cidr'] is not None:
        if 'kubernetesNetworkConfig' not in kwargs['options']:
            kwargs['options']['kubernetesNetworkConfig'] = {}
        kwargs['options']['kubernetesNetworkConfig']['servicesCidr'] = kwargs['services_cidr']
    kwargs.pop('services_cidr', None)

    # It seems like the service needs options param even if it is empty so leave it when invoking the create command

    ctx.invoke(containerengine_cli.create_cluster, **kwargs)
