# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci_cli import cli_util
from services.container_engine.src.oci_cli_container_engine.generated import containerengine_cli
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci._vendor.requests import Request
from oci.auth.signers import InstancePrincipalsDelegationTokenSigner
import click
import json
import os
import yaml
import base64
from datetime import datetime, timedelta

DEFAULT_KUBECONFIG_LOCATION = os.path.join('~', '.kube', 'config')
cli_util.rename_command(containerengine_cli, containerengine_cli.work_request_log_entry_group, containerengine_cli.list_work_request_logs,
                        "list")

cli_util.rename_command(containerengine_cli, containerengine_cli.cluster_group, containerengine_cli.update_cluster_endpoint_config, "update-endpoint-config")

containerengine_cli.node_pool_group.commands.pop(containerengine_cli.create_node_pool_node_source_via_image_details.name)
containerengine_cli.node_pool_group.commands.pop(containerengine_cli.update_node_pool_node_source_via_image_details.name)


@containerengine_cli.cluster_group.command(name=cli_util.override('generate_token.command_name', 'generate-token'),
                                           help=u"""Generate an ExecCredential based token for Kubernetes SDK/CLI authentication.""")
@cli_util.option('--cluster-id', required=True, help=u"""The OCID of the cluster.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def generate_token(ctx, from_json, cluster_id):
    if isinstance(cluster_id, str) and len(cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-id cannot be whitespace or empty string')

    client = cli_util.build_client('container_engine', 'container_engine', ctx)
    signer = client.base_client.signer

    url = "https://containerengine.%s.oraclecloud.com/cluster_request/%s" % (ctx.obj['config']['region'], cluster_id)

    # Create the presigned request that we need to sign.
    # The output of this signed request will be used to build the token.
    request = signer.do_request_sign(Request(
        "GET",
        url,
    ).prepare())

    # Now that we have the signed request we need to turn it into
    # the base64 encoded token that OKE will authenticate.

    header_params = {
        "authorization": request.headers["authorization"],
        "date": request.headers["date"],
    }

    if isinstance(signer, InstancePrincipalsDelegationTokenSigner):
        header_params['opc-obo-token'] = signer.delegation_token

    token_request = Request(
        "GET",
        url,
        params=header_params,
    ).prepare()

    # Generate the ExecCredential that the Kubernetes exec plugin provide requires.
    # https://kubernetes.io/docs/reference/access-authn-authz/authentication/#input-and-output-formats

    token = base64.urlsafe_b64encode(token_request.url.encode('utf-8')).decode('utf-8')
    # Get now+4 minutes in RFC3339 format.
    # This informs Kubernetes SDK/CLIs that it's time to refresh the token
    # before the token is actually expired.
    expiration_timestamp = (datetime.utcnow() + timedelta(minutes=4)).isoformat('T') + "Z"

    exec_credential = """
{
    "apiVersion": "client.authentication.k8s.io/v1beta1",
    "kind": "ExecCredential",
    "status": {
        "token": "%s",
        "expirationTimestamp": "%s"
    }
}
    """ % (token, expiration_timestamp)
    click.echo(exec_credential)


containerengine_cli.cluster_group.add_command(generate_token)


@cli_util.copy_params_from_generated_command(containerengine_cli.create_cluster, params_to_exclude=['options', 'endpoint_config'],
                                             copy_from_json=False)
@containerengine_cli.cluster_group.command(name=cli_util.override('create_cluster.command_name', 'create'),
                                           help="""Create a new cluster.""")
@cli_util.option('--service-lb-subnet-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""The two subnets\
 configured to host load balancers in a Kubernetes cluster.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--dashboard-enabled', type=click.BOOL, help="""Select if you want to use the Kubernetes Dashboard to\
 deploy and troubleshoot containerized applications, and to manage Kubernetes resources. Default value is false.""")
@cli_util.option('--tiller-enabled', type=click.BOOL, help="""Select if you want Tiller (the server portion of Helm)\
 to run in the Kubernetes cluster. Default value is false.""")
@cli_util.option('--oidc-issuer-url', help="""URL of the provider that allows the API server to discover public signing keys.
            Only URLs that use the https:// scheme are accepted. This is typically the provider's discovery URL,
            changed to have an empty path.""")
@cli_util.option('--oidc-client-id', help="""A client id that all tokens must be issued for.""")
@cli_util.option('--oidc-configuration-file', help="""A base64 encoded string of kubernetes oidc auth configuration file.""")
@cli_util.option('--oidc-username-claim', help="""JWT claim to use as the user name. By default sub, which is expected to be a unique identifier of the end
            user. Admins can choose other claims, such as email or name, depending on their provider. However, claims
            other than email will be prefixed with the issuer URL to prevent naming clashes with other plugins.""")
@cli_util.option('--oidc-username-prefix', help="""Prefix prepended to username claims to prevent clashes with existing names (such as system:users).
            For example, the value oidc: will create usernames like oidc:jane.doe. If this flag isn't provided and
            --oidc-username-claim is a value other than email the prefix defaults to ( Issuer URL )# where
            ( Issuer URL ) is the value of --oidc-issuer-url. The value - can be used to disable all prefixing.""")
@cli_util.option('--oidc-groups-claim', help="""JWT claim to use as the user's group. If the claim is present it must be an array of strings.""")
@cli_util.option('--oidc-groups-prefix', help="""Prefix prepended to group claims to prevent clashes with existing names (such as system:groups).""")
@cli_util.option('--oidc-required-claims', type=custom_types.CLI_COMPLEX_TYPE, help="""A key=value pair that describes a required claim in the ID Token. If set, the claim is verified to be present
            in the ID Token with a matching value. Repeat this flag to specify multiple claims.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--oidc-ca-certificate', help="""The path to the certificate for the CA that signed your identity provider's web certificate. Defaults to the
            host's root CAs.""")
@cli_util.option('--oidc-signing-algorithms', type=custom_types.CLI_COMPLEX_TYPE, help="""The signing algorithms accepted. Default is ["RS256"].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--open-id-connect-auth-enabled', type=click.BOOL, help="""Whether the cluster has OIDC Auth Config enabled. Defaults to false.""")
@cli_util.option('--open-id-connect-discovery-enabled', type=click.BOOL, help="""Whether the cluster has OIDC Discovery enabled. Defaults to false. If set to true, the cluster will be assigned a public OIDC Discovery endpoint.""")
@cli_util.option('--pods-cidr', help="""The available group of network addresses that can be allocated to pods running\
 in the cluster, expressed as a single, contiguous IPv4 CIDR block. For example, 10.244.0.0/16.""")
@cli_util.option('--services-cidr', help="""The available group of network addresses that can be exposed as Kubernetes\
 services (ClusterIPs), expressed as a single, contiguous IPv4 CIDR block. For example, 10.96.0.0/16.""")
@cli_util.option('--endpoint-subnet-id', help="""The OCID of the regional subnet in which to place the Cluster endpoint.""")
@cli_util.option('--service-lb-defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for the service load balancer. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--service-lb-freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for the service load balancer. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--persistent-volume-defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for the persistent volume. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--persistent-volume-freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for the persistent volume. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--endpoint-nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""A list of the OCIDs of the network\
 security groups (NSGs) to apply to the cluster endpoint. You must also specify --endpoint-subnet-id.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--endpoint-public-ip-enabled', type=click.BOOL, help="""Whether the cluster should be assigned a public\
 IP address. Defaults to false. If set to true on a private subnet, the cluster provisioning will fail. You must also specify --endpoint-subnet-id.""")
@cli_util.option('--ip-families', type=custom_types.CLI_COMPLEX_TYPE, help="""A list of IP families for the cluster. Example: '[\"IPv4\", \"IPv6\"]'""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option(
    {'defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
     'freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
     'service-lb-subnet-ids': {'module': 'container_engine', 'class': 'list[string]'},
     'endpoint-nsg-ids': {'module': 'container_engine', 'class': 'list[string]'},
     'service-lb-defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
     'service-lb-freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
     'persistent-volume-defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
     'persistent-volume-freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
     'image-policy-config': {'module': 'container_engine', 'class': 'CreateImagePolicyConfigDetails'},
     'governance-policy-config': {'module': 'container_engine', 'class': 'CreateGovernancePolicyConfigDetails'},
     'cluster-pod-network-options': {'module': 'container_engine', 'class': 'list[ClusterPodNetworkOptionDetails]'},
     'oidc-signing-algorithms': {'module': 'container_engine', 'class': 'list[string]'},
     'oidc-required-claims': {'module': 'container_engine', 'class': 'list[KeyValue]'},
     'ip-families': {'module': 'container_engine', 'class': 'list[string]'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={'defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
                                   'freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
                                   'service-lb-subnet-ids': {'module': 'container_engine', 'class': 'list[string]'},
                                   'endpoint-nsg-ids': {'module': 'container_engine', 'class': 'list[string]'},
                                   'service-lb-defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
                                   'service-lb-freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
                                   'persistent-volume-defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
                                   'persistent-volume-freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
                                   'image-policy-config': {'module': 'container_engine', 'class': 'CreateImagePolicyConfigDetails'},
                                   'governance-policy-config': {'module': 'container_engine', 'class': 'CreateGovernancePolicyConfigDetails'},
                                   'cluster-pod-network-options': {'module': 'container_engine', 'class': 'list[ClusterPodNetworkOptionDetails]'},
                                   'oidc-signing-algorithms': {'module': 'container_engine', 'class': 'list[string]'},
                                   'oidc-required-claims': {'module': 'container_engine', 'class': 'list[KeyValue]'},
                                   'ip-families': {'module': 'container_engine', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_cluster(ctx, **kwargs):
    kwargs['options'] = {}
    if 'service_lb_subnet_ids' in kwargs and kwargs['service_lb_subnet_ids'] is not None:
        kwargs['options'] = {'serviceLbSubnetIds': cli_util.parse_json_parameter("service_lb_subnet_ids",
                                                                                 kwargs['service_lb_subnet_ids'])}
    kwargs.pop('service_lb_subnet_ids', None)

    if 'ip_families' in kwargs and kwargs['ip_families'] is not None:
        kwargs['options'] = {'ipFamilies': cli_util.parse_json_parameter("ip_families",
                                                                         kwargs['ip_families'])}
    kwargs.pop('ip_families', None)

    if 'dashboard_enabled' in kwargs and kwargs['dashboard_enabled'] is not None:
        kwargs['options']['addOns'] = {}
        kwargs['options']['addOns']['isKubernetesDashboardEnabled'] = kwargs['dashboard_enabled']
    kwargs.pop('dashboard_enabled', None)

    if 'tiller_enabled' in kwargs and kwargs['tiller_enabled'] is not None:
        if 'addOns' not in kwargs['options']:
            kwargs['options']['addOns'] = {}
        kwargs['options']['addOns']['isTillerEnabled'] = kwargs['tiller_enabled']
    kwargs.pop('tiller_enabled', None)

    if 'oidc_issuer_url' in kwargs and kwargs['oidc_issuer_url'] is not None:
        if 'openIdConnectTokenAuthenticationConfig' not in kwargs['options']:
            kwargs['options']['openIdConnectTokenAuthenticationConfig'] = {}
        kwargs['options']['openIdConnectTokenAuthenticationConfig']['issuerUrl'] = kwargs['oidc_issuer_url']
    kwargs.pop('oidc_issuer_url', None)

    if 'oidc_client_id' in kwargs and kwargs['oidc_client_id'] is not None:
        if 'openIdConnectTokenAuthenticationConfig' not in kwargs['options']:
            kwargs['options']['openIdConnectTokenAuthenticationConfig'] = {}
        kwargs['options']['openIdConnectTokenAuthenticationConfig']['clientId'] = kwargs['oidc_client_id']
    kwargs.pop('oidc_client_id', None)

    if 'oidc_username_claim' in kwargs and kwargs['oidc_username_claim'] is not None:
        if 'openIdConnectTokenAuthenticationConfig' not in kwargs['options']:
            kwargs['options']['openIdConnectTokenAuthenticationConfig'] = {}
        kwargs['options']['openIdConnectTokenAuthenticationConfig']['usernameClaim'] = kwargs['oidc_username_claim']
    kwargs.pop('oidc_username_claim', None)

    if 'oidc_username_prefix' in kwargs and kwargs['oidc_username_prefix'] is not None:
        if 'openIdConnectTokenAuthenticationConfig' not in kwargs['options']:
            kwargs['options']['openIdConnectTokenAuthenticationConfig'] = {}
        kwargs['options']['openIdConnectTokenAuthenticationConfig']['usernamePrefix'] = kwargs['oidc_username_prefix']
    kwargs.pop('oidc_username_prefix', None)

    if 'oidc_groups_claim' in kwargs and kwargs['oidc_groups_claim'] is not None:
        if 'openIdConnectTokenAuthenticationConfig' not in kwargs['options']:
            kwargs['options']['openIdConnectTokenAuthenticationConfig'] = {}
        kwargs['options']['openIdConnectTokenAuthenticationConfig']['groupsClaim'] = kwargs['oidc_groups_claim']
    kwargs.pop('oidc_groups_claim', None)

    if 'oidc_groups_prefix' in kwargs and kwargs['oidc_groups_prefix'] is not None:
        if 'openIdConnectTokenAuthenticationConfig' not in kwargs['options']:
            kwargs['options']['openIdConnectTokenAuthenticationConfig'] = {}
        kwargs['options']['openIdConnectTokenAuthenticationConfig']['groupsPrefix'] = kwargs['oidc_groups_prefix']
    kwargs.pop('oidc_groups_prefix', None)

    if 'oidc_required_claims' in kwargs and kwargs['oidc_required_claims'] is not None:
        if 'openIdConnectTokenAuthenticationConfig' not in kwargs['options']:
            kwargs['options']['openIdConnectTokenAuthenticationConfig'] = {}
        kwargs['options']['openIdConnectTokenAuthenticationConfig']['requiredClaims'] = cli_util.parse_json_parameter("oidc_required_claims", kwargs['oidc_required_claims'])
    kwargs.pop('oidc_required_claims', None)

    if 'oidc_ca_certificate' in kwargs and kwargs['oidc_ca_certificate'] is not None:
        if 'openIdConnectTokenAuthenticationConfig' not in kwargs['options']:
            kwargs['options']['openIdConnectTokenAuthenticationConfig'] = {}
        kwargs['options']['openIdConnectTokenAuthenticationConfig']['caCertificate'] = kwargs['oidc_ca_certificate']
    kwargs.pop('oidc_ca_certificate', None)

    if 'oidc_configuration_file' in kwargs and kwargs['oidc_configuration_file'] is not None:
        if 'openIdConnectTokenAuthenticationConfig' not in kwargs['options']:
            kwargs['options']['openIdConnectTokenAuthenticationConfig'] = {}
        kwargs['options']['openIdConnectTokenAuthenticationConfig']['configurationFile'] = kwargs['oidc_configuration_file']
    kwargs.pop('oidc_configuration_file', None)

    if 'oidc_signing_algorithms' in kwargs and kwargs['oidc_signing_algorithms'] is not None:
        if 'openIdConnectTokenAuthenticationConfig' not in kwargs['options']:
            kwargs['options']['openIdConnectTokenAuthenticationConfig'] = {}
        kwargs['options']['openIdConnectTokenAuthenticationConfig']['signingAlgorithms'] = cli_util.parse_json_parameter("oidc_signing_algorithms", kwargs['oidc_signing_algorithms'])
    kwargs.pop('oidc_signing_algorithms', None)

    if 'open_id_connect_auth_enabled' in kwargs and kwargs['open_id_connect_auth_enabled'] is not None:
        if 'openIdConnectTokenAuthenticationConfig' not in kwargs['options']:
            kwargs['options']['openIdConnectTokenAuthenticationConfig'] = {}
        kwargs['options']['openIdConnectTokenAuthenticationConfig']['isOpenIdConnectAuthEnabled'] = kwargs['open_id_connect_auth_enabled']
    kwargs.pop('open_id_connect_auth_enabled', None)
    if 'open_id_connect_discovery_enabled' in kwargs and kwargs['open_id_connect_discovery_enabled'] is not None:
        if 'openIdConnectDiscovery' not in kwargs['options']:
            kwargs['options']['openIdConnectDiscovery'] = {}
        kwargs['options']['openIdConnectDiscovery']['isOpenIdConnectDiscoveryEnabled'] = kwargs['open_id_connect_discovery_enabled']
    kwargs.pop('open_id_connect_discovery_enabled', None)

    if 'pods_cidr' in kwargs and kwargs['pods_cidr'] is not None:
        kwargs['options']['kubernetesNetworkConfig'] = {}
        kwargs['options']['kubernetesNetworkConfig']['podsCidr'] = kwargs['pods_cidr']
    kwargs.pop('pods_cidr', None)

    if 'services_cidr' in kwargs and kwargs['services_cidr'] is not None:
        if 'kubernetesNetworkConfig' not in kwargs['options']:
            kwargs['options']['kubernetesNetworkConfig'] = {}
        kwargs['options']['kubernetesNetworkConfig']['servicesCidr'] = kwargs['services_cidr']
    kwargs.pop('services_cidr', None)

    if 'persistent_volume_freeform_tags' in kwargs and kwargs['persistent_volume_freeform_tags'] is not None:
        kwargs['options']['persistentVolumeConfig'] = {}
        kwargs['options']['persistentVolumeConfig']['freeformTags'] = cli_util.parse_json_parameter("persistent_volume_freeform_tags", kwargs['persistent_volume_freeform_tags'])
    kwargs.pop('persistent_volume_freeform_tags', None)

    if 'persistent_volume_defined_tags' in kwargs and kwargs['persistent_volume_defined_tags'] is not None:
        if 'persistentVolumeConfig' not in kwargs['options']:
            kwargs['options']['persistentVolumeConfig'] = {}
        kwargs['options']['persistentVolumeConfig']['definedTags'] = cli_util.parse_json_parameter("persistent_volume_defined_tags", kwargs['persistent_volume_defined_tags'])
    kwargs.pop('persistent_volume_defined_tags', None)

    if 'service_lb_freeform_tags' in kwargs and kwargs['service_lb_freeform_tags'] is not None:
        kwargs['options']['serviceLbConfig'] = {}
        kwargs['options']['serviceLbConfig']['freeformTags'] = cli_util.parse_json_parameter("service_lb_freeform_tags", kwargs['service_lb_freeform_tags'])
    kwargs.pop('service_lb_freeform_tags', None)

    if 'service_lb_defined_tags' in kwargs and kwargs['service_lb_defined_tags'] is not None:
        if 'serviceLbConfig' not in kwargs['options']:
            kwargs['options']['serviceLbConfig'] = {}
        kwargs['options']['serviceLbConfig']['definedTags'] = cli_util.parse_json_parameter("service_lb_defined_tags", kwargs['service_lb_defined_tags'])
    kwargs.pop('service_lb_defined_tags', None)

    if kwargs.get('endpoint_nsg_ids') and not kwargs.get('endpoint_subnet_id'):
        raise click.UsageError(
            'Cannot specify --endpoint-nsg-ids without --endpoint-subnet-id'
        )
    if 'endpoint_public_ip_enabled' in kwargs and kwargs['endpoint_public_ip_enabled'] is not None and not kwargs.get('endpoint_subnet_id'):
        raise click.UsageError(
            'Cannot specify --endpoint-public-ip-enabled without --endpoint-subnet-id'
        )

    if 'endpoint_subnet_id' in kwargs and kwargs['endpoint_subnet_id'] is not None:
        kwargs['endpoint_config'] = {}
        kwargs['endpoint_config']['subnetId'] = kwargs['endpoint_subnet_id']
        if 'endpoint_nsg_ids' in kwargs and kwargs['endpoint_nsg_ids'] is not None:
            kwargs['endpoint_config']['nsgIds'] = cli_util.parse_json_parameter("endpoint_nsg_ids", kwargs['endpoint_nsg_ids'])
        if 'endpoint_public_ip_enabled' in kwargs and kwargs['endpoint_public_ip_enabled'] is not None:
            kwargs['endpoint_config']['isPublicIpEnabled'] = kwargs['endpoint_public_ip_enabled']
    kwargs.pop('endpoint_subnet_id', None)
    kwargs.pop('endpoint_nsg_ids', None)
    kwargs.pop('endpoint_public_ip_enabled', None)

    # It seems like the service needs options param even if it is empty so leave it when invoking the create command

    ctx.invoke(containerengine_cli.create_cluster, **kwargs)


@cli_util.copy_params_from_generated_command(containerengine_cli.create_node_pool,
                                             params_to_exclude=['node_config_details', 'node_eviction_node_pool_settings'], copy_from_json=False)
@containerengine_cli.node_pool_group.command(name=cli_util.override('create_node_pool.command_name', 'create'),
                                             help="""Create a new node pool.""")
@cli_util.option('--node-image-id', help="""The OCID of the image used to launch the node. This is a shortcut for specifying an image id via the --node-source-details complex JSON parameter. If this parameter is provided, you cannot provide the --node-source-details parameter""")
@cli_util.option('--node-boot-volume-size-in-gbs', type=click.INT, help="""The size of the boot volume in GBs. This is a shortcut for specifying a boot volume size via the --node-source-details complex JSON parameter. If this parameter is provided, you cannot provide the --node-source-details parameter.""")
@cli_util.option('--size', type=click.INT, help="""The number of nodes spread across placement configurations.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""The OCIDs of the Network Security Group(s) to associate nodes for this node pool with.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--placement-configs', type=custom_types.CLI_COMPLEX_TYPE,
                 help="""The placement configurations that determine where the nodes will be placed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--node-freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for the nodes. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--node-defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for the nodes. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--node-eviction-node-pool-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Node eviction settings for this nodepool. Example: `{\"evictionGraceDuration\": \"PT30M\", \"isForceDeleteAfterGraceDuration\": \"true\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help="""The OCID of the Key Management Service key assigned to the boot volume.""")
@cli_util.option('--is-pv-encryption-in-transit-enabled', type=click.BOOL, help=u"""Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and boot volumes. The default value is false.""")
@cli_util.option('--max-pods-per-node', type=click.INT, help="""The maximum number of pods that will live on a node of the node pool.""")
@cli_util.option('--pod-nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""The OCIDs of the Network Security Group(s) to associate pods for this node pool with.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--pod-subnet-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""The OCIDs of the subnets in which to place pods for this node pool.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option(
    {'defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
     'freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
     'node-metadata': {'module': 'container_engine', 'class': 'dict(str, string)'},
     'initial-node-labels': {'module': 'container_engine', 'class': 'list[KeyValue]'},
     'subnet-ids': {'module': 'container_engine', 'class': 'list[string]'},
     'node-shape-config': {'module': 'container_engine', 'class': 'CreateNodeShapeConfigDetails'},
     'node-source-details': {'module': 'container_engine', 'class': 'NodeSourceDetails'},
     'placement-configs': {'module': 'container_engine', 'class': 'list[NodePoolPlacementConfigDetails]'},
     'node-defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
     'node-freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
     'nsg-ids': {'module': 'container_engine', 'class': 'list[string]'},
     'max-pods-per-node': {'module': 'container_engine', 'class': 'int'},
     'pod-nsg-ids': {'module': 'container_engine', 'class': 'list[string]'},
     'pod-subnet-ids': {'module': 'container_engine', 'class': 'list[string]'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={'defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
                                   'freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
                                   'node-metadata': {'module': 'container_engine', 'class': 'dict(str, string)'},
                                   'initial-node-labels': {'module': 'container_engine', 'class': 'list[KeyValue]'},
                                   'subnet-ids': {'module': 'container_engine', 'class': 'list[string]'},
                                   'node-shape-config': {'module': 'container_engine',
                                                         'class': 'CreateNodeShapeConfigDetails'},
                                   'node-source-details': {'module': 'container_engine', 'class': 'NodeSourceDetails'},
                                   'placement-configs': {'module': 'container_engine',
                                                         'class': 'list[NodePoolPlacementConfigDetails]'},
                                   'node-defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
                                   'node-freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
                                   'nsg-ids': {'module': 'container_engine', 'class': 'list[string]'},
                                   'node-eviction-node-pool-settings': {'module': 'container_engine', 'class': 'dict(str, str)'},
                                   'max-pods-per-node': {'module': 'container_engine', 'class': 'int'},
                                   'pod-nsg-ids': {'module': 'container_engine', 'class': 'list[string]'},
                                   'pod-subnet-ids': {'module': 'container_engine', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def create_node_pool(ctx, **kwargs):

    kwargs['node_config_details'] = {}

    if kwargs.get('max_pods_per_node') and not kwargs.get('pod_subnet_ids'):
        raise click.UsageError(
            'Cannot specify --max-pods-per-node without --pod-subnet-ids'
        )

    if kwargs.get('pod_nsg_ids') and not kwargs.get('pod_subnet_ids'):
        raise click.UsageError(
            'Cannot specify --pod-nsg-ids without --pod-subnet-ids'
        )

    nodePoolPodNetworkOptionDetails = {}
    if 'max_pods_per_node' in kwargs and kwargs['max_pods_per_node'] is not None:
        nodePoolPodNetworkOptionDetails['maxPodsPerNode'] = cli_util.parse_json_parameter("max_pods_per_node", kwargs['max_pods_per_node'])
    kwargs.pop('max_pods_per_node', None)

    if 'pod_nsg_ids' in kwargs and kwargs['pod_nsg_ids'] is not None:
        nodePoolPodNetworkOptionDetails['podNsgIds'] = cli_util.parse_json_parameter("pod_nsg_ids", kwargs['pod_nsg_ids'])
    kwargs.pop('pod_nsg_ids', None)

    # existence of pod_subnet_ids hints that the CNI used is OCI_VCN_IP_NATIVE
    # with it's absence, we will pass a null nodePoolPodNetworkOptionDetails, which means use default CNI FLANNEL_OVERLAY
    if 'pod_subnet_ids' in kwargs and kwargs['pod_subnet_ids'] is not None:
        # if cniType is absent, defaults to FLANNEL
        nodePoolPodNetworkOptionDetails['cniType'] = "OCI_VCN_IP_NATIVE"
        nodePoolPodNetworkOptionDetails['podSubnetIds'] = cli_util.parse_json_parameter("pod_subnet_ids", kwargs['pod_subnet_ids'])
        kwargs['node_config_details']['nodePoolPodNetworkOptionDetails'] = nodePoolPodNetworkOptionDetails
    kwargs.pop('pod_subnet_ids', None)

    if 'size' in kwargs and kwargs['size'] is not None:
        kwargs['node_config_details']['size'] = kwargs['size']
    kwargs.pop('size', None)

    if 'nsg_ids' in kwargs and kwargs['nsg_ids'] is not None:
        kwargs['node_config_details']['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", kwargs['nsg_ids'])
    kwargs.pop('nsg_ids', None)

    if 'placement_configs' in kwargs and kwargs['placement_configs'] is not None:
        kwargs['node_config_details']['placementConfigs'] = cli_util.parse_json_parameter("placement_configs", kwargs['placement_configs'])
    kwargs.pop('placement_configs', None)

    if 'node_defined_tags' in kwargs and kwargs['node_defined_tags'] is not None:
        kwargs['node_config_details']['definedTags'] = cli_util.parse_json_parameter("node_defined_tags", kwargs['node_defined_tags'])
    kwargs.pop('node_defined_tags', None)

    if 'node_freeform_tags' in kwargs and kwargs['node_freeform_tags'] is not None:
        kwargs['node_config_details']['freeformTags'] = cli_util.parse_json_parameter("node_freeform_tags", kwargs['node_freeform_tags'])
    kwargs.pop('node_freeform_tags', None)

    if kwargs.get('kms_key_id'):
        kwargs['node_config_details']['kmsKeyId'] = kwargs.get('kms_key_id')
    kwargs.pop('kms_key_id', None)

    if kwargs.get('is_pv_encryption_in_transit_enabled'):
        kwargs['node_config_details']['isPvEncryptionInTransitEnabled'] = kwargs.get('is_pv_encryption_in_transit_enabled')
    kwargs.pop('is_pv_encryption_in_transit_enabled', None)

    if kwargs.get('node_source_details') and (kwargs.get('node_image_id') or kwargs.get('node_boot_volume_size_in_gbs')):
        raise click.UsageError(
            'Cannot specify --node-source-details with any of: --node-image-id or --node-boot-volume-size-in-gbs'
        )
    if kwargs.get('node_boot_volume_size_in_gbs') and not kwargs.get('node_image_id'):
        raise click.UsageError(
            'Cannot specify --node-boot-volume-size-in-gbs without --node-image-id'
        )

    if kwargs.get('node_image_id'):
        source_details = {'sourceType': 'IMAGE', 'imageId': kwargs['node_image_id']}
        if kwargs.get('node_boot_volume_size_in_gbs'):
            source_details['bootVolumeSizeInGBs'] = kwargs.get('node_boot_volume_size_in_gbs')

        kwargs['node_source_details'] = json.dumps(source_details)

    # Remove the shortcuts for node image id and boot volume size
    kwargs.pop('node_image_id', None)
    kwargs.pop('node_boot_volume_size_in_gbs', None)

    ctx.invoke(containerengine_cli.create_node_pool, **kwargs)


@cli_util.copy_params_from_generated_command(containerengine_cli.update_node_pool,
                                             params_to_exclude=['node_config_details', 'node_eviction_node_pool_settings'], copy_from_json=False)
@containerengine_cli.node_pool_group.command(name=cli_util.override('update_node_pool.command_name', 'update'),
                                             help="""Update a node pool.""")
@cli_util.option('--size', type=click.INT, help="""The number of nodes spread across placement configurations.""")
@cli_util.option('--nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""The OCIDs of the Network Security Group(s) to associate nodes for this node pool with.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--placement-configs', type=custom_types.CLI_COMPLEX_TYPE,
                 help="""The placement configurations that determine where the nodes will be placed.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--node-freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for the nodes. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--node-defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for the nodes. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--node-eviction-node-pool-settings', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Node eviction settings for this nodepool. Example: `{\"evictionGraceDuration\": \"PT30M\", \"isForceDeleteAfterGraceDuration\": \"true\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--kms-key-id', help="""The OCID of the Key Management Service key assigned to the boot volume.""")
@cli_util.option('--is-pv-encryption-in-transit-enabled', type=click.BOOL, help=u"""Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and boot volumes. The default value is false.""")
@cli_util.option('--max-pods-per-node', type=click.INT, help="""The maximum number of pods that will live on a node of the node pool.""")
@cli_util.option('--pod-nsg-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""The OCIDs of the Network Security Group(s) to associate pods for this node pool with.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--pod-subnet-ids', type=custom_types.CLI_COMPLEX_TYPE, help="""The OCIDs of the subnets in which to place pods for this node pool.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option(
    {'defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
     'freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
     'initial-node-labels': {'module': 'container_engine', 'class': 'list[KeyValue]'},
     'subnet-ids': {'module': 'container_engine', 'class': 'list[string]'},
     'node-metadata': {'module': 'container_engine', 'class': 'dict(str, string)'},
     'node-source-details': {'module': 'container_engine', 'class': 'NodeSourceDetails'},
     'node-shape-config': {'module': 'container_engine', 'class': 'UpdateNodeShapeConfigDetails'},
     'placement-configs': {'module': 'container_engine', 'class': 'list[NodePoolPlacementConfigDetails]'},
     'node-defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
     'node-freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
     'nsg-ids': {'module': 'container_engine', 'class': 'list[string]'},
     'max-pods-per-node': {'module': 'container_engine', 'class': 'int'},
     'pod-nsg-ids': {'module': 'container_engine', 'class': 'list[string]'},
     'pod-subnet-ids': {'module': 'container_engine', 'class': 'list[string]'}})
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(
    input_params_to_complex_types={'defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
                                   'freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
                                   'initial-node-labels': {'module': 'container_engine', 'class': 'list[KeyValue]'},
                                   'subnet-ids': {'module': 'container_engine', 'class': 'list[string]'},
                                   'node-metadata': {'module': 'container_engine', 'class': 'dict(str, string)'},
                                   'node-source-details': {'module': 'container_engine', 'class': 'NodeSourceDetails'},
                                   'node-shape-config': {'module': 'container_engine', 'class': 'UpdateNodeShapeConfigDetails'},
                                   'placement-configs': {'module': 'container_engine',
                                                         'class': 'list[NodePoolPlacementConfigDetails]'},
                                   'node-defined-tags': {'module': 'container_engine', 'class': 'dict(str, dict(str, object))'},
                                   'node-freeform-tags': {'module': 'container_engine', 'class': 'dict(str, string)'},
                                   'nsg-ids': {'module': 'container_engine', 'class': 'list[string]'},
                                   'node-eviction-node-pool-settings': {'module': 'container_engine', 'class': 'dict(str, str)'},
                                   'max-pods-per-node': {'module': 'container_engine', 'class': 'int'},
                                   'pod-nsg-ids': {'module': 'container_engine', 'class': 'list[string]'},
                                   'pod-subnet-ids': {'module': 'container_engine', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def update_node_pool(ctx, **kwargs):
    kwargs['node_config_details'] = {}

    if kwargs.get('max_pods_per_node') and not kwargs.get('pod_subnet_ids'):
        raise click.UsageError(
            'Cannot specify --max-pods-per-node without --pod-subnet-ids'
        )

    if kwargs.get('pod_nsg_ids') and not kwargs.get('pod_subnet_ids'):
        raise click.UsageError(
            'Cannot specify --pod-nsg-ids without --pod-subnet-ids'
        )

    nodePoolPodNetworkOptionDetails = {}
    if 'max_pods_per_node' in kwargs and kwargs['max_pods_per_node'] is not None:
        nodePoolPodNetworkOptionDetails['maxPodsPerNode'] = cli_util.parse_json_parameter("max_pods_per_node", kwargs['max_pods_per_node'])
    kwargs.pop('max_pods_per_node', None)

    if 'pod_nsg_ids' in kwargs and kwargs['pod_nsg_ids'] is not None:
        nodePoolPodNetworkOptionDetails['podNsgIds'] = cli_util.parse_json_parameter("pod_nsg_ids", kwargs['pod_nsg_ids'])
    kwargs.pop('pod_nsg_ids', None)

    # existence of pod_subnet_ids hints that the CNI used is OCI_VCN_IP_NATIVE
    # with it's absence, we will pass a null nodePoolPodNetworkOptionDetails, which means use default CNI FLANNEL_OVERLAY
    if 'pod_subnet_ids' in kwargs and kwargs['pod_subnet_ids'] is not None:
        # if cniType is absent, defaults to FLANNEL
        nodePoolPodNetworkOptionDetails['cniType'] = "OCI_VCN_IP_NATIVE"
        nodePoolPodNetworkOptionDetails['podSubnetIds'] = cli_util.parse_json_parameter("pod_subnet_ids", kwargs['pod_subnet_ids'])
        kwargs['node_config_details']['nodePoolPodNetworkOptionDetails'] = nodePoolPodNetworkOptionDetails
    kwargs.pop('pod_subnet_ids', None)

    if 'size' in kwargs and kwargs['size'] is not None:
        kwargs['node_config_details']['size'] = kwargs['size']
    kwargs.pop('size', None)

    if 'nsg_ids' in kwargs and kwargs['nsg_ids'] is not None:
        kwargs['node_config_details']['nsgIds'] = cli_util.parse_json_parameter("nsg_ids", kwargs['nsg_ids'])
    kwargs.pop('nsg_ids', None)

    if 'placement_configs' in kwargs and kwargs['placement_configs'] is not None:
        if 'node_config_details' not in kwargs:
            kwargs['node_config_details'] = {}
        kwargs['node_config_details']['placementConfigs'] = cli_util.parse_json_parameter("placement_configs",
                                                                                          kwargs['placement_configs'])
    kwargs.pop('placement_configs', None)

    if 'node_defined_tags' in kwargs and kwargs['node_defined_tags'] is not None:
        kwargs['node_config_details']['definedTags'] = cli_util.parse_json_parameter("node_defined_tags",
                                                                                     kwargs['node_defined_tags'])
    kwargs.pop('node_defined_tags', None)

    if 'node_freeform_tags' in kwargs and kwargs['node_freeform_tags'] is not None:
        kwargs['node_config_details']['freeformTags'] = cli_util.parse_json_parameter("node_freeform_tags",
                                                                                      kwargs['node_freeform_tags'])
    kwargs.pop('node_freeform_tags', None)

    if kwargs.get('kms_key_id') is not None:
        kwargs['node_config_details']['kmsKeyId'] = kwargs.get('kms_key_id')
    kwargs.pop('kms_key_id', None)

    if kwargs.get('is_pv_encryption_in_transit_enabled') is not None:
        kwargs['node_config_details']['isPvEncryptionInTransitEnabled'] = kwargs.get('is_pv_encryption_in_transit_enabled')
    kwargs.pop('is_pv_encryption_in_transit_enabled', None)

    ctx.invoke(containerengine_cli.update_node_pool, **kwargs)


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
@cli_util.copy_params_from_generated_command(containerengine_cli.create_kubeconfig, params_to_exclude=['endpoint_parameterconflict', 'file', 'token_version'])
@containerengine_cli.cluster_group.command(name=cli_util.override('create_kubeconfig.command_name', 'create-kubeconfig'),
                                           help="""Create the Kubeconfig YAML for a cluster.""")
@cli_util.option('--file', type=click.Path(), default=DEFAULT_KUBECONFIG_LOCATION, show_default=True,
                 help="The name of the file that will be updated with response data, or '-' to write to STDOUT.")
@cli_util.option('--token-version', default="2.0.0", help=u"""The version of the kubeconfig token. Supported value is 2.0.0""", type=custom_types.CliCaseInsensitiveChoice(['2.0.0']))
@cli_util.option('--kube-endpoint', type=custom_types.CliCaseInsensitiveChoice(["LEGACY_KUBERNETES", "PUBLIC_ENDPOINT", "PRIVATE_ENDPOINT", "VCN_HOSTNAME"]), help=u"""The endpoint to target. A cluster may have multiple endpoints exposed but the kubeconfig can only target one at a time. Supported values LEGACY_KUBERNETES, PUBLIC_ENDPOINT, PRIVATE_ENDPOINT, VCN_HOSTNAME""")
@cli_util.option('--overwrite', is_flag=True, help="""Overwrites the contents of kubeconfig file specified using --file\
 option or kubeconfig file at default location if --file is not used.""")
@cli_util.option('--with-auth-context', default=False, is_flag=True, help="""Appends the current authentication context (values configured in --auth and --profile) of the OCI CLI command\
 to the kubeconfig user exec command if --with-auth-context is used or not append those information if --with-auth-context is not used""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def create_kubeconfig(ctx, from_json, file, cluster_id, token_version, expiration, kube_endpoint, overwrite, with_auth_context):
    if isinstance(cluster_id, str) and len(cluster_id.strip()) == 0:
        raise click.UsageError('Parameter --cluster-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    details = {}

    if token_version is not None:
        details['tokenVersion'] = token_version

    if expiration is not None:
        details['expiration'] = expiration

    if kube_endpoint is not None:
        details['endpoint'] = kube_endpoint

    client = cli_util.build_client('container_engine', 'container_engine', ctx)
    result = client.create_kubeconfig(
        cluster_id=cluster_id,
        create_cluster_kubeconfig_content_details=details,
        **kwargs
    )

    # kubeconfig is received in binary format.
    new_kubeconfig = b''
    for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
        new_kubeconfig = b''.join([new_kubeconfig, chunk])

    # enrich kubeconfig auth command with oci cli auth and profile
    auth = ctx.obj.get('auth', '')
    profile = ctx.obj.get('profile', '')
    try:
        temp_kubeconfig = yaml.safe_load(new_kubeconfig)
        if with_auth_context and auth:
            temp_kubeconfig['users'][0]['user']['exec']['args'].extend(['--auth', auth])
        if with_auth_context and profile:
            temp_kubeconfig['users'][0]['user']['exec']['args'].extend(['--profile', profile])
        new_kubeconfig = yaml.dump(temp_kubeconfig, encoding=('utf-8'))
    except yaml.YAMLError as e:
        click.echo('Error parsing configuration file {}'.format(e))
        return
    except (KeyError, IndexError):
        pass

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
    if dst_yaml[merge_key] is None:
        dst_yaml[merge_key] = []
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
