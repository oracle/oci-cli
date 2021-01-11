# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import pytest
import tempfile
import unittest
from tests import tag_data_container
from tests import test_config_container
from tests import util
import os.path

CASSETTE_LIBRARY_DIR = 'services/identity/tests/cassettes'


@pytest.mark.usefixtures("tag_namespace_and_tags")
class TestIdentity(unittest.TestCase):

    RENAME_COMPARTMENT_PREFIX = "PythonCliCompartmentRenameTest-"

    VALID_ACTIVE_CUSTOMER_SECRET_KEY_STATES = ['ACTIVE', 'CREATING']
    VALID_DELETED_CUSTOMER_SECRET_KEY_STATES = ['DELETED', 'DELETING']

    def setUp(self):
        util.set_admin_pass_phrase()

    # The operations not called are:
    #   - region list, region-subscription create/list
    #   - tag and tag-namespace operations (x12). These are handled via test_tagging and test_tag_management
    #   - dynamic group operations (create, get, update, delete, list)
    #   - smtp credential operations (create, update, delete, list) covered in test_email.py
    @test_config_container.RecordReplay('identity', cassette_library_dir=CASSETTE_LIBRARY_DIR)
    def test_all_operations(self):
        """Successfully calls every operation with basic options.  Exceptions are region list, region-subscription list region-subscription create"""
        try:
            self.subtest_availability_domain_operations()
            self.subtest_create_compartment()
            self.subtest_compartment_operations()
            self.subtest_compartment_rename()
            self.subtest_user_operations()
            self.subtest_group_operations()
            self.subtest_user_group_membership_operations()
            self.subtest_api_key_operations()
            self.subtest_ui_password_operations()
            self.subtest_swift_password_operations()
            self.subtest_policy_operations()
            self.subtest_customer_secret_key_operations()
            self.subtest_region_subscription_operations()
        finally:
            self.subtest_cleanup()

    def subtest_create_compartment(self):
        result = self.invoke(['compartment', 'create', '--name', 'PythonCLITest124', '--description', 'Create Compartment for CLI testing using wait for state ACTIVE', '--compartment-id', util.COMPARTMENT_ID, '--wait-for-state', 'ACTIVE'])
        self.validate_response(result, json_response_expected=False)
        assert 'NotAuthorizedOrNotFound' not in result.output
        created_compartment = util.get_json_from_mixed_string(result.output)
        assert created_compartment['data']['compartment-id'] == util.COMPARTMENT_ID
        assert created_compartment['data']['lifecycle-state'] == 'ACTIVE'
        result = self.invoke(['compartment', 'delete', '--compartment-id', created_compartment['data']['id'], '--force'])
        assert result.exit_code == 0

    def subtest_availability_domain_operations(self):
        result = self.invoke(['availability-domain', 'list', '--compartment-id', util.TENANT_ID])
        self.validate_response(result)

        result = self.invoke(['availability-domain', 'list'])
        self.validate_response(result)

    def subtest_compartment_operations(self):
        # We don't want to call compartment create with every run, so just call help to
        # make sure the command is at least there.
        result = self.invoke(['compartment', 'create', '--help', '--cli-rc-file', os.path.join('tests', 'resources', 'default_files', 'use_click_help')])
        self.validate_response(result, json_response_expected=False)

        result = self.invoke(['compartment', 'list', '--compartment-id', util.TENANT_ID, '--limit', '1000'])
        self.validate_response(result)

        result = self.invoke(['compartment', 'list', '--limit', '1000'])
        self.validate_response(result)

        result = self.invoke(['compartment', 'list', '--include-root'])
        self.validate_response(result)

        result = self.invoke(['compartment', 'list', '--include-root', '--limit', '10'])
        self.validate_response(result)
        self.assertEquals(len(json.loads(result.output)['data']), 10)

        result = self.invoke(['compartment', 'list', '--include-root', '--limit', '1'])
        self.validate_response(result)
        tenant_id = "ocid1.tenancy.oc1..aaaaaaaa3vi3ft3yi3sq4nhiql4nvbzjz6gipbn72h7werl6njs6xsq4wgdq"
        self.assertEquals(tenant_id, json.loads(result.output)['data'][0]['id'])
        self.assertEquals(len(json.loads(result.output)['data']), 1)

        result = self.invoke(['compartment', 'list', '--all', '--include-root'])
        self.validate_response(result)

        result = self.invoke(['compartment', 'list', '--compartment-id', util.TENANT_ID, '--include-root'])
        self.validate_response(result)

        result = self.invoke(['compartment', 'get', '--compartment-id', util.COMPARTMENT_ID])
        self.validate_response(result, expect_etag=True)

        update_description = 'Compartment used by CLI integration tests. {}'.format(util.random_number_string())
        result = self.invoke(
            ['compartment', 'update', '--compartment-id', util.COMPARTMENT_ID, '--description', update_description])
        self.validate_response(result, expect_etag=True)
        self.assertEquals(update_description, json.loads(result.output)['data']['description'])

    def subtest_compartment_rename(self):
        compartment_to_rename = self.get_compartment_to_rename()

        updated_name = '{}{}'.format(self.RENAME_COMPARTMENT_PREFIX, util.random_number_string())
        updated_description = 'Updated {}'.format(updated_name)
        result = self.invoke(['compartment', 'update', '--compartment-id', compartment_to_rename['id'], '--name', updated_name, '--description', updated_description])
        self.validate_response(result, expect_etag=True)

        parsed_result = json.loads(result.output)
        self.assertEquals(compartment_to_rename['id'], parsed_result['data']['id'])
        self.assertEquals(updated_description, parsed_result['data']['description'])
        self.assertEquals(updated_name, parsed_result['data']['name'])

    def subtest_user_operations(self):
        self.user_name = util.random_name('cli_test_user')
        self.user_description = 'Created by CLI identity tests.'

        result = self.invoke(['user', 'create', '--compartment-id', util.TENANT_ID, '--name', self.user_name, '--description', self.user_description])
        self.user_ocid = util.find_id_in_response(result.output)
        self.validate_response(result, extra_validation=self.validate_user, expect_etag=True)

        result = self.invoke(['user', 'list', '--compartment-id', util.TENANT_ID, '--limit', '1000'])
        self.validate_response(result, extra_validation=self.validate_user)

        result = self.invoke(['user', 'list', '--limit', '1000'])
        self.validate_response(result, extra_validation=self.validate_user)

        self.user_description = 'UPDATED ' + self.user_description
        result = self.invoke(['user', 'update', '--user-id', self.user_ocid, '--description', self.user_description])
        self.validate_response(result, extra_validation=self.validate_user, expect_etag=True)

        result = self.invoke(['user', 'update-user-state', '--user-id', self.user_ocid, '--blocked', 'false'])
        self.validate_response(result, extra_validation=self.validate_user, expect_etag=True)

        result = self.invoke(['user', 'get', '--user-id', self.user_ocid])
        self.validate_response(result, extra_validation=self.validate_user, expect_etag=True)

    def subtest_group_operations(self):
        self.group_name = util.random_name('cli_test_group')
        self.group_description = 'Created by CLI identity tests.'

        result = self.invoke(
            ['group', 'create', '--compartment-id', util.TENANT_ID, '--name', self.group_name, '--description',
             self.group_description])
        self.group_ocid = util.find_id_in_response(result.output)
        self.validate_response(result, extra_validation=self.validate_group, expect_etag=True)

        result = self.invoke(['group', 'list', '--compartment-id', util.TENANT_ID, '--limit', '1000'])
        self.validate_response(result, extra_validation=self.validate_group)

        result = self.invoke(['group', 'list', '--limit', '1000'])
        self.validate_response(result, extra_validation=self.validate_group)

        self.group_description = 'UPDATED ' + self.user_description
        result = self.invoke(['group', 'update', '--group-id', self.group_ocid, '--description', self.group_description])
        self.validate_response(result, extra_validation=self.validate_group, expect_etag=True)

        result = self.invoke(['group', 'get', '--group-id', self.group_ocid])
        self.validate_response(result, extra_validation=self.validate_group, expect_etag=True)

    def subtest_user_group_membership_operations(self):
        result = self.invoke(
            ['group', 'add-user', '--user-id', self.user_ocid, '--group-id', self.group_ocid])
        self.validate_response(result, expect_etag=True)

        result = self.invoke(
            ['group', 'list-users', '--compartment-id', util.TENANT_ID, '--group-id', self.group_ocid])
        self.validate_response(result)
        assert len(json.loads(result.output)['data']) == 1

        result = self.invoke(
            ['group', 'list-users', '--compartment-id', util.TENANT_ID, '--group-id', self.group_ocid, '--all'])
        self.validate_response(result)
        assert len(json.loads(result.output)['data']) == 1
        assert 'opc-next-page' not in result.output

        result = self.invoke(
            ['user', 'list-groups', '--compartment-id', util.TENANT_ID, '--user-id', self.user_ocid])
        self.validate_response(result)
        assert len(json.loads(result.output)['data']) == 1

        result = self.invoke(
            ['group', 'remove-user', '--compartment-id', util.TENANT_ID, '--user-id', self.user_ocid, '--group-id', self.group_ocid, '--force'])
        self.validate_response(result)

        result = self.invoke(
            ['group', 'list-users', '--compartment-id', util.TENANT_ID, '--group-id', self.group_ocid])
        self.validate_response(result)
        assert len(result.output) == 0

    def subtest_api_key_operations(self):
        public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0j0c6GtzuzSBGCT8D/nj
yFtYIl5hsySErWQt/+eSm9bhSMpPBXdNNw/4StMfdtyDlJS6jNDwPAOXXTOU149m
j+CQKiqphy1gawtgMc7riDNA8ufLZ3TisCeXcaC5N/InR7OfERovi2jckB78luXm
jA9txdv1xDcd1akKoHiq7RPlmZnLlPfXzUA0LdppAM0t5poZeeR0l6t/ytWgSxQt
wy9vTSr5jUrHkY1QgKjNmgcRHvIjMSJxOozBiPmFuckuJtOfh+r8jctoLmykB0JY
P8ZM9xRukuJ4bnPTe8olOFB8UCCkAEmkUxtZI4vF90HvDKDOV0KY4OH5YESY6apH
3QIDAQAB
-----END PUBLIC KEY-----"""

        result = self.invoke(
            ['user', 'api-key', 'upload', '--user-id', self.user_ocid, '--key', public_key])
        self.validate_response(result)

        result = self.invoke(
            ['user', 'api-key', 'list', '--user-id', self.user_ocid])
        self.validate_response(result)
        json_response = json.loads(result.output)
        assert len(json_response['data']) == 1
        fingerprint = json_response['data'][0]['fingerprint']

        result = self.invoke(
            ['user', 'api-key', 'delete', '--user-id', self.user_ocid, '--fingerprint', fingerprint, '--force'])
        self.validate_response(result)

        # upload via --key-file
        f = tempfile.NamedTemporaryFile(delete=False)
        try:
            f.write(public_key.encode('UTF-8'))
            f.close()

            result = self.invoke(
                ['user', 'api-key', 'upload', '--user-id', self.user_ocid, '--key-file', f.name])
            self.validate_response(result)

            result = self.invoke(
                ['user', 'api-key', 'list', '--user-id', self.user_ocid])
            self.validate_response(result)
            json_response = json.loads(result.output)
            assert len(json_response['data']) == 1
            fingerprint = json_response['data'][0]['fingerprint']

            result = self.invoke(
                ['user', 'api-key', 'delete', '--user-id', self.user_ocid, '--fingerprint', fingerprint, '--force'])
            self.validate_response(result)
        finally:
            if f:
                f.close()

    def subtest_ui_password_operations(self):
        result = self.invoke(
            ['user', 'ui-password', 'create-or-reset', '--user-id', self.user_ocid])
        self.validate_response(result)
        password = json.loads(result.output)['data']['password']
        assert len(password) > 5

        # Get a new password, verify that it has changed.
        result = self.invoke(
            ['user', 'ui-password', 'create-or-reset', '--user-id', self.user_ocid])
        self.validate_response(result)
        assert password != json.loads(result.output)['data']['password']

    def subtest_swift_password_operations(self):
        description = "Password created by CLI integration tests."
        result = self.invoke(
            ['user', 'swift-password', 'create', '--user-id', self.user_ocid, '--description', description])
        self.validate_response(result, expect_etag=True)
        json_result = json.loads(result.output, )
        password_ocid = json_result['data']['id']
        password = json_result['data']['password']
        assert len(password) > 5
        self.assertEquals(description, json_result['data']['description'])

        description = description + " UPDATED"
        result = self.invoke(
            ['user', 'swift-password', 'update', '--user-id', self.user_ocid, '--swift-password-id', password_ocid, '--description', description])
        self.validate_response(result, expect_etag=True)
        json_result = json.loads(result.output)
        self.assertEquals(description, json_result['data']['description'])

        result = self.invoke(
            ['user', 'swift-password', 'list', '--user-id', self.user_ocid])
        self.validate_response(result)
        json_result = json.loads(result.output)
        self.assertEquals(1, len(json_result['data']))

        result = self.invoke(
            ['user', 'swift-password', 'delete', '--user-id', self.user_ocid, '--swift-password-id', password_ocid, '--force'])
        self.validate_response(result)

    def subtest_policy_operations(self):
        policy_name = util.random_name('cli_test_policy')
        policy_description = 'Created by CLI identity tests.'

        statement_a_policy_base = 'Allow group {} to inspect volume-family in compartment'.format(self.group_name)
        statement_a = "{policy_base} {compartment_name}".format(policy_base=statement_a_policy_base, compartment_name=util.COMPARTMENT_NAME)

        statement_b_policy_base = 'Allow group {} to inspect virtual-network-family in compartment'.format(self.group_name)
        statement_b = "{policy_base} {compartment_name}".format(policy_base=statement_b_policy_base, compartment_name=util.COMPARTMENT_NAME)

        result = self.invoke(
            ['policy',
             'create',
             '--name', policy_name,
             '--compartment-id', util.TENANT_ID,
             '--description', policy_description,
             '--statements', '["{statement}"]'.format(statement=statement_a)])
        policy_ocid = util.find_id_in_response(result.output)
        self.validate_response(result, expect_etag=True)
        self.check_policy_statements_case_insensitive(statement_a_policy_base, result.output)

        # Update description only.
        policy_description = policy_description + "UPDATED!"
        result = self.invoke(
            ['policy',
             'update',
             '--policy-id', policy_ocid,
             '--description', policy_description])
        self.validate_response(result, expect_etag=True)
        self.check_policy_statements_case_insensitive(statement_a_policy_base, result.output)

        statements = '["{statement_a}", "{statement_b}"]'.format(statement_a=statement_a, statement_b=statement_b)
        version_date = "2016-01-01"

        # Try to update statements only - should fail.
        result = self.invoke(
            ['policy',
             'update',
             '--policy-id', policy_ocid,
             '--statements', statements])
        assert result.exit_code != 0

        # Try to update statements only - should fail.
        result = self.invoke(
            ['policy',
             'update',
             '--policy-id', policy_ocid,
             '--statements', statements])
        assert result.exit_code != 0

        # Update statements and version_date, but don't confirm.
        result = self.invoke(
            ['policy',
             'update',
             '--policy-id', policy_ocid,
             '--statements', statements,
             '--version-date', version_date])
        assert result.exit_code != 0

        # Update statements and version_date
        result = self.invoke(
            ['policy',
             'update',
             '--policy-id', policy_ocid,
             '--statements', statements,
             '--version-date', version_date,
             '--force'])
        self.validate_response(result, expect_etag=True)
        self.check_policy_statements_case_insensitive(statement_a_policy_base, result.output)
        self.check_policy_statements_case_insensitive(statement_b_policy_base, result.output)
        assert version_date in result.output

        etag = json.loads(result.output)['etag']
        # Set incorrect etag when updating statements
        result = self.invoke(
            ['policy',
             'update',
             '--policy-id', policy_ocid,
             '--statements', statements,
             '--version-date', version_date,
             '--if-match', 'incorrect_etag'
             '--force'])
        assert result.exit_code != 0

        # Set incorrect etag when updating description
        policy_description = policy_description + " updated again"
        result = self.invoke(
            ['policy',
             'update',
             '--policy-id', policy_ocid,
             '--description', policy_description,
             '--if-match', 'incorrect_etag'])
        assert result.exit_code != 0

        # Set correct etag when updating statements.
        # Remove statement a, clear the version date
        statements = '["{statement_b}"]'.format(statement_b=statement_b)
        result = self.invoke(
            ['policy',
             'update',
             '--policy-id', policy_ocid,
             '--statements', statements,
             '--version-date', "",
             '--if-match', etag,
             '--force'])
        self.validate_response(result, expect_etag=True)
        self.check_policy_statements_case_insensitive(statement_a_policy_base, result.output, check_not_in=True)
        self.check_policy_statements_case_insensitive(statement_b_policy_base, result.output)
        assert version_date not in result.output

        # Set correct etag when updating description
        etag = json.loads(result.output)['etag']
        policy_description = policy_description + " updated again"
        result = self.invoke(
            ['policy',
             'update',
             '--policy-id', policy_ocid,
             '--description', policy_description,
             '--if-match', etag])
        self.validate_response(result, expect_etag=True)
        assert policy_description in result.output
        self.check_policy_statements_case_insensitive(statement_a_policy_base, result.output, check_not_in=True)
        self.check_policy_statements_case_insensitive(statement_b_policy_base, result.output)
        assert version_date not in result.output

        # Get policy
        result = self.invoke(['policy', 'get', '--policy-id', policy_ocid])
        self.validate_response(result, expect_etag=True)
        assert policy_description in result.output
        self.check_policy_statements_case_insensitive(statement_a_policy_base, result.output, check_not_in=True)
        self.check_policy_statements_case_insensitive(statement_b_policy_base, result.output)
        assert version_date not in result.output

        # List policies
        result = self.invoke(['policy', 'list', '--compartment-id', util.TENANT_ID, '--limit', '1000'])
        self.validate_response(result)
        assert policy_description in result.output
        self.check_policy_statements_case_insensitive(statement_a_policy_base, result.output, check_not_in=True)
        self.check_policy_statements_case_insensitive(statement_b_policy_base, result.output)

        result = self.invoke(['policy', 'list', '--compartment-id', util.TENANT_ID, '--limit', '1'])
        self.validate_response(result)
        assert len(json.loads(result.output)['data']) == 1

        self.update_policy_with_tags(policy_ocid)

        # Delete policy
        result = self.invoke(['policy', 'delete', '--policy-id', policy_ocid, '--force'])
        self.validate_response(result)

    def subtest_customer_secret_key_operations(self):
        create_secret_key_one_parsed_result = self.create_and_assert_customer_secret_key('Secret Key One')

        result = self.invoke([
            'customer-secret-key', 'update',
            '--user-id', self.user_ocid,
            '--customer-secret-key-id',
            create_secret_key_one_parsed_result['data']['id'],
            '--display-name',
            'Updated Secret Key One'
        ])
        update_secret_key_one_parsed_result = json.loads(result.output)

        assert update_secret_key_one_parsed_result['data']['id'] == create_secret_key_one_parsed_result['data']['id']
        assert update_secret_key_one_parsed_result['data']['user-id'] == self.user_ocid
        assert update_secret_key_one_parsed_result['data']['display-name'] == 'Updated Secret Key One'
        assert update_secret_key_one_parsed_result['data']['time-created'] is not None
        assert update_secret_key_one_parsed_result['data']['time-expires'] is None
        assert update_secret_key_one_parsed_result['data']['lifecycle-state'] in self.VALID_ACTIVE_CUSTOMER_SECRET_KEY_STATES

        create_secret_key_two_parsed_result = self.create_and_assert_customer_secret_key('Secret Key Two')

        result = self.invoke(['customer-secret-key', 'list', '--user-id', self.user_ocid])
        parsed_list_result = json.loads(result.output)

        assert len(parsed_list_result['data']) == 2
        if parsed_list_result['data'][0]['id'] == create_secret_key_one_parsed_result['data']['id']:
            self.compare_secret_key_dicts(parsed_list_result['data'][0], update_secret_key_one_parsed_result['data'])
            self.compare_secret_key_dicts(parsed_list_result['data'][1], create_secret_key_two_parsed_result['data'])
        else:
            self.compare_secret_key_dicts(parsed_list_result['data'][0], create_secret_key_two_parsed_result['data'])
            self.compare_secret_key_dicts(parsed_list_result['data'][1], update_secret_key_one_parsed_result['data'])

        self.invoke([
            'customer-secret-key', 'delete',
            '--user-id', self.user_ocid,
            '--customer-secret-key-id', create_secret_key_one_parsed_result['data']['id'],
            '--force'
        ])
        self.invoke([
            'customer-secret-key', 'delete',
            '--user-id', self.user_ocid,
            '--customer-secret-key-id', create_secret_key_two_parsed_result['data']['id'],
            '--force'
        ])

        result = self.invoke(['customer-secret-key', 'list', '--user-id', self.user_ocid])
        if result.output:
            parsed_list_result = json.loads(result.output)

            if len(parsed_list_result['data']) != 0:
                for item in parsed_list_result['data']:
                    assert item['lifecycle-state'] in self.VALID_DELETED_CUSTOMER_SECRET_KEY_STATES

    def subtest_region_subscription_operations(self):
        result = self.invoke(['region-subscription', 'list', '--tenancy-id', util.TENANT_ID])
        self.validate_response(result)

        result = self.invoke(['region-subscription', 'list'])
        self.validate_response(result)

    def subtest_cleanup(self):
        if hasattr(self, 'user_ocid'):
            result = self.invoke(['user', 'delete', '--user-id', self.user_ocid], input='n')
            assert result.exit_code != 0

            result = self.invoke(['user', 'delete', '--user-id', self.user_ocid], input='y')
            self.validate_response(result, json_response_expected=False)

            result = self.invoke(['user', 'list', '--compartment-id', util.TENANT_ID, '--limit', '1000'])
            self.validate_response(result)
            assert self.user_ocid not in result.output

        if hasattr(self, 'group_ocid'):
            result = self.invoke(['group', 'delete', '--group-id', self.group_ocid, '--force'])
            self.validate_response(result)

    def validate_group(self, result):
        assert self.group_ocid in result.output
        assert self.group_name in result.output
        assert self.group_description in result.output

    def validate_user(self, result):
        assert self.user_ocid in result.output
        assert self.user_name in result.output
        assert self.user_description in result.output

    def validate_response(self, result, extra_validation=None, expect_etag=False, ** args):
        def common_validation(result):
            if expect_etag:
                assert "etag" in result.output

            if extra_validation:
                extra_validation(result)

        util.validate_response(result, extra_validation=common_validation, ** args)

    def invoke(self, params, debug=False, ** args):
        commands = ['iam'] + params

        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command_as_admin(commands, ** args)

    def check_policy_statements_case_insensitive(self, statement, result_output, check_not_in=False):
        if check_not_in:
            assert statement.lower() not in result_output.lower()
        else:
            assert statement.lower() in result_output.lower()

    def get_compartment_to_rename(self):
        keep_paginating = True
        next_page = None
        while keep_paginating:
            if next_page:
                result = self.invoke(['compartment', 'list', '--compartment-id', util.TENANT_ID, '--limit', '1000', '--page', next_page])
            else:
                result = self.invoke(['compartment', 'list', '--compartment-id', util.TENANT_ID, '--limit', '1000'])

            parsed_result = json.loads(result.output)

            for item in parsed_result['data']:
                if item['name'].find(self.RENAME_COMPARTMENT_PREFIX) == 0:
                    return item

            if 'opc-next-page' in parsed_result:
                next_page = parsed_result['opc-next-page']
            keep_paginating = (next_page is not None)

        # If we're here, we need to create the compartment.
        # Could also create PythonCliCompartmentRenameTest-0 ahead of time and add privs
        # to the the compartment via policy.
        result = self.invoke([
            'compartment', 'create',
            '--compartment-id', util.TENANT_ID,
            '--name', '{}{}'.format(self.RENAME_COMPARTMENT_PREFIX, util.random_number_string()),
            '--description', 'Compartment for CLI compartment rename testing',
            '--profile', 'ADMIN'
        ])
        parsed_result = json.loads(result.output)
        print('Created compartment: {}'.format(parsed_result['data']))

        return parsed_result['data']

    def create_and_assert_customer_secret_key(self, display_name):
        result = self.invoke(['customer-secret-key', 'create', '--user-id', self.user_ocid, '--display-name', display_name])
        create_secret_parsed_result = json.loads(result.output)

        assert create_secret_parsed_result['data']['key'] is not None
        assert create_secret_parsed_result['data']['id'] is not None
        assert create_secret_parsed_result['data']['user-id'] == self.user_ocid
        assert create_secret_parsed_result['data']['display-name'] == display_name
        assert create_secret_parsed_result['data']['time-created'] is not None
        assert create_secret_parsed_result['data']['time-expires'] is None
        assert create_secret_parsed_result['data']['lifecycle-state'] in self.VALID_ACTIVE_CUSTOMER_SECRET_KEY_STATES

        return create_secret_parsed_result

    def compare_secret_key_dicts(self, dict_one, dict_two):
        assert dict_one['id'] == dict_two['id']
        assert dict_one['display-name'] == dict_two['display-name']
        assert dict_one['user-id'] == dict_two['user-id']
        assert dict_one['display-name'] == dict_two['display-name']
        assert dict_one['time-created'] == dict_two['time-created']
        assert dict_one['time-expires'] == dict_two['time-expires']
        assert dict_one['lifecycle-state'] == dict_two['lifecycle-state']

    def update_policy_with_tags(self, policy_ocid):
        tag_names_to_values = {}
        for t in tag_data_container.tags:
            tag_names_to_values[t.name] = 'update_policy {} 1'.format(t.name)
        tag_data_container.write_defined_tags_to_file(
            os.path.join('tests', 'temp', 'defined_tags_identity.json'),
            tag_data_container.tag_namespace,
            tag_names_to_values
        )

        result = self.invoke([
            'policy', 'update',
            '--policy-id', policy_ocid,
            '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_1.json',
            '--defined-tags', 'file://tests/temp/defined_tags_identity.json',
            '--force'
        ])
        self.validate_response(result)
        parsed_result = json.loads(result.output)
        expected_freeform = {'tagOne': 'value1', 'tag_Two': 'value two'}
        expected_defined = {tag_data_container.tag_namespace.name: tag_names_to_values}
        assert expected_freeform == parsed_result['data']['freeform-tags']
        assert expected_defined == parsed_result['data']['defined-tags']

        result = self.invoke(['policy', 'get', '--policy-id', policy_ocid])
        parsed_result = json.loads(result.output)
        assert expected_freeform == parsed_result['data']['freeform-tags']
        assert expected_defined == parsed_result['data']['defined-tags']

        result = self.invoke(['policy', 'list', '-c', util.TENANT_ID, '--all'])
        parsed_result = json.loads(result.output)
        found_policy = False
        for pr in parsed_result['data']:
            if pr['id'] == policy_ocid:
                assert expected_freeform == pr['freeform-tags']
                assert expected_defined == pr['defined-tags']
                found_policy = True
                break
        assert found_policy

        tag_names_to_values.pop(tag_data_container.tags[1].name)
        tag_data_container.write_defined_tags_to_file(
            os.path.join('tests', 'temp', 'defined_tags_identity.json'),
            tag_data_container.tag_namespace,
            tag_names_to_values
        )
        result = self.invoke([
            'policy', 'update',
            '--policy-id', policy_ocid,
            '--freeform-tags', 'file://tests/resources/tagging/freeform_tags_2.json',
            '--defined-tags', 'file://tests/temp/defined_tags_identity.json',
            '--force'
        ])
        self.validate_response(result)
        parsed_result = json.loads(result.output)
        expected_freeform = {'tagOne': 'value three'}
        expected_defined = {tag_data_container.tag_namespace.name: tag_names_to_values}
        assert expected_freeform == parsed_result['data']['freeform-tags']
        assert expected_defined == parsed_result['data']['defined-tags']

        result = self.invoke(['policy', 'get', '--policy-id', policy_ocid])
        parsed_result = json.loads(result.output)
        assert expected_freeform == parsed_result['data']['freeform-tags']
        assert expected_defined == parsed_result['data']['defined-tags']

        result = self.invoke([
            'policy', 'update',
            '--policy-id', policy_ocid,
            '--freeform-tags', '{}',
            '--defined-tags', '{}',
            '--force'
        ])
        self.validate_response(result)
        parsed_result = json.loads(result.output)
        assert {} == parsed_result['data']['freeform-tags']
        assert {} == parsed_result['data']['defined-tags']

        result = self.invoke(['policy', 'get', '--policy-id', policy_ocid])
        parsed_result = json.loads(result.output)
        assert {} == parsed_result['data']['freeform-tags']
        assert {} == parsed_result['data']['defined-tags']

        result = self.invoke(['policy', 'list', '-c', util.TENANT_ID, '--all'])
        parsed_result = json.loads(result.output)
        found_policy = False
        for pr in parsed_result['data']:
            if pr['id'] == policy_ocid:
                assert {} == pr['freeform-tags']
                assert {} == pr['defined-tags']
                found_policy = True
                break
        assert found_policy


if __name__ == '__main__':
    unittest.main()
