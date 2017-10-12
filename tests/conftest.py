# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from click.testing import CliRunner
import oci
import os
import pytest
import random


def pytest_addoption(parser):
    parser.addoption("--fast", action="store_true", default=False, help="Skip slow tests, as marked with the @slow annotation.")
    parser.addoption("--enable-long-running", action="store_true", default=False, help="Enables tests marked with the @enable_long_running annotation")
    parser.addoption("--config-profile", action="store", help="profile to use from the config file", default=oci.config.DEFAULT_PROFILE)


@pytest.fixture(scope='session')
def malformed_config_file(config):
    # generate malformed config from real config
    sections = {
        'MISSING_USER': 'user',
        'MISSING_FINGERPRINT': 'fingerprint',
        'MISSING_KEY': 'key_file',
        'MISSING_TENANCY': 'tenancy',
        'MISSING_REGION': 'region'
    }

    malformed_config_file_path = os.path.join(get_resource_directory(), 'malformed_config')
    with open(malformed_config_file_path, 'w+') as f:
        for key in sections:
            f.write('\n\n')
            f.write('[{}]\n'.format(key))
            field_to_skip = sections[key]
            for valid_config_key in config:
                if valid_config_key != field_to_skip:
                    f.write('{} = {}\n'.format(valid_config_key, config[valid_config_key]))

        # write SPECIFY BAD ENDPOINT SECTION
        f.write('[SPECIFY_BAD_ENDPOINT]\n')
        for valid_config_key in config:
            f.write('{} = {}\n'.format(valid_config_key, config[valid_config_key]))
        f.write('endpoint = https://notaservice.us-phoenix-1.oraclecloud.com')

    yield malformed_config_file_path

    os.remove(malformed_config_file_path)


@pytest.fixture(scope='session')
def config_file():
    return os.environ['OCI_CLI_CONFIG_FILE']


@pytest.fixture(scope='session')
def config_profile(request):
    return request.config.getoption("--config-profile")


@pytest.fixture(scope='session')
def config(config_file, config_profile):
    config = oci.config.from_file(file_location=config_file, profile_name=config_profile)
    pass_phrase = os.environ.get('PYTHON_CLI_ADMIN_PASS_PHRASE')
    if pass_phrase:
        config['pass_phrase'] = pass_phrase
    return config


@pytest.fixture(scope="session")
def runner():
    return CliRunner()


@pytest.fixture(scope='session')
def test_id():
    return str(random.randint(0, 1000000))


@pytest.fixture(scope='session')
def object_storage_client(config):
    return oci.object_storage.ObjectStorageClient(config)


@pytest.fixture(scope='session')
def network_client(config):
    return oci.core.VirtualNetworkClient(config)


@pytest.fixture(scope='session')
def compute_client(config):
    return oci.core.ComputeClient(config)


def get_resource_directory():
    """Get the absolute path to the test resources directory.
    File is located based on the relative location of this file (util.py).
    """
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, "resources")


def get_resource_path(file_name):
    return os.path.join(get_resource_directory(), file_name)
