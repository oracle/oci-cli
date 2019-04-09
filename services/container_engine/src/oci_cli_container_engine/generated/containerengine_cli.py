# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('ce_root_group.command_name', 'ce'), cls=CommandGroupWithAlias, help=cli_util.override('ce_root_group.help', """API for the Container Engine for Kubernetes service. Use this API to build, deploy,
and manage cloud-native applications. For more information, see
[Overview of Container Engine for Kubernetes](/iaas/Content/ContEng/Concepts/contengoverview.htm).
"""), short_help=cli_util.override('ce_root_group.short_help', """Container Engine for Kubernetes API"""))
@cli_util.help_option_group
def ce_root_group():
    pass


@click.command(cli_util.override('cluster_group.command_name', 'cluster'), cls=CommandGroupWithAlias, help="""A Kubernetes cluster. Avoid entering confidential information.""")
@cli_util.help_option_group
def cluster_group():
    pass


@click.command(cli_util.override('work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""Errors related to a specific work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('node_pool_options_group.command_name', 'node-pool-options'), cls=CommandGroupWithAlias, help="""Options for creating or updating node pools.""")
@cli_util.help_option_group
def node_pool_options_group():
    pass


@click.command(cli_util.override('work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""Log entries related to a specific work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('node_pool_group.command_name', 'node-pool'), cls=CommandGroupWithAlias, help="""A pool of compute nodes attached to a cluster. Avoid entering confidential information.""")
@cli_util.help_option_group
def node_pool_group():
    pass


@click.command(cli_util.override('work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""An asynchronous work request.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('cluster_options_group.command_name', 'cluster-options'), cls=CommandGroupWithAlias, help="""Options for creating or updating clusters.""")
@cli_util.help_option_group
def cluster_options_group():
    pass


ce_root_group.add_command(cluster_group)
ce_root_group.add_command(work_request_error_group)
ce_root_group.add_command(node_pool_options_group)
ce_root_group.add_command(work_request_log_entry_group)
ce_root_group.add_command(node_pool_group)
ce_root_group.add_command(work_request_group)
ce_root_group.add_command(cluster_options_group)


@cluster_group.command(name=cli_util.override('create_cluster.command_name', 'create'), help=u"""Create a new cluster.""")
@cli_util.option('--name', required=True, help=u"""The name of the cluster. Avoid entering confidential information.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which to create the cluster.""")
@cli_util.option('--vcn-id', required=True, help=u"""The OCID of the virtual cloud network (VCN) in which to create the cluster.""")
@cli_util.option('--kubernetes-version', required=True, help=u"""The version of Kubernetes to install into the cluster masters.""")
@cli_util.option('--options', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Optional attributes for the cluster.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'options': {'module': 'container_engine', 'class': 'ClusterCreateOptions'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'options': {'module': 'container_engine', 'class': 'ClusterCreateOptions'}})
@cli_util.wrap_exceptions
def create_cluster(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, name, compartment_id, vcn_id, kubernetes_version, options):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['name'] = name
    details['compartmentId'] = compartment_id
    details['vcnId'] = vcn_id
    details['kubernetesVersion'] = kubernetes_version

    if options is not None:
        details['options'] = cli_util.parse_json_parameter("options", options)

    client = cli_util.build_client('container_engine', ctx)
    result = client.create_cluster(
        create_cluster_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cluster_group.command(name=cli_util.override('create_kubeconfig.command_name', 'create-kubeconfig'), help=u"""Create the Kubeconfig YAML for a cluster.""")
@cli_util.option('--cluster-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--token-version', help=u"""The version of the kubeconfig token.""")
@cli_util.option('--expiration', type=click.INT, help=u"""The desired expiration, in seconds, to use for the kubeconfig token.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_kubeconfig(ctx, from_json, file, cluster_id, token_version, expiration):

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

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@node_pool_group.command(name=cli_util.override('create_node_pool.command_name', 'create'), help=u"""Create a new node pool.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment in which the node pool exists.""")
@cli_util.option('--cluster-id', required=True, help=u"""The OCID of the cluster to which this node pool is attached.""")
@cli_util.option('--name', required=True, help=u"""The name of the node pool. Avoid entering confidential information.""")
@cli_util.option('--kubernetes-version', required=True, help=u"""The version of Kubernetes to install on the nodes in the node pool.""")
@cli_util.option('--node-image-name', required=True, help=u"""The name of the image running on the nodes in the node pool.""")
@cli_util.option('--node-shape', required=True, help=u"""The name of the node shape of the nodes in the node pool.""")
@cli_util.option('--subnet-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The OCIDs of the subnets in which to place nodes for this node pool.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--node-metadata', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of key/value pairs to add to each underlying OCI instance in the node pool.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--initial-node-labels', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of key/value pairs to add to nodes after they join the Kubernetes cluster.

This option is a JSON list with items of type KeyValue.  For documentation on KeyValue please see our API reference: https://docs.cloud.oracle.com/api/#/en/containerengine/20180222/datatypes/KeyValue.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--ssh-public-key', help=u"""The SSH public key to add to each node in the node pool.""")
@cli_util.option('--quantity-per-subnet', type=click.INT, help=u"""The number of nodes to create in each subnet.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'node-metadata': {'module': 'container_engine', 'class': 'dict(str, string)'}, 'initial-node-labels': {'module': 'container_engine', 'class': 'list[KeyValue]'}, 'subnet-ids': {'module': 'container_engine', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'node-metadata': {'module': 'container_engine', 'class': 'dict(str, string)'}, 'initial-node-labels': {'module': 'container_engine', 'class': 'list[KeyValue]'}, 'subnet-ids': {'module': 'container_engine', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_node_pool(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, cluster_id, name, kubernetes_version, node_image_name, node_shape, subnet_ids, node_metadata, initial_node_labels, ssh_public_key, quantity_per_subnet):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}
    details['compartmentId'] = compartment_id
    details['clusterId'] = cluster_id
    details['name'] = name
    details['kubernetesVersion'] = kubernetes_version
    details['nodeImageName'] = node_image_name
    details['nodeShape'] = node_shape
    details['subnetIds'] = cli_util.parse_json_parameter("subnet_ids", subnet_ids)

    if node_metadata is not None:
        details['nodeMetadata'] = cli_util.parse_json_parameter("node_metadata", node_metadata)

    if initial_node_labels is not None:
        details['initialNodeLabels'] = cli_util.parse_json_parameter("initial_node_labels", initial_node_labels)

    if ssh_public_key is not None:
        details['sshPublicKey'] = ssh_public_key

    if quantity_per_subnet is not None:
        details['quantityPerSubnet'] = quantity_per_subnet

    client = cli_util.build_client('container_engine', ctx)
    result = client.create_node_pool(
        create_node_pool_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@cluster_group.command(name=cli_util.override('delete_cluster.command_name', 'delete'), help=u"""Delete a cluster.""")
@cli_util.option('--cluster-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_cluster(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, cluster_id, if_match):

    if isinstance(cluster_id, six.string_types) and len(cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('container_engine', ctx)
    result = client.delete_cluster(
        cluster_id=cluster_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@node_pool_group.command(name=cli_util.override('delete_node_pool.command_name', 'delete'), help=u"""Delete a node pool.""")
@cli_util.option('--node-pool-id', required=True, help=u"""The OCID of the node pool.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_node_pool(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, node_pool_id, if_match):

    if isinstance(node_pool_id, six.string_types) and len(node_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --node-pool-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('container_engine', ctx)
    result = client.delete_node_pool(
        node_pool_id=node_pool_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('delete_work_request.command_name', 'delete'), help=u"""Cancel a work request that has not started.""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_work_request(ctx, from_json, work_request_id, if_match):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('container_engine', ctx)
    result = client.delete_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cluster_group.command(name=cli_util.override('get_cluster.command_name', 'get'), help=u"""Get the details of a cluster.""")
@cli_util.option('--cluster-id', required=True, help=u"""The OCID of the cluster.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'container_engine', 'class': 'Cluster'})
@cli_util.wrap_exceptions
def get_cluster(ctx, from_json, cluster_id):

    if isinstance(cluster_id, six.string_types) and len(cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('container_engine', ctx)
    result = client.get_cluster(
        cluster_id=cluster_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cluster_options_group.command(name=cli_util.override('get_cluster_options.command_name', 'get'), help=u"""Get options available for clusters.""")
@cli_util.option('--cluster-option-id', required=True, help=u"""The id of the option set to retrieve. Only \"all\" is supported.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'container_engine', 'class': 'ClusterOptions'})
@cli_util.wrap_exceptions
def get_cluster_options(ctx, from_json, cluster_option_id):

    if isinstance(cluster_option_id, six.string_types) and len(cluster_option_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-option-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('container_engine', ctx)
    result = client.get_cluster_options(
        cluster_option_id=cluster_option_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@node_pool_group.command(name=cli_util.override('get_node_pool.command_name', 'get'), help=u"""Get the details of a node pool.""")
@cli_util.option('--node-pool-id', required=True, help=u"""The OCID of the node pool.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'container_engine', 'class': 'NodePool'})
@cli_util.wrap_exceptions
def get_node_pool(ctx, from_json, node_pool_id):

    if isinstance(node_pool_id, six.string_types) and len(node_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --node-pool-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('container_engine', ctx)
    result = client.get_node_pool(
        node_pool_id=node_pool_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@node_pool_options_group.command(name=cli_util.override('get_node_pool_options.command_name', 'get'), help=u"""Get options available for node pools.""")
@cli_util.option('--node-pool-option-id', required=True, help=u"""The id of the option set to retrieve. Use \"all\" get all options, or use a cluster ID to get options specific to the provided cluster.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'container_engine', 'class': 'NodePoolOptions'})
@cli_util.wrap_exceptions
def get_node_pool_options(ctx, from_json, node_pool_option_id):

    if isinstance(node_pool_option_id, six.string_types) and len(node_pool_option_id.strip()) == 0:
        raise click.UsageError('Parameter --node-pool-option-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('container_engine', ctx)
    result = client.get_node_pool_options(
        node_pool_option_id=node_pool_option_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('get_work_request.command_name', 'get'), help=u"""Get the details of a work request.""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'container_engine', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('container_engine', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@cluster_group.command(name=cli_util.override('list_clusters.command_name', 'list'), help=u"""List all the cluster objects in a compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "FAILED", "DELETING", "DELETED", "UPDATING"]), multiple=True, help=u"""A cluster lifecycle state to filter on. Can have multiple parameters of this name.""")
@cli_util.option('--name', help=u"""The name to filter on.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The optional order in which to sort the results.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["ID", "NAME", "TIME_CREATED"]), help=u"""The optional field to sort the results by.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'container_engine', 'class': 'list[ClusterSummary]'})
@cli_util.wrap_exceptions
def list_clusters(ctx, from_json, all_pages, page_size, compartment_id, lifecycle_state, name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if lifecycle_state is not None and len(lifecycle_state) > 0:
        kwargs['lifecycle_state'] = lifecycle_state
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('container_engine', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_clusters,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_clusters,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_clusters(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@node_pool_group.command(name=cli_util.override('list_node_pools.command_name', 'list'), help=u"""List all the node pools in a compartment, and optionally filter by cluster.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--cluster-id', help=u"""The OCID of the cluster.""")
@cli_util.option('--name', help=u"""The name to filter on.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The optional order in which to sort the results.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["ID", "NAME", "TIME_CREATED"]), help=u"""The optional field to sort the results by.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'container_engine', 'class': 'list[NodePoolSummary]'})
@cli_util.wrap_exceptions
def list_node_pools(ctx, from_json, all_pages, page_size, compartment_id, cluster_id, name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if cluster_id is not None:
        kwargs['cluster_id'] = cluster_id
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('container_engine', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_node_pools,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_node_pools,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_node_pools(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('list_work_request_errors.command_name', 'list'), help=u"""Get the errors of a work request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'container_engine', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, compartment_id, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('container_engine', ctx)
    result = client.list_work_request_errors(
        compartment_id=compartment_id,
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Get the logs of a work request.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'container_engine', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, compartment_id, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('container_engine', ctx)
    result = client.list_work_request_logs(
        compartment_id=compartment_id,
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('list_work_requests.command_name', 'list'), help=u"""List all work requests in a compartment.""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--cluster-id', help=u"""The OCID of the cluster.""")
@cli_util.option('--resource-id', help=u"""The OCID of the resource associated with a work request""")
@cli_util.option('--resource-type', type=custom_types.CliCaseInsensitiveChoice(["CLUSTER", "NODEPOOL"]), help=u"""Type of the resource associated with a work request""")
@cli_util.option('--status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help=u"""A work request status to filter on. Can have multiple parameters of this name.""")
@cli_util.option('--limit', type=click.INT, help=u"""For list pagination. The maximum number of results per page, or items to return in a paginated \"List\" call. 1 is the minimum, 1000 is the maximum. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--page', help=u"""For list pagination. The value of the `opc-next-page` response header from the previous \"List\" call. For important details about how pagination works, see [List Pagination].""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The optional order in which to sort the results.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["ID", "OPERATION_TYPE", "STATUS", "TIME_ACCEPTED", "TIME_STARTED", "TIME_FINISHED"]), help=u"""The optional field to sort the results by.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'container_engine', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, cluster_id, resource_id, resource_type, status, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if cluster_id is not None:
        kwargs['cluster_id'] = cluster_id
    if resource_id is not None:
        kwargs['resource_id'] = resource_id
    if resource_type is not None:
        kwargs['resource_type'] = resource_type
    if status is not None and len(status) > 0:
        kwargs['status'] = status
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('container_engine', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@cluster_group.command(name=cli_util.override('update_cluster.command_name', 'update'), help=u"""Update the details of a cluster.""")
@cli_util.option('--cluster-id', required=True, help=u"""The OCID of the cluster.""")
@cli_util.option('--name', help=u"""The new name for the cluster. Avoid entering confidential information.""")
@cli_util.option('--kubernetes-version', help=u"""The version of Kubernetes to which the cluster masters should be upgraded.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def update_cluster(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, cluster_id, name, kubernetes_version, if_match):

    if isinstance(cluster_id, six.string_types) and len(cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if name is not None:
        details['name'] = name

    if kubernetes_version is not None:
        details['kubernetesVersion'] = kubernetes_version

    client = cli_util.build_client('container_engine', ctx)
    result = client.update_cluster(
        cluster_id=cluster_id,
        update_cluster_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@node_pool_group.command(name=cli_util.override('update_node_pool.command_name', 'update'), help=u"""Update the details of a node pool.""")
@cli_util.option('--node-pool-id', required=True, help=u"""The OCID of the node pool.""")
@cli_util.option('--name', help=u"""The new name for the cluster. Avoid entering confidential information.""")
@cli_util.option('--kubernetes-version', help=u"""The version of Kubernetes to which the nodes in the node pool should be upgraded.""")
@cli_util.option('--quantity-per-subnet', type=click.INT, help=u"""The number of nodes to ensure in each subnet.""")
@cli_util.option('--initial-node-labels', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of key/value pairs to add to nodes after they join the Kubernetes cluster.

This option is a JSON list with items of type KeyValue.  For documentation on KeyValue please see our API reference: https://docs.cloud.oracle.com/api/#/en/containerengine/20180222/datatypes/KeyValue.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--subnet-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The OCIDs of the subnets in which to place nodes for this node pool.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'initial-node-labels': {'module': 'container_engine', 'class': 'list[KeyValue]'}, 'subnet-ids': {'module': 'container_engine', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'initial-node-labels': {'module': 'container_engine', 'class': 'list[KeyValue]'}, 'subnet-ids': {'module': 'container_engine', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_node_pool(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, node_pool_id, name, kubernetes_version, quantity_per_subnet, initial_node_labels, subnet_ids, if_match):

    if isinstance(node_pool_id, six.string_types) and len(node_pool_id.strip()) == 0:
        raise click.UsageError('Parameter --node-pool-id cannot be whitespace or empty string')
    if not force:
        if initial_node_labels or subnet_ids:
            if not click.confirm("WARNING: Updates to initial-node-labels and subnet-ids will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if name is not None:
        details['name'] = name

    if kubernetes_version is not None:
        details['kubernetesVersion'] = kubernetes_version

    if quantity_per_subnet is not None:
        details['quantityPerSubnet'] = quantity_per_subnet

    if initial_node_labels is not None:
        details['initialNodeLabels'] = cli_util.parse_json_parameter("initial_node_labels", initial_node_labels)

    if subnet_ids is not None:
        details['subnetIds'] = cli_util.parse_json_parameter("subnet_ids", subnet_ids)

    client = cli_util.build_client('container_engine', ctx)
    result = client.update_node_pool(
        node_pool_id=node_pool_id,
        update_node_pool_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
