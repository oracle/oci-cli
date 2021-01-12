# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestOsManagement(unittest.TestCase):
    def setUp(self):
        pass

    # test managed-instance attach-child, attach-parent, detach-child, detach-parent
    def test_attach_software_source(self):

        result = util.invoke_command(['os-management', 'managed-instance', 'attach-child'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        assert 'software-source-id' in result.output
        result = util.invoke_command(['os-management', 'managed-instance', 'attach-parent'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        assert 'software-source-id' in result.output
        result = util.invoke_command(['os-management', 'managed-instance', 'detach-child'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        assert 'software-source-id' in result.output
        result = util.invoke_command(['os-management', 'managed-instance', 'detach-parent'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        assert 'software-source-id' in result.output

    # test managed-instance install-package, install-update, install-all-updates, remove-package
    def test_install_remove(self):
        result = util.invoke_command(['os-management', 'managed-instance', 'install-package'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        assert 'package-name' in result.output
        result = util.invoke_command(['os-management', 'managed-instance', 'install-update'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        assert 'package-name' in result.output
        result = util.invoke_command(['os-management', 'managed-instance', 'install-all-updates'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        result = util.invoke_command(['os-management', 'managed-instance', 'remove-package'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        assert 'package-name' in result.output

    # test managed-instance list-available-packages, list-available-updates, list-installed-packagess, list-available-software-sourcesx
    def test_managed_instance_list_commands(self):
        result = util.invoke_command(['os-management', 'managed-instance', 'list-available-packages'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        result = util.invoke_command(['os-management', 'managed-instance', 'list-available-updates'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        result = util.invoke_command(['os-management', 'managed-instance', 'list-installed-packages'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        result = util.invoke_command(['os-management', 'managed-instance', 'list-available-software-sources'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output

        result = util.invoke_command(['os-management', 'managed-instance', 'install-all-windows-updates'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        result = util.invoke_command(['os-management', 'managed-instance', 'install-windows-update'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        result = util.invoke_command(['os-management', 'managed-instance', 'list-available-windows-updates'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output
        result = util.invoke_command(['os-management', 'managed-instance', 'list-installed-windows-updates'])
        assert 'Error: Missing option(s)' in result.output
        assert 'managed-instance-id' in result.output

    # test scheduled job commands run-now, skip-next-execution
    def test_scheduled_job_commands(self):
        result = util.invoke_command(['os-management', 'scheduled-job', 'run-now'])
        assert 'Error: Missing option(s)' in result.output
        assert 'scheduled-job-id' in result.output
        result = util.invoke_command(['os-management', 'scheduled-job', 'skip-next-execution'])
        assert 'Error: Missing option(s)' in result.output
        assert 'scheduled-job-id' in result.output

    # test software-source commands get-package, list-packages, add-packages, remove-packages
    def test_software_source_commands(self):
        result = util.invoke_command(['os-management', 'software-source', 'get-package'])
        assert 'Error: Missing option(s)' in result.output
        assert 'software-source-id' in result.output
        assert 'package-name' in result.output
        result = util.invoke_command(['os-management', 'software-source', 'list-packages'])
        assert 'Error: Missing option(s)' in result.output
        assert 'software-source-id' in result.output
        result = util.invoke_command(['os-management', 'software-source', 'add-packages'])
        assert 'Error: Missing option(s)' in result.output
        assert 'software-source-id' in result.output
        assert 'package-names' in result.output
        result = util.invoke_command(['os-management', 'software-source', 'remove-packages'])
        assert 'Error: Missing option(s)' in result.output
        assert 'software-source-id' in result.output
        assert 'package-names' in result.output

    # test work-request commands
    def test_work_request_commands(self):
        result = util.invoke_command(['os-management', 'work-request', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert 'compartment-id' in result.output
