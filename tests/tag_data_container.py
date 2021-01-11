# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# A module which is intended to hold information on tag namespaces and tags
# so that they can be shared across test cases. This is primarily here because the CLI
# tests mix up unittest and pytest test suites so using fixtures (apart from autouse fixtures
# https://docs.pytest.org/en/3.3.1/unittest.html) is a bit of a pain. The state/data tracked
# here can be used by unittest suites to get any tag information they need.
#
# This module also contains some helper functions for generating tag test data.

import os
import os.path

tag_namespace = None
tags = []


def write_defined_tags_to_file(file_path, tag_namespace, tag_names_to_values):
    target_folder = os.path.dirname(file_path)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with open(file_path, 'w') as f:
        f.write('{{ "{}": {{'.format(tag_namespace.name))  # { "tagNamespace": {

        tag_names = list(tag_names_to_values.keys())
        for idx, tag in enumerate(tag_names):
            f.write('  "{}": "{}"'.format(tag, tag_names_to_values[tag]))  # "tagName": "tagValue",
            if idx != len(tag_names) - 1:
                f.write(',')
        f.write('}}')  # Close out the JSON document


# Makes sure that the tag namespace and tags known by this module are active so that they can be used. We do
# this by reactivating the namespace and then each tag.
#
# invoke_func is intended to be a function which can call a CLI command when passed an array representing
# the command and its arguments
def ensure_namespace_and_tags_active(invoke_func):
    invoke_func(['iam', 'tag-namespace', 'reactivate', '--tag-namespace-id', tag_namespace.id])
    for t in tags:
        invoke_func(['iam', 'tag', 'reactivate', '--tag-namespace-id', tag_namespace.id, '--tag-name', t.name])
