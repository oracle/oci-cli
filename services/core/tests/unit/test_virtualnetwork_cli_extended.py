# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util


class TestNetwork(unittest.TestCase):
    def setUp(self):
        pass

    def nsg_wrong_param_name(self, operation):
        result = util.invoke_command(['network', 'nsg'] + operation + ['--network-security-group-id'])
        assert 'Error: no such option:' in result.output
        assert 'network-security-group-id' in result.output

    def nsg_correct_param_name(self, operation, other_params, force):
        result = util.invoke_command(['network', 'nsg'] + operation + ['--nsg-id', 'dummy'] + other_params + (['--force'] if force else []))
        assert 'ServiceError' in result.output

    def nsg_correct_empty_param_name(self, operation, other_params, force):
        result = util.invoke_command(['network', 'nsg'] + operation + ['--nsg-id', ''] + other_params + (['--force'] if force else []))
        assert 'UsageError: Parameter --nsg-id cannot be whitespace or empty string' in result.output

    def nsg_param_checks(self, operation, other_params=[], force=False):
        self.nsg_wrong_param_name(operation)
        self.nsg_correct_param_name(operation, other_params, force)
        self.nsg_correct_empty_param_name(operation, other_params, force)

    def test_nsg_id_options(self):
        self.nsg_param_checks(['change-compartment'], other_params=['--compartment-id', 'dummy'])
        self.nsg_param_checks(['delete'], force=True)
        self.nsg_param_checks(['get'])
        self.nsg_param_checks(['rules', 'add'])
        self.nsg_param_checks(['rules', 'list'])
        self.nsg_param_checks(['rules', 'remove'])
        self.nsg_param_checks(['rules', 'update'])
        self.nsg_param_checks(['vnics', 'list'])
