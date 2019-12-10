# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import os
import json
import click
import pytest
import unittest
from tests import test_config_container
from tests import util

CASSETTE_LIBRARY_DIR = 'services/dts/tests/cassettes'

# To test on R1, set this value to R1. By default, the region is DESKTOP so make sure you have the DTS control plane
# running locally
REGION = "DESKTOP"


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('dts_integ_tests.yml'):
        yield


class IntegTestDTS(unittest.TestCase):
    class TestResult():
        Success = 1
        Skipped = 2
        Failed = 3

    def setUp(self):
        self.command_prefix = ["dts"]
        self.config = {
            "$COMPARTMENT": os.environ["OCI_CLI_COMPARTMENT_ID"],
            "$PROFILE": "DESKTOP",
            "$CERT_BUNDLE_PATH": "~/SDK/dts-oci-cli-env/dts-oci-cli-config/combined_r1.crt",
            "$BUCKET": "production_bucket",
            "$JOB_ID": "NOT_POPULATED",
            "$APPLIANCE_LABEL": "NOT_POPULATED",
        }

        self.commands = [
            {"verb": "list",
             "command_data":
                 ["job", "list", "--compartment-id", "$COMPARTMENT"]},
            {"verb": "create",
             "command_data":
                 ["job", "create",
                  "--compartment-id", "$COMPARTMENT", "--bucket", "$BUCKET", "--display-name", "oci-cli-test-job-1",
                  "--device-type", "APPLIANCE"], "extract_from_output": {"id": "$JOB_ID"}},
            {"verb": "update",
             "command_data":
                 ["job", "update", "--job-id", "$JOB_ID", "--display-name", "oci-cli-test-job-2"]},
            {"verb": "create",
             "command_data":
                 ["appliance", "request", "--job-id", "$JOB_ID", "--addressee",
                  "John Doe", "--care-of", "Oracle", "--address1", "4110 Network Circle", "--address2",
                  "Floor 3", "--address3", "Section 5", "--address4", "Cubicle 1234", "--city-or-locality",
                  "Santa Clara", "--state-province-region", "CA", "--country", "USA", "--zip-postal-code",
                  "95054", "--phone-number", "123-456-7890", "--email", "john.doe@or.com"],
             "extract_from_output": {"label": "$APPLIANCE_LABEL"}},
            {"verb": "list",
             "command_data":
                 ["appliance", "list", "--job-id", "$JOB_ID"]},
            {"verb": "show",
             "command_data":
                 ["appliance", "show", "--job-id", "$JOB_ID", "--appliance-label", "$APPLIANCE_LABEL"]},
            {"verb": "update",
             "command_data":
                 ["appliance", "update-shipping-address", "--job-id", "$JOB_ID", "--appliance-label",
                  "$APPLIANCE_LABEL", "--addressee", "John New Doe", "--care-of", "Oracle New",
                  "--address1", "4110 Network Circle New", "--address2", "Floor 3 New", "--address3", "Section 5 New",
                  "--address4", "Cubicle 1234 New", "--city-or-locality", "Santa Clara New",
                  "--state-province-region", "MI", "--country", "UK", "--zip-postal-code",
                  "95057", "--phone-number", "123-456-7999", "--email", "john.doe.new@or.com", "--force"]},
            {"verb": "delete",
             "command_data":
                 ["appliance", "delete", "--force", "--job-id", "$JOB_ID", "--appliance-label", "$APPLIANCE_LABEL"]},
            {"verb": "delete",
             "command_data":
                ["job", "delete", "--force", "--job-id", "$JOB_ID"]},
        ]

    def test_dts(self):
        success_count = 0
        failed_count = 0
        skipped_count = 0
        click.echo("")
        for command in self.commands:
            command_data = command["command_data"]
            if REGION == "DESKTOP":
                command_data.append("--endpoint")
                command_data.append("http://localhost:19000")
            else:
                command_data.append("--cert-bundle")
                command_data.append("$CERT_BUNDLE_PATH")
            command_data.append("--profile")
            command_data.append("$PROFILE")
            for i, val in enumerate(command_data):
                if val in self.config:
                    command_data[i] = self.config[val]
            ret, j = self._execute(command_data)
            if ret == 0:
                success_count += 1
            else:
                failed_count += 1
                click.echo("command=%s, Error=%d, output=%s" % (command["verb"], ret, json.dumps(j, indent=2)))
                continue
            click.echo("%s-output=\n%s" % (command["verb"], json.dumps(j, indent=2)))
            try:
                kv = command["extract_from_output"]
            except Exception as e:
                kv = {}
            for k in kv:
                if j is not None:
                    self.config[kv[k]] = j["data"][k]
                    click.echo("Extracted from output:%s=%s" % (kv[k], j["data"][k]))

        click.echo("Tests: success=%d, failures=%d, skipped=%d" % (success_count, failed_count, skipped_count))

    def _execute(self, command):
        j_out = {}
        ret = 0
        try:
            command = self.command_prefix + command
            click.echo("command=%s" % (command))
            result = util.invoke_command(command)
            s = result.output
            print("Output=%s" % (s))
            if len(s) > 0:
                try:
                    j_out = json.loads(s)
                except Exception as e:
                    j_out = None
        except Exception as e:
            click.echo("_execute() Exception:%s" % (repr(e)))
            ret = -1
        finally:
            return ret, j_out
