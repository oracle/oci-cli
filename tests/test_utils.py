# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from oci_cli.cli_util import warn_if_clock_skew_present
import arrow
import requests
from . import util

try:
    import unittest.mock as mock
except ImportError:
    import mock


def test_get_clock_skew_with_no_skew():
    with mock.patch('oci_cli.cli_util.arrow') as mock_arrow:
        with mock.patch('oci_cli.cli_util.requests') as mock_requests:
            response = requests.Response()
            response.headers['Date'] = 'Wed, 01 Jan 2014 00:00:30 GMT'
            mock_requests.head = mock.Mock(return_value=response)

            mock_arrow.get = arrow.get
            mock_arrow.utcnow = mock.Mock(return_value=arrow.get(2014, 1, 1))

            config = {
                'region': 'us-phoenix-1'
            }

            with util.capture() as out:
                warn_if_clock_skew_present(config)
                assert 'WARNING' not in out[1].getvalue()


def test_get_clock_skew_detects_skew():
    with mock.patch('oci_cli.cli_util.arrow') as mock_arrow:
        mock_arrow.get = arrow.get
        mock_arrow.utcnow = mock.Mock(return_value=arrow.get(2014, 1, 1))

        config = {
            'region': 'us-phoenix-1'
        }

        with util.capture() as out:
            warn_if_clock_skew_present(config)
            assert 'WARNING' in out[1].getvalue()
