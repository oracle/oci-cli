# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import datetime
import unittest
import json
import oci_cli
from . import command_coverage_validator
from . import util


DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


class TestAudit(unittest.TestCase):

    @command_coverage_validator.CommandCoverageValidator(oci_cli.audit_cli.audit_group, expected_not_called_count=2)
    def test_all_operations(self, validator):
        """Successfully calls every operation with basic options."""
        self.validator = validator

        self.subtest_event_list()
        self.subtest_config_get()

    def subtest_config_get(self):
        util.set_admin_pass_phrase()
        result = util.invoke_command_as_admin(['audit', 'config', 'get', '--compartment-id', util.TENANT_ID])
        util.unset_admin_pass_phrase()
        util.validate_response(result)
        response = json.loads(result.output)
        assert response["data"]["retention-period-days"] is not None

    def subtest_event_list(self):
        end_time = datetime.datetime.utcnow()
        start_time = end_time + datetime.timedelta(days=-1)
        result = self.invoke(['audit', 'event', 'list', '--compartment-id', util.COMPARTMENT_ID, '--start-time', start_time.strftime(DATETIME_FORMAT), '--end-time', end_time.strftime(DATETIME_FORMAT)])
        assert result.exit_code == 0
        if result.output:
            response = json.loads(result.output)
            for event in response["data"]:
                assert util.COMPARTMENT_ID == event["compartment-id"]

    def invoke(self, commands, debug=False, ** args):
        self.validator.register_call(commands)

        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, ** args)


if __name__ == '__main__':
    unittest.main()
