# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import random
import string

import click
import six

import oci
from oci_cli import cli_util


def get_compute_image_helper(ctx, image_id):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')
    ctx_endpoint = ctx.obj['endpoint']
    ctx.obj['endpoint'] = None
    if ctx.obj['config']['region'].split(".")[0] == "r1":
        ctx.obj['endpoint'] = "https://iaas.r1.oracleiaas.com"
    kwargs_request = {
        # 'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    }
    client = cli_util.build_client('core', 'compute', ctx)
    ctx.obj['endpoint'] = ctx_endpoint
    return client.get_image(
        image_id=image_id,
        **kwargs_request
    )


def export_compute_image_helper(ctx, image_id, destinationUri):
    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')
    export_details = {
        'destinationType': 'objectStorageUri',
        'destinationUri': destinationUri,
    }
    kwargs_request = {
        # 'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    }
    ctx_endpoint = ctx.obj['endpoint']
    ctx.obj['endpoint'] = None
    if ctx.obj['config']['region'].split(".")[0] == "r1":
        ctx.obj['endpoint'] = "https://iaas.r1.oracleiaas.com"
    client = cli_util.build_client('core', 'compute', ctx)
    ctx.obj['endpoint'] = ctx_endpoint
    return client.export_image(
        image_id=image_id,
        export_image_details=export_details,
        **kwargs_request
    )


def get_work_request(ctx, work_request_id):
    try:
        ctx_endpoint = ctx.obj['endpoint']
        ctx.obj['endpoint'] = None
        client = cli_util.build_client('work_requests', 'work_request', ctx)
        ctx.obj['endpoint'] = ctx_endpoint
        response = client.get_work_request(work_request_id=work_request_id)
        if response.data.status.lower() == "succeeded":
            return "SUCCEEDED"
        elif response.data.status.lower() == "failed":
            return "FAILED"
        else:
            percentage = 0 if response.data.status.lower() == "accepted" else response.data.percent_complete
            return str(percentage) + "% " + "IN_PROGRESS"
    except oci.exceptions.ServiceError as e:
        return "FAILED" if e.status == 404 else "NA"
    except Exception as e:
        return "NA"


def export_compute_image_status_helper(ctx, work_request_id):
    if work_request_id is None:
        return "NA"
    elif work_request_id.lower() == "exported":
        return "SUCCEEDED"
    elif work_request_id.find("ocid") >= 0:
        return get_work_request(ctx, work_request_id)


def prompt_for_secrets(secret_type):
    return click.prompt(text='Enter {0} (minimum 8 characters)'.format(secret_type), default='',
                        hide_input=True, show_default=False, confirmation_prompt=True)


def prompt_for_workload_delete():
    return click.prompt("Enter workload number to be deleted", type=int)


def modify_image_workload_name(image_workload_name):
    image_workload_name = image_workload_name.replace(" ", "")
    return image_workload_name


def create_master_key_policy_rover_resource(resource_name, ctx, **kwargs):
    confirm_prompt_policy = "You are providing your own master key ID, please create a policy to allow " \
                            "Roving Edge Infrastructure to create DEKs and use the master key ID to encrypt " \
                            "and decrypt data. Do you want to create the policy now?(Y/N)"
    value_policy = click.confirm(click.style(confirm_prompt_policy, fg="yellow"))
    if value_policy:
        policy_kwargs = {'master_key_id': kwargs['master_key_id']}
        #  Validate policy parameters. If policy-compartment-id is not provided,
        #  Check if policy should be created in the same compartment as the rover resource
        validate_policy_parameters(**kwargs)
        if not kwargs['policy_compartment_id']:
            confirm_policy_compartment = "Do you want to create the policy in the rover " + resource_name + \
                                         "'s compartment?(Y/N)"
            value_policy_compartment = click.confirm(click.style(confirm_policy_compartment, fg="yellow"))
            if value_policy_compartment:
                policy_kwargs['policy_compartment_id'] = kwargs['compartment_id']

        # Pass policy name as display name if provided else generate one
        if kwargs['policy_name']:
            policy_kwargs['policy_name'] = kwargs['policy_name'].strip()
        else:
            policy_kwargs['policy_name'] = kwargs['display_name'].strip() + "-" + generate_random_string()
        setup_master_key_policy(ctx, **policy_kwargs)
    else:
        click.echo("WARNING: Creation of the rover " + resource_name + " might fail if the policies are not provided")


def setup_master_key_policy(ctx, **kwargs):
    # Validate master-key-id
    if isinstance(kwargs['master_key_id'], six.string_types) and len(kwargs['master_key_id'].strip()) == 0:
        raise click.UsageError('Parameter master_key_id cannot be whitespace or empty string')
    config = oci.config.from_file(file_location=ctx.obj['config_file'], profile_name=ctx.obj['profile'])
    root_compartment = config['tenancy']
    # Use compartment id if provided, otherwise Use root tenancy
    if not kwargs['policy_compartment_id']:
        click.echo("WARNING: policy-compartment-id not provided, policy will be created in root tenancy")
        kwargs['policy_compartment_id'] = root_compartment

    # Validate policy name is provided, else generate one
    if not kwargs['policy_name']:
        kwargs['policy_name'] = config['user'][-8:] + "-" + generate_random_string()

    ctx.endpoint = None
    ctx.obj['endpoint'] = None
    compartment_id = kwargs['policy_compartment_id']
    policy_name = kwargs['policy_name'] + "-master-key-id-policy"

    # setting up home region and configuration in ctx since IAM resources can be created only in the home region of
    # the tenancy
    identity_client = cli_util.build_client('identity', 'identity', ctx)
    subscription_kwargs = {}
    subscriptions_result = identity_client.list_region_subscriptions(
        tenancy_id=root_compartment, **subscription_kwargs)

    if len(subscriptions_result.data) > 1:
        for subscription in subscriptions_result.data:
            if subscription.is_home_region:
                ctx.obj['region'] = subscription.region_name
                ctx.obj['config']['region'] = subscription.region_name
            break

    # Get identity client
    identity_client = cli_util.build_client('identity', 'identity', ctx)

    # setting up policies
    click.echo('Setting up the policies in the compartment.')
    statement_1 = "Allow service rover to use keys where target.key.id is " + kwargs['master_key_id']
    iam_kwargs = {}
    iam_details = {
        'compartmentId': compartment_id,
        'name': policy_name,
        'statements': [statement_1],
        'description': "The policies to use customer's master key"
    }

    create_policies_result = identity_client.create_policy(
        create_policy_details=iam_details,
        **iam_kwargs
    )
    return create_policies_result


def validate_policy_parameters(**kwargs):
    if 'policy_compartment_id' in kwargs and kwargs['policy_compartment_id']:
        if isinstance(kwargs['policy_compartment_id'], six.string_types) and \
                len(kwargs['policy_compartment_id'].strip()) == 0:
            raise click.UsageError('Parameter policy-compartment-id cannot be whitespace or empty string')
    if 'policy_name' in kwargs and kwargs['policy_name']:
        if isinstance(kwargs['policy_name'], six.string_types) and len(kwargs['policy_name'].strip()) == 0:
            raise click.UsageError('Policy name cannot be whitespace or empty string')


def generate_random_string():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(10))


def remove_additional_params_after_policy(**kwargs):
    if 'policy_name' in kwargs:
        kwargs.pop('policy_name')
    if 'policy_compartment_id' in kwargs:
        kwargs.pop('policy_compartment_id')
    return kwargs


def get_object_storage_helper(ctx):
    # Override the region for r1 for os public endpoint
    if 'config' in ctx.obj:
        if 'region' in ctx.obj['config'] and ctx.obj['config']['region']:  # region present in ~/.oci/config
            if ctx.obj['config']['region'].strip().split(".")[0] == "r1":
                region = ctx.obj['config']['region']
                ctx.obj['region'] = "r1.oracleiaas.com"
                object_cli = cli_util.build_client('object_storage', 'object_storage', ctx)
                ctx.obj['region'] = region
                return object_cli
    return cli_util.build_client('object_storage', 'object_storage', ctx)


def validate_get_image(ctx, **kwargs):
    if 'image_id' in kwargs and not kwargs['image_id']:
        raise click.UsageError('Parameter image-id cannot be whitespace or empty string')
    image_id = kwargs['image_id']
    try:
        compute_image_obj = get_compute_image_helper(ctx, image_id)
        if compute_image_obj is None or compute_image_obj.data is None:
            raise click.UsageError("Image not authorized or not found")
    except Exception as e:
        raise click.UsageError("Image not authorized or not found")
    return compute_image_obj


def validate_bucket(ctx, **kwargs):
    if kwargs['type'].lower() == "bucket":
        if not ('bucket_id' in kwargs and kwargs['bucket_id']) or not (
                'bucket_name' in kwargs and kwargs['bucket_name']):
            raise click.UsageError('Parameter bucket-id and bucket-name cannot be whitespace or empty string')
        try:
            object_storage_obj = get_object_storage_helper(ctx)
            namespace = object_storage_obj.get_namespace().data
            result = object_storage_obj.get_bucket(
                namespace_name=namespace,
                bucket_name=kwargs['bucket_name']
            )
            if result is None or result.data is None:
                raise click.UsageError("Bucket not authorized or not found")
        except Exception as e:
            raise click.UsageError("Bucket not authorized or not found")
    return result


def prepare_bucket_workload_data(result_bucket, **kwargs):
    workload_data = [{
        "workloadType": "BUCKET", "id": kwargs['bucket_id'], "name": kwargs['bucket_name'],
        "compartmentId": result_bucket.data.compartment_id,
        'prefix': kwargs['prefix'], 'rangeStart': kwargs['range_start'], 'rangeEnd': kwargs['range_end']
    }]
    return workload_data


def prepare_image_workload_data(compute_image_obj, image_id):
    compute_image_obj_name = modify_image_workload_name(compute_image_obj.data.display_name)
    workload_data = [
        {'workloadType': "IMAGE", 'id': image_id, 'name': compute_image_obj_name,
         'size': compute_image_obj.data.size_in_mbs, 'compartmentId': compute_image_obj.data.compartment_id,
         }
    ]
    return workload_data
