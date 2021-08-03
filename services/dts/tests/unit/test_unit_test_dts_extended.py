# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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

import datetime
import enum
import json
import click
import oci
import pytest
import unittest

from oci.dts.models import UpdateApplianceExportJobDetails, TransferJob, TransferAppliance

from services.dts.src.oci_cli_dts.appliance_constants import APPLIANCE_STATE_NOT_LOCKED, APPLIANCE_STATE_LOCKED, \
    APPLIANCE_STATUS_NA
from services.dts.src.oci_cli_transfer_job.transferjob_cli_extended import show_transfer_job_with_details, \
    validate_bucket_belongs_to_compartment
from tests import test_config_container
from tests import util

import unittest.mock as mock
from oci.object_storage.models import Bucket
from oci.response import Response
from oci.request import Request
from services.dts.src.oci_cli_dts.physical_appliance_control_plane.client.models.nfs_dataset_info import NfsDatasetInfo
from oci.dts.models.transfer_appliance_entitlement_summary import TransferApplianceEntitlementSummary
from oci.object_storage.models.list_objects import ListObjects
from oci.object_storage.models.object_summary import ObjectSummary
from services.dts.src.oci_cli_appliance_export_job.applianceexportjob_constants import \
    OBJECT_STORAGE_BUCKET_TYPE_ARCHIVE, LIFECYCLE_STATE_DETAILS_CUSTOMER_RECEIVED, \
    LIFECYCLE_STATE_DETAILS_CUSTOMER_PROCESSING, LIFECYCLE_STATE_DETAILS_ORACLE_SHIPPED, \
    LIFECYCLE_STATE_DETAILS_PENDING_APPROVAL
from services.dts.src.oci_cli_appliance_export_job.applianceexportjob_cli_extended import appliance_state_update, \
    appliance_encryption_check, appliance_unlock, deactivate_nfs_dataset

CASSETTE_LIBRARY_DIR = 'services/dts/tests/cassettes'


@pytest.fixture(autouse=True, scope='module')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('dts_unit_tests.yml'):
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


class UnitTestDTS(unittest.TestCase):
    class TestResult(enum.Enum):
        Success = 1
        Skipped = 2
        Failed = 3

    class TestType(enum.Enum):
        NoArgs = "NoArgs"
        OnlyRequiredArgs = "OnlyRequiredArgs"
        AllArgs = "AllArgs"
        GenFullCommandFromJson = "GenFullCommandFromJson"

    Missing_params_Text = "Error: Missing option(s)"

    def setUp(self):
        self.test_specific_set = {}  # When empty, all tests are run.
        # self.test_specific_set = {"appliance":["request"]}

        self.specific_arg_values = {"profile": "DEFAULT", "device-type": "APPLIANCE", "if-match": "True", "all": None,
                                    "wait": None, "rw": "True", "world": "True", "lifecycle-state": "CREATING",
                                    "test_defined_tag": '{"string1": "string", "string2": "string"}', "force": None,
                                    "debug": None, "setup-notifications": "True", "skip-upload-user-check": None}
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

        self.job_subcommands = [
            {"sub_command": "create",
             "required_params": ["compartment-id", "bucket", "display-name", "device-type"],
             "optional_params": ["defined-tags", "freeform-tags", "profile", "skip-upload-user-check"]},
            {"sub_command": "show",
             "required_params": ["job-id"],
             "optional_params": []},
            {"sub_command": "update",
             "required_params": ["job-id"],
             "optional_params": ["defined-tags", "freeform-tags", "display-name"]},
            {"sub_command": "delete",
             "required_params": ["job-id"],
             "optional_params": []},
            {"sub_command": "close",
             "required_params": ["job-id"],
             "optional_params": []},
            {"sub_command": "verify-upload-user-credentials",
             "required_params": ["bucket"],
             "optional_params": []},
            {"sub_command": "change-compartment",
             "required_params": ["job-id", "compartment-id"],
             "optional_params": []},
            {"sub_command": "setup-notifications",
             "required_params": ["job-id"],
             "optional_params": []}
        ]
        self.appliance_subcommands = [
            {"sub_command": "request",
             "required_params": ["job-id", "addressee", "care-of", "address1", "city-or-locality",
                                 "state-province-region", "country", "zip-postal-code", "phone-number", "email"],
             "optional_params": ["address2", "address3", "address4"]},
            {"sub_command": "show",
             "required_params": ["job-id", "appliance-label"],
             "optional_params": []},
            {"sub_command": "list",
             "required_params": ["job-id"],
             "optional_params": []},
            {"sub_command": "get-passphrase",
             "required_params": ["job-id", "appliance-label"],
             "optional_params": []},
            {"sub_command": "never-receive",
             "required_params": ["job-id", "appliance-label"],
             "optional_params": []},
            {"sub_command": "cancel",
             "required_params": ["job-id", "appliance-label"],
             "optional_params": []},
            {"sub_command": "delete",
             "required_params": ["job-id", "appliance-label"],
             "optional_params": []},
            {"sub_command": "update-shipping-address",
             "required_params": ["job-id", "appliance-label", "addressee"],
             "optional_params": ["address2", "address3", "address4", "care-of", "address1", "city-or-locality",
                                 "state-province-region", "country", "zip-postal-code", "phone-number", "email"]},
            {"sub_command": "setup-notifications",
             "required_params": ["appliance-label"],
             "optional_params": []}
        ]
        self.pa_subcommands = [
            {"sub_command": "list",
             "required_params": [],
             "optional_params": []},
            {"sub_command": "configure-encryption",
             "required_params": ["job-id", "appliance-label"],
             "optional_params": ["appliance-profile"]},
            {"sub_command": "show",
             "required_params": [],
             "optional_params": ["appliance-profile"]},
            {"sub_command": "unlock",
             "required_params": ["job-id", "appliance-label"],
             "optional_params": ["appliance-profile"]},
            # {"sub_command": "finalize",
            #  "required_params": ["job-id", "appliance-label"],
            #  "optional_params": ["appliance-profile", "profile"],
            #  "methods_to_side_effect": {}},
        ]
        nfs_datasets = [{'name': '123', 'state': NfsDatasetInfo.STATE_ACTIVE,
                         'dataset_type': NfsDatasetInfo.DATASET_TYPE_NFS, 'nfs_export_details': None}]
        self.nfs_ds_subcommands = [
            {"sub_command": "create",
             "required_params": ["name"],
             "optional_params": ["rw", "world", "ip", "subnet-mask-length", "appliance-profile"]},
            {"sub_command": "set-export",
             "required_params": ["name", "rw", "world"],
             "optional_params": ["ip", "subnet-mask-length", "appliance-profile"]},
            {"sub_command": "show",
             "required_params": ["name"],
             "optional_params": ["appliance-profile"]},
            {"sub_command": "list",
             "required_params": [],
             "optional_params": ["appliance-profile"]},
            {"sub_command": "delete",
             "required_params": ["name"],
             "optional_params": ["appliance-profile"]},
            # {"sub_command": "activate",
            #  "required_params": ["name"],
            #  "optional_params": ["rw", "world", "ip", "subnet-mask-length", "appliance-profile"],
            #  "methods_to_side_effect": {"mock_nfs_dataset_client": {"list_nfs_datasets": (200, {}, nfs_datasets)}}},
            {"sub_command": "deactivate",
             "required_params": ["name"],
             "optional_params": ["appliance-profile"]},
            # {"sub_command": "seal",
            #  "required_params": [],
            #  "optional_params": ["name", "appliance-profile"],
            #  "methods_to_side_effect": {"mock_nfs_dataset_client": {"list_nfs_datasets": (200, {}, nfs_datasets)}}},
            {"sub_command": "reopen",
             "required_params": ["name"],
             "optional_params": ["appliance-profile"]},
            {"sub_command": "seal-status",
             "required_params": ["name"],
             "optional_params": ["appliance-profile"]},
            {"sub_command": "get-seal-manifest",
             "required_params": ["name", "output-file"],
             "optional_params": ["appliance-profile"]},
        ]
        list_objects = ListObjects()
        list_objects.objects = [
            ObjectSummary(name="first_object", size=20, md5="def456", time_created=datetime.datetime.now(),
                          etag="tag1")]
        headers = {'etag': 'etag', 'opc-multipart-md5': 'md5', 'opc-content-md5': 'md5'}

        self.export_job_subcommands = [
            {"sub_command": "create",
             "required_params": ["compartment-id", "bucket-name", "display-name", "addressee", "care-of", "address1",
                                 "city-or-locality", "state-province-region", "country", "zip-postal-code",
                                 "phone-number", "email"],
             "optional_params": ["freeform-tags", "defined-tags", "address2", "address3", "address4",
                                 "setup-notifications"],
             "methods_to_side_effect": {
                 "mock_prompt_for_emails": "'abc.xyz@123.com'"}},
            {"sub_command": "change-compartment",
             "required_params": ["compartment-id", "job-id"],
             "optional_params": ["if-match"]},
            {"sub_command": "delete",
             "required_params": ["job-id"],
             "optional_params": ["if-match", "force"]},
            {"sub_command": "show",
             "required_params": ["job-id"],
             "optional_params": []},
            {"sub_command": "get-passphrase",
             "required_params": ["job-id"],
             "optional_params": []},
            {"sub_command": "list",
             "required_params": ["compartment-id"],
             "optional_params": ["lifecycle-state", "display-name", "page", "page-size"]},
            {"sub_command": "update",
             "required_params": ["job-id"],
             "optional_params": ["display-name", "manifest-file",
                                 "freeform-tags", "defined-tags", "if-match", "force", "care-of", "address1",
                                 "address2", "address3", "address4", "city-or-locality", "state-province-region",
                                 "country", "zip-postal-code", "phone-number", "email", "addressee"]},
            # {"sub_command": "generate-manifest",
            #  "required_params": ["job-id", "compartment-id", "bucket"],
            #  "optional_params": ["prefix", "start", "end"],
            #  "methods_to_side_effect": {
            #      "mock_os_client": {
            #          "list_objects": (200, headers, list_objects),
            #          "put_object": (200, headers, list_objects),
            #          "upload_part": (200, headers, list_objects),
            #          "commit_multipart_upload": (200, headers, list_objects)}}},
            {"sub_command": "request-appliance",
             "required_params": ["job-id"],
             "optional_params": []},
            {"sub_command": "create-policy",
             "required_params": ["job-id"],
             "optional_params": []},
        ]

        entitlement = TransferApplianceEntitlementSummary()
        entitlement.id = '123'
        entitlements = [entitlement]
        self.entitlement_subcommands = [
            {"sub_command": "request-entitlement",
             "required_params": ["compartment-id", "name", "email"],
             "optional_params": []},
            {"sub_command": "show-entitlement",
             "required_params": ["compartment-id"],
             "optional_params": [],
             "methods_to_side_effect": {
                 "mock_client": {"list_transfer_appliance_entitlement": (200, {}, entitlements)}}},
        ]
        self.command_defs = [
            {"command": "job", "sub_commands": self.job_subcommands},
            {"command": "appliance", "sub_commands": self.appliance_subcommands},
            {"command": "physical-appliance", "sub_commands": self.pa_subcommands},
            {"command": "nfs-dataset", "sub_commands": self.nfs_ds_subcommands},
            {"command": "appliance", "sub_commands": self.entitlement_subcommands},
            {"command": "export", "sub_commands": self.export_job_subcommands},
        ]

        self.success_count = 0
        self.failed_count = 0
        self.skipped_count = 0
        self.failure_msg_list = []

    # For each sub-command, test that
    #       - CLI errors when any of the Required params is not supplied.
    #       - CLI accepts all Required params
    #       - CLI accepts all Optional params

    @mock.patch('services.dts.src.oci_cli_dts.physicalappliance_cli_extended.validate_upload_user_credentials', return_value=None)
    @mock.patch('services.dts.src.oci_cli_transfer_job.transferjob_cli_extended.validate_bucket_belongs_to_compartment', return_value=None)
    @mock.patch('services.dts.src.oci_cli_transfer_job.transferjob_cli_extended.validate_upload_user_credentials', return_value=None)
    @mock.patch('services.dts.src.oci_cli_transfer_job.transferjob_cli_extended.create_transfer_job_client')
    @mock.patch('services.dts.src.oci_cli_dts.cli_utils.create_rule_helper')
    @mock.patch('services.dts.src.oci_cli_dts.cli_utils.create_subscription_helper')
    @mock.patch('services.dts.src.oci_cli_dts.cli_utils.prompt_for_emails')
    @mock.patch('services.dts.src.oci_cli_dts.cli_utils.get_topic_id')
    @mock.patch('services.dts.src.oci_cli_dts.cli_utils.get_topic_client')
    @mock.patch('services.dts.src.oci_cli_appliance_export_job.applianceexportjob_cli_extended.get_bucket_access_policies')
    @mock.patch('services.dts.src.oci_cli_appliance_export_job.applianceexportjob_cli_extended.create_os_client')
    @mock.patch('services.dts.src.oci_cli_appliance_export_job.applianceexportjob_cli_extended.reset_passphrase')
    @mock.patch('services.dts.src.oci_cli_dts.nfsdataset_cli_extended.write_to_file')
    @mock.patch('services.dts.src.oci_cli_dts.nfsdataset_cli_extended.create_nfs_dataset_client')
    @mock.patch('services.dts.src.oci_cli_dts.physicalappliance_cli_extended.create_appliance_client')
    @mock.patch('services.dts.src.oci_cli_dts.physicalappliance_cli_extended.create_init_auth')
    @mock.patch('click.prompt', return_value=True)
    @mock.patch('oci_cli.cli_util.build_client')
    def test_dts(self, mock_client, mock_prompt, mock_init_auth, mock_appliance_client,
                 mock_nfs_dataset_client, mock_write_to_file, mock_reset_passphrase, mock_os_client,
                 mock_get_bucket_access_policies, mock_topic_client, mock_get_topic_id, mock_prompt_for_emails,
                 mock_create_subscription_helper, mock_create_rule_helper, mock_transfer_job_client, mock_transferjobj_validate_upload_user,
                 mock_validate_bucket_compartment, mock_pa_validate_upload_user):

        click.echo("")
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
                                    # TODO: Find a better way to do this since exec is not allowed in python 2
                                    # exec("{}.return_value.{}.side_effect = method_side_effect".format(
                                    #     key, k)) in globals(), locals()
                            else:
                                print(key, value)
                                # exec("{}.return_value = {}".format(key, value))
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
            if len(c_list) == 3 and sub_command_def["sub_command"] == "unlock":
                continue
            click.echo(c_list)
            result = util.invoke_command(c_list)
            ret = self._validate_result(command, result, sub_command_def, test_type)
            if ret == self.TestResult.Success:
                self.success_count += 1
            else:
                self.failed_count += 1

    def _generate_command_list(self, command, sub_command_def, test_type):
        # click.echo("command=%s,sub_command=%s::::%s" % (command, sub_command_def["sub_command"], test_type))
        c_list = ["dts", command, sub_command_def["sub_command"]]
        if (test_type == self.TestType.NoArgs):
            return c_list

        if 'update' in sub_command_def["sub_command"] or 'delete' in sub_command_def["sub_command"] \
                and command not in ['physical-appliance', 'nfs-dataset']:
            c_list.append("--force")
        c_arg_list = []
        if test_type == self.TestType.OnlyRequiredArgs:
            c_arg_list += sub_command_def["required_params"]
        elif test_type == self.TestType.AllArgs:
            c_arg_list += sub_command_def["required_params"] + sub_command_def["optional_params"]
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
        if test_type == self.TestType.NoArgs:
            cmd_result = UnitTestDTS.TestResult.Success
            if len(required_params) and self.Missing_params_Text not in result.output:
                self._print_error(command, sub_command_def["sub_command"],
                                  "Spec issue: %s need to be marked as Required." % (required_params))
                return UnitTestDTS.TestResult.Failed

            msg = ""
            for r_p in required_params:
                s = "--" + r_p

                try:
                    if s not in result.output:
                        msg += r_p + ","
                except Exception as e:
                    self._print_error(command, sub_command_def["sub_command"],
                                      "result does not carry field output: %s" % (result))
            if len(msg) > 0:
                msg = "Spec issue: %s need to be marked as Required." % (msg)
                self._print_error(command, sub_command_def["sub_command"], msg)
                cmd_result = UnitTestDTS.TestResult.Failed
            return cmd_result
        elif test_type == self.TestType.AllArgs or test_type == self.TestType.OnlyRequiredArgs:
            if result.exception is None:
                return UnitTestDTS.TestResult.Success
            else:
                self._print_error(
                    command, sub_command_def["sub_command"], "Incorrect result:**#%s#**" % result.stdout_bytes)
                return UnitTestDTS.TestResult.Failed
        elif test_type == self.TestType.GenFullCommandFromJson:
            if "Error:" in result.output:
                self._print_error(command, sub_command_def["sub_command"], "Incorrect result:**#%s#**" % result.output)
                return UnitTestDTS.TestResult.Failed
            else:
                return UnitTestDTS.TestResult.Success

    @mock.patch('services.dts.src.oci_cli_appliance_export_job.applianceexportjob_cli_extended.create_os_client')
    def test_archive_bucket_export_job_create_prevention(self, mock_os_client):

        def mock_get_namespace():
            return Response(200, {}, "test-namespace", Request("mock.method", "mock.url"))

        def mock_get_bucket(namespace_name, bucket_name):
            return Response(200, {}, Bucket(namespace="test-namespace", compartment_id="compartment_id",
                                            name="test-bucket-name", storage_tier=OBJECT_STORAGE_BUCKET_TYPE_ARCHIVE),
                            Request("mock.method", "mock.url")
                            )

        mock_os_client.return_value.get_namespace.side_effect = mock_get_namespace
        mock_os_client.return_value.get_bucket.side_effect = mock_get_bucket

        args_list = ['dts', 'export', 'create', '--compartment-id', '123', '--bucket-name', '123', '--display-name',
                     '123', '--addressee', '123', '--care-of', '123', '--address1', '123', '--city-or-locality',
                     '123', '--state-province-region', '123', '--country', '123', '--zip-postal-code', '123',
                     '--phone-number', '123', '--email', '123', '--address2', '123', '--address3', '123', '--address4',
                     '123', '--setup-notifications', 'True']
        result = util.invoke_command(args_list)
        assert (isinstance(result.exception, SystemExit))
        assert "Export for Archive buckets is currently not supported" in result.exception.__str__()

    @mock.patch('services.dts.src.oci_cli_appliance_export_job.applianceexportjob_cli_extended.create_os_client')
    def test_archive_bucket_export_prevention(self, mock_os_client):

        def mock_get_namespace():
            return Response(200, {}, "test-namespace", Request("mock.method", "mock.url"))

        def mock_get_bucket(namespace_name, bucket_name):
            return Response(200, {}, Bucket(namespace="test-namespace", compartment_id="compartment_id",
                                            name="test-bucket-name", storage_tier=OBJECT_STORAGE_BUCKET_TYPE_ARCHIVE),
                            Request("mock.method", "mock.url")
                            )

        mock_os_client.return_value.get_namespace.side_effect = mock_get_namespace
        mock_os_client.return_value.get_bucket.side_effect = mock_get_bucket

        args_list = ['dts', 'export', 'generate-manifest', '--compartment-id', "123", '--job-id',
                     "123", '--bucket', 'test-bucket-name']
        result = util.invoke_command(args_list)
        assert (isinstance(result.exception, SystemExit))
        assert "Export for Archive buckets is currently not supported" in result.exception.__str__()

    def test_appliance_state_update(self):

        target_appliance_state = appliance_state_update(UpdateApplianceExportJobDetails.LIFECYCLE_STATE_ACTIVE, LIFECYCLE_STATE_DETAILS_ORACLE_SHIPPED, **{'job_id': '123'})
        assert target_appliance_state is None

        target_appliance_state = appliance_state_update(UpdateApplianceExportJobDetails.LIFECYCLE_STATE_INPROGRESS, LIFECYCLE_STATE_DETAILS_CUSTOMER_PROCESSING, **{'job_id': '123'})
        assert target_appliance_state is None

        target_appliance_state = appliance_state_update(UpdateApplianceExportJobDetails.LIFECYCLE_STATE_INPROGRESS, LIFECYCLE_STATE_DETAILS_ORACLE_SHIPPED, **{'job_id': '123'})
        assert target_appliance_state['lifecycle_state_details'] is LIFECYCLE_STATE_DETAILS_CUSTOMER_PROCESSING

        target_appliance_state = appliance_state_update(UpdateApplianceExportJobDetails.LIFECYCLE_STATE_INPROGRESS, LIFECYCLE_STATE_DETAILS_CUSTOMER_RECEIVED, **{'job_id': '123'})
        assert target_appliance_state['lifecycle_state_details'] is LIFECYCLE_STATE_DETAILS_CUSTOMER_PROCESSING

        with pytest.raises(click.ClickException):
            target_appliance_state = appliance_state_update(UpdateApplianceExportJobDetails.LIFECYCLE_STATE_INPROGRESS, LIFECYCLE_STATE_DETAILS_PENDING_APPROVAL, **{'job_id': '123'})
            assert target_appliance_state is None

    def test_appliance_encryption_check(self):

        result = appliance_encryption_check(encryptionConfigured='True')
        assert result is None

        with pytest.raises(oci.exceptions.ClientError):
            appliance_encryption_check(encryptionConfigured='False')

    @mock.patch('services.dts.src.oci_cli_appliance_export_job.applianceexportjob_cli_extended.pa_unlock_helper')
    def test_appliance_unlock(self, mocker_pa):
        appliance_profile = 'test'
        passphrase = '123'
        ctx_obj = '123'

        def mock_pa_unlock_helper(ctx_obj, appliance_profile, passphrase):
            # do nothing
            pass

        mocker_pa.side_effect = mock_pa_unlock_helper

        # Test case #1, Appliance state = NOT_LOCKED, do nothing
        appliance_unlock(ctx=ctx_obj, appliance_profile=appliance_profile, passphrase=passphrase,
                         appliance_lock_status=APPLIANCE_STATE_NOT_LOCKED)
        mocker_pa.assert_not_called()

        # Test case #2, Appliance state = LOCKED, invoke unlock()
        appliance_unlock(ctx=ctx_obj, appliance_profile=appliance_profile, passphrase=passphrase,
                         appliance_lock_status=APPLIANCE_STATE_LOCKED)
        mocker_pa.assert_called_with(ctx_obj, appliance_profile, passphrase)

        # Test case #3, Appliance state = NA, invoke unlock()
        appliance_unlock(ctx=ctx_obj, appliance_profile=appliance_profile, passphrase=passphrase,
                         appliance_lock_status=APPLIANCE_STATUS_NA)
        mocker_pa.assert_called_with(ctx_obj, appliance_profile, passphrase)

    @mock.patch('services.dts.src.oci_cli_dts.physicalappliance_cli_extended.create_appliance_client')
    @mock.patch('services.dts.src.oci_cli_dts.physicalappliance_cli_extended.create_init_auth')
    @mock.patch('click.prompt', return_value=True)
    @mock.patch('oci_cli.cli_util.build_client')
    def test_appliance_init_auth_export_job(self, mock_build_client, mock_prompt, mock_create_init_auth, mock_create_appliance_client):

        args_list = ['dts', 'physical-appliance', 'initialize-authentication', '--export-job-id', 'exportJobId',
                     '--appliance-ip', '1.2.3.4', '--appliance-port', '443', '--appliance-cert-fingerprint', '12:34:56',
                     '--access-token', 'accessToken', '--profile', 'profile', '--appliance-profile', 'applianceProfile']

        result = util.invoke_command(args_list)

        assert result.exception is None
        assert result.exit_code == 0

    @mock.patch('services.dts.src.oci_cli_dts.physicalappliance_cli_extended.create_appliance_client')
    @mock.patch('services.dts.src.oci_cli_dts.physicalappliance_cli_extended.create_init_auth')
    @mock.patch('click.prompt', return_value=True)
    @mock.patch('oci_cli.cli_util.build_client')
    def test_appliance_init_auth_import_job(self, mock_build_client, mock_prompt, mock_create_init_auth, mock_create_appliance_client):

        args_list = ['dts', 'physical-appliance', 'initialize-authentication', '--job-id', 'jobId',
                     '--appliance-label', 'applianceLabel', '--appliance-ip', '1.2.3.4', '--appliance-port', '443',
                     '--appliance-cert-fingerprint', '12:34:56', '--access-token', 'accessToken',
                     '--profile', 'profile', '--appliance-profile', 'applianceProfile']

        result = util.invoke_command(args_list)

        assert result.exception is None
        assert result.exit_code == 0

    @mock.patch('services.dts.src.oci_cli_dts.physicalappliance_cli_extended.create_appliance_client')
    @mock.patch('services.dts.src.oci_cli_dts.physicalappliance_cli_extended.create_init_auth')
    @mock.patch('click.prompt', return_value=True)
    @mock.patch('oci_cli.cli_util.build_client')
    def test_appliance_init_auth_wrong_job_info(self, mock_build_client, mock_prompt, mock_create_init_auth, mock_create_appliance_client):

        # Passing no job ID, appliance label or export job ID
        args_list = ['dts', 'physical-appliance', 'initialize-authentication',
                     '--appliance-ip', '1.2.3.4', '--appliance-port', '443', '--appliance-cert-fingerprint', '12:34:56',
                     '--access-token', 'accessToken', '--profile', 'profile', '--appliance-profile', 'applianceProfile']

        result = util.invoke_command(args_list)

        assert (isinstance(result.exception, SystemExit))
        assert "Either use --export-job-id or a combination of --job-id and --appliance-label" in result.exception.__str__()

        # Passing job ID without appliance label
        args_list = ['dts', 'physical-appliance', 'initialize-authentication', '--job-id', 'jobId',
                     '--appliance-ip', '1.2.3.4', '--appliance-port', '443', '--appliance-cert-fingerprint', '12:34:56',
                     '--access-token', 'accessToken', '--profile', 'profile', '--appliance-profile', 'applianceProfile']

        result = util.invoke_command(args_list)

        assert (isinstance(result.exception, SystemExit))
        assert "Either use --export-job-id or a combination of --job-id and --appliance-label" in result.exception.__str__()

    @mock.patch('services.dts.src.oci_cli_dts.nfsdataset_cli_extended.nfs_dataset_deactivate_helper')
    def test_deactivate_nfs_dataset(self, mocker_nfs_dataset_deactivate):
        appliance_profile = 'test'
        ctx_obj = '123'

        def mock_nfs_dataset_deactivate_helper(ctx_obj, **kwargs):
            # do nothing
            pass

        mocker_nfs_dataset_deactivate.side_effect = mock_nfs_dataset_deactivate_helper

        deactivate_nfs_dataset(ctx_obj, appliance_profile, **{'name': 'test-dataset', 'state':
                               NfsDatasetInfo.STATE_INACTIVE, 'dataset_type': 'NFS', 'nfs_export_details':
                               'NfsExportDetails'})
        mocker_nfs_dataset_deactivate.assert_not_called()

        deactivate_nfs_dataset(ctx_obj, appliance_profile, **{'name': 'test-dataset', 'state':
                               NfsDatasetInfo.STATE_ACTIVE, 'dataset_type': 'NFS', 'nfs_export_details':
                               'NfsExportDetails'})
        mocker_nfs_dataset_deactivate.assert_called_with(ctx_obj, **{'name': 'test-dataset',
                                                         'appliance_profile': appliance_profile})

    @mock.patch('services.dts.src.oci_cli_transfer_job.transferjob_cli_extended.get_transfer_appliance_helper')
    @mock.patch('services.dts.src.oci_cli_transfer_job.transferjob_cli_extended.get_transfer_job_helper')
    def test_show_transfer_job(self, mock_get_transfer_job, mock_get_transfer_appliance):

        def mock_get_transfer_job_helper(ctx, from_json, id):
            return Response(200, {}, TransferJob(id='test-job-id', compartment_id='test-compartment-id', label='test-transfer-job',
                                                 device_type='APPLIANCE', lifecycle_state='PREPARING', attached_transfer_appliance_labels=['XA-test-1', 'XA_test-2'],
                                                 upload_bucket_name='test-bucket'),
                            Request("mock.method", "mock.url")
                            )

        def mock_get_transfer_appliance_helper(ctx, from_json, id, appliance_lbl):
            if appliance_lbl == 'XA-test-1':
                return Response(200, {}, TransferAppliance(transfer_job_id='test-job-id', label='XA-test-1', serial_number='test-serial-no-1',
                                                           lifecycle_state='PREPARING', upload_status_log_uri='fakepath/upload_summary1.txt'), Request("mock.method", "mock.url"))
            else:
                return Response(200, {}, TransferAppliance(transfer_job_id='test-job-id', label='XA-test-2', serial_number='test-serial-no-2',
                                                           lifecycle_state='PREPARING', upload_status_log_uri='fakepath/upload_summary2.txt'), Request("mock.method", "mock.url"))

        mock_context = get_mock_context()

        mock_get_transfer_job.side_effect = mock_get_transfer_job_helper
        mock_get_transfer_appliance.side_effect = mock_get_transfer_appliance_helper

        result = show_transfer_job_with_details(mock_context, **{"id": 'test-job-id', 'from_json': None})

        appliance_details_1 = {'label': 'XA-test-1', 'serialNumber': 'test-serial-no-1', 'status': 'PREPARING', 'uploadStatusLogURL': 'fakepath/upload_summary1.txt'}
        appliance_details_2 = {'label': 'XA_test-2', 'serialNumber': 'test-serial-no-2', 'status': 'PREPARING', 'uploadStatusLogURL': 'fakepath/upload_summary2.txt'}
        assert result.data.id == 'test-job-id'
        assert len(result.data.attached_transfer_appliance_labels) == 2
        assert appliance_details_1 in result.data.attached_transfer_appliance_labels
        assert appliance_details_2 in result.data.attached_transfer_appliance_labels

    @mock.patch('services.dts.src.oci_cli_transfer_job.transferjob_cli_extended.create_os_client')
    def test_validate_bucket_belongs_to_compartment(self, mock_os_client):

        def mock_get_namespace():
            return Response(200, {}, "test-namespace", Request("mock.method", "mock.url"))

        def mock_get_bucket(namespace_name, bucket_name):
            return Response(200, {}, Bucket(namespace="test-namespace", compartment_id="test-compartment-id",
                                            name="test-bucket-name", storage_tier=OBJECT_STORAGE_BUCKET_TYPE_ARCHIVE),
                            Request("mock.method", "mock.url")
                            )

        mock_context = get_mock_context()
        mock_os_client.return_value.get_namespace.side_effect = mock_get_namespace
        mock_os_client.return_value.get_bucket.side_effect = mock_get_bucket

        with pytest.raises(oci.exceptions.ClientError):
            validate_bucket_belongs_to_compartment(ctx=mock_context, bucket="test-bucket", compartment_id="compartment-id")
        assert validate_bucket_belongs_to_compartment(ctx=mock_context, bucket="test-bucket", compartment_id="test-compartment-id") is None
