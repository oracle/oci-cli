# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import hashlib
import json
import os
import pytest
import threading
import time
import oci_cli
from . import util

CONTENT_OUTPUT_FILE = 'tests/resources/content_output.txt'
LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES = 100
DEFAULT_TEST_PART_SIZE = 1


@pytest.fixture(scope='function')
def content_input_file():
    filename = 'tests/temp/multipart_content_input.txt'

    # generate large file for multipart testing
    util.create_large_file(filename, LARGE_CONTENT_FILE_SIZE_IN_MEBIBYTES)

    yield filename

    if os.path.exists(filename):
        os.remove(filename)


@pytest.fixture(scope='module')
def temp_bucket(runner, config_file, config_profile, test_id):
    bucket_name = 'cli_temp_multipart_bucket_' + test_id

    # ns get
    result = invoke(runner, config_file, config_profile, ['ns', 'get'])
    validate_response(result)
    assert util.NAMESPACE in result.output

    # bucket create
    result = invoke(runner, config_file, config_profile, ['bucket', 'create', '-ns', util.NAMESPACE, '--compartment-id', util.COMPARTMENT_ID, '--name', bucket_name])
    validate_response(result)

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


def setup_function():
    if os.path.exists(CONTENT_OUTPUT_FILE):
        os.remove(CONTENT_OUTPUT_FILE)


def test_multipart_put_object(runner, config_file, config_profile, temp_bucket, content_input_file):
    object_name = 'a'

    # object put (large file so multipart is used)
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', temp_bucket,
                                                          '--name', object_name, '--file', content_input_file,
                                                          '--part-size', str(DEFAULT_TEST_PART_SIZE)])

    validate_response(result, json_response_expected=False)

    response = parse_json_response_from_multipart_output(result.output)
    assert response
    assert response["etag"]
    assert response["last-modified"]
    assert response["opc-multipart-md5"]

    upload_id = parse_upload_id_from_multipart_output(result.output)
    assert upload_id

    # object get (confirm object exists)
    result = invoke(runner, config_file, config_profile, ['object', 'get', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name, '--file', CONTENT_OUTPUT_FILE])
    validate_response(result, json_response_expected=False)

    assert checksum_md5(content_input_file) == checksum_md5(CONTENT_OUTPUT_FILE)
    assert os.stat(content_input_file).st_size == os.stat(CONTENT_OUTPUT_FILE).st_size

    # object delete
    result = invoke(runner, config_file, config_profile,
                    ['object', 'delete', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name], input='y')
    validate_response(result, json_response_expected=False)


def test_resume_multipart_upload(runner, config_file, config_profile, content_input_file, temp_bucket):
    object_name = 'a'

    def move_file(src, dest):
        time.sleep(2)
        os.rename(src, dest)

    parts = os.path.splitext(content_input_file)
    temp_filename = parts[0] + '_updated' + parts[1]

    # rename file to break upload while in progress
    t1 = threading.Thread(target=lambda: move_file(content_input_file, temp_filename))
    t1.start()

    # object put (relatively large file with small part size, so multipart is used)
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name, '--file', content_input_file, '--part-size', str(DEFAULT_TEST_PART_SIZE)])

    # copy file back to initial location to continue upload
    os.rename(temp_filename, content_input_file)

    # TODO: update response validation logic once it is JSON
    # validate that upload failed due to file moving
    error_message = 'No such file or directory'
    assert error_message in result.output

    upload_id = parse_upload_id_from_multipart_output(result.output)

    # list uploads and confirm this one shows up
    result = invoke(runner, config_file, config_profile, ['multipart', 'list', '-ns', util.NAMESPACE, '-bn', temp_bucket])
    validate_response(result)

    multipart_uploads = json.loads(result.output)["data"]
    assert len(multipart_uploads) == 1
    current_upload = multipart_uploads[0]
    assert current_upload["bucket"] == temp_bucket
    assert current_upload["object"] == object_name
    assert current_upload["upload-id"] == upload_id

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


def test_abort_multipart_upload(runner, config_file, config_profile, temp_bucket, content_input_file):
    object_name = 'a_abort'

    def remove_file(src):
        time.sleep(2)
        os.remove(src)

    # rename file to break upload while in progress
    t1 = threading.Thread(target=lambda: remove_file(content_input_file))
    t1.start()

    # object put (large file so multipart is used)
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name, '--file', content_input_file, '--part-size', str(DEFAULT_TEST_PART_SIZE)])

    # TODO: update response validation logic once it is JSON
    # validate that upload failed due to file moving
    error_message = 'No such file or directory'
    assert error_message in result.output

    upload_id = parse_upload_id_from_multipart_output(result.output)

    # list uploads and confirm this one shows up
    result = invoke(runner, config_file, config_profile, ['multipart', 'list', '-ns', util.NAMESPACE, '-bn', temp_bucket])
    validate_response(result)

    multipart_uploads = json.loads(result.output)["data"]
    assert len(multipart_uploads) == 1
    current_upload = multipart_uploads[0]
    assert current_upload["bucket"] == temp_bucket
    assert current_upload["object"] == object_name
    assert current_upload["upload-id"] == upload_id

    # abort multipart upload
    result = invoke(runner, config_file, config_profile, ['multipart', 'abort', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--object-name', object_name, '--upload-id', upload_id], input='y')
    validate_response(result, json_response_expected=False)

    # list uploads and confirm that there are none
    result = invoke(runner, config_file, config_profile, ['multipart', 'list', '-ns', util.NAMESPACE, '-bn', temp_bucket])
    validate_response(result)
    assert result.output == ''


def test_multipart_upload_with_metadata(runner, config_file, config_profile, temp_bucket, content_input_file):
    object_name = 'a_metadata'

    # object put (large file so multipart is used)
    result = invoke(runner, config_file, config_profile, ['object', 'put', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name, '--file', content_input_file, '--part-size', str(DEFAULT_TEST_PART_SIZE), '--metadata', '{"foo1":"bar1","key_with_underscore":"value_with_underscore"}'])

    # TODO: we dont expect JSON because there are print statements from the SDK right now
    validate_response(result, json_response_expected=False)

    response = parse_json_response_from_multipart_output(result.output)
    assert response
    assert response["etag"]
    assert response["last-modified"]
    assert response["opc-multipart-md5"]

    # object get (confirm object exists)
    result = invoke(runner, config_file, config_profile, ['object', 'get', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name, '--file', CONTENT_OUTPUT_FILE])
    validate_response(result, json_response_expected=False)

    assert checksum_md5(content_input_file) == checksum_md5(CONTENT_OUTPUT_FILE)
    assert os.stat(content_input_file).st_size == os.stat(CONTENT_OUTPUT_FILE).st_size

    # object head to confirm metadata
    result = invoke(runner, config_file, config_profile, ['object', 'head', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name])
    validate_response(result, json_response_expected=False)
    assert 'foo1' in result.output
    assert 'key_with_underscore' in result.output

    # object delete
    result = invoke(runner, config_file, config_profile, ['object', 'delete', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name], input='y')
    validate_response(result, json_response_expected=False)


def test_resume_with_unknown_upload_id(runner, config_file, config_profile, temp_bucket, content_input_file):
    object_name = 'a'
    upload_id = 'UNKNOWN_UPLOAD_ID'

    # resume multipart upload
    result = invoke(runner, config_file, config_profile, ['object', 'resume-put', '-ns', util.NAMESPACE, '-bn', temp_bucket, '--name', object_name, '--file', content_input_file, '--upload-id', upload_id])
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
