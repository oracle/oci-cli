# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
import oci_cli
import pytest
from tests import util
from tests import test_config_container

CASSETTE_LIBRARY_DIR = 'services/os_management/tests/cassettes'
INSTANCE_NAME = 'InstanceForCLITesting'
OLD_PACKAGE = 'ovm-template-config-authentication-3.7-5.el7.noarch'
NEW_PACKAGE = 'ovm-template-config-authentication-3.7-6.el7.noarch'
PACKAGE_NAME = 'ovmd-3.7-14.el7.x86_64'
DEFAULT_WAIT_TIME = 600

util.set_admin_pass_phrase()


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    with test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR).use_cassette('os_management_{name}.yml'.format(name=request.function.__name__)):
        yield


@pytest.fixture(scope='module')
def managed_instance_id_fixture(runner, config_file, config_profile):
    managed_instance_id = None
    params = [
        'os-management', 'managed-instance', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--display-name', INSTANCE_NAME
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    managed_instance = json.loads(result.output)['data'][0]
    managed_instance_id = managed_instance['id']

    return managed_instance_id


def test_managed_instance_group_crud(managed_instance_id_fixture, runner, config_file, config_profile):
    managed_instance_group_id = None
    try:
        # create a managed instance group
        params = [
            'os-management', 'managed-instance-group', 'create',
            '--display-name', util.random_name('managed_instance_group', insert_underscore=False),
            '--description', 'my test group',
            '--compartment-id', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        managed_instance_group_id = json.loads(result.output)['data']['id']

        # list the managed instance groups
        params = [
            'os-management', 'managed-instance-group', 'list',
            '-c', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # attach an instance to the group
        params = [
            'os-management', 'managed-instance-group', 'attach',
            '--managed-instance-group-id', managed_instance_group_id,
            '--managed-instance-id', managed_instance_id_fixture
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # get the managed instance group
        params = [
            'os-management', 'managed-instance-group', 'get',
            '--managed-instance-group-id', managed_instance_group_id
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # update the managed instance group
        params = [
            'os-management', 'managed-instance-group', 'update',
            '--managed-instance-group-id', managed_instance_group_id,
            '--description', 'updated description'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # detach the instance from the group
        params = [
            'os-management', 'managed-instance-group', 'detach',
            '--managed-instance-group-id', managed_instance_group_id,
            '--managed-instance-id', managed_instance_id_fixture
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # move the managed instance group
        params = [
            'os-management', 'managed-instance-group', 'change-compartment',
            '--managed-instance-group-id', managed_instance_group_id,
            '--compartment-id', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

    finally:
        if managed_instance_group_id:
            # delete the managed instance group
            params = [
                'os-management', 'managed-instance-group', 'delete',
                '--managed-instance-group-id', managed_instance_group_id,
                '--force'
            ]

            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)


def test_managed_instance_tests(managed_instance_id_fixture, runner, config_file, config_profile):
    # test managed instance list
    params = [
        'os-management', 'managed-instance', 'list',
        '--compartment-id', util.COMPARTMENT_ID,
        '--display-name', INSTANCE_NAME
    ]

    managed_instance_id = managed_instance_id_fixture
    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    managed_instance = json.loads(result.output)['data'][0]
    managed_instance_id = managed_instance['id']

    # test managed instance get
    params = [
        'os-management', 'managed-instance', 'get',
        '--managed-instance-id', managed_instance_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    managed_instance = json.loads(result.output)['data']
    child_software_sources = managed_instance['child-software-sources']
    parent_software_source_id = managed_instance['parent-software-source']['id']

    # test list installed packages
    params = [
        'os-management', 'managed-instance', 'list-installed-packages',
        '--managed-instance-id', managed_instance_id,
        '--limit', '5'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # test list available software sources
    params = [
        'os-management', 'managed-instance', 'list-available-software-sources',
        '--managed-instance-id', managed_instance_id,
        '--limit', '5'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # test list available packages
    params = [
        'os-management', 'managed-instance', 'list-available-packages',
        '--managed-instance-id', managed_instance_id,
        '--limit', '5'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # test list available updates
    params = [
        'os-management', 'managed-instance', 'list-available-updates',
        '--managed-instance-id', managed_instance_id,
        '--limit', '5'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


def test_managed_instance_install_package(managed_instance_id_fixture, runner, config_file, config_profile):
    # test install package operation
    managed_instance_id = managed_instance_id_fixture

    params = [
        'os-management', 'managed-instance', 'install-package',
        '--managed-instance-id', managed_instance_id,
        '--package-name', OLD_PACKAGE
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    # response = json.loads(result.output)
    # work_request_id = response['opc-work-request-id']
    #    util.wait_until(['os-management', 'work-request', 'get', '--work-request-id', work_request_id], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)

    # sleep(60)


def test_managed_instance_install_update(managed_instance_id_fixture, runner, config_file, config_profile):
    # test update package operations
    managed_instance_id = managed_instance_id_fixture

    params = [
        'os-management', 'managed-instance', 'install-update',
        '--managed-instance-id', managed_instance_id,
        '--package-name', NEW_PACKAGE
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    # response = json.loads(result.output)
    # work_request_id = response['opc-work-request-id']
    #    util.wait_until(['os-management', 'work-request', 'get', '--work-request-id', work_request_id], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)

    # sleep(120)


def test_managed_instance_remove_package(managed_instance_id_fixture, runner, config_file, config_profile):
    # test remove package operation
    managed_instance_id = managed_instance_id_fixture

    params = [
        'os-management', 'managed-instance', 'remove-package',
        '--managed-instance-id', managed_instance_id,
        '--package-name', NEW_PACKAGE
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    # response = json.loads(result.output)
    # work_request_id = response['opc-work-request-id']
    #    util.wait_until(['os-management', 'work-request', 'get', '--work-request-id', work_request_id], 'SUCCEEDED', max_wait_seconds=DEFAULT_WAIT_TIME)

    # sleep(120)


def test_managed_instance_install_all_updates(managed_instance_id_fixture, runner, config_file, config_profile):
    # test update all operations
    managed_instance_id = managed_instance_id_fixture

    params = [
        'os-management', 'managed-instance', 'install-all-updates',
        '--managed-instance-id', managed_instance_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


def test_managed_instance_software_source(managed_instance_id_fixture, runner, config_file, config_profile):
    managed_instance_id = managed_instance_id_fixture

    # get the managed instance
    params = [
        'os-management', 'managed-instance', 'get',
        '--managed-instance-id', managed_instance_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    managed_instance = json.loads(result.output)['data']
    child_software_sources = managed_instance['child-software-sources']
    parent_software_source_id = managed_instance['parent-software-source']['id']

    # test detach of child software source
    child_software_source_id = child_software_sources[0]['id']
    params = [
        'os-management', 'managed-instance', 'detach-child',
        '--managed-instance-id', managed_instance_id,
        '--software-source-id', child_software_source_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # test detach of parent software source
    params = [
        'os-management', 'managed-instance', 'detach-parent',
        '--managed-instance-id', managed_instance_id,
        '--software-source-id', parent_software_source_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # test attach of parent software source
    params = [
        'os-management', 'managed-instance', 'attach-parent',
        '--managed-instance-id', managed_instance_id,
        '--software-source-id', parent_software_source_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # test attach of child software sources
    for child_software_source in child_software_sources:
        child_software_source_id = child_software_source['id']
        params = [
            'os-management', 'managed-instance', 'attach-child',
            '--managed-instance-id', managed_instance_id,
            '--software-source-id', child_software_source_id
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def test_software_source_crud(runner, config_file, config_profile):
    software_source_id = None
    try:
        params = [
            'os-management', 'software-source', 'create',
            '--display-name', util.random_name('software_source', insert_underscore=False),
            '--description', 'test software source',
            '--arch-type', 'X86_64',
            '--compartment-id', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        software_source_id = json.loads(result.output)['data']['id']

        # test get software source
        params = [
            'os-management', 'software-source', 'get',
            '--software-source-id', software_source_id
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # test list software sources
        params = [
            'os-management', 'software-source', 'list',
            '-c', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # test update software source
        params = [
            'os-management', 'software-source', 'update',
            '--software-source-id', software_source_id,
            '--display-name', 'CLITestUpdateName',
            '--description', 'a description'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # test search software sources - search-packages, get-package, list-packages
        params = [
            'os-management', 'software-source', 'search-packages',
            '--package-name', PACKAGE_NAME
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # add packages, remove packages
        packages = str.format("[ '{}', '{}' ]", OLD_PACKAGE, NEW_PACKAGE)
        params = [
            'os-management', 'software-source', 'add-packages',
            '--software-source-id', software_source_id,
            '--package-names', '[ "ovm-template-config-authentication-3.7-5.el7.noarch", "ovm-template-config-authentication-3.7-6.el7.noarch"]'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # list packages
        params = [
            'os-management', 'software-source', 'list-packages',
            '--software-source-id', software_source_id,
            '--display-name', 'ovm'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        software_packages = json.loads(result.output)['data']
        software_package = software_packages[0]
        software_package_name = software_package['name']

        # get package
        params = [
            'os-management', 'software-source', 'get-package',
            '--software-source-id', software_source_id,
            '--package-name', software_package_name
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # remove packages
        params = [
            'os-management', 'software-source', 'remove-packages',
            '--software-source-id', software_source_id,
            '--package-names', '[ "ovm-template-config-authentication-3.7-5.el7.noarch", "ovm-template-config-authentication-3.7-6.el7.noarch"]'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # move the software source
        params = [
            'os-management', 'software-source', 'change-compartment',
            '--software-source-id', software_source_id,
            '--compartment-id', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

    finally:
        if software_source_id:
            params = [
                'os-management', 'software-source', 'delete',
                '--software-source-id', software_source_id,
                '--force'
            ]

            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)


def test_scheduled_job_crud(managed_instance_id_fixture, runner, config_file, config_profile):
    managed_instance_id = managed_instance_id_fixture
    # test scheduled job creation
    scheduled_job_id = None
    try:
        params = [
            'os-management', 'scheduled-job', 'create',
            '--display-name', util.random_name('scheduled_job', insert_underscore=False),
            '--description', 'test scheduled job',
            '--compartment-id', util.COMPARTMENT_ID,
            '--operation-type', 'UPDATEALL',
            '--schedule-type', 'RECURRING',
            '--update-type', 'SECURITY',
            '--interval-value', '2',
            '--interval-type', 'MONTH',
            '--operation-type', 'UPDATEALL',
            '--time-next-execution', '2022-09-15T20:30:00.123Z',
            '--managed-instances', '[ { "id":"ocid1.instance.oc1.phx.anyhqljts3fhncicbtozuo5jgoxfcmkciou7oeocqaxlcu3y743reukuin5a"} ]'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        scheduled_job_id = json.loads(result.output)['data']['id']

        # test get scheduled job
        params = [
            'os-management', 'scheduled-job', 'get',
            '--scheduled-job-id', scheduled_job_id
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # test list scheduled job
        params = [
            'os-management', 'scheduled-job', 'list',
            '--compartment-id', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # test list upcoming scheduled jobs
        params = [
            'os-management', 'scheduled-job', 'list-upcoming',
            '--time-end', '2025-09-15T20:30:00.123000Z',
            '--compartment-id', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # test update scheduled job
        params = [
            'os-management', 'scheduled-job', 'update',
            '--scheduled-job-id', scheduled_job_id,
            '--display-name', 'CLITestUpdateName',
            '--description', 'a new description'
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)
        assert len(json.loads(result.output)['data']) > 0

        # move the scheduled job
        params = [
            'os-management', 'scheduled-job', 'change-compartment',
            '--scheduled-job-id', scheduled_job_id,
            '--compartment-id', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # test scheduled job skip next execution
        params = [
            'os-management', 'scheduled-job', 'skip-next-execution',
            '--scheduled-job-id', scheduled_job_id
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # test scheduled job run now
        params = [
            'os-management', 'scheduled-job', 'run-now',
            '--scheduled-job-id', scheduled_job_id
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

        # move the scheduled job
        params = [
            'os-management', 'scheduled-job', 'change-compartment',
            '--scheduled-job-id', scheduled_job_id,
            '--compartment-id', util.COMPARTMENT_ID
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)

    finally:
        if scheduled_job_id:
            params = [
                'os-management', 'scheduled-job', 'delete',
                '--scheduled-job-id', scheduled_job_id,
                '--force'
            ]

            result = invoke(runner, config_file, config_profile, params)
            util.validate_response(result)


def test_work_requests(managed_instance_id_fixture, runner, config_file, config_profile):
    managed_instance_id = managed_instance_id_fixture

    # test list work requests
    params = [
        'os-management', 'work-request', 'list',
        '--compartment-id', util.COMPARTMENT_ID
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    assert len(json.loads(result.output)['data']) > 0

    work_request = json.loads(result.output)['data'][0]
    work_request_id = work_request['id']

    # test work request get
    params = [
        'os-management', 'work-request', 'get',
        '--work-request-id', work_request_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # test work request list-errors
    params = [
        'os-management', 'work-request', 'list-errors',
        '--work-request-id', work_request_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)

    # test work request list-logs
    params = [
        'os-management', 'work-request', 'list-logs',
        '--work-request-id', work_request_id
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)


def test_erratum(managed_instance_id_fixture, runner, config_file, config_profile):
    managed_instance_id = managed_instance_id_fixture
    # get list available updates
    params = [
        'os-management', 'managed-instance', 'list-available-updates',
        '--managed-instance-id', managed_instance_id,
        '--limit', '5'
    ]

    result = invoke(runner, config_file, config_profile, params)
    util.validate_response(result)
    availableUpdates = json.loads(result.output)['data']
    erratumId = None
    for availableUpdate in availableUpdates:
        errata = availableUpdate['errata']
        if len(errata) > 0:
            for erratum in errata:
                erratumId = erratum['id']

    if erratumId is not None:
        params = [
            'os-management', 'erratum', 'get',
            '--erratum-id', erratumId
        ]

        result = invoke(runner, config_file, config_profile, params)
        util.validate_response(result)


def invoke(runner, config_file, config_profile, params, debug=False, root_params=None, strip_progress_bar=True, strip_multipart_stderr_output=True, ** args):
    root_params = root_params or []
    if debug is True:
        result = runner.invoke(oci_cli.cli, root_params + ['--debug', '--config-file', config_file, '--profile', config_profile] + params, ** args)
    else:
        result = runner.invoke(oci_cli.cli, root_params + ['--config-file', config_file, '--profile', config_profile] + params, ** args)

    return result
