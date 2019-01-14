# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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
