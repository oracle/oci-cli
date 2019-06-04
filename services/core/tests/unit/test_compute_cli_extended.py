# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util


class TestCompute(unittest.TestCase):
    def setUp(self):
        pass

    def test_volume_attachment(self):
        result = util.invoke_command(['compute', 'volume-attachment', 'attach-paravirtualized-volume'])
        assert 'Error: Missing option(s)' in result.output

        result = util.invoke_command(['compute', 'volume-attachment', 'attach'])
        assert 'Error: Missing option(s)' in result.output

        result = util.invoke_command(['compute', 'volume-attachment', 'attach', '--type', 'x'])
        assert 'Error: Invalid value for "--type":' in result.output
        assert '(choose from service_determined, emulated, iscsi, paravirtualized)' in result.output

        result = util.invoke_command(['compute', 'volume-attachment', 'attach', '--type', 'service_determined'])
        assert 'Error: Missing option(s)' in result.output
        result = util.invoke_command(['compute', 'volume-attachment', 'attach', '--type', 'emulated'])
        assert 'Error: Missing option(s)' in result.output
        result = util.invoke_command(['compute', 'volume-attachment', 'attach', '--type', 'iscsi'])
        assert 'Error: Missing option(s)' in result.output
        result = util.invoke_command(['compute', 'volume-attachment', 'attach', '--type', 'paravirtualized'])
        assert 'Error: Missing option(s)' in result.output

    def test_attach_iscsi_volume(self):
        result = util.invoke_command(['compute', 'volume-attachment'])
        assert 'attach-iscsi-volume' in result.output

        result = util.invoke_command(['compute', 'volume-attachment', 'attach-iscsi-volume'])
        assert 'Error: Missing option(s) --instance-id, --volume-id.' in result.output
