# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# A module which holds test configuration information. This is intended to be a shared space where tests
# can figure out what kind of recording (via VCR) is being done and also so that they can take actions (e.g. waiting)
# in a VCR compatible/friendly way

from . import vcr_mods  # noqa: F401

import json
import logging
import oci
import os
import six
import vcr

from vcr.persisters.filesystem import FilesystemPersister
from . import cli_testing_service_client

vcr_mode = None
vcr_logger = logging.getLogger("vcr")


KEYS_TO_IGNORE_COMPARING_REQUEST_BODIES = [
    # we generate opcRequestId client side in some cases and we don't want the recording to mismatch as a result
    'opcRequestId',
    # responseJson includes the full response from the server
    # when new fields are added to the Python SDK, they will show up as null in this field
    # and thus not pass an equality check.  We don't want tests to fail based on this difference
    'responseJson'
]


def using_vcr_with_mock_responses():
    return vcr_mode != 'all'


def create_vcr(**kwargs):
    location = kwargs.get('cassette_library_dir', 'tests/fixtures/cassettes')
    vcr_to_use = vcr.VCR(
        serializer='yaml',
        cassette_library_dir=location,
        record_mode=vcr_mode
    )

    # by default, only match keys in JSON request bodies
    # if explicitly specified, also match values in JSON request bodies
    match_request_json_object_values = False
    if kwargs.get('match_request_json_object_values'):
        match_request_json_object_values = True

    vcr_to_use.register_matcher('vcr_query_matcher', vcr_query_matcher)
    vcr_to_use.register_matcher('vcr_path_matcher', vcr_path_matcher)
    vcr_to_use.register_matcher('vcr_host_matcher', vcr_host_matcher)
    vcr_to_use.register_matcher('vcr_port_matcher', vcr_port_matcher)
    vcr_to_use.register_matcher('vcr_body_matcher', create_vcr_body_matcher(match_request_json_object_values))

    vcr_to_use.register_persister(CassetteOverwritingPersister)

    if 'match_on' in kwargs:
        vcr_to_use.match_on = kwargs['match_on']
    else:
        vcr_to_use.match_on = [
            'method',
            'scheme',
            'vcr_host_matcher',
            'vcr_port_matcher',
            'vcr_path_matcher',
            'vcr_query_matcher',
            'vcr_body_matcher'
        ]

    return vcr_to_use


# A wrapper around the standard waiter functionality so that if we're mocking responses we don't sleep as we normally
# would (since responses are just going to get returned immediately by VCR anyway)
def do_wait(client, *args, **kwargs):
    if vcr_mode == 'none':
        kwargs['max_interval_seconds'] = 0

    oci.wait_until(client, *args, **kwargs)


class RecordReplay(object):
    def __init__(self, test_namespace='', **vcr_additional_kwargs):
        self.test_namespace = test_namespace
        self.vcr_additional_kwargs = vcr_additional_kwargs

    def __call__(self, func):
        my_vcr = create_vcr(**self.vcr_additional_kwargs)

        def wrapped_call(ctx, *args, **kwargs):
            with my_vcr.use_cassette(self.test_namespace + '_' + func.__name__ + '_cassette.yml'):
                func(ctx, *args, **kwargs)

        return wrapped_call


class RecordReplayWithNoClickContext(object):
    def __init__(self, test_namespace='', **vcr_additional_kwargs):
        self.test_namespace = test_namespace
        self.vcr_additional_kwargs = vcr_additional_kwargs

    def __call__(self, func):
        my_vcr = create_vcr(**self.vcr_additional_kwargs)

        def wrapped_call(*args, **kwargs):
            with my_vcr.use_cassette(self.test_namespace + '_' + func.__name__ + '_cassette.yml'):
                func(*args, **kwargs)

        return wrapped_call


# Below custom query matcher for VCR cassettes is created to allow running VCRs recorded on different tenancies
# with a different test environment setup.
# Query matching for VCR cassettes is based on below criteria:
# Query params having any of {sessionId, compartmentId, tenancyId, userId} are ignored during comparison.
# However, it is taken care that if a query has compartmentId and other query has tenancyId as query parameter,
# they are still compared and determined as non-matching queries.
# In future, if there are more query keys that need to be ignored, they can be added to query_ignore_keys list below.
# Inputs:
# r1 - vcr.Request object corresponding to the http request that was made during the recording of the
# cassette.
# r2 - vcr.Request object corresponding to the http request created while running the test
# Note: 'query' is one of the properties in vcr.Request object. It contains the parsed query string of the http request.
#       It is sorted list of name, value pairs.
# OUTPUT: boolean value indicating if the queries in requests r1 and r2 match.
def vcr_query_matcher(r1, r2):
    if len(r1.query) != len(r2.query):
        return False

    query_ignore_keys = [
        'sessionId',
        'compartmentId',
        'tenancyId',
        'userId'
    ]
    r1_updated_query = list(r1.query)
    r2_updated_query = list(r2.query)

    for t1, t2 in zip(r1.query, r2.query):
        if t1[0] in query_ignore_keys and t1[0] == t2[0]:
            r1_updated_query.remove(t1)
            r2_updated_query.remove(t2)

    return r1_updated_query == r2_updated_query


# Below custom path matcher for VCR cassettes is created to allow running VCRs recorded on different tenancies
# with a different test environment setup.
# Path matching for VCR cassettes is based on below criteria:
# Path params having any of {compartmentId, tenancyId, userId, tagNamespaceId} are ignored during comparison.
# However, it is taken care that if a path has compartmentId and other path has tenancyId as path parameter,
# they are still compared and determined as non-matching paths.
# In future, if there are more OCID strings that need to be ignored, they can be added to path_ignore_strings list
# # below.
# Inputs:
# r1 - vcr.Request object corresponding to the http request that was made during the recording of the
# cassette.
# r2 - vcr.Request object corresponding to the http request created while running the test
# Note: 'path' is one of the properties in vcr.Request object. It contains the path of the http request.
#       For example “/” or “/home.html”
# OUTPUT: boolean value indicating if the paths in requests r1 and r2 match.
def vcr_path_matcher(r1, r2):
    path_ignore_strings = [
        'ocid1.compartment',
        'ocid1.tenancy',
        'ocid1.user',
        'ocid1.tagnamespace'
    ]

    r1_path = r1.path.split('/')
    r2_path = r2.path.split('/')
    if r2_path[-1] == '':
        r2_path.pop()

    r1_updated_path = list(r1_path)
    r2_updated_path = list(r2_path)
    if r2_updated_path[-1] == '':
        r2_updated_path.pop()

    if len(r1_path) != len(r2_path):
        return False

    for s1, s2 in zip(r1_path, r2_path):
        for s in path_ignore_strings:
            if s in s1 and s in s2:
                r1_updated_path.remove(s1)
                r2_updated_path.remove(s2)

    while '' in r1_updated_path:
        r1_updated_path.remove('')
    while '' in r2_updated_path:
        r2_updated_path.remove('')

    return r1_updated_path == r2_updated_path


# Below custom hostname matcher for VCR cassettes is created to allow running VCRs recorded on different tenancies
# with a different test environment setup.
# Hostname matching for VCR cassettes is based on below criteria:
# 1. If both the requests 'path' contain 'SDKTestingService' string, we declare the hostnames match i.e. we ignore the
# hostnames in http requests while doing the hostname matching and treat them as match
# 2. If the requests have the same 'service name' in the hostname string, we consider them as match i.e. we ignore the
# region name, subdomain and domain name part of the endpoint string and only consider the service name part for
# matching.
# Note: The endpoint naming convention has recently changed and we will need to be backward compatible. To support this
#       requirement, VCR Host matcher uses a utility API "get_servicename_from_endpoint" defined below which extracts
#       service name from the old or new style endpoint string passed as argument to it.
# In future, if there are more conditions for hostname or some of the above assumptions change, the matcher needs to
# change as well.
# Inputs:
# r1 - vcr.Request object corresponding to the http request that was made during the recording of the
# cassette.
# r2 - vcr.Request object corresponding to the http request created while running the test
# Note: 'host' and 'path' are properties in vcr.Request object. 'host' property contains the hostname of the http
#       request. For example: kms.us-phoenix-1.oraclecloud.com. 'path' property contains the path of the http request.
#       For example “/” or “/home.html”
# OUTPUT: boolean value indicating if the hostnames in requests r1 and r2 match.
def vcr_host_matcher(r1, r2):
    testing_service_path = '/{path}/'.format(path=cli_testing_service_client.SERVICE_PATH)
    if r1.path.startswith(testing_service_path) and r2.path.startswith(testing_service_path):
        return True
    if get_servicename_from_endpoint(r1.host) == get_servicename_from_endpoint(r2.host):
        return True
    return r1.host == r2.host


# If recordings are done against testing service, then the hostname URL will have port number in it. We allow the port
# number to be different in this case. In all other cases, we match port numbers.
def vcr_port_matcher(r1, r2):
    if 'localhost' in r1.host and 'localhost' in r2.host:
        return True
    return r1.port == r2.port


# New Endpoint format: <region>.<service>.<oci/ocp/ocs>.<oraclecloud/oracleiaas>.com
# Old Endpoint format: <Service Identifier>.<Region ID>.oraclecloud.com OR <Service Identifier>.<AD#>.<Region ID>.<oraclecloud/oracleiaas>.com
# Above info is from below confluence links:
# Old endpoint naming convention: https://confluence.oci.oraclecorp.com/display/PM/OCI+-+Service+Endpoints
# New endpoint naming convention: https://confluence.oci.oraclecorp.com/display/~sumidey/Service+Endpoint+Update
# Input: endpoint - endpoint of a service (string) e.g. kms.us-phoenix-1.oraclecloud.com
# Output: service name string extracted from endpoint e.g. kms
def get_servicename_from_endpoint(endpoint):
    # New endpoints follow <service>.<region>.<oci/ocp/ocs>.<oraclecloud/oracleiaas>.com
    # We can directly compare name of the service by indexing on the first index
    # subdomain = ['.oci.', '.ocp.', '.ocs.']
    # if any(x in endpoint for x in subdomain):
    #     service_name_idx = 1
    # else:
    #     service_name_idx = 0

    return endpoint.split('.')[0]


def create_vcr_body_matcher(match_request_json_object_values):
    def match(r1, r2):
        return vcr_body_matcher(r1, r2, match_request_json_object_values)

    return match


# Custom VCR matcher to check that request bodies are equivalent
# The following conditions are evaluated:
# - if the request body is JSON, confirm that the keys in the JSON object match
#   the recording exactly (except ignored keys)
# - if the request body is NOT JSON, check that the request body matches the recording exactly
#
# If match_request_json_object_values is True, the matcher will also validate that the values inside
# the JSON object match (not just the keys)
def vcr_body_matcher(r1, r2, match_request_json_object_values=False):
    r1_body = r1.body
    r2_body = r2.body

    # body may be a stream, in which case read the content
    if hasattr(r1.body, 'read'):
        r1_body = r1.body.read()

    if hasattr(r2.body, 'read'):
        r2_body = r2.body.read()

    # if bodies are identical its a match
    if r1_body == r2_body:
        return True

    # if either body is None (but both aren't none) then its NOT a match
    if r1_body is None or r2_body is None:
        return False

    # try to decode both reponses as JSON
    # if the request body is NOT JSON, then we expect the content to match EXACTLY which is covered by the
    # r1_body == r2_body check above
    try:
        r1_json = json.loads(r1_body.decode('UTF-8')) if hasattr(r1_body, 'decode') else json.loads(r1_body)
        r2_json = json.loads(r2_body.decode('UTF-8')) if hasattr(r2_body, 'decode') else json.loads(r2_body)
    except ValueError:
        return False

    # both request bodies were valid JSON, so validate that they are 'equivalent' (according to normalize_json_request_bodies_for_comparison)
    if r1_json is not None and r2_json is not None:
        r1_normalized = normalize_json_request_bodies_for_comparison(r1_json, not match_request_json_object_values)
        r2_normalized = normalize_json_request_bodies_for_comparison(r2_json, not match_request_json_object_values)

        result = r1_normalized == r2_normalized
        # if it is not a match then print DEBUG level logs showing info to debug the mismatch
        if not result:
            vcr_logger.debug("normalized request body from test run: " + str(r1_normalized))
            vcr_logger.debug("normalized request body from recording:  " + str(r2_normalized))

        return result

    return True


# removes blacklisted keys that we know may not match on subsequent test runs
# optionally replaces all values with empty strings so that we can compare only keys
def normalize_json_request_bodies_for_comparison(obj, replace_all_values):
    if isinstance(obj, dict):
        processed = {k: normalize_json_request_bodies_for_comparison(v, replace_all_values) for k, v in six.iteritems(obj) if k not in KEYS_TO_IGNORE_COMPARING_REQUEST_BODIES}
        return processed
    if isinstance(obj, list):
        return [normalize_json_request_bodies_for_comparison(x, replace_all_values) for x in obj]
    if isinstance(obj, str):
        try:
            return normalize_json_request_bodies_for_comparison(json.loads(obj), replace_all_values)
        except ValueError:
            pass

    return "" if replace_all_values else obj


# A custom persister which deletes cassettes before re-writing them in vcr-record-mode=all
# This allows --vcr-record-mode=all to function as an 'overwrite' of the cassette instead of an 'append'
class CassetteOverwritingPersister(FilesystemPersister):
    # partner teams do not want to overwrite these recordings, so never write them out
    CASSETTES_TO_NEVER_OVERWRITE = [
        'create_test_service_session.yml',
        'close_test_service_session.yml'
    ]

    @classmethod
    def load_cassette(cls, cassette_path, serializer):
        if os.path.exists(cassette_path) and vcr_mode == 'all' and os.path.basename(cassette_path) not in cls.CASSETTES_TO_NEVER_OVERWRITE:
            os.remove(cassette_path)

        return FilesystemPersister.load_cassette(cassette_path, serializer)

    @staticmethod
    def save_cassette(cassette_path, cassette_dict, serializer):
        if os.path.basename(cassette_path) in CassetteOverwritingPersister.CASSETTES_TO_NEVER_OVERWRITE:
            return

        return FilesystemPersister.save_cassette(cassette_path, cassette_dict, serializer)
