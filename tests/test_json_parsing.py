import click
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
        'anArray': ['value1', 'value2'],
        'aNestedObject': {
            'key': 'value',
            'anotherArray': ['value1'],
            'anotherComplex': {
                'nestedKey': 'nestedVal'
            }
        }
    }
    assert param_value == expected_value


def test_parameter_value_key_auto_camelization():
    param_value = oci_cli.cli_util.parse_json_parameter(
        'test-param',
        '{ "object-name": "image-to-import.qcow2", "anArray": [{"camelize-me": 123}, {"alreadyCamelized": 345}], "aNestedObject": { "key": "value", "anotherArray": ["value1"], "another-complex": { "nested_key": "nestedVal" }  } }')

    expected_value = {
        'objectName': 'image-to-import.qcow2',
        'anArray': [{"camelizeMe": 123}, {"alreadyCamelized": 345}],
        'aNestedObject': {
            'key': 'value',
            'anotherArray': ['value1'],
            'anotherComplex': {
                'nestedKey': 'nestedVal'
            }
        }
    }
    assert param_value == expected_value


def test_parameter_value_key_no_auto_camelization():
    param_value = oci_cli.cli_util.parse_json_parameter(
        'test-param',
        '{ "object-name": "image-to-import.qcow2", "anArray": [{"camelize-me": 123}, {"alreadyCamelized": 345}], "aNestedObject": { "key": "value", "anotherArray": ["value1"], "another-complex": { "nested_key": "nestedVal" }  } }',
        camelize_keys=False)

    expected_value = {
        'object-name': 'image-to-import.qcow2',
        'anArray': [{'camelize-me': 123}, {'alreadyCamelized': 345}],
        'aNestedObject': {
            'key': 'value',
            'anotherArray': ['value1'],
            'another-complex': {
                'nested_key': 'nestedVal'
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
        'anArray': ['value1', 'value2'],
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


def test_load_from_file_auto_camelization():
    param_value = oci_cli.cli_util.parse_json_parameter(
        'test-param',
        'file://tests/resources/json_parsing/test_camelized.json')

    expected_value = {
        'objectName': 'image-to-import.qcow2',
        'anArray': ['value1', 'value2'],
        'aNestedObject': {
            'key': 'value',
            'anotherArray': [1, 2, 3],
            'complexArray': [{'one': 'two'}, {'purplePeopleEater': 'three'}],
            'anotherComplex': {
                'nestedKey': 'nestedVal',
                'someNumber': 11
            }
        },
        'aNumber': 12345
    }
    assert param_value == expected_value


def test_load_from_file_no_auto_camelization():
    param_value = oci_cli.cli_util.parse_json_parameter(
        'test-param',
        'file://tests/resources/json_parsing/test_camelized.json',
        camelize_keys=False)

    expected_value = {
        'object-name': 'image-to-import.qcow2',
        'anArray': ['value1', 'value2'],
        'aNestedObject': {
            'key': 'value',
            'anotherArray': [1, 2, 3],
            'complex-array': [{'one': 'two'}, {'purple-people-eater': 'three'}],
            'another-complex': {
                'nested-key': 'nestedVal',
                'someNumber': 11
            }
        },
        'aNumber': 12345
    }
    assert param_value == expected_value


def test_default_camelize_when_no_parameter_name_or_complex_parameter_type():
    test_dict = {
        'key-one': 'one',
        'key-two': {
            'key-three': 'four',
            'keyFive': 'five'
        },
        'key-six': [{'key-one': 'val'}, {'keyTwo': 'val2'}]
    }

    dict_after_call = oci_cli.cli_util.make_dict_keys_camel_case(test_dict)

    expected_dict = {
        'keyOne': 'one',
        'keyTwo': {
            'keyThree': 'four',
            'keyFive': 'five'
        },
        'keySix': [{'keyOne': 'val'}, {'keyTwo': 'val2'}]
    }

    assert expected_dict == dict_after_call


def test_camelize_when_type_is_dict_of_primitive_to_primitive():
    test_dict = {
        'key-one': 'one',
        'key-two': 'two',
        'key-three': 'three'
    }

    dict_after_call = oci_cli.cli_util.make_dict_keys_camel_case(test_dict, complex_parameter_type={'module': 'core', 'class': 'dict(str, str)'})

    assert test_dict == dict_after_call


def test_camelize_when_type_is_dict_of_primitive_to_primitive_collection():
    test_dict = {
        'key-one': [1, 2, 3],
        'key-two': [4, 5, 6],
        'key-three': [7, 8, 9]
    }

    dict_after_call = oci_cli.cli_util.make_dict_keys_camel_case(test_dict, complex_parameter_type={'module': 'core', 'class': 'dict(str, list[int])'})

    assert test_dict == dict_after_call


def test_camelize_when_type_is_dict_of_primitive_to_known_type():
    # The known object is EgressSecurityRule. We also inject some stuff which needs camelization so that we know that works
    test_dict = {
        'key-one': {
            'destination': 'string',
            'icmp-options': {'code': 0, 'type': 0},
            'isStateless': True,
            'protocol': 'string',
            'tcpOptions': {
                'destination-port-range': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            },
            'udpOptions': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            }
        },
        'keyTwo': {
            'destination': 'string',
            'icmpOptions': {'code': 0, 'type': 0},
            'isStateless': True,
            'protocol': 'string',
            'tcpOptions': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'source-port-range': {'max': 0, 'min': 0}
            },
            'udp-options': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            }
        }
    }

    dict_after_call = oci_cli.cli_util.make_dict_keys_camel_case(test_dict, complex_parameter_type={'module': 'core', 'class': 'dict(str, EgressSecurityRule)'})

    expected_dict = {
        'key-one': {
            'destination': 'string',
            'icmpOptions': {'code': 0, 'type': 0},
            'isStateless': True,
            'protocol': 'string',
            'tcpOptions': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            },
            'udpOptions': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            }
        },
        'keyTwo': {
            'destination': 'string',
            'icmpOptions': {'code': 0, 'type': 0},
            'isStateless': True,
            'protocol': 'string',
            'tcpOptions': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            },
            'udpOptions': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            }
        }
    }

    assert expected_dict == dict_after_call


def test_camelize_when_type_is_list_of_primitive():
    test_obj = ['one', 'two', 'three']
    obj_after_call = oci_cli.cli_util.make_dict_keys_camel_case(test_obj, complex_parameter_type={'module': 'core', 'class': 'list[str]'})

    assert test_obj == obj_after_call


def test_camelize_when_type_is_list_of_known_type():
    test_obj = [
        {
            'destination': 'string',
            'icmp-options': {'code': 0, 'type': 0},
            'isStateless': True,
            'protocol': 'string',
            'tcpOptions': {
                'destination-port-range': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            },
            'udpOptions': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            }
        },
        {
            'destination': 'string',
            'icmpOptions': {'code': 0, 'type': 0},
            'isStateless': True,
            'protocol': 'string',
            'tcpOptions': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'source-port-range': {'max': 0, 'min': 0}
            },
            'udp-options': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            }
        }
    ]

    obj_after_call = oci_cli.cli_util.make_dict_keys_camel_case(test_obj, complex_parameter_type={'module': 'core', 'class': 'list[EgressSecurityRule]'})

    expected_obj = [
        {
            'destination': 'string',
            'icmpOptions': {'code': 0, 'type': 0},
            'isStateless': True,
            'protocol': 'string',
            'tcpOptions': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            },
            'udpOptions': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            }
        },
        {
            'destination': 'string',
            'icmpOptions': {'code': 0, 'type': 0},
            'isStateless': True,
            'protocol': 'string',
            'tcpOptions': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            },
            'udpOptions': {
                'destinationPortRange': {'max': 0, 'min': 0},
                'sourcePortRange': {'max': 0, 'min': 0}
            }
        }
    ]

    assert expected_obj == obj_after_call


def test_camelize_when_list_of_dict_of_primitive():
    test_obj = [
        {'key-one': 'blah', 'keyTwo': 77},
        {'user-key': 'world'}
    ]

    obj_after_call = oci_cli.cli_util.make_dict_keys_camel_case(test_obj, complex_parameter_type={'module': 'core', 'class': 'list[dict(str, str)]'})

    assert obj_after_call == test_obj


def test_camelize_when_list_of_dict_of_arbitrary_object():
    test_obj = [
        {'key-one': {'preserve_me': 'please'}, 'keyTwo': {'hello-world': 'stuff', 'thingThing': 'thing'}},
        {'user-key': {'an-array': [1, 2, 3]}}
    ]

    obj_after_call = oci_cli.cli_util.make_dict_keys_camel_case(test_obj, complex_parameter_type={'module': 'core', 'class': 'list[dict(str, object)]'})

    assert obj_after_call == test_obj


def test_camelize_when_known_type_has_internal_complex_types_and_dict_types():
    # LaunchInstanceDetails is an example of this (it has metadata and extendedMetadata,
    # which are a dict of string to string & and dict of string to object, respectively)
    test_obj = {
        'availability_domain': 'availabilityDomain',
        'compartment_id': 'compartmentId',
        'create_vnic_details': {
            'assign_public_ip': True,
            'display_name': 'str',
            'hostnameLabel': 'str',
            'private_ip': 'str',
            'subnet_id': 'str'
        },
        'display_name': 'displayName',
        'extended_metadata': {
            'key': {'hello': 'world', 'snake-case': 'snake'},
            'another-key_value': {'world': 'tree'}
        },
        'hostname_label': 'hostnameLabel',
        'image_id': 'imageId',
        'ipxe_script': 'ipxeScript',
        'metadata': {
            'my-key': 'blah',
            'my_other_key': 'dfhkjsdfsdf',
            'reallyStuff': 'stuff'
        },
        'shape': 'shape',
        'subnet_id': 'subnetId'
    }

    obj_after_call = oci_cli.cli_util.make_dict_keys_camel_case(test_obj, complex_parameter_type={'module': 'core', 'class': 'LaunchInstanceDetails'})

    expected_obj = {
        'availabilityDomain': 'availabilityDomain',
        'compartmentId': 'compartmentId',
        'createVnicDetails': {
            'assignPublicIp': True,
            'displayName': 'str',
            'hostnameLabel': 'str',
            'privateIp': 'str',
            'subnetId': 'str'
        },
        'displayName': 'displayName',
        'extendedMetadata': {
            'key': {'hello': 'world', 'snake-case': 'snake'},
            'another-key_value': {'world': 'tree'}
        },
        'hostnameLabel': 'hostnameLabel',
        'imageId': 'imageId',
        'ipxeScript': 'ipxeScript',
        'metadata': {
            'my-key': 'blah',
            'my_other_key': 'dfhkjsdfsdf',
            'reallyStuff': 'stuff'
        },
        'shape': 'shape',
        'subnetId': 'subnetId'
    }

    assert expected_obj == obj_after_call


def test_camelize_with_provided_parameter_name_in_context():
    context = set_up_context({'paramOne': {'module': 'core', 'class': 'LaunchInstanceDetails'}})
    click.globals.push_context(context)

    test_obj = {
        'availability_domain': 'availabilityDomain',
        'compartment_id': 'compartmentId',
        'create_vnic_details': {
            'assign_public_ip': True,
            'display_name': 'str',
            'hostnameLabel': 'str',
            'private_ip': 'str',
            'subnet_id': 'str'
        },
        'display_name': 'displayName',
        'extended_metadata': {
            'key': {'hello': 'world', 'snake-case': 'snake'},
            'another-key_value': {'world': 'tree'}
        },
        'hostname_label': 'hostnameLabel',
        'image_id': 'imageId',
        'ipxe_script': 'ipxeScript',
        'metadata': {
            'my-key': 'blah',
            'my_other_key': 'dfhkjsdfsdf',
            'reallyStuff': 'stuff'
        },
        'shape': 'shape',
        'subnet_id': 'subnetId'
    }

    obj_after_call = oci_cli.cli_util.make_dict_keys_camel_case(test_obj, parameter_name='paramOne')

    expected_obj = {
        'availabilityDomain': 'availabilityDomain',
        'compartmentId': 'compartmentId',
        'createVnicDetails': {
            'assignPublicIp': True,
            'displayName': 'str',
            'hostnameLabel': 'str',
            'privateIp': 'str',
            'subnetId': 'str'
        },
        'displayName': 'displayName',
        'extendedMetadata': {
            'key': {'hello': 'world', 'snake-case': 'snake'},
            'another-key_value': {'world': 'tree'}
        },
        'hostnameLabel': 'hostnameLabel',
        'imageId': 'imageId',
        'ipxeScript': 'ipxeScript',
        'metadata': {
            'my-key': 'blah',
            'my_other_key': 'dfhkjsdfsdf',
            'reallyStuff': 'stuff'
        },
        'shape': 'shape',
        'subnetId': 'subnetId'
    }

    assert expected_obj == obj_after_call


def test_camelize_with_provided_parameter_name_not_in_context_but_keys_are_known_types():
    context = set_up_context({
        'create-vnic-details': {'module': 'core', 'class': 'CreateVnicDetails'},
        'extended-metadata': {'module': 'core', 'class': 'dict(str, object)'},
        'metadata': {'module': 'core', 'class': 'dict(str, str)'}
    })
    click.globals.push_context(context)

    test_obj = {
        'availability_domain': 'availabilityDomain',
        'compartment_id': 'compartmentId',
        'create_vnic_details': {
            'assign_public_ip': True,
            'display_name': 'str',
            'hostnameLabel': 'str',
            'private_ip': 'str',
            'subnet_id': 'str'
        },
        'display_name': 'displayName',
        'extended_metadata': {
            'key': {'hello': 'world', 'snake-case': 'snake'},
            'another-key_value': {'world': 'tree'}
        },
        'hostname_label': 'hostnameLabel',
        'image_id': 'imageId',
        'ipxe_script': 'ipxeScript',
        'metadata': {
            'my-key': 'blah',
            'my_other_key': 'dfhkjsdfsdf',
            'reallyStuff': 'stuff'
        },
        'shape': 'shape',
        'subnet_id': 'subnetId'
    }

    obj_after_call = oci_cli.cli_util.make_dict_keys_camel_case(test_obj, parameter_name='full_json')

    expected_obj = {
        'availabilityDomain': 'availabilityDomain',
        'compartmentId': 'compartmentId',
        'createVnicDetails': {
            'assignPublicIp': True,
            'displayName': 'str',
            'hostnameLabel': 'str',
            'privateIp': 'str',
            'subnetId': 'str'
        },
        'displayName': 'displayName',
        'extendedMetadata': {
            'key': {'hello': 'world', 'snake-case': 'snake'},
            'another-key_value': {'world': 'tree'}
        },
        'hostnameLabel': 'hostnameLabel',
        'imageId': 'imageId',
        'ipxeScript': 'ipxeScript',
        'metadata': {
            'my-key': 'blah',
            'my_other_key': 'dfhkjsdfsdf',
            'reallyStuff': 'stuff'
        },
        'shape': 'shape',
        'subnetId': 'subnetId'
    }

    assert expected_obj == obj_after_call


def set_up_context(input_params_to_complex_types={}):
    command = click.Command('unit-test-command')
    context_obj = {'input_params_to_complex_types': input_params_to_complex_types}
    context = click.Context(command, parent=None, info_name='unit-test', obj=context_obj)

    return context
