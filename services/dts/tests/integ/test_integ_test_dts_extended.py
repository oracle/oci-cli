# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os
import sys
import re
import json
import click
import pytest
import unittest
from tests import test_config_container
from tests import util

CASSETTE_LIBRARY_DIR = 'services/dts/tests/cassettes'

# To test on PHX, set PHX config to DEFAULT profile, change to R1 if needed
REGION = "DEFAULT"
BUCKET_NAME = "dtsIntegTestBucket"

# Requires following env variables to be sourced:
# export OCI_CLI_CONFIG_FILE=<path/to/.oci/config>
# export OCI_CLI_COMPARTMENT_ID=<ocid-of-test-tenancy>


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('dts_integ_tests.yml'):
        yield


class IntegTestDTS(unittest.TestCase):

    def setUp(self):
        self.config = {
            "$COMPARTMENT": os.environ["OCI_CLI_COMPARTMENT_ID"],
            "$JOB_ID": "NOT_POPULATED",
            "$BUCKET": BUCKET_NAME,
            "$APPLIANCE_LABEL": "NOT_POPULATED",
            "$EXPORT_JOB_ID": "NOT_POPULATED",
        }
        if REGION == "R1":
            self.config.update({"$CERT_BUNDLE_PATH": "~/.oci/combined_r1.crt"})

        self.commands = [
            {"verb": "list",
             "command_data":
                 ["dts", "job", "list", "--compartment-id", "$COMPARTMENT"]},
            {"verb": "create",
             "command_data":
                 ["dts", "job", "create",
                  "--compartment-id", "$COMPARTMENT", "--bucket", "$BUCKET", "--display-name", "oci-cli-test-job-1",
                  "--device-type", "APPLIANCE", '--skip-upload-user-check'], "extract_from_output": {"id": "$JOB_ID"}},
            {"verb": "update",
             "command_data":
                 ["dts", "job", "update", "--job-id", "$JOB_ID", "--display-name", "oci-cli-test-job-2"]},
            {"verb": "delete",
             "command_data":
                ["dts", "job", "delete", "--force", "--job-id", "$JOB_ID"]},

            {"verb": "export-job-list",
             "command_data":
                 ["dts", "export", "list", "--compartment-id", "$COMPARTMENT"]},
            {"verb": "export-job-create",
             "command_data":
                 ["dts", "export", "create",
                  "--compartment-id", "$COMPARTMENT", "--bucket-name", "$BUCKET", "--display-name", "oci-cli-test-export-job-1",
                  "--addressee", "John New Doe", "--care-of", "Oracle New", "--address1", "4110 Network Circle New",
                  "--city-or-locality", "Santa Clara New", "--state-province-region", "CA", "--country", "US", "--zip-postal-code",
                  "95057", "--phone-number", "123-456-7999", "--email", "john.doe.new@or.com", "--setup-notifications", 'False'],
                 "extract_from_output": {"id": "$EXPORT_JOB_ID"}},
            {"verb": "export-job-update",
             "command_data":
                 ["dts", "export", "update", "--job-id", "$EXPORT_JOB_ID", "--phone-number", "123-456-7890", "--force"]},
            {"verb": "export-job-delete",
             "command_data":
                ["dts", "export", "delete", "--job-id", "$EXPORT_JOB_ID", "--force"]},
        ]

    def test_dts(self):
        click.echo("")
        for command in self.commands:
            command_data = command["command_data"]
            if REGION == "R1":
                command_data.append("--cert-bundle")
                command_data.append("$CERT_BUNDLE_PATH")
            for i, val in enumerate(command_data):
                if val in self.config:
                    command_data[i] = self.config[val]
            cmd_output = self._execute(command_data)
            click.echo("%s-output=\n%s" % (command["verb"], json.dumps(cmd_output, indent=2)))
            try:
                output_var = command["extract_from_output"]
            except Exception as extract_output_var:
                output_var = {}
            for extract_key in output_var:
                if cmd_output is not None:
                    self.config[output_var[extract_key]] = cmd_output["data"][extract_key]
                    click.echo(
                        "Extracted from output:%s=%s" % (output_var[extract_key], cmd_output["data"][extract_key]))
        click.echo("All tests passed successfully")

    def _execute(self, command):
        click.echo("command=%s" % command)
        result = util.invoke_command(command)
        output = result.output
        print("Raw Output=%s" % (output))
        cmd_output = {}  # when output_str is empty. Applicable ONLY for delete operations

        if result.exit_code == 0:
            try:
                json_match = re.search(r"({[\s\S]+\n})", output)
                if json_match:
                    cmd_output = json_match.group(0)
                    cmd_output = json.loads(cmd_output)
            except Exception as JSONDecodeError:
                return cmd_output
            return cmd_output
        else:
            sys.exit("Command %s\n  Exception:%s" % (command, result.exception))
