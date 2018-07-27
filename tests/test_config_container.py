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

    if 'match_on' in kwargs:
        vcr_to_use.match_on = kwargs['match_on']

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
