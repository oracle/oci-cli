# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

# A module which holds test configuration information. This is intended to be a shared space where tests
# can figure out what kind of recording (via VCR) is being done and also so that they can take actions (e.g. waiting)
# in a VCR compatible/friendly way

from . import vcr_mods  # noqa: F401

import oci
import vcr

vcr_mode = None


def using_vcr_with_mock_responses():
    return vcr_mode != 'all'


def create_vcr(**kwargs):
    vcr_to_use = vcr.VCR(
        serializer='yaml',
        cassette_library_dir='tests/fixtures/cassettes',
        record_mode=vcr_mode
    )

    vcr_to_use.register_matcher('vcr_query_matcher', vcr_query_matcher)
    vcr_to_use.register_matcher('vcr_path_matcher', vcr_path_matcher)

    if 'match_on' in kwargs:
        vcr_to_use.match_on = kwargs['match_on']
    else:
        vcr_to_use.match_on = ['method', 'scheme', 'host', 'port', 'vcr_path_matcher', 'vcr_query_matcher']

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
    r1_updated_path = list(r1_path)
    r2_updated_path = list(r2_path)

    if len(r1_path) != len(r2_path):
        return False

    for s1, s2 in zip(r1_path, r2_path):
        for s in path_ignore_strings:
            if s in s1 and s in s2:
                r1_updated_path.remove(s1)
                r2_updated_path.remove(s2)

    return r1_updated_path == r2_updated_path
