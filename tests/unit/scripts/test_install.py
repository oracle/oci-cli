# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os
import unittest
import subprocess
import re
import shutil

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
RESOURCE_DIR = os.path.join(SCRIPT_DIR, '..', '..', 'resources')


class TestInstall(unittest.TestCase):
    def setUp(self):
        self.base_install_command = ['python', './scripts/install/install.py', '--accept-all-defaults', '--dry-run', '--install-dir', '/tmp/cli-install-dir']
        if hasattr(self, 'cwd'):
            os.chdir(self.cwd)
        else:
            self.cwd = os.getcwd()

    def tearDown(self):
        os.chdir(self.cwd)

    def test_base_install(self):
        print("\ntest_base_install")
        install_command = self.base_install_command[:]
        output = str(subprocess.check_output(install_command).strip())
        print(output)
        self.assertIn("-- Verifying Python version.", output)
        self.assertTrue(re.search("-- Python version (.)* okay.", output))
        self.assertTrue(re.search("-- The executable will be in (.)*bin", output))
        self.assertTrue(re.search("-- The scripts will be in (.)*bin(.)*oci-cli-scripts", output))
        self.assertTrue(re.search("-- The optional packages installed will be (.)*'(.)*'", output))
        self.assertTrue(re.search("-- dry-run: Skipping CLI install, cmd=", output))
        self.assertTrue(re.search("-- dry-run: Skipping CLI install, cmd=(.)*pip(.)*install(.)*oci_cli(.)*'", output))
        self.assertIn("dry-run: update_path_and_enable_tab_completion=False", output)
        self.assertIn("dry-run: rc_file_path=None", output)

    def test_install_version(self):
        print("\ntest_install_version")
        install_command = self.base_install_command[:]
        install_command.extend(['--oci-cli-version', '2.5.11+preview.1'])
        output = str(subprocess.check_output(install_command).strip())
        print(output)
        self.assertTrue(re.search("-- dry-run: Skipping CLI install, cmd=(.)*pip(.)*install(.)*oci_cli==2.5.11\+preview.1", output))  # noqa: W605

    def test_install_exec_dir(self):
        print("\ntest_install_exec_dir")
        install_command = self.base_install_command[:]
        install_command.extend(['--exec-dir', '/tmp/oci-cli-exec-dir'])
        output = str(subprocess.check_output(install_command).strip())
        print(output)
        self.assertIn("dry-run: exec_dir=/tmp/oci-cli-exec-dir", output)

    def test_install_script_dir(self):
        print("\ntest_install_script_dir")
        install_command = self.base_install_command[:]
        install_command.extend(['--script-dir', '/tmp/oci-cli-script-dir'])
        output = str(subprocess.check_output(install_command).strip())
        print(output)
        self.assertIn("dry-run: script_dir=/tmp/oci-cli-script-dir", output)

    def test_install_update_path_and_enable_tab_completion(self):
        print("\ntest_install_update_path_and_enable_tab_completion")
        install_command = self.base_install_command[:]
        install_command.extend(['--update-path-and-enable-tab-completion'])
        output = str(subprocess.check_output(install_command).strip())
        print(output)
        self.assertIn("dry-run: update_path_and_enable_tab_completion=True", output)

    def test_install_rc_file_path(self):
        print("\ntest_install_rc_file_path")
        install_command = self.base_install_command[:]
        install_command.extend(['--rc-file-path', '/tmp/oci-cli-rc-file'])
        output = str(subprocess.check_output(install_command).strip())
        print(output)
        self.assertIn("dry-run: rc_file_path=/tmp/oci-cli-rc-file", output)

    def test_install_optional_features(self):
        print("\ntest_install_optional_features")
        install_command = self.base_install_command[:]
        install_command.extend(['--optional-features', 'db'])
        output = str(subprocess.check_output(install_command).strip())
        print(output)
        self.assertIn("oci_cli[db]", output)
        self.assertTrue(re.search("-- dry-run: Skipping CLI install, cmd=(.)*pip(.)*install(.)*oci_cli\[db\]", output))  # noqa: W605

    def test_install_help(self):
        print("\ntest_install_help")
        install_command = self.base_install_command[:]
        install_command.extend(['--help'])
        output = str(subprocess.check_output(install_command).strip())
        print(output)
        self.assertIn("usage: install.py [-h]", output)
        install_command = self.base_install_command[:]
        install_command.extend(['-h'])
        output = str(subprocess.check_output(install_command).strip())
        print(output)
        self.assertIn("usage: install.py [-h]", output)

    def test_install_full_install(self):
        print("\ntest_install_full_install")
        shutil.copy('./scripts/install/install.py', './tests/resources/install')
        os.chdir('./tests/resources/install')
        install_command = ['python', './install.py', '--accept-all-defaults', '--dry-run', '--install-dir', '/tmp/cli-install-dir']
        output = str(subprocess.check_output(install_command).strip())
        print(output)
        self.assertIn("oci_cli-2.5.10", output)
        self.assertTrue(re.search("-- dry-run: Skipping CLI install, cmd=(.)*pip(.)*install(.)*oci_cli-2.5.10\+(.)*py2.py3-none-any.whl", output))  # noqa: W605
        self.assertTrue(re.search("-- Installing oci_cli-2.5.10\+(.)*-py2.py3-none-any.whl from local resources.", output))  # noqa: W605
        os.chdir(self.cwd)

    def test_install_full_install_version(self):
        print("\ntest_install_full_install_version")
        shutil.copy('./scripts/install/install.py', './tests/resources/install')
        os.chdir('./tests/resources/install')
        install_command = ['python', './install.py', '--accept-all-defaults', '--dry-run', '--install-dir', '/tmp/cli-install-dir']
        install_command.extend(['--oci-cli-version', '2.5.10'])
        output = str(subprocess.check_output(install_command).strip())
        print(output)
        self.assertIn("oci_cli-2.5.10", output)
        self.assertTrue(re.search("-- dry-run: Skipping CLI install, cmd=(.)*pip(.)*install(.)*oci_cli-2.5.10\+(.)*py2.py3-none-any.whl", output))  # noqa: W605
        self.assertTrue(re.search("-- Installing oci_cli-2.5.10\+(.)*-py2.py3-none-any.whl from local resources.", output))  # noqa: W605

        install_command = ['python', './install.py', '--accept-all-defaults', '--dry-run', '--install-dir', '/tmp/cli-install-dir']
        install_command.extend(['--oci-cli-version', '2.5.10+1870'])
        output = str(subprocess.check_output(install_command).strip())
        print(output)
        self.assertIn("oci_cli-2.5.10", output)
        self.assertTrue(re.search("-- dry-run: Skipping CLI install, cmd=(.)*pip(.)*install(.)*oci_cli-2.5.10\+1870-py2.py3-none-any.whl", output))  # noqa: W605
        self.assertTrue(re.search("-- Installing oci_cli-2.5.10\+1870-py2.py3-none-any.whl from local resources.", output))   # noqa: W605
        os.chdir(self.cwd)
