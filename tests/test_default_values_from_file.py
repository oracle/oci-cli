import click
import os
import pytest

import oci_cli


def test_not_required_value_provided_default_exists():
    context = set_up_context()
    context.obj['default_values_from_file']['param'] = 'A different value'

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', 'A value', False)

    assert coalesced_value == 'A value'


def test_not_required_value_not_provided_default_exists():
    context = set_up_context()
    context.obj['default_values_from_file']['param'] = 'A different value'

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', None, False)

    assert coalesced_value == 'A different value'


def test_not_required_value_not_provided_default_not_exists():
    context = set_up_context()

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', None, False)

    assert coalesced_value is None


def test_required_value_provided_default_exists():
    context = set_up_context()
    context.obj['default_values_from_file']['param'] = 'A different value'

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', 'A value', True)

    assert coalesced_value == 'A value'


def test_required_value_not_provided_default_exists():
    context = set_up_context()
    context.obj['default_values_from_file']['param'] = 'A different value'

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', None, True)

    assert coalesced_value == 'A different value'


def test_required_value_not_provided_default_not_exists():
    context = set_up_context()

    with pytest.raises(oci_cli.cli_exceptions.RequiredValueNotInDefaultOrUserInputError):
        oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', None, True)


def test_command_level_default_used():
    context = set_up_context()
    context.obj['default_values_from_file']['param'] = 'top-level'
    context.obj['default_values_from_file']['cmdgrp.param'] = 'cmdgrp-level'
    context.obj['default_values_from_file']['cmdgrp.subgrp.param'] = 'subgrp-level'
    context.obj['default_values_from_file']['cmdgrp.subgrp.cmd.param'] = 'cmd-level'

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', None, False)

    assert coalesced_value == 'cmd-level'


def test_sub_group_level_default_used():
    context = set_up_context()
    context.obj['default_values_from_file']['param'] = 'top-level'
    context.obj['default_values_from_file']['cmdgrp.param'] = 'cmdgrp-level'
    context.obj['default_values_from_file']['cmdgrp.subgrp.param'] = 'subgrp-level'

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', None, False)

    assert coalesced_value == 'subgrp-level'


def test_command_group_level_default_used():
    context = set_up_context()
    context.obj['default_values_from_file']['param'] = 'top-level'
    context.obj['default_values_from_file']['cmdgrp.param'] = 'cmdgrp-level'

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', None, False)

    assert coalesced_value == 'cmdgrp-level'


def test_top_level_default_used():
    context = set_up_context()
    context.obj['default_values_from_file']['param'] = 'top-level'

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', None, False)

    assert coalesced_value == 'top-level'


def test_param_lookup_heirarchy_generation():
    context = set_up_context()

    generated_heirarchy = oci_cli.cli_util.get_param_lookup_heirarchy_from_context(context)
    expected_heirarchy = ["cmdgrp.subgrp.cmd", "cmdgrp.subgrp", "cmdgrp", ""]

    assert expected_heirarchy == generated_heirarchy


def test_load_context_object_when_values_not_already_in_obj():
    context = set_up_context()

    context.obj['default_values_from_file']['cmdgrp.debug'] = True
    context.obj['default_values_from_file']['region'] = 'my region'
    context.obj['default_values_from_file']['cmdgrp.subgrp.cmd.endpoint'] = 'https://some.endpoint'
    context.obj['default_values_from_file']['cmdgrp.subgrp.cert-bundle'] = '/path/to/my/bundle'
    context.obj['default_values_from_file']['cmdgrp.output'] = 'json'

    oci_cli.cli_util.load_context_obj_values_from_defaults(context)

    assert context.obj['debug']
    assert context.obj['region'] == 'my region'
    assert context.obj['endpoint'] == 'https://some.endpoint'
    assert context.obj['cert_bundle'] == '/path/to/my/bundle'
    assert context.obj['output'] == 'json'


def test_load_context_object_when_values_already_in_obj():
    context = set_up_context()

    context.obj['debug'] = False
    context.obj['region'] = 'do-not-change'
    context.obj['endpoint'] = 'https://no.replace'
    context.obj['cert_bundle'] = '/do/not/change/this/path'
    context.obj['output'] = 'table'

    context.obj['default_values_from_file']['cmdgrp.debug'] = True
    context.obj['default_values_from_file']['region'] = 'my region'
    context.obj['default_values_from_file']['endpoint'] = 'https://some.endpoint'
    context.obj['default_values_from_file']['cert-bundle'] = '/path/to/my/bundle'
    context.obj['default_values_from_file']['cmdgrp.subgrp.cert-bundle'] = '/path/to/my/bundle'
    context.obj['default_values_from_file']['cmdgrp.output'] = 'json'

    oci_cli.cli_util.load_context_obj_values_from_defaults(context)

    assert context.obj['debug']
    assert context.obj['region'] == 'do-not-change'
    assert context.obj['endpoint'] == 'https://no.replace'
    assert context.obj['cert_bundle'] == '/do/not/change/this/path'
    assert context.obj['output'] == 'table'


def test_flag_parameter_handling():
    command_with_flag = click.Command(
        'unit-test-command',
        params=[click.Option(['--param'], is_flag=True)]
    )
    context = set_up_context(command_with_flag)

    context.obj['default_values_from_file']['param'] = True

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', False, False)
    assert coalesced_value

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', True, False)
    assert coalesced_value

    context.obj['default_values_from_file'].pop('param')
    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', False, False)
    assert not coalesced_value


def test_param_type_conversions():
    command_with_different_types = click.Command(
        'unit-test-command',
        params=[
            click.Option(['--param'], type=click.STRING),
            click.Option(['--param2'], type=click.INT),
            click.Option(['--param3'], type=click.FLOAT),
            click.Option(['--param-truthy-bool'], type=click.BOOL),
            click.Option(['--param-falsey-bool'], type=click.BOOL),
            click.Option(['--param4'], type=click.UNPROCESSED)
        ]
    )
    context = set_up_context(command_with_different_types)

    context.obj['default_values_from_file']['param'] = 'hello world'
    context.obj['default_values_from_file']['cmdgrp.param2'] = '55'
    context.obj['default_values_from_file']['cmdgrp.subgrp.param3'] = '17.5'
    context.obj['default_values_from_file']['cmdgrp.subgrp.cmd.param-truthy-bool'] = 'true'
    context.obj['default_values_from_file']['cmdgrp.subgrp.cmd.param-falsey-bool'] = 'no'
    context.obj['default_values_from_file']['cmdgrp.subgrp.cmd.param5'] = 'hello again world'

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', None, False)
    assert 'hello world' == coalesced_value

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param2', None, False)
    assert 55 == coalesced_value

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param3', None, False)
    assert 17.5 == coalesced_value

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param-truthy-bool', None, False)
    assert coalesced_value

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param-falsey-bool', None, False)
    assert not coalesced_value

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param5', None, False)
    assert 'hello again world' == coalesced_value


def test_param_type_conversions_when_param_accepts_multiple():
    command_with_different_types = click.Command(
        'unit-test-command',
        params=[
            click.Option(['--param'], type=click.STRING, multiple=True),
            click.Option(['--param2'], type=click.INT, multiple=True),
            click.Option(['--param3'], type=click.FLOAT, multiple=True),
            click.Option(['--param-truthy-bool'], type=click.BOOL, multiple=True),
            click.Option(['--param-falsey-bool'], type=click.BOOL, multiple=True),
            click.Option(['--param4'], type=click.UNPROCESSED, multiple=True)
        ]
    )
    context = set_up_context(command_with_different_types)

    context.obj['default_values_from_file']['param'] = 'hello world\nitem two\nitem three'
    context.obj['default_values_from_file']['cmdgrp.param2'] = '55\n65\n77'
    context.obj['default_values_from_file']['cmdgrp.subgrp.param3'] = '17.5\n16\n99.99'
    context.obj['default_values_from_file']['cmdgrp.subgrp.cmd.param-truthy-bool'] = 'true\ny\n1\nyes\non'
    context.obj['default_values_from_file']['cmdgrp.subgrp.cmd.param-falsey-bool'] = 'no\n0\nfalse\nn'
    context.obj['default_values_from_file']['cmdgrp.subgrp.cmd.param4'] = 'hello again world\nunprocessed type\nanother entry'

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', None, False)
    assert ['hello world', 'item two', 'item three'] == coalesced_value

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param2', None, False)
    assert [55, 65, 77] == coalesced_value

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param3', None, False)
    assert [17.5, 16, 99.99] == coalesced_value

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param-truthy-bool', None, False)
    assert [True, True, True, True, True] == coalesced_value

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param-falsey-bool', None, False)
    assert [False, False, False, False] == coalesced_value

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param4', None, False)
    assert ['hello again world', 'unprocessed type', 'another entry'] == coalesced_value


def test_variable_expansion():
    os.environ['TO_SUB'] = "substitute"

    context = set_up_context()
    context.obj['default_values_from_file']['param'] = 'top-level'
    context.obj['default_values_from_file']['cmdgrp.param'] = 'You should $TO_SUB me'

    coalesced_value = oci_cli.cli_util.coalesce_provided_and_default_value(context, 'param', None, False)

    assert coalesced_value == 'You should substitute me'


def set_up_context(command=click.Command('unit-test-command')):
    context_obj = {'default_values_from_file': {}, 'parameter_aliases': {}}

    top_context = click.Context(command, parent=None, info_name='oci')
    command_group_context = click.Context(command, parent=top_context, info_name='cmdgrp')
    command_subgroup_context = click.Context(command, parent=command_group_context, info_name='subgrp')
    command_context = click.Context(command, parent=command_subgroup_context, info_name='cmd', obj=context_obj)

    return command_context
