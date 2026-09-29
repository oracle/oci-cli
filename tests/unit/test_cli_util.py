# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates. All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
import os
import oci
import sys
import pytest
import requests
import tempfile
import unittest
import unittest.mock as mock
from oci_cli import cli_constants, cli_util


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


class MockSseEvent(object):
    def __init__(self, data):
        self.data = data


class MockSseStream(object):
    def __init__(self, events):
        self._events = events

    def events(self):
        return iter(self._events)


class TestCliUtil(unittest.TestCase):

    @staticmethod
    def _build_ctx():
        ctx = Obj()
        ctx.obj = Obj()
        ctx.obj['query'] = None
        ctx.obj['debug'] = False
        ctx.obj['default_values_from_file'] = {}
        return ctx

    @staticmethod
    def _build_paginated_response(data, has_next_page=False, next_page=None):
        response = Obj()
        response.status = 200
        response.headers = {'opc-request-id': 'test'}
        response.data = data
        response.request = 'request'
        response.has_next_page = has_next_page
        response.next_page = next_page
        return response

    @staticmethod
    def _build_sse_response(event_payloads):
        response = Obj()
        response.status = 200
        response.headers = {'content-type': 'text/event-stream'}
        response.data = MockSseStream([MockSseEvent(payload) for payload in event_payloads])
        return response

    @staticmethod
    def _build_pkcs11_client_config():
        client_config = {
            'user': 'ocid1.user.oc1..test',
            'tenancy': 'ocid1.tenancy.oc1..test',
            'region': 'us-phoenix-1'
        }

        return client_config

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

    def _assert_pkcs11_signer_values(
        self,
        ctx,
        expected_pin='123456',
        expected_slot=None,
        expected_key_id=None,
        expected_token_label=None,
        expected_token_serial=None,
        expected_key_id_override=None,
        expected_module_path=None,
        env=None
    ):
        client_config = self._build_pkcs11_client_config()
        signer = Obj()
        signer.pkcs11_signer = Obj()

        class FakePKCS11RequestSigner(object):
            @staticmethod
            def get_pkcs11_signer(config, pin, pkcs11_slot=None, pkcs11_key_id=None, pkcs11_token_label=None, pkcs11_token_serial=None, pkcs11_key_id_override=None, pkcs11_module_path=None):
                assert config is client_config
                assert pin == expected_pin
                assert pkcs11_slot == expected_slot
                assert pkcs11_key_id == expected_key_id
                assert pkcs11_token_label == expected_token_label
                assert pkcs11_token_serial == expected_token_serial
                assert pkcs11_key_id_override == expected_key_id_override
                assert pkcs11_module_path == expected_module_path
                return signer

            @staticmethod
            def get_pkcs11_pin():
                return expected_pin

        with mock.patch.object(oci.auth.signers, 'PKCS11RequestSigner', FakePKCS11RequestSigner, create=True):
            with mock.patch.dict(os.environ, env or {}, clear=True):
                assert cli_util.get_pkcs11_signer(ctx, client_config) is signer

    def test_pkcs11_config_can_be_valid_from_env_without_fingerprint_or_key_file(self):
        command_args = {
            'auth': cli_constants.OCI_CLI_AUTH_PKCS11,
            'region': None
        }

        with mock.patch.dict(os.environ, {
            cli_constants.OCI_CLI_USER_ENV_VAR: 'ocid1.user.oc1..test',
            cli_constants.OCI_CLI_TENANCY_ENV_VAR: 'ocid1.tenancy.oc1..test',
            cli_constants.OCI_CLI_REGION_ENV_VAR: 'us-phoenix-1'
        }, clear=True):
            assert cli_util.is_config_valid_from_env(command_args)

    def test_pkcs11_config_from_env_accepts_region_from_root_option(self):
        command_args = {
            'auth': cli_constants.OCI_CLI_AUTH_PKCS11,
            'region': 'us-phoenix-1'
        }

        with mock.patch.dict(os.environ, {
            cli_constants.OCI_CLI_USER_ENV_VAR: 'ocid1.user.oc1..test',
            cli_constants.OCI_CLI_TENANCY_ENV_VAR: 'ocid1.tenancy.oc1..test'
        }, clear=True):
            assert cli_util.is_config_valid_from_env(command_args)

    def test_pkcs11_config_from_env_requires_user_and_tenancy(self):
        command_args = {
            'auth': cli_constants.OCI_CLI_AUTH_PKCS11,
            'region': 'us-phoenix-1'
        }

        with mock.patch.dict(os.environ, {
            cli_constants.OCI_CLI_USER_ENV_VAR: 'ocid1.user.oc1..test'
        }, clear=True):
            assert not cli_util.is_config_valid_from_env(command_args)

    @pytest.mark.skipif(sys.version_info < (3, 9),
                        reason="Python 3.9.0 or higher is required for using pkcs11 authentication. Skipping this test.")
    def test_get_pkcs11_signer_reads_optional_values_from_profile_rc_defaults(self):
        ctx = self._build_ctx()
        ctx.obj['settings'] = {}
        ctx.obj['default_values_from_file'] = {
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_SLOT_LABEL_KEY: 'PIV AUTH',
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_TOKEN_LABEL_KEY: 'token-label-from-rc',
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_KEY_ID_OVERRIDE_KEY: 'override-from-rc',
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_MODULE_PATH_KEY: '/tmp/pkcs11-from-rc.so'
        }

        self._assert_pkcs11_signer_values(
            ctx,
            expected_slot='PIV AUTH',
            expected_token_label='token-label-from-rc',
            expected_key_id_override='override-from-rc',
            expected_module_path='/tmp/pkcs11-from-rc.so'
        )

    @pytest.mark.skipif(sys.version_info < (3, 9),
                        reason="Python 3.9.0 or higher is required for using pkcs11 authentication. Skipping this test.")
    def test_get_pkcs11_signer_env_overrides_profile_rc_defaults(self):
        ctx = self._build_ctx()
        ctx.obj['settings'] = {}
        ctx.obj['default_values_from_file'] = {
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_SLOT_LABEL_KEY: 'PIV AUTH',
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_TOKEN_SERIAL_NUMBER_KEY: 'serial-from-rc',
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_KEY_ID_OVERRIDE_KEY: 'override-from-rc',
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_MODULE_PATH_KEY: '/tmp/pkcs11-from-rc.so'
        }

        self._assert_pkcs11_signer_values(
            ctx,
            expected_slot='CARD AUTH',
            expected_token_serial='serial-from-env',
            expected_key_id_override='override-from-env',
            expected_module_path='/tmp/pkcs11-from-env.so',
            expected_pin='pin-from-env',
            env={
                cli_constants.OCI_CLI_PKCS11_SLOT_LABEL_ENV_VAR: 'CARD AUTH',
                cli_constants.OCI_CLI_PKCS11_TOKEN_SERIAL_ENV_VAR: 'serial-from-env',
                cli_constants.OCI_CLI_PKCS11_KEY_ID_OVERRIDE_ENV_VAR: 'override-from-env',
                cli_constants.OCI_CLI_PKCS11_MODULE_PATH_ENV_VAR: '/tmp/pkcs11-from-env.so',
                cli_constants.OCI_CLI_PKCS11_PIN_ENV_VAR: 'pin-from-env'
            }
        )

    @pytest.mark.skipif(sys.version_info < (3, 9),
                        reason="Python 3.9.0 or higher is required for using pkcs11 authentication. Skipping this test.")
    def test_get_pkcs11_signer_prompts_for_piv_auth_when_env_pin_is_set(self):
        ctx = self._build_ctx()
        ctx.obj['settings'] = {}
        ctx.obj['default_values_from_file'] = {
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_SLOT_LABEL_KEY: 'PIV AUTH'
        }
        self._assert_pkcs11_signer_values(
            ctx,
            expected_pin='prompted-pin',
            expected_slot='PIV AUTH',
            env={cli_constants.OCI_CLI_PKCS11_PIN_ENV_VAR: 'pin-from-env'}
        )

    @pytest.mark.skipif(sys.version_info < (3, 9),
                        reason="Python 3.9.0 or higher is required for using pkcs11 authentication. Skipping this test.")
    def test_get_pkcs11_signer_uses_env_pin_for_card_auth_without_prompting(self):
        ctx = self._build_ctx()
        ctx.obj['settings'] = {}
        ctx.obj['default_values_from_file'] = {
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_SLOT_LABEL_KEY: 'CARD AUTH'
        }
        client_config = self._build_pkcs11_client_config()
        signer = Obj()
        signer.pkcs11_signer = Obj()

        class FakePKCS11RequestSigner(object):
            @staticmethod
            def get_pkcs11_signer(config, pin, **kwargs):
                assert config is client_config
                assert pin == 'pin-from-env'
                assert kwargs['pkcs11_slot'] == 'CARD AUTH'
                return signer

            @staticmethod
            def get_pkcs11_pin():
                raise AssertionError('PIN prompt should not be used when OCI_CLI_PKCS11_PIN is set')

        with mock.patch.object(oci.auth.signers, 'PKCS11RequestSigner', FakePKCS11RequestSigner, create=True):
            with mock.patch.dict(os.environ, {cli_constants.OCI_CLI_PKCS11_PIN_ENV_VAR: 'pin-from-env'}, clear=True):
                with mock.patch.object(click, 'echo') as echo:
                    assert cli_util.get_pkcs11_signer(ctx, client_config) is signer

        warning = echo.call_args_list[0][0][0]
        assert cli_constants.OCI_CLI_PKCS11_PIN_ENV_VAR in warning
        assert 'Unset it' in warning

    @pytest.mark.skipif(sys.version_info < (3, 9),
                        reason="Python 3.9.0 or higher is required for using pkcs11 authentication. Skipping this test.")
    def test_get_pkcs11_signer_warns_and_prompts_for_card_auth_without_env_pin(self):
        ctx = self._build_ctx()
        ctx.obj['settings'] = {}
        ctx.obj['default_values_from_file'] = {
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_SLOT_LABEL_KEY: 'CARD AUTH'
        }
        client_config = self._build_pkcs11_client_config()
        signer = Obj()
        signer.pkcs11_signer = Obj()

        class FakePKCS11RequestSigner(object):
            @staticmethod
            def get_pkcs11_signer(config, pin, **kwargs):
                assert config is client_config
                assert pin == 'prompted-pin'
                assert kwargs['pkcs11_slot'] == 'CARD AUTH'
                return signer

            @staticmethod
            def get_pkcs11_pin():
                return 'prompted-pin'

        with mock.patch.object(oci.auth.signers, 'PKCS11RequestSigner', FakePKCS11RequestSigner, create=True):
            with mock.patch.dict(os.environ, {}, clear=True):
                with mock.patch.object(click, 'echo') as echo:
                    assert cli_util.get_pkcs11_signer(ctx, client_config) is signer

        warning = echo.call_args_list[0][0][0]
        assert cli_constants.OCI_CLI_PKCS11_PIN_ENV_VAR in warning
        assert 'each CLI command' in warning

    @pytest.mark.skipif(sys.version_info < (3, 9),
                        reason="Python 3.9.0 or higher is required for using pkcs11 authentication. Skipping this test.")
    def test_get_pkcs11_signer_rejects_empty_pin(self):
        ctx = self._build_ctx()
        ctx.obj['settings'] = {}
        client_config = self._build_pkcs11_client_config()

        class FakePKCS11RequestSigner(object):
            @staticmethod
            def get_pkcs11_pin():
                return ''

        with mock.patch.object(oci.auth.signers, 'PKCS11RequestSigner', FakePKCS11RequestSigner, create=True):
            with mock.patch.dict(os.environ, {}, clear=True):
                with self.assertRaises(SystemExit) as raised:
                    cli_util.get_pkcs11_signer(ctx, client_config)

        assert "PKCS#11 PIN cannot be empty." in str(raised.exception)

    @pytest.mark.skipif(sys.version_info < (3, 9),
                        reason="Python 3.9.0 or higher is required for using pkcs11 authentication. Skipping this test.")
    def test_get_pkcs11_signer_warns_and_prefers_slot_label_over_key_id(self):
        ctx = self._build_ctx()
        ctx.obj['default_values_from_file'] = {
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_SLOT_LABEL_KEY: 'CARD AUTH',
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_KEY_ID_KEY: '04'
        }
        signer = Obj()
        signer.pkcs11_signer = Obj()

        class FakePKCS11RequestSigner(object):
            @staticmethod
            def get_pkcs11_signer(config, pin, **kwargs):
                assert kwargs['pkcs11_slot'] == 'CARD AUTH'
                assert kwargs['pkcs11_key_id'] is None
                return signer

        with mock.patch.object(oci.auth.signers, 'PKCS11RequestSigner', FakePKCS11RequestSigner, create=True):
            with mock.patch.dict(os.environ, {cli_constants.OCI_CLI_PKCS11_PIN_ENV_VAR: 'pin-from-env'}, clear=True):
                with mock.patch.object(click, 'echo') as echo:
                    assert cli_util.get_pkcs11_signer(ctx, self._build_pkcs11_client_config()) is signer

        assert "pkcs11_slot_label and pkcs11_key_id cannot both be provided" in echo.call_args_list[0][0][0]

    @pytest.mark.skipif(sys.version_info < (3, 9),
                        reason="Python 3.9.0 or higher is required for using pkcs11 authentication. Skipping this test.")
    def test_get_pkcs11_signer_warns_and_prefers_token_label_over_token_serial(self):
        ctx = self._build_ctx()
        ctx.obj['default_values_from_file'] = {
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_TOKEN_LABEL_KEY: 'token-label',
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_TOKEN_SERIAL_NUMBER_KEY: 'serial'
        }
        signer = Obj()
        signer.pkcs11_signer = Obj()

        class FakePKCS11RequestSigner(object):
            @staticmethod
            def get_pkcs11_signer(config, pin, **kwargs):
                assert kwargs['pkcs11_token_label'] == 'token-label'
                assert kwargs['pkcs11_token_serial'] is None
                return signer

            @staticmethod
            def get_pkcs11_pin():
                return 'prompted-pin'

        with mock.patch.object(oci.auth.signers, 'PKCS11RequestSigner', FakePKCS11RequestSigner, create=True):
            with mock.patch.dict(os.environ, {}, clear=True):
                with mock.patch.object(click, 'echo') as echo:
                    assert cli_util.get_pkcs11_signer(ctx, self._build_pkcs11_client_config()) is signer

        assert "pkcs11_token_label and pkcs11_token_serial cannot both be provided" in echo.call_args_list[0][0][0]

    @pytest.mark.skipif(sys.version_info < (3, 9),
                        reason="Python 3.9.0 or higher is required for using pkcs11 authentication. Skipping this test.")
    def test_get_pkcs11_signer_shows_actionable_pin_incorrect_error(self):
        ctx = self._build_ctx()
        ctx.obj['settings'] = {}
        ctx.obj['default_values_from_file'] = {
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_SLOT_LABEL_KEY: 'PIV AUTH'
        }
        client_config = self._build_pkcs11_client_config()

        class PinIncorrect(RuntimeError):
            pass

        class FakePKCS11RequestSigner(object):
            @staticmethod
            def get_pkcs11_signer(config, pin, **kwargs):
                raise PinIncorrect('PIN_INCORRECT')

            @staticmethod
            def get_pkcs11_pin():
                return '123456'

        with mock.patch.object(oci.auth.signers, 'PKCS11RequestSigner', FakePKCS11RequestSigner, create=True):
            with mock.patch.dict(os.environ, {}, clear=True):
                with self.assertRaises(SystemExit) as raised:
                    cli_util.get_pkcs11_signer(ctx, client_config)

        assert "Failed to initialize PKCS#11 signer: The PKCS#11 PIN was rejected by the token." in str(raised.exception)

    @pytest.mark.skipif(sys.version_info < (3, 9),
                        reason="Python 3.9.0 or higher is required for using pkcs11 authentication. Skipping this test.")
    def test_get_pkcs11_signer_shows_actionable_user_not_logged_in_error(self):
        ctx = self._build_ctx()
        ctx.obj['settings'] = {}
        ctx.obj['default_values_from_file'] = {
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_SLOT_LABEL_KEY: 'CARD AUTH'
        }
        client_config = self._build_pkcs11_client_config()

        class UserNotLoggedIn(RuntimeError):
            pass

        class FakePKCS11RequestSigner(object):
            @staticmethod
            def get_pkcs11_signer(config, pin, **kwargs):
                assert pin == '123456'
                raise UserNotLoggedIn('USER_NOT_LOGGED_IN')

            @staticmethod
            def get_pkcs11_pin():
                return '123456'

        with mock.patch.object(oci.auth.signers, 'PKCS11RequestSigner', FakePKCS11RequestSigner, create=True):
            with mock.patch.dict(os.environ, {}, clear=True):
                with self.assertRaises(SystemExit) as raised:
                    cli_util.get_pkcs11_signer(ctx, client_config)

        assert "Failed to initialize PKCS#11 signer: The selected PKCS#11 key requires user login before signing." in str(raised.exception)

    @pytest.mark.skipif(sys.version_info < (3, 9),
                        reason="Python 3.9.0 or higher is required for using pkcs11 authentication. Skipping this test.")
    def test_get_pkcs11_signer_prints_card_auth_touch_guidance(self):
        ctx = self._build_ctx()
        ctx.obj['settings'] = {}
        ctx.obj['default_values_from_file'] = {
            cli_constants.CLI_RC_GENERIC_SETTINGS_PKCS11_SLOT_LABEL_KEY: 'CARD AUTH'
        }
        client_config = self._build_pkcs11_client_config()
        signer = Obj()
        signer.pkcs11_signer = Obj()

        class FakePKCS11RequestSigner(object):
            @staticmethod
            def get_pkcs11_signer(config, pin, **kwargs):
                assert pin == 'pin-from-env'
                assert kwargs['pkcs11_slot'] == 'CARD AUTH'
                return signer

        with mock.patch.object(oci.auth.signers, 'PKCS11RequestSigner', FakePKCS11RequestSigner, create=True):
            with mock.patch.dict(os.environ, {cli_constants.OCI_CLI_PKCS11_PIN_ENV_VAR: 'pin-from-env'}, clear=True):
                with mock.patch('oci_cli.cli_util.click.echo') as mock_echo:
                    assert cli_util.get_pkcs11_signer(ctx, client_config) is signer

        assert mock_echo.call_count == 2
        assert 'Using PKCS#11 CARD AUTH PIN from' in mock_echo.call_args_list[0][0][0]
        assert 'Touch the pkcs11 external authenticator when it blinks to authorize signing.' in mock_echo.call_args_list[1][0][0]

    def test_root_command_rejects_removed_pkcs11_selector_option(self):
        from click.testing import CliRunner
        from oci_cli.cli_root import cli

        result = CliRunner().invoke(cli, ['--pkcs11-slot-label', 'CARD AUTH', '--help'])

        assert result.exit_code == 2
        assert 'No such command' in result.output

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

    def test_set_request_session_properties_uses_requests_ca_bundle_env(self):
        ctx = Obj()
        ctx.obj = {
            'cert_bundle': None,
            'proxy': None,
            'settings': {}
        }
        session = requests.Session()
        session.trust_env = False

        with tempfile.NamedTemporaryFile() as cert_bundle:
            with mock.patch.dict(os.environ, {'REQUESTS_CA_BUNDLE': cert_bundle.name}):
                cli_util.set_request_session_properties_from_context(session, ctx)

            assert session.verify == cert_bundle.name

    def test_set_request_session_properties_uses_curl_ca_bundle_env(self):
        ctx = Obj()
        ctx.obj = {
            'cert_bundle': None,
            'proxy': None,
            'settings': {}
        }
        session = requests.Session()
        session.trust_env = False

        with tempfile.NamedTemporaryFile() as cert_bundle:
            with mock.patch.dict(os.environ, {'CURL_CA_BUNDLE': cert_bundle.name}, clear=False):
                os.environ.pop('REQUESTS_CA_BUNDLE', None)
                cli_util.set_request_session_properties_from_context(session, ctx)

            assert session.verify == cert_bundle.name

    def test_set_request_session_properties_rejects_missing_env_ca_bundle(self):
        ctx = Obj()
        ctx.obj = {
            'cert_bundle': None,
            'proxy': None,
            'settings': {}
        }
        session = requests.Session()
        session.trust_env = False

        with tempfile.NamedTemporaryFile() as missing_bundle:
            missing_bundle_path = missing_bundle.name

        with mock.patch.dict(os.environ, {'REQUESTS_CA_BUNDLE': missing_bundle_path}):
            with self.assertRaises(click.BadParameter):
                cli_util.set_request_session_properties_from_context(session, ctx)

    def test_set_request_session_properties_cert_bundle_overrides_env(self):
        ctx = Obj()
        ctx.obj = {
            'proxy': None,
            'settings': {}
        }
        session = requests.Session()
        session.trust_env = False

        with tempfile.NamedTemporaryFile() as cert_bundle:
            ctx.obj['cert_bundle'] = cert_bundle.name
            with mock.patch.dict(os.environ, {'REQUESTS_CA_BUNDLE': '/tmp/test-ca-bundle.pem'}):
                cli_util.set_request_session_properties_from_context(session, ctx)

            assert session.verify == cert_bundle.name

    def test_get_possible_subtype_based_on_payload(self):
        payload = {
            'instanceType': 'compute',
            'instanceDetails': {}
        }

        subtype = cli_util.get_possible_subtype_based_on_payload(oci.core.models.InstanceConfigurationInstanceDetails, 'core', payload)
        assert subtype.__class__.__name__ == 'ComputeInstanceDetails'

    def test_list_call_get_all_results_stream_output_returns_response(self):
        ctx = self._build_ctx()

        with mock.patch('oci_cli.cli_util.stream_header') as mock_stream_header:
            with mock.patch('oci_cli.cli_util.stream_page', return_value=True) as mock_stream_page:
                with mock.patch('oci_cli.cli_util.stream_footer') as mock_stream_footer:
                    response = cli_util.list_call_get_all_results(
                        lambda **kwargs: self._build_paginated_response(['item']),
                        ctx=ctx,
                        stream_output=True
                    )

        assert response.status == 200
        assert response.headers == {'opc-request-id': 'test'}
        assert response.data == []
        assert response.request == 'request'
        mock_stream_header.assert_called_once()
        mock_stream_page.assert_called_once()
        mock_stream_footer.assert_called_once()

    def test_list_call_get_all_results_stream_output_does_not_swallow_exceptions(self):
        ctx = self._build_ctx()

        with mock.patch('oci_cli.cli_util.stream_header'):
            with mock.patch('oci_cli.cli_util.stream_footer'):
                with self.assertRaises(RuntimeError):
                    cli_util.list_call_get_all_results(
                        lambda **kwargs: (_ for _ in ()).throw(RuntimeError('boom')),
                        ctx=ctx,
                        stream_output=True
                    )

    def test_list_call_get_all_results_multiple_keys_stream_output_returns_response(self):
        ctx = self._build_ctx()

        with mock.patch('oci_cli.cli_util.stream_header') as mock_stream_header:
            with mock.patch('oci_cli.cli_util.stream_page', return_value=True) as mock_stream_page:
                with mock.patch('oci_cli.cli_util.stream_footer') as mock_stream_footer:
                    response = cli_util.list_call_get_all_results_multiple_keys(
                        lambda **kwargs: self._build_paginated_response(['item']),
                        ctx=ctx,
                        stream_output=True
                    )

        assert response.status == 200
        assert response.headers == {'opc-request-id': 'test'}
        assert response.data == []
        assert response.request == 'request'
        mock_stream_header.assert_called_once()
        mock_stream_page.assert_called_once()
        mock_stream_footer.assert_called_once()

    def test_list_call_get_all_results_multiple_keys_stream_output_does_not_swallow_exceptions(self):
        ctx = self._build_ctx()

        with mock.patch('oci_cli.cli_util.stream_header'):
            with mock.patch('oci_cli.cli_util.stream_footer'):
                with self.assertRaises(RuntimeError):
                    cli_util.list_call_get_all_results_multiple_keys(
                        lambda **kwargs: (_ for _ in ()).throw(RuntimeError('boom')),
                        ctx=ctx,
                        stream_output=True
                    )

    def test_render_response_outputs_non_json_sse_event_without_crashing(self):
        ctx = self._build_ctx()
        ctx.obj['output'] = 'json'
        ctx.obj['raw_output'] = None
        response = self._build_sse_response([
            '{"index": 0, "message": {"role": "ASSISTANT"}}',
            '{"usage": {"completionTokens": 8, "promptTokens": 4, "totalTokens": 12}}',
            '[DONE]'
        ])

        with mock.patch('oci_cli.cli_util.render') as mock_render:
            with mock.patch('oci_cli.cli_util.print') as mock_print:
                cli_util.render_response(response, ctx)

        self.assertEqual(2, mock_render.call_count)
        self.assertEqual(1, mock_print.call_count)
        mock_print.assert_called_once_with('"[DONE]"')

    def test_render_response_skips_empty_or_whitespace_only_sse_events(self):
        ctx = self._build_ctx()
        ctx.obj['output'] = 'json'
        ctx.obj['raw_output'] = None
        response = self._build_sse_response([
            '{"index": 0, "message": {"role": "ASSISTANT"}}',
            '{"usage": {"completionTokens": 8, "promptTokens": 4, "totalTokens": 12}}',
            '    ',
            '\n\t\t',
            '  [DONE]  \t'
        ])

        with mock.patch('oci_cli.cli_util.render') as mock_render:
            with mock.patch('oci_cli.cli_util.print') as mock_print:
                cli_util.render_response(response, ctx)

        self.assertEqual(2, mock_render.call_count)
        self.assertEqual(1, mock_print.call_count)
        mock_print.assert_called_once_with('"[DONE]"')
