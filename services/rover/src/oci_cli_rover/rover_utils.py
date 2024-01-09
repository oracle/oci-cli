# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import json
import random
import re
import string
import math
import sys
import time
import click
import six
import os

import oci
from oci_cli import cli_util
from oci.retry import DEFAULT_RETRY_STRATEGY, RetryStrategyBuilder
from oci.object_storage import UploadManager, MultipartObjectAssembler
from oci.util import Sentinel

from services.object_storage.src.oci_cli_object_storage.object_storage_transfer_manager.wrapped_semaphore import \
    WrappedSemaphore

from services.rover.src.constants import (
    ROVER_UPGRADE_BUNDLE_UPLOAD_BUCKET,
    ROVER_DIAGNOSTIC_BUNDLE_API_BASE_PATH,
    DEFAULT_ROVER_DEVICE_ENDPOINT,
    TERMINAL_STATES,
    NON_TERMINAL_STATES)

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher,
    algorithms,
    modes)
from timeit import default_timer as timer
from pathlib import Path


missing = Sentinel("Missing")


class RoverDiagAPI:
    def __init__(self, data=None, headers=None):
        self.data = data
        self.headers = headers


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
    return click.prompt(text='Enter {0} (minimum 8 characters)'.format(secret_type), default=None,
                        hide_input=True, show_default=False, confirmation_prompt=True)


def prompt_for_workload_delete():
    return click.prompt("Enter workload number to be deleted", type=int)


def modify_image_workload_name(image_workload_name):
    image_workload_name = image_workload_name.replace(" ", "")
    return image_workload_name


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
    if 'default_values_from_file' in ctx.obj and 'os.endpoint' in ctx.obj['default_values_from_file']:
        endpoint = ctx.obj['endpoint']
        ctx.obj['endpoint'] = ctx.obj['default_values_from_file']['os.endpoint']
        object_cli = cli_util.build_client('object_storage', 'object_storage', ctx)
        ctx.obj['endpoint'] = endpoint
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


def prepare_bucket_workload_data(compartment_id, **kwargs):
    workload_data = [{
        "workloadType": "BUCKET", "id": kwargs['bucket_name'], "name": kwargs['bucket_name'],
        "compartmentId": compartment_id,
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
        else:
            policy_kwargs['policy_compartment_id'] = kwargs['policy_compartment_id']

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
    statement_1 = "Allow service rover to use keys in compartment ID " + \
        compartment_id + " where target.key.id = " + kwargs['master_key_id']
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


def prepare_set_secrets_request(is_create, **kwargs_request):
    confirm_super_user_password = "Do you want to set the super user password?(Y/N)"
    value_super_user_password = click.confirm(click.style(confirm_super_user_password, fg="yellow"))
    if value_super_user_password:
        super_user_password = prompt_for_secrets("super_user_password")
        if not super_user_password:
            raise click.UsageError('Super user password cannot be whitespace or empty string')
        kwargs_request['super_user_password'] = super_user_password

    confirm_unlock_passphrase = "Do you want to set the unlock passphrase?(Y/N)"
    value_unlock_passphrase = click.confirm(click.style(confirm_unlock_passphrase, fg="yellow"))
    if value_unlock_passphrase:
        unlock_passphrase = prompt_for_secrets("unlock_passphrase")
        if not unlock_passphrase:
            raise click.UsageError('Unlock passphrase cannot be whitespace or empty string')
        kwargs_request['unlock_passphrase'] = unlock_passphrase

    if 'super_user_password' not in kwargs_request and 'unlock_passphrase' not in kwargs_request and not is_create:
        raise click.UsageError('Super user password or unlock passphrase needs to be supplied to set the secrets')
    return kwargs_request


def upload_bundle_for_upgrade(ctx, bundle_file_path):
    if not hasattr(bundle_file_path, 'name'):
        raise click.UsageError('Corrupt file, exiting upload!!!')
    else:
        display_name = os.path.basename(bundle_file_path.name).split("/")[-1]
        upload_bundle_to_bucket(ctx, bundle_file_path, display_name)


def import_bundle_for_upgrade(ctx, bundle_file_path, wait):
    display_name = bundle_file_path.split("/")[-1]
    if ctx.obj['endpoint']:
        endpoint = ctx.obj['endpoint']
    else:
        endpoint = DEFAULT_ROVER_DEVICE_ENDPOINT
    task_id = import_bundle_task(ctx, endpoint, display_name)
    if wait:
        check_status_for_upgrade(ctx, task_id, endpoint)


def check_status(ctx, task_id, should_wait):
    if ctx.obj['endpoint']:
        endpoint = ctx.obj['endpoint']
    else:
        endpoint = DEFAULT_ROVER_DEVICE_ENDPOINT
    if should_wait:
        check_status_for_upgrade(ctx, task_id, endpoint)
    else:
        check_status_for_upgrade_no_poll(ctx, task_id, endpoint)


def check_status_for_upgrade(ctx, task_id, endpoint):
    while True:
        status = monitor_import_progress(ctx, endpoint, task_id)
        if check_if_state_matches(status.upper(), TERMINAL_STATES):
            print('Import status is: ' + status)
            print("EXITING")
            break
        else:
            if check_if_state_matches(status.upper(), NON_TERMINAL_STATES):
                print("Import status at " + status + '...')
                time.sleep(15)
            else:
                print('Unknown status is: ' + status)
                print("EXITING")
                break


def check_status_for_upgrade_no_poll(ctx, task_id, endpoint):
    status = monitor_import_progress(ctx, endpoint, task_id)
    if check_if_state_matches(status.upper(), TERMINAL_STATES):
        print('Import status is: ' + status)
    elif check_if_state_matches(status.upper(), NON_TERMINAL_STATES):
        print("Import status at " + status + '...')
    else:
        print('Unknown status is: ' + status)


def check_import_history(ctx):
    print('Checking the import status for all tasks.')
    if ctx.obj['endpoint']:
        endpoint = ctx.obj['endpoint']
    else:
        endpoint = DEFAULT_ROVER_DEVICE_ENDPOINT
    target_uri = endpoint + '/20180828/importBundleTask'

    http_method = 'GET'
    retry_strategy = DEFAULT_RETRY_STRATEGY
    parsed_request_body = ''
    additional_headers = {}
    jmespath_expression = cli_util.get_jmespath_expression_from_context(ctx)
    with cli_util.build_raw_requests_session(ctx) as requests_session:
        response = retry_strategy.make_retrying_call(
            requests_session.request,
            method=http_method,
            url=target_uri,
            data=parsed_request_body,
            headers=additional_headers
        )

        result_dict = {
            'status': '{} {}'.format(response.status_code, response.reason),
            'headers': {key: value for (key, value) in response.headers.items()}
        }
        try:
            dict_from_response_body = response.json()
            if jmespath_expression:
                result_dict['data'] = jmespath_expression.search(dict_from_response_body)
            else:
                result_dict['data'] = dict_from_response_body
        except ValueError:
            # We may not have gotten valid JSON. In that case, do our best and just display something
            result_dict['data'] = response.text
        print(cli_util.pretty_print_format(result_dict))


def upload_bundle_to_bucket(ctx, request_body, display_name):
    print('Starting upload of bundle to bucket')
    os_client = get_object_storage_helper(ctx)
    namespace = os_client.get_namespace().data
    result = upload_multi_part(ctx, request_body, namespace, ROVER_UPGRADE_BUNDLE_UPLOAD_BUCKET, display_name)
    click.echo(result)
    print("Upload of bundle " + display_name + " to the bucket " + ROVER_UPGRADE_BUNDLE_UPLOAD_BUCKET + " successfully  completed")


def upload_multi_part(ctx, file, namespace, bucket_name, name):
    client = get_object_storage_helper(ctx)
    client_request_id = ctx.obj['request_id']
    kwargs = {'opc_client_request_id': client_request_id}
    part_size_mib = 10 * 1024 * 1024
    total_size = os.fstat(file.fileno()).st_size
    part_size = 0

    if math.ceil(total_size / part_size_mib) > 10000:
        part_size = math.ceil(math.ceil(total_size / 10000) / (1024 * 1024))
        kwargs['part_size'] = part_size * (1024 * 1024)

    size_qualifies_for_multipart = UploadManager._use_multipart(total_size, part_size) if part_size else UploadManager._use_multipart(total_size)

    ma = None
    if size_qualifies_for_multipart:

        kwargs['parallel_process_count'] = 10

        UploadManager._add_adapter_to_service_client(client, True, kwargs['parallel_process_count'])

        ma = MultipartObjectAssembler(client,
                                      namespace,
                                      bucket_name,
                                      name,
                                      **kwargs)

        ma.new_upload()
        click.echo('Upload ID: {}'.format(ma.manifest["uploadId"]), file=sys.stderr)
        ma.add_parts_from_file(file.name)
        click.echo('Split file into {} parts for upload.'.format(len(ma.manifest["parts"])), file=sys.stderr)

        max_attempts = 60

        # max_attempts retries - with exponential sleep time and a max wait of 60 secs.
        retry_strategy = RetryStrategyBuilder(retry_max_wait_between_calls_seconds=60).add_max_attempts(max_attempts) \
            .no_total_elapsed_time() \
            .add_service_error_check() \
            .get_retry_strategy()

        with ProgressBar(total_size, 'Uploading object') as bar:
            try:
                ma.upload(retry_strategy=retry_strategy, progress_callback=bar.update)
                response = ma.commit(retry_strategy=retry_strategy)
            except RuntimeError as re:
                if 'thread' in str(re) or 'Thread' in str(re):
                    raise Exception('Cannot start that many threads, please reduce the parallel-upload-count. The '
                                    'default is ' + str(10))
                else:
                    raise re
            except Exception as e:
                raise e
    else:
        # if file is empty, progress_callback will never be called (no bytes will be read), so dont show progress bar
        bar = None
        if total_size > 0:
            bar = ProgressBar(total_size, 'Uploading object')
            kwargs['progress_callback'] = bar.update
        try:
            upload_manager = UploadManager(client, allow_multipart_uploads=False)
            response = upload_manager.upload_file(namespace, bucket_name, name, file.name, **kwargs)
        except Exception as e:
            if bar:
                bar.render_finish()
            raise e

        if bar:
            bar.render_finish()


def import_bundle_task(ctx, endpoint, display_name):
    print('Starting import bundle task request submission')
    target_uri = endpoint + '/20180828/importBundleTask'
    http_method = 'POST'
    retry_strategy = DEFAULT_RETRY_STRATEGY
    request_headers = construct_request_headers(display_name)

    parsed_request_body = ''
    additional_headers = {}
    if request_headers:
        additional_headers = cli_util.parse_json_parameter('request_headers', request_headers, 'camelize_keys', False)
    jmespath_expression = cli_util.get_jmespath_expression_from_context(ctx)
    with cli_util.build_raw_requests_session(ctx) as requests_session:
        try:
            response = retry_strategy.make_retrying_call(
                requests_session.request,
                method=http_method,
                url=target_uri,
                data=parsed_request_body,
                headers=additional_headers
            )
        except Exception as e:
            print(e)

        result_dict = {
            'status': '{} {}'.format(response.status_code, response.reason),
            'headers': {key: value for (key, value) in response.headers.items()}
        }
        try:
            dict_from_response_body = response.json()
            if jmespath_expression:
                result_dict['data'] = jmespath_expression.search(dict_from_response_body)
            else:
                result_dict['data'] = dict_from_response_body
            task_id = result_dict['data']['taskId']
            print("Submitted successfully request for import with taskId = " + task_id)
        except Exception as e:
            # We may not have gotten valid JSON. In that case, do our best and just display something
            result_dict['data'] = response.text
            if not ('taskId' in result_dict['data'] and result_dict['data']['taskId']):
                raise Exception("Error submitting the import task for bundle")
            else:
                raise Exception(e)
        print("Submitted successfully request for import with taskId2 = " + task_id)
        return task_id


def monitor_import_progress(ctx, endpoint, task_id):
    print('Checking the import progress for task ' + task_id)
    target_uri = endpoint + '/20180828/importBundleTask/' + task_id

    http_method = 'GET'
    retry_strategy = DEFAULT_RETRY_STRATEGY
    parsed_request_body = ''
    additional_headers = {}
    jmespath_expression = cli_util.get_jmespath_expression_from_context(ctx)
    with cli_util.build_raw_requests_session(ctx) as requests_session:
        response = retry_strategy.make_retrying_call(
            requests_session.request,
            method=http_method,
            url=target_uri,
            data=parsed_request_body,
            headers=additional_headers
        )

        result_dict = {
            'status': '{} {}'.format(response.status_code, response.reason),
            'headers': {key: value for (key, value) in response.headers.items()}
        }
        try:
            dict_from_response_body = response.json()
            if jmespath_expression:
                result_dict['data'] = jmespath_expression.search(dict_from_response_body)
            else:
                result_dict['data'] = dict_from_response_body
        except ValueError:
            # We may not have gotten valid JSON. In that case, do our best and just display something
            result_dict['data'] = response.text

        status = result_dict['data']['status']['state']['state']
        print("The import progress for task " + task_id + " is currently at status :" + status)
        return status


def get_service_endpoint(ctx, endpoint_param_name):
    """
    parse the endpoint that will be used for all diag API requests
    """
    endpoint = None
    if ctx.obj['default_values_from_file'] is not None and \
            ctx.obj['default_values_from_file'].get(endpoint_param_name) is not None:
        endpoint = ctx.obj['default_values_from_file'].get(endpoint_param_name)
    if ctx.obj['endpoint']:
        endpoint = ctx.obj['endpoint']
    if endpoint is None:
        raise click.UsageError(
            f'Error: Missing option --endpoint.\nINFO: set {endpoint_param_name} in oci_cli_rc file or add command line option --endpoint')
    return endpoint


def parse_basic_auth_creds(ctx):
    if ctx.obj["config"].get("basic_auth_file") is None:
        raise click.UsageError("Basic Auth File Location Missing\n INFO: set basic_auth_file in oci config file")
    if ctx.obj["debug"]:
        click.echo("DEBUG: Rover Diagnostics Basic Auth File:" + ctx.obj["config"].get("basic_auth_file"))
    auth_creds = cli_util.load_file_contents(f"file://{ctx.obj['config'].get('basic_auth_file')}")
    user = None
    password = None
    for line in auth_creds.splitlines():
        user_test = re.match(r"^user\s+(\D.+)", line)
        pass_test = re.match(r"^password\s+(.+)", line)
        if user_test:
            user = user_test.group(1)
        if pass_test:
            password = pass_test.group(1)
    if user is None or password is None:
        raise click.UsageError(f"Diagnostic Service Basic Auth Credentials Not Found in basic_auth_file: {ctx.obj['config'].get('basic_auth_file')}")
    return (user, password)


def save_stream(response, filename):
    with click.progressbar(length=int(response.headers["content-length"]),
                           label="Downloading Rover Diagnostic Bundle",
                           file=sys.stderr) as bar:
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=2048):
                if chunk:
                    f.write(chunk)
                    bar.update(2048)
        bar.finished = True
        bar.render_finish()


def _print_debug_info(**kwargs):
    debug_info = {}
    if kwargs.get("type") == "request":
        click.echo("Sending request.......")
        debug_info["headers"] = dict(kwargs.get("session").headers)
        debug_info["method"] = kwargs.get("method")
        debug_info["url"] = kwargs.get("url", "").split("?")[0]
        debug_info["queryParams"] = kwargs.get("params", {})

    elif kwargs.get("type") == "response":
        click.echo("Receiving response......")
        debug_info["headers"] = {key: value for (key, value) in kwargs.get("response").headers.items()}
        debug_info["reason"] = kwargs.get("response").reason
        debug_info["status_code"] = kwargs.get("response").status_code
        debug_info["url"] = kwargs.get("url")

    click.echo(cli_util.pretty_print_format((debug_info)))


def _make_rover_service_api_call(requests_session, http_method, url, params=None, data=None, stream=False, debug=False):
    if debug:
        _print_debug_info(type="request", session=requests_session, url=url, method=http_method,
                          params=params, data=data)

    start = timer()
    service_api_strategy = RetryStrategyBuilder(total_elapsed_time_seconds=120).get_retry_strategy()
    try:
        response = service_api_strategy.make_retrying_call(
            requests_session.request,
            method=http_method,
            url=url,
            json=data,
            stream=stream
        )
    except Exception as e:
        click.echo(f"ERROR: Rover Service API Error: {(e)}")
        if debug:
            raise e

    try:
        end = timer()
        response.raise_for_status()
        if debug:
            _print_debug_info(type="response", url=url, response=response)
            click.echo(('DEBUG: Rover Service: time elapsed for request: {:.2f} secs'.format((end - start))))
        return response

    except Exception as e:
        click.echo(f"ERROR: Rover Service API Error: {cli_util.pretty_print_format(response.json())}")
        if debug:
            click.echo(f"DEBUG: Rover Service: REQUEST URL: {response.request.url}")
            click.echo(f"DEBUG: Rover Service: REQUEST HEADERS: {response.request.headers}")
            raise e


def monitor_bundle_state(requests_session, wait, url, params=None, debug=False):
    start_time = time.time()
    count = 1
    while True:
        response = _make_rover_service_api_call(requests_session, "POST", url, params=params, data={}, debug=debug)
        current_state = response.json()["nodes"][0]["lifecycleState"]
        if current_state in wait["state"]:
            return response.json()

        elapsed_seconds = (time.time() - start_time)

        if elapsed_seconds > wait["max_wait_seconds"]:
            click.echo("Maximum wait time has been exceeded for diagnostic bundle. Currently in state:{current_state}, waiting for state(s): {wait['state']}")
            sys.exit(-1)

        if debug:
            result_dict = {
                'status': '{} {}'.format(response.status_code, response.reason),
                'headers': {key: value for (key, value) in response.headers.items()}
            }
            result_dict['data'] = response.json()

            click.echo(cli_util.pretty_print_format(result_dict))
        if count == 1:
            click.echo(f"\nAction completed. Waiting until the resource has entered state: {wait['state']}")
        if debug:
            click.echo(f"DEBUG: Rover Diagnostics: Checked state {count} time(s)")

        count += 1
        time.sleep(wait["interval_seconds"])


def dispatch_diag_request(ctx, additional_url_path="", params=None, basic_auth=False,
                          http_method=None, data=None, stream=False,
                          stream_file_location=None, wait=None):
    url = get_service_endpoint(ctx,
                               'diagnostics.endpoint') + ROVER_DIAGNOSTIC_BUNDLE_API_BASE_PATH + "/" + additional_url_path

    with cli_util.build_raw_requests_session(ctx) as requests_session:
        # if basic_auth is needed we need to obtain the user/pass information from file
        # located in the oci config file attribute of basic_auth_file
        if params:
            requests_session.params.update(params)
        if basic_auth:
            requests_session.auth = parse_basic_auth_creds(ctx)

        response = _make_rover_service_api_call(requests_session, http_method, url, params,
                                                data, stream, ctx.obj["debug"])

        if response:
            result_dict = {
                'status': '{} {}'.format(response.status_code, response.reason),
                'headers': {key: value for (key, value) in response.headers.items()}
            }
        if not stream:
            try:
                dict_from_response_body = response.json()
                result_dict['data'] = dict_from_response_body
            except ValueError:
                # We may not have gotten valid JSON. In that case, do our best and just display something
                result_dict['data'] = response.text
            if wait is not None:
                if http_method == "DELETE" or \
                   dict_from_response_body['nodes'][0]['lifecycleState'] not in wait["state"]:
                    if http_method == "DELETE":
                        bundle_id = additional_url_path
                    else:
                        bundle_id = dict_from_response_body["id"]

                    monitor_url = get_service_endpoint(ctx,
                                                       'diagnostics.endpoint') + ROVER_DIAGNOSTIC_BUNDLE_API_BASE_PATH + "/" + bundle_id + "/actions/viewSummary"

                    click.echo(cli_util.pretty_print_format(monitor_bundle_state(requests_session,
                                                                                 wait,
                                                                                 monitor_url,
                                                                                 params=params,
                                                                                 debug=ctx.obj["debug"])))

            else:  # no wait and no stream - just print the latest API Call response
                if http_method != "DELETE":
                    cli_util.render_response(RoverDiagAPI(data=result_dict["data"], headers=result_dict["headers"]), ctx)
                else:
                    if ctx.obj["debug"]:
                        cli_util.render_response(RoverDiagAPI(data=result_dict["data"], headers=result_dict["headers"]), ctx)

        else:
            save_stream(response, stream_file_location)


def dispatch_datasync_request(ctx, base_path, additional_url_path="", params=None, http_method=None, data=None,
                              print_response=True):
    url = get_service_endpoint(ctx, 'data-sync.endpoint') + base_path + "/" + additional_url_path

    with cli_util.build_raw_requests_session(ctx) as requests_session:
        if params:
            requests_session.params.update(params)

        response = _make_rover_service_api_call(requests_session, http_method, url, params,
                                                data, False, ctx.obj["debug"])

        result_dict = {}
        if response is not None:
            result_dict['status'] = '{} {}'.format(response.status_code, response.reason)
            result_dict['headers'] = {key: value for (key, value) in response.headers.items()}

            try:
                dict_from_response_body = response.json()
                result_dict['data'] = dict_from_response_body
            except ValueError:
                # We may not have gotten valid JSON. In that case, do our best and just display something
                result_dict['data'] = response.text

            if print_response:
                cli_util.render_response(RoverDiagAPI(data=result_dict["data"], headers=result_dict["headers"]), ctx)

            return result_dict["data"]
        return None


def read_json_file(filepath):
    with open(filepath, 'r') as jsonfile:
        data = jsonfile.read()

    # parse file
    return json.loads(data)


def read_json_string(json_string):
    return json.loads(json_string)


def bundle_decrypt(in_file, out_file, key):
    bkey = bytes.fromhex(key.ljust(32, '0'))
    enc_data = Path(in_file).read_bytes()
    alg = algorithms.AES(bkey)
    mode = modes.CBC(bkey)
    cipher = Cipher(alg, mode, backend=default_backend())
    decryptor = cipher.decryptor()
    pad_dec_data = decryptor.update(enc_data) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    dec_data = unpadder.update(pad_dec_data) + unpadder.finalize()
    Path(out_file).write_bytes(dec_data)


def construct_request_headers(object_name):
    result_dict = {
        "object-name": object_name
    }
    return result_dict


def check_if_state_matches(state, list_of_states):
    return any(state in x for x in list_of_states)


class ProgressBar:
    PROGRESS_BAR_GRANULARITY = 10000

    def __init__(self, total_bytes, label, next_part=None):
        self._total_bytes = 1 if total_bytes == 0 else total_bytes
        self._total_progress_bytes = 0
        self._last_progress = 0
        self._progressbar = click.progressbar(length=ProgressBar.PROGRESS_BAR_GRANULARITY,
                                              label=label, file=sys.stderr)
        # To synchronize as same progressbar is being shared between the threads
        self._semaphore = WrappedSemaphore(1)

    def __enter__(self):
        self._progressbar.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self._progressbar.__exit__(exc_type, exc_value, tb)

    def update(self, bytes_read):
        self._total_progress_bytes += bytes_read
        current_progress = ProgressBar.PROGRESS_BAR_GRANULARITY * (float(self._total_progress_bytes) / self._total_bytes)
        if current_progress != self._last_progress:
            self._progressbar.update(current_progress - self._last_progress)
            self._last_progress = current_progress

    def update_indeterminate_size(self, bytes_read):
        self._total_progress_bytes += bytes_read

        # This should make the bar wrap around itself (i.e. it gets to the end and then resets)
        if self._total_progress_bytes >= self._total_bytes:
            self.reset_progress(self._total_bytes, self._progressbar.label)

        self.update(bytes_read)

    def reset_progress(self, total_bytes, new_label):
        self._semaphore.acquire()
        self._progressbar.label = new_label
        self._progressbar.pos = 0
        self._progressbar.avg = []
        self._progressbar.finished = False

        self._total_bytes = total_bytes
        self._last_progress = 0
        self._total_progress_bytes = 0
        self._semaphore.release()

    def update_label_to_end(self, new_label):
        self._semaphore.acquire()
        self._progressbar.label = new_label
        self._progressbar.finished = True
        self._progressbar.render_progress()
        print()
        self._semaphore.release()

    def render_finish(self):
        self._progressbar.render_finish()
