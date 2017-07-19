# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import oraclebmc_cli
import unittest
from . import command_coverage_validator
from . import util
from oraclebmc_cli import config

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

import os
import os.path
import sys

TEMP_DIR = 'tests/temp'

CONFIG_FILENAME = os.path.join(TEMP_DIR, 'config')
REGION = 'us-phoenix-1'
PASSPHRASE = 'passphrase'
PASSPHRASE_FILE = 'tests/resources/test_passphrase_file.txt'

PUBLIC_KEY_FILENAME = os.path.join(TEMP_DIR, 'bmcs_api_key_public.pem')
PRIVATE_KEY_FILENAME = os.path.join(TEMP_DIR, 'bmcs_api_key.pem')


class TestSetup(unittest.TestCase):

    @util.log_test
    @command_coverage_validator.CommandCoverageValidator(oraclebmc_cli.cli_setup.setup_group)
    def test_all_operations(self, validator):
        self.validator = validator

        self.subtest_keys()
        self.subtest_keys_with_passphrase_option()
        self.subtest_keys_with_passphrase_file_option()
        self.subtest_keys_with_passphrase_file_option_from_stdin()
        self.subtest_keys_passphrase_and_passphrase_file_both_specified_returns_error()

        self.subtest_config_generate_keys()
        self.subtest_config_existing_keys()
        self.subtest_config_existing_keys_expands_user_directory()
        self.subtest_config_invalid_user_ocid()
        self.subtest_config_invalid_tenancy_ocid()

        self.subtest_autocomplete_deny_bash_rc_access()

    @util.log_test
    def subtest_keys(self):
        stdin = [
            PASSPHRASE,     # passphrase
            PASSPHRASE      # confirm passphrase
        ]

        self.invoke(
            ['setup', 'keys', '--output-dir', TEMP_DIR, '--overwrite'], input='\n'.join(stdin))

        assert os.path.isfile(PUBLIC_KEY_FILENAME), 'bmcs setup keys should generate private key file'
        assert os.path.isfile(PRIVATE_KEY_FILENAME), 'bmcs setup keys should generate public key file'

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key
        assert oraclebmc_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME, PASSPHRASE)

        self.cleanup_default_generated_files()

    @util.log_test
    def subtest_keys_with_passphrase_option(self):

        self.invoke(
            ['setup', 'keys', '--output-dir', TEMP_DIR, '--overwrite', '--passphrase', PASSPHRASE])

        assert os.path.isfile(PUBLIC_KEY_FILENAME), 'bmcs setup keys should generate private key file'
        assert os.path.isfile(PRIVATE_KEY_FILENAME), 'bmcs setup keys should generate public key file'

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key
        assert oraclebmc_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME, PASSPHRASE)

        self.cleanup_default_generated_files()

    @util.log_test
    def subtest_keys_with_passphrase_file_option(self):

        self.invoke(
            ['setup', 'keys', '--output-dir', TEMP_DIR, '--overwrite', '--passphrase-file', PASSPHRASE_FILE])

        assert os.path.isfile(PUBLIC_KEY_FILENAME), 'bmcs setup keys should generate private key file'
        assert os.path.isfile(PRIVATE_KEY_FILENAME), 'bmcs setup keys should generate public key file'

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key
        assert oraclebmc_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME, PASSPHRASE)

        self.cleanup_default_generated_files()

    @util.log_test
    def subtest_keys_with_passphrase_file_option_from_stdin(self):

        self.invoke(
            ['setup', 'keys', '--output-dir', TEMP_DIR, '--overwrite', '--passphrase-file', '-'], input=PASSPHRASE)

        assert os.path.isfile(PUBLIC_KEY_FILENAME), 'bmcs setup keys should generate private key file'
        assert os.path.isfile(PRIVATE_KEY_FILENAME), 'bmcs setup keys should generate public key file'

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key
        assert oraclebmc_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME, PASSPHRASE)

        self.cleanup_default_generated_files()

    @util.log_test
    def subtest_keys_passphrase_and_passphrase_file_both_specified_returns_error(self):

        result = self.invoke(
            ['setup', 'keys', '--output-dir', TEMP_DIR, '--overwrite', '--passphrase', PASSPHRASE,
             '--passphrase-file', PASSPHRASE_FILE])

        assert result.exit_code != 0

        self.cleanup_default_generated_files()

    @util.log_test
    def subtest_keys_empty_passphrase(self):

        # single 'return' to enter empty for the password prompt
        stdin = '\n'
        self.invoke(
            ['setup', 'keys', '--output-dir', TEMP_DIR, '--overwrite'], input=stdin)

        assert os.path.isfile(PUBLIC_KEY_FILENAME), 'bmcs setup keys should generate private key file'
        assert os.path.isfile(PRIVATE_KEY_FILENAME), 'bmcs setup keys should generate public key file'

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key
        assert oraclebmc_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME)

        self.cleanup_default_generated_files()

    @util.log_test
    def subtest_config_generate_keys(self):

        self.cleanup_default_generated_files()

        # input for interactive prompts - expanding for readability
        stdin = [
            CONFIG_FILENAME,
            util.USER_ID,
            util.TENANT_ID,
            REGION,
            'Y',            # generate new keys
            TEMP_DIR,       # key location
            '',             # use default key name
            PASSPHRASE,
            PASSPHRASE,     # confirm passphrase
            'Y'             # write passphrase to config
        ]

        result = self.invoke(
            ['setup', 'config'], input='\n'.join(stdin))

        print('Output: {}'.format(str(result.output)))

        assert 'Config written to' in result.output, 'Config generation script should run until completion'

        test_config = config.from_file(file_location=CONFIG_FILENAME, profile_name='DEFAULT')
        config.validate_config(test_config)

        print('Config: {}'.format(str(test_config)))

        assert test_config['user'] == util.USER_ID
        assert test_config['tenancy'] == util.TENANT_ID
        assert test_config['region'] == REGION
        assert test_config['pass_phrase'] == PASSPHRASE

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key w/ passphrase
        assert oraclebmc_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME, PASSPHRASE)

        # clean up config and keys
        self.cleanup_default_generated_files()

    @util.log_test
    def subtest_config_existing_keys(self):

        self.cleanup_default_generated_files()

        # generate keys
        keys_stdin = [
            PASSPHRASE,  # passphrase
            PASSPHRASE   # confirm passphrase
        ]
        self.invoke(
            ['setup', 'keys', '--output-dir', TEMP_DIR, '--overwrite'], input='\n'.join(keys_stdin))

        # input for interactive prompts - expanding for readability
        stdin = [
            CONFIG_FILENAME,
            util.USER_ID,
            util.TENANT_ID,
            REGION,
            'n',                    # use existing keys
            PRIVATE_KEY_FILENAME,   # private key location
            PASSPHRASE,             # passphrase
            'Y'                     # write passphrase to config
        ]

        result = self.invoke(
            ['setup', 'config'], input='\n'.join(stdin))

        print('Output: {}'.format(str(result.output)))

        assert 'Config written to' in result.output, 'Config generation script should run until completion'

        test_config = config.from_file(file_location=CONFIG_FILENAME, profile_name='DEFAULT')
        config.validate_config(test_config)

        print('Config: {}'.format(str(test_config)))

        assert test_config['user'] == util.USER_ID
        assert test_config['tenancy'] == util.TENANT_ID
        assert test_config['region'] == REGION
        assert test_config['pass_phrase'] == PASSPHRASE

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key w/ passphrase
        assert oraclebmc_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME, PASSPHRASE)

        # clean up config and keys
        self.cleanup_default_generated_files()

    @util.log_test
    def subtest_config_existing_keys_expands_user_directory(self):

        self.cleanup_default_generated_files()

        # generate keys
        keys_stdin = [
            PASSPHRASE,  # passphrase
            PASSPHRASE   # confirm passphrase
        ]
        self.invoke(
            ['setup', 'keys', '--output-dir', TEMP_DIR, '--overwrite'], input='\n'.join(keys_stdin))

        key_file_with_user_directory = os.path.join("~/fakedir/", PRIVATE_KEY_FILENAME)

        # input for interactive prompts - expanding for readability
        stdin = [
            CONFIG_FILENAME,
            util.USER_ID,
            util.TENANT_ID,
            REGION,
            'n',                            # use existing keys
            key_file_with_user_directory,   # private key location (with user dir)
            PRIVATE_KEY_FILENAME,           # private key location (valid)
            PASSPHRASE,                     # passphrase
            'Y'                             # write passphrase to config
        ]

        result = self.invoke(
            ['setup', 'config'], input='\n'.join(stdin))

        print('Output: {}'.format(str(result.output)))

        assert 'Config written to' in result.output, 'Config generation script should run until completion'

        # validate that user directory was expanded in file not found error
        assert 'No file found at: {}'.format(os.path.expanduser(key_file_with_user_directory)) in result.output

        # clean up config and keys
        self.cleanup_default_generated_files()

    def subtest_config_invalid_user_ocid(self):
        self.cleanup_default_generated_files()

        # input for interactive prompts - expanding for readability
        stdin = [
            CONFIG_FILENAME,
            'invalid_user_ocid',
            util.USER_ID,
            util.TENANT_ID,
            REGION,
            'Y',            # generate new keys
            TEMP_DIR,       # key location
            '',             # use default key name
            PASSPHRASE,
            PASSPHRASE,     # confirm passphrase
            'Y'             # write passphrase to config
        ]

        result = self.invoke(
            ['setup', 'config'], input='\n'.join(stdin))

        print('Output: {}'.format(str(result.output)))

        assert 'Invalid OCID format' in result.output

        self.cleanup_default_generated_files()

    def subtest_config_invalid_tenancy_ocid(self):
        self.cleanup_default_generated_files()

        # input for interactive prompts - expanding for readability
        stdin = [
            CONFIG_FILENAME,
            util.USER_ID,
            'invalid_tenancy_ocid',
            util.TENANT_ID,
            REGION,
            'Y',            # generate new keys
            TEMP_DIR,       # key location
            '',             # use default key name
            PASSPHRASE,
            PASSPHRASE,     # confirm passphrase
            'Y'             # write passphrase to config
        ]

        result = self.invoke(
            ['setup', 'config'], input='\n'.join(stdin))

        print('Output: {}'.format(str(result.output)))

        assert 'Invalid OCID format' in result.output

        self.cleanup_default_generated_files()

    def subtest_autocomplete_deny_bash_rc_access(self):
        # fully testing the command would edit the machine's bash_profile / bash_rc
        # this test rejects the prompt to edit the bash_profile but provides a basic smoke test for the command
        result = self.invoke(
            ['setup', 'autocomplete'], input='n')

        assert result.exit_code == 0

        # on windows the command quits with an error message
        if sys.platform == 'win32' or sys.platform == 'cygwin':
            assert 'not currently available on Windows' in result.output
        else:
            assert 'Exiting script. Tab completion not set up.' in result.output

    def cleanup_default_generated_files(self):
        # ensure that keys don't already exists
        if os.path.exists(CONFIG_FILENAME):
            os.remove(CONFIG_FILENAME)

        if os.path.exists(PUBLIC_KEY_FILENAME):
            os.remove(PUBLIC_KEY_FILENAME)

        if os.path.exists(PRIVATE_KEY_FILENAME):
            os.remove(PRIVATE_KEY_FILENAME)

    def validate_public_key_file(self, filename):
        if os.path.isfile(filename):
            with open(filename, 'rb') as f:
                try:
                    serialization.load_pem_public_key(data=f.read(), backend=default_backend())
                    return True
                except ValueError:
                    pass

        return False

    def invoke(self, commands, debug=False, ** args):
        self.validator.register_call(commands)

        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, ** args)


if __name__ == '__main__':
    unittest.main()
