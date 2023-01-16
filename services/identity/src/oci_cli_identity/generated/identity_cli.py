# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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


@cli.command(cli_util.override('iam.iam_root_group.command_name', 'iam'), cls=CommandGroupWithAlias, help=cli_util.override('iam.iam_root_group.help', """APIs for managing users, groups, compartments, policies, and identity domains."""), short_help=cli_util.override('iam.iam_root_group.short_help', """Identity and Access Management Service API"""))
@cli_util.help_option_group
def iam_root_group():
    pass


@click.command(cli_util.override('iam.fault_domain_group.command_name', 'fault-domain'), cls=CommandGroupWithAlias, help="""A Fault Domain is a logical grouping of hardware and infrastructure within an Availability Domain that can become unavailable in its entirety either due to hardware failure such as Top-of-rack (TOR) switch failure or due to planned software maintenance such as security updates that reboot your instances.""")
@cli_util.help_option_group
def fault_domain_group():
    pass


@click.command(cli_util.override('iam.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""The asynchronous API request does not take effect immediately. This request spawns an asynchronous workflow to fulfill the request. WorkRequest objects provide visibility for in-progress workflows.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('iam.tagging_work_request_log_group.command_name', 'tagging-work-request-log'), cls=CommandGroupWithAlias, help="""The log entity.""")
@cli_util.help_option_group
def tagging_work_request_log_group():
    pass


@click.command(cli_util.override('iam.compartment_group.command_name', 'compartment'), cls=CommandGroupWithAlias, help="""A collection of related resources. Compartments are a fundamental component of Oracle Cloud Infrastructure for organizing and isolating your cloud resources. You use them to clearly separate resources for the purposes of measuring usage and billing, access (through the use of IAM Service policies), and isolation (separating the resources for one project or business unit from another). A common approach is to create a compartment for each major part of your organization. For more information, see [Overview of IAM] and also [Setting Up Your Tenancy].

To place a resource in a compartment, simply specify the compartment ID in the \"Create\" request object when initially creating the resource. For example, to launch an instance into a particular compartment, specify that compartment's OCID in the `LaunchInstance` request. You can't move an existing resource from one compartment to another.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Get Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def compartment_group():
    pass


@click.command(cli_util.override('iam.network_sources_group.command_name', 'network-sources'), cls=CommandGroupWithAlias, help="""A network source specifies a list of source IP addresses that are allowed to make authorization requests. Use the network source in policy statements to restrict access to only requests that come from the specified IPs. For more information, see [Managing Network Sources].""")
@cli_util.help_option_group
def network_sources_group():
    pass


@click.command(cli_util.override('iam.authentication_policy_group.command_name', 'authentication-policy'), cls=CommandGroupWithAlias, help="""Authentication policy, currently set for the given compartment.""")
@cli_util.help_option_group
def authentication_policy_group():
    pass


@click.command(cli_util.override('iam.smtp_credential_group.command_name', 'smtp-credential'), cls=CommandGroupWithAlias, help="""Simple Mail Transfer Protocol (SMTP) credentials are needed to send email through Email Delivery. The SMTP credentials are used for SMTP authentication with the service. The credentials never expire. A user can have up to 2 SMTP credentials at a time.

**Note:** The credential set is always an Oracle-generated SMTP user name and password pair; you cannot designate the SMTP user name or the SMTP password.

For more information, see [Managing User Credentials].""")
@cli_util.help_option_group
def smtp_credential_group():
    pass


@click.command(cli_util.override('iam.scim_client_credentials_group.command_name', 'scim-client-credentials'), cls=CommandGroupWithAlias, help="""The OAuth2 client credentials.""")
@cli_util.help_option_group
def scim_client_credentials_group():
    pass


@click.command(cli_util.override('iam.tag_group.command_name', 'tag'), cls=CommandGroupWithAlias, help="""A tag definition that belongs to a specific tag namespace.  \"Defined tags\" must be set up in your tenancy before you can apply them to resources. For more information, see [Managing Tags and Tag Namespaces].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def tag_group():
    pass


@click.command(cli_util.override('iam.iam_work_request_log_group.command_name', 'iam-work-request-log'), cls=CommandGroupWithAlias, help="""(For tenancies that support identity domains) The log entity for a IAM work request.""")
@cli_util.help_option_group
def iam_work_request_log_group():
    pass


@click.command(cli_util.override('iam.bulk_edit_tags_resource_type_collection_group.command_name', 'bulk-edit-tags-resource-type-collection'), cls=CommandGroupWithAlias, help="""The list of resource types that support bulk editing of tags.""")
@cli_util.help_option_group
def bulk_edit_tags_resource_type_collection_group():
    pass


@click.command(cli_util.override('iam.group_group.command_name', 'group'), cls=CommandGroupWithAlias, help="""A collection of users who all need the same type of access to a particular set of resources or compartment. For conceptual information about groups and other IAM Service components, see [Overview of IAM].

If you're federating with an identity provider (IdP), you need to create mappings between the groups defined in the IdP and groups you define in the IAM service. For more information, see [Identity Providers and Federation]. Also see [IdentityProvider] and [IdpGroupMapping].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Get Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def group_group():
    pass


@click.command(cli_util.override('iam.policy_group.command_name', 'policy'), cls=CommandGroupWithAlias, help="""A document that specifies the type of access a group has to the resources in a compartment. For information about policies and other IAM Service components, see [Overview of IAM]. If you're new to policies, see [Get Started with Policies].

The word \"policy\" is used by people in different ways:

  * An individual statement written in the policy language   * A collection of statements in a single, named \"policy\" document (which has an Oracle Cloud ID (OCID) assigned to it)   * The overall body of policies your organization uses to control access to resources

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator.

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def policy_group():
    pass


@click.command(cli_util.override('iam.tag_namespace_group.command_name', 'tag-namespace'), cls=CommandGroupWithAlias, help="""A managed container for defined tags. A tag namespace is unique in a tenancy. For more information, see [Managing Tags and Tag Namespaces].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def tag_namespace_group():
    pass


@click.command(cli_util.override('iam.availability_domain_group.command_name', 'availability-domain'), cls=CommandGroupWithAlias, help="""One or more isolated, fault-tolerant Oracle data centers that host cloud resources such as instances, volumes, and subnets. A region contains several Availability Domains. For more information, see [Regions and Availability Domains].""")
@cli_util.help_option_group
def availability_domain_group():
    pass


@click.command(cli_util.override('iam.bulk_action_resource_type_collection_group.command_name', 'bulk-action-resource-type-collection'), cls=CommandGroupWithAlias, help="""Collection of resource-types supported by a compartment bulk action.""")
@cli_util.help_option_group
def bulk_action_resource_type_collection_group():
    pass


@click.command(cli_util.override('iam.customer_secret_key_group.command_name', 'customer-secret-key'), cls=CommandGroupWithAlias, help="""A `CustomerSecretKey` is an Oracle-provided key for using the Object Storage Service's [Amazon S3 compatible API]. The key consists of a secret key/access key pair. A user can have up to two secret keys at a time.

**Note:** The secret key is always an Oracle-generated string; you can't change it to a string of your choice.

For more information, see [Managing User Credentials].""")
@cli_util.help_option_group
def customer_secret_key_group():
    pass


@click.command(cli_util.override('iam.idp_group_mapping_group.command_name', 'idp-group-mapping'), cls=CommandGroupWithAlias, help="""A mapping between a single group defined by the identity provider (IdP) you're federating with and a single IAM Service [group] in Oracle Cloud Infrastructure. For more information about group mappings and what they're for, see [Identity Providers and Federation].

A given IdP group can be mapped to zero, one, or multiple IAM Service groups, and vice versa. But each `IdPGroupMapping` object is between only a single IdP group and IAM Service group. Each `IdPGroupMapping` object has its own OCID.

**Note:** Any users who are in more than 50 IdP groups cannot be authenticated to use the Oracle Cloud Infrastructure Console.""")
@cli_util.help_option_group
def idp_group_mapping_group():
    pass


@click.command(cli_util.override('iam.tenancy_group.command_name', 'tenancy'), cls=CommandGroupWithAlias, help="""The root compartment that contains all of your organization's compartments and other Oracle Cloud Infrastructure cloud resources. When you sign up for Oracle Cloud Infrastructure, Oracle creates a tenancy for your company, which is a secure and isolated partition where you can create, organize, and administer your cloud resources.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Get Started with Policies].""")
@cli_util.help_option_group
def tenancy_group():
    pass


@click.command(cli_util.override('iam.user_group_membership_group.command_name', 'user-group-membership'), cls=CommandGroupWithAlias, help="""An object that represents the membership of a user in a group. When you add a user to a group, the result is a `UserGroupMembership` with its own OCID. To remove a user from a group, you delete the `UserGroupMembership` object.""")
@cli_util.help_option_group
def user_group_membership_group():
    pass


@click.command(cli_util.override('iam.mfa_totp_device_group.command_name', 'mfa-totp-device'), cls=CommandGroupWithAlias, help="""Users can enable multi-factor authentication (MFA) for their own user accounts. After MFA is enabled, the user is prompted for a time-based one-time password (TOTP) to authenticate before they can sign in to the Console. To enable multi-factor authentication, the user must register a mobile device with a TOTP authenticator app installed. The registration process creates the `MfaTotpDevice` object. The registration process requires interaction with the Console and cannot be completed programmatically. For more information, see [Managing Multi-Factor Authentication].""")
@cli_util.help_option_group
def mfa_totp_device_group():
    pass


@click.command(cli_util.override('iam.ui_password_information_group.command_name', 'ui-password-information'), cls=CommandGroupWithAlias, help="""Information about the UIPassword, which is a text password that enables a user to sign in to the Console, the user interface for interacting with Oracle Cloud Infrastructure.

For more information about user credentials, see [User Credentials].""")
@cli_util.help_option_group
def ui_password_information_group():
    pass


@click.command(cli_util.override('iam.identity_provider_group.command_name', 'identity-provider'), cls=CommandGroupWithAlias, help="""The resulting base object when you add an identity provider to your tenancy. A [Saml2IdentityProvider] is a specific type of `IdentityProvider` that supports the SAML 2.0 protocol. Each `IdentityProvider` object has its own OCID. For more information, see [Identity Providers and Federation].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Get Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def identity_provider_group():
    pass


@click.command(cli_util.override('iam.identity_provider_group_group.command_name', 'identity-provider-group'), cls=CommandGroupWithAlias, help="""A group created in an identity provider that can be mapped to a group in OCI""")
@cli_util.help_option_group
def identity_provider_group_group():
    pass


@click.command(cli_util.override('iam.ui_password_group.command_name', 'ui-password'), cls=CommandGroupWithAlias, help="""A text password that enables a user to sign in to the Console, the user interface for interacting with Oracle Cloud Infrastructure.

For more information about user credentials, see [User Credentials].""")
@cli_util.help_option_group
def ui_password_group():
    pass


@click.command(cli_util.override('iam.api_key_group.command_name', 'api-key'), cls=CommandGroupWithAlias, help="""A PEM-format RSA credential for securing requests to the Oracle Cloud Infrastructure REST API. Also known as an *API signing key*. Specifically, this is the public key from the key pair. The private key remains with the user calling the API. For information about generating a key pair in the required PEM format, see [Required Keys and OCIDs].

**Important:** This is **not** the SSH key for accessing compute instances.

Each user can have a maximum of three API signing keys.

For more information about user credentials, see [User Credentials].""")
@cli_util.help_option_group
def api_key_group():
    pass


@click.command(cli_util.override('iam.domain_group.command_name', 'domain'), cls=CommandGroupWithAlias, help="""(For tenancies that support identity domains) Properties for an identity domain. An identity domain is used to manage users and groups, integration standards, external identities, and secure application integration through Oracle Single Sign-on (SSO) configuration.""")
@cli_util.help_option_group
def domain_group():
    pass


@click.command(cli_util.override('iam.tagging_work_request_error_group.command_name', 'tagging-work-request-error'), cls=CommandGroupWithAlias, help="""The error entity.""")
@cli_util.help_option_group
def tagging_work_request_error_group():
    pass


@click.command(cli_util.override('iam.region_subscription_group.command_name', 'region-subscription'), cls=CommandGroupWithAlias, help="""An object that represents your tenancy's access to a particular region (i.e., a subscription), the status of that access, and whether that region is the home region. For more information, see [Managing Regions].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Get Started with Policies].""")
@cli_util.help_option_group
def region_subscription_group():
    pass


@click.command(cli_util.override('iam.standard_tag_namespace_template_group.command_name', 'standard-tag-namespace-template'), cls=CommandGroupWithAlias, help="""The template of the standard tag namespace. This object includes necessary details to create the provided standard tag namespace.""")
@cli_util.help_option_group
def standard_tag_namespace_template_group():
    pass


@click.command(cli_util.override('iam.iam_work_request_group.command_name', 'iam-work-request'), cls=CommandGroupWithAlias, help="""(For tenancies that support identity domains) An IAM work request object that allows users to track the status of asynchronous API requests.""")
@cli_util.help_option_group
def iam_work_request_group():
    pass


@click.command(cli_util.override('iam.tagging_work_request_group.command_name', 'tagging-work-request'), cls=CommandGroupWithAlias, help="""The asynchronous API request does not take effect immediately. This request spawns an asynchronous workflow to fulfill the request. WorkRequest objects provide visibility for in-progress workflows.""")
@cli_util.help_option_group
def tagging_work_request_group():
    pass


@click.command(cli_util.override('iam.dynamic_group_group.command_name', 'dynamic-group'), cls=CommandGroupWithAlias, help="""A dynamic group defines a matching rule. Every bare metal or virtual machine instance is deployed with an instance certificate. The certificate contains metadata about the instance. This includes the instance OCID and the compartment OCID, along with a few other optional properties. When an API call is made using this instance certificate as the authenticator, the certificate can be matched to one or multiple dynamic groups. The instance can then get access to the API based on the permissions granted in policies written for the dynamic groups.

This works like regular user/group membership. But in that case, the membership is a static relationship, whereas in a dynamic group, the membership of an instance certificate to a dynamic group is determined during runtime. For more information, see [Managing Dynamic Groups].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def dynamic_group_group():
    pass


@click.command(cli_util.override('iam.region_group.command_name', 'region'), cls=CommandGroupWithAlias, help="""A localized geographic area, such as Phoenix, AZ. Oracle Cloud Infrastructure is hosted in regions and Availability Domains. A region is composed of several Availability Domains. An Availability Domain is one or more data centers located within a region. For more information, see [Regions and Availability Domains].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Get Started with Policies].""")
@cli_util.help_option_group
def region_group():
    pass


@click.command(cli_util.override('iam.auth_token_group.command_name', 'auth-token'), cls=CommandGroupWithAlias, help="""An `AuthToken` is an Oracle-generated token string that you can use to authenticate with third-party APIs that do not support Oracle Cloud Infrastructure's signature-based authentication. For example, use an `AuthToken` to authenticate with a Swift client with the Object Storage Service.

The auth token is associated with the user's Console login. Auth tokens never expire. A user can have up to two auth tokens at a time.

**Note:** The token is always an Oracle-generated string; you can't change it to a string of your choice.

For more information, see [Managing User Credentials].""")
@cli_util.help_option_group
def auth_token_group():
    pass


@click.command(cli_util.override('iam.swift_password_group.command_name', 'swift-password'), cls=CommandGroupWithAlias, help="""**Deprecated. Use [AuthToken] instead.**

Swift is the OpenStack object storage service. A `SwiftPassword` is an Oracle-provided password for using a Swift client with the Object Storage Service. This password is associated with the user's Console login. Swift passwords never expire. A user can have up to two Swift passwords at a time.

**Note:** The password is always an Oracle-generated string; you can't change it to a string of your choice.

For more information, see [Managing User Credentials].""")
@cli_util.help_option_group
def swift_password_group():
    pass


@click.command(cli_util.override('iam.tag_default_group.command_name', 'tag-default'), cls=CommandGroupWithAlias, help="""Tag defaults let you specify a default tag (tagnamespace.tag=\"value\") to apply to all resource types in a specified compartment. The tag default is applied at the time the resource is created. Resources that exist in the compartment before you create the tag default are not tagged. The `TagDefault` object specifies the tag and compartment details.

Tag defaults are inherited by child compartments. This means that if you set a tag default on the root compartment for a tenancy, all resources that are created in the tenancy are tagged. For more information about using tag defaults, see [Managing Tag Defaults].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator.""")
@cli_util.help_option_group
def tag_default_group():
    pass


@click.command(cli_util.override('iam.user_group.command_name', 'user'), cls=CommandGroupWithAlias, help="""An individual employee or system that needs to manage or use your company's Oracle Cloud Infrastructure resources. Users might need to launch instances, manage remote disks, work with your cloud network, etc. Users have one or more IAM Service credentials ([ApiKey], [UIPassword], [SwiftPassword] and [AuthToken]). For more information, see [User Credentials]). End users of your application are not typically IAM Service users, but for tenancies that have identity domains, they might be. For conceptual information about users and other IAM Service components, see [Overview of IAM].

These users are created directly within the Oracle Cloud Infrastructure system, via the IAM service. They are different from *federated users*, who authenticate themselves to the Oracle Cloud Infrastructure Console via an identity provider. For more information, see [Identity Providers and Federation].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Get Started with Policies].

**Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.""")
@cli_util.help_option_group
def user_group():
    pass


iam_root_group.add_command(fault_domain_group)
iam_root_group.add_command(work_request_group)
iam_root_group.add_command(tagging_work_request_log_group)
iam_root_group.add_command(compartment_group)
iam_root_group.add_command(network_sources_group)
iam_root_group.add_command(authentication_policy_group)
iam_root_group.add_command(smtp_credential_group)
iam_root_group.add_command(scim_client_credentials_group)
iam_root_group.add_command(tag_group)
iam_root_group.add_command(iam_work_request_log_group)
iam_root_group.add_command(bulk_edit_tags_resource_type_collection_group)
iam_root_group.add_command(group_group)
iam_root_group.add_command(policy_group)
iam_root_group.add_command(tag_namespace_group)
iam_root_group.add_command(availability_domain_group)
iam_root_group.add_command(bulk_action_resource_type_collection_group)
iam_root_group.add_command(customer_secret_key_group)
iam_root_group.add_command(idp_group_mapping_group)
iam_root_group.add_command(tenancy_group)
iam_root_group.add_command(user_group_membership_group)
iam_root_group.add_command(mfa_totp_device_group)
iam_root_group.add_command(ui_password_information_group)
iam_root_group.add_command(identity_provider_group)
iam_root_group.add_command(identity_provider_group_group)
iam_root_group.add_command(ui_password_group)
iam_root_group.add_command(api_key_group)
iam_root_group.add_command(domain_group)
iam_root_group.add_command(tagging_work_request_error_group)
iam_root_group.add_command(region_subscription_group)
iam_root_group.add_command(standard_tag_namespace_template_group)
iam_root_group.add_command(iam_work_request_group)
iam_root_group.add_command(tagging_work_request_group)
iam_root_group.add_command(dynamic_group_group)
iam_root_group.add_command(region_group)
iam_root_group.add_command(auth_token_group)
iam_root_group.add_command(swift_password_group)
iam_root_group.add_command(tag_default_group)
iam_root_group.add_command(user_group)


@domain_group.command(name=cli_util.override('iam.activate_domain.command_name', 'activate'), help=u"""(For tenancies that support identity domains) Activates a deactivated identity domain. You can only activate identity domains that your user account is not a part of.

After you send the request, the `lifecycleDetails` of the identity domain is set to ACTIVATING. When the operation completes, the `lifecycleDetails` is set to null and the `lifecycleState` of the identity domain is set to ACTIVE.

To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status. \n[Command Reference](activateDomain)""")
@cli_util.option('--domain-id', required=True, help=u"""The OCID of the identity domain.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def activate_domain(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, domain_id, if_match):

    if isinstance(domain_id, six.string_types) and len(domain_id.strip()) == 0:
        raise click.UsageError('Parameter --domain-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.activate_domain(
        domain_id=domain_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_iam_work_request') and callable(getattr(client, 'get_iam_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_iam_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@mfa_totp_device_group.command(name=cli_util.override('iam.activate_mfa_totp_device.command_name', 'activate'), help=u"""Activates the specified MFA TOTP device for the user. Activation requires manual interaction with the Console. \n[Command Reference](activateMfaTotpDevice)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--mfa-totp-device-id', required=True, help=u"""The OCID of the MFA TOTP device.""")
@cli_util.option('--totp-token', help=u"""The Totp token for MFA.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'MfaTotpDeviceSummary'})
@cli_util.wrap_exceptions
def activate_mfa_totp_device(ctx, from_json, user_id, mfa_totp_device_id, totp_token, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(mfa_totp_device_id, six.string_types) and len(mfa_totp_device_id.strip()) == 0:
        raise click.UsageError('Parameter --mfa-totp-device-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if totp_token is not None:
        _details['totpToken'] = totp_token

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.activate_mfa_totp_device(
        user_id=user_id,
        mfa_totp_device_id=mfa_totp_device_id,
        mfa_totp_token=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tag_default_group.command(name=cli_util.override('iam.add_tag_default_lock.command_name', 'add'), help=u"""Add a resource lock to a tag default. \n[Command Reference](addTagDefaultLock)""")
@cli_util.option('--tag-default-id', required=True, help=u"""The OCID of the tag default.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["FULL", "DELETE"]), help=u"""Type of the lock.""")
@cli_util.option('--related-resource-id', help=u"""The ID of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.""")
@cli_util.option('--message', help=u"""A message added by the creator of the lock. This is typically used to give an indication of why the resource is locked.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'TagDefault'})
@cli_util.wrap_exceptions
def add_tag_default_lock(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_default_id, type, related_resource_id, message, if_match):

    if isinstance(tag_default_id, six.string_types) and len(tag_default_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-default-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    if related_resource_id is not None:
        _details['relatedResourceId'] = related_resource_id

    if message is not None:
        _details['message'] = message

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.add_tag_default_lock(
        tag_default_id=tag_default_id,
        add_lock_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag_default') and callable(getattr(client, 'get_tag_default')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag_default(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tag_namespace_group.command(name=cli_util.override('iam.add_tag_namespace_lock.command_name', 'add'), help=u"""Add a resource lock to a tag namespace. \n[Command Reference](addTagNamespaceLock)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["FULL", "DELETE"]), help=u"""Type of the lock.""")
@cli_util.option('--related-resource-id', help=u"""The ID of the resource that is locking this resource. Indicates that deleting this resource will remove the lock.""")
@cli_util.option('--message', help=u"""A message added by the creator of the lock. This is typically used to give an indication of why the resource is locked.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'TagNamespace'})
@cli_util.wrap_exceptions
def add_tag_namespace_lock(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_namespace_id, type, related_resource_id, message, if_match):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    if related_resource_id is not None:
        _details['relatedResourceId'] = related_resource_id

    if message is not None:
        _details['message'] = message

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.add_tag_namespace_lock(
        tag_namespace_id=tag_namespace_id,
        add_lock_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag_namespace') and callable(getattr(client, 'get_tag_namespace')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag_namespace(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@user_group_membership_group.command(name=cli_util.override('iam.add_user_to_group.command_name', 'add'), help=u"""Adds the specified user to the specified group and returns a `UserGroupMembership` object with its own OCID.

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE. \n[Command Reference](addUserToGroup)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--group-id', required=True, help=u"""The OCID of the group.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'UserGroupMembership'})
@cli_util.wrap_exceptions
def add_user_to_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, user_id, group_id):

    kwargs = {}

    _details = {}
    _details['userId'] = user_id
    _details['groupId'] = group_id

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.add_user_to_group(
        add_user_to_group_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_user_group_membership') and callable(getattr(client, 'get_user_group_membership')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_user_group_membership(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tag_default_group.command(name=cli_util.override('iam.assemble_effective_tag_set.command_name', 'assemble-effective-tag-set'), help=u"""Assembles tag defaults in the specified compartment and any parent compartments to determine the tags to apply. Tag defaults from parent compartments do not override tag defaults referencing the same tag in a compartment lower down the hierarchy. This set of tag defaults includes all tag defaults from the current compartment back to the root compartment. \n[Command Reference](assembleEffectiveTagSet)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[TagDefaultSummary]'})
@cli_util.wrap_exceptions
def assemble_effective_tag_set(ctx, from_json, compartment_id, lifecycle_state):

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.assemble_effective_tag_set(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compartment_group.command(name=cli_util.override('iam.bulk_delete_resources.command_name', 'bulk-delete-resources'), help=u"""Deletes multiple resources in the compartment. All resources must be in the same compartment. You must have the appropriate permissions to delete the resources in the request. This API can only be invoked from the tenancy's [home region]. This operation creates a [WorkRequest]. Use the [GetWorkRequest] API to monitor the status of the bulk action. \n[Command Reference](bulkDeleteResources)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--resources', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The resources to be deleted.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'resources': {'module': 'identity', 'class': 'list[BulkActionResource]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'resources': {'module': 'identity', 'class': 'list[BulkActionResource]'}})
@cli_util.wrap_exceptions
def bulk_delete_resources(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, resources):

    if isinstance(compartment_id, six.string_types) and len(compartment_id.strip()) == 0:
        raise click.UsageError('Parameter --compartment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['resources'] = cli_util.parse_json_parameter("resources", resources)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.bulk_delete_resources(
        compartment_id=compartment_id,
        bulk_delete_resources_details=_details,
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


@tag_group.command(name=cli_util.override('iam.bulk_delete_tags.command_name', 'bulk-delete'), help=u"""Deletes the specified tag key definitions. This operation triggers a process that removes the tags from all resources in your tenancy. The tag key definitions must be within the same tag namespace.

The following actions happen immediately: \u00A0   * If the tag is a cost-tracking tag, the tag no longer counts against your   10 cost-tracking tags limit, even if you do not disable the tag before running this operation.   * If the tag is used with dynamic groups, the rules that contain the tag are no longer   evaluated against the tag.

After you start this operation, the state of the tag changes to DELETING, and tag removal from resources begins. This process can take up to 48 hours depending on the number of resources that are tagged and the regions in which those resources reside.

When all tags have been removed, the state changes to DELETED. You cannot restore a deleted tag. After the tag state changes to DELETED, you can use the same tag name again.

After you start this operation, you cannot start either the [DeleteTag] or the [CascadeDeleteTagNamespace] operation until this process completes.

In order to delete tags, you must first retire the tags. Use [UpdateTag] to retire a tag. \n[Command Reference](bulkDeleteTags)""")
@cli_util.option('--tag-definition-ids', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The OCIDs of the tag definitions to delete""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'tag-definition-ids': {'module': 'identity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'tag-definition-ids': {'module': 'identity', 'class': 'list[string]'}})
@cli_util.wrap_exceptions
def bulk_delete_tags(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_definition_ids, is_lock_override):

    kwargs = {}
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['tagDefinitionIds'] = cli_util.parse_json_parameter("tag_definition_ids", tag_definition_ids)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.bulk_delete_tags(
        bulk_delete_tags_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tagging_work_request') and callable(getattr(client, 'get_tagging_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tagging_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@tag_group.command(name=cli_util.override('iam.bulk_edit_tags.command_name', 'bulk-edit'), help=u"""Edits the specified list of tag key definitions for the selected resources. This operation triggers a process that edits the tags on all selected resources. The possible actions are:

  * Add a defined tag when the tag does not already exist on the resource.   * Update the value for a defined tag when the tag is present on the resource.   * Add a defined tag when it does not already exist on the resource or update the value for a defined tag when the tag is present on the resource.   * Remove a defined tag from a resource. The tag is removed from the resource regardless of the tag value.

See [BulkEditOperationDetails] for more information.

The edits can include a combination of operations and tag sets. However, multiple operations cannot apply to one key definition in the same request. For example, if one request adds `tag set-1` to a resource and sets a tag value to `tag set-2`, `tag set-1` and `tag set-2` cannot have any common tag definitions. \n[Command Reference](bulkEditTags)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where the bulk tag edit request is submitted.""")
@cli_util.option('--resources', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The resources to be updated.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--bulk-edit-operations', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The operations associated with the request to bulk edit tags.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'resources': {'module': 'identity', 'class': 'list[BulkEditResource]'}, 'bulk-edit-operations': {'module': 'identity', 'class': 'list[BulkEditOperationDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'resources': {'module': 'identity', 'class': 'list[BulkEditResource]'}, 'bulk-edit-operations': {'module': 'identity', 'class': 'list[BulkEditOperationDetails]'}})
@cli_util.wrap_exceptions
def bulk_edit_tags(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, resources, bulk_edit_operations):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['resources'] = cli_util.parse_json_parameter("resources", resources)
    _details['bulkEditOperations'] = cli_util.parse_json_parameter("bulk_edit_operations", bulk_edit_operations)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.bulk_edit_tags(
        bulk_edit_tags_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tagging_work_request') and callable(getattr(client, 'get_tagging_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tagging_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@compartment_group.command(name=cli_util.override('iam.bulk_move_resources.command_name', 'bulk-move-resources'), help=u"""Moves multiple resources from one compartment to another. All resources must be in the same compartment. This API can only be invoked from the tenancy's [home region]. To move resources, you must have the appropriate permissions to move the resource in both the source and target compartments. This operation creates a [WorkRequest]. Use the [GetWorkRequest] API to monitor the status of the bulk action. \n[Command Reference](bulkMoveResources)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--resources', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""The resources to be moved.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-compartment-id', required=True, help=u"""The [OCID] of the destination compartment into which to move the resources.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'resources': {'module': 'identity', 'class': 'list[BulkActionResource]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'resources': {'module': 'identity', 'class': 'list[BulkActionResource]'}})
@cli_util.wrap_exceptions
def bulk_move_resources(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, resources, target_compartment_id):

    if isinstance(compartment_id, six.string_types) and len(compartment_id.strip()) == 0:
        raise click.UsageError('Parameter --compartment-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['resources'] = cli_util.parse_json_parameter("resources", resources)
    _details['targetCompartmentId'] = target_compartment_id

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.bulk_move_resources(
        compartment_id=compartment_id,
        bulk_move_resources_details=_details,
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


@tag_namespace_group.command(name=cli_util.override('iam.cascade_delete_tag_namespace.command_name', 'cascade-delete'), help=u"""Deletes the specified tag namespace. This operation triggers a process that removes all of the tags defined in the specified tag namespace from all resources in your tenancy and then deletes the tag namespace.

After you start the delete operation:

  * New tag key definitions cannot be created under the namespace.   * The state of the tag namespace changes to DELETING.   * Tag removal from the resources begins.

This process can take up to 48 hours depending on the number of tag definitions in the namespace, the number of resources that are tagged, and the locations of the regions in which those resources reside.

After all tags are removed, the state changes to DELETED. You cannot restore a deleted tag namespace. After the deleted tag namespace changes its state to DELETED, you can use the name of the deleted tag namespace again.

After you start this operation, you cannot start either the [DeleteTag] or the [BulkDeleteTags] operation until this process completes.

To delete a tag namespace, you must first retire it. Use [UpdateTagNamespace] to retire a tag namespace. \n[Command Reference](cascadeDeleteTagNamespace)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def cascade_delete_tag_namespace(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_namespace_id, if_match, is_lock_override):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.cascade_delete_tag_namespace(
        tag_namespace_id=tag_namespace_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tagging_work_request') and callable(getattr(client, 'get_tagging_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tagging_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@domain_group.command(name=cli_util.override('iam.change_domain_compartment.command_name', 'change-compartment'), help=u"""(For tenancies that support identity domains) Moves the identity domain to a different compartment in the tenancy.

To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status. \n[Command Reference](changeDomainCompartment)""")
@cli_util.option('--domain-id', required=True, help=u"""The OCID of the identity domain.""")
@cli_util.option('--compartment-id', required=True, help=u"""The [OCID] of the destination compartment into which to move the identity domain.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_domain_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, domain_id, compartment_id, if_match):

    if isinstance(domain_id, six.string_types) and len(domain_id.strip()) == 0:
        raise click.UsageError('Parameter --domain-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.change_domain_compartment(
        domain_id=domain_id,
        change_domain_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_iam_work_request') and callable(getattr(client, 'get_iam_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_iam_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@domain_group.command(name=cli_util.override('iam.change_domain_license_type.command_name', 'change-domain-license-type'), help=u"""(For tenancies that support identity domains) Changes the license type of the given identity domain. The identity domain's `lifecycleState` must be set to ACTIVE and the requested `licenseType` must be allowed. To retrieve the allowed `licenseType` for the identity domain, use [ListAllowedDomainLicenseTypes].

After you send your request, the `lifecycleDetails` of this identity domain is set to UPDATING. When the update of the identity domain completes, then the `lifecycleDetails` is set to null.

To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status. \n[Command Reference](changeDomainLicenseType)""")
@cli_util.option('--domain-id', required=True, help=u"""The OCID of the identity domain.""")
@cli_util.option('--license-type', help=u"""The license type of the identity domain.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_domain_license_type(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, domain_id, license_type, if_match):

    if isinstance(domain_id, six.string_types) and len(domain_id.strip()) == 0:
        raise click.UsageError('Parameter --domain-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if license_type is not None:
        _details['licenseType'] = license_type

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.change_domain_license_type(
        domain_id=domain_id,
        change_domain_license_type_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_iam_work_request') and callable(getattr(client, 'get_iam_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_iam_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@tag_namespace_group.command(name=cli_util.override('iam.change_tag_namespace_compartment.command_name', 'change-compartment'), help=u"""Moves the specified tag namespace to the specified compartment within the same tenancy.

To move the tag namespace, you must have the manage tag-namespaces permission on both compartments. For more information about IAM policies, see [Details for IAM].

Moving a tag namespace moves all the tag key definitions contained in the tag namespace. \n[Command Reference](changeTagNamespaceCompartment)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--compartment-id', required=True, help=u"""The Oracle Cloud ID (OCID) of the destination compartment.""")
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_tag_namespace_compartment(ctx, from_json, tag_namespace_id, compartment_id, is_lock_override):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    kwargs = {}
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.change_tag_namespace_compartment(
        tag_namespace_id=tag_namespace_id,
        change_tag_namespace_compartment_detail=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auth_token_group.command(name=cli_util.override('iam.create_auth_token.command_name', 'create'), help=u"""Creates a new auth token for the specified user. For information about what auth tokens are for, see [Managing User Credentials].

You must specify a *description* for the auth token (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateAuthToken].

Every user has permission to create an auth token for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to create an auth token for any user, including themselves. \n[Command Reference](createAuthToken)""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the auth token during creation. Does not have to be unique, and it's changeable.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'AuthToken'})
@cli_util.wrap_exceptions
def create_auth_token(ctx, from_json, description, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}
    _details['description'] = description

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_auth_token(
        user_id=user_id,
        create_auth_token_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compartment_group.command(name=cli_util.override('iam.create_compartment.command_name', 'create'), help=u"""Creates a new compartment in the specified compartment.

Specify the parent compartment's OCID as the compartment ID in the request object. Remember that the tenancy is simply the root compartment. For information about OCIDs, see [Resource Identifiers].

You must also specify a *name* for the compartment, which must be unique across all compartments in your tenancy. You can use this name or the OCID when writing policies that apply to the compartment. For more information about policies, see [How Policies Work].

You must also specify a *description* for the compartment (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateCompartment].

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE. \n[Command Reference](createCompartment)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the parent compartment containing the compartment.""")
@cli_util.option('--name', required=True, help=u"""The name you assign to the compartment during creation. The name must be unique across all compartments in the parent compartment. Avoid entering confidential information.""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the compartment during creation. Does not have to be unique, and it's changeable.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'Compartment'})
@cli_util.wrap_exceptions
def create_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, name, description, freeform_tags, defined_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['name'] = name
    _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_compartment(
        create_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_compartment') and callable(getattr(client, 'get_compartment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_compartment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@customer_secret_key_group.command(name=cli_util.override('iam.create_customer_secret_key.command_name', 'create'), help=u"""Creates a new secret key for the specified user. Secret keys are used for authentication with the Object Storage Service's Amazon S3 compatible API. The secret key consists of an Access Key/Secret Key pair. For information, see [Managing User Credentials].

You must specify a *description* for the secret key (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateCustomerSecretKey].

Every user has permission to create a secret key for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to create a secret key for any user, including themselves. \n[Command Reference](createCustomerSecretKey)""")
@cli_util.option('--display-name', required=True, help=u"""The name you assign to the secret key during creation. Does not have to be unique, and it's changeable.""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'CustomerSecretKey'})
@cli_util.wrap_exceptions
def create_customer_secret_key(ctx, from_json, display_name, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}
    _details['displayName'] = display_name

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_customer_secret_key(
        user_id=user_id,
        create_customer_secret_key_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.create_db_credential.command_name', 'create-db-credential'), help=u"""Creates a new DB credential for the specified user. \n[Command Reference](createDbCredential)""")
@cli_util.option('--password', required=True, help=u"""The password for the DB credentials during creation.""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the DB credentials during creation.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'DbCredential'})
@cli_util.wrap_exceptions
def create_db_credential(ctx, from_json, password, description, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['password'] = password
    _details['description'] = description

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_db_credential(
        user_id=user_id,
        create_db_credential_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@domain_group.command(name=cli_util.override('iam.create_domain.command_name', 'create'), help=u"""(For tenancies that support identity domains) Creates a new identity domain in the tenancy with the identity domain home in `homeRegion`. After you send your request, the temporary `lifecycleState` of this identity domain is set to CREATING and `lifecycleDetails` to UPDATING. When creation of the identity domain completes, this identity domain's `lifecycleState` is set to ACTIVE and `lifecycleDetails` to null.

To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status.

After creating an `identity domain`, first make sure its `lifecycleState` changes from CREATING to ACTIVE before you use it. \n[Command Reference](createDomain)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where the identity domain is created.""")
@cli_util.option('--display-name', required=True, help=u"""The mutable display name of the identity domain.""")
@cli_util.option('--description', required=True, help=u"""The identity domain description. You can have an empty description.""")
@cli_util.option('--home-region', required=True, help=u"""The region's name identifier. See [Regions and Availability Domains] for the full list of supported region names.

Example: `us-phoenix-1`""")
@cli_util.option('--license-type', required=True, help=u"""The license type of the identity domain.""")
@cli_util.option('--is-hidden-on-login', type=click.BOOL, help=u"""Indicates whether the identity domain is hidden on the sign-in screen or not.""")
@cli_util.option('--admin-first-name', help=u"""The administrator's first name.""")
@cli_util.option('--admin-last-name', help=u"""The administrator's last name.""")
@cli_util.option('--admin-user-name', help=u"""The administrator's user name.""")
@cli_util.option('--admin-email', help=u"""The administrator's email address.""")
@cli_util.option('--is-notification-bypassed', type=click.BOOL, help=u"""Indicates whether or not the administrator user created in the IDCS stripe would like to receive notifications like a welcome email. This field is required only if admin information is provided. This field is otherwise optional.""")
@cli_util.option('--is-primary-email-required', type=click.BOOL, help=u"""Optional field to indicate whether users in the identity domain are required to have a primary email address or not. The default is true.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_domain(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, description, home_region, license_type, is_hidden_on_login, admin_first_name, admin_last_name, admin_user_name, admin_email, is_notification_bypassed, is_primary_email_required, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['displayName'] = display_name
    _details['description'] = description
    _details['homeRegion'] = home_region
    _details['licenseType'] = license_type

    if is_hidden_on_login is not None:
        _details['isHiddenOnLogin'] = is_hidden_on_login

    if admin_first_name is not None:
        _details['adminFirstName'] = admin_first_name

    if admin_last_name is not None:
        _details['adminLastName'] = admin_last_name

    if admin_user_name is not None:
        _details['adminUserName'] = admin_user_name

    if admin_email is not None:
        _details['adminEmail'] = admin_email

    if is_notification_bypassed is not None:
        _details['isNotificationBypassed'] = is_notification_bypassed

    if is_primary_email_required is not None:
        _details['isPrimaryEmailRequired'] = is_primary_email_required

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_domain(
        create_domain_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_iam_work_request') and callable(getattr(client, 'get_iam_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_iam_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@dynamic_group_group.command(name=cli_util.override('iam.create_dynamic_group.command_name', 'create'), help=u"""Creates a new dynamic group in your tenancy.

You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies) reside within the tenancy itself, unlike cloud resources such as compute instances, which typically reside within compartments inside the tenancy. For information about OCIDs, see [Resource Identifiers].

You must also specify a *name* for the dynamic group, which must be unique across all dynamic groups in your tenancy, and cannot be changed. Note that this name has to be also unique across all groups in your tenancy. You can use this name or the OCID when writing policies that apply to the dynamic group. For more information about policies, see [How Policies Work].

You must also specify a *description* for the dynamic group (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateDynamicGroup].

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE. \n[Command Reference](createDynamicGroup)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy containing the group.""")
@cli_util.option('--name', required=True, help=u"""The name you assign to the group during creation. The name must be unique across all groups in the tenancy and cannot be changed.""")
@cli_util.option('--matching-rule', required=True, help=u"""The matching rule to dynamically match an instance certificate to this dynamic group. For rule syntax, see [Managing Dynamic Groups].""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the group during creation. Does not have to be unique, and it's changeable.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'DynamicGroup'})
@cli_util.wrap_exceptions
def create_dynamic_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, name, matching_rule, description, freeform_tags, defined_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['name'] = name
    _details['matchingRule'] = matching_rule
    _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_dynamic_group(
        create_dynamic_group_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dynamic_group') and callable(getattr(client, 'get_dynamic_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_dynamic_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@group_group.command(name=cli_util.override('iam.create_group.command_name', 'create'), help=u"""Creates a new group in your tenancy.

You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies) reside within the tenancy itself, unlike cloud resources such as compute instances, which typically reside within compartments inside the tenancy. For information about OCIDs, see [Resource Identifiers].

You must also specify a *name* for the group, which must be unique across all groups in your tenancy and cannot be changed. You can use this name or the OCID when writing policies that apply to the group. For more information about policies, see [How Policies Work].

You must also specify a *description* for the group (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateGroup].

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.

After creating the group, you need to put users in it and write policies for it. See [AddUserToGroup] and [CreatePolicy]. \n[Command Reference](createGroup)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy containing the group.""")
@cli_util.option('--name', required=True, help=u"""The name you assign to the group during creation. The name must be unique across all groups in the tenancy and cannot be changed.""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the group during creation. Does not have to be unique, and it's changeable.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'Group'})
@cli_util.wrap_exceptions
def create_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, name, description, freeform_tags, defined_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['name'] = name
    _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_group(
        create_group_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_group') and callable(getattr(client, 'get_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@identity_provider_group.command(name=cli_util.override('iam.create_identity_provider.command_name', 'create'), help=u"""**Deprecated.** For more information, see [Deprecated IAM Service APIs].

Creates a new identity provider in your tenancy. For more information, see [Identity Providers and Federation].

You must specify your tenancy's OCID as the compartment ID in the request object. Remember that the tenancy is simply the root compartment. For information about OCIDs, see [Resource Identifiers].

You must also specify a *name* for the `IdentityProvider`, which must be unique across all `IdentityProvider` objects in your tenancy and cannot be changed.

You must also specify a *description* for the `IdentityProvider` (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateIdentityProvider].

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE. \n[Command Reference](createIdentityProvider)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of your tenancy.""")
@cli_util.option('--name', required=True, help=u"""The name you assign to the `IdentityProvider` during creation. The name must be unique across all `IdentityProvider` objects in the tenancy and cannot be changed.""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the `IdentityProvider` during creation. Does not have to be unique, and it's changeable.""")
@cli_util.option('--product-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["IDCS", "ADFS"]), help=u"""The identity provider service or product. Supported identity providers are Oracle Identity Cloud Service (IDCS) and Microsoft Active Directory Federation Services (ADFS).

Example: `IDCS`""")
@cli_util.option('--protocol', required=True, type=custom_types.CliCaseInsensitiveChoice(["SAML2", "ADFS"]), help=u"""The protocol used for federation.

Example: `SAML2`""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'IdentityProvider'})
@cli_util.wrap_exceptions
def create_identity_provider(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, name, description, product_type, protocol, freeform_tags, defined_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['name'] = name
    _details['description'] = description
    _details['productType'] = product_type
    _details['protocol'] = protocol

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_identity_provider(
        create_identity_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_identity_provider') and callable(getattr(client, 'get_identity_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_identity_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@identity_provider_group.command(name=cli_util.override('iam.create_identity_provider_create_saml2_identity_provider_details.command_name', 'create-identity-provider-create-saml2-identity-provider-details'), help=u"""**Deprecated.** For more information, see [Deprecated IAM Service APIs].

Creates a new identity provider in your tenancy. For more information, see [Identity Providers and Federation].

You must specify your tenancy's OCID as the compartment ID in the request object. Remember that the tenancy is simply the root compartment. For information about OCIDs, see [Resource Identifiers].

You must also specify a *name* for the `IdentityProvider`, which must be unique across all `IdentityProvider` objects in your tenancy and cannot be changed.

You must also specify a *description* for the `IdentityProvider` (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateIdentityProvider].

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE. \n[Command Reference](createIdentityProvider)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of your tenancy.""")
@cli_util.option('--name', required=True, help=u"""The name you assign to the `IdentityProvider` during creation. The name must be unique across all `IdentityProvider` objects in the tenancy and cannot be changed.""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the `IdentityProvider` during creation. Does not have to be unique, and it's changeable.""")
@cli_util.option('--product-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["IDCS", "ADFS"]), help=u"""The identity provider service or product. Supported identity providers are Oracle Identity Cloud Service (IDCS) and Microsoft Active Directory Federation Services (ADFS).

Example: `IDCS`""")
@cli_util.option('--metadata-url', required=True, help=u"""The URL for retrieving the identity provider's metadata, which contains information required for federating.""")
@cli_util.option('--metadata', required=True, help=u"""The XML that contains the information required for federating.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-attributes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Extra name value pairs associated with this identity provider. Example: `{\"clientId\": \"app_sf3kdjf3\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'freeform-attributes': {'module': 'identity', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'freeform-attributes': {'module': 'identity', 'class': 'dict(str, string)'}}, output_type={'module': 'identity', 'class': 'IdentityProvider'})
@cli_util.wrap_exceptions
def create_identity_provider_create_saml2_identity_provider_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, name, description, product_type, metadata_url, metadata, freeform_tags, defined_tags, freeform_attributes):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['name'] = name
    _details['description'] = description
    _details['productType'] = product_type
    _details['metadataUrl'] = metadata_url
    _details['metadata'] = metadata

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if freeform_attributes is not None:
        _details['freeformAttributes'] = cli_util.parse_json_parameter("freeform_attributes", freeform_attributes)

    _details['protocol'] = 'SAML2'

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_identity_provider(
        create_identity_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_identity_provider') and callable(getattr(client, 'get_identity_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_identity_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@idp_group_mapping_group.command(name=cli_util.override('iam.create_idp_group_mapping.command_name', 'create'), help=u"""**Deprecated.** For more information, see [Deprecated IAM Service APIs].

Creates a single mapping between an IdP group and an IAM Service [group]. \n[Command Reference](createIdpGroupMapping)""")
@cli_util.option('--idp-group-name', required=True, help=u"""The name of the IdP group you want to map.""")
@cli_util.option('--group-id', required=True, help=u"""The OCID of the IAM Service [group] you want to map to the IdP group.""")
@cli_util.option('--identity-provider-id', required=True, help=u"""The OCID of the identity provider.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'IdpGroupMapping'})
@cli_util.wrap_exceptions
def create_idp_group_mapping(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, idp_group_name, group_id, identity_provider_id):

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}
    _details['idpGroupName'] = idp_group_name
    _details['groupId'] = group_id

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_idp_group_mapping(
        identity_provider_id=identity_provider_id,
        create_idp_group_mapping_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_idp_group_mapping') and callable(getattr(client, 'get_idp_group_mapping')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_idp_group_mapping(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@mfa_totp_device_group.command(name=cli_util.override('iam.create_mfa_totp_device.command_name', 'create'), help=u"""Creates a new MFA TOTP device for the user. A user can have one MFA TOTP device. \n[Command Reference](createMfaTotpDevice)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'MfaTotpDevice'})
@cli_util.wrap_exceptions
def create_mfa_totp_device(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_mfa_totp_device(
        user_id=user_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_mfa_totp_device') and callable(getattr(client, 'get_mfa_totp_device')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_mfa_totp_device(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@network_sources_group.command(name=cli_util.override('iam.create_network_source.command_name', 'create'), help=u"""Creates a new network source in your tenancy.

You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies) reside within the tenancy itself, unlike cloud resources such as compute instances, which typically reside within compartments inside the tenancy. For information about OCIDs, see [Resource Identifiers].

You must also specify a *name* for the network source, which must be unique across all network sources in your tenancy, and cannot be changed. You can use this name or the OCID when writing policies that apply to the network source. For more information about policies, see [How Policies Work].

You must also specify a *description* for the network source (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateNetworkSource].

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.

After your network resource is created, you can use it in policy to restrict access to only requests made from an allowed IP address specified in your network source. For more information, see [Managing Network Sources]. \n[Command Reference](createNetworkSource)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy (root compartment) containing the network source object.""")
@cli_util.option('--name', required=True, help=u"""The name you assign to the network source during creation. The name must be unique across all groups in the tenancy and cannot be changed.""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the network source during creation. Does not have to be unique, and it's changeable.""")
@cli_util.option('--public-source-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of allowed public IP addresses and CIDR ranges.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--virtual-source-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of allowed VCN OCID and IP range pairs. Example:`\"vcnId\": \"ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID\", \"ipRanges\": [ \"129.213.39.0/24\" ]`

This option is a JSON list with items of type NetworkSourcesVirtualSourceList.  For documentation on NetworkSources_virtualSourceList please see our API reference: https://docs.cloud.oracle.com/api/#/en/identity/20160918/datatypes/NetworkSourcesVirtualSourceList.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--services', type=custom_types.CLI_COMPLEX_TYPE, help=u"""-- The services attribute has no effect and is reserved for use by Oracle. --""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'public-source-list': {'module': 'identity', 'class': 'list[string]'}, 'virtual-source-list': {'module': 'identity', 'class': 'list[NetworkSourcesVirtualSourceList]'}, 'services': {'module': 'identity', 'class': 'list[string]'}, 'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'public-source-list': {'module': 'identity', 'class': 'list[string]'}, 'virtual-source-list': {'module': 'identity', 'class': 'list[NetworkSourcesVirtualSourceList]'}, 'services': {'module': 'identity', 'class': 'list[string]'}, 'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'NetworkSources'})
@cli_util.wrap_exceptions
def create_network_source(ctx, from_json, compartment_id, name, description, public_source_list, virtual_source_list, services, freeform_tags, defined_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['name'] = name
    _details['description'] = description

    if public_source_list is not None:
        _details['publicSourceList'] = cli_util.parse_json_parameter("public_source_list", public_source_list)

    if virtual_source_list is not None:
        _details['virtualSourceList'] = cli_util.parse_json_parameter("virtual_source_list", virtual_source_list)

    if services is not None:
        _details['services'] = cli_util.parse_json_parameter("services", services)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_network_source(
        create_network_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.create_o_auth_client_credential.command_name', 'create-o-auth-client-credential'), help=u"""Creates Oauth token for the user \n[Command Reference](createOAuthClientCredential)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--name', required=True, help=u"""Name of the oauth credential to help user differentiate them.""")
@cli_util.option('--description', required=True, help=u"""Description of the oauth credential to help user differentiate them.""")
@cli_util.option('--scopes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Allowed scopes for the given oauth credential.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'scopes': {'module': 'identity', 'class': 'list[FullyQualifiedScope]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'scopes': {'module': 'identity', 'class': 'list[FullyQualifiedScope]'}}, output_type={'module': 'identity', 'class': 'OAuth2ClientCredential'})
@cli_util.wrap_exceptions
def create_o_auth_client_credential(ctx, from_json, user_id, name, description, scopes):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}
    _details['name'] = name
    _details['description'] = description
    _details['scopes'] = cli_util.parse_json_parameter("scopes", scopes)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_o_auth_client_credential(
        user_id=user_id,
        create_o_auth2_client_credential_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ui_password_group.command(name=cli_util.override('iam.create_or_reset_ui_password.command_name', 'create-or-reset'), help=u"""Creates a new Console one-time password for the specified user. For more information about user credentials, see [User Credentials].

Use this operation after creating a new user, or if a user forgets their password. The new one-time password is returned to you in the response, and you must securely deliver it to the user. They'll be prompted to change this password the next time they sign in to the Console. If they don't change it within 7 days, the password will expire and you'll need to create a new one-time password for the user.

(For tenancies that support identity domains) Resetting a user's password generates a reset password email with a link that the user must follow to reset their password. If the user does not reset their password before the link expires, you'll need to reset the user's password again.

**Note:** The user's Console login is the unique name you specified when you created the user (see [CreateUser]). \n[Command Reference](createOrResetUIPassword)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'UIPassword'})
@cli_util.wrap_exceptions
def create_or_reset_ui_password(ctx, from_json, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_or_reset_ui_password(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@policy_group.command(name=cli_util.override('iam.create_policy.command_name', 'create'), help=u"""Creates a new policy in the specified compartment (either the tenancy or another of your compartments). If you're new to policies, see [Get Started with Policies].

You must specify a *name* for the policy, which must be unique across all policies in your tenancy and cannot be changed.

You must also specify a *description* for the policy (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdatePolicy].

You must specify one or more policy statements in the statements array. For information about writing policies, see [How Policies Work] and [Common Policies].

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.

New policies take effect typically within 10 seconds. \n[Command Reference](createPolicy)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment containing the policy (either the tenancy or another compartment).""")
@cli_util.option('--name', required=True, help=u"""The name you assign to the policy during creation. The name must be unique across all policies in the tenancy and cannot be changed.""")
@cli_util.option('--statements', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of policy statements written in the policy language. See [How Policies Work] and [Common Policies].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', required=True, help=u"""The description you assign to the policy during creation. Does not have to be unique, and it's changeable.""")
@cli_util.option('--version-date', type=custom_types.CLI_DATETIME, help=u"""The version of the policy. If null or set to an empty string, when a request comes in for authorization, the policy will be evaluated according to the current behavior of the services at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'statements': {'module': 'identity', 'class': 'list[string]'}, 'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'statements': {'module': 'identity', 'class': 'list[string]'}, 'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'Policy'})
@cli_util.wrap_exceptions
def create_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, name, statements, description, version_date, freeform_tags, defined_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['name'] = name
    _details['statements'] = cli_util.parse_json_parameter("statements", statements)
    _details['description'] = description

    if version_date is not None:
        _details['versionDate'] = version_date

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_policy(
        create_policy_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_policy') and callable(getattr(client, 'get_policy')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_policy(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@region_subscription_group.command(name=cli_util.override('iam.create_region_subscription.command_name', 'create'), help=u"""Creates a subscription to a region for a tenancy. \n[Command Reference](createRegionSubscription)""")
@cli_util.option('--region-key', required=True, help=u"""The regions's key. See [Regions and Availability Domains] for the full list of supported 3-letter region codes.

Example: `PHX`""")
@cli_util.option('--tenancy-id', required=True, help=u"""The OCID of the tenancy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'RegionSubscription'})
@cli_util.wrap_exceptions
def create_region_subscription(ctx, from_json, region_key, tenancy_id):

    if isinstance(tenancy_id, six.string_types) and len(tenancy_id.strip()) == 0:
        raise click.UsageError('Parameter --tenancy-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}
    _details['regionKey'] = region_key

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_region_subscription(
        tenancy_id=tenancy_id,
        create_region_subscription_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@smtp_credential_group.command(name=cli_util.override('iam.create_smtp_credential.command_name', 'create'), help=u"""Creates a new SMTP credential for the specified user. An SMTP credential has an SMTP user name and an SMTP password. You must specify a *description* for the SMTP credential (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateSmtpCredential]. \n[Command Reference](createSmtpCredential)""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the SMTP credentials during creation. Does not have to be unique, and it's changeable.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'SmtpCredential'})
@cli_util.wrap_exceptions
def create_smtp_credential(ctx, from_json, description, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}
    _details['description'] = description

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_smtp_credential(
        user_id=user_id,
        create_smtp_credential_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@swift_password_group.command(name=cli_util.override('iam.create_swift_password.command_name', 'create'), help=u"""**Deprecated. Use [CreateAuthToken] instead.**

Creates a new Swift password for the specified user. For information about what Swift passwords are for, see [Managing User Credentials].

You must specify a *description* for the Swift password (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateSwiftPassword].

Every user has permission to create a Swift password for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to create a Swift password for any user, including themselves. \n[Command Reference](createSwiftPassword)""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the Swift password during creation. Does not have to be unique, and it's changeable.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'SwiftPassword'})
@cli_util.wrap_exceptions
def create_swift_password(ctx, from_json, description, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}
    _details['description'] = description

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_swift_password(
        user_id=user_id,
        create_swift_password_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tag_group.command(name=cli_util.override('iam.create_tag.command_name', 'create'), help=u"""Creates a new tag in the specified tag namespace.

The tag requires either the OCID or the name of the tag namespace that will contain this tag definition.

You must specify a *name* for the tag, which must be unique across all tags in the tag namespace and cannot be changed. The name can contain any ASCII character except the space (_) or period (.) characters. Names are case insensitive. That means, for example, \"myTag\" and \"mytag\" are not allowed in the same namespace. If you specify a name that's already in use in the tag namespace, a 409 error is returned.

The tag must have a *description*. It does not have to be unique, and you can change it with [UpdateTag].

The tag must have a value type, which is specified with a validator. Tags can use either a static value or a list of possible values. Static values are entered by a user applying the tag to a resource. Lists are created by you and the user must apply a value from the list. Lists are validiated.

* If no `validator` is set, the user applying the tag to a resource can type in a static value or leave the tag value empty. * If a `validator` is set, the user applying the tag to a resource must select from a list of values that you supply with [EnumTagDefinitionValidator]. \n[Command Reference](createTag)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--name', required=True, help=u"""The name you assign to the tag during creation. This is the tag key definition. The name must be unique within the tag namespace and cannot be changed.""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the tag during creation.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-cost-tracking', type=click.BOOL, help=u"""Indicates whether the tag is enabled for cost tracking.""")
@cli_util.option('--validator', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'validator': {'module': 'identity', 'class': 'BaseTagDefinitionValidator'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'validator': {'module': 'identity', 'class': 'BaseTagDefinitionValidator'}}, output_type={'module': 'identity', 'class': 'Tag'})
@cli_util.wrap_exceptions
def create_tag(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_namespace_id, name, description, freeform_tags, defined_tags, is_cost_tracking, validator, is_lock_override):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    kwargs = {}
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override

    _details = {}
    _details['name'] = name
    _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if is_cost_tracking is not None:
        _details['isCostTracking'] = is_cost_tracking

    if validator is not None:
        _details['validator'] = cli_util.parse_json_parameter("validator", validator)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_tag(
        tag_namespace_id=tag_namespace_id,
        create_tag_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag') and callable(getattr(client, 'get_tag')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tag_group.command(name=cli_util.override('iam.create_tag_default_tag_definition_validator.command_name', 'create-tag-default-tag-definition-validator'), help=u"""Creates a new tag in the specified tag namespace.

The tag requires either the OCID or the name of the tag namespace that will contain this tag definition.

You must specify a *name* for the tag, which must be unique across all tags in the tag namespace and cannot be changed. The name can contain any ASCII character except the space (_) or period (.) characters. Names are case insensitive. That means, for example, \"myTag\" and \"mytag\" are not allowed in the same namespace. If you specify a name that's already in use in the tag namespace, a 409 error is returned.

The tag must have a *description*. It does not have to be unique, and you can change it with [UpdateTag].

The tag must have a value type, which is specified with a validator. Tags can use either a static value or a list of possible values. Static values are entered by a user applying the tag to a resource. Lists are created by you and the user must apply a value from the list. Lists are validiated.

* If no `validator` is set, the user applying the tag to a resource can type in a static value or leave the tag value empty. * If a `validator` is set, the user applying the tag to a resource must select from a list of values that you supply with [EnumTagDefinitionValidator]. \n[Command Reference](createTag)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--name', required=True, help=u"""The name you assign to the tag during creation. This is the tag key definition. The name must be unique within the tag namespace and cannot be changed.""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the tag during creation.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-cost-tracking', type=click.BOOL, help=u"""Indicates whether the tag is enabled for cost tracking.""")
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'Tag'})
@cli_util.wrap_exceptions
def create_tag_default_tag_definition_validator(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_namespace_id, name, description, freeform_tags, defined_tags, is_cost_tracking, is_lock_override):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    kwargs = {}
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override

    _details = {}
    _details['validator'] = {}
    _details['name'] = name
    _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if is_cost_tracking is not None:
        _details['isCostTracking'] = is_cost_tracking

    _details['validator']['validatorType'] = 'DEFAULT'

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_tag(
        tag_namespace_id=tag_namespace_id,
        create_tag_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag') and callable(getattr(client, 'get_tag')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tag_group.command(name=cli_util.override('iam.create_tag_enum_tag_definition_validator.command_name', 'create-tag-enum-tag-definition-validator'), help=u"""Creates a new tag in the specified tag namespace.

The tag requires either the OCID or the name of the tag namespace that will contain this tag definition.

You must specify a *name* for the tag, which must be unique across all tags in the tag namespace and cannot be changed. The name can contain any ASCII character except the space (_) or period (.) characters. Names are case insensitive. That means, for example, \"myTag\" and \"mytag\" are not allowed in the same namespace. If you specify a name that's already in use in the tag namespace, a 409 error is returned.

The tag must have a *description*. It does not have to be unique, and you can change it with [UpdateTag].

The tag must have a value type, which is specified with a validator. Tags can use either a static value or a list of possible values. Static values are entered by a user applying the tag to a resource. Lists are created by you and the user must apply a value from the list. Lists are validiated.

* If no `validator` is set, the user applying the tag to a resource can type in a static value or leave the tag value empty. * If a `validator` is set, the user applying the tag to a resource must select from a list of values that you supply with [EnumTagDefinitionValidator]. \n[Command Reference](createTag)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--name', required=True, help=u"""The name you assign to the tag during creation. This is the tag key definition. The name must be unique within the tag namespace and cannot be changed.""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the tag during creation.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-cost-tracking', type=click.BOOL, help=u"""Indicates whether the tag is enabled for cost tracking.""")
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@cli_util.option('--validator-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of allowed values for a definedTag value.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'validator-values': {'module': 'identity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'validator-values': {'module': 'identity', 'class': 'list[string]'}}, output_type={'module': 'identity', 'class': 'Tag'})
@cli_util.wrap_exceptions
def create_tag_enum_tag_definition_validator(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_namespace_id, name, description, freeform_tags, defined_tags, is_cost_tracking, is_lock_override, validator_values):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    kwargs = {}
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override

    _details = {}
    _details['validator'] = {}
    _details['name'] = name
    _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if is_cost_tracking is not None:
        _details['isCostTracking'] = is_cost_tracking

    if validator_values is not None:
        _details['validator']['values'] = cli_util.parse_json_parameter("validator_values", validator_values)

    _details['validator']['validatorType'] = 'ENUM'

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_tag(
        tag_namespace_id=tag_namespace_id,
        create_tag_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag') and callable(getattr(client, 'get_tag')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tag_default_group.command(name=cli_util.override('iam.create_tag_default.command_name', 'create'), help=u"""Creates a new tag default in the specified compartment for the specified tag definition.

If you specify that a value is required, a value is set during resource creation (either by the user creating the resource or another tag defualt). If no value is set, resource creation is blocked.

* If the `isRequired` flag is set to \"true\", the value is set during resource creation. * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation. \n[Command Reference](createTagDefault)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment. The tag default will be applied to all new resources created in this compartment.""")
@cli_util.option('--tag-definition-id', required=True, help=u"""The OCID of the tag definition. The tag default will always assign a default value for this tag definition.""")
@cli_util.option('--value', required=True, help=u"""The default value for the tag definition. This will be applied to all new resources created in the compartment.""")
@cli_util.option('--is-required', type=click.BOOL, help=u"""If you specify that a value is required, a value is set during resource creation (either by the user creating the resource or another tag defualt). If no value is set, resource creation is blocked.

* If the `isRequired` flag is set to \"true\", the value is set during resource creation. * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation.

Example: `false`""")
@cli_util.option('--locks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Locks associated with this resource.

This option is a JSON list with items of type AddLockDetails.  For documentation on AddLockDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/identity/20160918/datatypes/AddLockDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'locks': {'module': 'identity', 'class': 'list[AddLockDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'locks': {'module': 'identity', 'class': 'list[AddLockDetails]'}}, output_type={'module': 'identity', 'class': 'TagDefault'})
@cli_util.wrap_exceptions
def create_tag_default(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, tag_definition_id, value, is_required, locks):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['tagDefinitionId'] = tag_definition_id
    _details['value'] = value

    if is_required is not None:
        _details['isRequired'] = is_required

    if locks is not None:
        _details['locks'] = cli_util.parse_json_parameter("locks", locks)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_tag_default(
        create_tag_default_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag_default') and callable(getattr(client, 'get_tag_default')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag_default(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tag_namespace_group.command(name=cli_util.override('iam.create_tag_namespace.command_name', 'create'), help=u"""Creates a new tag namespace in the specified compartment.

You must specify the compartment ID in the request object (remember that the tenancy is simply the root compartment).

You must also specify a *name* for the namespace, which must be unique across all namespaces in your tenancy and cannot be changed. The name can contain any ASCII character except the space (_) or period (.). Names are case insensitive. That means, for example, \"myNamespace\" and \"mynamespace\" are not allowed in the same tenancy. Once you created a namespace, you cannot change the name. If you specify a name that's already in use in the tenancy, a 409 error is returned.

You must also specify a *description* for the namespace. It does not have to be unique, and you can change it with [UpdateTagNamespace]. \n[Command Reference](createTagNamespace)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy containing the tag namespace.""")
@cli_util.option('--name', required=True, help=u"""The name you assign to the tag namespace during creation. It must be unique across all tag namespaces in the tenancy and cannot be changed.""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the tag namespace during creation.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--locks', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Locks associated with this resource.

This option is a JSON list with items of type AddLockDetails.  For documentation on AddLockDetails please see our API reference: https://docs.cloud.oracle.com/api/#/en/identity/20160918/datatypes/AddLockDetails.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'locks': {'module': 'identity', 'class': 'list[AddLockDetails]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'locks': {'module': 'identity', 'class': 'list[AddLockDetails]'}}, output_type={'module': 'identity', 'class': 'TagNamespace'})
@cli_util.wrap_exceptions
def create_tag_namespace(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, name, description, freeform_tags, defined_tags, locks):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['name'] = name
    _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if locks is not None:
        _details['locks'] = cli_util.parse_json_parameter("locks", locks)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_tag_namespace(
        create_tag_namespace_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag_namespace') and callable(getattr(client, 'get_tag_namespace')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag_namespace(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.create_user.command_name', 'create'), help=u"""Creates a new user in your tenancy. For conceptual information about users, your tenancy, and other IAM Service components, see [Overview of IAM].

You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies) reside within the tenancy itself, unlike cloud resources such as compute instances, which typically reside within compartments inside the tenancy. For information about OCIDs, see [Resource Identifiers].

You must also specify a *name* for the user, which must be unique across all users in your tenancy and cannot be changed. Allowed characters: No spaces. Only letters, numerals, hyphens, periods, underscores, +, and @. If you specify a name that's already in use, you'll get a 409 error. This name will be the user's login to the Console. You might want to pick a name that your company's own identity system (e.g., Active Directory, LDAP, etc.) already uses. If you delete a user and then create a new user with the same name, they'll be considered different users because they have different OCIDs.

You must also specify a *description* for the user (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateUser]. You can use the field to provide the user's full name, a description, a nickname, or other information to generally identify the user.

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.

A new user has no permissions until you place the user in one or more groups (see [AddUserToGroup]). If the user needs to access the Console, you need to provide the user a password (see [CreateOrResetUIPassword]). If the user needs to access the Oracle Cloud Infrastructure REST API, you need to upload a public API signing key for that user (see [Required Keys and OCIDs] and also [UploadApiKey]).

**Important:** Make sure to inform the new user which compartment(s) they have access to. \n[Command Reference](createUser)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the tenancy containing the user.""")
@cli_util.option('--name', required=True, help=u"""The name you assign to the user during creation. This is the user's login for the Console. The name must be unique across all users in the tenancy and cannot be changed.""")
@cli_util.option('--description', required=True, help=u"""The description you assign to the user during creation. Does not have to be unique, and it's changeable.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--email', help=u"""The email you assign to the user during creation. The email must be unique across all users in the tenancy.

(For tenancies that support identity domains) You must provide an email for each user.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'User'})
@cli_util.wrap_exceptions
def create_user(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, name, description, email, freeform_tags, defined_tags):

    kwargs = {}

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['name'] = name
    _details['description'] = description

    if email is not None:
        _details['email'] = email

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.create_user(
        create_user_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_user') and callable(getattr(client, 'get_user')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_user(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@domain_group.command(name=cli_util.override('iam.deactivate_domain.command_name', 'deactivate'), help=u"""(For tenancies that support identity domains) Deactivates the specified identity domain. Identity domains must be in an ACTIVE `lifecycleState` and have no active apps present in the domain or underlying Identity Cloud Service stripe. You cannot deactivate the default identity domain.

After you send your request, the `lifecycleDetails` of this identity domain is set to DEACTIVATING. When the operation completes, then the `lifecycleDetails` is set to null and the `lifecycleState` is set to INACTIVE.

To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status. \n[Command Reference](deactivateDomain)""")
@cli_util.option('--domain-id', required=True, help=u"""The OCID of the identity domain.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def deactivate_domain(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, domain_id, if_match):

    if isinstance(domain_id, six.string_types) and len(domain_id.strip()) == 0:
        raise click.UsageError('Parameter --domain-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.deactivate_domain(
        domain_id=domain_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_iam_work_request') and callable(getattr(client, 'get_iam_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_iam_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@api_key_group.command(name=cli_util.override('iam.delete_api_key.command_name', 'delete'), help=u"""Deletes the specified API signing key for the specified user.

Every user has permission to use this operation to delete a key for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to delete a key for any user, including themselves. \n[Command Reference](deleteApiKey)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--fingerprint', required=True, help=u"""The key's fingerprint.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_api_key(ctx, from_json, user_id, fingerprint, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(fingerprint, six.string_types) and len(fingerprint.strip()) == 0:
        raise click.UsageError('Parameter --fingerprint cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_api_key(
        user_id=user_id,
        fingerprint=fingerprint,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auth_token_group.command(name=cli_util.override('iam.delete_auth_token.command_name', 'delete'), help=u"""Deletes the specified auth token for the specified user. \n[Command Reference](deleteAuthToken)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--auth-token-id', required=True, help=u"""The OCID of the auth token.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_auth_token(ctx, from_json, user_id, auth_token_id, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(auth_token_id, six.string_types) and len(auth_token_id.strip()) == 0:
        raise click.UsageError('Parameter --auth-token-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_auth_token(
        user_id=user_id,
        auth_token_id=auth_token_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compartment_group.command(name=cli_util.override('iam.delete_compartment.command_name', 'delete'), help=u"""Deletes the specified compartment. The compartment must be empty. \n[Command Reference](deleteCompartment)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, if_match):

    if isinstance(compartment_id, six.string_types) and len(compartment_id.strip()) == 0:
        raise click.UsageError('Parameter --compartment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_compartment(
        compartment_id=compartment_id,
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


@customer_secret_key_group.command(name=cli_util.override('iam.delete_customer_secret_key.command_name', 'delete'), help=u"""Deletes the specified secret key for the specified user. \n[Command Reference](deleteCustomerSecretKey)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--customer-secret-key-id', required=True, help=u"""The access token of the secret key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_customer_secret_key(ctx, from_json, user_id, customer_secret_key_id, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(customer_secret_key_id, six.string_types) and len(customer_secret_key_id.strip()) == 0:
        raise click.UsageError('Parameter --customer-secret-key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_customer_secret_key(
        user_id=user_id,
        customer_secret_key_id=customer_secret_key_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.delete_db_credential.command_name', 'delete-db-credential'), help=u"""Deletes the specified DB credential for the specified user. \n[Command Reference](deleteDbCredential)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--db-credential-id', required=True, help=u"""The OCID of the DB credential.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_db_credential(ctx, from_json, user_id, db_credential_id, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(db_credential_id, six.string_types) and len(db_credential_id.strip()) == 0:
        raise click.UsageError('Parameter --db-credential-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_db_credential(
        user_id=user_id,
        db_credential_id=db_credential_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@domain_group.command(name=cli_util.override('iam.delete_domain.command_name', 'delete'), help=u"""(For tenancies that support identity domains) Deletes an identity domain. The identity domain must have no active apps present in the underlying IDCS stripe. You must also deactivate the identity domain, rendering the `lifecycleState` of the identity domain INACTIVE. Furthermore, as the authenticated user performing the operation, you cannot be a member of the identity domain you are deleting. Lastly, you cannot delete the default identity domain. A tenancy must always have at least the default identity domain.

To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status. \n[Command Reference](deleteDomain)""")
@cli_util.option('--domain-id', required=True, help=u"""The OCID of the identity domain.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_domain(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, domain_id, if_match):

    if isinstance(domain_id, six.string_types) and len(domain_id.strip()) == 0:
        raise click.UsageError('Parameter --domain-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_domain(
        domain_id=domain_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_iam_work_request') and callable(getattr(client, 'get_iam_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_iam_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@dynamic_group_group.command(name=cli_util.override('iam.delete_dynamic_group.command_name', 'delete'), help=u"""Deletes the specified dynamic group. \n[Command Reference](deleteDynamicGroup)""")
@cli_util.option('--dynamic-group-id', required=True, help=u"""The OCID of the dynamic group.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_dynamic_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dynamic_group_id, if_match):

    if isinstance(dynamic_group_id, six.string_types) and len(dynamic_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dynamic-group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_dynamic_group(
        dynamic_group_id=dynamic_group_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dynamic_group') and callable(getattr(client, 'get_dynamic_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_dynamic_group(dynamic_group_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@group_group.command(name=cli_util.override('iam.delete_group.command_name', 'delete'), help=u"""Deletes the specified group. The group must be empty. \n[Command Reference](deleteGroup)""")
@cli_util.option('--group-id', required=True, help=u"""The OCID of the group.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_group(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, group_id, if_match):

    if isinstance(group_id, six.string_types) and len(group_id.strip()) == 0:
        raise click.UsageError('Parameter --group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_group(
        group_id=group_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_group') and callable(getattr(client, 'get_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_group(group_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@identity_provider_group.command(name=cli_util.override('iam.delete_identity_provider.command_name', 'delete'), help=u"""**Deprecated.** For more information, see [Deprecated IAM Service APIs].

Deletes the specified identity provider. The identity provider must not have any group mappings (see [IdpGroupMapping]). \n[Command Reference](deleteIdentityProvider)""")
@cli_util.option('--identity-provider-id', required=True, help=u"""The OCID of the identity provider.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_identity_provider(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, identity_provider_id, if_match):

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_identity_provider(
        identity_provider_id=identity_provider_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_identity_provider') and callable(getattr(client, 'get_identity_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_identity_provider(identity_provider_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@idp_group_mapping_group.command(name=cli_util.override('iam.delete_idp_group_mapping.command_name', 'delete'), help=u"""**Deprecated.** For more information, see [Deprecated IAM Service APIs].

Deletes the specified group mapping. \n[Command Reference](deleteIdpGroupMapping)""")
@cli_util.option('--identity-provider-id', required=True, help=u"""The OCID of the identity provider.""")
@cli_util.option('--mapping-id', required=True, help=u"""The OCID of the group mapping.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_idp_group_mapping(ctx, from_json, identity_provider_id, mapping_id, if_match):

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    if isinstance(mapping_id, six.string_types) and len(mapping_id.strip()) == 0:
        raise click.UsageError('Parameter --mapping-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_idp_group_mapping(
        identity_provider_id=identity_provider_id,
        mapping_id=mapping_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@mfa_totp_device_group.command(name=cli_util.override('iam.delete_mfa_totp_device.command_name', 'delete'), help=u"""Deletes the specified MFA TOTP device for the specified user. \n[Command Reference](deleteMfaTotpDevice)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--mfa-totp-device-id', required=True, help=u"""The OCID of the MFA TOTP device.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_mfa_totp_device(ctx, from_json, user_id, mfa_totp_device_id, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(mfa_totp_device_id, six.string_types) and len(mfa_totp_device_id.strip()) == 0:
        raise click.UsageError('Parameter --mfa-totp-device-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_mfa_totp_device(
        user_id=user_id,
        mfa_totp_device_id=mfa_totp_device_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@network_sources_group.command(name=cli_util.override('iam.delete_network_source.command_name', 'delete'), help=u"""Deletes the specified network source. \n[Command Reference](deleteNetworkSource)""")
@cli_util.option('--network-source-id', required=True, help=u"""The OCID of the network source.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_network_source(ctx, from_json, network_source_id, if_match):

    if isinstance(network_source_id, six.string_types) and len(network_source_id.strip()) == 0:
        raise click.UsageError('Parameter --network-source-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_network_source(
        network_source_id=network_source_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.delete_o_auth_client_credential.command_name', 'delete-o-auth-client-credential'), help=u"""Delete Oauth token for the user \n[Command Reference](deleteOAuthClientCredential)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--oauth2-client-credential-id', required=True, help=u"""The ID of the Oauth credential.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_o_auth_client_credential(ctx, from_json, user_id, oauth2_client_credential_id, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(oauth2_client_credential_id, six.string_types) and len(oauth2_client_credential_id.strip()) == 0:
        raise click.UsageError('Parameter --oauth2-client-credential-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_o_auth_client_credential(
        user_id=user_id,
        oauth2_client_credential_id=oauth2_client_credential_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@policy_group.command(name=cli_util.override('iam.delete_policy.command_name', 'delete'), help=u"""Deletes the specified policy. The deletion takes effect typically within 10 seconds. \n[Command Reference](deletePolicy)""")
@cli_util.option('--policy-id', required=True, help=u"""The OCID of the policy.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_policy(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, policy_id, if_match):

    if isinstance(policy_id, six.string_types) and len(policy_id.strip()) == 0:
        raise click.UsageError('Parameter --policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_policy(
        policy_id=policy_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_policy') and callable(getattr(client, 'get_policy')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_policy(policy_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@smtp_credential_group.command(name=cli_util.override('iam.delete_smtp_credential.command_name', 'delete'), help=u"""Deletes the specified SMTP credential for the specified user. \n[Command Reference](deleteSmtpCredential)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--smtp-credential-id', required=True, help=u"""The OCID of the SMTP credential.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_smtp_credential(ctx, from_json, user_id, smtp_credential_id, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(smtp_credential_id, six.string_types) and len(smtp_credential_id.strip()) == 0:
        raise click.UsageError('Parameter --smtp-credential-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_smtp_credential(
        user_id=user_id,
        smtp_credential_id=smtp_credential_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@swift_password_group.command(name=cli_util.override('iam.delete_swift_password.command_name', 'delete'), help=u"""**Deprecated. Use [DeleteAuthToken] instead.**

Deletes the specified Swift password for the specified user. \n[Command Reference](deleteSwiftPassword)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--swift-password-id', required=True, help=u"""The OCID of the Swift password.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_swift_password(ctx, from_json, user_id, swift_password_id, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(swift_password_id, six.string_types) and len(swift_password_id.strip()) == 0:
        raise click.UsageError('Parameter --swift-password-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_swift_password(
        user_id=user_id,
        swift_password_id=swift_password_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tag_group.command(name=cli_util.override('iam.delete_tag.command_name', 'delete'), help=u"""Deletes the specified tag definition. This operation triggers a process that removes the tag from all resources in your tenancy.

These things happen immediately:   * If the tag was a cost-tracking tag, it no longer counts against your 10 cost-tracking   tags limit, whether you first disabled it or not.   * If the tag was used with dynamic groups, none of the rules that contain the tag will   be evaluated against the tag.

When you start the delete operation, the state of the tag changes to DELETING and tag removal from resources begins. This can take up to 48 hours depending on the number of resources that were tagged as well as the regions in which those resources reside.

When all tags have been removed, the state changes to DELETED. You cannot restore a deleted tag. Once the deleted tag changes its state to DELETED, you can use the same tag name again.

After you start this operation, you cannot start either the [BulkDeleteTags] or the [CascadeDeleteTagNamespace] operation until this process completes.

To delete a tag, you must first retire it. Use [UpdateTag] to retire a tag. \n[Command Reference](deleteTag)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--tag-name', required=True, help=u"""The name of the tag.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_tag(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_namespace_id, tag_name, if_match, is_lock_override):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    if isinstance(tag_name, six.string_types) and len(tag_name.strip()) == 0:
        raise click.UsageError('Parameter --tag-name cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_tag(
        tag_namespace_id=tag_namespace_id,
        tag_name=tag_name,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tagging_work_request') and callable(getattr(client, 'get_tagging_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tagging_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@tag_default_group.command(name=cli_util.override('iam.delete_tag_default.command_name', 'delete'), help=u"""Deletes the the specified tag default. \n[Command Reference](deleteTagDefault)""")
@cli_util.option('--tag-default-id', required=True, help=u"""The OCID of the tag default.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_tag_default(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_default_id, if_match, is_lock_override):

    if isinstance(tag_default_id, six.string_types) and len(tag_default_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-default-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_tag_default(
        tag_default_id=tag_default_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag_default') and callable(getattr(client, 'get_tag_default')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_tag_default(tag_default_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tag_namespace_group.command(name=cli_util.override('iam.delete_tag_namespace.command_name', 'delete'), help=u"""Deletes the specified tag namespace. Only an empty tag namespace can be deleted with this operation. To use this operation to delete a tag namespace that contains tag definitions, first delete all of its tag definitions.

Use [CascadeDeleteTagNamespace] to delete a tag namespace along with all of the tag definitions contained within that namespace.

Use [DeleteTag] to delete a tag definition. \n[Command Reference](deleteTagNamespace)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_tag_namespace(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_namespace_id, if_match, is_lock_override):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_tag_namespace(
        tag_namespace_id=tag_namespace_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag_namespace') and callable(getattr(client, 'get_tag_namespace')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_tag_namespace(tag_namespace_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.delete_user.command_name', 'delete'), help=u"""Deletes the specified user. The user must not be in any groups. \n[Command Reference](deleteUser)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_user(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, user_id, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.delete_user(
        user_id=user_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_user') and callable(getattr(client, 'get_user')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_user(user_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@domain_group.command(name=cli_util.override('iam.enable_replication_to_region.command_name', 'enable-replication-to-region'), help=u"""(For tenancies that support identity domains) Replicates the identity domain to a new region (provided that the region is the tenancy home region or other region that the tenancy subscribes to). You can only replicate identity domains that are in an ACTIVE `lifecycleState` and not currently updating or already replicating. You also can only trigger the replication of secondary identity domains. The default identity domain is automatically replicated to all regions that the tenancy subscribes to.

After you send the request, the `state` of the identity domain in the replica region is set to ENABLING_REPLICATION. When the operation completes, the `state` is set to REPLICATION_ENABLED.

To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status. \n[Command Reference](enableReplicationToRegion)""")
@cli_util.option('--domain-id', required=True, help=u"""The OCID of the identity domain.""")
@cli_util.option('--replica-region', help=u"""A region to which you want identity domain replication to occur. See [Regions and Availability Domains] for the full list of supported region names.

Example: `us-phoenix-1`""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def enable_replication_to_region(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, domain_id, replica_region, if_match):

    if isinstance(domain_id, six.string_types) and len(domain_id.strip()) == 0:
        raise click.UsageError('Parameter --domain-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if replica_region is not None:
        _details['replicaRegion'] = replica_region

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.enable_replication_to_region(
        domain_id=domain_id,
        enable_replication_to_region_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_iam_work_request') and callable(getattr(client, 'get_iam_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_iam_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@mfa_totp_device_group.command(name=cli_util.override('iam.generate_totp_seed.command_name', 'generate-totp-seed'), help=u"""Generate seed for the MFA TOTP device. \n[Command Reference](generateTotpSeed)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--mfa-totp-device-id', required=True, help=u"""The OCID of the MFA TOTP device.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'MfaTotpDevice'})
@cli_util.wrap_exceptions
def generate_totp_seed(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, user_id, mfa_totp_device_id, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(mfa_totp_device_id, six.string_types) and len(mfa_totp_device_id.strip()) == 0:
        raise click.UsageError('Parameter --mfa-totp-device-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.generate_totp_seed(
        user_id=user_id,
        mfa_totp_device_id=mfa_totp_device_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_mfa_totp_device') and callable(getattr(client, 'get_mfa_totp_device')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_mfa_totp_device(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@authentication_policy_group.command(name=cli_util.override('iam.get_authentication_policy.command_name', 'get'), help=u"""Gets the authentication policy for the given tenancy. You must specify your tenant\u2019s OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). \n[Command Reference](getAuthenticationPolicy)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'AuthenticationPolicy'})
@cli_util.wrap_exceptions
def get_authentication_policy(ctx, from_json, compartment_id):

    if isinstance(compartment_id, six.string_types) and len(compartment_id.strip()) == 0:
        raise click.UsageError('Parameter --compartment-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_authentication_policy(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compartment_group.command(name=cli_util.override('iam.get_compartment.command_name', 'get'), help=u"""Gets the specified compartment's information.

This operation does not return a list of all the resources inside the compartment. There is no single API operation that does that. Compartments can contain multiple types of resources (instances, block storage volumes, etc.). To find out what's in a compartment, you must call the \"List\" operation for each resource type and specify the compartment's OCID as a query parameter in the request. For example, call the [ListInstances] operation in the Cloud Compute Service or the [ListVolumes] operation in Cloud Block Storage. \n[Command Reference](getCompartment)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Compartment'})
@cli_util.wrap_exceptions
def get_compartment(ctx, from_json, compartment_id):

    if isinstance(compartment_id, six.string_types) and len(compartment_id.strip()) == 0:
        raise click.UsageError('Parameter --compartment-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_compartment(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@domain_group.command(name=cli_util.override('iam.get_domain.command_name', 'get'), help=u"""(For tenancies that support identity domains) Gets the specified identity domain's information. \n[Command Reference](getDomain)""")
@cli_util.option('--domain-id', required=True, help=u"""The OCID of the identity domain.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Domain'})
@cli_util.wrap_exceptions
def get_domain(ctx, from_json, domain_id):

    if isinstance(domain_id, six.string_types) and len(domain_id.strip()) == 0:
        raise click.UsageError('Parameter --domain-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_domain(
        domain_id=domain_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@dynamic_group_group.command(name=cli_util.override('iam.get_dynamic_group.command_name', 'get'), help=u"""Gets the specified dynamic group's information. \n[Command Reference](getDynamicGroup)""")
@cli_util.option('--dynamic-group-id', required=True, help=u"""The OCID of the dynamic group.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'DynamicGroup'})
@cli_util.wrap_exceptions
def get_dynamic_group(ctx, from_json, dynamic_group_id):

    if isinstance(dynamic_group_id, six.string_types) and len(dynamic_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dynamic-group-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_dynamic_group(
        dynamic_group_id=dynamic_group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@group_group.command(name=cli_util.override('iam.get_group.command_name', 'get'), help=u"""Gets the specified group's information.

This operation does not return a list of all the users in the group. To do that, use [ListUserGroupMemberships] and provide the group's OCID as a query parameter in the request. \n[Command Reference](getGroup)""")
@cli_util.option('--group-id', required=True, help=u"""The OCID of the group.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Group'})
@cli_util.wrap_exceptions
def get_group(ctx, from_json, group_id):

    if isinstance(group_id, six.string_types) and len(group_id.strip()) == 0:
        raise click.UsageError('Parameter --group-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_group(
        group_id=group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@iam_work_request_group.command(name=cli_util.override('iam.get_iam_work_request.command_name', 'get'), help=u"""Gets the details of a specified IAM work request. The workRequestID is returned in the opc-workrequest-id header for any asynchronous operation in the Identity and Access Management service. \n[Command Reference](getIamWorkRequest)""")
@cli_util.option('--iam-work-request-id', required=True, help=u"""The OCID of the IAM work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'IamWorkRequest'})
@cli_util.wrap_exceptions
def get_iam_work_request(ctx, from_json, iam_work_request_id):

    if isinstance(iam_work_request_id, six.string_types) and len(iam_work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --iam-work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_iam_work_request(
        iam_work_request_id=iam_work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@identity_provider_group.command(name=cli_util.override('iam.get_identity_provider.command_name', 'get'), help=u"""**Deprecated.** For more information, see [Deprecated IAM Service APIs].

Gets the specified identity provider's information. \n[Command Reference](getIdentityProvider)""")
@cli_util.option('--identity-provider-id', required=True, help=u"""The OCID of the identity provider.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'IdentityProvider'})
@cli_util.wrap_exceptions
def get_identity_provider(ctx, from_json, identity_provider_id):

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_identity_provider(
        identity_provider_id=identity_provider_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@idp_group_mapping_group.command(name=cli_util.override('iam.get_idp_group_mapping.command_name', 'get'), help=u"""**Deprecated.** For more information, see [Deprecated IAM Service APIs].

Gets the specified group mapping. \n[Command Reference](getIdpGroupMapping)""")
@cli_util.option('--identity-provider-id', required=True, help=u"""The OCID of the identity provider.""")
@cli_util.option('--mapping-id', required=True, help=u"""The OCID of the group mapping.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'IdpGroupMapping'})
@cli_util.wrap_exceptions
def get_idp_group_mapping(ctx, from_json, identity_provider_id, mapping_id):

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    if isinstance(mapping_id, six.string_types) and len(mapping_id.strip()) == 0:
        raise click.UsageError('Parameter --mapping-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_idp_group_mapping(
        identity_provider_id=identity_provider_id,
        mapping_id=mapping_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@mfa_totp_device_group.command(name=cli_util.override('iam.get_mfa_totp_device.command_name', 'get'), help=u"""Get the specified MFA TOTP device for the specified user. \n[Command Reference](getMfaTotpDevice)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--mfa-totp-device-id', required=True, help=u"""The OCID of the MFA TOTP device.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'MfaTotpDeviceSummary'})
@cli_util.wrap_exceptions
def get_mfa_totp_device(ctx, from_json, user_id, mfa_totp_device_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(mfa_totp_device_id, six.string_types) and len(mfa_totp_device_id.strip()) == 0:
        raise click.UsageError('Parameter --mfa-totp-device-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_mfa_totp_device(
        user_id=user_id,
        mfa_totp_device_id=mfa_totp_device_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@network_sources_group.command(name=cli_util.override('iam.get_network_source.command_name', 'get'), help=u"""Gets the specified network source's information. \n[Command Reference](getNetworkSource)""")
@cli_util.option('--network-source-id', required=True, help=u"""The OCID of the network source.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'NetworkSources'})
@cli_util.wrap_exceptions
def get_network_source(ctx, from_json, network_source_id):

    if isinstance(network_source_id, six.string_types) and len(network_source_id.strip()) == 0:
        raise click.UsageError('Parameter --network-source-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_network_source(
        network_source_id=network_source_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@policy_group.command(name=cli_util.override('iam.get_policy.command_name', 'get'), help=u"""Gets the specified policy's information. \n[Command Reference](getPolicy)""")
@cli_util.option('--policy-id', required=True, help=u"""The OCID of the policy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Policy'})
@cli_util.wrap_exceptions
def get_policy(ctx, from_json, policy_id):

    if isinstance(policy_id, six.string_types) and len(policy_id.strip()) == 0:
        raise click.UsageError('Parameter --policy-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_policy(
        policy_id=policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@standard_tag_namespace_template_group.command(name=cli_util.override('iam.get_standard_tag_template.command_name', 'get-standard-tag-template'), help=u"""Retrieve the standard tag namespace template given the standard tag namespace name. \n[Command Reference](getStandardTagTemplate)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--standard-tag-namespace-name', required=True, help=u"""The name of the standard tag namespace tempate that is requested""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'StandardTagNamespaceTemplate'})
@cli_util.wrap_exceptions
def get_standard_tag_template(ctx, from_json, compartment_id, standard_tag_namespace_name):

    if isinstance(standard_tag_namespace_name, six.string_types) and len(standard_tag_namespace_name.strip()) == 0:
        raise click.UsageError('Parameter --standard-tag-namespace-name cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_standard_tag_template(
        compartment_id=compartment_id,
        standard_tag_namespace_name=standard_tag_namespace_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tag_group.command(name=cli_util.override('iam.get_tag.command_name', 'get'), help=u"""Gets the specified tag's information. \n[Command Reference](getTag)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--tag-name', required=True, help=u"""The name of the tag.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Tag'})
@cli_util.wrap_exceptions
def get_tag(ctx, from_json, tag_namespace_id, tag_name):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    if isinstance(tag_name, six.string_types) and len(tag_name.strip()) == 0:
        raise click.UsageError('Parameter --tag-name cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_tag(
        tag_namespace_id=tag_namespace_id,
        tag_name=tag_name,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tag_default_group.command(name=cli_util.override('iam.get_tag_default.command_name', 'get'), help=u"""Retrieves the specified tag default. \n[Command Reference](getTagDefault)""")
@cli_util.option('--tag-default-id', required=True, help=u"""The OCID of the tag default.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'TagDefault'})
@cli_util.wrap_exceptions
def get_tag_default(ctx, from_json, tag_default_id):

    if isinstance(tag_default_id, six.string_types) and len(tag_default_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-default-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_tag_default(
        tag_default_id=tag_default_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tag_namespace_group.command(name=cli_util.override('iam.get_tag_namespace.command_name', 'get'), help=u"""Gets the specified tag namespace's information. \n[Command Reference](getTagNamespace)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'TagNamespace'})
@cli_util.wrap_exceptions
def get_tag_namespace(ctx, from_json, tag_namespace_id):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_tag_namespace(
        tag_namespace_id=tag_namespace_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tagging_work_request_group.command(name=cli_util.override('iam.get_tagging_work_request.command_name', 'get'), help=u"""Gets details on a specified work request. The workRequestID is returned in the opc-workrequest-id header for any asynchronous operation in tagging service. \n[Command Reference](getTaggingWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'TaggingWorkRequest'})
@cli_util.wrap_exceptions
def get_tagging_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_tagging_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tenancy_group.command(name=cli_util.override('iam.get_tenancy.command_name', 'get'), help=u"""Get the specified tenancy's information. \n[Command Reference](getTenancy)""")
@cli_util.option('--tenancy-id', required=True, help=u"""The OCID of the tenancy.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Tenancy'})
@cli_util.wrap_exceptions
def get_tenancy(ctx, from_json, tenancy_id):

    if isinstance(tenancy_id, six.string_types) and len(tenancy_id.strip()) == 0:
        raise click.UsageError('Parameter --tenancy-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_tenancy(
        tenancy_id=tenancy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.get_user.command_name', 'get'), help=u"""Gets the specified user's information. \n[Command Reference](getUser)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'User'})
@cli_util.wrap_exceptions
def get_user(ctx, from_json, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_user(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group_membership_group.command(name=cli_util.override('iam.get_user_group_membership.command_name', 'get'), help=u"""Gets the specified UserGroupMembership's information. \n[Command Reference](getUserGroupMembership)""")
@cli_util.option('--user-group-membership-id', required=True, help=u"""The OCID of the userGroupMembership.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'UserGroupMembership'})
@cli_util.wrap_exceptions
def get_user_group_membership(ctx, from_json, user_group_membership_id):

    if isinstance(user_group_membership_id, six.string_types) and len(user_group_membership_id.strip()) == 0:
        raise click.UsageError('Parameter --user-group-membership-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_user_group_membership(
        user_group_membership_id=user_group_membership_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ui_password_information_group.command(name=cli_util.override('iam.get_user_ui_password_information.command_name', 'get-user'), help=u"""Gets the specified user's console password information. The returned object contains the user's OCID, but not the password itself. The actual password is returned only when created or reset. \n[Command Reference](getUserUIPasswordInformation)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'UIPasswordInformation'})
@cli_util.wrap_exceptions
def get_user_ui_password_information(ctx, from_json, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_user_ui_password_information(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('iam.get_work_request.command_name', 'get'), help=u"""Gets details on a specified work request. The workRequestID is returned in the opc-workrequest-id header for any asynchronous operation in the compartment service. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tag_group.command(name=cli_util.override('iam.import_standard_tags.command_name', 'import-standard-tags'), help=u"""OCI will release Tag Namespaces that our customers can import. These Tag Namespaces will provide Tags for our customers and Partners to provide consistency and enable data reporting. \n[Command Reference](importStandardTags)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where the bulk create request is submitted and where the tag namespaces will be created.""")
@cli_util.option('--standard-tag-namespace-name', required=True, help=u"""The name of standard tag namespace that will be imported in bulk""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def import_standard_tags(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, standard_tag_namespace_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['standardTagNamespaceName'] = standard_tag_namespace_name

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.import_standard_tags(
        import_standard_tags_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tagging_work_request') and callable(getattr(client, 'get_tagging_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tagging_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@domain_group.command(name=cli_util.override('iam.list_allowed_domain_license_types.command_name', 'list-allowed-domain-license-types'), help=u"""(For tenancies that support identity domains) Lists the license types for identity domains supported by Oracle Cloud Infrastructure. (License types are also referred to as domain types.)

If `currentLicenseTypeName` is provided, then the request returns license types that the identity domain with the specified license type name can change to. Otherwise, the request returns all valid license types currently supported. \n[Command Reference](listAllowedDomainLicenseTypes)""")
@cli_util.option('--current-license-type-name', help=u"""The license type of the identity domain.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[AllowedDomainLicenseTypeSummary]'})
@cli_util.wrap_exceptions
def list_allowed_domain_license_types(ctx, from_json, all_pages, current_license_type_name):

    kwargs = {}
    if current_license_type_name is not None:
        kwargs['current_license_type_name'] = current_license_type_name
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.list_allowed_domain_license_types(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@api_key_group.command(name=cli_util.override('iam.list_api_keys.command_name', 'list'), help=u"""Lists the API signing keys for the specified user. A user can have a maximum of three keys.

Every user has permission to use this API call for *their own user ID*.  An administrator in your organization does not need to write a policy to give users this ability. \n[Command Reference](listApiKeys)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[ApiKey]'})
@cli_util.wrap_exceptions
def list_api_keys(ctx, from_json, all_pages, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.list_api_keys(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auth_token_group.command(name=cli_util.override('iam.list_auth_tokens.command_name', 'list'), help=u"""Lists the auth tokens for the specified user. The returned object contains the token's OCID, but not the token itself. The actual token is returned only upon creation. \n[Command Reference](listAuthTokens)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[AuthToken]'})
@cli_util.wrap_exceptions
def list_auth_tokens(ctx, from_json, all_pages, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.list_auth_tokens(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@availability_domain_group.command(name=cli_util.override('iam.list_availability_domains.command_name', 'list'), help=u"""Lists the availability domains in your tenancy. Specify the OCID of either the tenancy or another of your compartments as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID]. Note that the order of the results returned can change if availability domains are added or removed; therefore, do not create a dependency on the list order. \n[Command Reference](listAvailabilityDomains)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[AvailabilityDomain]'})
@cli_util.wrap_exceptions
def list_availability_domains(ctx, from_json, all_pages, compartment_id):

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.list_availability_domains(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bulk_action_resource_type_collection_group.command(name=cli_util.override('iam.list_bulk_action_resource_types.command_name', 'list-bulk-action-resource-types'), help=u"""Lists the resource-types supported by compartment bulk actions. Use this API to help you provide the correct resource-type information to the [BulkDeleteResources] and [BulkMoveResources] operations. The returned list of resource-types provides the appropriate resource-type names to use with the bulk action operations along with the type of identifying information you'll need to provide for each resource-type. Most resource-types just require an [OCID] to identify a specific resource, but some resource-types, such as buckets, require you to provide other identifying information. \n[Command Reference](listBulkActionResourceTypes)""")
@cli_util.option('--bulk-action-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["BULK_MOVE_RESOURCES", "BULK_DELETE_RESOURCES"]), help=u"""The type of bulk action.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'BulkActionResourceTypeCollection'})
@cli_util.wrap_exceptions
def list_bulk_action_resource_types(ctx, from_json, all_pages, page_size, bulk_action_type, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_bulk_action_resource_types,
            bulk_action_type=bulk_action_type,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_bulk_action_resource_types,
            limit,
            page_size,
            bulk_action_type=bulk_action_type,
            **kwargs
        )
    else:
        result = client.list_bulk_action_resource_types(
            bulk_action_type=bulk_action_type,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@bulk_edit_tags_resource_type_collection_group.command(name=cli_util.override('iam.list_bulk_edit_tags_resource_types.command_name', 'list-bulk-edit-tags-resource-types'), help=u"""Lists the resource types that support bulk tag editing. \n[Command Reference](listBulkEditTagsResourceTypes)""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'BulkEditTagsResourceTypeCollection'})
@cli_util.wrap_exceptions
def list_bulk_edit_tags_resource_types(ctx, from_json, all_pages, page_size, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_bulk_edit_tags_resource_types,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_bulk_edit_tags_resource_types,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_bulk_edit_tags_resource_types(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@compartment_group.command(name=cli_util.override('iam.list_compartments.command_name', 'list'), help=u"""Lists the compartments in a specified compartment. The members of the list returned depends on the values set for several parameters.

With the exception of the tenancy (root compartment), the ListCompartments operation returns only the first-level child compartments in the parent compartment specified in `compartmentId`. The list does not include any subcompartments of the child compartments (grandchildren).

The parameter `accessLevel` specifies whether to return only those compartments for which the requestor has INSPECT permissions on at least one resource directly or indirectly (the resource can be in a subcompartment).

The parameter `compartmentIdInSubtree` applies only when you perform ListCompartments on the tenancy (root compartment). When set to true, the entire hierarchy of compartments can be returned. To get a full list of all compartments and subcompartments in the tenancy (root compartment), set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ANY.

See [Where to Get the Tenancy's OCID and User's OCID]. \n[Command Reference](listCompartments)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--access-level', type=custom_types.CliCaseInsensitiveChoice(["ANY", "ACCESSIBLE"]), help=u"""Valid values are `ANY` and `ACCESSIBLE`. Default is `ANY`. Setting this to `ACCESSIBLE` returns only those compartments for which the user has INSPECT permissions directly or indirectly (permissions can be on a resource in a subcompartment). For the compartments on which the user indirectly has INSPECT permissions, a restricted set of fields is returned.

When set to `ANY` permissions are not checked.""")
@cli_util.option('--compartment-id-in-subtree', type=click.BOOL, help=u"""Default is false. Can only be set to true when performing ListCompartments on the tenancy (root compartment). When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the the setting of `accessLevel`.""")
@cli_util.option('--name', help=u"""A filter to only return resources that match the given name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[Compartment]'})
@cli_util.wrap_exceptions
def list_compartments(ctx, from_json, all_pages, page_size, compartment_id, page, limit, access_level, compartment_id_in_subtree, name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if access_level is not None:
        kwargs['access_level'] = access_level
    if compartment_id_in_subtree is not None:
        kwargs['compartment_id_in_subtree'] = compartment_id_in_subtree
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_compartments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_compartments,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_compartments(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@tag_group.command(name=cli_util.override('iam.list_cost_tracking_tags.command_name', 'list-cost-tracking'), help=u"""Lists all the tags enabled for cost-tracking in the specified tenancy. For information about cost-tracking tags, see [Using Cost-tracking Tags]. \n[Command Reference](listCostTrackingTags)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[Tag]'})
@cli_util.wrap_exceptions
def list_cost_tracking_tags(ctx, from_json, all_pages, page_size, compartment_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_cost_tracking_tags,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_cost_tracking_tags,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_cost_tracking_tags(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@customer_secret_key_group.command(name=cli_util.override('iam.list_customer_secret_keys.command_name', 'list'), help=u"""Lists the secret keys for the specified user. The returned object contains the secret key's OCID, but not the secret key itself. The actual secret key is returned only upon creation. \n[Command Reference](listCustomerSecretKeys)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[CustomerSecretKeySummary]'})
@cli_util.wrap_exceptions
def list_customer_secret_keys(ctx, from_json, all_pages, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.list_customer_secret_keys(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.list_db_credentials.command_name', 'list-db-credentials'), help=u"""Lists the DB credentials for the specified user. The returned object contains the credential's OCID \n[Command Reference](listDbCredentials)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--name', help=u"""A filter to only return resources that match the given name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[DbCredentialSummary]'})
@cli_util.wrap_exceptions
def list_db_credentials(ctx, from_json, all_pages, page_size, user_id, page, limit, name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_db_credentials,
            user_id=user_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_db_credentials,
            limit,
            page_size,
            user_id=user_id,
            **kwargs
        )
    else:
        result = client.list_db_credentials(
            user_id=user_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@domain_group.command(name=cli_util.override('iam.list_domains.command_name', 'list'), help=u"""(For tenancies that support identity domains) Lists all identity domains within a tenancy. \n[Command Reference](listDomains)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--display-name', help=u"""The mutable display name of the identity domain.""")
@cli_util.option('--url', help=u"""The region-agnostic identity domain URL.""")
@cli_util.option('--home-region-url', help=u"""The region-specific identity domain URL.""")
@cli_util.option('--type', help=u"""The identity domain type.""")
@cli_util.option('--license-type', help=u"""The license type of the identity domain.""")
@cli_util.option('--is-hidden-on-login', type=click.BOOL, help=u"""Indicates whether or not the identity domain is visible at the sign-in screen.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--name', help=u"""A filter to only return resources that match the given name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "INACTIVE"]), help=u"""A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[DomainSummary]'})
@cli_util.wrap_exceptions
def list_domains(ctx, from_json, all_pages, page_size, compartment_id, display_name, url, home_region_url, type, license_type, is_hidden_on_login, page, limit, name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if url is not None:
        kwargs['url'] = url
    if home_region_url is not None:
        kwargs['home_region_url'] = home_region_url
    if type is not None:
        kwargs['type'] = type
    if license_type is not None:
        kwargs['license_type'] = license_type
    if is_hidden_on_login is not None:
        kwargs['is_hidden_on_login'] = is_hidden_on_login
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_domains,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_domains,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_domains(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@dynamic_group_group.command(name=cli_util.override('iam.list_dynamic_groups.command_name', 'list'), help=u"""Lists the dynamic groups in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID]. \n[Command Reference](listDynamicGroups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--name', help=u"""A filter to only return resources that match the given name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[DynamicGroup]'})
@cli_util.wrap_exceptions
def list_dynamic_groups(ctx, from_json, all_pages, page_size, compartment_id, page, limit, name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_dynamic_groups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_dynamic_groups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_dynamic_groups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@fault_domain_group.command(name=cli_util.override('iam.list_fault_domains.command_name', 'list'), help=u"""Lists the Fault Domains in your tenancy. Specify the OCID of either the tenancy or another of your compartments as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID]. \n[Command Reference](listFaultDomains)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--availability-domain', required=True, help=u"""The name of the availabilityDomain.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[FaultDomain]'})
@cli_util.wrap_exceptions
def list_fault_domains(ctx, from_json, all_pages, compartment_id, availability_domain):

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.list_fault_domains(
        compartment_id=compartment_id,
        availability_domain=availability_domain,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@group_group.command(name=cli_util.override('iam.list_groups.command_name', 'list'), help=u"""Lists the groups in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID]. \n[Command Reference](listGroups)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--name', help=u"""A filter to only return resources that match the given name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[Group]'})
@cli_util.wrap_exceptions
def list_groups(ctx, from_json, all_pages, page_size, compartment_id, page, limit, name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_groups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_groups,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_groups(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@iam_work_request_group.command(name=cli_util.override('iam.list_iam_work_request_errors.command_name', 'list-iam-work-request-errors'), help=u"""Gets error details for a specified IAM work request. The workRequestID is returned in the opc-workrequest-id header for any asynchronous operation in the Identity and Access Management service. \n[Command Reference](listIamWorkRequestErrors)""")
@cli_util.option('--iam-work-request-id', required=True, help=u"""The OCID of the IAM work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[IamWorkRequestErrorSummary]'})
@cli_util.wrap_exceptions
def list_iam_work_request_errors(ctx, from_json, all_pages, page_size, iam_work_request_id, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(iam_work_request_id, six.string_types) and len(iam_work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --iam-work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_iam_work_request_errors,
            iam_work_request_id=iam_work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_iam_work_request_errors,
            limit,
            page_size,
            iam_work_request_id=iam_work_request_id,
            **kwargs
        )
    else:
        result = client.list_iam_work_request_errors(
            iam_work_request_id=iam_work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@iam_work_request_log_group.command(name=cli_util.override('iam.list_iam_work_request_logs.command_name', 'list'), help=u"""Gets logs for a specified IAM work request. The workRequestID is returned in the opc-workrequest-id header for any asynchronous operation in the Identity and Access Management service. \n[Command Reference](listIamWorkRequestLogs)""")
@cli_util.option('--iam-work-request-id', required=True, help=u"""The OCID of the IAM work request.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[IamWorkRequestLogSummary]'})
@cli_util.wrap_exceptions
def list_iam_work_request_logs(ctx, from_json, all_pages, page_size, iam_work_request_id, limit, page, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(iam_work_request_id, six.string_types) and len(iam_work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --iam-work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_iam_work_request_logs,
            iam_work_request_id=iam_work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_iam_work_request_logs,
            limit,
            page_size,
            iam_work_request_id=iam_work_request_id,
            **kwargs
        )
    else:
        result = client.list_iam_work_request_logs(
            iam_work_request_id=iam_work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@iam_work_request_group.command(name=cli_util.override('iam.list_iam_work_requests.command_name', 'list'), help=u"""Lists the IAM work requests in compartment. The workRequestID is returned in the opc-workrequest-id header for any asynchronous operation in the Identity and Access Management service. \n[Command Reference](listIamWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--resource-identifier', help=u"""The identifier of the resource the work request affects.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[IamWorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_iam_work_requests(ctx, from_json, all_pages, page_size, compartment_id, page, limit, resource_identifier):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if resource_identifier is not None:
        kwargs['resource_identifier'] = resource_identifier
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_iam_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_iam_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_iam_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@identity_provider_group_group.command(name=cli_util.override('iam.list_identity_provider_groups.command_name', 'list'), help=u"""**Deprecated.** For more information, see [Deprecated IAM Service APIs].

Lists the identity provider groups. \n[Command Reference](listIdentityProviderGroups)""")
@cli_util.option('--identity-provider-id', required=True, help=u"""The OCID of the identity provider.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--name', help=u"""A filter to only return resources that match the given name exactly.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[IdentityProviderGroupSummary]'})
@cli_util.wrap_exceptions
def list_identity_provider_groups(ctx, from_json, all_pages, page_size, identity_provider_id, page, limit, name, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_identity_provider_groups,
            identity_provider_id=identity_provider_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_identity_provider_groups,
            limit,
            page_size,
            identity_provider_id=identity_provider_id,
            **kwargs
        )
    else:
        result = client.list_identity_provider_groups(
            identity_provider_id=identity_provider_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@identity_provider_group.command(name=cli_util.override('iam.list_identity_providers.command_name', 'list'), help=u"""**Deprecated.** For more information, see [Deprecated IAM Service APIs].

Lists all the identity providers in your tenancy. You must specify the identity provider type (e.g., `SAML2` for identity providers using the SAML2.0 protocol). You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID]. \n[Command Reference](listIdentityProviders)""")
@cli_util.option('--protocol', required=True, help=u"""The protocol used for federation. Allowed values are: SAML2""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--name', help=u"""A filter to only return resources that match the given name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[IdentityProvider]'})
@cli_util.wrap_exceptions
def list_identity_providers(ctx, from_json, all_pages, page_size, protocol, compartment_id, page, limit, name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_identity_providers,
            protocol=protocol,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_identity_providers,
            limit,
            page_size,
            protocol=protocol,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_identity_providers(
            protocol=protocol,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@idp_group_mapping_group.command(name=cli_util.override('iam.list_idp_group_mappings.command_name', 'list'), help=u"""**Deprecated.** For more information, see [Deprecated IAM Service APIs].

Lists the group mappings for the specified identity provider. \n[Command Reference](listIdpGroupMappings)""")
@cli_util.option('--identity-provider-id', required=True, help=u"""The OCID of the identity provider.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[IdpGroupMapping]'})
@cli_util.wrap_exceptions
def list_idp_group_mappings(ctx, from_json, all_pages, page_size, identity_provider_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_idp_group_mappings,
            identity_provider_id=identity_provider_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_idp_group_mappings,
            limit,
            page_size,
            identity_provider_id=identity_provider_id,
            **kwargs
        )
    else:
        result = client.list_idp_group_mappings(
            identity_provider_id=identity_provider_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@mfa_totp_device_group.command(name=cli_util.override('iam.list_mfa_totp_devices.command_name', 'list'), help=u"""Lists the MFA TOTP devices for the specified user. The returned object contains the device's OCID, but not the seed. The seed is returned only upon creation or when the IAM service regenerates the MFA seed for the device. \n[Command Reference](listMfaTotpDevices)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[MfaTotpDeviceSummary]'})
@cli_util.wrap_exceptions
def list_mfa_totp_devices(ctx, from_json, all_pages, page_size, user_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_mfa_totp_devices,
            user_id=user_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_mfa_totp_devices,
            limit,
            page_size,
            user_id=user_id,
            **kwargs
        )
    else:
        result = client.list_mfa_totp_devices(
            user_id=user_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@network_sources_group.command(name=cli_util.override('iam.list_network_sources.command_name', 'list'), help=u"""Lists the network sources in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID]. \n[Command Reference](listNetworkSources)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--name', help=u"""A filter to only return resources that match the given name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[NetworkSourcesSummary]'})
@cli_util.wrap_exceptions
def list_network_sources(ctx, from_json, all_pages, page_size, compartment_id, page, limit, name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_network_sources,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_network_sources,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_network_sources(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.list_o_auth_client_credentials.command_name', 'list-o-auth-client-credentials'), help=u"""List of Oauth tokens for the user \n[Command Reference](listOAuthClientCredentials)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[OAuth2ClientCredentialSummary]'})
@cli_util.wrap_exceptions
def list_o_auth_client_credentials(ctx, from_json, all_pages, page_size, user_id, page, limit, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_o_auth_client_credentials,
            user_id=user_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_o_auth_client_credentials,
            limit,
            page_size,
            user_id=user_id,
            **kwargs
        )
    else:
        result = client.list_o_auth_client_credentials(
            user_id=user_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@policy_group.command(name=cli_util.override('iam.list_policies.command_name', 'list'), help=u"""Lists the policies in the specified compartment (either the tenancy or another of your compartments). See [Where to Get the Tenancy's OCID and User's OCID].

To determine which policies apply to a particular group or compartment, you must view the individual statements inside all your policies. There isn't a way to automatically obtain that information via the API. \n[Command Reference](listPolicies)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--name', help=u"""A filter to only return resources that match the given name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[Policy]'})
@cli_util.wrap_exceptions
def list_policies(ctx, from_json, all_pages, page_size, compartment_id, page, limit, name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_policies,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_policies,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_policies(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@region_subscription_group.command(name=cli_util.override('iam.list_region_subscriptions.command_name', 'list'), help=u"""Lists the region subscriptions for the specified tenancy. \n[Command Reference](listRegionSubscriptions)""")
@cli_util.option('--tenancy-id', required=True, help=u"""The OCID of the tenancy.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[RegionSubscription]'})
@cli_util.wrap_exceptions
def list_region_subscriptions(ctx, from_json, all_pages, tenancy_id):

    if isinstance(tenancy_id, six.string_types) and len(tenancy_id.strip()) == 0:
        raise click.UsageError('Parameter --tenancy-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.list_region_subscriptions(
        tenancy_id=tenancy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@region_group.command(name=cli_util.override('iam.list_regions.command_name', 'list'), help=u"""Lists all the regions offered by Oracle Cloud Infrastructure. \n[Command Reference](listRegions)""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[Region]'})
@cli_util.wrap_exceptions
def list_regions(ctx, from_json, all_pages, ):

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.list_regions(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@smtp_credential_group.command(name=cli_util.override('iam.list_smtp_credentials.command_name', 'list'), help=u"""Lists the SMTP credentials for the specified user. The returned object contains the credential's OCID, the SMTP user name but not the SMTP password. The SMTP password is returned only upon creation. \n[Command Reference](listSmtpCredentials)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[SmtpCredentialSummary]'})
@cli_util.wrap_exceptions
def list_smtp_credentials(ctx, from_json, all_pages, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.list_smtp_credentials(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@standard_tag_namespace_template_group.command(name=cli_util.override('iam.list_standard_tag_namespaces.command_name', 'list-standard-tag-namespaces'), help=u"""Lists available standard tag namespaces that users can create. \n[Command Reference](listStandardTagNamespaces)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[StandardTagNamespaceTemplateSummary]'})
@cli_util.wrap_exceptions
def list_standard_tag_namespaces(ctx, from_json, all_pages, page_size, compartment_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_standard_tag_namespaces,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_standard_tag_namespaces,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_standard_tag_namespaces(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@swift_password_group.command(name=cli_util.override('iam.list_swift_passwords.command_name', 'list'), help=u"""**Deprecated. Use [ListAuthTokens] instead.**

Lists the Swift passwords for the specified user. The returned object contains the password's OCID, but not the password itself. The actual password is returned only upon creation. \n[Command Reference](listSwiftPasswords)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[SwiftPassword]'})
@cli_util.wrap_exceptions
def list_swift_passwords(ctx, from_json, all_pages, user_id):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.list_swift_passwords(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tag_default_group.command(name=cli_util.override('iam.list_tag_defaults.command_name', 'list'), help=u"""Lists the tag defaults for tag definitions in the specified compartment. \n[Command Reference](listTagDefaults)""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--id', help=u"""A filter to only return resources that match the specified OCID exactly.""")
@cli_util.option('--compartment-id', help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--tag-definition-id', help=u"""The OCID of the tag definition.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[TagDefaultSummary]'})
@cli_util.wrap_exceptions
def list_tag_defaults(ctx, from_json, all_pages, page_size, page, limit, id, compartment_id, tag_definition_id, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if id is not None:
        kwargs['id'] = id
    if compartment_id is not None:
        kwargs['compartment_id'] = compartment_id
    if tag_definition_id is not None:
        kwargs['tag_definition_id'] = tag_definition_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_tag_defaults,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_tag_defaults,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_tag_defaults(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@tag_namespace_group.command(name=cli_util.override('iam.list_tag_namespaces.command_name', 'list'), help=u"""Lists the tag namespaces in the specified compartment. \n[Command Reference](listTagNamespaces)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--include-subcompartments', type=click.BOOL, help=u"""An optional boolean parameter indicating whether to retrieve all tag namespaces in subcompartments. If this parameter is not specified, only the tag namespaces defined in the specified compartment are retrieved.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETING", "DELETED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[TagNamespaceSummary]'})
@cli_util.wrap_exceptions
def list_tag_namespaces(ctx, from_json, all_pages, page_size, compartment_id, page, limit, include_subcompartments, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if include_subcompartments is not None:
        kwargs['include_subcompartments'] = include_subcompartments
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_tag_namespaces,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_tag_namespaces,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_tag_namespaces(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@tagging_work_request_error_group.command(name=cli_util.override('iam.list_tagging_work_request_errors.command_name', 'list'), help=u"""Gets the errors for a work request. \n[Command Reference](listTaggingWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[TaggingWorkRequestErrorSummary]'})
@cli_util.wrap_exceptions
def list_tagging_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_tagging_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_tagging_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_tagging_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@tagging_work_request_log_group.command(name=cli_util.override('iam.list_tagging_work_request_logs.command_name', 'list'), help=u"""Gets the logs for a work request. \n[Command Reference](listTaggingWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the work request.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[TaggingWorkRequestLogSummary]'})
@cli_util.wrap_exceptions
def list_tagging_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_tagging_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_tagging_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_tagging_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@tagging_work_request_group.command(name=cli_util.override('iam.list_tagging_work_requests.command_name', 'list'), help=u"""Lists the tagging work requests in compartment. \n[Command Reference](listTaggingWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--resource-identifier', help=u"""The identifier of the resource the work request affects.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[TaggingWorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_tagging_work_requests(ctx, from_json, all_pages, page_size, compartment_id, page, limit, resource_identifier):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if resource_identifier is not None:
        kwargs['resource_identifier'] = resource_identifier
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_tagging_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_tagging_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_tagging_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@tag_group.command(name=cli_util.override('iam.list_tags.command_name', 'list'), help=u"""Lists the tag definitions in the specified tag namespace. \n[Command Reference](listTags)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETING", "DELETED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[TagSummary]'})
@cli_util.wrap_exceptions
def list_tags(ctx, from_json, all_pages, page_size, tag_namespace_id, page, limit, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_tags,
            tag_namespace_id=tag_namespace_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_tags,
            limit,
            page_size,
            tag_namespace_id=tag_namespace_id,
            **kwargs
        )
    else:
        result = client.list_tags(
            tag_namespace_id=tag_namespace_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@user_group_membership_group.command(name=cli_util.override('iam.list_user_group_memberships.command_name', 'list'), help=u"""Lists the `UserGroupMembership` objects in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (see [Where to Get the Tenancy's OCID and User's OCID]). You must also then filter the list in one of these ways:

- You can limit the results to just the memberships for a given user by specifying a `userId`. - Similarly, you can limit the results to just the memberships for a given group by specifying a `groupId`. - You can set both the `userId` and `groupId` to determine if the specified user is in the specified group. If the answer is no, the response is an empty list. - Although`userId` and `groupId` are not individually required, you must set one of them. \n[Command Reference](listUserGroupMemberships)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--user-id', help=u"""The OCID of the user.""")
@cli_util.option('--group-id', help=u"""The OCID of the group.""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[UserGroupMembership]'})
@cli_util.wrap_exceptions
def list_user_group_memberships(ctx, from_json, all_pages, page_size, compartment_id, user_id, group_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if user_id is not None:
        kwargs['user_id'] = user_id
    if group_id is not None:
        kwargs['group_id'] = group_id
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_user_group_memberships,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_user_group_memberships,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_user_group_memberships(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.list_users.command_name', 'list'), help=u"""Lists the users in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID]. \n[Command Reference](listUsers)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--identity-provider-id', help=u"""The id of the identity provider.""")
@cli_util.option('--external-identifier', help=u"""The id of a user in the identity provider.""")
@cli_util.option('--name', help=u"""A filter to only return resources that match the given name exactly.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "NAME"]), help=u"""The field to sort by. You can provide one sort order (`sortOrder`). Default order for TIMECREATED is descending. Default order for NAME is ascending. The NAME sort order is case sensitive.

**Note:** In general, some \"List\" operations (for example, `ListInstances`) let you optionally filter by Availability Domain if the scope of the resource type is within a single Availability Domain. If you call one of these \"List\" operations without specifying an Availability Domain, the resources are grouped by Availability Domain, then sorted.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order is case sensitive.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), help=u"""A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[User]'})
@cli_util.wrap_exceptions
def list_users(ctx, from_json, all_pages, page_size, compartment_id, page, limit, identity_provider_id, external_identifier, name, sort_by, sort_order, lifecycle_state):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if identity_provider_id is not None:
        kwargs['identity_provider_id'] = identity_provider_id
    if external_identifier is not None:
        kwargs['external_identifier'] = external_identifier
    if name is not None:
        kwargs['name'] = name
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    client = cli_util.build_client('identity', 'identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_users,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_users,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_users(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('iam.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment (remember that the tenancy is simply the root compartment).""")
@cli_util.option('--page', help=u"""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in a paginated \"List\" call.""")
@cli_util.option('--resource-identifier', help=u"""The identifier of the resource the work request affects.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, page, limit, resource_identifier):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if resource_identifier is not None:
        kwargs['resource_identifier'] = resource_identifier
    client = cli_util.build_client('identity', 'identity', ctx)
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


@compartment_group.command(name=cli_util.override('iam.move_compartment.command_name', 'move'), help=u"""Move the compartment to a different parent compartment in the same tenancy. When you move a compartment, all its contents (subcompartments and resources) are moved with it. Note that the `CompartmentId` that you specify in the path is the compartment that you want to move.

**IMPORTANT**: After you move a compartment to a new parent compartment, the access policies of the new parent take effect and the policies of the previous parent no longer apply. Ensure that you are aware of the implications for the compartment contents before you move it. For more information, see [Moving a Compartment]. \n[Command Reference](moveCompartment)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--target-compartment-id', required=True, help=u"""The [OCID] of the destination compartment into which to move the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def move_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, target_compartment_id, if_match):

    if isinstance(compartment_id, six.string_types) and len(compartment_id.strip()) == 0:
        raise click.UsageError('Parameter --compartment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['targetCompartmentId'] = target_compartment_id

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.move_compartment(
        compartment_id=compartment_id,
        move_compartment_details=_details,
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


@compartment_group.command(name=cli_util.override('iam.recover_compartment.command_name', 'recover'), help=u"""Recover the compartment from DELETED state to ACTIVE state. \n[Command Reference](recoverCompartment)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Compartment'})
@cli_util.wrap_exceptions
def recover_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, if_match):

    if isinstance(compartment_id, six.string_types) and len(compartment_id.strip()) == 0:
        raise click.UsageError('Parameter --compartment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.recover_compartment(
        compartment_id=compartment_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_compartment') and callable(getattr(client, 'get_compartment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_compartment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tag_default_group.command(name=cli_util.override('iam.remove_tag_default_lock.command_name', 'remove'), help=u"""Remove a resource lock from a tag default. \n[Command Reference](removeTagDefaultLock)""")
@cli_util.option('--tag-default-id', required=True, help=u"""The OCID of the tag default.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["FULL", "DELETE"]), help=u"""Type of the lock.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'TagDefault'})
@cli_util.wrap_exceptions
def remove_tag_default_lock(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_default_id, type, if_match):

    if isinstance(tag_default_id, six.string_types) and len(tag_default_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-default-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.remove_tag_default_lock(
        tag_default_id=tag_default_id,
        remove_lock_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag_default') and callable(getattr(client, 'get_tag_default')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag_default(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tag_namespace_group.command(name=cli_util.override('iam.remove_tag_namespace_lock.command_name', 'remove'), help=u"""Remove a resource lock from a tag namespace. \n[Command Reference](removeTagNamespaceLock)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--type', required=True, type=custom_types.CliCaseInsensitiveChoice(["FULL", "DELETE"]), help=u"""Type of the lock.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'TagNamespace'})
@cli_util.wrap_exceptions
def remove_tag_namespace_lock(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_namespace_id, type, if_match):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['type'] = type

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.remove_tag_namespace_lock(
        tag_namespace_id=tag_namespace_id,
        remove_lock_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag_namespace') and callable(getattr(client, 'get_tag_namespace')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag_namespace(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@user_group_membership_group.command(name=cli_util.override('iam.remove_user_from_group.command_name', 'remove'), help=u"""Removes a user from a group by deleting the corresponding `UserGroupMembership`. \n[Command Reference](removeUserFromGroup)""")
@cli_util.option('--user-group-membership-id', required=True, help=u"""The OCID of the userGroupMembership.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def remove_user_from_group(ctx, from_json, user_group_membership_id, if_match):

    if isinstance(user_group_membership_id, six.string_types) and len(user_group_membership_id.strip()) == 0:
        raise click.UsageError('Parameter --user-group-membership-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.remove_user_from_group(
        user_group_membership_id=user_group_membership_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@scim_client_credentials_group.command(name=cli_util.override('iam.reset_idp_scim_client.command_name', 'reset-idp-scim-client'), help=u"""Resets the OAuth2 client credentials for the SCIM client associated with this identity provider. \n[Command Reference](resetIdpScimClient)""")
@cli_util.option('--identity-provider-id', required=True, help=u"""The OCID of the identity provider.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'ScimClientCredentials'})
@cli_util.wrap_exceptions
def reset_idp_scim_client(ctx, from_json, identity_provider_id):

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.reset_idp_scim_client(
        identity_provider_id=identity_provider_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@auth_token_group.command(name=cli_util.override('iam.update_auth_token.command_name', 'update'), help=u"""Updates the specified auth token's description. \n[Command Reference](updateAuthToken)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--auth-token-id', required=True, help=u"""The OCID of the auth token.""")
@cli_util.option('--description', help=u"""The description you assign to the auth token. Does not have to be unique, and it's changeable.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'AuthToken'})
@cli_util.wrap_exceptions
def update_auth_token(ctx, from_json, user_id, auth_token_id, description, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(auth_token_id, six.string_types) and len(auth_token_id.strip()) == 0:
        raise click.UsageError('Parameter --auth-token-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if description is not None:
        _details['description'] = description

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_auth_token(
        user_id=user_id,
        auth_token_id=auth_token_id,
        update_auth_token_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@authentication_policy_group.command(name=cli_util.override('iam.update_authentication_policy.command_name', 'update'), help=u"""Updates authentication policy for the specified tenancy. \n[Command Reference](updateAuthenticationPolicy)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--password-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--network-policy', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'password-policy': {'module': 'identity', 'class': 'PasswordPolicy'}, 'network-policy': {'module': 'identity', 'class': 'NetworkPolicy'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'password-policy': {'module': 'identity', 'class': 'PasswordPolicy'}, 'network-policy': {'module': 'identity', 'class': 'NetworkPolicy'}}, output_type={'module': 'identity', 'class': 'AuthenticationPolicy'})
@cli_util.wrap_exceptions
def update_authentication_policy(ctx, from_json, force, compartment_id, password_policy, network_policy, if_match):

    if isinstance(compartment_id, six.string_types) and len(compartment_id.strip()) == 0:
        raise click.UsageError('Parameter --compartment-id cannot be whitespace or empty string')
    if not force:
        if password_policy or network_policy:
            if not click.confirm("WARNING: Updates to password-policy and network-policy will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if password_policy is not None:
        _details['passwordPolicy'] = cli_util.parse_json_parameter("password_policy", password_policy)

    if network_policy is not None:
        _details['networkPolicy'] = cli_util.parse_json_parameter("network_policy", network_policy)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_authentication_policy(
        compartment_id=compartment_id,
        update_authentication_policy_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compartment_group.command(name=cli_util.override('iam.update_compartment.command_name', 'update'), help=u"""Updates the specified compartment's description or name. You can't update the root compartment. \n[Command Reference](updateCompartment)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment.""")
@cli_util.option('--description', help=u"""The description you assign to the compartment. Does not have to be unique, and it's changeable.""")
@cli_util.option('--name', help=u"""The new name you assign to the compartment. The name must be unique across all compartments in the parent compartment. Avoid entering confidential information.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'Compartment'})
@cli_util.wrap_exceptions
def update_compartment(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, description, name, freeform_tags, defined_tags, if_match):

    if isinstance(compartment_id, six.string_types) and len(compartment_id.strip()) == 0:
        raise click.UsageError('Parameter --compartment-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if description is not None:
        _details['description'] = description

    if name is not None:
        _details['name'] = name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_compartment(
        compartment_id=compartment_id,
        update_compartment_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_compartment') and callable(getattr(client, 'get_compartment')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_compartment(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@customer_secret_key_group.command(name=cli_util.override('iam.update_customer_secret_key.command_name', 'update'), help=u"""Updates the specified secret key's description. \n[Command Reference](updateCustomerSecretKey)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--customer-secret-key-id', required=True, help=u"""The access token of the secret key.""")
@cli_util.option('--display-name', help=u"""The description you assign to the secret key. Does not have to be unique, and it's changeable.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'CustomerSecretKeySummary'})
@cli_util.wrap_exceptions
def update_customer_secret_key(ctx, from_json, user_id, customer_secret_key_id, display_name, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(customer_secret_key_id, six.string_types) and len(customer_secret_key_id.strip()) == 0:
        raise click.UsageError('Parameter --customer-secret-key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_customer_secret_key(
        user_id=user_id,
        customer_secret_key_id=customer_secret_key_id,
        update_customer_secret_key_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@domain_group.command(name=cli_util.override('iam.update_domain.command_name', 'update'), help=u"""(For tenancies that support identity domains) Updates identity domain information and the associated Identity Cloud Service (IDCS) stripe.

To track the progress of the request, submitting an HTTP GET on the /iamWorkRequests/{iamWorkRequestsId} endpoint retrieves the operation's status. \n[Command Reference](updateDomain)""")
@cli_util.option('--domain-id', required=True, help=u"""The OCID of the identity domain.""")
@cli_util.option('--description', help=u"""The identity domain description. You can have an empty description.""")
@cli_util.option('--display-name', help=u"""The mutable display name of the identity domain.""")
@cli_util.option('--is-hidden-on-login', type=click.BOOL, help=u"""Indicates whether the identity domain is hidden on the sign-in screen or not.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_domain(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, domain_id, description, display_name, is_hidden_on_login, freeform_tags, defined_tags, if_match):

    if isinstance(domain_id, six.string_types) and len(domain_id.strip()) == 0:
        raise click.UsageError('Parameter --domain-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if is_hidden_on_login is not None:
        _details['isHiddenOnLogin'] = is_hidden_on_login

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_domain(
        domain_id=domain_id,
        update_domain_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_iam_work_request') and callable(getattr(client, 'get_iam_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_iam_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
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


@dynamic_group_group.command(name=cli_util.override('iam.update_dynamic_group.command_name', 'update'), help=u"""Updates the specified dynamic group. \n[Command Reference](updateDynamicGroup)""")
@cli_util.option('--dynamic-group-id', required=True, help=u"""The OCID of the dynamic group.""")
@cli_util.option('--description', help=u"""The description you assign to the dynamic group. Does not have to be unique, and it's changeable.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--matching-rule', help=u"""The matching rule to dynamically match an instance certificate to this dynamic group. For rule syntax, see [Managing Dynamic Groups].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'DynamicGroup'})
@cli_util.wrap_exceptions
def update_dynamic_group(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, dynamic_group_id, description, matching_rule, freeform_tags, defined_tags, if_match):

    if isinstance(dynamic_group_id, six.string_types) and len(dynamic_group_id.strip()) == 0:
        raise click.UsageError('Parameter --dynamic-group-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if description is not None:
        _details['description'] = description

    if matching_rule is not None:
        _details['matchingRule'] = matching_rule

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_dynamic_group(
        dynamic_group_id=dynamic_group_id,
        update_dynamic_group_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_dynamic_group') and callable(getattr(client, 'get_dynamic_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_dynamic_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@group_group.command(name=cli_util.override('iam.update_group.command_name', 'update'), help=u"""Updates the specified group. \n[Command Reference](updateGroup)""")
@cli_util.option('--group-id', required=True, help=u"""The OCID of the group.""")
@cli_util.option('--description', help=u"""The description you assign to the group. Does not have to be unique, and it's changeable.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'Group'})
@cli_util.wrap_exceptions
def update_group(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, group_id, description, freeform_tags, defined_tags, if_match):

    if isinstance(group_id, six.string_types) and len(group_id.strip()) == 0:
        raise click.UsageError('Parameter --group-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_group(
        group_id=group_id,
        update_group_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_group') and callable(getattr(client, 'get_group')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_group(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@identity_provider_group.command(name=cli_util.override('iam.update_identity_provider.command_name', 'update'), help=u"""**Deprecated.** For more information, see [Deprecated IAM Service APIs].

Updates the specified identity provider. \n[Command Reference](updateIdentityProvider)""")
@cli_util.option('--identity-provider-id', required=True, help=u"""The OCID of the identity provider.""")
@cli_util.option('--protocol', required=True, type=custom_types.CliCaseInsensitiveChoice(["SAML2"]), help=u"""The protocol used for federation.

Example: `SAML2`""")
@cli_util.option('--description', help=u"""The description you assign to the `IdentityProvider`. Does not have to be unique, and it's changeable.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'IdentityProvider'})
@cli_util.wrap_exceptions
def update_identity_provider(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, identity_provider_id, protocol, description, freeform_tags, defined_tags, if_match):

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}
    _details['protocol'] = protocol

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_identity_provider(
        identity_provider_id=identity_provider_id,
        update_identity_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_identity_provider') and callable(getattr(client, 'get_identity_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_identity_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@identity_provider_group.command(name=cli_util.override('iam.update_identity_provider_update_saml2_identity_provider_details.command_name', 'update-identity-provider-update-saml2-identity-provider-details'), help=u"""**Deprecated.** For more information, see [Deprecated IAM Service APIs].

Updates the specified identity provider. \n[Command Reference](updateIdentityProvider)""")
@cli_util.option('--identity-provider-id', required=True, help=u"""The OCID of the identity provider.""")
@cli_util.option('--description', help=u"""The description you assign to the `IdentityProvider`. Does not have to be unique, and it's changeable.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--metadata-url', help=u"""The URL for retrieving the identity provider's metadata, which contains information required for federating.""")
@cli_util.option('--metadata', help=u"""The XML that contains the information required for federating.""")
@cli_util.option('--freeform-attributes', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Extra name value pairs associated with this identity provider. Example: `{\"clientId\": \"app_sf3kdjf3\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'freeform-attributes': {'module': 'identity', 'class': 'dict(str, string)'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'freeform-attributes': {'module': 'identity', 'class': 'dict(str, string)'}}, output_type={'module': 'identity', 'class': 'IdentityProvider'})
@cli_util.wrap_exceptions
def update_identity_provider_update_saml2_identity_provider_details(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, identity_provider_id, description, freeform_tags, defined_tags, metadata_url, metadata, freeform_attributes, if_match):

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or freeform_attributes:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and freeform-attributes will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if description is not None:
        _details['description'] = description

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if metadata_url is not None:
        _details['metadataUrl'] = metadata_url

    if metadata is not None:
        _details['metadata'] = metadata

    if freeform_attributes is not None:
        _details['freeformAttributes'] = cli_util.parse_json_parameter("freeform_attributes", freeform_attributes)

    _details['protocol'] = 'SAML2'

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_identity_provider(
        identity_provider_id=identity_provider_id,
        update_identity_provider_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_identity_provider') and callable(getattr(client, 'get_identity_provider')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_identity_provider(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@idp_group_mapping_group.command(name=cli_util.override('iam.update_idp_group_mapping.command_name', 'update'), help=u"""**Deprecated.** For more information, see [Deprecated IAM Service APIs].

Updates the specified group mapping. \n[Command Reference](updateIdpGroupMapping)""")
@cli_util.option('--identity-provider-id', required=True, help=u"""The OCID of the identity provider.""")
@cli_util.option('--mapping-id', required=True, help=u"""The OCID of the group mapping.""")
@cli_util.option('--idp-group-name', help=u"""The idp group name.""")
@cli_util.option('--group-id', help=u"""The OCID of the group.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'IdpGroupMapping'})
@cli_util.wrap_exceptions
def update_idp_group_mapping(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, identity_provider_id, mapping_id, idp_group_name, group_id, if_match):

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    if isinstance(mapping_id, six.string_types) and len(mapping_id.strip()) == 0:
        raise click.UsageError('Parameter --mapping-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if idp_group_name is not None:
        _details['idpGroupName'] = idp_group_name

    if group_id is not None:
        _details['groupId'] = group_id

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_idp_group_mapping(
        identity_provider_id=identity_provider_id,
        mapping_id=mapping_id,
        update_idp_group_mapping_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_idp_group_mapping') and callable(getattr(client, 'get_idp_group_mapping')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_idp_group_mapping(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@network_sources_group.command(name=cli_util.override('iam.update_network_source.command_name', 'update'), help=u"""Updates the specified network source. \n[Command Reference](updateNetworkSource)""")
@cli_util.option('--network-source-id', required=True, help=u"""The OCID of the network source.""")
@cli_util.option('--description', help=u"""The description you assign to the network source. Does not have to be unique, and it's changeable.""")
@cli_util.option('--public-source-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of allowed public IP addresses and CIDR ranges.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--virtual-source-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of allowed VCN OCID and IP range pairs. Example:`\"vcnId\": \"ocid1.vcn.oc1.iad.aaaaaaaaexampleuniqueID\", \"ipRanges\": [ \"129.213.39.0/24\" ]`

This option is a JSON list with items of type NetworkSourcesVirtualSourceList.  For documentation on NetworkSources_virtualSourceList please see our API reference: https://docs.cloud.oracle.com/api/#/en/identity/20160918/datatypes/NetworkSourcesVirtualSourceList.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--services', type=custom_types.CLI_COMPLEX_TYPE, help=u"""-- The services attribute has no effect and is reserved for use by Oracle. --""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'public-source-list': {'module': 'identity', 'class': 'list[string]'}, 'virtual-source-list': {'module': 'identity', 'class': 'list[NetworkSourcesVirtualSourceList]'}, 'services': {'module': 'identity', 'class': 'list[string]'}, 'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'public-source-list': {'module': 'identity', 'class': 'list[string]'}, 'virtual-source-list': {'module': 'identity', 'class': 'list[NetworkSourcesVirtualSourceList]'}, 'services': {'module': 'identity', 'class': 'list[string]'}, 'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'NetworkSources'})
@cli_util.wrap_exceptions
def update_network_source(ctx, from_json, force, network_source_id, description, public_source_list, virtual_source_list, services, freeform_tags, defined_tags, if_match):

    if isinstance(network_source_id, six.string_types) and len(network_source_id.strip()) == 0:
        raise click.UsageError('Parameter --network-source-id cannot be whitespace or empty string')
    if not force:
        if public_source_list or virtual_source_list or services or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to public-source-list and virtual-source-list and services and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if description is not None:
        _details['description'] = description

    if public_source_list is not None:
        _details['publicSourceList'] = cli_util.parse_json_parameter("public_source_list", public_source_list)

    if virtual_source_list is not None:
        _details['virtualSourceList'] = cli_util.parse_json_parameter("virtual_source_list", virtual_source_list)

    if services is not None:
        _details['services'] = cli_util.parse_json_parameter("services", services)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_network_source(
        network_source_id=network_source_id,
        update_network_source_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.update_o_auth_client_credential.command_name', 'update-o-auth-client-credential'), help=u"""Updates Oauth token for the user \n[Command Reference](updateOAuthClientCredential)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--oauth2-client-credential-id', required=True, help=u"""The ID of the Oauth credential.""")
@cli_util.option('--description', required=True, help=u"""Description of the oauth credential to help user differentiate them.""")
@cli_util.option('--scopes', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Allowed scopes for the given oauth credential.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-reset-password', type=click.BOOL, help=u"""Indicate if the password to be reset or not in the update.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'scopes': {'module': 'identity', 'class': 'list[FullyQualifiedScope]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'scopes': {'module': 'identity', 'class': 'list[FullyQualifiedScope]'}}, output_type={'module': 'identity', 'class': 'OAuth2ClientCredential'})
@cli_util.wrap_exceptions
def update_o_auth_client_credential(ctx, from_json, force, user_id, oauth2_client_credential_id, description, scopes, is_reset_password, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(oauth2_client_credential_id, six.string_types) and len(oauth2_client_credential_id.strip()) == 0:
        raise click.UsageError('Parameter --oauth2-client-credential-id cannot be whitespace or empty string')
    if not force:
        if scopes:
            if not click.confirm("WARNING: Updates to scopes will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}
    _details['description'] = description
    _details['scopes'] = cli_util.parse_json_parameter("scopes", scopes)

    if is_reset_password is not None:
        _details['isResetPassword'] = is_reset_password

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_o_auth_client_credential(
        user_id=user_id,
        oauth2_client_credential_id=oauth2_client_credential_id,
        update_o_auth2_client_credential_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@policy_group.command(name=cli_util.override('iam.update_policy.command_name', 'update'), help=u"""Updates the specified policy. You can update the description or the policy statements themselves.

Policy changes take effect typically within 10 seconds. \n[Command Reference](updatePolicy)""")
@cli_util.option('--policy-id', required=True, help=u"""The OCID of the policy.""")
@cli_util.option('--description', help=u"""The description you assign to the policy. Does not have to be unique, and it's changeable.""")
@cli_util.option('--statements', type=custom_types.CLI_COMPLEX_TYPE, help=u"""An array of policy statements written in the policy language. See [How Policies Work] and [Common Policies].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--version-date', type=custom_types.CLI_DATETIME, help=u"""The version of the policy. If null or set to an empty string, when a request comes in for authorization, the policy will be evaluated according to the current behavior of the services at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'statements': {'module': 'identity', 'class': 'list[string]'}, 'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'statements': {'module': 'identity', 'class': 'list[string]'}, 'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'Policy'})
@cli_util.wrap_exceptions
def update_policy(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, policy_id, description, statements, version_date, freeform_tags, defined_tags, if_match):

    if isinstance(policy_id, six.string_types) and len(policy_id.strip()) == 0:
        raise click.UsageError('Parameter --policy-id cannot be whitespace or empty string')
    if not force:
        if statements or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to statements and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if description is not None:
        _details['description'] = description

    if statements is not None:
        _details['statements'] = cli_util.parse_json_parameter("statements", statements)

    if version_date is not None:
        _details['versionDate'] = version_date

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_policy(
        policy_id=policy_id,
        update_policy_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_policy') and callable(getattr(client, 'get_policy')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_policy(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@smtp_credential_group.command(name=cli_util.override('iam.update_smtp_credential.command_name', 'update'), help=u"""Updates the specified SMTP credential's description. \n[Command Reference](updateSmtpCredential)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--smtp-credential-id', required=True, help=u"""The OCID of the SMTP credential.""")
@cli_util.option('--description', help=u"""The description you assign to the SMTP credential. Does not have to be unique, and it's changeable.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'SmtpCredentialSummary'})
@cli_util.wrap_exceptions
def update_smtp_credential(ctx, from_json, user_id, smtp_credential_id, description, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(smtp_credential_id, six.string_types) and len(smtp_credential_id.strip()) == 0:
        raise click.UsageError('Parameter --smtp-credential-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if description is not None:
        _details['description'] = description

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_smtp_credential(
        user_id=user_id,
        smtp_credential_id=smtp_credential_id,
        update_smtp_credential_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@swift_password_group.command(name=cli_util.override('iam.update_swift_password.command_name', 'update'), help=u"""**Deprecated. Use [UpdateAuthToken] instead.**

Updates the specified Swift password's description. \n[Command Reference](updateSwiftPassword)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--swift-password-id', required=True, help=u"""The OCID of the Swift password.""")
@cli_util.option('--description', help=u"""The description you assign to the Swift password. Does not have to be unique, and it's changeable.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'SwiftPassword'})
@cli_util.wrap_exceptions
def update_swift_password(ctx, from_json, user_id, swift_password_id, description, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(swift_password_id, six.string_types) and len(swift_password_id.strip()) == 0:
        raise click.UsageError('Parameter --swift-password-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if description is not None:
        _details['description'] = description

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_swift_password(
        user_id=user_id,
        swift_password_id=swift_password_id,
        update_swift_password_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tag_group.command(name=cli_util.override('iam.update_tag.command_name', 'update'), help=u"""Updates the specified tag definition.

Setting `validator` determines the value type. Tags can use either a static value or a list of possible values. Static values are entered by a user applying the tag to a resource. Lists are created by you and the user must apply a value from the list. On update, any values in a list that were previously set do not change, but new values must pass validation. Values already applied to a resource do not change.

You cannot remove list values that appear in a TagDefault. To remove a list value that appears in a TagDefault, first update the TagDefault to use a different value. \n[Command Reference](updateTag)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--tag-name', required=True, help=u"""The name of the tag.""")
@cli_util.option('--description', help=u"""The description you assign to the tag during creation.""")
@cli_util.option('--is-retired', type=click.BOOL, help=u"""Whether the tag is retired. See [Retiring Key Definitions and Namespace Definitions].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-cost-tracking', type=click.BOOL, help=u"""Indicates whether the tag is enabled for cost tracking.""")
@cli_util.option('--validator', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'validator': {'module': 'identity', 'class': 'BaseTagDefinitionValidator'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'validator': {'module': 'identity', 'class': 'BaseTagDefinitionValidator'}}, output_type={'module': 'identity', 'class': 'Tag'})
@cli_util.wrap_exceptions
def update_tag(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_namespace_id, tag_name, description, is_retired, freeform_tags, defined_tags, is_cost_tracking, validator, if_match, is_lock_override):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    if isinstance(tag_name, six.string_types) and len(tag_name.strip()) == 0:
        raise click.UsageError('Parameter --tag-name cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags or validator:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags and validator will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override

    _details = {}

    if description is not None:
        _details['description'] = description

    if is_retired is not None:
        _details['isRetired'] = is_retired

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if is_cost_tracking is not None:
        _details['isCostTracking'] = is_cost_tracking

    if validator is not None:
        _details['validator'] = cli_util.parse_json_parameter("validator", validator)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_tag(
        tag_namespace_id=tag_namespace_id,
        tag_name=tag_name,
        update_tag_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag') and callable(getattr(client, 'get_tag')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tag_group.command(name=cli_util.override('iam.update_tag_default_tag_definition_validator.command_name', 'update-tag-default-tag-definition-validator'), help=u"""Updates the specified tag definition.

Setting `validator` determines the value type. Tags can use either a static value or a list of possible values. Static values are entered by a user applying the tag to a resource. Lists are created by you and the user must apply a value from the list. On update, any values in a list that were previously set do not change, but new values must pass validation. Values already applied to a resource do not change.

You cannot remove list values that appear in a TagDefault. To remove a list value that appears in a TagDefault, first update the TagDefault to use a different value. \n[Command Reference](updateTag)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--tag-name', required=True, help=u"""The name of the tag.""")
@cli_util.option('--description', help=u"""The description you assign to the tag during creation.""")
@cli_util.option('--is-retired', type=click.BOOL, help=u"""Whether the tag is retired. See [Retiring Key Definitions and Namespace Definitions].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-cost-tracking', type=click.BOOL, help=u"""Indicates whether the tag is enabled for cost tracking.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'Tag'})
@cli_util.wrap_exceptions
def update_tag_default_tag_definition_validator(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_namespace_id, tag_name, description, is_retired, freeform_tags, defined_tags, is_cost_tracking, if_match, is_lock_override):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    if isinstance(tag_name, six.string_types) and len(tag_name.strip()) == 0:
        raise click.UsageError('Parameter --tag-name cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override

    _details = {}
    _details['validator'] = {}

    if description is not None:
        _details['description'] = description

    if is_retired is not None:
        _details['isRetired'] = is_retired

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if is_cost_tracking is not None:
        _details['isCostTracking'] = is_cost_tracking

    _details['validator']['validatorType'] = 'DEFAULT'

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_tag(
        tag_namespace_id=tag_namespace_id,
        tag_name=tag_name,
        update_tag_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag') and callable(getattr(client, 'get_tag')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tag_group.command(name=cli_util.override('iam.update_tag_enum_tag_definition_validator.command_name', 'update-tag-enum-tag-definition-validator'), help=u"""Updates the specified tag definition.

Setting `validator` determines the value type. Tags can use either a static value or a list of possible values. Static values are entered by a user applying the tag to a resource. Lists are created by you and the user must apply a value from the list. On update, any values in a list that were previously set do not change, but new values must pass validation. Values already applied to a resource do not change.

You cannot remove list values that appear in a TagDefault. To remove a list value that appears in a TagDefault, first update the TagDefault to use a different value. \n[Command Reference](updateTag)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--tag-name', required=True, help=u"""The name of the tag.""")
@cli_util.option('--description', help=u"""The description you assign to the tag during creation.""")
@cli_util.option('--is-retired', type=click.BOOL, help=u"""Whether the tag is retired. See [Retiring Key Definitions and Namespace Definitions].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags].

Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags].

Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-cost-tracking', type=click.BOOL, help=u"""Indicates whether the tag is enabled for cost tracking.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@cli_util.option('--validator-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of allowed values for a definedTag value.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'validator-values': {'module': 'identity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}, 'validator-values': {'module': 'identity', 'class': 'list[string]'}}, output_type={'module': 'identity', 'class': 'Tag'})
@cli_util.wrap_exceptions
def update_tag_enum_tag_definition_validator(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_namespace_id, tag_name, description, is_retired, freeform_tags, defined_tags, is_cost_tracking, if_match, is_lock_override, validator_values):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')

    if isinstance(tag_name, six.string_types) and len(tag_name.strip()) == 0:
        raise click.UsageError('Parameter --tag-name cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override

    _details = {}
    _details['validator'] = {}

    if description is not None:
        _details['description'] = description

    if is_retired is not None:
        _details['isRetired'] = is_retired

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if is_cost_tracking is not None:
        _details['isCostTracking'] = is_cost_tracking

    if validator_values is not None:
        _details['validator']['values'] = cli_util.parse_json_parameter("validator_values", validator_values)

    _details['validator']['validatorType'] = 'ENUM'

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_tag(
        tag_namespace_id=tag_namespace_id,
        tag_name=tag_name,
        update_tag_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag') and callable(getattr(client, 'get_tag')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tag_default_group.command(name=cli_util.override('iam.update_tag_default.command_name', 'update'), help=u"""Updates the specified tag default. If you specify that a value is required, a value is set during resource creation (either by the user creating the resource or another tag defualt). If no value is set, resource creation is blocked.

* If the `isRequired` flag is set to \"true\", the value is set during resource creation. * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation. \n[Command Reference](updateTagDefault)""")
@cli_util.option('--tag-default-id', required=True, help=u"""The OCID of the tag default.""")
@cli_util.option('--value', required=True, help=u"""The default value for the tag definition. This will be applied to all resources created in the Compartment.""")
@cli_util.option('--is-required', type=click.BOOL, help=u"""If you specify that a value is required, a value is set during resource creation (either by the user creating the resource or another tag defualt). If no value is set, resource creation is blocked.

* If the `isRequired` flag is set to \"true\", the value is set during resource creation. * If the `isRequired` flag is set to \"false\", the value you enter is set during resource creation.

Example: `false`""")
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'TagDefault'})
@cli_util.wrap_exceptions
def update_tag_default(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_default_id, value, is_required, is_lock_override, if_match):

    if isinstance(tag_default_id, six.string_types) and len(tag_default_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-default-id cannot be whitespace or empty string')

    kwargs = {}
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['value'] = value

    if is_required is not None:
        _details['isRequired'] = is_required

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_tag_default(
        tag_default_id=tag_default_id,
        update_tag_default_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag_default') and callable(getattr(client, 'get_tag_default')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag_default(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@tag_namespace_group.command(name=cli_util.override('iam.update_tag_namespace.command_name', 'update'), help=u"""Updates the the specified tag namespace. You can't update the namespace name.

Updating `isRetired` to 'true' retires the namespace and all the tag definitions in the namespace. Reactivating a namespace (changing `isRetired` from 'true' to 'false') does not reactivate tag definitions. To reactivate the tag definitions, you must reactivate each one individually *after* you reactivate the namespace, using [UpdateTag]. For more information about retiring tag namespaces, see [Retiring Key Definitions and Namespace Definitions].

You can't add a namespace with the same name as a retired namespace in the same tenancy. \n[Command Reference](updateTagNamespace)""")
@cli_util.option('--tag-namespace-id', required=True, help=u"""The OCID of the tag namespace.""")
@cli_util.option('--description', help=u"""The description you assign to the tag namespace.""")
@cli_util.option('--is-retired', type=click.BOOL, help=u"""Whether the tag namespace is retired. See [Retiring Key Definitions and Namespace Definitions].""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-lock-override', type=click.BOOL, help=u"""Whether to override locks (if any exist).""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'TagNamespace'})
@cli_util.wrap_exceptions
def update_tag_namespace(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, tag_namespace_id, description, is_retired, freeform_tags, defined_tags, is_lock_override):

    if isinstance(tag_namespace_id, six.string_types) and len(tag_namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --tag-namespace-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if is_lock_override is not None:
        kwargs['is_lock_override'] = is_lock_override

    _details = {}

    if description is not None:
        _details['description'] = description

    if is_retired is not None:
        _details['isRetired'] = is_retired

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_tag_namespace(
        tag_namespace_id=tag_namespace_id,
        update_tag_namespace_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_tag_namespace') and callable(getattr(client, 'get_tag_namespace')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_tag_namespace(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.update_user.command_name', 'update'), help=u"""Updates the description of the specified user. \n[Command Reference](updateUser)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--description', help=u"""The description you assign to the user. Does not have to be unique, and it's changeable.

(For tenancies that support identity domains) You can have an empty description.""")
@cli_util.option('--email', help=u"""The email you assign to the user during creation. The email must be unique across all users in the tenancy.

(For tenancies that support identity domains) You must provide an email for each user.""")
@cli_util.option('--db-user-name', help=u"""DB username of the DB credential. Has to be unique across the tenancy.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags]. Example: `{\"Department\": \"Finance\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags]. Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'identity', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'identity', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'identity', 'class': 'User'})
@cli_util.wrap_exceptions
def update_user(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, user_id, description, email, db_user_name, freeform_tags, defined_tags, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if description is not None:
        _details['description'] = description

    if email is not None:
        _details['email'] = email

    if db_user_name is not None:
        _details['dbUserName'] = db_user_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_user(
        user_id=user_id,
        update_user_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_user') and callable(getattr(client, 'get_user')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_user(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.update_user_capabilities.command_name', 'update-user-capabilities'), help=u"""Updates the capabilities of the specified user. \n[Command Reference](updateUserCapabilities)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--can-use-console-password', type=click.BOOL, help=u"""Indicates if the user can log in to the console.""")
@cli_util.option('--can-use-api-keys', type=click.BOOL, help=u"""Indicates if the user can use API keys.""")
@cli_util.option('--can-use-auth-tokens', type=click.BOOL, help=u"""Indicates if the user can use SWIFT passwords / auth tokens.""")
@cli_util.option('--can-use-smtp-credentials', type=click.BOOL, help=u"""Indicates if the user can use SMTP passwords.""")
@cli_util.option('--can-use-db-credentials', type=click.BOOL, help=u"""Indicates if the user can use DB passwords.""")
@cli_util.option('--can-use-customer-secret-keys', type=click.BOOL, help=u"""Indicates if the user can use SigV4 symmetric keys.""")
@cli_util.option('--can-use-o-auth2-client-credentials', type=click.BOOL, help=u"""Indicates if the user can use OAuth2 credentials and tokens.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'User'})
@cli_util.wrap_exceptions
def update_user_capabilities(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, user_id, can_use_console_password, can_use_api_keys, can_use_auth_tokens, can_use_smtp_credentials, can_use_db_credentials, can_use_customer_secret_keys, can_use_o_auth2_client_credentials, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if can_use_console_password is not None:
        _details['canUseConsolePassword'] = can_use_console_password

    if can_use_api_keys is not None:
        _details['canUseApiKeys'] = can_use_api_keys

    if can_use_auth_tokens is not None:
        _details['canUseAuthTokens'] = can_use_auth_tokens

    if can_use_smtp_credentials is not None:
        _details['canUseSmtpCredentials'] = can_use_smtp_credentials

    if can_use_db_credentials is not None:
        _details['canUseDBCredentials'] = can_use_db_credentials

    if can_use_customer_secret_keys is not None:
        _details['canUseCustomerSecretKeys'] = can_use_customer_secret_keys

    if can_use_o_auth2_client_credentials is not None:
        _details['canUseOAuth2ClientCredentials'] = can_use_o_auth2_client_credentials

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_user_capabilities(
        user_id=user_id,
        update_user_capabilities_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_user') and callable(getattr(client, 'get_user')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_user(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('iam.update_user_state.command_name', 'update-user-state'), help=u"""Updates the state of the specified user. \n[Command Reference](updateUserState)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--blocked', type=click.BOOL, help=u"""Update state to blocked or unblocked. Only \"false\" is supported (for changing the state to unblocked).""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'User'})
@cli_util.wrap_exceptions
def update_user_state(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, user_id, blocked, if_match):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    _details = {}

    if blocked is not None:
        _details['blocked'] = blocked

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.update_user_state(
        user_id=user_id,
        update_state_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_user') and callable(getattr(client, 'get_user')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_user(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@api_key_group.command(name=cli_util.override('iam.upload_api_key.command_name', 'upload'), help=u"""Uploads an API signing key for the specified user.

Every user has permission to use this operation to upload a key for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to upload a key for any user, including themselves.

**Important:** Even though you have permission to upload an API key, you might not yet have permission to do much else. If you try calling an operation unrelated to your own credential management (e.g., `ListUsers`, `LaunchInstance`) and receive an \"unauthorized\" error, check with an administrator to confirm which IAM Service group(s) you're in and what access you have. Also confirm you're working in the correct compartment.

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE. \n[Command Reference](uploadApiKey)""")
@cli_util.option('--user-id', required=True, help=u"""The OCID of the user.""")
@cli_util.option('--key', required=True, help=u"""The public key.  Must be an RSA key in PEM format.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'ApiKey'})
@cli_util.wrap_exceptions
def upload_api_key(ctx, from_json, user_id, key):

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}

    _details = {}
    _details['key'] = key

    client = cli_util.build_client('identity', 'identity', ctx)
    result = client.upload_api_key(
        user_id=user_id,
        create_api_key_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
