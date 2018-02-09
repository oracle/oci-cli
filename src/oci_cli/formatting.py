# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import six
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
        for (param, code) in six.iteritems(config_exception.errors)
    ]
    data = [headers] + pieces
    # TODO include config_file name?
    table = terminaltables.AsciiTable(table_data=data, title="Config Errors")
    return table.table
