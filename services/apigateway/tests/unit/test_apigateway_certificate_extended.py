# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util
import pytest


# pytest -s services/apigateway/tests/unit/test_apigateway_certificate_extended.py
class TestApiGatewayCertificate(unittest.TestCase):
    def setUp(self):
        pass

    def test_cert(self):
        result = util.invoke_command(['api-gateway', 'certificate'])
        expected = ['Usage:', 'Commands:', 'Options:', '--help',
                    'change-compartment', 'create', 'delete', 'get', 'list',
                    'update']
        for command in expected:
            assert command in result.output

    def test_cert_compartment_change(self):
        pytest.skip('To fix image tests failure.')
        result = util.invoke_command(
            ['api-gateway', 'certificate', 'change-compartment'])
        expected = ['Usage:', 'Error: Missing option(s)', '--certificate-id',
                    '--compartment-id.']
        verify(result, expected)

        result = util.invoke_command(
            ['api-gateway', 'certificate', 'change-compartment', '-h'])
        expected = ['Options:', '--certificate-id', '--compartment-id',
                    '--if-match', '--from-json', '--help']
        verify(result, expected)

        for command in expected[1:-2]:
            result = util.invoke_command(
                ['api-gateway', 'certificate', 'change-compartment', command])

            verify(result, ['Error: {c} option requires an argument'.format(
                c=command)])

    def test_cert_create(self):
        pytest.skip('To fix image tests failure.')
        result = util.invoke_command(
            ['api-gateway', 'certificate', 'create'])
        expected = ['Usage:', 'Error: Missing option(s)', '--compartment-id',
                    '--private-key-file', '--certificate-file']
        verify(result, expected)

        result = util.invoke_command(
            ['api-gateway', 'certificate', 'create', '-h'])
        expected = ['Options:', '--compartment-id', '--display-name',
                    '--freeform-tags', '--defined-tags', '--wait-for-state',
                    '--max-wait-seconds', '--wait-interval-seconds',
                    '--private-key-file', '--certificate-file',
                    '--intermediate-certificates-file', '--from-json', '--help']
        verify(result, expected)

        for command in expected[1:-2]:
            result = util.invoke_command(
                ['api-gateway', 'certificate', 'create', command])

            verify(result, ['Error: {c} option requires an argument'.format(
                c=command)])

    def test_cert_delete(self):
        pytest.skip('To fix image tests failure.')
        result = util.invoke_command(
            ['api-gateway', 'certificate', 'delete'])
        expected = ['Usage:', 'Error: Missing option(s)', '--certificate-id']
        verify(result, expected)

        result = util.invoke_command(
            ['api-gateway', 'certificate', 'delete', '--force'])
        verify(result, expected)

        result = util.invoke_command(
            ['api-gateway', 'certificate', 'delete', '-h'])
        expected = ['Options:', '--certificate-id', '--if-match',
                    '--wait-for-state', '--max-wait-seconds',
                    '--wait-interval-seconds', '--from-json', '--help']
        verify(result, expected)

        for command in expected[1:-2]:
            result = util.invoke_command(
                ['api-gateway', 'certificate', 'delete', command])
            verify(result, ['Error: {c} option requires an argument'.format(
                c=command)])

    def test_cert_get(self):
        pytest.skip('To fix image tests failure.')
        result = util.invoke_command(
            ['api-gateway', 'certificate', 'get'])
        expected = ['Usage:', 'Error: Missing option(s)', '--certificate-id']
        verify(result, expected)

        result = util.invoke_command(
            ['api-gateway', 'certificate', 'get', '-h'])
        expected = ['Options:', '--certificate-id', '--from-json', '--help']
        verify(result, expected)

        for command in expected[1:-2]:
            result = util.invoke_command(
                ['api-gateway', 'certificate', 'get', command])
            verify(result, ['Error: {c} option requires an argument'.format(
                c=command)])

    def test_cert_list(self):
        pytest.skip('To fix image tests failure.')
        result = util.invoke_command(
            ['api-gateway', 'certificate', 'list'])
        expected = ['Usage:', 'Error: Missing option(s)', '--compartment-id']
        verify(result, expected)

        result = util.invoke_command(
            ['api-gateway', 'certificate', 'list', '--all'])
        verify(result, expected)

        result = util.invoke_command(
            ['api-gateway', 'certificate', 'list', '-h'])
        expected = ['Options:', '--compartment-id', '--display-name',
                    '--lifecycle-state', '--limit', '--page', '--sort-order',
                    '--sort-by', '--page-size', '--from-json',
                    '--help']
        verify(result, expected)

        for command in expected[1:-2]:
            result = util.invoke_command(
                ['api-gateway', 'certificate', 'list', command])
            verify(result, ['Error: {c} option requires an argument'.format(
                c=command)])

    def test_cert_update(self):
        pytest.skip('To fix image tests failure.')
        result = util.invoke_command(
            ['api-gateway', 'certificate', 'update'])
        expected = ['Usage:', 'Error: Missing option(s)', '--certificate-id']
        verify(result, expected)

        result = util.invoke_command(
            ['api-gateway', 'certificate', 'update', '--force'])
        verify(result, expected)

        result = util.invoke_command(
            ['api-gateway', 'certificate', 'update', '-h'])
        expected = ['Options:', '--certificate-id', '--defined-tags',
                    '--if-match', '--wait-for-state',
                    '--max-wait-seconds', '--wait-interval-seconds',
                    '--from-json', '--help']
        verify(result, expected)
        for command in expected[1:-2]:
            result = util.invoke_command(
                ['api-gateway', 'certificate', 'update', command])
            verify(result, ['Error: {c} option requires an argument'.format(
                c=command)])


def verify(res, expect):
    for reply in expect:
        assert reply in res.output
