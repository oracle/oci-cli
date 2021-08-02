# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import datetime
import unittest
import json
import pytz
from dateutil.parser import parse
from tests import test_config_container
from tests import util

CASSETTE_LIBRARY_DIR = 'services/audit/tests/cassettes'
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


class TestAudit(unittest.TestCase):

    # For recording, don't match on the query string because that includes the date range for the query
    # (and that will change between runs)
    @test_config_container.RecordReplay('audit', cassette_library_dir=CASSETTE_LIBRARY_DIR, match_on=['method', 'scheme', 'host', 'port', 'vcr_path_matcher'])
    def test_all_operations(self):
        """Successfully calls every operation with basic options."""
        self.subtest_event_list()
        # Not present in the preview spec
        self.subtest_config_get()

    def subtest_config_get(self):
        result = self.invoke(['audit', 'config', 'get', '--compartment-id', util.COMPARTMENT_ID])

        util.validate_response(result)
        response = json.loads(result.output)
        assert response["data"]["retention-period-days"] is not None

    def subtest_event_list(self):
        end_time = datetime.datetime.utcnow()
        start_time = end_time + datetime.timedelta(days=-197)

        result = self.invoke(['audit', 'event', 'list', '--compartment-id', util.COMPARTMENT_ID, '--start-time', start_time.strftime(DATETIME_FORMAT), '--end-time', end_time.strftime(DATETIME_FORMAT)])
        assert result.exit_code == 0 or result.exit_code is None
        if result.output:
            response = json.loads(result.output)
            # Some jitter because audit needs a RFC3339 date but only works with minute precision
            end_time_with_zone = pytz.utc.localize(end_time) + datetime.timedelta(minutes=5)
            start_time_with_zone = pytz.utc.localize(start_time) + datetime.timedelta(minutes=-5)
            for event in response["data"]:
                if not test_config_container.using_vcr_with_mock_responses():
                    parsed_date = parse(event["event-time"])
                    assert parsed_date >= start_time_with_zone
                    assert parsed_date <= end_time_with_zone

    @test_config_container.RecordReplay('audit', cassette_library_dir=CASSETTE_LIBRARY_DIR)
    def test_event_list(self):
        start_time = datetime.datetime(2020, 5, 5)
        end_time = start_time + datetime.timedelta(minutes=30)

        # This is the original, default version of the command.
        # Subsequent commands with additional parameters should produce pretty much the same output.
        result = self.invoke(
            ['audit', 'event', 'list',
                '--all',
                '--compartment-id', util.COMPARTMENT_ID,
                '--start-time', start_time.strftime(DATETIME_FORMAT),
                '--end-time', end_time.strftime(DATETIME_FORMAT)])
        assert result.exit_code == 0
        response = json.loads(result.output)
        events = response["data"]
        event_count = len(events)
        self.assertGreater(len(events), 0)
        for event in events:
            parsed_date = parse(event["event-time"])
            event_type = event["event-type"]
            event_source = event["source"]
            credential_id = event["data"]["identity"]

        # This should match the original with no changes.
        result = self.invoke(
            ['audit', 'event', 'list',
                '--all', '--stream-output',
                '--compartment-id', util.COMPARTMENT_ID,
                '--start-time', start_time.strftime(DATETIME_FORMAT),
                '--end-time', end_time.strftime(DATETIME_FORMAT)])
        assert result.exit_code == 0
        response = json.loads(result.output)
        events = response["data"]
        self.assertEquals(len(events), event_count)
        for event in events:
            parsed_date = parse(event["event-time"])
            event_type = event["event-type"]
            event_source = event["source"]
            credential_id = event["data"]["identity"]

        # This should have the same count as the original but with camelCaseNames instead of dash-names.
        result = self.invoke(
            ['audit', 'event', 'list',
                '--all', '--skip-deserialization',
                '--compartment-id', util.COMPARTMENT_ID,
                '--start-time', start_time.strftime(DATETIME_FORMAT),
                '--end-time', end_time.strftime(DATETIME_FORMAT)])
        assert result.exit_code == 0
        response = json.loads(result.output)
        events = response["data"]
        self.assertEquals(len(events), event_count)
        for event in events:
            parsed_date = parse(event["eventTime"])
            event_type = event["eventType"]
            event_source = event["source"]
            credential_id = event["data"]["identity"]

        # This should have the same count as the original but with camelCaseNames instead of dash-names.
        result = self.invoke(
            ['audit', 'event', 'list',
                '--all', '--skip-deserialization', '--stream-output',
                '--compartment-id', util.COMPARTMENT_ID,
                '--start-time', start_time.strftime(DATETIME_FORMAT),
                '--end-time', end_time.strftime(DATETIME_FORMAT)])
        assert result.exit_code == 0
        response = json.loads(result.output)
        events = response["data"]
        self.assertEquals(len(events), event_count)
        for event in events:
            parsed_date = parse(event["eventTime"])
            event_type = event["eventType"]
            event_source = event["source"]
            credential_id = event["data"]["identity"]

        # This should have camelCaseNames instead of dash-names.
        result = self.invoke(
            ['audit', 'event', 'list',
                '--skip-deserialization',
                '--compartment-id', util.COMPARTMENT_ID,
                '--start-time', start_time.strftime(DATETIME_FORMAT),
                '--end-time', end_time.strftime(DATETIME_FORMAT)])
        assert result.exit_code == 0 or result.exit_code is None
        response = json.loads(result.output)
        events = response["data"]
        for event in events:
            parsed_date = parse(event["eventTime"])
            event_type = event["eventType"]
            event_source = event["source"]
            credential_id = event["data"]["identity"]

        # These will throw a validation error.
        result = self.invoke(
            ['audit', 'event', 'list',
                '--stream-output',
                '--compartment-id', util.COMPARTMENT_ID,
                '--start-time', start_time.strftime(DATETIME_FORMAT),
                '--end-time', end_time.strftime(DATETIME_FORMAT)])
        assert 'requires --all' in result.output
        result = self.invoke(
            ['audit', 'event', 'list',
                '--skip-deserialization', '--stream-output',
                '--compartment-id', util.COMPARTMENT_ID,
                '--start-time', start_time.strftime(DATETIME_FORMAT),
                '--end-time', end_time.strftime(DATETIME_FORMAT)])
        assert 'requires --all' in result.output

    @test_config_container.RecordReplay('audit', cassette_library_dir=CASSETTE_LIBRARY_DIR)
    def test_event_list_query(self):
        start_time = datetime.datetime(2020, 5, 5, minute=1)
        end_time = start_time + datetime.timedelta(minutes=30)

        # This is the original, default version of the command.
        # Subsequent queries with additional parameters should produce pretty much the same output.
        result = self.invoke(
            ['audit', 'event', 'list',
                '--all',
                '--compartment-id', util.COMPARTMENT_ID,
                '--start-time', start_time.strftime(DATETIME_FORMAT),
                '--end-time', end_time.strftime(DATETIME_FORMAT),
                '--query',
                "data[?contains(\"event-type\",'com.oraclecloud.Audit.ListEvents')].{\"event-type\":\"event-type\",\"source\":\"source\",LoginDate:\"event-time\",\"user\":\"data\".\"identity\".\"credentials\"}"])
        assert result.exit_code == 0
        events = json.loads(result.output)
        event_count = len(events)
        self.assertGreater(len(events), 0)
        for event in events:
            parsed_date = parse(event["LoginDate"])
            event_type = event["event-type"]
            event_source = event["source"]
            credential_id = event["user"]

        result = self.invoke(
            ['audit', 'event', 'list',
                '--all',
                '--compartment-id', util.COMPARTMENT_ID,
                '--start-time', start_time.strftime(DATETIME_FORMAT),
                '--end-time', end_time.strftime(DATETIME_FORMAT),
                '--stream-output',
                '--query',
                "data[?contains(\"event-type\",'com.oraclecloud.Audit.ListEvents')].{\"event-type\":\"event-type\",\"source\":\"source\",LoginDate:\"event-time\",\"user\":\"data\".\"identity\".\"credentials\"}"])
        assert result.exit_code == 0
        events = json.loads(result.output)
        self.assertEquals(len(events), event_count)
        for event in events:
            parsed_date = parse(event["LoginDate"])
            event_type = event["event-type"]
            event_source = event["source"]
            credential_id = event["user"]

        # The query fields need to be camelCaseNames instead of dash-names.
        result = self.invoke(
            ['audit', 'event', 'list',
                '--all',
                '--compartment-id', util.COMPARTMENT_ID,
                '--start-time', start_time.strftime(DATETIME_FORMAT),
                '--end-time', end_time.strftime(DATETIME_FORMAT),
                '--skip-deserialization',
                '--query',
                "data[?contains(\"eventType\",'com.oraclecloud.Audit.ListEvents')].{\"event-type\":\"eventTtype\",\"source\":\"source\",LoginDate:\"eventTime\",\"user\":\"data\".\"identity\".\"credentials\"}"])
        assert result.exit_code == 0
        events = json.loads(result.output)
        self.assertEquals(len(events), event_count)
        for event in events:
            parsed_date = parse(event["LoginDate"])
            event_type = event["event-type"]
            event_source = event["source"]
            credential_id = event["user"]

        # The query fields need to be camelCaseNames instead of dash-names.
        result = self.invoke(
            ['audit', 'event', 'list',
                '--all',
                '--compartment-id', util.COMPARTMENT_ID,
                '--start-time', start_time.strftime(DATETIME_FORMAT),
                '--end-time', end_time.strftime(DATETIME_FORMAT),
                '--stream-output', '--skip-deserialization',
                '--query',
                "data[?contains(\"eventType\",'com.oraclecloud.Audit.ListEvents')].{\"event-type\":\"eventType\",\"source\":\"source\",LoginDate:\"eventTime\",\"user\":\"data\".\"identity\".\"credentials\"}"])
        assert result.exit_code == 0
        events = json.loads(result.output)
        self.assertEquals(len(events), event_count)
        for event in events:
            parsed_date = parse(event["LoginDate"])
            event_type = event["event-type"]
            event_source = event["source"]
            credential_id = event["user"]

    def invoke(self, commands, debug=False, ** args):
        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, ** args)


if __name__ == '__main__':
    unittest.main()
