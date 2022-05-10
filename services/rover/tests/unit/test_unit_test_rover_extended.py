# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


# A note on the tests.
# These tests are for asserting the command line syntax.
# These tests do NOT need to connect to the control plane.
# Tests:
# test-1: Run command without any arguments.
#      Assert that the output is reporting missing params for all REQUIRED params.
# test-2: Supply all required args
#     Assert that we get a 404 or 401. config.unittest has valid cred for R1 so that it connects.
# test-3: Supply all required AND optional params
#     Assert the same as test-2.
#     This tests that the command accepts all optional params.

import enum
import json
import click
import pytest
import unittest
import random

from tests import test_config_container
from tests import util

import mock
from oci.response import Response
from oci.request import Request

CASSETTE_LIBRARY_DIR = 'services/rover/tests/cassettes'


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('rover_unit_tests.yml'):
        yield


def get_mock_context():
    context_obj = {'config': {'log_requests': False, 'additional_user_agent': '', 'pass_phrase': None,
                              'user': 'ocid1.user.oc1..test-user', 'fingerprint': '00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00',
                              'key_file': '/fakepath/.oci/oci_api_key.pem', 'tenancy': 'ocid1.tenancy.oc1..tenancy-id',
                              'region': 'us-phoenix-1'},
                   'region': 'us-phoenix-1'}
    return click.Context(click.Command('unit-test-command', params={}), parent=None,
                         info_name='unit-test',
                         obj=context_obj)


class mock_compute_img_obj():
    class data:
        display_name = 'name1'
        size_in_mbs = 123
        compartment_id = 'compartment1'


class mock_object_storage_obj():
    class data:
        compartment_id = 'compartment1'


class UnitTestRover(unittest.TestCase):
    class TestResult(enum.Enum):
        Success = 1
        Skipped = 2
        Failed = 3

    class TestType(enum.Enum):
        # NoArgs = "NoArgs"
        OnlyRequiredArgs = "OnlyRequiredArgs"
        AllArgs = "AllArgs"
        GenFullCommandFromJson = "GenFullCommandFromJson"

    Missing_params_Text = "Error: Missing option(s)"

    def setUp(self):
        self.test_specific_set = {}  # When empty, all tests are run.

        self.specific_arg_values = {"profile": "DEFAULT", "if-match": "True", "all": None, 'cluster-workloads': None, 'cluster-type': ["STANDALONE", "STATION"],
                                    'cluster-size': str(random.randint(5, 30)), 'node-workloads': None, "wait": None, "lifecycle-state": "CREATING",
                                    'shipping-preference': 'ORACLE_SHIPPED', 'type': ["BUCKET", "IMAGE"],
                                    "test_defined_tag": '{"string1": "string", "string2": "string"}', "force": None,
                                    "debug": None, "super-user-password": None, "unlock-passphrase": None, "subscription-id": "test subscription-id"}
        self.complex_data_defs = {
            "customer-shipping-address": {
                "required_params": ["addressee", "care-of", "address1", "city-or-locality", "state-or-region",
                                    "country", "zipcode", "phone-number", "email"],
                "optional_params": ["address2", "address3", "address4"]
            },
            "freeform-tags": {
                "required_params": ["string1"],
                "optional_params": []
            },
            "defined-tags": {
                "required_params": ["test_defined_tag"],
                "optional_params": []
            },
        }

        self.cluster_subcommands = [
            {"sub_command": "create",
             "required_params": ["compartment-id", "display-name", "cluster-size", "cluster-type"],
             "optional_params": ["shipping-preference", "point-of-contact-phone-number", "point-of-contact",
                                 "addressee", "care-of", "address1",
                                 "city-or-locality", "state-province-region", "country", "zip-postal-code",
                                 "phone-number", "email", "freeform-tags", "defined-tags", "address2", "address3",
                                 "address4", "master-key-id", "policy-name", "policy-compartment-id"],
             },
            {"sub_command": "change-compartment",
             "required_params": ["compartment-id", "cluster-id"],
             "optional_params": ["if-match"]},
            {"sub_command": "delete",
             "required_params": ["cluster-id"],
             "optional_params": ["if-match", "force"]},
            {"sub_command": "show",
             "required_params": ["cluster-id"],
             "optional_params": []},
            {"sub_command": "update",
             "required_params": ["cluster-id"],
             "optional_params": ["addressee", "care-of", "address1",
                                 "city-or-locality", "lifecycle-state-details", "state-province-region",
                                 "country", "zip-postal-code", "phone-number", "email"]},
            {"sub_command": "request-approval",
             "required_params": ["cluster-id"],
             "optional_params": []},
            {"sub_command": "add-workload",
             "required_params": ["cluster-id", "type"],
             "test_necessary_params": ["bucket-name", "force"],
             "optional_params": ["prefix", "range-start", "range-end"]},
            {"sub_command": "add-workload",
             "required_params": ["cluster-id", "type"],
             "test_necessary_params": ["image-id", "force"],
             "optional_params": ["prefix", "range-start", "range-end"]},
            {"sub_command": "delete-workload",
             "required_params": [],
             "test_necessary_params": ["cluster-id", "force"],
             "optional_params": []},
            {"sub_command": "set-secrets",
             "required_params": ["cluster-id"],
             "test_necessary_params": [],
             "optional_params": ["super-user-password", "unlock-passphrase"],
             "methods_to_side_effect": {
                 "mock_prompt_for_secrets": "'rover123'"}},
        ]

        self.node_subcommands = [
            {"sub_command": "create",
             "required_params": ["compartment-id", "display-name", "shape"],
             "optional_params": ["shipping-preference", "point-of-contact-phone-number", "point-of-contact", "addressee", "care-of", "address1",
                                 "city-or-locality", "state-province-region", "country", "zip-postal-code",
                                 "phone-number", "email", "freeform-tags", "defined-tags", "address2", "address3",
                                 "address4", "master-key-id", "policy-name",
                                 "policy-compartment-id"]},
            {"sub_command": "change-compartment",
             "required_params": ["compartment-id", "node-id"],
             "optional_params": ["if-match"]},
            {"sub_command": "delete",
             "required_params": ["node-id"],
             "optional_params": ["if-match", "force"]},
            {"sub_command": "show",
             "required_params": ["node-id"],
             "optional_params": []},
            {"sub_command": "update",
             "required_params": ["node-id"],
             "optional_params": ["addressee", "care-of", "address1",
                                 "city-or-locality", "lifecycle-state-details", "state-province-region", "country", "zip-postal-code",
                                 "phone-number", "email"]},
            {"sub_command": "request-approval",
             "required_params": ["node-id"],
             "optional_params": []},
            {"sub_command": "add-workload",
             "required_params": ["node-id", "type"],
             "test_necessary_params": ["bucket-name", "force"],
             "optional_params": ["prefix", "range-start", "range-end"]},
            {"sub_command": "add-workload",
             "required_params": ["node-id", "type"],
             "test_necessary_params": ["image-id", "force"],
             "optional_params": ["prefix", "range-start", "range-end"]},
            # {"sub_command": "delete-workload",
            #  "required_params": [],
            #  "test_necessary_params": ["node-id", "force"],
            #  "optional_params": []},
            {"sub_command": "set-secrets",
             "required_params": ["node-id"],
             "test_necessary_params": [],
             "optional_params": ["super-user-password", "unlock-passphrase"],
             "methods_to_side_effect": {
                 "mock_prompt_for_secrets": "'rover123'"}},
        ]

        self.shape_subcommands = [
            {"sub_command": "list",
             "required_params": ["compartment-id"],
             "optional_params": []},
        ]

        self.policy_subcommands = [
            {"sub_command": "create-master-key-policy",
             "required_params": ["master-key-id"],
             "optional_params": ["policy-name", "policy-compartment-id"]},
        ]

        self.command_defs = [
            {"command": "standalone-cluster", "sub_commands": self.cluster_subcommands},
            {"command": "station-cluster", "sub_commands": self.cluster_subcommands},
            {"command": "node", "sub_commands": self.node_subcommands},
            {"command": "shape", "sub_commands": self.shape_subcommands},
            {"command": "rover", "sub_commands": self.policy_subcommands}
        ]
        self.success_count = 0
        self.failed_count = 0
        self.skipped_count = 0
        self.failure_msg_list = []

    # For each sub-command, test that
    #       - CLI errors when any of the Required params is not supplied.
    #       - CLI accepts all Required params
    #       - CLI accepts all Optional params
    @mock.patch('services.rover.src.oci_cli_rover_cluster.rovercluster_utils.validate_bucket', return_value=mock_object_storage_obj)
    @mock.patch('services.rover.src.oci_cli_rover_node.rovernode_cli_extended.validate_bucket', return_value=mock_object_storage_obj)
    @mock.patch('services.rover.src.oci_cli_rover_cluster.rovercluster_utils.validate_get_image', return_value=mock_compute_img_obj)
    @mock.patch('services.rover.src.oci_cli_rover_node.rovernode_cli_extended.validate_get_image', return_value=mock_compute_img_obj)
    @mock.patch('services.rover.src.oci_cli_rover_cluster.rovercluster_utils.export_compute_image_helper')
    @mock.patch('services.rover.src.oci_cli_rover_node.rovernode_cli_extended.export_compute_image_helper')
    @mock.patch('services.rover.src.oci_cli_rover.rover_utils.prompt_for_secrets')
    @mock.patch('click.prompt', return_value=True)
    @mock.patch('oci_cli.cli_util.build_client')
    @mock.patch('oci_cli.cli_util.render_response')
    def test_rover(self, mock_client_render_response, mock_client, mock_prompt, mock_prompt_for_secrets, mock_node_export_compute_image,
                   mock_cluster_export_compute_image, mock_node_validate_image, mock_cluster_validate_image, mock_node_validate_bucket,
                   mock_cluster_validate_bucket):
        for command_def in self.command_defs:
            command = command_def["command"]
            specific_sub_command_set = self._sub_command_list_in_specific_test_set(command)
            if specific_sub_command_set is None:
                click.echo("Skipping command=%s; Not in test_specific_set;" % (command))
                self.skipped_count += 1
                continue
            for sub_command_def in command_def["sub_commands"]:
                if len(specific_sub_command_set) == 0 or sub_command_def["sub_command"] in specific_sub_command_set:
                    if 'methods_to_side_effect' in sub_command_def.keys():
                        # The key is the mock object name and the value is a dict of the side effects
                        for key, value in sub_command_def['methods_to_side_effect'].items():
                            # k is the method to side effect and v is the tuple of {status, headers, data}
                            if type(value) == dict:
                                for k, v in value.items():
                                    def method_side_effect(*args, **kwargs):
                                        return Response(v[0], v[1], v[2], Request("mock.method", "mock.url"))

                                    key.return_value.k.side_effect = method_side_effect
                            else:
                                print(key, value)
                    self._execute_subcommand(command, sub_command_def)
                else:
                    click.echo("Skipping command::sub-command=%s::%s; Not in test_specific_set;" % (
                        command, sub_command_def["sub_command"]))
                    self.skipped_count += 1
                    continue

        click.echo("Consolidated-ErrorList=")
        for item in self.failure_msg_list:
            click.echo(item)
        click.echo(
            "Tests: success=%d, failures=%d, skipped=%d" % (self.success_count, self.failed_count, self.skipped_count))

    def _sub_command_list_in_specific_test_set(self, command):
        if len(self.test_specific_set) == 0:
            return []
        else:
            if command in self.test_specific_set:
                return self.test_specific_set[command]
            else:
                return None

    def _execute_subcommand(self, command, sub_command_def):
        click.echo("command=%s,sub_command=%s" % (command, sub_command_def["sub_command"]))
        try:
            if sub_command_def["skip"].upper() == "TRUE":
                click.echo("Skipping...")
                self.skipped_count += 1
                return
        except Exception as e:
            pass
        # For focused testing. TODO: Promote to an env variable.
        specific_test_type = None
        # specific_test_type = self.TestType.OnlyRequiredArgs
        for test_type in self.TestType:
            if specific_test_type is not None and specific_test_type != test_type:
                continue
            c_list = self._generate_command_list(command, sub_command_def, test_type)
            c_list += ['-d']
            click.echo(c_list)
            result = util.invoke_command(c_list)
            ret = self._validate_result(command, result, sub_command_def, test_type)
            if ret == self.TestResult.Success:
                self.success_count += 1
            else:
                self.failed_count += 1

    def _generate_command_list(self, command, sub_command_def, test_type):
        # click.echo("command=%s,sub_command=%s::::%s" % (command, sub_command_def["sub_command"], test_type))
        if command == 'rover':
            c_list = [command, sub_command_def["sub_command"]]
        else:
            c_list = ["rover", command, sub_command_def["sub_command"]]
        # if (test_type == self.TestType.NoArgs):
        #     return c_list
        if 'update' in sub_command_def["sub_command"] or 'delete' in sub_command_def["sub_command"]:
            c_list.append("--force")
        c_arg_list = []
        if test_type == self.TestType.OnlyRequiredArgs:
            c_arg_list += sub_command_def["required_params"]
            if "test_necessary_params" in sub_command_def.keys():
                c_arg_list += sub_command_def["test_necessary_params"]
        elif test_type == self.TestType.AllArgs:
            c_arg_list += sub_command_def["required_params"] + sub_command_def["optional_params"]
            if "test_necessary_params" in sub_command_def.keys():
                c_arg_list += sub_command_def["test_necessary_params"]
        elif test_type == self.TestType.GenFullCommandFromJson:
            c_list += ["--generate-full-command-json-input"]
        else:
            click.echo("_generate_command_list:Uncoded TestType=%s" % (test_type))
            return None
        c_list += self._add_args(c_arg_list, test_type)
        return c_list

    def _add_args(self, arg_list, test_type):
        new_arg_list = []
        for item in arg_list:
            s = ""
            new_arg_list.append("--" + item)
            if item in self.specific_arg_values:
                if item == "cluster-type":
                    if int(self.specific_arg_values['cluster-size']) >= 15:
                        s = "STATION"
                    else:
                        s = "STANDALONE"
                elif item == "type":
                    if "image-id" in arg_list:
                        s = "IMAGE"
                    else:
                        s = "BUCKET"
                else:
                    s = self.specific_arg_values[item]
            elif item in self.complex_data_defs:
                j = {}
                complex_data_args = self.complex_data_defs[item]
                if test_type == self.TestType.OnlyRequiredArgs or test_type == self.TestType.AllArgs:
                    for arg in complex_data_args["required_params"]:
                        if arg in self.specific_arg_values:
                            j[arg] = json.loads(self.specific_arg_values[arg])
                        else:
                            j[arg] = "456"
                if test_type == self.TestType.AllArgs:
                    for arg in complex_data_args["optional_params"]:
                        if arg in self.specific_arg_values:
                            j[arg] = json.loads(self.specific_arg_values[arg])
                        else:
                            j[arg] = "789"
                s = json.dumps(j)
            else:
                s = "123"
            if s is not None:
                new_arg_list.append(s)
        return new_arg_list

    def _print_error(self, command, sub_command, s):
        err = "command=%s,sub_command=%s,Error=%s\n" % (command, sub_command, s)
        click.echo(err)
        self.failure_msg_list.append(err)

    def _validate_result(self, command, result, sub_command_def, test_type):
        required_params = sub_command_def["required_params"]
        if test_type == self.TestType.AllArgs or test_type == self.TestType.OnlyRequiredArgs:
            if result.exception is None:
                return UnitTestRover.TestResult.Success
            else:
                # Uncomment following line to view traceback
                # print(result)
                self._print_error(
                    command, sub_command_def["sub_command"], "Incorrect result:**#%s#**" % result.stdout_bytes)
                return UnitTestRover.TestResult.Failed
        elif test_type == self.TestType.GenFullCommandFromJson:
            if "Error:" in result.output:
                self._print_error(command, sub_command_def["sub_command"], "Incorrect result:**#%s#**" % result.output)
                return UnitTestRover.TestResult.Failed
            else:
                return UnitTestRover.TestResult.Success
