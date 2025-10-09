# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import terminaltables

error_hints = {
    ("tenancy", "missing"): "log into the console and find this OCID at the bottom of any page",
    ("tenancy", "malformed"): "this must be an OCID",
    ("user", "missing"): "log into the console and go to the user's settings page to find their OCID",
    ("user", "malformed"): "this must be an OCID",
    ("fingerprint", "missing"): "openssl rsa -pubout -outform DER -in <path to your private key> | openssl md5 -c",
    ("fingerprint", "malformed"): "openssl rsa -pubout -outform DER -in <path to your private key> | openssl md5 -c",
    ("region", "missing"): "for example, us-phoenix-1",
    ("key_file", "missing"): "the full path and filename of the private PEM key file"
}


def render_config_errors(config_exception):
    """Return a str of the ascii table of errors"""
    headers = ["Key", "Error", "Hint"]
    # (key, code, hint)
    pieces = [
        [param, code, error_hints.get((param, code), "")]
        for (param, code) in config_exception.errors.items()
    ]
    data = [headers] + pieces
    # TODO include config_file name?
    table = terminaltables.AsciiTable(table_data=data, title="Config Errors")
    return table.table
