# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click


class CliCaseInsensitiveChoice(click.Choice):
    def __init__(self, choices):
        super(CliCaseInsensitiveChoice, self).__init__(choices)

    # This is: https://github.com/pallets/click/blob/b471d346e93b818d7c8a87d8cee9e0705435ac19/click/types.py#L145 but instead of relying
    # on the presence of a token_normalize_func, we always do a case insensitive match
    def convert(self, value, param, ctx):
        if value in self.choices:
            return value

        for choice in self.choices:
            if value.lower() == choice.lower():
                return choice

        self.fail('invalid choice: {}. (choose from {})'.format(value, ', '.join(self.choices)), param, ctx)
