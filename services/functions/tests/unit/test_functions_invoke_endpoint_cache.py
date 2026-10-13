# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import datetime
import json
import os
import tempfile
import unittest

from services.functions.src.oci_cli_functions import invoke_endpoint_cache


def _ctx(cache_dir):
    return {
        "auth": "api_key",
        "config": {"region": "us-phoenix-1"},
        "config_file": os.path.join(cache_dir, "config"),
        "enable_dual_stack": False,
        "endpoint": None,
        "profile": "DEFAULT",
        "region": None
    }


class TestInvokeEndpointCache(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

    def test_endpoint_cache_returns_cached_endpoint(self):
        ctx = _ctx(self.temp_dir.name)
        now = datetime.datetime(2026, 7, 17, 10, 0, 0)

        invoke_endpoint_cache.put_cached_endpoint(ctx, "ocid1.fnfunc.oc1.phx.example", "https://invoke.example.com", now=now)

        self.assertEqual(
            "https://invoke.example.com",
            invoke_endpoint_cache.get_cached_endpoint(
                ctx,
                "ocid1.fnfunc.oc1.phx.example",
                ttl_seconds=900,
                now=now + datetime.timedelta(seconds=30)
            )
        )

    def test_endpoint_cache_expires_entries(self):
        ctx = _ctx(self.temp_dir.name)
        now = datetime.datetime(2026, 7, 17, 10, 0, 0)

        invoke_endpoint_cache.put_cached_endpoint(ctx, "ocid1.fnfunc.oc1.phx.example", "https://invoke.example.com", now=now)

        self.assertIsNone(invoke_endpoint_cache.get_cached_endpoint(
            ctx,
            "ocid1.fnfunc.oc1.phx.example",
            ttl_seconds=60,
            now=now + datetime.timedelta(seconds=61)
        ))

    def test_endpoint_cache_ttl_zero_disables_cache(self):
        ctx = _ctx(self.temp_dir.name)
        now = datetime.datetime(2026, 7, 17, 10, 0, 0)

        invoke_endpoint_cache.put_cached_endpoint(ctx, "ocid1.fnfunc.oc1.phx.example", "https://invoke.example.com", now=now)

        self.assertIsNone(invoke_endpoint_cache.get_cached_endpoint(
            ctx,
            "ocid1.fnfunc.oc1.phx.example",
            ttl_seconds=0,
            now=now
        ))

    def test_endpoint_cache_uses_context_in_cache_key(self):
        ctx = _ctx(self.temp_dir.name)
        other_ctx = _ctx(self.temp_dir.name)
        other_ctx["profile"] = "OTHER"
        now = datetime.datetime(2026, 7, 17, 10, 0, 0)

        invoke_endpoint_cache.put_cached_endpoint(ctx, "ocid1.fnfunc.oc1.phx.example", "https://invoke.example.com", now=now)

        self.assertIsNone(invoke_endpoint_cache.get_cached_endpoint(
            other_ctx,
            "ocid1.fnfunc.oc1.phx.example",
            ttl_seconds=900,
            now=now
        ))

    def test_endpoint_cache_uses_dual_stack_in_cache_key(self):
        ctx = _ctx(self.temp_dir.name)
        dual_stack_ctx = _ctx(self.temp_dir.name)
        dual_stack_ctx["enable_dual_stack"] = True
        now = datetime.datetime(2026, 7, 17, 10, 0, 0)

        invoke_endpoint_cache.put_cached_endpoint(ctx, "ocid1.fnfunc.oc1.phx.example", "https://invoke.example.com", now=now)

        self.assertIsNone(invoke_endpoint_cache.get_cached_endpoint(
            dual_stack_ctx,
            "ocid1.fnfunc.oc1.phx.example",
            ttl_seconds=900,
            now=now
        ))

    def test_endpoint_cache_ignores_invalid_cache_file(self):
        ctx = _ctx(self.temp_dir.name)
        cache_file = invoke_endpoint_cache.get_cache_file_path(ctx)
        with open(cache_file, "w") as cache:
            cache.write("{invalid json")

        self.assertIsNone(invoke_endpoint_cache.get_cached_endpoint(
            ctx,
            "ocid1.fnfunc.oc1.phx.example",
            ttl_seconds=900,
            now=datetime.datetime(2026, 7, 17, 10, 0, 0)
        ))

    def test_endpoint_cache_deletes_entry(self):
        ctx = _ctx(self.temp_dir.name)
        now = datetime.datetime(2026, 7, 17, 10, 0, 0)

        invoke_endpoint_cache.put_cached_endpoint(ctx, "ocid1.fnfunc.oc1.phx.example", "https://invoke.example.com", now=now)
        invoke_endpoint_cache.delete_cached_endpoint(ctx, "ocid1.fnfunc.oc1.phx.example")

        self.assertIsNone(invoke_endpoint_cache.get_cached_endpoint(
            ctx,
            "ocid1.fnfunc.oc1.phx.example",
            ttl_seconds=900,
            now=now
        ))

        with open(invoke_endpoint_cache.get_cache_file_path(ctx), "r") as cache:
            cache_data = json.load(cache)
        self.assertEqual({}, cache_data["entries"])


if __name__ == "__main__":
    unittest.main()
