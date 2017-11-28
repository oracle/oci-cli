# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import six  # noqa: F401
from ..cli_root import cli
from .. import cli_util
from .. import json_skeleton_utils
from .. import retry_utils  # noqa: F401
from .. import custom_types  # noqa: F401
from ..aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('identity_group.command_name', 'identity'), cls=CommandGroupWithAlias, help=cli_util.override('identity_group.help', """APIs for managing users, groups, compartments, and policies."""))
@cli_util.help_option_group
def identity_group():
    pass


@click.command(cli_util.override('availability_domain_group.command_name', 'availability-domain'), cls=CommandGroupWithAlias, help="""One or more isolated, fault-tolerant Oracle data centers that host cloud resources such as instances, volumes,
and subnets. A region contains several Availability Domains. For more information, see
[Regions and Availability Domains].""")
@cli_util.help_option_group
def availability_domain_group():
    pass


@click.command(cli_util.override('customer_secret_key_group.command_name', 'customer-secret-key'), cls=CommandGroupWithAlias, help="""A `CustomerSecretKey` is an Oracle-provided key for using the Object Storage Service's
[Amazon S3 compatible API].
A user can have up to two secret keys at a time.

**Note:** The secret key is always an Oracle-generated string; you can't change it to a string of your choice.

For more information, see [Managing User Credentials].""")
@cli_util.help_option_group
def customer_secret_key_group():
    pass


@click.command(cli_util.override('idp_group_mapping_group.command_name', 'idp-group-mapping'), cls=CommandGroupWithAlias, help="""A mapping between a single group defined by the identity provider (IdP) you're federating with
and a single IAM Service [group] in Oracle Cloud Infrastructure.
For more information about group mappings and what they're for, see
[Identity Providers and Federation].

A given IdP group can be mapped to zero, one, or multiple IAM Service groups, and vice versa.
But each `IdPGroupMapping` object is between only a single IdP group and IAM Service group.
Each `IdPGroupMapping` object has its own OCID.

**Note:** Any users who are in more than 50 IdP groups cannot be authenticated to use the Oracle
Cloud Infrastructure Console.""")
@cli_util.help_option_group
def idp_group_mapping_group():
    pass


@click.command(cli_util.override('tenancy_group.command_name', 'tenancy'), cls=CommandGroupWithAlias, help="""The root compartment that contains all of your organization's compartments and other
Oracle Cloud Infrastructure cloud resources. When you sign up for Oracle Cloud Infrastructure,
Oracle creates a tenancy for your company, which is a secure and isolated partition
where you can create, organize, and administer your cloud resources.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access,
see [Getting Started with Policies].""")
@cli_util.help_option_group
def tenancy_group():
    pass


@click.command(cli_util.override('user_group_membership_group.command_name', 'user-group-membership'), cls=CommandGroupWithAlias, help="""An object that represents the membership of a user in a group. When you add a user to a group, the result is a
`UserGroupMembership` with its own OCID. To remove a user from a group, you delete the `UserGroupMembership` object.""")
@cli_util.help_option_group
def user_group_membership_group():
    pass


@click.command(cli_util.override('identity_provider_group.command_name', 'identity-provider'), cls=CommandGroupWithAlias, help="""The resulting base object when you add an identity provider to your tenancy. A
[Saml2IdentityProvider]
is a specific type of `IdentityProvider` that supports the SAML 2.0 protocol. Each
`IdentityProvider` object has its own OCID. For more information, see
[Identity Providers and Federation].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access,
see [Getting Started with Policies].""")
@cli_util.help_option_group
def identity_provider_group():
    pass


@click.command(cli_util.override('ui_password_group.command_name', 'ui-password'), cls=CommandGroupWithAlias, help="""A text password that enables a user to sign in to the Console, the user interface for interacting with Oracle
Cloud Infrastructure.

For more information about user credentials, see [User Credentials].""")
@cli_util.help_option_group
def ui_password_group():
    pass


@click.command(cli_util.override('api_key_group.command_name', 'api-key'), cls=CommandGroupWithAlias, help="""A PEM-format RSA credential for securing requests to the Oracle Cloud Infrastructure REST API. Also known
as an *API signing key*. Specifically, this is the public key from the key pair. The private key remains with
the user calling the API. For information about generating a key pair
in the required PEM format, see [Required Keys and OCIDs].

**Important:** This is **not** the SSH key for accessing compute instances.

Each user can have a maximum of three API signing keys.

For more information about user credentials, see [User Credentials].""")
@cli_util.help_option_group
def api_key_group():
    pass


@click.command(cli_util.override('region_subscription_group.command_name', 'region-subscription'), cls=CommandGroupWithAlias, help="""An object that represents your tenancy's access to a particular region (i.e., a subscription), the status of that
access, and whether that region is the home region. For more information, see [Managing Regions].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access,
see [Getting Started with Policies].""")
@cli_util.help_option_group
def region_subscription_group():
    pass


@click.command(cli_util.override('compartment_group.command_name', 'compartment'), cls=CommandGroupWithAlias, help="""A collection of related resources. Compartments are a fundamental component of Oracle Cloud Infrastructure
for organizing and isolating your cloud resources. You use them to clearly separate resources for the purposes
of measuring usage and billing, access (through the use of IAM Service policies), and isolation (separating the
resources for one project or business unit from another). A common approach is to create a compartment for each
major part of your organization. For more information, see
[Overview of the IAM Service] and also
[Setting Up Your Tenancy].

To place a resource in a compartment, simply specify the compartment ID in the "Create" request object when
initially creating the resource. For example, to launch an instance into a particular compartment, specify
that compartment's OCID in the `LaunchInstance` request. You can't move an existing resource from one
compartment to another.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access,
see [Getting Started with Policies].""")
@cli_util.help_option_group
def compartment_group():
    pass


@click.command(cli_util.override('region_group.command_name', 'region'), cls=CommandGroupWithAlias, help="""A localized geographic area, such as Phoenix, AZ. Oracle Cloud Infrastructure is hosted in regions and Availability
Domains. A region is composed of several Availability Domains. An Availability Domain is one or more data centers
located within a region. For more information, see [Regions and Availability Domains].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access,
see [Getting Started with Policies].""")
@cli_util.help_option_group
def region_group():
    pass


@click.command(cli_util.override('swift_password_group.command_name', 'swift-password'), cls=CommandGroupWithAlias, help="""Swift is the OpenStack object storage service. A `SwiftPassword` is an Oracle-provided password for using a
Swift client with the Oracle Cloud Infrastructure Object Storage Service. This password is associated with
the user's Console login. Swift passwords never expire. A user can have up to two Swift passwords at a time.

**Note:** The password is always an Oracle-generated string; you can't change it to a string of your choice.

For more information, see [Managing User Credentials].""")
@cli_util.help_option_group
def swift_password_group():
    pass


@click.command(cli_util.override('user_group.command_name', 'user'), cls=CommandGroupWithAlias, help="""An individual employee or system that needs to manage or use your company's Oracle Cloud Infrastructure
resources. Users might need to launch instances, manage remote disks, work with your cloud network, etc. Users
have one or more IAM Service credentials ([ApiKey],
[UIPassword], and [SwiftPassword]).
For more information, see [User Credentials]). End users of your
application are not typically IAM Service users. For conceptual information about users and other IAM Service
components, see [Overview of the IAM Service].

These users are created directly within the Oracle Cloud Infrastructure system, via the IAM service.
They are different from *federated users*, who authenticate themselves to the Oracle Cloud Infrastructure
Console via an identity provider. For more information, see
[Identity Providers and Federation].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access,
see [Getting Started with Policies].""")
@cli_util.help_option_group
def user_group():
    pass


@click.command(cli_util.override('group_group.command_name', 'group'), cls=CommandGroupWithAlias, help="""A collection of users who all need the same type of access to a particular set of resources or compartment.
For conceptual information about groups and other IAM Service components, see
[Overview of the IAM Service].

If you're federating with an identity provider (IdP), you need to create mappings between the groups
defined in the IdP and groups you define in the IAM service. For more information, see
[Identity Providers and Federation]. Also see
[IdentityProvider] and
[IdpGroupMapping].

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator. If you're an administrator who needs to write policies to give users access,
see [Getting Started with Policies].""")
@cli_util.help_option_group
def group_group():
    pass


@click.command(cli_util.override('policy_group.command_name', 'policy'), cls=CommandGroupWithAlias, help="""A document that specifies the type of access a group has to the resources in a compartment. For information about
policies and other IAM Service components, see
[Overview of the IAM Service]. If you're new to policies, see
[Getting Started with Policies].

The word "policy" is used by people in different ways:

  * An individual statement written in the policy language
  * A collection of statements in a single, named "policy" document (which has an Oracle Cloud ID (OCID) assigned to it)
  * The overall body of policies your organization uses to control access to resources

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
talk to an administrator.""")
@cli_util.help_option_group
def policy_group():
    pass


@user_group_membership_group.command(name=cli_util.override('add_user_to_group.command_name', 'add'), help="""Adds the specified user to the specified group and returns a `UserGroupMembership` object with its own OCID.

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--group-id', help="""The OCID of the group. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'UserGroupMembership'})
@cli_util.wrap_exceptions
def add_user_to_group(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id, group_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)
    group_id = cli_util.coalesce_provided_and_default_value(ctx, 'group-id', group_id, True)

    kwargs = {}

    details = {}
    details['userId'] = user_id
    details['groupId'] = group_id

    client = cli_util.build_client('identity', ctx)
    result = client.add_user_to_group(
        add_user_to_group_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compartment_group.command(name=cli_util.override('create_compartment.command_name', 'create'), help="""Creates a new compartment in your tenancy.

**Important:** Compartments cannot be deleted.

You must specify your tenancy's OCID as the compartment ID in the request object. Remember that the tenancy is simply the root compartment. For information about OCIDs, see [Resource Identifiers].

You must also specify a *name* for the compartment, which must be unique across all compartments in your tenancy. You can use this name or the OCID when writing policies that apply to the compartment. For more information about policies, see [How Policies Work].

You must also specify a *description* for the compartment (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateCompartment].

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.""")
@click.option('--compartment-id', help="""The OCID of the tenancy containing the compartment. [required]""")
@click.option('--name', help="""The name you assign to the compartment during creation. The name must be unique across all compartments in the tenancy. [required]""")
@click.option('--description', help="""The description you assign to the compartment during creation. Does not have to be unique, and it's changeable. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Compartment'})
@cli_util.wrap_exceptions
def create_compartment(ctx, generate_full_command_json_input, generate_param_json_input, from_json, compartment_id, name, description):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    name = cli_util.coalesce_provided_and_default_value(ctx, 'name', name, True)
    description = cli_util.coalesce_provided_and_default_value(ctx, 'description', description, True)

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['name'] = name
    details['description'] = description

    client = cli_util.build_client('identity', ctx)
    result = client.create_compartment(
        create_compartment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@customer_secret_key_group.command(name=cli_util.override('create_customer_secret_key.command_name', 'create'), help="""Creates a new secret key for the specified user. Secret keys are used for authentication with the Object Storage Service's Amazon S3 compatible API. For information, see [Managing User Credentials].

You must specify a *description* for the secret key (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateCustomerSecretKey].

Every user has permission to create a secret key for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to create a secret key for any user, including themselves.""")
@click.option('--display-name', help="""The name you assign to the secret key during creation. Does not have to be unique, and it's changeable. [required]""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'CustomerSecretKey'})
@cli_util.wrap_exceptions
def create_customer_secret_key(ctx, generate_full_command_json_input, generate_param_json_input, from_json, display_name, user_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    display_name = cli_util.coalesce_provided_and_default_value(ctx, 'display-name', display_name, True)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}

    details = {}
    details['displayName'] = display_name

    client = cli_util.build_client('identity', ctx)
    result = client.create_customer_secret_key(
        user_id=user_id,
        create_customer_secret_key_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@group_group.command(name=cli_util.override('create_group.command_name', 'create'), help="""Creates a new group in your tenancy.

You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies) reside within the tenancy itself, unlike cloud resources such as compute instances, which typically reside within compartments inside the tenancy. For information about OCIDs, see [Resource Identifiers].

You must also specify a *name* for the group, which must be unique across all groups in your tenancy and cannot be changed. You can use this name or the OCID when writing policies that apply to the group. For more information about policies, see [How Policies Work].

You must also specify a *description* for the group (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateGroup].

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.

After creating the group, you need to put users in it and write policies for it. See [AddUserToGroup] and [CreatePolicy].""")
@click.option('--compartment-id', help="""The OCID of the tenancy containing the group. [required]""")
@click.option('--name', help="""The name you assign to the group during creation. The name must be unique across all groups in the tenancy and cannot be changed. [required]""")
@click.option('--description', help="""The description you assign to the group during creation. Does not have to be unique, and it's changeable. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Group'})
@cli_util.wrap_exceptions
def create_group(ctx, generate_full_command_json_input, generate_param_json_input, from_json, compartment_id, name, description):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    name = cli_util.coalesce_provided_and_default_value(ctx, 'name', name, True)
    description = cli_util.coalesce_provided_and_default_value(ctx, 'description', description, True)

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['name'] = name
    details['description'] = description

    client = cli_util.build_client('identity', ctx)
    result = client.create_group(
        create_group_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@identity_provider_group.command(name=cli_util.override('create_identity_provider.command_name', 'create'), help="""Creates a new identity provider in your tenancy. For more information, see [Identity Providers and Federation].

You must specify your tenancy's OCID as the compartment ID in the request object. Remember that the tenancy is simply the root compartment. For information about OCIDs, see [Resource Identifiers].

You must also specify a *name* for the `IdentityProvider`, which must be unique across all `IdentityProvider` objects in your tenancy and cannot be changed.

You must also specify a *description* for the `IdentityProvider` (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateIdentityProvider].

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.""")
@click.option('--compartment-id', help="""The OCID of your tenancy. [required]""")
@click.option('--name', help="""The name you assign to the `IdentityProvider` during creation. The name must be unique across all `IdentityProvider` objects in the tenancy and cannot be changed. [required]""")
@click.option('--description', help="""The description you assign to the `IdentityProvider` during creation. Does not have to be unique, and it's changeable. [required]""")
@click.option('--product-type', type=custom_types.CliCaseInsensitiveChoice(["IDCS", "ADFS"]), help="""The identity provider service or product. Supported identity providers are Oracle Identity Cloud Service (IDCS) and Microsoft Active Directory Federation Services (ADFS).

Example: `IDCS` [required]""")
@click.option('--protocol', type=custom_types.CliCaseInsensitiveChoice(["SAML2"]), help="""The protocol used for federation.

Example: `SAML2` [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'IdentityProvider'})
@cli_util.wrap_exceptions
def create_identity_provider(ctx, generate_full_command_json_input, generate_param_json_input, from_json, compartment_id, name, description, product_type, protocol):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    name = cli_util.coalesce_provided_and_default_value(ctx, 'name', name, True)
    description = cli_util.coalesce_provided_and_default_value(ctx, 'description', description, True)
    product_type = cli_util.coalesce_provided_and_default_value(ctx, 'product-type', product_type, True)
    protocol = cli_util.coalesce_provided_and_default_value(ctx, 'protocol', protocol, True)

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['name'] = name
    details['description'] = description
    details['productType'] = product_type
    details['protocol'] = protocol

    client = cli_util.build_client('identity', ctx)
    result = client.create_identity_provider(
        create_identity_provider_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@idp_group_mapping_group.command(name=cli_util.override('create_idp_group_mapping.command_name', 'create'), help="""Creates a single mapping between an IdP group and an IAM Service [group].""")
@click.option('--idp-group-name', help="""The name of the IdP group you want to map. [required]""")
@click.option('--group-id', help="""The OCID of the IAM Service [group] you want to map to the IdP group. [required]""")
@click.option('--identity-provider-id', help="""The OCID of the identity provider. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'IdpGroupMapping'})
@cli_util.wrap_exceptions
def create_idp_group_mapping(ctx, generate_full_command_json_input, generate_param_json_input, from_json, idp_group_name, group_id, identity_provider_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    idp_group_name = cli_util.coalesce_provided_and_default_value(ctx, 'idp-group-name', idp_group_name, True)
    group_id = cli_util.coalesce_provided_and_default_value(ctx, 'group-id', group_id, True)
    identity_provider_id = cli_util.coalesce_provided_and_default_value(ctx, 'identity-provider-id', identity_provider_id, True)

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    kwargs = {}

    details = {}
    details['idpGroupName'] = idp_group_name
    details['groupId'] = group_id

    client = cli_util.build_client('identity', ctx)
    result = client.create_idp_group_mapping(
        identity_provider_id=identity_provider_id,
        create_idp_group_mapping_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@ui_password_group.command(name=cli_util.override('create_or_reset_ui_password.command_name', 'create-or-reset'), help="""Creates a new Console one-time password for the specified user. For more information about user credentials, see [User Credentials].

Use this operation after creating a new user, or if a user forgets their password. The new one-time password is returned to you in the response, and you must securely deliver it to the user. They'll be prompted to change this password the next time they sign in to the Console. If they don't change it within 7 days, the password will expire and you'll need to create a new one-time password for the user.

**Note:** The user's Console login is the unique name you specified when you created the user (see [CreateUser]).""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'UIPassword'})
@cli_util.wrap_exceptions
def create_or_reset_ui_password(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.create_or_reset_ui_password(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@policy_group.command(name=cli_util.override('create_policy.command_name', 'create'), help="""Creates a new policy in the specified compartment (either the tenancy or another of your compartments). If you're new to policies, see [Getting Started with Policies].

You must specify a *name* for the policy, which must be unique across all policies in your tenancy and cannot be changed.

You must also specify a *description* for the policy (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdatePolicy].

You must specify one or more policy statements in the statements array. For information about writing policies, see [How Policies Work] and [Common Policies].

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.

New policies take effect typically within 10 seconds.""")
@click.option('--compartment-id', help="""The OCID of the compartment containing the policy (either the tenancy or another compartment). [required]""")
@click.option('--name', help="""The name you assign to the policy during creation. The name must be unique across all policies in the tenancy and cannot be changed. [required]""")
@click.option('--statements', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of policy statements written in the policy language. See [How Policies Work] and [Common Policies]. [required]""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--description', help="""The description you assign to the policy during creation. Does not have to be unique, and it's changeable. [required]""")
@click.option('--version-date', type=custom_types.CLI_DATETIME, help="""The version of the policy. If null or set to an empty string, when a request comes in for authorization, the policy will be evaluated according to the current behavior of the services at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({'statements': {'module': 'identity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={'statements': {'module': 'identity', 'class': 'list[string]'}}, output_type={'module': 'identity', 'class': 'Policy'})
@cli_util.wrap_exceptions
def create_policy(ctx, generate_full_command_json_input, generate_param_json_input, from_json, compartment_id, name, statements, description, version_date):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    name = cli_util.coalesce_provided_and_default_value(ctx, 'name', name, True)
    statements = cli_util.coalesce_provided_and_default_value(ctx, 'statements', statements, True)
    description = cli_util.coalesce_provided_and_default_value(ctx, 'description', description, True)
    version_date = cli_util.coalesce_provided_and_default_value(ctx, 'version-date', version_date, False)

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['name'] = name
    details['statements'] = cli_util.parse_json_parameter("statements", statements)
    details['description'] = description

    if version_date is not None:
        details['versionDate'] = version_date

    client = cli_util.build_client('identity', ctx)
    result = client.create_policy(
        create_policy_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@region_subscription_group.command(name=cli_util.override('create_region_subscription.command_name', 'create'), help="""Creates a subscription to a region for a tenancy.""")
@click.option('--region-key', help="""The regions's key.

Allowed values are: - `PHX` - `IAD` - `FRA`

Example: `PHX` [required]""")
@click.option('--tenancy-id', help="""The OCID of the tenancy. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'RegionSubscription'})
@cli_util.wrap_exceptions
def create_region_subscription(ctx, generate_full_command_json_input, generate_param_json_input, from_json, region_key, tenancy_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    region_key = cli_util.coalesce_provided_and_default_value(ctx, 'region-key', region_key, True)
    tenancy_id = cli_util.coalesce_provided_and_default_value(ctx, 'tenancy-id', tenancy_id, True)

    if isinstance(tenancy_id, six.string_types) and len(tenancy_id.strip()) == 0:
        raise click.UsageError('Parameter --tenancy-id cannot be whitespace or empty string')

    kwargs = {}

    details = {}
    details['regionKey'] = region_key

    client = cli_util.build_client('identity', ctx)
    result = client.create_region_subscription(
        tenancy_id=tenancy_id,
        create_region_subscription_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@swift_password_group.command(name=cli_util.override('create_swift_password.command_name', 'create'), help="""Creates a new Swift password for the specified user. For information about what Swift passwords are for, see [Managing User Credentials].

You must specify a *description* for the Swift password (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateSwiftPassword].

Every user has permission to create a Swift password for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to create a Swift password for any user, including themselves.""")
@click.option('--description', help="""The description you assign to the Swift password during creation. Does not have to be unique, and it's changeable. [required]""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'SwiftPassword'})
@cli_util.wrap_exceptions
def create_swift_password(ctx, generate_full_command_json_input, generate_param_json_input, from_json, description, user_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    description = cli_util.coalesce_provided_and_default_value(ctx, 'description', description, True)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}

    details = {}
    details['description'] = description

    client = cli_util.build_client('identity', ctx)
    result = client.create_swift_password(
        user_id=user_id,
        create_swift_password_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('create_user.command_name', 'create'), help="""Creates a new user in your tenancy. For conceptual information about users, your tenancy, and other IAM Service components, see [Overview of the IAM Service].

You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies) reside within the tenancy itself, unlike cloud resources such as compute instances, which typically reside within compartments inside the tenancy. For information about OCIDs, see [Resource Identifiers].

You must also specify a *name* for the user, which must be unique across all users in your tenancy and cannot be changed. Allowed characters: No spaces. Only letters, numerals, hyphens, periods, underscores, +, and @. If you specify a name that's already in use, you'll get a 409 error. This name will be the user's login to the Console. You might want to pick a name that your company's own identity system (e.g., Active Directory, LDAP, etc.) already uses. If you delete a user and then create a new user with the same name, they'll be considered different users because they have different OCIDs.

You must also specify a *description* for the user (although it can be an empty string). It does not have to be unique, and you can change it anytime with [UpdateUser]. You can use the field to provide the user's full name, a description, a nickname, or other information to generally identify the user.

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.

A new user has no permissions until you place the user in one or more groups (see [AddUserToGroup]). If the user needs to access the Console, you need to provide the user a password (see [CreateOrResetUIPassword]). If the user needs to access the Oracle Cloud Infrastructure REST API, you need to upload a public API signing key for that user (see [Required Keys and OCIDs] and also [UploadApiKey]).

**Important:** Make sure to inform the new user which compartment(s) they have access to.""")
@click.option('--compartment-id', help="""The OCID of the tenancy containing the user. [required]""")
@click.option('--name', help="""The name you assign to the user during creation. This is the user's login for the Console. The name must be unique across all users in the tenancy and cannot be changed. [required]""")
@click.option('--description', help="""The description you assign to the user during creation. Does not have to be unique, and it's changeable. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'User'})
@cli_util.wrap_exceptions
def create_user(ctx, generate_full_command_json_input, generate_param_json_input, from_json, compartment_id, name, description):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    name = cli_util.coalesce_provided_and_default_value(ctx, 'name', name, True)
    description = cli_util.coalesce_provided_and_default_value(ctx, 'description', description, True)

    kwargs = {}

    details = {}
    details['compartmentId'] = compartment_id
    details['name'] = name
    details['description'] = description

    client = cli_util.build_client('identity', ctx)
    result = client.create_user(
        create_user_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@api_key_group.command(name=cli_util.override('delete_api_key.command_name', 'delete'), help="""Deletes the specified API signing key for the specified user.

Every user has permission to use this operation to delete a key for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to delete a key for any user, including themselves.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--fingerprint', help="""The key's fingerprint. [required]""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_api_key(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id, fingerprint, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)
    fingerprint = cli_util.coalesce_provided_and_default_value(ctx, 'fingerprint', fingerprint, True)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(fingerprint, six.string_types) and len(fingerprint.strip()) == 0:
        raise click.UsageError('Parameter --fingerprint cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', ctx)
    result = client.delete_api_key(
        user_id=user_id,
        fingerprint=fingerprint,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@customer_secret_key_group.command(name=cli_util.override('delete_customer_secret_key.command_name', 'delete'), help="""Deletes the specified secret key for the specified user.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--customer-secret-key-id', help="""The OCID of the secret key. [required]""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_customer_secret_key(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id, customer_secret_key_id, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)
    customer_secret_key_id = cli_util.coalesce_provided_and_default_value(ctx, 'customer-secret-key-id', customer_secret_key_id, True)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(customer_secret_key_id, six.string_types) and len(customer_secret_key_id.strip()) == 0:
        raise click.UsageError('Parameter --customer-secret-key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', ctx)
    result = client.delete_customer_secret_key(
        user_id=user_id,
        customer_secret_key_id=customer_secret_key_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@group_group.command(name=cli_util.override('delete_group.command_name', 'delete'), help="""Deletes the specified group. The group must be empty.""")
@click.option('--group-id', help="""The OCID of the group. [required]""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_group(ctx, generate_full_command_json_input, generate_param_json_input, from_json, group_id, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    group_id = cli_util.coalesce_provided_and_default_value(ctx, 'group-id', group_id, True)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(group_id, six.string_types) and len(group_id.strip()) == 0:
        raise click.UsageError('Parameter --group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', ctx)
    result = client.delete_group(
        group_id=group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@identity_provider_group.command(name=cli_util.override('delete_identity_provider.command_name', 'delete'), help="""Deletes the specified identity provider. The identity provider must not have any group mappings (see [IdpGroupMapping]).""")
@click.option('--identity-provider-id', help="""The OCID of the identity provider. [required]""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_identity_provider(ctx, generate_full_command_json_input, generate_param_json_input, from_json, identity_provider_id, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    identity_provider_id = cli_util.coalesce_provided_and_default_value(ctx, 'identity-provider-id', identity_provider_id, True)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', ctx)
    result = client.delete_identity_provider(
        identity_provider_id=identity_provider_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@idp_group_mapping_group.command(name=cli_util.override('delete_idp_group_mapping.command_name', 'delete'), help="""Deletes the specified group mapping.""")
@click.option('--identity-provider-id', help="""The OCID of the identity provider. [required]""")
@click.option('--mapping-id', help="""The OCID of the group mapping. [required]""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_idp_group_mapping(ctx, generate_full_command_json_input, generate_param_json_input, from_json, identity_provider_id, mapping_id, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    identity_provider_id = cli_util.coalesce_provided_and_default_value(ctx, 'identity-provider-id', identity_provider_id, True)
    mapping_id = cli_util.coalesce_provided_and_default_value(ctx, 'mapping-id', mapping_id, True)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    if isinstance(mapping_id, six.string_types) and len(mapping_id.strip()) == 0:
        raise click.UsageError('Parameter --mapping-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', ctx)
    result = client.delete_idp_group_mapping(
        identity_provider_id=identity_provider_id,
        mapping_id=mapping_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@policy_group.command(name=cli_util.override('delete_policy.command_name', 'delete'), help="""Deletes the specified policy. The deletion takes effect typically within 10 seconds.""")
@click.option('--policy-id', help="""The OCID of the policy. [required]""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_policy(ctx, generate_full_command_json_input, generate_param_json_input, from_json, policy_id, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    policy_id = cli_util.coalesce_provided_and_default_value(ctx, 'policy-id', policy_id, True)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(policy_id, six.string_types) and len(policy_id.strip()) == 0:
        raise click.UsageError('Parameter --policy-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', ctx)
    result = client.delete_policy(
        policy_id=policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@swift_password_group.command(name=cli_util.override('delete_swift_password.command_name', 'delete'), help="""Deletes the specified Swift password for the specified user.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--swift-password-id', help="""The OCID of the Swift password. [required]""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_swift_password(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id, swift_password_id, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)
    swift_password_id = cli_util.coalesce_provided_and_default_value(ctx, 'swift-password-id', swift_password_id, True)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(swift_password_id, six.string_types) and len(swift_password_id.strip()) == 0:
        raise click.UsageError('Parameter --swift-password-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', ctx)
    result = client.delete_swift_password(
        user_id=user_id,
        swift_password_id=swift_password_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('delete_user.command_name', 'delete'), help="""Deletes the specified user. The user must not be in any groups.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_user(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', ctx)
    result = client.delete_user(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compartment_group.command(name=cli_util.override('get_compartment.command_name', 'get'), help="""Gets the specified compartment's information.

This operation does not return a list of all the resources inside the compartment. There is no single API operation that does that. Compartments can contain multiple types of resources (instances, block storage volumes, etc.). To find out what's in a compartment, you must call the \"List\" operation for each resource type and specify the compartment's OCID as a query parameter in the request. For example, call the [ListInstances] operation in the Cloud Compute Service or the [ListVolumes] operation in Cloud Block Storage.""")
@click.option('--compartment-id', help="""The OCID of the compartment. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Compartment'})
@cli_util.wrap_exceptions
def get_compartment(ctx, generate_full_command_json_input, generate_param_json_input, from_json, compartment_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)

    if isinstance(compartment_id, six.string_types) and len(compartment_id.strip()) == 0:
        raise click.UsageError('Parameter --compartment-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.get_compartment(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@group_group.command(name=cli_util.override('get_group.command_name', 'get'), help="""Gets the specified group's information.

This operation does not return a list of all the users in the group. To do that, use [ListUserGroupMemberships] and provide the group's OCID as a query parameter in the request.""")
@click.option('--group-id', help="""The OCID of the group. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Group'})
@cli_util.wrap_exceptions
def get_group(ctx, generate_full_command_json_input, generate_param_json_input, from_json, group_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    group_id = cli_util.coalesce_provided_and_default_value(ctx, 'group-id', group_id, True)

    if isinstance(group_id, six.string_types) and len(group_id.strip()) == 0:
        raise click.UsageError('Parameter --group-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.get_group(
        group_id=group_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@identity_provider_group.command(name=cli_util.override('get_identity_provider.command_name', 'get'), help="""Gets the specified identity provider's information.""")
@click.option('--identity-provider-id', help="""The OCID of the identity provider. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'IdentityProvider'})
@cli_util.wrap_exceptions
def get_identity_provider(ctx, generate_full_command_json_input, generate_param_json_input, from_json, identity_provider_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    identity_provider_id = cli_util.coalesce_provided_and_default_value(ctx, 'identity-provider-id', identity_provider_id, True)

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.get_identity_provider(
        identity_provider_id=identity_provider_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@idp_group_mapping_group.command(name=cli_util.override('get_idp_group_mapping.command_name', 'get'), help="""Gets the specified group mapping.""")
@click.option('--identity-provider-id', help="""The OCID of the identity provider. [required]""")
@click.option('--mapping-id', help="""The OCID of the group mapping. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'IdpGroupMapping'})
@cli_util.wrap_exceptions
def get_idp_group_mapping(ctx, generate_full_command_json_input, generate_param_json_input, from_json, identity_provider_id, mapping_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    identity_provider_id = cli_util.coalesce_provided_and_default_value(ctx, 'identity-provider-id', identity_provider_id, True)
    mapping_id = cli_util.coalesce_provided_and_default_value(ctx, 'mapping-id', mapping_id, True)

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    if isinstance(mapping_id, six.string_types) and len(mapping_id.strip()) == 0:
        raise click.UsageError('Parameter --mapping-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.get_idp_group_mapping(
        identity_provider_id=identity_provider_id,
        mapping_id=mapping_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@policy_group.command(name=cli_util.override('get_policy.command_name', 'get'), help="""Gets the specified policy's information.""")
@click.option('--policy-id', help="""The OCID of the policy. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Policy'})
@cli_util.wrap_exceptions
def get_policy(ctx, generate_full_command_json_input, generate_param_json_input, from_json, policy_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    policy_id = cli_util.coalesce_provided_and_default_value(ctx, 'policy-id', policy_id, True)

    if isinstance(policy_id, six.string_types) and len(policy_id.strip()) == 0:
        raise click.UsageError('Parameter --policy-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.get_policy(
        policy_id=policy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@tenancy_group.command(name=cli_util.override('get_tenancy.command_name', 'get'), help="""Get the specified tenancy's information.""")
@click.option('--tenancy-id', help="""The OCID of the tenancy. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Tenancy'})
@cli_util.wrap_exceptions
def get_tenancy(ctx, generate_full_command_json_input, generate_param_json_input, from_json, tenancy_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    tenancy_id = cli_util.coalesce_provided_and_default_value(ctx, 'tenancy-id', tenancy_id, True)

    if isinstance(tenancy_id, six.string_types) and len(tenancy_id.strip()) == 0:
        raise click.UsageError('Parameter --tenancy-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.get_tenancy(
        tenancy_id=tenancy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('get_user.command_name', 'get'), help="""Gets the specified user's information.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'User'})
@cli_util.wrap_exceptions
def get_user(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.get_user(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group_membership_group.command(name=cli_util.override('get_user_group_membership.command_name', 'get'), help="""Gets the specified UserGroupMembership's information.""")
@click.option('--user-group-membership-id', help="""The OCID of the userGroupMembership. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'UserGroupMembership'})
@cli_util.wrap_exceptions
def get_user_group_membership(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_group_membership_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_group_membership_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-group-membership-id', user_group_membership_id, True)

    if isinstance(user_group_membership_id, six.string_types) and len(user_group_membership_id.strip()) == 0:
        raise click.UsageError('Parameter --user-group-membership-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.get_user_group_membership(
        user_group_membership_id=user_group_membership_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@api_key_group.command(name=cli_util.override('list_api_keys.command_name', 'list'), help="""Lists the API signing keys for the specified user. A user can have a maximum of three keys.

Every user has permission to use this API call for *their own user ID*.  An administrator in your organization does not need to write a policy to give users this ability.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[ApiKey]'})
@cli_util.wrap_exceptions
def list_api_keys(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.list_api_keys(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@availability_domain_group.command(name=cli_util.override('list_availability_domains.command_name', 'list'), help="""Lists the Availability Domains in your tenancy. Specify the OCID of either the tenancy or another of your compartments as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID].""")
@click.option('--compartment-id', help="""The OCID of the compartment (remember that the tenancy is simply the root compartment). [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[AvailabilityDomain]'})
@cli_util.wrap_exceptions
def list_availability_domains(ctx, generate_full_command_json_input, generate_param_json_input, from_json, compartment_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.list_availability_domains(
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compartment_group.command(name=cli_util.override('list_compartments.command_name', 'list'), help="""Lists the compartments in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID].""")
@click.option('--compartment-id', help="""The OCID of the compartment (remember that the tenancy is simply the root compartment). [required]""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@click.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[Compartment]'})
@cli_util.wrap_exceptions
def list_compartments(ctx, generate_full_command_json_input, generate_param_json_input, from_json, all_pages, page_size, compartment_id, page, limit):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    page = cli_util.coalesce_provided_and_default_value(ctx, 'page', page, False)
    limit = cli_util.coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    all_pages = cli_util.coalesce_provided_and_default_value(ctx, 'all', all_pages, False)
    page_size = cli_util.coalesce_provided_and_default_value(ctx, 'page-size', page_size, False)
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_compartments,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@customer_secret_key_group.command(name=cli_util.override('list_customer_secret_keys.command_name', 'list'), help="""Lists the secret keys for the specified user. The returned object contains the secret key's OCID, but not the secret key itself. The actual secret key is returned only upon creation.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[CustomerSecretKeySummary]'})
@cli_util.wrap_exceptions
def list_customer_secret_keys(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.list_customer_secret_keys(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@group_group.command(name=cli_util.override('list_groups.command_name', 'list'), help="""Lists the groups in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID].""")
@click.option('--compartment-id', help="""The OCID of the compartment (remember that the tenancy is simply the root compartment). [required]""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@click.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[Group]'})
@cli_util.wrap_exceptions
def list_groups(ctx, generate_full_command_json_input, generate_param_json_input, from_json, all_pages, page_size, compartment_id, page, limit):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    page = cli_util.coalesce_provided_and_default_value(ctx, 'page', page, False)
    limit = cli_util.coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    all_pages = cli_util.coalesce_provided_and_default_value(ctx, 'all', all_pages, False)
    page_size = cli_util.coalesce_provided_and_default_value(ctx, 'page-size', page_size, False)
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_groups,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@identity_provider_group.command(name=cli_util.override('list_identity_providers.command_name', 'list'), help="""Lists all the identity providers in your tenancy. You must specify the identity provider type (e.g., `SAML2` for identity providers using the SAML2.0 protocol). You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID].""")
@click.option('--protocol', help="""The protocol used for federation. Allowed values are: SAML2 [required]""")
@click.option('--compartment-id', help="""The OCID of the compartment (remember that the tenancy is simply the root compartment). [required]""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@click.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[IdentityProvider]'})
@cli_util.wrap_exceptions
def list_identity_providers(ctx, generate_full_command_json_input, generate_param_json_input, from_json, all_pages, page_size, protocol, compartment_id, page, limit):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    protocol = cli_util.coalesce_provided_and_default_value(ctx, 'protocol', protocol, True)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    page = cli_util.coalesce_provided_and_default_value(ctx, 'page', page, False)
    limit = cli_util.coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    all_pages = cli_util.coalesce_provided_and_default_value(ctx, 'all', all_pages, False)
    page_size = cli_util.coalesce_provided_and_default_value(ctx, 'page-size', page_size, False)
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_identity_providers,
            protocol=protocol,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@idp_group_mapping_group.command(name=cli_util.override('list_idp_group_mappings.command_name', 'list'), help="""Lists the group mappings for the specified identity provider.""")
@click.option('--identity-provider-id', help="""The OCID of the identity provider. [required]""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@click.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[IdpGroupMapping]'})
@cli_util.wrap_exceptions
def list_idp_group_mappings(ctx, generate_full_command_json_input, generate_param_json_input, from_json, all_pages, page_size, identity_provider_id, page, limit):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    identity_provider_id = cli_util.coalesce_provided_and_default_value(ctx, 'identity-provider-id', identity_provider_id, True)
    page = cli_util.coalesce_provided_and_default_value(ctx, 'page', page, False)
    limit = cli_util.coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    all_pages = cli_util.coalesce_provided_and_default_value(ctx, 'all', all_pages, False)
    page_size = cli_util.coalesce_provided_and_default_value(ctx, 'page-size', page_size, False)
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_idp_group_mappings,
            identity_provider_id=identity_provider_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@policy_group.command(name=cli_util.override('list_policies.command_name', 'list'), help="""Lists the policies in the specified compartment (either the tenancy or another of your compartments). See [Where to Get the Tenancy's OCID and User's OCID].

To determine which policies apply to a particular group or compartment, you must view the individual statements inside all your policies. There isn't a way to automatically obtain that information via the API.""")
@click.option('--compartment-id', help="""The OCID of the compartment (remember that the tenancy is simply the root compartment). [required]""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@click.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[Policy]'})
@cli_util.wrap_exceptions
def list_policies(ctx, generate_full_command_json_input, generate_param_json_input, from_json, all_pages, page_size, compartment_id, page, limit):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    page = cli_util.coalesce_provided_and_default_value(ctx, 'page', page, False)
    limit = cli_util.coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    all_pages = cli_util.coalesce_provided_and_default_value(ctx, 'all', all_pages, False)
    page_size = cli_util.coalesce_provided_and_default_value(ctx, 'page-size', page_size, False)
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_policies,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@region_subscription_group.command(name=cli_util.override('list_region_subscriptions.command_name', 'list'), help="""Lists the region subscriptions for the specified tenancy.""")
@click.option('--tenancy-id', help="""The OCID of the tenancy. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[RegionSubscription]'})
@cli_util.wrap_exceptions
def list_region_subscriptions(ctx, generate_full_command_json_input, generate_param_json_input, from_json, tenancy_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    tenancy_id = cli_util.coalesce_provided_and_default_value(ctx, 'tenancy-id', tenancy_id, True)

    if isinstance(tenancy_id, six.string_types) and len(tenancy_id.strip()) == 0:
        raise click.UsageError('Parameter --tenancy-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.list_region_subscriptions(
        tenancy_id=tenancy_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@region_group.command(name=cli_util.override('list_regions.command_name', 'list'), help="""Lists all the regions offered by Oracle Cloud Infrastructure.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[Region]'})
@cli_util.wrap_exceptions
def list_regions(ctx, generate_full_command_json_input, generate_param_json_input, from_json, ):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.list_regions(
        **kwargs
    )
    cli_util.render_response(result, ctx)


@swift_password_group.command(name=cli_util.override('list_swift_passwords.command_name', 'list'), help="""Lists the Swift passwords for the specified user. The returned object contains the password's OCID, but not the password itself. The actual password is returned only upon creation.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[SwiftPassword]'})
@cli_util.wrap_exceptions
def list_swift_passwords(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    client = cli_util.build_client('identity', ctx)
    result = client.list_swift_passwords(
        user_id=user_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group_membership_group.command(name=cli_util.override('list_user_group_memberships.command_name', 'list'), help="""Lists the `UserGroupMembership` objects in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (see [Where to Get the Tenancy's OCID and User's OCID]). You must also then filter the list in one of these ways:

- You can limit the results to just the memberships for a given user by specifying a `userId`. - Similarly, you can limit the results to just the memberships for a given group by specifying a `groupId`. - You can set both the `userId` and `groupId` to determine if the specified user is in the specified group. If the answer is no, the response is an empty list.""")
@click.option('--compartment-id', help="""The OCID of the compartment (remember that the tenancy is simply the root compartment). [required]""")
@click.option('--user-id', help="""The OCID of the user.""")
@click.option('--group-id', help="""The OCID of the group.""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@click.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[UserGroupMembership]'})
@cli_util.wrap_exceptions
def list_user_group_memberships(ctx, generate_full_command_json_input, generate_param_json_input, from_json, all_pages, page_size, compartment_id, user_id, group_id, page, limit):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, False)
    group_id = cli_util.coalesce_provided_and_default_value(ctx, 'group-id', group_id, False)
    page = cli_util.coalesce_provided_and_default_value(ctx, 'page', page, False)
    limit = cli_util.coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    all_pages = cli_util.coalesce_provided_and_default_value(ctx, 'all', all_pages, False)
    page_size = cli_util.coalesce_provided_and_default_value(ctx, 'page-size', page_size, False)
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
    client = cli_util.build_client('identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_user_group_memberships,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@user_group.command(name=cli_util.override('list_users.command_name', 'list'), help="""Lists the users in your tenancy. You must specify your tenancy's OCID as the value for the compartment ID (remember that the tenancy is simply the root compartment). See [Where to Get the Tenancy's OCID and User's OCID].""")
@click.option('--compartment-id', help="""The OCID of the compartment (remember that the tenancy is simply the root compartment). [required]""")
@click.option('--page', help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--limit', type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.""")
@click.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'list[User]'})
@cli_util.wrap_exceptions
def list_users(ctx, generate_full_command_json_input, generate_param_json_input, from_json, all_pages, page_size, compartment_id, page, limit):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    page = cli_util.coalesce_provided_and_default_value(ctx, 'page', page, False)
    limit = cli_util.coalesce_provided_and_default_value(ctx, 'limit', limit, False)
    all_pages = cli_util.coalesce_provided_and_default_value(ctx, 'all', all_pages, False)
    page_size = cli_util.coalesce_provided_and_default_value(ctx, 'page-size', page_size, False)
    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    client = cli_util.build_client('identity', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_users,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
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


@user_group_membership_group.command(name=cli_util.override('remove_user_from_group.command_name', 'remove'), help="""Removes a user from a group by deleting the corresponding `UserGroupMembership`.""")
@click.option('--user-group-membership-id', help="""The OCID of the userGroupMembership. [required]""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def remove_user_from_group(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_group_membership_id, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_group_membership_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-group-membership-id', user_group_membership_id, True)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(user_group_membership_id, six.string_types) and len(user_group_membership_id.strip()) == 0:
        raise click.UsageError('Parameter --user-group-membership-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('identity', ctx)
    result = client.remove_user_from_group(
        user_group_membership_id=user_group_membership_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@compartment_group.command(name=cli_util.override('update_compartment.command_name', 'update'), help="""Updates the specified compartment's description or name. You can't update the root compartment.""")
@click.option('--compartment-id', help="""The OCID of the compartment. [required]""")
@click.option('--description', help="""The description you assign to the compartment. Does not have to be unique, and it's changeable.""")
@click.option('--name', help="""The new name you assign to the compartment. The name must be unique across all compartments in the tenancy.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Compartment'})
@cli_util.wrap_exceptions
def update_compartment(ctx, generate_full_command_json_input, generate_param_json_input, from_json, compartment_id, description, name, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    compartment_id = cli_util.coalesce_provided_and_default_value(ctx, 'compartment-id', compartment_id, True)
    description = cli_util.coalesce_provided_and_default_value(ctx, 'description', description, False)
    name = cli_util.coalesce_provided_and_default_value(ctx, 'name', name, False)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(compartment_id, six.string_types) and len(compartment_id.strip()) == 0:
        raise click.UsageError('Parameter --compartment-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if description is not None:
        details['description'] = description

    if name is not None:
        details['name'] = name

    client = cli_util.build_client('identity', ctx)
    result = client.update_compartment(
        compartment_id=compartment_id,
        update_compartment_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@customer_secret_key_group.command(name=cli_util.override('update_customer_secret_key.command_name', 'update'), help="""Updates the specified secret key's description.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--customer-secret-key-id', help="""The OCID of the secret key. [required]""")
@click.option('--display-name', help="""The description you assign to the secret key. Does not have to be unique, and it's changeable.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'CustomerSecretKeySummary'})
@cli_util.wrap_exceptions
def update_customer_secret_key(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id, customer_secret_key_id, display_name, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)
    customer_secret_key_id = cli_util.coalesce_provided_and_default_value(ctx, 'customer-secret-key-id', customer_secret_key_id, True)
    display_name = cli_util.coalesce_provided_and_default_value(ctx, 'display-name', display_name, False)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(customer_secret_key_id, six.string_types) and len(customer_secret_key_id.strip()) == 0:
        raise click.UsageError('Parameter --customer-secret-key-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('identity', ctx)
    result = client.update_customer_secret_key(
        user_id=user_id,
        customer_secret_key_id=customer_secret_key_id,
        update_customer_secret_key_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@group_group.command(name=cli_util.override('update_group.command_name', 'update'), help="""Updates the specified group.""")
@click.option('--group-id', help="""The OCID of the group. [required]""")
@click.option('--description', help="""The description you assign to the group. Does not have to be unique, and it's changeable.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'Group'})
@cli_util.wrap_exceptions
def update_group(ctx, generate_full_command_json_input, generate_param_json_input, from_json, group_id, description, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    group_id = cli_util.coalesce_provided_and_default_value(ctx, 'group-id', group_id, True)
    description = cli_util.coalesce_provided_and_default_value(ctx, 'description', description, False)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(group_id, six.string_types) and len(group_id.strip()) == 0:
        raise click.UsageError('Parameter --group-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if description is not None:
        details['description'] = description

    client = cli_util.build_client('identity', ctx)
    result = client.update_group(
        group_id=group_id,
        update_group_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@identity_provider_group.command(name=cli_util.override('update_identity_provider.command_name', 'update'), help="""Updates the specified identity provider.""")
@click.option('--identity-provider-id', help="""The OCID of the identity provider. [required]""")
@click.option('--protocol', type=custom_types.CliCaseInsensitiveChoice(["SAML2"]), help="""The protocol used for federation.

Example: `SAML2` [required]""")
@click.option('--description', help="""The description you assign to the `IdentityProvider`. Does not have to be unique, and it's changeable.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'IdentityProvider'})
@cli_util.wrap_exceptions
def update_identity_provider(ctx, generate_full_command_json_input, generate_param_json_input, from_json, identity_provider_id, protocol, description, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    identity_provider_id = cli_util.coalesce_provided_and_default_value(ctx, 'identity-provider-id', identity_provider_id, True)
    protocol = cli_util.coalesce_provided_and_default_value(ctx, 'protocol', protocol, True)
    description = cli_util.coalesce_provided_and_default_value(ctx, 'description', description, False)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}
    details['protocol'] = protocol

    if description is not None:
        details['description'] = description

    client = cli_util.build_client('identity', ctx)
    result = client.update_identity_provider(
        identity_provider_id=identity_provider_id,
        update_identity_provider_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@idp_group_mapping_group.command(name=cli_util.override('update_idp_group_mapping.command_name', 'update'), help="""Updates the specified group mapping.""")
@click.option('--identity-provider-id', help="""The OCID of the identity provider. [required]""")
@click.option('--mapping-id', help="""The OCID of the group mapping. [required]""")
@click.option('--idp-group-name', help="""The idp group name.""")
@click.option('--group-id', help="""The OCID of the group.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'IdpGroupMapping'})
@cli_util.wrap_exceptions
def update_idp_group_mapping(ctx, generate_full_command_json_input, generate_param_json_input, from_json, identity_provider_id, mapping_id, idp_group_name, group_id, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    identity_provider_id = cli_util.coalesce_provided_and_default_value(ctx, 'identity-provider-id', identity_provider_id, True)
    mapping_id = cli_util.coalesce_provided_and_default_value(ctx, 'mapping-id', mapping_id, True)
    idp_group_name = cli_util.coalesce_provided_and_default_value(ctx, 'idp-group-name', idp_group_name, False)
    group_id = cli_util.coalesce_provided_and_default_value(ctx, 'group-id', group_id, False)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(identity_provider_id, six.string_types) and len(identity_provider_id.strip()) == 0:
        raise click.UsageError('Parameter --identity-provider-id cannot be whitespace or empty string')

    if isinstance(mapping_id, six.string_types) and len(mapping_id.strip()) == 0:
        raise click.UsageError('Parameter --mapping-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if idp_group_name is not None:
        details['idpGroupName'] = idp_group_name

    if group_id is not None:
        details['groupId'] = group_id

    client = cli_util.build_client('identity', ctx)
    result = client.update_idp_group_mapping(
        identity_provider_id=identity_provider_id,
        mapping_id=mapping_id,
        update_idp_group_mapping_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@policy_group.command(name=cli_util.override('update_policy.command_name', 'update'), help="""Updates the specified policy. You can update the description or the policy statements themselves.

Policy changes take effect typically within 10 seconds.""")
@click.option('--policy-id', help="""The OCID of the policy. [required]""")
@click.option('--description', help="""The description you assign to the policy. Does not have to be unique, and it's changeable.""")
@click.option('--statements', type=custom_types.CLI_COMPLEX_TYPE, help="""An array of policy statements written in the policy language. See [How Policies Work] and [Common Policies].""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@click.option('--version-date', type=custom_types.CLI_DATETIME, help="""The version of the policy. If null or set to an empty string, when a request comes in for authorization, the policy will be evaluated according to the current behavior of the services at that moment. If set to a particular date (YYYY-MM-DD), the policy will be evaluated according to the behavior of the services on that date.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({'statements': {'module': 'identity', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={'statements': {'module': 'identity', 'class': 'list[string]'}}, output_type={'module': 'identity', 'class': 'Policy'})
@cli_util.wrap_exceptions
def update_policy(ctx, generate_full_command_json_input, generate_param_json_input, from_json, force, policy_id, description, statements, version_date, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    policy_id = cli_util.coalesce_provided_and_default_value(ctx, 'policy-id', policy_id, True)
    description = cli_util.coalesce_provided_and_default_value(ctx, 'description', description, False)
    statements = cli_util.coalesce_provided_and_default_value(ctx, 'statements', statements, False)
    version_date = cli_util.coalesce_provided_and_default_value(ctx, 'version-date', version_date, False)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)
    force = cli_util.coalesce_provided_and_default_value(ctx, 'force', force, False)

    if isinstance(policy_id, six.string_types) and len(policy_id.strip()) == 0:
        raise click.UsageError('Parameter --policy-id cannot be whitespace or empty string')

    if not force:
        if statements:
            if not click.confirm("WARNING: Updates to statements will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if description is not None:
        details['description'] = description

    if statements is not None:
        details['statements'] = cli_util.parse_json_parameter("statements", statements)

    if version_date is not None:
        details['versionDate'] = version_date

    client = cli_util.build_client('identity', ctx)
    result = client.update_policy(
        policy_id=policy_id,
        update_policy_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@swift_password_group.command(name=cli_util.override('update_swift_password.command_name', 'update'), help="""Updates the specified Swift password's description.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--swift-password-id', help="""The OCID of the Swift password. [required]""")
@click.option('--description', help="""The description you assign to the Swift password. Does not have to be unique, and it's changeable.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'SwiftPassword'})
@cli_util.wrap_exceptions
def update_swift_password(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id, swift_password_id, description, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)
    swift_password_id = cli_util.coalesce_provided_and_default_value(ctx, 'swift-password-id', swift_password_id, True)
    description = cli_util.coalesce_provided_and_default_value(ctx, 'description', description, False)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    if isinstance(swift_password_id, six.string_types) and len(swift_password_id.strip()) == 0:
        raise click.UsageError('Parameter --swift-password-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if description is not None:
        details['description'] = description

    client = cli_util.build_client('identity', ctx)
    result = client.update_swift_password(
        user_id=user_id,
        swift_password_id=swift_password_id,
        update_swift_password_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('update_user.command_name', 'update'), help="""Updates the description of the specified user.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--description', help="""The description you assign to the user. Does not have to be unique, and it's changeable.""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'User'})
@cli_util.wrap_exceptions
def update_user(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id, description, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)
    description = cli_util.coalesce_provided_and_default_value(ctx, 'description', description, False)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if description is not None:
        details['description'] = description

    client = cli_util.build_client('identity', ctx)
    result = client.update_user(
        user_id=user_id,
        update_user_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@user_group.command(name=cli_util.override('update_user_state.command_name', 'update-user-state'), help="""Updates the state of the specified user.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--blocked', type=click.BOOL, help="""Update state to blocked or unblocked. Only \"false\" is supported (for changing the state to unblocked).""")
@click.option('--if-match', help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource.  The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'User'})
@cli_util.wrap_exceptions
def update_user_state(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id, blocked, if_match):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)
    blocked = cli_util.coalesce_provided_and_default_value(ctx, 'blocked', blocked, False)
    if_match = cli_util.coalesce_provided_and_default_value(ctx, 'if-match', if_match, False)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if blocked is not None:
        details['blocked'] = blocked

    client = cli_util.build_client('identity', ctx)
    result = client.update_user_state(
        user_id=user_id,
        update_state_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@api_key_group.command(name=cli_util.override('upload_api_key.command_name', 'upload'), help="""Uploads an API signing key for the specified user.

Every user has permission to use this operation to upload a key for *their own user ID*. An administrator in your organization does not need to write a policy to give users this ability. To compare, administrators who have permission to the tenancy can use this operation to upload a key for any user, including themselves.

**Important:** Even though you have permission to upload an API key, you might not yet have permission to do much else. If you try calling an operation unrelated to your own credential management (e.g., `ListUsers`, `LaunchInstance`) and receive an \"unauthorized\" error, check with an administrator to confirm which IAM Service group(s) you're in and what access you have. Also confirm you're working in the correct compartment.

After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the object, first make sure its `lifecycleState` has changed to ACTIVE.""")
@click.option('--user-id', help="""The OCID of the user. [required]""")
@click.option('--key', help="""The public key.  Must be an RSA key in PEM format. [required]""")
@click.option('--generate-full-command-json-input', is_flag=True, is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Prints out a JSON document which represents all possible options that can be provided to this command.

This JSON document can be saved to a file, modified with the appropriate option values, and then passed back via the --from-json option. This provides an alternative to typing options out on the command line.""")
@click.option('--generate-param-json-input', is_eager=True, callback=json_skeleton_utils.generate_json_skeleton_click_callback, help="""Complex input, such as arrays and objects, are passed in JSON format.

When passed the name of an option which takes complex input, this will print out example JSON of what needs to be passed to that option.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_wrapper_metadata(input_params_to_complex_types={}, output_type={'module': 'identity', 'class': 'ApiKey'})
@cli_util.wrap_exceptions
def upload_api_key(ctx, generate_full_command_json_input, generate_param_json_input, from_json, user_id, key):
    if generate_param_json_input and generate_full_command_json_input:
        raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")

    if generate_full_command_json_input:
        json_skeleton_utils.generate_json_skeleton_for_full_command(ctx)
    elif generate_param_json_input:
        json_skeleton_utils.generate_json_skeleton_for_option(ctx, generate_param_json_input)

    cli_util.load_context_obj_values_from_defaults(ctx)
    user_id = cli_util.coalesce_provided_and_default_value(ctx, 'user-id', user_id, True)
    key = cli_util.coalesce_provided_and_default_value(ctx, 'key', key, True)

    if isinstance(user_id, six.string_types) and len(user_id.strip()) == 0:
        raise click.UsageError('Parameter --user-id cannot be whitespace or empty string')

    kwargs = {}

    details = {}
    details['key'] = key

    client = cli_util.build_client('identity', ctx)
    result = client.upload_api_key(
        user_id=user_id,
        create_api_key_details=details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
