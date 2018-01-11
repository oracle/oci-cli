import click
import pytest
import oci_cli


def test_generate_input_dict_simple_types_only():
    params = [
        click.Option(['--param-one'], type=click.STRING),
        click.Option(['--param2'], type=click.INT),
        click.Option(['--some-float-param'], type=click.FLOAT),
        click.Option(['--boolparam'], type=click.BOOL),
        click.Option(['--datetimeparam'], type=oci_cli.custom_types.CLI_DATETIME)
    ]

    ctx = set_up_command_and_context(params)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {
        'paramOne': 'string',
        'param2': 0,
        'someFloatParam': 0.0,
        'boolparam': True,
        'datetimeparam': '2017-01-01T00:00:00.000000+00:00'
    }

    assert expected_dict == generated_dict


def test_generate_input_dict_no_params():
    ctx = set_up_command_and_context()

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {}

    assert expected_dict == generated_dict


def test_generate_input_dict_omits_help_and_generate_json_flags():
    params = [
        click.Option(['--param-one'], type=click.STRING),
        click.Option(['--help'], type=click.BOOL),
        click.Option(['--generate-param-json-input'], type=click.STRING),
        click.Option(['--generate-full-command-json-input'], type=click.BOOL)
    ]

    ctx = set_up_command_and_context(params)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {'paramOne': 'string'}

    assert expected_dict == generated_dict


def test_generate_input_dict_complex_param_is_dictionary_with_primitive_value():
    params = [
        click.Option(['--param-one'], type=click.STRING)
    ]

    input_params_to_complex_types = {
        'param-one': {'module': 'core', 'class': 'dict(string, int)'}
    }

    ctx = set_up_command_and_context(params, input_params_to_complex_types)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {
        'paramOne': {
            'string1': 0,
            'string2': 0
        }
    }

    assert expected_dict == generated_dict


def test_generate_input_dict_complex_param_is_dictionary_with_list_value():
    params = [
        click.Option(['--param-one'], type=click.STRING)
    ]

    input_params_to_complex_types = {
        'param-one': {'module': 'core', 'class': 'dict(string, list[string])'}
    }

    ctx = set_up_command_and_context(params, input_params_to_complex_types)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {
        'paramOne': {
            'string1': ['string', 'string'],
            'string2': ['string', 'string'],
        }
    }

    assert expected_dict == generated_dict


def test_generate_input_dict_complex_param_is_dictionary_with_dictionary_value():
    params = [
        click.Option(['--param-one'], type=click.STRING)
    ]

    input_params_to_complex_types = {
        'param-one': {'module': 'core', 'class': 'dict(string, dict(int, IcmpOptions))'}
    }

    ctx = set_up_command_and_context(params, input_params_to_complex_types)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {
        'paramOne': {
            'string1': {
                0: {'code': 0, 'type': 0},
                1: {'code': 0, 'type': 0},
            },
            'string2': {
                0: {'code': 0, 'type': 0},
                1: {'code': 0, 'type': 0},
            }
        }
    }

    assert expected_dict == generated_dict


def test_generate_input_dict_complex_param_is_dictionary_with_complex_value():
    params = [
        click.Option(['--param-one'], type=click.STRING)
    ]

    input_params_to_complex_types = {
        'param-one': {'module': 'core', 'class': 'dict(string, FastConnectProviderService)'}
    }

    ctx = set_up_command_and_context(params, input_params_to_complex_types)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {
        'paramOne': {
            'string1': {
                'supportedVirtualCircuitTypes': ['string', 'string'],
                'providerServiceName': 'string',
                'publicPeeringBgpManagement': 'string',
                'description': 'string',
                'type': 'string',
                'providerName': 'string',
                'id': 'string',
                'privatePeeringBgpManagement': 'string'
            },
            'string2': {
                'supportedVirtualCircuitTypes': ['string', 'string'],
                'providerServiceName': 'string',
                'publicPeeringBgpManagement': 'string',
                'description': 'string',
                'type': 'string',
                'providerName': 'string',
                'id': 'string',
                'privatePeeringBgpManagement': 'string'
            }
        }
    }

    assert expected_dict == generated_dict


def test_generate_input_dict_complex_param_is_list_of_primitives():
    params = [
        click.Option(['--param-one'], type=click.STRING)
    ]

    input_params_to_complex_types = {
        'param-one': {'module': 'core', 'class': 'list[float]'}
    }

    ctx = set_up_command_and_context(params, input_params_to_complex_types)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {
        'paramOne': [0.0, 0.0]
    }

    assert expected_dict == generated_dict


def test_generate_input_dict_complex_param_is_list_of_lists():
    params = [
        click.Option(['--param-one'], type=click.STRING)
    ]

    input_params_to_complex_types = {
        'param-one': {'module': 'core', 'class': 'list[list[string]]'}
    }

    ctx = set_up_command_and_context(params, input_params_to_complex_types)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {
        'paramOne': [['string', 'string'], ['string', 'string']]
    }

    assert expected_dict == generated_dict


def test_generate_input_dict_complex_param_is_list_of_complex_type():
    params = [
        click.Option(['--param-one'], type=click.STRING)
    ]

    input_params_to_complex_types = {
        'param-one': {'module': 'core', 'class': 'list[InternetGateway]'}
    }

    ctx = set_up_command_and_context(params, input_params_to_complex_types)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {
        'paramOne': [
            {
                'compartmentId': 'string',
                'displayName': 'string',
                'id': 'string',
                'isEnabled': True,
                'lifecycleState': 'string',
                'timeCreated': '2017-01-01T00:00:00.000000+00:00',
                'vcnId': 'string'
            },
            {
                'compartmentId': 'string',
                'displayName': 'string',
                'id': 'string',
                'isEnabled': True,
                'lifecycleState': 'string',
                'timeCreated': '2017-01-01T00:00:00.000000+00:00',
                'vcnId': 'string'
            }
        ]
    }

    assert expected_dict == generated_dict


def test_generate_input_dict_complex_param_is_list_of_dictionary():
    params = [
        click.Option(['--param-one'], type=click.STRING)
    ]

    input_params_to_complex_types = {
        'param-one': {'module': 'core', 'class': 'list[dict(string, date)]'}
    }

    ctx = set_up_command_and_context(params, input_params_to_complex_types)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {
        'paramOne': [
            {'string1': '2017-01-01', 'string2': '2017-01-01'},
            {'string1': '2017-01-01', 'string2': '2017-01-01'}
        ]
    }

    assert expected_dict == generated_dict


def test_generate_input_dict_complex_param_is_model():
    params = [
        click.Option(['--param-one'], type=click.STRING)
    ]

    input_params_to_complex_types = {
        'param-one': {'module': 'core', 'class': 'CreateRouteTableDetails'}
    }

    ctx = set_up_command_and_context(params, input_params_to_complex_types)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {
        'paramOne': {
            'compartmentId': 'string',
            'displayName': 'string',
            'vcnId': 'string',
            'routeRules': [
                {'cidrBlock': 'string', 'networkEntityId': 'string'},
                {'cidrBlock': 'string', 'networkEntityId': 'string'}
            ],
            'freeformTags': {
                'string1': 'string',
                'string2': 'string'
            },
            'definedTags': {
                'string1': {
                    'string1': {
                        'string1': 'string',
                        'string2': 'string'
                    },
                    'string2': {
                        'string1': 'string',
                        'string2': 'string'
                    }
                },
                'string2': {
                    'string1': {
                        'string1': 'string',
                        'string2': 'string'
                    },
                    'string2': {
                        'string1': 'string',
                        'string2': 'string'
                    }
                }
            }
        }
    }

    assert expected_dict == generated_dict


def test_generate_input_dict_complex_param_is_model_with_subclasses():
    params = [
        click.Option(['--param-one'], type=click.STRING)
    ]

    input_params_to_complex_types = {
        'param-one': {'module': 'core', 'class': 'ImageSourceDetails'}
    }

    ctx = set_up_command_and_context(params, input_params_to_complex_types)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {
        'paramOne': [
            'This parameter should actually be a JSON object rather than an array - pick one of the following object variants to use',
            {
                'bucketName': 'string',
                'namespaceName': 'string',
                'objectName': 'string',
                'sourceType': 'objectStorageTuple',
                'sourceImageType': 'string'
            },
            {
                'sourceType': 'objectStorageUri',
                'sourceUri': 'string',
                'sourceImageType': 'string'
            }
        ]
    }

    assert expected_dict == generated_dict


def test_generate_input_dict_complex_and_non_complex_params_strip_duplicates():
    params = [
        click.Option(['--param-one'], type=click.STRING),
        click.Option(['--compartment-id'], type=click.STRING)
    ]

    input_params_to_complex_types = {
        'param-one': {'module': 'core', 'class': 'CreateRouteTableDetails'}
    }

    ctx = set_up_command_and_context(params, input_params_to_complex_types)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx)
    expected_dict = {
        'compartmentId': 'string',
        'paramOne': {
            'displayName': 'string',
            'vcnId': 'string',
            'routeRules': [
                {'cidrBlock': 'string', 'networkEntityId': 'string'},
                {'cidrBlock': 'string', 'networkEntityId': 'string'}
            ],
            'freeformTags': {
                'string1': 'string',
                'string2': 'string'
            },
            'definedTags': {
                'string1': {
                    'string1': {
                        'string1': 'string',
                        'string2': 'string'
                    },
                    'string2': {
                        'string1': 'string',
                        'string2': 'string'
                    }
                },
                'string2': {
                    'string1': {
                        'string1': 'string',
                        'string2': 'string'
                    },
                    'string2': {
                        'string1': 'string',
                        'string2': 'string'
                    }
                }
            }
        }
    }

    assert expected_dict == generated_dict


def test_generate_input_dict_complex_and_non_complex_params_request_only_complex_param():
    params = [
        click.Option(['--param-one'], type=click.STRING),
        click.Option(['--compartment-id'], type=click.STRING)
    ]

    input_params_to_complex_types = {
        'param-one': {'module': 'core', 'class': 'CreateRouteTableDetails'}
    }

    ctx = set_up_command_and_context(params, input_params_to_complex_types)

    generated_dict = oci_cli.json_skeleton_utils.generate_input_dict_for_skeleton(ctx, 'param-one')
    expected_dict = {
        'displayName': 'string',
        'vcnId': 'string',
        'routeRules': [
            {'cidrBlock': 'string', 'networkEntityId': 'string'},
            {'cidrBlock': 'string', 'networkEntityId': 'string'}
        ],
        'freeformTags': {
            'string1': 'string',
            'string2': 'string'
        },
        'definedTags': {
            'string1': {
                'string1': {
                    'string1': 'string',
                    'string2': 'string'
                },
                'string2': {
                    'string1': 'string',
                    'string2': 'string'
                }
            },
            'string2': {
                'string1': {
                    'string1': 'string',
                    'string2': 'string'
                },
                'string2': {
                    'string1': 'string',
                    'string2': 'string'
                }
            }
        }
    }

    assert expected_dict == generated_dict


def test_cli_json_input_empty():
    ctx = set_up_command_and_context()
    oci_cli.json_skeleton_utils.cli_json_input_callback(ctx, 'cli-json-input', '{}')

    assert ctx.default_map is None  # Empty dict is false-y


def test_cli_json_input_direct():
    ctx = set_up_command_and_context()
    oci_cli.json_skeleton_utils.cli_json_input_callback(
        ctx,
        'cli-json-input',
        '{ "objectName": "image-to-import.qcow2", "anArray": ["value1", "value2"], "aNestedObject": { "key": "value", "anotherArray": ["value1"], "anotherComplex": { "nestedKey": "nestedVal" }  } }'
    )

    expected_value = {
        'object_name': 'image-to-import.qcow2',
        'an_array': ["value1", "value2"],
        'a_nested_object': {
            'key': 'value',
            'anotherArray': ["value1"],
            'anotherComplex': {
                'nestedKey': 'nestedVal'
            }
        }
    }

    assert expected_value == ctx.default_map


def test_cli_json_input_direct_is_collection():
    ctx = set_up_command_and_context()

    with pytest.raises(SystemExit):
        oci_cli.json_skeleton_utils.cli_json_input_callback(
            ctx,
            'cli-json-input',
            '[ { "hello": "world" }, { "second": "element" } ]'
        )


def test_cli_json_input_from_file_is_collection():
    ctx = set_up_command_and_context()

    with pytest.raises(SystemExit):
        oci_cli.json_skeleton_utils.cli_json_input_callback(
            ctx,
            'cli-json-input',
            'file://tests/resources/json_parsing/collection.json'
        )


def test_cli_json_input_from_file():
    ctx = set_up_command_and_context()
    oci_cli.json_skeleton_utils.cli_json_input_callback(
        ctx,
        'cli-json-input',
        'file://tests/resources/json_parsing/nested.json'
    )

    expected_value = {
        'object_name': 'image-to-import.qcow2',
        'an_array': ["value1", "value2"],
        'a_nested_object': {
            'key': 'value',
            'anotherArray': [1, 2, 3],
            'anotherComplex': {
                "nestedKey": "nestedVal",
                "someNumber": 11
            }
        },
        "a_number": 12345
    }

    assert expected_value == ctx.default_map


def set_up_command_and_context(params=[], input_params_to_complex_types={}):
    command = click.Command('unit-test-command', params=params)
    context_obj = {'input_params_to_complex_types': input_params_to_complex_types}
    context = click.Context(command, parent=None, info_name='unit-test', obj=context_obj)

    return context
