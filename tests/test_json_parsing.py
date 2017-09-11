import pytest
import oci_cli


def test_none_parameter_value_no_default_provided():
    param_value = oci_cli.cli_util.parse_json_parameter('test-param', None)
    assert param_value is None


def test_none_parameter_value_default_provided():
    param_value = oci_cli.cli_util.parse_json_parameter('test-param', None, {'key': 'value'})

    expected_value = {'key': 'value'}
    assert param_value == expected_value


def test_parameter_value_is_raw_json_string_simple():
    param_value = oci_cli.cli_util.parse_json_parameter(
        'test-param',
        '{ "objectName": "image-to-import.qcow2", "bucketName": "MyBucket", "namespaceName": "MyNamespace", "sourceType": "objectStorageTuple" }')

    expected_value = {'objectName': 'image-to-import.qcow2', 'bucketName': 'MyBucket', 'namespaceName': 'MyNamespace', 'sourceType': 'objectStorageTuple'}
    assert param_value == expected_value


def test_parameter_value_is_raw_json_string_nested():
    param_value = oci_cli.cli_util.parse_json_parameter(
        'test-param',
        '{ "objectName": "image-to-import.qcow2", "anArray": ["value1", "value2"], "aNestedObject": { "key": "value", "anotherArray": ["value1"], "anotherComplex": { "nestedKey": "nestedVal" }  } }')

    expected_value = {
        'objectName': 'image-to-import.qcow2',
        'anArray': ["value1", "value2"],
        'aNestedObject': {
            'key': 'value',
            'anotherArray': ["value1"],
            'anotherComplex': {
                'nestedKey': 'nestedVal'
            }
        }
    }
    assert param_value == expected_value


def test_load_from_file_bad_prefix():
    with pytest.raises(SystemExit):
        oci_cli.cli_util.parse_json_parameter('test-param', 'protocol://some-junk.json')


def test_load_from_file_no_path():
    with pytest.raises(SystemExit):
        oci_cli.cli_util.parse_json_parameter('test-param', 'file://')


def test_load_from_non_existent_file():
    with pytest.raises(SystemExit):
        oci_cli.cli_util.parse_json_parameter('test-param', 'file://this-file-better-not-exist')


def test_load_from_file_empty():
    with pytest.raises(SystemExit):
        oci_cli.cli_util.parse_json_parameter('test-param', 'file://tests/resources/json_parsing/empty.json')


def test_load_from_file_invalid_json():
    with pytest.raises(SystemExit):
        oci_cli.cli_util.parse_json_parameter('test-param', 'file://tests/resources/json_parsing/invalid_json.json')


def test_load_from_file_simple_json():
    param_value = oci_cli.cli_util.parse_json_parameter('test-param', 'file://tests/resources/json_parsing/simple.json')

    expected_value = {'objectName': 'image-to-import.qcow2', 'bucketName': 'MyBucket', 'namespaceName': 'MyNamespace', 'sourceType': 'objectStorageTuple'}
    assert param_value == expected_value


def test_load_from_file_nested_json():
    param_value = oci_cli.cli_util.parse_json_parameter('test-param', 'file://tests/resources/json_parsing/nested.json')

    expected_value = {
        'objectName': 'image-to-import.qcow2',
        'anArray': ["value1", "value2"],
        'aNestedObject': {
            'key': 'value',
            'anotherArray': [1, 2, 3],
            'anotherComplex': {
                'nestedKey': 'nestedVal',
                'someNumber': 11
            }
        },
        'aNumber': 12345
    }
    assert param_value == expected_value


def test_load_from_file_collection():
    param_value = oci_cli.cli_util.parse_json_parameter('test-param', 'file://tests/resources/json_parsing/collection.json')

    expected_value = [
        {'cidrBlock': '0.0.0.0/0', 'networkEntityId': 'ocid1.internetgateway.oc1.phx.aaaaaaaa3vcd7gmqqh4po6wnsjhcdkxlddeqinmnbanzz2wsh5gdrwt574ka'},
        {'cidrBlock': '10.0.0.0/16', 'networkEntityId': 'ocid1.internetgateway.oc1.phx.aaaaaaaa3vcd7gmqqh4po6wnsjhcdkxlddeqinmnbanzz2wsh5gdrwt574kb'},
    ]
    assert param_value == expected_value
