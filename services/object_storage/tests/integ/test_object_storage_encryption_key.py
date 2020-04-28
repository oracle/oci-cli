# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import base64
import click
import os
import os.path
import pytest
import re
import oci_cli
from tests import util
from tests import test_config_container
import random

CASSETTE_LIBRARY_DIR = 'services/object_storage/tests/cassettes'
CONTENT_INPUT_FILE = 'tests/resources/content_input.txt'
GENERATED_ENC_KEY1_FILE = 'tests/temp/generated_enc_key1.txt'
GENERATED_ENC_KEY2_FILE = 'tests/temp/generated_enc_key2.txt'
GENERATED_CONTENT_INPUT_FILE = 'tests/temp/generated_content_input.txt'
CONTENT_OUTPUT_FILE = 'tests/resources/content_output.txt'
LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES = 5
DEFAULT_TEST_PART_SIZE = 2
MOVE_BUCKET_TO_COMPARTMENT_ID = os.environ.get('OCI_CLI_MOVE_BUCKET_TO_COMPARTMENT_ID')


@pytest.fixture
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette(
            'object_storage_encryption_key_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture
def content_input_file():
    return GENERATED_CONTENT_INPUT_FILE


@pytest.fixture(params=[True, False])
def multipart(request):
    return request.param


@pytest.fixture(params=[True, False])
def debug(request):
    return request.param


@pytest.fixture(scope='module', autouse=True)
def test_data(object_storage_client):
    # Setup test data
    util.ensure_test_data(object_storage_client, util.NAMESPACE, util.COMPARTMENT_ID,
                          util.bucket_regional_prefix() + 'Cli')


def generate_aes256_key_str():
    key = os.urandom(32)
    return base64.b64encode(key).decode('utf-8')


def setup_function():
    if os.path.exists(CONTENT_OUTPUT_FILE):
        os.remove(CONTENT_OUTPUT_FILE)


def setup_module():
    if os.getenv('RECORD_ONLY', '') == '1':
        return
    # generate large file for multipart testing
    util.create_large_file(GENERATED_CONTENT_INPUT_FILE, LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)

    # generate files, each containing a base64 string of an AES encryption key
    for fname in [GENERATED_ENC_KEY1_FILE, GENERATED_ENC_KEY2_FILE]:
        enc_key_str = generate_aes256_key_str()
        with open(fname, 'w') as f:
            f.write(enc_key_str)


def teardown_module():
    if os.path.exists(CONTENT_OUTPUT_FILE):
        os.remove(CONTENT_OUTPUT_FILE)

    if os.path.exists(GENERATED_CONTENT_INPUT_FILE):
        os.remove(GENERATED_CONTENT_INPUT_FILE)

    for fname in [GENERATED_ENC_KEY1_FILE, GENERATED_ENC_KEY2_FILE]:
        if os.path.exists(fname):
            os.remove(fname)


def test_run_all_operations(runner, config_file, config_profile, debug):
    """Successfully calls every operation with required arguments only."""
    bucket_name = 'cli_temp_bucket_' + str(random.randint(0, 1000000)) + ('_debug' if debug else '_no_debug')
    object_name = 'a'

    # ns get
    result = invoke(runner, config_file, config_profile, ['ns', 'get'], debug=debug)
    validate_response(result, includes_debug_data=debug)
    assert util.NAMESPACE in result.output

    # bucket create
    result = invoke(runner, config_file, config_profile,
                    ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name',
                     bucket_name], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object put
    result = invoke(runner, config_file, config_profile,
                    ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file',
                     CONTENT_INPUT_FILE, '--encryption-key-file', GENERATED_ENC_KEY1_FILE], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object get without SSE-C headers should result in a 400
    result = invoke(runner, config_file, config_profile,
                    ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file',
                     CONTENT_OUTPUT_FILE], debug=debug)
    util.validate_service_error(result, 'The service returned error code 400', debug)

    # object get with the wrong SSE-C key should result in a 403
    result = invoke(runner, config_file, config_profile,
                    ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file',
                     CONTENT_OUTPUT_FILE, '--encryption-key-file', GENERATED_ENC_KEY2_FILE], debug=debug)
    util.validate_service_error(result, 'The service returned error code 403', debug)

    # object get with the correct SSE-C key
    result = invoke(runner, config_file, config_profile,
                    ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file',
                     CONTENT_OUTPUT_FILE, '--encryption-key-file', GENERATED_ENC_KEY1_FILE], debug=debug)
    validate_response(result, json_response_expected=False, includes_debug_data=debug)
    assertEqual(get_file_content(CONTENT_INPUT_FILE), get_file_content(CONTENT_OUTPUT_FILE))

    # object head without any SSE-C data should fail with 400
    result = invoke(runner, config_file, config_profile,
                    ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name], debug=debug)
    util.validate_service_error(result, 'The service returned error code 400', debug)

    # object head with an incorrect SSE-C key should fail with 403
    result = invoke(runner, config_file, config_profile,
                    ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                     '--encryption-key-file', GENERATED_ENC_KEY2_FILE], debug=debug)
    util.validate_service_error(result, 'The service returned error code 403', debug)

    # object head with the right SSE-C key
    result = invoke(runner, config_file, config_profile,
                    ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                     '--encryption-key-file', GENERATED_ENC_KEY1_FILE], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object list (doesn't require SSE-C information)
    result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name],
                    debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object delete (doesn't require SSE-C information)
    result = invoke(runner, config_file, config_profile,
                    ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name], input='n',
                    debug=debug)
    assert result.exit_code != 0
    result = invoke(runner, config_file, config_profile,
                    ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name], input='y',
                    debug=debug)
    validate_response(result, json_response_expected=False, includes_debug_data=debug)

    # bucket delete
    result = invoke(runner, config_file, config_profile,
                    ['bucket', 'delete', '-ns', util.NAMESPACE, '--name', bucket_name, '--force'], debug=debug)
    validate_response(result, includes_debug_data=debug)


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True,
           strip_multipart_stderr_output=True, **args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli,
                               root_params + ['--debug', '--config-file', config_file, '--profile', config_profile,
                                              'os'] + params, **args)
    else:
        result = runner.invoke(oci_cli.cli,
                               root_params + ['--config-file', config_file, '--profile', config_profile, 'os'] + params,
                               **args)

    # many object storage operations output a progress bar in stderr but click doesnt differentiate between
    # stdout and stderr in result.output so we have to strip it out in order to validate the json response
    if strip_progress_bar and ('Uploading object' in result.output or 'Downloading object' in result.output):
        cleaned_output = result.output.replace('Uploading object', '').replace('Downloading object', '')
        try:
            new_output_bytes = bytes(cleaned_output, result.runner.charset)
        except TypeError:
            new_output_bytes = cleaned_output
        finally:
            result = click.testing.Result(result.runner, new_output_bytes, result.exit_code, result.exception,
                                          result.exc_info)

    # multipart uploads print out an upload ID and information when each part is uploaded successfully
    # for doing validation we need to strip this out
    if strip_multipart_stderr_output and result.output.startswith('Upload ID: '):
        cleaned_output = re.search('{(.*)}', result.output.replace('\n', '')).group(0)
        try:
            new_output_bytes = bytes(cleaned_output, result.runner.charset)
        except TypeError:
            new_output_bytes = cleaned_output
        finally:
            result = click.testing.Result(result.runner, new_output_bytes, result.exit_code, result.exception,
                                          result.exc_info)

    return result


def get_file_content(filename):
    with open(filename, 'r') as file:
        return file.read()


def extra_response_validation(result):
    assert 'opc-client-request-id' in result.output


def validate_response(result, includes_debug_data=False, json_response_expected=True):
    extra_validation = None
    if includes_debug_data:
        extra_validation = extra_response_validation
    util.validate_response(result, extra_validation=extra_validation, includes_debug_data=includes_debug_data,
                           json_response_expected=json_response_expected)


# TODO: clean up and remove all of these which are drop in replacements for unittest validations
def assertEqual(a, b):
    assert a == b


def assertEquals(a, b):
    assertEqual(a, b)


def assertListEqual(a, b):
    if len(a) != len(b):
        return False

    equal = True
    for i in range(0, len(a)):
        equal = equal and a[i] == b[i]

    return equal


def assertNotEquals(a, b):
    assert not a == b
