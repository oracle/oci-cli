# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci_cli
import unittest
from . import util
from oci.regions import REGIONS
from oci_cli import config

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

from io import StringIO
import os
import os.path
import six
import stat
import subprocess
import sys
import tempfile

TEMP_DIR = os.path.join('tests', 'temp')

CONFIG_FILENAME = os.path.join(TEMP_DIR, 'config')
REGION = 'us-phoenix-1'
PASSPHRASE = 'passphrase'
PASSPHRASE_FILE = os.path.join('tests', 'resources', 'test_passphrase_file.txt')

PUBLIC_KEY_FILENAME = os.path.join(TEMP_DIR, 'oci_api_key_public.pem')
PRIVATE_KEY_FILENAME = os.path.join(TEMP_DIR, 'oci_api_key.pem')


class TestSetup(unittest.TestCase):

    @util.log_test
    def test_all_operations(self):
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
        self.subtest_config_region_with_valid_index()
        self.subtest_config_invalid_region_by_index_or_name_with_not_continue()
        self.subtest_config_invalid_region_by_index_or_name_with_continue()

        self.subtest_autocomplete_deny_bash_rc_access()

        self.subtest_repair_file_permissions()

        self.subtest_oci_cli_rc_file()

    @util.log_test
    def subtest_keys(self):
        stdin = [
            PASSPHRASE,     # passphrase
            PASSPHRASE      # confirm passphrase
        ]

        self.invoke(['setup', 'keys', '--output-dir', TEMP_DIR, '--overwrite'], input='\n'.join(stdin))

        assert os.path.isfile(PUBLIC_KEY_FILENAME), 'oci setup keys should generate private key file'
        assert os.path.isfile(PRIVATE_KEY_FILENAME), 'oci setup keys should generate public key file'

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key
        assert oci_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME, PASSPHRASE)

        assert self.validate_file_permissions(PRIVATE_KEY_FILENAME)
        assert self.validate_file_permissions(PUBLIC_KEY_FILENAME)

        self.cleanup_default_generated_files()

    @util.log_test
    def subtest_keys_with_passphrase_option(self):

        self.invoke(
            ['setup', 'keys', '--output-dir', TEMP_DIR, '--overwrite', '--passphrase', PASSPHRASE])

        assert os.path.isfile(PUBLIC_KEY_FILENAME), 'oci setup keys should generate public key file'
        assert os.path.isfile(PRIVATE_KEY_FILENAME), 'oci setup keys should generate private key file'

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key
        assert oci_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME, PASSPHRASE)

        self.cleanup_default_generated_files()

    @util.log_test
    def subtest_keys_with_passphrase_file_option(self):

        self.invoke(
            ['setup', 'keys', '--output-dir', TEMP_DIR, '--overwrite', '--passphrase-file', PASSPHRASE_FILE])

        assert os.path.isfile(PUBLIC_KEY_FILENAME), 'oci setup keys should generate public key file'
        assert os.path.isfile(PRIVATE_KEY_FILENAME), 'oci setup keys should generate private key file'

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key
        assert oci_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME, PASSPHRASE)

        self.cleanup_default_generated_files()

    @util.log_test
    def subtest_keys_with_passphrase_file_option_from_stdin(self):

        self.invoke(
            ['setup', 'keys', '--output-dir', TEMP_DIR, '--overwrite', '--passphrase-file', '-'], input=PASSPHRASE)

        assert os.path.isfile(PUBLIC_KEY_FILENAME), 'oci setup keys should generate public key file'
        assert os.path.isfile(PRIVATE_KEY_FILENAME), 'oci setup keys should generate private key file'

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key
        assert oci_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME, PASSPHRASE)

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

        assert os.path.isfile(PUBLIC_KEY_FILENAME), 'oci setup keys should generate private key file'
        assert os.path.isfile(PRIVATE_KEY_FILENAME), 'oci setup keys should generate public key file'

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key
        assert oci_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME)

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
        self.validate_config(test_config)

        print('Config: {}'.format(str(test_config)))

        assert test_config['user'] == util.USER_ID
        assert test_config['tenancy'] == util.TENANT_ID
        assert test_config['region'] == REGION
        assert test_config['pass_phrase'] == PASSPHRASE

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key w/ passphrase
        assert oci_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME, PASSPHRASE)

        assert self.validate_file_permissions(CONFIG_FILENAME)

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
        self.validate_config(test_config)

        print('Config: {}'.format(str(test_config)))

        assert test_config['user'] == util.USER_ID
        assert test_config['tenancy'] == util.TENANT_ID
        assert test_config['region'] == REGION
        assert test_config['pass_phrase'] == PASSPHRASE

        # validate public key
        assert self.validate_public_key_file(PUBLIC_KEY_FILENAME)

        # validate private key w/ passphrase
        assert oci_cli.cli_setup.validate_private_key_passphrase(PRIVATE_KEY_FILENAME, PASSPHRASE)

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

    @util.log_test
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

    @util.log_test
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

    @util.log_test
    def subtest_config_region_with_valid_index(self):

        self.cleanup_default_generated_files()

        valid_index_of_region = str(sorted(REGIONS).index(REGION) + 1)

        # input for interactive prompts - expanding for readability
        stdin = [
            CONFIG_FILENAME,
            util.USER_ID,
            util.TENANT_ID,
            valid_index_of_region,
            'Y',  # generate new keys
            TEMP_DIR,  # key location
            '',  # use default key name
            PASSPHRASE,
            PASSPHRASE,  # confirm passphrase
            'Y'  # write passphrase to config
        ]

        result = self.invoke(
            ['setup', 'config'], input='\n'.join(stdin))

        assert '{}: {}'.format(valid_index_of_region, REGION) in result.output, 'Region list should be correctly formatted'

        test_config = config.from_file(file_location=CONFIG_FILENAME, profile_name='DEFAULT')
        self.validate_config(test_config)

        assert test_config['region'] == REGION

        # clean up config and keys
        self.cleanup_default_generated_files()

    @util.log_test
    def subtest_config_invalid_region_by_index_or_name_with_not_continue(self):

        self.cleanup_default_generated_files()

        for invalid_region in ['-1', '0', '9999', str(len(REGIONS) + 1), 'aaa']:

            # input for interactive prompts - expanding for readability
            stdin = [
                CONFIG_FILENAME,
                util.USER_ID,
                util.TENANT_ID,
                invalid_region,
                'N',  # re-enter region
                REGION,
                'Y',  # generate new keys
                TEMP_DIR,  # key location
                '',  # use default key name
                PASSPHRASE,
                PASSPHRASE,  # confirm passphrase
                'Y'  # write passphrase to config
            ]

            result = self.invoke(
                ['setup', 'config'], input='\n'.join(stdin))

            assert 'Unrecognized region: {}'.format(invalid_region) in result.output, 'An expected hit should be given'
            assert "Continue with unrecognized region? (Enter 'n' to re-enter region) [y/N]:" in result.output, 'A continue choice should be given'

            test_config = config.from_file(file_location=CONFIG_FILENAME, profile_name='DEFAULT')
            self.validate_config(test_config)

            assert test_config['region'] == REGION

            # clean up config and keys
            self.cleanup_default_generated_files()

    @util.log_test
    def subtest_config_invalid_region_by_index_or_name_with_continue(self):

        self.cleanup_default_generated_files()

        for invalid_region in ['-1', '0', '9999', str(len(REGIONS) + 1), 'aaa']:

            # input for interactive prompts - expanding for readability
            stdin = [
                CONFIG_FILENAME,
                util.USER_ID,
                util.TENANT_ID,
                invalid_region,
                'y',  # continue with unrecognized region
                'Y',  # generate new keys
                TEMP_DIR,  # key location
                '',  # use default key name
                PASSPHRASE,
                PASSPHRASE,  # confirm passphrase
                'Y'  # write passphrase to config
            ]

            result = self.invoke(
                ['setup', 'config'], input='\n'.join(stdin))

            assert 'Unrecognized region: {}'.format(invalid_region) in result.output, 'An expected hit should be given'
            assert "Continue with unrecognized region? (Enter 'n' to re-enter region) [y/N]:" in result.output, 'A continue choice should be given'

            test_config = config.from_file(file_location=CONFIG_FILENAME, profile_name='DEFAULT')
            self.validate_config(test_config)

            assert test_config['region'] == invalid_region

            # clean up config and keys
            self.cleanup_default_generated_files()

    @util.log_test
    def subtest_autocomplete_deny_bash_rc_access(self):
        if oci_cli.cli_util.is_windows() and six.PY2:
            print(
                """
                Skipping subtest_autocomplete_deny_bash_rc_access on Windows without Python 3 as the CliRunner click offers for testing seems to use a StringIO
                to back stdout, which throws an error when sys.stdout.encoding is called since there is no encoding attribute on a StringIO.

                Running manually on Windows with and without Python 3 both work, just this case breaks.
                """
            )
            return

        # fully testing the command would edit the machine's bash_profile / bash_rc
        # this test rejects the prompt to edit the bash_profile but provides a basic smoke test for the command
        result = self.invoke(
            ['setup', 'autocomplete'], input='n')

        assert result.exit_code == 0

        # on windows the command quits with an error message
        if sys.platform == 'cygwin':
            assert 'Tab completion only available on Windows when using Powershell' in result.output
        else:
            assert 'Exiting script. Tab completion not set up.' in result.output

    @util.log_test
    def subtest_repair_file_permissions(self):
        try:
            # for this test we need to make sure the warning is NOT suppressed, but set it back to current setting at the end
            original_suppress_warning_value = os.environ.get('OCI_CLI_SUPPRESS_FILE_PERMISSIONS_WARNING')
            os.environ['OCI_CLI_SUPPRESS_FILE_PERMISSIONS_WARNING'] = 'False'

            # capture stdout / stderr so we can validate warnings
            if oci_cli.cli_util.is_windows():
                with util.capture() as out:
                    # create a temporary file and set some unnecessary permissions
                    tmp = tempfile.NamedTemporaryFile()
                    subprocess.check_output('icacls "{path}" /grant Everyone:F'.format(path=tmp.name), stderr=subprocess.STDOUT)

                    # warning should be emitted because permissions are too loose
                    oci_cli.cli_util.FilePermissionChecker.warn_on_invalid_file_permissions(tmp.name)
                    assert 'WARNING' in out[1].getvalue()

                    # reset captured stderr
                    out[1] = StringIO()

                    result = self.invoke(
                        ['setup', 'repair-file-permissions', '--file', tmp.name]
                    )

                    assert result.exit_code == 0

                    # no warning should be emitted because we repaired the permissions
                    oci_cli.cli_util.FilePermissionChecker.warn_on_invalid_file_permissions(tmp.name)
                    assert 'WARNING' not in out[1].getvalue()
            else:
                with util.capture() as out:
                    # create a temporary file and set some unnecessary permissions
                    tmp = tempfile.NamedTemporaryFile()
                    os.chmod(tmp.name, 509)  # octal 775

                    # warning should be emitted because permissions are too loose
                    oci_cli.cli_util.FilePermissionChecker.warn_on_invalid_file_permissions(tmp.name)
                    assert 'WARNING' in out[1].getvalue()

                    # reset captured stderr
                    out[1] = StringIO()

                    result = self.invoke(
                        ['setup', 'repair-file-permissions', '--file', tmp.name]
                    )

                    assert result.exit_code == 0
                    assert oct(stat.S_IMODE(os.lstat(tmp.name).st_mode)) == oct(384)  # 600

                    # no warning should be emitted because we repaired the permissions
                    oci_cli.cli_util.FilePermissionChecker.warn_on_invalid_file_permissions(tmp.name)
                    assert 'WARNING' not in out[1].getvalue()

                with util.capture() as out:
                    # validate that 400 file permissions are accepted as well
                    os.chmod(tmp.name, 256)  # octal 400
                    oci_cli.cli_util.FilePermissionChecker.warn_on_invalid_file_permissions(tmp.name)
                    assert 'WARNING' not in out[1].getvalue()
        finally:
            if original_suppress_warning_value is None:
                del os.environ['OCI_CLI_SUPPRESS_FILE_PERMISSIONS_WARNING']
            else:
                os.environ['OCI_CLI_SUPPRESS_FILE_PERMISSIONS_WARNING'] = original_suppress_warning_value

    @util.log_test
    def subtest_oci_cli_rc_file(self):
        result = self.invoke(['setup', 'oci-cli-rc', '--file', CONFIG_FILENAME])
        assert 'Predefined queries written under section {}'.format(oci_cli.cli_constants.CLI_RC_CANNED_QUERIES_SECTION_NAME) in result.output
        assert 'Command aliases written under section {}'.format(oci_cli.cli_constants.CLI_RC_COMMAND_ALIASES_SECTION_NAME) in result.output
        assert 'Parameter aliases written under section {}'.format(oci_cli.cli_constants.CLI_RC_PARAM_ALIASES_SECTION_NAME) in result.output

        with open(CONFIG_FILENAME, 'rb') as f:
            contents = f.read().decode()

        assert oci_cli.cli_setup.default_canned_queries in contents
        assert oci_cli.cli_setup.default_command_aliases in contents
        assert oci_cli.cli_setup.default_param_aliases in contents

        result = self.invoke(['setup', 'oci-cli-rc', '--file', CONFIG_FILENAME])
        assert 'Predefined queries will not be written as the specified file already contains a section for these queries' in result.output
        assert 'Command aliases will not be written as the specified file already contains a section for command aliases' in result.output
        assert 'Parameter aliases will not be written as the specified file already contains a section for parameter aliases' in result.output

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

    def validate_file_permissions(self, filename):
        with util.capture() as out:
            oci_cli.cli_util.FilePermissionChecker.warn_on_invalid_file_permissions(filename)
            return 'WARNING' not in out

    def validate_config(self, input_config):
        config.validate_config(input_config)
        assert os.path.isabs(input_config['key_file'])

    def invoke(self, commands, debug=False, ** args):
        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, ** args)


if __name__ == '__main__':
    unittest.main()
