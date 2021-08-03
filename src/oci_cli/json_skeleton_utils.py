# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
import functools
import json
import re
import six
import sys

from . import cli_util
from . import cli_exceptions

from .custom_types import CliFromJson, CLI_DATETIME
from .string_utils import camelize, underscore

import collections.abc as abc

CLICK_TYPES_TO_EXAMPLE_VALUES = {
    click.STRING: 'string',
    click.INT: 0,
    click.FLOAT: 0.0,
    click.BOOL: True,
    CLI_DATETIME: '2017-01-01T00:00:00+00:00',
}


# There are some intentional synonyms here (e.g. "str" and "string")
PRIMITIVE_TYPES_TO_EXAMPLE_SCALAR_VALUES = {
    'str': 'string',
    'string': 'string',
    'date': '2017-01-01',
    'datetime': '2017-01-01T00:00:00+00:00',
    'bool': True,
    'int': 0,
    'integer': 0,
    'float': 0.0
}

STORAGE_UNIT_MAP = {
    'MBs': 'Mbs',
    'KBs': 'Kbs',
    'GBs': 'Gbs'
}

# There are some intentional synonyms here (e.g. "str" and "string")
PRIMITIVE_TYPES_TO_EXAMPLE_KEY_VALUES = {
    'str': ['string1', 'string2'],
    'string': ['string1', 'string2'],
    'date': ['2017-01-01', '2017-01-02'],
    'datetime': ['2017-01-01T00:00:00+00:00', '2017-01-01T00:00:00+00:00'],
    'bool': [True, False],
    'int': [0, 1],
    'float': [0.0, 0.5]
}


def json_skeleton_generation_handler(input_params_to_complex_types={}, output_type=None):
    def inner_decorator(func):
        @functools.wraps(func)
        def wrapped_call(ctx, *args, **kwargs):
            try:
                cli_util.load_context_obj_values_from_defaults(ctx)

                ctx.obj['input_params_to_complex_types'] = input_params_to_complex_types
                ctx.obj['output_type'] = output_type

                if ctx.obj['generate_full_command_json_input'] and ctx.obj['generate_param_json_input']:
                    raise click.UsageError("Cannot specify both the --generate-full-command-json-input and --generate-param-json-input parameters")
                elif ctx.obj['generate_full_command_json_input']:
                    generate_json_skeleton_for_full_command(ctx)
                    sys.exit(0)
                elif ctx.obj['generate_param_json_input']:
                    generate_json_skeleton_for_option(ctx, ctx.obj['generate_param_json_input'])
                    sys.exit(0)

                func(ctx, *args, **kwargs)
            except cli_exceptions.RequiredValueNotInDefaultOrUserInputError as exception:
                if ctx.obj["debug"]:
                    raise
                tpl = "{usage}\n\nError: {details}"
                sys.exit(tpl.format(usage=ctx.get_usage(), details=str(exception)))
            except cli_exceptions.RequiredValueNotAvailableInternallyOrUserInputError as exception:
                if ctx.obj["debug"]:
                    raise
                tpl = "{usage}\n\nError: {details}"
                sys.exit(tpl.format(usage=ctx.get_usage(), details=str(exception)))
            except Exception as exception:
                if ctx.obj["debug"]:
                    raise
                tpl = "{exc}: {details}"
                sys.exit(tpl.format(exc=exception.__class__.__name__, details=str(exception)))

        return wrapped_call

    return inner_decorator


# This callback is intended to fire when someone specifies the --generate-full-command-json-input or --generate-param-json-input options.
# Since the intent of the option is that the caller wants to see example input rather than run the command, we flip any required commands
# to non-required. This will let us pass into the command method body and actually do the JSON rendering
#
# This path is a bit strange (e.g. why don't we just process JSON in the callback), but it's done like this because at the time the
# callback gets invoked the @json_skeleton_utils.json_skeleton_generation_handler decorator hasn't been processed and so we don't have
# enough of the metadata mapping to generate the JSON (this will be available once we pass into the method body)
def generate_json_skeleton_click_callback(ctx, param, value):
    if value:
        for p in ctx.command.params:
            if p.required:
                p.required = False
            if p.prompt:
                p.callback = None
                p.prompt = None

    return value


# Generates a JSON skeleton for a command based on a provided option value:
#
#    None: do nothing
#    <option name>: generates dummy JSON input for a given option. This is useful for complex parameter
#    types where the user is expected to provide some sort of JSON
def generate_json_skeleton_for_option(ctx, option_name):
    if option_name is None:
        return None

    if option_name not in ctx.obj['input_params_to_complex_types']:
        click.echo(message='Option {} is not a recognized complex type, so no example JSON can be produced. Invoke help for this command (--help/-h/-?) to see available documentation on this option'.format(option_name), file=sys.stderr)
    else:
        print(json.dumps(generate_input_dict_for_skeleton(ctx, option_name), indent=2, sort_keys=True))

    sys.exit(0)


# Generates a JSON skeleton for a full command. We assume that all the command information is available in the
# provided context
def generate_json_skeleton_for_full_command(ctx):
    print(json.dumps(generate_input_dict_for_skeleton(ctx), indent=2, sort_keys=True))
    sys.exit(0)


# Based on the current command (we assume all the information is available in the click Context), generate a dict
# which can be serialized to JSON and represent what input a user should provide if they want to give a JSON string
# or file rather than command line switches/options.
#
# Additionally, we can customize this so that instead of emitting JSON for the entire command, we can emit example
# JSON for a single option. This is useful if the option represents some JSON which a user would need to provide as
# a string or file
def generate_input_dict_for_skeleton(ctx, targeted_complex_param=None):
    input_params_to_complex_types = ctx.obj['input_params_to_complex_types']

    input_as_dict = {}
    inv_alias = {}
    already_processed_params = set()
    options = ctx.command.params  # This is an array of click.Option objects
    if 'parameter_aliases' in ctx.obj:
        inv_alias = {v[0]: k for k, v in ctx.obj['parameter_aliases'].items()}  # Inverse of the parameter aliases in rc

    # First we go through all the options and for the "simple" ones (i.e. those which are some sort of primitive type)
    # we add them to our dictionary. We also mark what params get processed so that we can remove any redundant elements
    # we pull in from the complex parameters
    for o in options:
        opts = o.opts
        option_type = o.type

        for opt_name in opts:
            if opt_name.find('--') == 0:
                leading_dashes_removed = opt_name[2:]

                # We don't want to include custom aliases in the JSON output.
                # Skip all aliases that were listed in the oci_cli_rc file.
                if opt_name in inv_alias:
                    continue

                # We don't need to include the help flag in the JSON, or the options which are used to signal
                # to generate JSON or pass in the command's input as JSON
                if leading_dashes_removed == 'help' or leading_dashes_removed == 'generate-full-command-json-input' or leading_dashes_removed == 'generate-param-json-input' or leading_dashes_removed == 'from-json':
                    continue

                if leading_dashes_removed not in input_params_to_complex_types:
                    attribute_name = camelize(leading_dashes_removed)
                    already_processed_params.add(attribute_name)
                    if option_type in CLICK_TYPES_TO_EXAMPLE_VALUES:
                        input_as_dict[attribute_name] = CLICK_TYPES_TO_EXAMPLE_VALUES[option_type]
                    elif isinstance(option_type, click.Choice):
                        if o.multiple:
                            input_as_dict[attribute_name] = ['|'.join(option_type.choices)]
                        else:
                            input_as_dict[attribute_name] = '|'.join(option_type.choices)
                    elif isinstance(option_type, click.File):
                        input_as_dict[attribute_name] = '/path/to/file'

    if targeted_complex_param is not None:
        tags_obj = get_example_object_for_tags(targeted_complex_param)
        if tags_obj:
            return tags_obj
        example_obj = translate_complex_param_to_example_object(input_params_to_complex_types[targeted_complex_param], set())

        # If this is a dictionary, remove any redundant elements from the top level (as they have
        # been splatted out of the complex param)
        remove_keys_if_dict(example_obj, already_processed_params)

        return example_obj

    # Complex parameters represent some sort of model type or at least something non-primitive like a list or a dict so
    # we'll represent them as a nested object inside the dict generated by this method
    for attr_name, complex_param_entry in six.iteritems(input_params_to_complex_types):
        tags_obj = get_example_object_for_tags(attr_name)
        if tags_obj:
            input_as_dict[camelize(attr_name)] = tags_obj
        else:
            example_obj = translate_complex_param_to_example_object(complex_param_entry, set())
            remove_keys_if_dict(example_obj, already_processed_params)
            input_as_dict[camelize(attr_name)] = example_obj

    return input_as_dict


def get_example_object_for_tags(targeted_complex_param):
    if targeted_complex_param in ["defined-tags", "definedTags"]:
        return generate_input_dict_for_defined_tags()
    if targeted_complex_param in ["freeform-tags", "freeformTags"]:
        return generate_input_dict_for_freeform_tags()

    return None


def generate_input_dict_for_defined_tags():
    dict = {}
    dict['tagNamespace1'] = {}
    dict['tagNamespace1']['tagKey1'] = 'tagValue1'
    dict['tagNamespace1']['tagKey2'] = 'tagValue2'
    dict['tagNamespace2'] = {}
    dict['tagNamespace2']['tagKey1'] = 'tagValue1'
    dict['tagNamespace2']['tagKey2'] = 'tagValue2'
    return dict


def generate_input_dict_for_freeform_tags():
    dict = {}
    dict['tagKey1'] = 'tagValue1'
    dict['tagKey2'] = 'tagValue2'
    return dict


def translate_complex_param_to_example_object(complex_param_entry, visited):
    cls = complex_param_entry['class']

    # For lists we produce an example 2 element list containing objects of whatever the list type is
    if cls.startswith('list['):
        sub_kls = re.match('list\[(.*)\]', cls).group(1)  # noqa: W605
        return [
            translate_complex_param_to_example_object({'module': complex_param_entry['module'], 'class': sub_kls}, visited),
            translate_complex_param_to_example_object({'module': complex_param_entry['module'], 'class': sub_kls}, visited)
        ]

    # For dictionaries we produce an example 2 element dictionary. We assume that dictionary keys are
    # some sort of primitive, though values may not be.
    #
    # Also, treat "object" as a generic JSON object by making it a dict of string to string. Since there isn't
    # any other type information this is our best guess (for a practical example of where this occurs, see
    # extended-metadata when launching an instance)
    if cls.startswith('dict(') or cls == 'object':
        if cls == 'object':
            key_sub_kls = 'str'
            value_sub_kls = 'str'
        else:
            key_sub_kls = re.match('dict\(([^,]*), (.*)\)', cls).group(1)    # noqa: W605
            value_sub_kls = re.match('dict\(([^,]*), (.*)\)', cls).group(2)  # noqa: W605

        value = translate_complex_param_to_example_object({'module': complex_param_entry['module'], 'class': value_sub_kls}, visited)
        return {PRIMITIVE_TYPES_TO_EXAMPLE_KEY_VALUES[key_sub_kls][0]: value, PRIMITIVE_TYPES_TO_EXAMPLE_KEY_VALUES[key_sub_kls][1]: value}

    # If the value is a primitive then just return an example value
    if cls in PRIMITIVE_TYPES_TO_EXAMPLE_SCALAR_VALUES:
        return PRIMITIVE_TYPES_TO_EXAMPLE_SCALAR_VALUES[cls]

    # If we're at this point, we're some sort of model object so pull out what class we actually are
    try:
        cls_type = cli_util.MODULE_TO_TYPE_MAPPINGS[complex_param_entry['module']][cls]
    except KeyError:
        # Temp fix: If we do not find the class in SDK mappings, return string
        # as it is due to the class not being generated for enums defined in the spec.
        return PRIMITIVE_TYPES_TO_EXAMPLE_SCALAR_VALUES['string']

    # Check if we already visited this Class, this is important to cut any cycle.
    if cls in visited:
        return None
    visited.add(cls)

    # If we have subclasses it gets a little odd to communicate the variants to cusomters. To do this, we create an array where
    # the first element is a warning that says it isn't actually an array and the remaining elements are examples of what the
    # subclasses look like so the caller can pick one
    subclasses = cls_type.__subclasses__()
    subclasses = sorted(subclasses, key=lambda x: x.__name__)
    if len(subclasses) > 0:
        subclass_definitions = ['This parameter should actually be a JSON object rather than an array - pick one of the following object variants to use']
        for sc in subclasses:
            subclass_definitions.append(translate_complex_param_to_example_object({'module': complex_param_entry['module'], 'class': sc.__name__}, visited))

        return subclass_definitions

    # If we've reached this point, we're some sort of model object so just translate it to a dictionary
    obj_as_dict = {}
    instance = cls_type()
    for attr_name, attr_type in sorted(instance.swagger_types.items()):
        property_name = instance.attribute_map[attr_name]
        attribute_value = getattr(instance, attr_name, None)

        # If the field name is definedTags or freeformTags, add tags examples
        tags_obj = get_example_object_for_tags(property_name)
        if tags_obj:
            obj_as_dict[property_name] = tags_obj
        elif attribute_value is not None:
            # If there is some sort of default value then use it. This is useful in cases like subclasses where the type field is prepopulated
            # with information
            obj_as_dict[property_name] = attribute_value
        elif attr_type in PRIMITIVE_TYPES_TO_EXAMPLE_SCALAR_VALUES:
            obj_as_dict[property_name] = PRIMITIVE_TYPES_TO_EXAMPLE_SCALAR_VALUES[attr_type]
        else:
            obj_as_dict[property_name] = translate_complex_param_to_example_object({'module': complex_param_entry['module'], 'class': attr_type}, visited)
    visited.remove(cls)
    return obj_as_dict


# Callback which will be invoked if someone specifies the --from-json argument and provides either a file or a JSON string. This will
# parse the JSON and assign entries to the default_map of the provided context. The default_map is used as a source of default values if the
# command caller hasn't provided a parameter value, so it can support scenarios where a caller provides all of the command input in the JSON
# (as then everything will be sourced from the default_map). However, if the caller explicitly provides an option value it will be used instead
# of whatever is in the default map - this lets us support the scenario where someone provides the JSON input and then selectively overrides a couple
# of options.
#
# The --from-json option (& callback) is eager evaluated, so it should run before other options are processed. There are some caveats around eager
# callbacks in that click honours whatever order it was provided by the user in the command line (see: http://click.pocoo.org/5/advanced/#callback-evaluation-order).
#
# This means for the purposes of having an eager callback option which actually sets/modifies values that we want the command to subsequently use (e.g. in the default
# map) there should be only one (like Highlander) because if there is more than one we can't control the order without additional complexity.
def cli_json_input_callback(ctx, param, value):
    if hasattr(param, 'type') and isinstance(param.type, CliFromJson):
        ctx.obj['input_params_to_complex_types'] = param.type.json_input_metadata

    parsed_json = cli_util.parse_json_parameter('from-json', value)
    if parsed_json:
        # We need to have some sort of key-value mapping at the top level in order to work propery.
        # If someone passes us an array of JSON objects, that's valid JSON and will parse successfully but
        # we won't really know how to grab value out of it and map it to parameters
        if not isinstance(parsed_json, abc.Mapping):
            sys.exit('We expect a JSON object to be provided to --from-json')

        option_name_to_cannonical_name = {}
        for param in ctx.command.params:
            for o in param.opts:
                if o.startswith('--'):
                    option_name_to_cannonical_name[o[2:]] = param.name
                elif o.startswith('-'):
                    option_name_to_cannonical_name[o[1:]] = param.name

        if ctx.default_map is None:
            ctx.default_map = {}
        for key, val in six.iteritems(parsed_json):
            # Even if parsed_json[key] represents a JSON object or an array of JSON objects, we will leave their keys as-is without
            # converting them to underscores. The reason for this is that the top-level keys correspond to named parameters we pass
            # to each command method and so we underscore their names to help map the key to the named parameter.
            #
            # Deeper than that we're dealing with a complex object which a customer would usually pass as a command line argument
            # as a JSON string or a reference to a JSON file, in which case it's just going to get shuttled along to the underlying
            # Python SDK functionality anyway, so we leave it untouched
            for unit in STORAGE_UNIT_MAP:
                if key.endswith(unit):
                    key = key.replace(unit, STORAGE_UNIT_MAP[unit])
            underscored_key = underscore(key)
            ctx.default_map[underscored_key] = val

            if underscored_key in option_name_to_cannonical_name:
                ctx.default_map[option_name_to_cannonical_name[underscored_key]] = val

    return value


def get_cli_json_input_option(json_metadata):
    return click.option(
        '--from-json',
        type=CliFromJson(json_metadata),
        is_eager=True,
        callback=cli_json_input_callback,
        help="""Provide input to this command as a JSON document from a file using the file://path-to/file syntax.

        The --generate-full-command-json-input option can be used to generate a sample json file to be used with this command option. The key names are pre-populated and match the command option names (converted to camelCase format, e.g. compartment-id --> compartmentId), while the values of the keys need to be populated by the user before using the sample file as an input to this command. For any command option that accepts multiple values, the value of the key can be a JSON array.

        Options can still be provided on the command line. If an option exists in both the JSON document and the command line then the command line specified value will be used.

        For examples on usage of this option, please see our "using CLI with advanced JSON options" link: https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSONOptions""")


# Intended for when we take in params from **kwargs in an _extended CLI and then shuttle them down to a corresponding command in a
# generated/ CLI. In this case, because the JSON skeleton parameters have already been evaluated in the _extended CLI we don't want
# to re-evaluate them in the generated/ one
def remove_json_skeleton_params_from_dict(target_dict):
    target_dict.pop('generate_param_json_input', None)
    target_dict.pop('generate_full_command_json_input', None)
    target_dict.pop('from_json', None)


def remove_keys_if_dict(obj, keys):
    if type(obj) is dict:
        for k in keys:
            obj.pop(k, None)
