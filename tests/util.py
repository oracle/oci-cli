# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function

import collections.abc as abc
import contextlib
import functools
import json
import os
import random
import sys
import time
import traceback
from inspect import getsourcefile
from os.path import abspath

import oci
import pytest
import six
from oci.object_storage.transfer.constants import MEBIBYTE
from six import StringIO

import oci_cli.cli_util
from conftest import runner
from oci_cli.dynamic_loader import ALL_SERVICES_DIR
from . import test_config_container
from oci_cli.service_mapping import service_mapping
from common_util import ignored_commands

TEST_DATA_VERSION = '1'

NUM_INVOKE_COMMAND_RETRIES = 3

WAIT_INTERVAL_SECONDS = '30' if test_config_container.vcr_mode != 'none' else '0'

USER_ID = os.environ['OCI_CLI_USER_ID']
ADMIN_USER_ID = os.environ['OCI_CLI_ADMIN_USER_ID']
TENANT_ID = os.environ['OCI_CLI_TENANT_ID']
COMPARTMENT_ID = os.environ['OCI_CLI_COMPARTMENT_ID']
COMPARTMENT_NAME = os.environ['OCI_CLI_COMPARTMENT_NAME']
NAMESPACE = os.environ['OCI_CLI_NAMESPACE']
SSH_AUTHORIZED_KEYS_FILE = os.environ['OCI_CLI_PUBLIC_SSH_KEY_FILE']
OS_REPLICATION_DESTINATION_REGION = 'us-phoenix-1'

# Currently used for serial console validation
SSH_AUTHORISED_KEY_FINGERPRINT = os.environ['OCI_CLI_PUBLIC_SSH_KEY_FINGERPRINT']

REGIONAL_CONFIG = {
    'us-phoenix-1': {
        'bucket_regional_prefix': '',
        'windows_vm_image': 'ocid1.image.oc1.phx.aaaaaaaa53cliasgvqmutflwqkafbro2y4ywjebci5szc4eus5byy2e2b7ua',
        'oracle_linux_image': 'ocid1.image.oc1.phx.aaaaaaaaxyc7rpmh3v4yyuxcdjndofxuuus4iwd7a7wjc63u2ykycojr5djq'},
    'us-ashburn-1': {
        'bucket_regional_prefix': 'iad_',
        'windows_vm_image': 'ocid1.image.oc1.iad.aaaaaaaatob7wb2ljtvsvjy7olpsyuttodb7ok3osflx3hqd2nt4l6jagxla',
        'oracle_linux_image': 'ocid1.image.oc1.iad.aaaaaaaazq7xlunevyn3cf4wppcx2j53eb26pnnc4ukqtfj4tbjjcklnhpaa'}
}

PROFILE_TO_REGION = {
    'ADMIN': 'us-phoenix-1',
    oci.config.DEFAULT_PROFILE: 'us-phoenix-1',
    'IAD': 'us-ashburn-1'
}

LARGE_FILE_NAME = 'reallyLargeFile.dat'
LARGE_FILE_LOCATION = os.path.join('data', LARGE_FILE_NAME)

# The check_json_key_format method validates that keys are snake-cased and all in lower case
# (e.g. this-is-a-valid-key, ButThisIsNot, And_neither_is_this). However, there are exceptions such
# as where the key is sourced directly from user input (e.g. metadata, tagging) and we should
# preserve these as-is rather than imposing our rules
SKIP_JSON_KEY_FORMAT_CHECK = set([
    "metadata",
    "extended-metadata",
    "backend-sets",
    "certificates",
    "default-backend-set-name",
    "defined-tags",
    "freeform-tags",
    "cdbDefault"  # This is for test_database.py
])


# This allows generated tests to look up operations that have been moved in code in the CLI.
# It is populated by the code that follows.
MOVED_COMMANDS = {
}
# This dynamically adds the generated test operation subsitutions from the extended file.
# This will process files under the generated_test_extensions that are named "extend_test*.py".
# If those files have a "MOVED_COMMANDS" dictionary defined in them, they will be added to the
# MOVED_COMMANDS dictionary defined above.
this_file_path = abspath(getsourcefile(lambda: 0))
python_cli_root_dir = this_file_path[:-14]  # chop off "/tests/util.py"
for service_dir in os.listdir(python_cli_root_dir + '/' + ALL_SERVICES_DIR):
    test_dir = os.path.join(python_cli_root_dir, ALL_SERVICES_DIR, service_dir, 'tests')
    if os.path.isdir(test_dir):
        for file in os.listdir(test_dir):
            if "extend_test" in file:
                try:
                    extend_test_module = __import__("services." + service_dir + ".tests." + file[:-3], fromlist=['MOVED_COMMANDS'])
                    MOVED_COMMANDS.update(extend_test_module.MOVED_COMMANDS)
                except Exception:
                    pass
            if "generated_test_request_transformers" in file:
                try:
                    __import__("services." + service_dir + ".tests." + file[:-3])
                except Exception:
                    pass

# This global can be changed to influence what configuration data this module vends.
target_region = PROFILE_TO_REGION[pytest.config.getoption("--config-profile")]

# Primary and secondary availability domains used as part of the tests
first_ad = None
second_ad = None

# Tests marked with @slow will only be skipped if '--fast' is specified for the test run.
slow = pytest.mark.skipif(
    pytest.config.getoption("--fast"),
    reason="Slow tests are skipped when using the --fast option."
)


def availability_domain():
    init_availability_domain_variables()
    return first_ad


def second_availability_domain():
    init_availability_domain_variables()
    return second_ad


def init_availability_domain_variables():
    global first_ad, second_ad
    with test_config_container.create_vcr().use_cassette('initialize_availability_domains.yml'):
        if first_ad is None or second_ad is None:
            first_ad, second_ad = retrieve_availability_domains()


def retrieve_availability_domains():
    response = invoke_command(['iam', 'availability-domain', 'list', '--compartment-id', TENANT_ID])
    availability_domains = json.loads(response.output)['data']

    if len(availability_domains) == 1:
        first_availability_domain = availability_domains[0]['name']
        second_availability_domain = availability_domains[0]['name']
    elif len(availability_domains) == 2:
        first_availability_domain = availability_domains[0]['name']
        second_availability_domain = availability_domains[1]['name']
    else:
        # We need consistency in the vended availability domains if we're mocking, so don't randomize
        if test_config_container.using_vcr_with_mock_responses():
            first_availability_domain = availability_domains[0]['name']
            second_availability_domain = availability_domains[1]['name']
        else:
            chosen_domains = random.sample(availability_domains, 2)
            first_availability_domain = chosen_domains[0]['name']
            second_availability_domain = chosen_domains[1]['name']
    return first_availability_domain, second_availability_domain


# long running tests are marked with @util.long_running
# using --enable-long-running will run all of the tests *including* long_running ones
# using -m long_running will *only* run long running tests
def long_running(func):
    def internal(function):
        return pytest.mark.skipif(
            not pytest.config.getoption("--enable-long-running"),
            reason="Long running tests are only run when specifically asked for"
        )(function)

    if pytest.config.getoption('-m') == 'long_running':
        return pytest.mark.long_running(func)
    else:
        return pytest.mark.long_running(internal(func))


# Along with long running tests, tests which are marked with @util.skip_while_rerecording
# will not be executed when using --run-recordable-tests-only.
def skip_while_rerecording(func):
    def internal(function):
        return pytest.mark.skipif(
            pytest.config.getoption("--run-recordable-tests-only"),
            reason="These tests are not run when with the run-recordable-tests-only option."
        )(function)

    return pytest.mark.skip_while_rerecording(internal(func))


def instance_principals(func):
    def internal(function):
        return pytest.mark.skipif(
            not pytest.config.getoption("--instance-principals"),
            reason="These tests are only run with the instance-principals option."
        )(function)

    return pytest.mark.instance_principals(internal(func))


def random_name(prefix, insert_underscore=True):
    if test_config_container.using_vcr_with_mock_responses():
        return prefix + ('_' if insert_underscore else '') + 'vcr'
    else:
        return prefix + ('_' if insert_underscore else '') + str(random.randint(0, 1000000))


def random_number_string():
    if test_config_container.using_vcr_with_mock_responses():
        return '10000'
    else:
        return str(random.randint(0, 10000))


def bucket_regional_prefix():
    return REGIONAL_CONFIG[target_region]['bucket_regional_prefix']


def oracle_linux_image():
    return REGIONAL_CONFIG[target_region]['oracle_linux_image']


def windows_vm_image():
    return REGIONAL_CONFIG[target_region]['windows_vm_image']


def find_id_in_response(response):
    """Finds the ID of the response data. Response must be JSON."""
    try:
        return json.loads(response)['data']['id']
    except Exception:
        raise RuntimeError("Could not parse id from json response: " + response)


def remove_outer_quotes(text):
    if text.startswith("'") and text.endswith("'"):
        return text[1:-1]
    else:
        return text


def validate_response(result, extra_validation=None, includes_debug_data=False, json_response_expected=True, expect_etag=False):
    try:
        assert result.exit_code == 0 or result.exit_code is None

        if includes_debug_data:
            assert 'opc-request-id' in result.output
            assert 'opc-client-info' in result.output
            assert 'Oracle-PythonCLI/' in result.output
            assert 'user-agent' in result.output
            assert '200' in result.output or '204' in result.output
        elif json_response_expected:
            validate_json_response(result.output)

        if expect_etag:
            assert "etag" in result.output

        if extra_validation:
            extra_validation(result)

    except AssertionError:
        if result and hasattr(result, 'output'):
            print("validate_response response output=" + result.output)
        else:
            print("validate_response response=" + str(result))
        raise


def validate_service_error(result, error_message=None, debug=False):
    try:
        assert result.exit_code != 0
        if debug:
            assert isinstance(result.exception, oci.exceptions.ServiceError)
            if error_message:
                assert error_message in str(result.exception)
        else:
            if error_message:
                assert error_message in result.output
    except AssertionError:
        # TODO better inspection for failing tests
        print(result.output)
        raise


def invoke_command_as_admin(command, ** args):
    num_tries = 0

    while num_tries < NUM_INVOKE_COMMAND_RETRIES:
        command_output = runner().invoke(oci_cli.cli, ['--config-file', os.environ['OCI_CLI_CONFIG_FILE'], '--profile', 'ADMIN'] + command, ** args)

        if command_output.exception:
            output_to_test = str(command_output.exception)
        else:
            output_to_test = command_output.output

        if should_retry(output_to_test):
            num_tries += 1
            if num_tries >= NUM_INVOKE_COMMAND_RETRIES:
                return command_output
            else:
                time.sleep(2 ** num_tries)  # Backoff
                time.sleep(random.random() * 2)  # Jitter
        else:
            return command_output

    # Always return some sort of output so that the test can handle it (or try and do something). Retries are
    # a bit strange here because we don't get exceptions (as such) but they are instead dumped out into the
    # terminal
    return command_output


def invoke_command(command, ** args):
    num_tries = 0

    while num_tries < NUM_INVOKE_COMMAND_RETRIES:
        command_output = runner().invoke(oci_cli.cli, ['--config-file', os.environ['OCI_CLI_CONFIG_FILE'], '--profile', pytest.config.getoption("--config-profile")] + command, ** args)

        if command_output.exception:
            output_to_test = str(command_output.exception)
        else:
            output_to_test = command_output.output

        if should_retry(output_to_test):
            num_tries += 1
            if num_tries >= NUM_INVOKE_COMMAND_RETRIES:
                return command_output
            else:
                time.sleep(2 ** num_tries)  # Backoff
                time.sleep(random.random() * 2)  # Jitter
        else:
            return command_output

    return command_output


def invoke_command_with_overrides(command, profile_override, ** args):
    num_tries = 0

    if profile_override != '':
        command = ['--profile', profile_override] + command

    while num_tries < NUM_INVOKE_COMMAND_RETRIES:
        command_output = runner().invoke(oci_cli.cli, command, ** args)

        if command_output.exception:
            output_to_test = str(command_output.exception)
        else:
            output_to_test = command_output.output

        if should_retry(output_to_test):
            num_tries += 1
            if num_tries >= NUM_INVOKE_COMMAND_RETRIES:
                return command_output
            else:
                time.sleep(2 ** num_tries)  # Backoff
                time.sleep(random.random() * 2)  # Jitter
        else:
            return command_output

    return command_output


def invoke_command_with_auth(command, ** args):
    num_tries = 0

    while num_tries < NUM_INVOKE_COMMAND_RETRIES:
        command_output = runner().invoke(oci_cli.cli, ['--auth', os.environ['OCI_CLI_AUTH']] + command, **args)

        if command_output.exception:
            output_to_test = str(command_output.exception)
        else:
            output_to_test = command_output.output

        if should_retry(output_to_test):
            num_tries += 1
            if num_tries >= NUM_INVOKE_COMMAND_RETRIES:
                return command_output
            else:
                time.sleep(2 ** num_tries)  # Backoff
                time.sleep(random.random() * 2)  # Jitter
        else:
            return command_output

    return command_output


def wait_until(get_command, state, max_wait_seconds=30, max_interval_seconds=15, succeed_if_not_found=False, item_index_in_list_response=None, state_property_name='lifecycle-state'):
    """Poll the given get command until the result has a lifecycle-state that matches the given state.
    The Polling interval will double with each call until max_interval_seconds is reached."""
    sleep_interval_seconds = 1
    start_time = time.time()
    result = None

    while (True):
        result = invoke_command(get_command)

        if result.exit_code != 0:
            if succeed_if_not_found and "404" in result.output:
                break
            else:
                raise RuntimeError('Error while waiting for state: ' + str(result.exception))

        # if an index is supplied, check the state of the corresponding item in the list
        if result.output:
            if item_index_in_list_response is not None:
                if json.loads(result.output)['data'][item_index_in_list_response][state_property_name] == state:
                    break
            elif json.loads(result.output)['data'][state_property_name] == state:
                break

        if test_config_container.vcr_mode != 'none':
            time.sleep(sleep_interval_seconds)

        # Double the sleep each time up to the maximum.
        sleep_interval_seconds = min(sleep_interval_seconds * 2, max_interval_seconds)

        elapsed_seconds = (time.time() - start_time)

        if elapsed_seconds + sleep_interval_seconds > max_wait_seconds:
            if max_wait_seconds <= elapsed_seconds:
                if result.output:
                    print("wait_until result.output=" + str(result.output))
                raise RuntimeError('Maximum wait time has been exceeded.')

    return result


def print_latest_exception(exception):
    print("ERROR {type}: {message}".format(type=exception.__class__.__name__, message=str(exception)))
    traceback.print_exc()


def log_test(func):
    @functools.wraps(func)
    def wrapped_call(ctx, *args, **kwargs):
        print("Test {name}...".format(name=func.__name__))
        func(ctx, *args, **kwargs)
        print("Test {name} Complete".format(name=func.__name__))

    return wrapped_call


def collect_commands(command, prefix=None, leaf_commands_only=False):
    """Returns a list of commands under and including the given command.
        Each entry is a list of strings to invoke a particular command,
        such as ["oci", "iam", "user", "list"]."""
    for path, _, _ in _collect_commands(command, prefix, leaf_commands_only):
        yield path


def collect_leaf_commands_with_counts(command):
    """
     Returns a list of tuples (command, number of params, number of required params) for leaf commands.
    """
    return _collect_commands(command, None, True)


def _collect_commands(command, prefix=None, leaf_commands_only=False):
    """
    Returns a list of tuples (command, number of params, number of required params).
    Command is a list of all the strings required to invoke a particular command.
    The count of params and required params is 0 for non leaf commands.
    """
    prefix = prefix or []
    subcommands = getattr(command, "commands", {})

    if subcommands:
        if not leaf_commands_only:
            yield prefix, 0, 0

        for name, command in six.iteritems(subcommands):
            for path, params_count, req_params_count in \
                    _collect_commands(command, prefix + [name], leaf_commands_only=leaf_commands_only):
                yield path, params_count, req_params_count
    else:
        params_count = len(command.params)
        req_params_count = len(list(filter(lambda param: param.help.endswith(' [required]'), command.params)))

        yield prefix, params_count, req_params_count


def collect_commands_with_given_args(command, include_args=[], match_mode='any', prefix=None):
    prefix = prefix or []
    subcommands = getattr(command, "commands", {})

    if subcommands:
        for name, command in six.iteritems(subcommands):
            for path in collect_commands_with_given_args(command, include_args=include_args, match_mode=match_mode, prefix=prefix + [name]):
                yield path
    else:
        match_args = (match_mode == 'all')
        command_opts = []

        for p in command.params:
            command_opts.extend(p.opts)

        for a in include_args:
            if match_mode == 'any':
                if a in command_opts:
                    match_args = True
                    break
            else:
                if a not in command_opts:
                    match_args = False
                    break

        if match_args:
            yield prefix


def build_config_decorator(method):
    """Get the pass phrase from an environment variable and inject it into the config."""

    def decorate_build_config(command_args):
        client_config = method(command_args)
        pass_phrase = os.environ.get('CLI_TESTS_ADMIN_PASS_PHRASE', None)

        if not pass_phrase:
            print("To run these tests, you must provide the pass phrase "
                  "for the admin user key (key/admin_cli_integration_test_user_key) "
                  "in the environment variable CLI_TESTS_ADMIN_PASS_PHRASE.")

        client_config["pass_phrase"] = pass_phrase
        return client_config

    if hasattr(method, 'original_method'):
        # Already decorated
        return method
    else:
        decorate_build_config.original_method = method
        return decorate_build_config


def validate_json_response(data):
    """Ensure that data is either empty or valid JSON."""
    if len(data) > 0:
        json_data = json.loads(data)
        check_json_key_format(json_data)


def check_json_key_format(json_data):
    """Ensure that all keys in the json data are in the correct format.
    The exceptions include metadata dictionaries and tags, which must reflect user
    input"""
    if isinstance(json_data, six.string_types):
        pass
    elif isinstance(json_data, abc.Mapping):
        for key, value in six.iteritems(json_data):
            if key not in SKIP_JSON_KEY_FORMAT_CHECK:
                assert "_" not in key
                assert key.islower()
                check_json_key_format(value)
    elif isinstance(json_data, abc.Iterable):
        for item in json_data:
            check_json_key_format(item)


def set_admin_pass_phrase():
    oci_cli.cli_util.build_config = build_config_decorator(oci_cli.cli_util.build_config)


def unset_admin_pass_phrase():
    if hasattr(oci_cli.cli_util.build_config, 'original_method'):
        oci_cli.cli_util.build_config = oci_cli.cli_util.build_config.original_method


def ensure_test_data(api, namespace, compartment, bucket_prefix):
    """The test data will be deleted and recreated only if the version has changed."""
    test_data_metadata_bucket = bucket_prefix + '_test_metadata'
    test_data_version_object = 'test_data_version'

    # Check test data version.
    try:
        version = api.get_object(
            namespace,
            test_data_metadata_bucket,
            test_data_version_object).data.content.decode('UTF-8')

        if version == TEST_DATA_VERSION:
            return
    except Exception as error:
        # if either the _test_metadata bucket doesnt exist or the version object doesnt exist, we want to continue
        # and create new test data
        if error.status != 404:
            raise error

    print("Recreating test data.")
    clear_test_data(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket')

    print('Creating test data.')
    if not os.path.exists(LARGE_FILE_LOCATION):
        os.makedirs('data')
        create_large_file(LARGE_FILE_LOCATION, 100)

    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket1',
                  objects=['object1', 'object2', 'object3', 'object4', 'object5'])
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket2',
                  objects=['a/b/c/object1', 'a/b/c/object2', 'a/b/c/object3', 'a/b/object4', 'a/b/object5'])
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket3', objects=['a/b/object1'])
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket4')
    create_object(api, namespace, bucket_prefix + 'ReadOnlyTestBucket4', LARGE_FILE_NAME, file_name=LARGE_FILE_LOCATION)
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket5', {'foo1': 'bar1', 'foo2': 'bar2'})
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket6', versioning=True)

    for num in range(1, 213):
        create_object(api, namespace, bucket_prefix + 'ReadOnlyTestBucket6', 'ob' + str(num))

    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket7')
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket8')

    create_object(api, namespace, bucket_prefix + 'ReadOnlyTestBucket8', "a/b/c")
    create_object(api, namespace, bucket_prefix + 'ReadOnlyTestBucket8', "b/c")
    create_object(api, namespace, bucket_prefix + 'ReadOnlyTestBucket8', "f/b/c")
    create_object(api, namespace, bucket_prefix + 'ReadOnlyTestBucket8', "s/b/c")

    # Update test data version
    try:
        create_bucket(api, namespace, compartment, test_data_metadata_bucket)
    except Exception as error:
        # will get a 409 if the bucket already exists which we can safely ignore
        if error.status != 409:
            raise error

    api.put_object(namespace, test_data_metadata_bucket, test_data_version_object, TEST_DATA_VERSION)


def create_bucket(api, namespace, compartment, bucket_name, metadata=None, objects=None, versioning=False):
    """Deletes all buckets and objects in the given compartment."""
    request = oci.object_storage.models.CreateBucketDetails()
    request.name = bucket_name
    request.compartment_id = compartment
    request.metadata = metadata
    if versioning:
        request.versioning = 'Enabled'
    api.create_bucket(namespace, request)
    show_progress()

    if objects:
        for obj in objects:
            create_object(api, namespace, bucket_name, obj)


def create_object(api, namespace, bucket_name, object_name, file_name=None, metadata=None):
    args = {}
    if metadata:
        # TODO what is this for?
        args['opc_meta', metadata]
    if file_name:
        with open(file_name, 'rb') as file:
            api.put_object(namespace, bucket_name, object_name, file, **args)
    else:
        api.put_object(namespace, bucket_name, object_name, object_name, **args)

    show_progress()


CLEAN_UP_STATS = """
Finished deleting test data.
total_elapsed_time: {total_time}
total_objects: {obj_count}
total_buckets: {bucket_count}
"""


def clear_test_data(api, namespace, compartment, bucket_prefix):
    print('Deleting test data.')
    next_page = None
    list_bucket_page_count = 0
    object_count = 0
    bucket_count = 0
    start_time = time.time()
    while True:
        if next_page:
            response = api.list_buckets(namespace, compartment, page=next_page)
        else:
            response = api.list_buckets(namespace, compartment)
        for bucket in response.data:
            if bucket_prefix not in bucket.name:
                continue

            result = invoke_command(['os', 'bucket', 'delete', '--namespace', namespace, '--bucket-name', bucket.name,
                                     '--empty', '--force'])
            parsed_result = parse_json_response_from_mixed_output(result.output)
            bucket_count += 1
            object_count += len(parsed_result["object"]['deleted-objects'])
            show_progress()

        list_bucket_page_count += 1
        if list_bucket_page_count > 100:
            raise RuntimeError("Too many pages, something is probably wrong.")

        if not response.has_next_page:
            break
        next_page = response.next_page

    print(CLEAN_UP_STATS.format(
        total_time=str(time.time() - start_time),
        obj_count=object_count,
        bucket_count=bucket_count
    ))


def show_progress():
    try:
        print('.', end='', flush=True)
    except TypeError:
        print('.', end='')


def create_large_file(filename, size_in_mebibytes):
    sample_content = b'a'
    with open(filename, 'wb') as f:
        f.write(sample_content * MEBIBYTE * size_in_mebibytes)


def vcr_mode_aware_sleep(duration):
    if test_config_container.vcr_mode != 'none':
        time.sleep(duration)


@contextlib.contextmanager
def capture():
    oldout, olderr = sys.stdout, sys.stderr
    try:
        out = [StringIO(), StringIO()]
        sys.stdout, sys.stderr = out
        yield out
    finally:
        sys.stdout, sys.stderr = oldout, olderr
        out[0] = out[0].getvalue()
        out[1] = out[1].getvalue()


# We retry on:
#
#   - Timeouts
#   - Connection errors
#   - Internal server errors
#   - Throttles (HTTP 429)
#   - HTTP 409s which have a code of Conflict
def should_retry(command_output):
    if 'Timeout' in command_output or 'ConnectionError' in command_output:
        return True
    elif 'ServiceError' in command_output:
        # Note: This could also parse the output into JSON as the service error appears in a JSON structure, but
        # string checking seems to work OK for now
        if '"status": 5' in command_output or '429' in command_output:
            return True
        elif '409' in command_output:
            return 'Conflict' in command_output
        else:
            return False
    else:
        return False


def get_json_from_mixed_string(source_string):
    lines = source_string.split('\n')
    json_str = ''
    object_begun = False
    for line in lines:
        if object_begun or line.startswith('{'):
            object_begun = True
            json_str += line

    return json.loads(json_str)


def get_command_list(root_command, parent, leaf, multiple_tags=False):
    command_id_tuple = (root_command, parent, leaf)
    if command_id_tuple in MOVED_COMMANDS:
        return MOVED_COMMANDS[(root_command, parent, leaf)]
    # for spec with multiple tags, we just have to check if the passed tuple(root_command, parent, leaf) is a subset of
    # any of the MOVED commands keys since we do not have the newly added nested root group info.
    if multiple_tags:
        for cmd in MOVED_COMMANDS:
            if set(command_id_tuple).issubset(cmd):
                return MOVED_COMMANDS[cmd]

    parent = parent.replace('_', '-')
    leaf = leaf.replace('_', '-')

    commands = collect_commands(oci_cli.cli)
    for command in commands:
        if (len(command) > 2
                and ((multiple_tags and command[1] == root_command) or command[0] == root_command)
                and command[-2] == parent
                and command[-1] == leaf):
            # Find matching command and return. The second condition above is explained as below with examples:
            # spec with single tags e.g. iam: command[0](iam) == root_command(iam) is True
            # spec with multiple tags e.g. kms: multiple_tags and command[1](kmsCrypto) == root_command(kmsCrypto) is True
            # spec with multiple tags and root group removed e.g. core: command[0](compute) == root_command(compute) is True
            return command


# TODO: This is a temporary fix for overriding variables returned by the testing service.
# This table is repeated here from OracleCodegenHelper.java in the codegen repository
# Please remove this table and subsequent function once the fix has been implemented in the testing service.
VARIABLE_NAME_OVERRIDES = {
    "dataStorageSizeInTBs": "dataStorageSizeInTbs",
    "sizeInMBs": "sizeInMbs",
    "dataStorageSizeInGBs": "dataStorageSizeInGbs",
    "sizeInGBs": "sizeInGbs",
    "uniqueSizeInGBs": "uniqueSizeInGbs",
    "bootVolumeSizeInGBs": "bootVolumeSizeInGbs",
    "dbDataSizeInMBs": "dbDataSizeInMbs",
    "query": "queryText"
}


def variable_name_override(key):
    return VARIABLE_NAME_OVERRIDES.get(key, None)


def abort_multipart_uploading(api, namespace, bucket_name):
    multipart_uploads_list = api.list_multipart_uploads(namespace, bucket_name)
    for multipart_upload in multipart_uploads_list.data:
        api.abort_multipart_upload(namespace, bucket_name, multipart_upload.object, multipart_upload.upload_id)


# Trivial object to provide dictionary and dot accessor capabilities
class Obj(dict):
    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Obj, self).__setitem__(key, value)
        self.__dict__.update({key: value})


# Pull JSON data out of output which may have stuff other than JSON in it. Assumes that nothing
# comes after the JSON data
def parse_json_response_from_mixed_output(output):
    lines = output.split('\n')
    json_str = ''
    object_begun = False
    for line in lines:
        if object_begun or line.startswith('{'):
            object_begun = True
            json_str += line
    return json.loads(json_str)


COMMANDS_LIST = [cmd for cmd in sorted(collect_commands(oci_cli.cli, leaf_commands_only=True))]


def find_service_name_from_command(command, service_name):
    if command[0] in service_mapping and service_mapping[command[0]][0] == service_name:
        return command
    else:
        return None


def filter_commands_list(service):
    service_commands_list = []
    commands_list_all = [cmd for cmd in COMMANDS_LIST if cmd not in ignored_commands.IGNORED_COMMANDS]
    if service == 'all':
        return commands_list_all
    else:
        for command in commands_list_all:
            service_cmd_name = find_service_name_from_command(command, service)
            if service_cmd_name:
                service_commands_list.append(service_cmd_name)
        return service_commands_list
