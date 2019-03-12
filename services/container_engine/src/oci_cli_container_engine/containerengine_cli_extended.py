# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from oci_cli import cli_util
from oci_cli_container_engine.generated import containerengine_cli
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
import click
import six
import os
import yaml

DEFAULT_KUBECONFIG_LOCATION = os.path.join('~', '.kube', 'config')
cli_util.rename_command(containerengine_cli.work_request_log_entry_group, containerengine_cli.list_work_request_logs, "list")


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


# create-kubeconfig command is overridden here to provide the following functionality:
# 1. Running the CLI command ‘oci ce cluster create-kubeconfig --cluster-id <CLUSTER-ID>’
# for obtaining kubeconfig always ‘merges’ the new kubeconfig information with the current kubeconfig in formation at
# the default location ($HOME/.kube/) and under the file name ‘config’. If there is no kubeconfig file at the default
# location, a new one is created with the name ‘config’.
# 2. Changing --file flag value to a different location path in the CLI command
# ‘oci ce cluster create-kubeconfig --cluster-id <CLUSTER-ID> --file <custom_location>’
# always ‘merges’the new kubeconfig information with the current kubeconfig information at the destination or create a
# new one, if it does not exist.
# 3. Running CLI command to obtain new kubeconfig always sets the default context to the new cluster.
# 4. A ‘merged’ kubeconfig file does not have any duplicates and the information is not lost or corrupted in any way.
@cli_util.copy_params_from_generated_command(containerengine_cli.create_kubeconfig, params_to_exclude=['file'])
@containerengine_cli.cluster_group.command(name=cli_util.override('create_kubeconfig.command_name', 'create-kubeconfig'),
                                           help="""Create the Kubeconfig YAML for a cluster.""")
@cli_util.option('--file', type=click.Path(), default=DEFAULT_KUBECONFIG_LOCATION, show_default=True,
                 help="The name of the file that will be updated with response data, or '-' to write to STDOUT.")
@cli_util.option('--overwrite', is_flag=True, help="""Overwrites the contents of kubeconfig file specified using --file\
 option or kubeconfig file at default location if --file is not used.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_kubeconfig(ctx, from_json, file, cluster_id, token_version, expiration, overwrite):

    if isinstance(cluster_id, six.string_types) and len(cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if token_version is not None:
        details['tokenVersion'] = token_version

    if expiration is not None:
        details['expiration'] = expiration

    client = cli_util.build_client('container_engine', ctx)
    result = client.create_kubeconfig(
        cluster_id=cluster_id,
        create_cluster_kubeconfig_content_details=details,
        **kwargs
    )

    # kubeconfig is received in binary format.
    new_kubeconfig = b''
    for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
        new_kubeconfig = b''.join([new_kubeconfig, chunk])

    file = os.path.expandvars(os.path.expanduser(file))
    # If the user wants stdout; just print it after decoding in utf-8 format.
    if file == '-':
        click.echo(new_kubeconfig.decode('utf-8'))
    # If user wants to overwrite the existing kubeconfig OR there exists no kubeconfig with the user given file name,
    # in both the above cases, overwrite the new config returned by the command in the kubeconfig
    elif overwrite or not os.path.isfile(file):
        if os.path.dirname(file) and not os.path.exists(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))
        with open((file), 'wb') as f:
            f.write(new_kubeconfig)
            click.echo('New config written to the Kubeconfig file {}'.format(file))
    # If overwrite is not set and a kubeconfig already exists, then the new config is merged with the existing one
    else:
        _merge_kubeconfig(new_kubeconfig, file)
        click.echo('Existing Kubeconfig file found at {} and new config merged into it'.format(file))


def _merge_kubeconfig(new_kubeconfig, file):

    # This is only called when the file exists so no need to check for IOError on file open/read.
    with open(file, 'rb+') as f:
        # If the file is empty, just write the new config and return
        if os.stat(file).st_size == 0:
            f.write(new_kubeconfig)
            return
        # Read the existing kubeconfig in yaml format and load it as python object
        existing_kubeconfig = f.read()
        try:
            existing_kubeconfig_yaml = yaml.safe_load(existing_kubeconfig)
            new_kubeconfig_yaml = yaml.safe_load(new_kubeconfig)
        except yaml.YAMLError as e:
            click.echo('Error parsing configuration file {}'.format(e))
            return
        # Merge the root level keys which have no nesting. Pick the values coming from the new downloaded kubeconfig
        # returned by this command during merge.
        kubeconfig_keys_to_copy = [
            'apiVersion',
            'kind',
            'preferences',
            'current-context'
        ]
        for key in kubeconfig_keys_to_copy:
            if key in new_kubeconfig_yaml:
                existing_kubeconfig_yaml[key] = new_kubeconfig_yaml[key]
        # Merge clusters, contexts and users.
        _merge_kubeconfig_yaml(existing_kubeconfig_yaml, new_kubeconfig_yaml, 'clusters')
        _merge_kubeconfig_yaml(existing_kubeconfig_yaml, new_kubeconfig_yaml, 'contexts')
        _merge_kubeconfig_yaml(existing_kubeconfig_yaml, new_kubeconfig_yaml, 'users')
    # Open the file again for writing the merged kubeconfig
    with open(file, 'wb') as f:
        yaml.dump(existing_kubeconfig_yaml, f, encoding='utf-8', default_flow_style=False)


def _merge_kubeconfig_yaml(dst_yaml, src_yaml, merge_key):
    if src_yaml[merge_key] is None:
        return
    tmp_yaml = dict(dst_yaml)
    for i in src_yaml[merge_key]:
        match = False
        for idx, j in enumerate(tmp_yaml[merge_key]):
            # The match for clusters/contexts/users is determined from the unique key "name" within them.
            if i['name'] == j['name']:
                # It is either an update or repeat of an existing record so we need to update the existing record with
                # new one
                match = True
                dst_yaml[merge_key][idx] = i
        if not match:
            # It is a new record so we need to add it to the list
            dst_yaml[merge_key].append(i)
