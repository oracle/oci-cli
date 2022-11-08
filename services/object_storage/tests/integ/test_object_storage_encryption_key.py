# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import base64
import click
import os
import os.path
import pytest
import re
import oci_cli
from tests import util


CASSETTE_LIBRARY_DIR = 'services/object_storage/tests/cassettes'
CONTENT_INPUT_FILE = 'tests/resources/content_input.txt'
GENERATED_ENC_KEY1_FILE = 'tests/temp/generated_enc_key1.txt'
GENERATED_ENC_KEY2_FILE = 'tests/temp/generated_enc_key2.txt'
GENERATED_ENC_KEY1_FILE_WITH_NEWLINE = 'tests/temp/generated_enc_key1_with_newline.txt'
GENERATED_CONTENT_INPUT_FILE = 'tests/temp/generated_content_input.txt'
CONTENT_OUTPUT_FILE = 'tests/resources/content_output_encryption.txt'
LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES = 5
DEFAULT_TEST_PART_SIZE = 2
MOVE_BUCKET_TO_COMPARTMENT_ID = os.environ.get('OCI_CLI_MOVE_BUCKET_TO_COMPARTMENT_ID')

created_buckets = 'created_buckets'


def remove_file_at_loction(filename):
    if os.path.exists(filename):
        os.remove(filename)


@pytest.fixture(scope='function')
def delete_pending_buckets():
    data = {created_buckets: []}
    yield data
    for bucket_name in data[created_buckets]:
        delete_bucket(bucket_name)


def delete_bucket(bucket_name):
    invoke_new(['os', 'bucket', 'delete', '--namespace', util.NAMESPACE, '--bucket-name', bucket_name, '--empty', '--force'])


def invoke_new(commands, debug=False, ** args):
    if debug is True:
        commands = ['--debug'] + commands
    return util.invoke_command(commands, ** args)


@pytest.fixture
def content_input_file():
    yield GENERATED_CONTENT_INPUT_FILE
    remove_file_at_loction(GENERATED_CONTENT_INPUT_FILE)


@pytest.fixture(scope='function')
def content_output_file(test_id):
    content_output_file_location = f'tests/resources/content_output_encryption_{test_id}.txt'
    remove_file_at_loction(content_output_file_location)
    yield content_output_file_location
    remove_file_at_loction(content_output_file_location)


@pytest.fixture(params=[True, False])
def multipart(request):
    return request.param


@pytest.fixture(params=[True, False])
def debug(request):
    return request.param


def generate_aes256_key_str():
    key = os.urandom(32)
    return base64.b64encode(key).decode('utf-8')


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

    # generate file with leading, trailing whitespaces and newline added to it
    with open(GENERATED_ENC_KEY1_FILE) as fh:
        with open(GENERATED_ENC_KEY1_FILE_WITH_NEWLINE, 'w') as fw:
            fw.write('   ' + fh.read() + os.linesep + '   ')


def teardown_module():
    for fname in [GENERATED_ENC_KEY1_FILE, GENERATED_ENC_KEY2_FILE]:
        remove_file_at_loction(fname)


def test_run_all_operations(runner, config_file, config_profile, debug, delete_pending_buckets, content_output_file, test_id):
    """Successfully calls every operation with required arguments only."""
    bucket_name = 'cli_temp_bucket_' + test_id + ('_debug' if debug else '_no_debug')
    object_name = 'a'

    # check if GENERATED_ENC_KEY1_FILE is equal to the stripped version of GENERATED_ENC_KEY1_FILE_WITH_NEWLINE
    with open(GENERATED_ENC_KEY1_FILE) as f1:
        with open(GENERATED_ENC_KEY1_FILE_WITH_NEWLINE) as f2:
            assertNotEquals(f1.read(), f2.read())
            assertEquals(f1.read(), f2.read().strip())

    # ns get
    result = invoke(runner, config_file, config_profile, ['ns', 'get'], debug=debug)
    validate_response(result, includes_debug_data=debug)
    assert util.NAMESPACE in result.output

    # bucket create
    result = invoke(runner, config_file, config_profile,
                    ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name',
                     bucket_name], debug=debug)
    delete_pending_buckets[created_buckets].append(bucket_name)
    validate_response(result, includes_debug_data=debug)

    # object put
    result = invoke(runner, config_file, config_profile,
                    ['object', 'put', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file',
                     CONTENT_INPUT_FILE, '--encryption-key-file', GENERATED_ENC_KEY1_FILE], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object get without SSE-C headers should result in a 400
    result = invoke(runner, config_file, config_profile,
                    ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file',
                     content_output_file], debug=debug)
    util.validate_service_error(result, 'The service returned error code 400', debug)

    # object get with the wrong SSE-C key should result in a 403
    result = invoke(runner, config_file, config_profile,
                    ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file',
                     content_output_file, '--encryption-key-file', GENERATED_ENC_KEY2_FILE], debug=debug)
    util.validate_service_error(result, 'The service returned error code 403', debug)

    # object get with the correct SSE-C key.
    # checking the integrity of this test with newline added to the enc key.
    result = invoke(runner, config_file, config_profile,
                    ['object', 'get', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name, '--file',
                     content_output_file, '--encryption-key-file', GENERATED_ENC_KEY1_FILE_WITH_NEWLINE], debug=debug)
    validate_response(result, json_response_expected=False, includes_debug_data=debug)
    assertEqual(get_file_content(CONTENT_INPUT_FILE), get_file_content(content_output_file))

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

    # object reencrypt using the default/Oracle-managed key.
    # checking the integrity of this test with newline added to the enc key file.
    result = invoke(runner, config_file, config_profile,
                    ['object', 'reencrypt', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                     '--source-encryption-key-file', GENERATED_ENC_KEY1_FILE_WITH_NEWLINE], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # reencrypting the object again using the default/Oracle-managed key should not fail (no-op)
    result = invoke(runner, config_file, config_profile,
                    ['object', 'reencrypt', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name],
                    debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object head without any SSE-C data should succeed
    result = invoke(runner, config_file, config_profile,
                    ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # reencrypt the object using an SSE-C key
    result = invoke(runner, config_file, config_profile,
                    ['object', 'reencrypt', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                     '--encryption-key-file', GENERATED_ENC_KEY1_FILE], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object head without any SSE-C data should fail
    result = invoke(runner, config_file, config_profile,
                    ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name], debug=debug)
    util.validate_service_error(result, 'The service returned error code 400', debug)

    # object head with the right SSE-C key should succeed
    result = invoke(runner, config_file, config_profile,
                    ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                     '--encryption-key-file', GENERATED_ENC_KEY1_FILE], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # reencrypt the object using yet another SSE-C key.
    # checking the integrity of this test with newline added to enc key file.
    result = invoke(runner, config_file, config_profile,
                    ['object', 'reencrypt', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                     '--source-encryption-key-file', GENERATED_ENC_KEY1_FILE_WITH_NEWLINE,
                     '--encryption-key-file', GENERATED_ENC_KEY2_FILE],
                    debug=debug)
    validate_response(result, includes_debug_data=debug)

    # object head without any SSE-C data should fail
    result = invoke(runner, config_file, config_profile,
                    ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name], debug=debug)
    util.validate_service_error(result, 'The service returned error code 400', debug)

    # object head with an incorrect SSE-C key should fail with 403
    result = invoke(runner, config_file, config_profile,
                    ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                     '--encryption-key-file', GENERATED_ENC_KEY1_FILE], debug=debug)
    util.validate_service_error(result, 'The service returned error code 403', debug)

    # object head with the right SSE-C key should succeed
    result = invoke(runner, config_file, config_profile,
                    ['object', 'head', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                     '--encryption-key-file', GENERATED_ENC_KEY2_FILE], debug=debug)
    validate_response(result, includes_debug_data=debug)

    # specifying both KMS and SSE-C encryption keys to reencrypt the object should result in a 400 error
    result = invoke(runner, config_file, config_profile,
                    ['object', 'reencrypt', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', object_name,
                     '--kms-key-id', 'kms123456',
                     '--encryption-key-file', GENERATED_ENC_KEY1_FILE],
                    debug=debug)
    util.validate_service_error(result, 'The object re-encryption key must be specified either in the kmsKeyId field or in the sseCustomerKey field, but not in both', debug)

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
    delete_pending_buckets[created_buckets].remove(bucket_name)


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
