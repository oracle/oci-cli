# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from click.testing import CliRunner
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from oci_cli import cli_constants, cli_util, cli_setup, dynamic_loader, final_command_processor
from oci import object_storage, core, file_storage, identity, dns

import click
import datetime
import logging
import oci
import os
import os.path
import pytest
import random
import time
import configparser
import sys

from inspect import getsourcefile
from os.path import abspath

this_file_path = abspath(getsourcefile(lambda: 0))
python_cli_root_dir = this_file_path[:-20]
sys.path.append(python_cli_root_dir)
from tests import tag_data_container     # noqa: E402
from tests import test_config_container  # noqa: E402


WAIT_INTERVAL_SECONDS = 30 if test_config_container.vcr_mode != 'none' else 0

# docs on VCR log levels: http://vcrpy.readthedocs.io/en/latest/debugging.html
logging.basicConfig()
vcr_log = logging.getLogger("vcr")
vcr_log.setLevel(logging.INFO)

if not os.path.exists(os.path.join('tests', 'temp')):
    os.makedirs(os.path.join('tests', 'temp'))

dynamic_loader.load_all_services()
final_command_processor.process()


def pytest_addoption(parser):
    add_test_option(parser, "--fast", "store_true", False, "Skip slow tests, as marked with the @slow annotation.")
    add_test_option(parser, "--enable-long-running", "store_true", False, "Enables tests marked with the @enable_long_running annotation")
    add_test_option(parser, "--config-profile", "store", oci.config.DEFAULT_PROFILE, "profile to use from the config file")
    add_test_option(parser, "--vcr-record-mode", "store", 'once', "Record mode option for VCRpy library.")
    add_test_option(parser, "--run-recordable-tests-only", "store", False, "Skip tests where we don't want to record their output.")
    add_test_option(parser, "--instance-principals", "store_true", False, "Enables tests for instance principals")
    add_test_option(parser, "--service", "store", "all", "Name of the service for which you want to run test")


def add_test_option(parser, option, action, default, help):
    try:
        parser.addoption(option, action=action, default=default, help=help)
    except ValueError as ve:
        # ValueError: option names {'--fast'} already added
        if 'already added' in str(ve):
            pass
        else:
            raise ve


def pytest_configure(config):
    test_config_container.vcr_mode = config.getoption("--vcr-record-mode")


@pytest.fixture(scope="session", autouse=True)
def service(pytestconfig):
    return pytestconfig.getoption("service")


@pytest.fixture(scope='session', autouse=True)
def move_cli_config_rc_file():
    expanded_rc_location = os.path.expandvars(os.path.expanduser(cli_constants.CLI_RC_DEFAULT_LOCATION))
    expanded_rc_fallback_location = os.path.expandvars(os.path.expanduser(cli_constants.CLI_RC_FALLBACK_LOCATION))

    moved_rc_file = False
    moved_rc_fallback_file = False

    if os.path.exists(expanded_rc_location):
        os.rename(expanded_rc_location, '{}.moved'.format(expanded_rc_location))
        print('Moved: {}'.format(expanded_rc_location))
        moved_rc_file = True

    if os.path.exists(expanded_rc_fallback_location):
        os.rename(expanded_rc_fallback_location, '{}.moved'.format(expanded_rc_fallback_location))
        print('Moved: {}'.format(expanded_rc_fallback_location))
        moved_rc_fallback_file = True

    yield

    if moved_rc_file:
        os.rename('{}.moved'.format(expanded_rc_location), expanded_rc_location)
        print('Moved Back: {}'.format(expanded_rc_location))

    if moved_rc_fallback_file:
        os.rename('{}.moved'.format(expanded_rc_fallback_location), expanded_rc_fallback_location)
        print('Moved Back: {}'.format(expanded_rc_fallback_location))


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

    if os.path.exists(malformed_config_file_path):
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
    # click does not distinguish between stdout and stderr in Result.output so we are wrapping invoke to strip out common stderr warnings
    # this allows the output to be json parseable which many tests expect
    cli_runner = CliRunner()
    old_invoke = cli_runner.invoke

    def invoke(*args, **kwargs):
        result = old_invoke(*args, **kwargs)
        if result.output and cli_util.LIST_NOT_ALL_ITEMS_RETURNED_WARNING in result.output:
            cleaned_output = result.output.replace(cli_util.LIST_NOT_ALL_ITEMS_RETURNED_WARNING, '')
            try:
                new_output_bytes = bytes(cleaned_output, result.runner.charset)
            except TypeError:
                new_output_bytes = cleaned_output
            finally:
                result = click.testing.Result(result.runner, new_output_bytes, result.exit_code, result.exception, result.exc_info)

        return result

    cli_runner.invoke = invoke
    return cli_runner


@pytest.fixture(scope='session')
def test_id(request):
    is_recording_test = request.config.getoption("--run-recordable-tests-only")
    if is_recording_test:
        return '1000000'
    return str(random.randint(0, 1000000))


@pytest.fixture(scope='session')
def test_id_recorded(test_id):
    if test_config_container.using_vcr_with_mock_responses():
        return '1000000'
    else:
        return test_id


@pytest.fixture(scope='session')
def object_storage_client(config):
    return object_storage.ObjectStorageClient(config)


@pytest.fixture(scope='session')
def network_client(config):
    return core.VirtualNetworkClient(config)


@pytest.fixture(scope='session')
def compute_client(config):
    return core.ComputeClient(config)


@pytest.fixture(scope='session')
def filestorage_client(config):
    return file_storage.FileStorageClient(config)


@pytest.fixture(scope='session')
def identity_client(config):
    return identity.IdentityClient(config)


@pytest.fixture(scope='session')
def dns_client(config):
    return dns.DnsClient(config)


@pytest.fixture(scope='session')
def blockstorage_client(config):
    return core.BlockstorageClient(config)


@pytest.fixture(scope='session')
def cli_testing_service_client():
    try:
        from tests.cli_testing_service_client import CLITestingServiceClient
        client = CLITestingServiceClient()

        with test_config_container.create_vcr().use_cassette('generated/create_test_service_session.yml'):
            client.create_session()

        yield client

        with test_config_container.create_vcr().use_cassette('generated/close_test_service_session.yml'):
            client.end_session()
    except ImportError:
        yield None


# Input: config file location
# Output: 1) ConfigParser config object and
#         2) List of sections from config file e.g. ['DEFAULT', 'ADMIN', 'PHX']
def get_config_profiles(config_file):
    expanded_file_location = os.path.expandvars(os.path.expanduser(config_file))
    config = configparser.ConfigParser(interpolation=None)
    if not config.read(expanded_file_location):
        raise IOError("No such file or directory: {}".format(expanded_file_location))
    config_profiles = config.sections()
    # The 'DEFAULT' section is not returned as part of sections() call so we need to add it if present in config object.
    if 'DEFAULT' in config:
        config_profiles.extend(['DEFAULT'])
    return config, config_profiles


# This fixture ensures the file permissions are correct when CLI pytests are run.
# We generally expect users to source test_setup.sh which ensures correct file permissions before running the tests.
# This fixture helps in cases where permissions accidentally get changed again causing errors while running tests.
# The function below fixes the 'key_file' permissions for all profiles in the config file since at this point we do not
# know which profile user will use for a test case.
# There is a corner case where user might give a file path explicitly in the test case. This should be rare and is
# intentionally not taken care of as a trade-off for an elegant solution. This function has an added benefit of
# throwing an early and appropriate 'File not found' error if the config file location is incorrect.
# Input: config_file fixture
# Output: None. It changes the file permissions for 'config' and 'key' files for all profiles in config file.
@pytest.fixture(scope='session', autouse=True)
def fix_config_and_key_file_permissions(config_file):
    cli_util.apply_user_only_access_permissions(os.path.expandvars(os.path.expanduser(config_file)))
    config, config_profiles = get_config_profiles(config_file)
    for config_profile_name in config_profiles:
        config_key_file_path = os.path.expandvars(os.path.expanduser(config[config_profile_name]['key_file']))
        # Below check ensures we do not raise an exception when the key file is not found for a particular profile
        if (os.path.isfile(config_key_file_path)):
            cli_util.apply_user_only_access_permissions(config_key_file_path)


@pytest.fixture(scope='module')
def key_pair_files():
    temp_dir = os.path.join('tests', 'temp')
    private_key = cli_util.generate_key()
    public_key = private_key.public_key()

    public_key_filename = os.path.join(temp_dir, 'key_public.pem')
    private_key_filename = os.path.join(temp_dir, 'key.pem')
    certificate_filename = os.path.join(temp_dir, 'certificate.pem')

    with open(public_key_filename, "wb") as f:
        f.write(cli_util.serialize_key(public_key=public_key))

    with open(private_key_filename, "wb") as f:
        f.write(cli_util.serialize_key(private_key=private_key, passphrase='secret!'))

    # Various details about who we are. For a self-signed certificate the
    # subject and issuer are always the same.
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"WA"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Seattle"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Oracle"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"company.com"),
    ])

    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        public_key
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        # Our certificate will be valid for 10 days
        datetime.datetime.utcnow() + datetime.timedelta(days=10)
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"localhost")]), critical=False).sign(private_key, hashes.SHA256(), default_backend())

    # Write our certificate out to disk.
    with open(certificate_filename, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

    result = [public_key_filename, private_key_filename, certificate_filename]
    yield result

    for filename in result:
        if os.path.isfile(filename):
            os.remove(filename)


@pytest.fixture(scope='module')
def vcn_and_subnets(network_client):
    from tests import util

    with test_config_container.create_vcr().use_cassette('_conftest_fixture_vcn_and_subnets.yml'):
        # create VCN
        vcn_name = util.random_name('cli_lb_test_vcn')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        create_vcn_details = oci.core.models.CreateVcnDetails()
        create_vcn_details.cidr_block = cidr_block
        create_vcn_details.display_name = vcn_name
        create_vcn_details.compartment_id = os.environ['OCI_CLI_COMPARTMENT_ID']
        create_vcn_details.dns_label = vcn_dns_label

        result = network_client.create_vcn(create_vcn_details)
        vcn_ocid = result.data.id
        assert result.status == 200

        oci.wait_until(network_client, network_client.get_vcn(vcn_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300, max_interval_seconds=WAIT_INTERVAL_SECONDS)

        # create subnet in first AD
        subnet_name = util.random_name('cli_lb_test_subnet')
        cidr_block = "10.0.1.0/24"
        subnet_dns_label = util.random_name('subnet', insert_underscore=False)

        create_subnet_details = oci.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = os.environ['OCI_CLI_COMPARTMENT_ID']
        create_subnet_details.availability_domain = util.availability_domain()
        create_subnet_details.display_name = subnet_name
        create_subnet_details.vcn_id = vcn_ocid
        create_subnet_details.cidr_block = cidr_block
        create_subnet_details.dns_label = subnet_dns_label

        result = network_client.create_subnet(create_subnet_details)
        subnet_ocid_1 = result.data.id
        assert result.status == 200

        oci.wait_until(network_client, network_client.get_subnet(subnet_ocid_1), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300, max_interval_seconds=WAIT_INTERVAL_SECONDS)

        # create subnet in second AD
        subnet_name = util.random_name('cli_lb_test_subnet')
        cidr_block = "10.0.0.0/24"
        subnet_dns_label = util.random_name('subnet2', insert_underscore=False)

        create_subnet_details = oci.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = os.environ['OCI_CLI_COMPARTMENT_ID']
        create_subnet_details.availability_domain = util.second_availability_domain()
        create_subnet_details.display_name = subnet_name
        create_subnet_details.vcn_id = vcn_ocid
        create_subnet_details.cidr_block = cidr_block
        create_subnet_details.dns_label = subnet_dns_label

        result = network_client.create_subnet(create_subnet_details)
        subnet_ocid_2 = result.data.id
        assert result.status == 200

        oci.wait_until(network_client, network_client.get_subnet(subnet_ocid_2), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300, max_interval_seconds=WAIT_INTERVAL_SECONDS)

    yield [vcn_ocid, subnet_ocid_1, subnet_ocid_2]

    # For some reason VCR doesn't like that the post-yield stuff here is all in one cassette. Splitting into different cassettes seems to work
    with test_config_container.create_vcr().use_cassette('_conftest_fixture_vcn_and_subnets_delete.yml'):
        # delete VCN and subnets
        network_client.delete_subnet(subnet_ocid_1)

        try:
            oci.wait_until(network_client, network_client.get_subnet(subnet_ocid_1), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600, max_interval_seconds=WAIT_INTERVAL_SECONDS)
        except oci.exceptions.ServiceError as error:
            if not hasattr(error, 'status') or error.status != 404:
                util.print_latest_exception(error)

        network_client.delete_subnet(subnet_ocid_2)

        try:
            oci.wait_until(network_client, network_client.get_subnet(subnet_ocid_2), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600, max_interval_seconds=WAIT_INTERVAL_SECONDS)
        except oci.exceptions.ServiceError as error:
            if not hasattr(error, 'status') or error.status != 404:
                util.print_latest_exception(error)

        network_client.delete_vcn(vcn_ocid)


@pytest.fixture(scope='session')
def tag_namespace_and_tags(identity_client, test_id_recorded):
    with test_config_container.create_vcr().use_cassette('_conftest_fixture_tag_namespace_and_tags.yml',
                                                         match_on=['method', 'scheme', 'host', 'port', 'vcr_query_matcher']):
        if not os.environ.get('OCI_CLI_TAG_NAMESPACE_ID'):
            tag_namespace_name = 'cli_tag_ns_{}'.format(test_id_recorded)
            create_tag_namespace_response = identity_client.create_tag_namespace(
                oci.identity.models.CreateTagNamespaceDetails(
                    compartment_id=os.environ['OCI_CLI_COMPARTMENT_ID'],
                    name=tag_namespace_name,
                    description='Python SDK integ test namespace'
                )
            )

            tag_namespace = create_tag_namespace_response.data
        else:
            print('Reusing tag namespace: {}'.format(os.environ.get('OCI_CLI_TAG_NAMESPACE_ID')))
            get_tag_namespace_response = identity_client.get_tag_namespace(os.environ.get('OCI_CLI_TAG_NAMESPACE_ID'))

            if get_tag_namespace_response.data.is_retired:
                update_tag_namespace_response = identity_client.update_tag_namespace(
                    get_tag_namespace_response.data.id,
                    oci.identity.models.UpdateTagNamespaceDetails(is_retired=False)
                )
                tag_namespace = update_tag_namespace_response.data
            else:
                tag_namespace = get_tag_namespace_response.data

        tags = []
        if not os.environ.get('OCI_CLI_TAG_ONE_NAME'):
            tag_one_name = 'cli_tag_{}'.format(test_id_recorded)
            create_tag_response = identity_client.create_tag(
                tag_namespace.id,
                oci.identity.models.CreateTagDetails(name=tag_one_name, description='CLI integration test tag')
            )
            tags.append(create_tag_response.data)
        else:
            print('Reusing tag: {}'.format(os.environ.get('OCI_CLI_TAG_ONE_NAME')))
            tags.append(get_and_reactivate_tag(identity_client, tag_namespace, os.environ.get('OCI_CLI_TAG_ONE_NAME')))

        if not os.environ.get('OCI_CLI_TAG_TWO_NAME'):
            tag_two_name = 'cli_tag2_{}'.format(test_id_recorded)
            create_tag_response = identity_client.create_tag(
                tag_namespace.id,
                oci.identity.models.CreateTagDetails(name=tag_two_name, description='CLI integration test tag')
            )
            tags.append(create_tag_response.data)
        else:
            print('Reusing tag: {}'.format(os.environ.get('OCI_CLI_TAG_TWO_NAME')))
            tags.append(get_and_reactivate_tag(identity_client, tag_namespace, os.environ.get('OCI_CLI_TAG_TWO_NAME')))

        # Avoid eventual consistency issue where we try and use tags we just created and get a 404 (though it
        # would succeed on retry)
        time.sleep(10)

        tag_data_container.tag_namespace = tag_namespace
        tag_data_container.tags = tags

    yield {'namespace': tag_namespace, 'tags': tags}

    with test_config_container.create_vcr().use_cassette('_conftest_fixture_tag_namespace_and_tags_retire.yml'):
        # Only retire if we're not reusing a namespace or tags, otherwise on parallel runs we can get conflicts since one run retires a tag that
        # another run expects to not be retired
        if not os.environ.get('OCI_CLI_TAG_NAMESPACE_ID') and not os.environ.get('OCI_CLI_TAG_ONE_NAME') and not os.environ.get('OCI_CLI_TAG_TWO_NAME'):
            for tag in tags:
                identity_client.update_tag(
                    tag.tag_namespace_id,
                    tag.name,
                    oci.identity.models.UpdateTagDetails(is_retired=True)
                )

            update_tag_namespace_response = identity_client.update_tag_namespace(
                tag_namespace.id,
                oci.identity.models.UpdateTagNamespaceDetails(is_retired=True)
            )


def get_and_reactivate_tag(identity_client, tag_namespace, tag_name):
    get_tag_response = identity_client.get_tag(
        tag_namespace.id,
        tag_name
    )

    if get_tag_response.data.is_retired:
        update_tag_response = identity_client.update_tag(
            tag_namespace.id,
            tag_name,
            oci.identity.models.UpdateTagDetails(is_retired=False)
        )

        return update_tag_response.data
    else:
        return get_tag_response.data


def get_resource_directory():
    """Get the absolute path to the test resources directory.
    File is located based on the relative location of this file (util.py).
    """
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(here, "tests", "resources")


def get_resource_path(file_name):
    return os.path.join(get_resource_directory(), file_name)
