# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import base64
import hashlib
import json
import os
import pytest
import time
import oci_cli
from tests import util
from tests import test_config_container
from oci.object_storage import MultipartObjectAssembler
import random

CONTENT_OUTPUT_FILE = 'tests/resources/content_output.txt'
LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES = 100
DEFAULT_TEST_PART_SIZE = 1
CASSETTE_LIBRARY_DIR = 'services/object_storage/tests/cassettes'
GENERATED_ENC_KEY_FILE = 'tests/temp/generated_enc_key.txt'


@pytest.fixture
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('object_storage_multipart_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture(scope='function')
def content_input_file():
    filename = 'tests/temp/multipart_content_input.txt'

    # generate large file for multipart testing
    util.create_large_file(filename, LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)

    yield filename

    if os.path.exists(filename):
        os.remove(filename)


@pytest.fixture(scope='module')
def temp_bucket(runner, config_file, config_profile):
    bucket_name = 'cli_temp_multipart_bucket_' + str(random.randint(0, 1000000))
    print("Bucket Name: ", bucket_name)

    # ns get
    result = invoke(runner, config_file, config_profile, ['ns', 'get'])
    validate_response(result)
    assert util.NAMESPACE in result.output

    # bucket create
    result = invoke(runner, config_file, config_profile, ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name', bucket_name])
    validate_response(result)

    # create the SSE-C encryption key
    enc_key_str = generate_aes256_key_str()
    with open(GENERATED_ENC_KEY_FILE, 'w') as f:
        f.write(enc_key_str)

    yield bucket_name

    # clean up, delete bucket
    error_count = 0
    try:
        result = invoke(runner, config_file, config_profile, ['object', 'list', '-ns', util.NAMESPACE, '-bn', bucket_name])
        validate_response(result)
        response = json.loads(result.output)
        if 'data' in response:
            objects = response['data']
            for obj in objects:
                invoke(runner, config_file, config_profile, ['object', 'delete', '-ns', util.NAMESPACE, '-bn', bucket_name, '--name', obj['name'], '--force'])
                validate_response(result)
    except Exception as error:
        util.print_latest_exception(error)
        error_count = error_count + 1

    try:
        print("Deleting bucket")
        result = invoke(runner, config_file, config_profile, ['bucket', 'delete', '-ns', util.NAMESPACE, '--name', bucket_name, '--force'])
        validate_response(result)
    except Exception as error:
        util.print_latest_exception(error)
        error_count = error_count + 1

    assert 0 == error_count

    # remove the SSE-C key file
    if os.path.exists(GENERATED_ENC_KEY_FILE):
        os.remove(GENERATED_ENC_KEY_FILE)


@pytest.fixture(params=[False, True])
def customer_key(request):
    return request.param


def setup_function():
    if os.path.exists(CONTENT_OUTPUT_FILE):
        os.remove(CONTENT_OUTPUT_FILE)


def test_multipart_put_object(runner, config_file, config_profile, temp_bucket, content_input_file, customer_key):
    object_name = 'a'

    ssec_params = []
    if customer_key:
        ssec_params = ['--encryption-key-file', GENERATED_ENC_KEY_FILE]

    # object put (large file so multipart is used)
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', temp_bucket,
                                                          '--name', object_name, '--file', content_input_file,
                                                          '--part-size', str(DEFAULT_TEST_PART_SIZE)] + ssec_params)

    validate_response(result, json_response_expected=False)

    response = parse_json_response_from_multipart_output(result.output)
    assert response
    assert response["etag"]
    assert response["last-modified"]
    assert response["opc-multipart-md5"]

    upload_id = parse_upload_id_from_multipart_output(result.output)
    assert upload_id

    # object get (confirm object exists)
    result = invoke(runner, config_file, config_profile, ['object', 'get', '-ns', util.NAMESPACE, '-bn', temp_bucket,
                                                          '--name', object_name,
                                                          '--file', CONTENT_OUTPUT_FILE] + ssec_params)
    validate_response(result, json_response_expected=False)

    assert checksum_md5(content_input_file) == checksum_md5(CONTENT_OUTPUT_FILE)
    assert os.stat(content_input_file).st_size == os.stat(CONTENT_OUTPUT_FILE).st_size

    # object put (large file so multipart is used)
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', temp_bucket,
                                                          '--name', object_name, '--file', content_input_file,
                                                          '--part-size', str(DEFAULT_TEST_PART_SIZE),
                                                          '--force',
                                                          '--verify-checksum'] + ssec_params)
    validate_response(result, json_response_expected=False)
    assert "md5 checksum matches" in result.output

    # object delete
    result = invoke(runner, config_file, config_profile,
                    ['object', 'delete', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name], input='y')
    validate_response(result, json_response_expected=False)


def test_multipart_put_ia_object(runner, config_file, config_profile, temp_bucket, content_input_file, customer_key):
    object_name = 'a-ia'

    ssec_params = []
    if customer_key:
        ssec_params = ['--encryption-key-file', GENERATED_ENC_KEY_FILE]

    # object put (large file so multipart is used)
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', temp_bucket,
                                                          '--name', object_name, '--file', content_input_file,
                                                          '--storage-tier', 'InfrequentAccess',
                                                          '--part-size', str(DEFAULT_TEST_PART_SIZE)] + ssec_params)

    validate_response(result, json_response_expected=False)

    response = parse_json_response_from_multipart_output(result.output)
    assert response
    assert response["etag"]
    assert response["last-modified"]
    assert response["opc-multipart-md5"]

    upload_id = parse_upload_id_from_multipart_output(result.output)
    assert upload_id

    # object get (confirm object exists)
    result = invoke(runner, config_file, config_profile, ['object', 'get', '-ns', util.NAMESPACE, '-bn', temp_bucket,
                                                          '--name', object_name,
                                                          '--file', CONTENT_OUTPUT_FILE] + ssec_params)
    validate_response(result, json_response_expected=False)

    assert checksum_md5(content_input_file) == checksum_md5(CONTENT_OUTPUT_FILE)
    assert os.stat(content_input_file).st_size == os.stat(CONTENT_OUTPUT_FILE).st_size

    # object head (confirm storage-tier)
    result = invoke(runner, config_file, config_profile, ['object', 'head', '-ns', util.NAMESPACE, '-bn', temp_bucket,
                                                          '--name', object_name] + ssec_params)
    validate_response(result, json_response_expected=True)
    head_output = json.loads(result.output)
    assert 'storage-tier' in head_output
    assert 'InfrequentAccess' == head_output['storage-tier']

    # object delete
    result = invoke(runner, config_file, config_profile,
                    ['object', 'delete', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name], input='y')
    validate_response(result, json_response_expected=False)


def test_resume_multipart_upload(runner, config_file, config_profile, content_input_file, temp_bucket, object_storage_client):
    object_name = 'a'

    upload_id = setup_resume_abort_multipart_upload(content_input_file, object_storage_client, util.NAMESPACE, temp_bucket, object_name)

    # validate cannot resume with different part size
    result = invoke(runner, config_file, config_profile, ['object', 'resume-put', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name, '--file', content_input_file, '--upload-id', upload_id, '--part-size', str(DEFAULT_TEST_PART_SIZE + 1)])
    assert result.exit_code != 0

    # resume multipart upload
    time.sleep(20)
    result = invoke(runner, config_file, config_profile, ['object', 'resume-put', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name, '--file', content_input_file, '--upload-id', upload_id, '--part-size', str(DEFAULT_TEST_PART_SIZE)])
    validate_response(result, json_response_expected=False)

    # object get (confirm object exists and is the same as input content)
    result = invoke(runner, config_file, config_profile, ['object', 'get', '-ns', util.NAMESPACE,
                    '-bn', temp_bucket, '--name', object_name, '--file', CONTENT_OUTPUT_FILE])
    validate_response(result, json_response_expected=False)

    assert checksum_md5(content_input_file) == checksum_md5(CONTENT_OUTPUT_FILE)
    assert os.stat(content_input_file).st_size == os.stat(CONTENT_OUTPUT_FILE).st_size

    # object delete
    result = invoke(runner, config_file, config_profile, ['object', 'delete', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name, '--force'])
    validate_response(result)


# Initiates multipart upload, uploads first part of the file contents to the bucket, returns upload id.
def setup_resume_abort_multipart_upload(content_input_file, object_storage_client, namespace, bucket_name, object_name):
    # Upload the first part. part_size is 1 MiB
    kwargs = {'part_size': DEFAULT_TEST_PART_SIZE * 1024 * 1024}
    ma = MultipartObjectAssembler(object_storage_client, namespace, bucket_name, object_name, **kwargs)
    ma.new_upload()
    ma.add_parts_from_file(content_input_file)
    parts = list(enumerate(ma.manifest['parts']))
    ma._upload_part(part_num=parts[0][0] + 1, part=parts[0][1])

    upload_id = ma.manifest['uploadId']

    return upload_id


def test_abort_multipart_upload(runner, config_file, config_profile, temp_bucket, content_input_file, object_storage_client):
    object_name = 'a_abort'

    upload_id = setup_resume_abort_multipart_upload(content_input_file, object_storage_client, util.NAMESPACE, temp_bucket, object_name)

    # abort multipart upload
    result = invoke(runner, config_file, config_profile, ['multipart', 'abort', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--object-name', object_name, '--upload-id', upload_id], input='y')
    validate_response(result, json_response_expected=False)

    # list uploads and confirm that there are none
    result = invoke(runner, config_file, config_profile, ['multipart', 'list', '-ns', util.NAMESPACE, '-bn', temp_bucket])
    validate_response(result)
    assert result.output == ''


def test_multipart_upload_with_metadata(runner, config_file, config_profile, temp_bucket, content_input_file, customer_key):
    object_name = 'a_metadata'

    ssec_params = []
    if customer_key:
        ssec_params = ['--encryption-key-file', GENERATED_ENC_KEY_FILE]

    # object put (large file so multipart is used)
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', temp_bucket,
                                                          '--name', object_name, '--file', content_input_file,
                                                          '--part-size', str(DEFAULT_TEST_PART_SIZE),
                                                          '--metadata', '{"foo1":"bar1","key_with_underscore":"value_with_underscore"}'] + ssec_params)

    # TODO: we dont expect JSON because there are print statements from the SDK right now
    validate_response(result, json_response_expected=False)

    response = parse_json_response_from_multipart_output(result.output)
    assert response
    assert response["etag"]
    assert response["last-modified"]
    assert response["opc-multipart-md5"]

    # object get (confirm object exists)
    result = invoke(runner, config_file, config_profile, ['object', 'get', '-ns', util.NAMESPACE, '-bn', temp_bucket,
                                                          '--name', object_name,
                                                          '--file', CONTENT_OUTPUT_FILE] + ssec_params)
    validate_response(result, json_response_expected=False)

    assert checksum_md5(content_input_file) == checksum_md5(CONTENT_OUTPUT_FILE)
    assert os.stat(content_input_file).st_size == os.stat(CONTENT_OUTPUT_FILE).st_size

    # object head to confirm metadata
    result = invoke(runner, config_file, config_profile, ['object', 'head', '-ns', util.NAMESPACE, '-bn', temp_bucket,
                                                          '--name', object_name] + ssec_params)
    validate_response(result, json_response_expected=False)
    assert 'foo1' in result.output
    assert 'key_with_underscore' in result.output

    # object delete
    result = invoke(runner, config_file, config_profile, ['object', 'delete', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name], input='y')
    validate_response(result, json_response_expected=False)


@util.skip_while_rerecording
def test_resume_with_unknown_upload_id(vcr_fixture, runner, config_file, config_profile, content_input_file, test_id):
    object_name = 'a'
    upload_id = 'UNKNOWN_UPLOAD_ID'

    # resume multipart upload
    result = invoke(runner, config_file, config_profile, ['object', 'resume-put', '-ns', util.NAMESPACE, '-bn', "cli_temp_multipart_bucket_" + test_id, '--name', object_name, '--file', content_input_file, '--upload-id', upload_id])
    util.validate_service_error(result, error_message='No such upload')


def test_put_object_multipart_and_parallel_options(runner, config_file, config_profile, content_input_file):
    object_name = 'a'

    # validate error is returned if --parallel-upload-count and --disable-parallel-uploads are used
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', 'unknown_bucket', '--name', object_name, '--file', content_input_file, '--parallel-upload-count', '2', '--disable-parallel-uploads'])
    util.validate_service_error(result)

    # validate error is returned if --parallel-upload-count and --no-multipart are used
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', 'unknown_bucket', '--name', object_name, '--file', content_input_file, '--parallel-upload-count', '2', '--no-multipart'])
    util.validate_service_error(result)


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(
            oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile, 'os'] + params, ** args)
    else:
        result = runner.invoke(
            oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile, 'os'] + params, ** args)

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
    util.validate_response(result, extra_validation=extra_validation, includes_debug_data=includes_debug_data, json_response_expected=json_response_expected)


def checksum_md5(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            md5.update(chunk)
    return md5.digest()


def parse_json_response_from_multipart_output(output):
    lines = output.split('\n')
    json_str = ''
    object_begun = False
    for line in lines:
        if object_begun or line.startswith('{'):
            object_begun = True
            json_str += line

    return json.loads(json_str)


def parse_upload_id_from_multipart_output(output):
    token = 'Upload ID: '
    try:
        start = output.find(token)
        if start != -1:
            start += len(token)
            end = output.find('\n', start)
            return output[start:end]
        else:
            raise ValueError("Failed to find '{}' in output: {}".format(token, output))
    except IndexError:
        raise ValueError('Failed to parse upload id from output: {}'.format(output))


def generate_aes256_key_str():
    key = os.urandom(32)
    return base64.b64encode(key).decode('utf-8')
