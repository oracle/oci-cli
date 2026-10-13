# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import datetime
import hashlib
import json
import os
import tempfile


CACHE_VERSION = 1
CACHE_FILE_NAME = "functions-invoke-endpoint-cache.json"
DEFAULT_ENDPOINT_CACHE_TTL_SECONDS = 15 * 60
ENDPOINT_CACHE_TTL_ENV_VAR = "OCI_CLI_FUNCTIONS_INVOKE_ENDPOINT_CACHE_TTL"


def get_cached_endpoint(ctx_obj, function_id, ttl_seconds=None, now=None):
    ttl_seconds = _normalize_ttl(ttl_seconds)
    if ttl_seconds <= 0:
        return None

    cache = _read_cache(ctx_obj)
    entry = cache.get("entries", {}).get(_cache_key(ctx_obj, function_id))
    if not entry:
        return None

    endpoint = entry.get("endpoint")
    cached_at = _parse_time(entry.get("cached_at"))
    if not endpoint or cached_at is None:
        return None

    now = now or datetime.datetime.utcnow()
    if now - cached_at > datetime.timedelta(seconds=ttl_seconds):
        return None

    return endpoint


def put_cached_endpoint(ctx_obj, function_id, endpoint, now=None):
    if not endpoint:
        return

    cache = _read_cache(ctx_obj)
    cache["version"] = CACHE_VERSION
    entries = cache.setdefault("entries", {})
    key = _cache_key(ctx_obj, function_id)
    entries[key] = {
        "key": _cache_key_parts(ctx_obj, function_id),
        "endpoint": endpoint,
        "cached_at": _format_time(now or datetime.datetime.utcnow())
    }
    _write_cache(ctx_obj, cache)


def delete_cached_endpoint(ctx_obj, function_id):
    cache = _read_cache(ctx_obj)
    entries = cache.get("entries", {})
    key = _cache_key(ctx_obj, function_id)
    if key not in entries:
        return

    del entries[key]
    _write_cache(ctx_obj, cache)


def get_cache_file_path(ctx_obj):
    config_file = ctx_obj.get("config_file") if ctx_obj else None
    if config_file:
        config_file = os.path.abspath(os.path.expandvars(os.path.expanduser(str(config_file))))
        cache_dir = os.path.dirname(config_file)
    else:
        cache_dir = os.path.join(os.path.expanduser("~"), ".oci")

    return os.path.join(cache_dir, CACHE_FILE_NAME)


def _normalize_ttl(ttl_seconds):
    if ttl_seconds is None:
        return DEFAULT_ENDPOINT_CACHE_TTL_SECONDS
    return max(int(ttl_seconds), 0)


def _read_cache(ctx_obj):
    cache_file = get_cache_file_path(ctx_obj)
    try:
        with open(cache_file, "r") as cache:
            data = json.load(cache)
    except Exception:
        return {"version": CACHE_VERSION, "entries": {}}

    if data.get("version") != CACHE_VERSION or not isinstance(data.get("entries"), dict):
        return {"version": CACHE_VERSION, "entries": {}}
    return data


def _write_cache(ctx_obj, cache_data):
    cache_file = get_cache_file_path(ctx_obj)
    cache_dir = os.path.dirname(cache_file)
    temp_file = None

    try:
        if not os.path.isdir(cache_dir):
            os.makedirs(cache_dir, 0o700)

        fd, temp_file = tempfile.mkstemp(prefix=".%s." % CACHE_FILE_NAME, dir=cache_dir)
        with os.fdopen(fd, "w") as cache:
            json.dump(cache_data, cache, indent=2, sort_keys=True)
            cache.write("\n")
        os.replace(temp_file, cache_file)
    except Exception:
        if temp_file and os.path.exists(temp_file):
            try:
                os.unlink(temp_file)
            except Exception:
                pass


def _cache_key(ctx_obj, function_id):
    return hashlib.sha256(json.dumps(_cache_key_parts(ctx_obj, function_id), sort_keys=True).encode("utf-8")).hexdigest()


def _cache_key_parts(ctx_obj, function_id):
    ctx_obj = ctx_obj or {}
    config = ctx_obj.get("config") or {}
    config_file = ctx_obj.get("config_file")
    if config_file:
        config_file = os.path.abspath(os.path.expandvars(os.path.expanduser(str(config_file))))

    return {
        "auth": _to_text(ctx_obj.get("auth")),
        "config_file": _to_text(config_file),
        "endpoint": _to_text(ctx_obj.get("endpoint") or config.get("endpoint")),
        "enable_dual_stack": _to_text(ctx_obj.get("enable_dual_stack")),
        "function_id": _to_text(function_id),
        "profile": _to_text(ctx_obj.get("profile")),
        "region": _to_text(ctx_obj.get("region") or config.get("region"))
    }


def _to_text(value):
    return "" if value is None else str(value)


def _format_time(value):
    return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def _parse_time(value):
    if not value:
        return None

    try:
        return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return None
