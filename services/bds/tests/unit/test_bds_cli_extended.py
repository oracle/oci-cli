# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util


class TestBds(unittest.TestCase):
    def setUp(self):
        pass

    def test_bds_instance_rename(self):
        result = util.invoke_command(['bds', 'bds-instance'])
        assert 'Error: No such command "bds-instance"' in result.output
        result = util.invoke_command(['bds', 'instance'])
        assert 'Usage: oci bds instance' in result.output

    def test_bds_work_request_logs_rename(self):
        result = util.invoke_command(['bds', 'work-request-log-entry', 'list-work-request-logs'])
        assert 'Error: No such command "list-work-request-logs"' in result.output
        result = util.invoke_command(['bds', 'work-request-log-entry', 'list'])
        assert 'Usage: oci bds work-request-log-entry list' in result.output

    def test_bds_add_worker_nodes_command(self):
        result = util.invoke_command(['bds', 'instance', 'add'])
        assert 'Error: No such command "add"' in result.output
        result = util.invoke_command(['bds', 'instance', 'worker-nodes', 'add'])
        assert 'Usage: oci bds instance worker-nodes add' in result.output

    def test_bds_added_commands(self):
        result = util.invoke_command(['bds', 'block-storage', 'add'])
        assert 'Usage: oci bds block-storage add' in result.output
        result = util.invoke_command(['bds', 'cloudsql', 'add'])
        assert 'Usage: oci bds cloudsql add' in result.output
        result = util.invoke_command(['bds', 'cloudsql', 'add'])
        assert 'Usage: oci bds cloudsql add' in result.output
