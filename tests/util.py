# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import functools
import json
import random
import os
import pytest
import six
import time
import traceback
from click.testing import CliRunner
import oraclebmc_cli.cli_util
import oraclebmc
from oraclebmc.object_storage.transfer.constants import MEBIBYTE

try:
    # PY3+
    import collections.abc as abc
except ImportError:
    # PY2
    import collections as abc

TEST_DATA_VERSION = '1'

USER_ID = os.environ['BMCS_CLI_USER_ID']
TENANT_ID = os.environ['BMCS_CLI_TENANT_ID']
COMPARTMENT_ID = os.environ['BMCS_CLI_COMPARTMENT_ID']
COMPARTMENT_NAME = os.environ['BMCS_CLI_COMPARTMENT_NAME']
AVAILABILITY_DOMAIN = os.environ['BMCS_CLI_AD']
NAMESPACE = os.environ['BMCS_CLI_NAMESPACE']
SSH_AUTHORIZED_KEYS_FILE = os.environ['BMCS_CLI_PUBLIC_SSH_KEY_FILE']


# Tests marked with @slow will only be skipped if '--fast' is specified for the test run.
slow = pytest.mark.skipif(
    pytest.config.getoption("--fast"),
    reason="Slow tests are skipped when using the --fast option."
)


def random_name(prefix, insert_underscore=True):
    return prefix + ('_' if insert_underscore else '') + str(random.randint(0, 1000000))


def find_id_in_response(response):
    """Finds the ID of the response data. Response must be JSON."""
    try:
        return json.loads(response)['data']['id']
    except Exception:
        raise RuntimeError("Could not parse id from json response: " + response)


def remove_outer_quotes(text):
    if (text.startswith("'") and text.endswith("'")):
        return text[1:-1]
    else:
        return text


def validate_response(result, extra_validation=None, includes_debug_data=False, json_response_expected=True, expect_etag=False):
    try:
        assert result.exit_code == 0

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
        print(result.output)
        raise


def validate_service_error(result, error_message=None, debug=False):
    try:
        assert result.exit_code != 0
        if debug:
            assert isinstance(result.exception, oraclebmc.exceptions.ServiceError)
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
    return CliRunner().invoke(oraclebmc_cli.cli, ['--config-file', os.environ['BMCS_CLI_CONFIG_FILE'], '--profile', 'ADMIN'] + command, ** args)


def invoke_command(command, ** args):
    return CliRunner().invoke(oraclebmc_cli.cli, ['--config-file', os.environ['BMCS_CLI_CONFIG_FILE']] + command, ** args)


def wait_until(get_command, state, max_wait_seconds=30, max_interval_seconds=15, succeed_if_not_found=False, item_index_in_list_response=None):
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
                if json.loads(result.output)['data'][item_index_in_list_response]['lifecycle-state'] == state:
                    break
            elif json.loads(result.output)['data']['lifecycle-state'] == state:
                break

        time.sleep(sleep_interval_seconds)

        # Double the sleep each time up to the maximum.
        sleep_interval_seconds = min(sleep_interval_seconds * 2, max_interval_seconds)

        elapsed_seconds = (time.time() - start_time)

        if elapsed_seconds + sleep_interval_seconds > max_wait_seconds:
            if max_wait_seconds <= elapsed_seconds:
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
    such as ["bmcs", "iam", "user", "list"]."""
    prefix = prefix or []
    subcommands = getattr(command, "commands", {})

    if subcommands:
        if not leaf_commands_only:
            yield prefix

        for name, command in six.iteritems(subcommands):
            for path in collect_commands(command, prefix + [name], leaf_commands_only=leaf_commands_only):
                yield path
    else:
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
    The one exception is metadata dictionaries, which must reflect user
    input"""
    if isinstance(json_data, six.string_types):
        pass
    elif isinstance(json_data, abc.Mapping):
        for key, value in six.iteritems(json_data):
            if key != "metadata":
                assert "_" not in key
                assert key.islower()
                check_json_key_format(value)
    elif isinstance(json_data, abc.Iterable):
        for item in json_data:
            check_json_key_format(item)


def set_admin_pass_phrase():
    oraclebmc_cli.cli_util.build_config = build_config_decorator(oraclebmc_cli.cli_util.build_config)


def unset_admin_pass_phrase():
    if hasattr(oraclebmc_cli.cli_util.build_config, 'original_method'):
        oraclebmc_cli.cli_util.build_config = oraclebmc_cli.cli_util.build_config.original_method


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
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket1',
                  objects=['object1', 'object2', 'object3', 'object4', 'object5'])
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket2',
                  objects=['a/b/c/object1', 'a/b/c/object2', 'a/b/c/object3', 'a/b/object4', 'a/b/object5'])
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket3', objects=['a/b/object1'])
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket4')
    create_object(api, namespace, bucket_prefix + 'ReadOnlyTestBucket4', 'reallyLargeFile.dat', file_name='data/reallyLargeFile.dat')
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket5', {'foo1': 'bar1', 'foo2': 'bar2'})
    create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket6')

    for num in range(1, 213):
        create_object(api, namespace, bucket_prefix + 'ReadOnlyTestBucket6', 'ob' + str(num))

    for num in range(7, 209):
        create_bucket(api, namespace, compartment, bucket_prefix + 'ReadOnlyTestBucket' + str(num))

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


def create_bucket(api, namespace, compartment, bucket_name, metadata=None, objects=None):
    """Deletes all buckets and objects in the given compartment."""
    request = oraclebmc.object_storage.models.CreateBucketDetails()
    request.name = bucket_name
    request.compartment_id = compartment
    request.metadata = metadata
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


def clear_test_data(api, namespace, compartment, bucket_prefix):
    print('Deleting test data.')
    bucket_list = []
    next_page = None
    count = 0
    while True:
        if next_page:
            response = api.list_buckets(namespace, compartment, page=next_page)
        else:
            response = api.list_buckets(namespace, compartment)

        bucket_list.extend([bucket.name for bucket in response.data])

        count += 1
        if count > 100:
            raise RuntimeError("Too many pages, something is probably wrong.")

        if not response.has_next_page:
            break
        next_page = response.next_page

    for bucket in bucket_list:
        # only delete buckets starting with prefix (i.e. CliReadOnlyTestBucket)
        if bucket_prefix not in bucket:
            continue

        object_list = []
        next_start = None
        count = 0
        while True:
            if next_start:
                response = api.list_objects(namespace, bucket, start=next_start)
            else:
                response = api.list_objects(namespace, bucket)

            object_list.extend([obj.name for obj in response.data.objects])

            count += 1
            if count > 100:
                raise RuntimeError("Too many pages, something is probably wrong.")

            next_start = response.data.next_start_with
            if next_start is None:
                break

        for obj in object_list:
            api.delete_object(namespace, bucket, obj)

        api.delete_bucket(namespace, bucket)
        show_progress()


def show_progress():
    print('.', end='', flush=True)


def create_large_file(filename, size_in_mebibytes):
    sample_content = b'a'
    with open(filename, 'wb') as f:
        f.write(sample_content * MEBIBYTE * size_in_mebibytes)
