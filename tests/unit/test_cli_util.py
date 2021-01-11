# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
import oci
import tempfile
import unittest
from oci_cli import cli_util


# Trivial object to provide dictionary and dot accessor capabilities
class Obj(dict):
    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Obj, self).__setitem__(key, value)
        self.__dict__.update({key: value})


class Mock():
    expected_result = None

    @staticmethod
    def build_config(ctx):
        return Mock.expected_result


class TestCliUtil(unittest.TestCase):

    def test_iam_coalesce_provided_and_default_value(self):
        ctx = Obj()
        ctx.obj = Obj()
        ctx.obj['parameter_aliases'] = {}
        ctx.obj['default_values_from_file'] = {}

        ctx.info_name = ""
        ctx.command = Obj()
        ctx.command.params = {}
        ctx.command.name = "list"

        ctx.parent = Obj()
        ctx.parent.info_name = ""
        ctx.parent.command = Obj()
        ctx.parent.command.name = "compartment"

        ctx.parent.parent = Obj()
        ctx.parent.parent.info_name = ""
        ctx.parent.parent.command = Obj()
        ctx.parent.parent.command.name = "iam"

        ctx.parent.parent.parent = Obj()
        ctx.parent.parent.parent.info_name = ""
        ctx.parent.parent.parent.command = Obj()
        ctx.parent.parent.parent.command.name = "oci"

        ctx.parent.parent.parent.parent = None

        is_required = True
        original_value = None

        # Test "oci iam compartment list"
        # No default value, no config value
        param_name = "compartment-id"
        value = None
        try:
            value = cli_util.coalesce_provided_and_default_value(ctx, param_name, original_value, is_required)
        except Exception:
            pass
        assert value is None

        # No default value but config value
        is_required = True
        cli_util.build_config = Mock.build_config
        Mock.expected_result = {'tenancy': 'abc'}
        value = cli_util.coalesce_provided_and_default_value(ctx, param_name, original_value, is_required)
        assert value == 'abc'

        # Default value and config value
        ctx.obj['default_values_from_file'] = {'compartment-id': 'xyz'}
        value = cli_util.coalesce_provided_and_default_value(ctx, param_name, original_value, is_required)
        assert value == 'xyz'

        # Default value but no config value
        Mock.expected_result = {}
        ctx.obj['default_values_from_file'] = {'compartment-id': 'xyz'}
        value = cli_util.coalesce_provided_and_default_value(ctx, param_name, original_value, is_required)
        assert value == 'xyz'

        # Test "oci iam compartment get" -- this should not use the config
        ctx.command.name = "get"
        Mock.expected_result = {'tenancy': 'abc'}
        ctx.obj['default_values_from_file'] = {}
        value = None
        try:
            value = cli_util.coalesce_provided_and_default_value(ctx, param_name, original_value, is_required)
        except Exception:
            pass
        assert value is None

        # Test "oci iam region-subscription list" which uses tenancy-id instead of compartment-id
        ctx.parent.command.name = "region-subscription"
        ctx.command.name = "list"
        param_name = "tenancy-id"
        Mock.expected_result = {'tenancy': 'abc'}
        value = cli_util.coalesce_provided_and_default_value(ctx, param_name, original_value, is_required)
        assert value == 'abc'

    # TODO: This test does not work on Windows due to the use of tempfile.NamedTemoraryFile.
    # https://bugs.python.org/issue14243
    def test_coalesce_param_with_explicit_default_value_for_file_type_param(self):
        ctx = Obj()
        ctx.obj = Obj()
        ctx.obj['parameter_aliases'] = {}
        ctx.obj['default_values_from_file'] = {}
        ctx.obj['parameter_lookup_heirarchy'] = []

        ctx.command = Obj()
        ctx.command.params = []

        param = Obj()
        param.type = click.File(mode='r')
        param.name = 'test'

        ctx.call_on_close = lambda x: x

        with tempfile.NamedTemporaryFile() as f:
            value = cli_util._coalesce_param(ctx, param, None, False, explicit_default=f.name)

            # ensure that returned value is a file handle, not a string
            assert hasattr(value, 'read')

    def test_get_possible_subtype_based_on_payload(self):
        payload = {
            'instanceType': 'compute',
            'instanceDetails': {}
        }

        subtype = cli_util.get_possible_subtype_based_on_payload(oci.core.models.InstanceConfigurationInstanceDetails, 'core', payload)
        assert subtype.__class__.__name__ == 'ComputeInstanceDetails'
