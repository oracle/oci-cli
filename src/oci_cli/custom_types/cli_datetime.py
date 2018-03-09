# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import arrow
import click
import six


class CliDatetime(click.ParamType):
    name = 'datetime'

    VALID_DATETIME_FORMATS = [
        {'format_string': 'YYYY-MM-DDTHH:mm:ss.SSS[Z]', 'use_timezone': None},  # Literal Z at the end for UTC with milliseconds
        {'format_string': 'YYYY-MM-DDTHH:mm:ss[Z]', 'use_timezone': None},  # Literal Z at the end for UTC without milliseconds
        {'format_string': 'YYYY-MM-DDTHH:mm:ss.SSSZZ', 'use_timezone': None},  # Full RFC 3339 date with milliseconds, e.g. 2018-06-08T10:11:51.456+02:00
        {'format_string': 'YYYY-MM-DDTHH:mm:ssZZ', 'use_timezone': None},  # RFC 3339 date without the milliseconds
        {'format_string': 'YYYY-MM-DD', 'use_timezone': 'utc'}
    ]

    VALID_DATETIME_EXCEPTION_MESSAGE = """The following datetime formats are supported:

    YYYY-MM-DDTHH:mm:ss.sssTZD (UTC) with milliseconds, e.g., 2017-09-15T20:30:00.123Z
    YYYY-MM-DDTHH:mm:ssTZD (UTC) without milliseconds, e.g., 2017-09-15T20:30:00Z
    YYYY-MM-DDTHH:mm:ssTZD (timzone with offset) with milliseconds, e.g., 2017-09-15T12:30:00.456-08:00
    YYYY-MM-DDTHH:mm:ssTZD (timezone with offset) without milliseconds, e.g., 2017-09-15T12:30:00-08:00
    YYYY-MM-DD, e.g., 2017-09-15. This date will be taken as midnight UTC of that day
    Unix time in seconds, e.g. 1412195400
    """

    VALID_DATETIME_CLI_HELP_MESSAGE = """The following datetime formats are supported:

UTC with milliseconds
***********************
Format:
YYYY-MM-DDTHH:mm:ss.sssTZD
Example: 2017-09-15T20:30:00.123Z

UTC without milliseconds
**************************
Format:
YYYY-MM-DDTHH:mm:ssTZD
Example: 2017-09-15T20:30:00Z

Timezone with milliseconds
***************************
Format:
YYYY-MM-DDTHH:mm:ssTZD
Example: 2017-09-15T12:30:00.456-08:00

Timezone without milliseconds
*******************************
Format:
YYYY-MM-DDTHH:mm:ssTZD
Example: 2017-09-15T12:30:00-08:00

Date Only
*********
This date will be taken as midnight UTC of that day

Format:
YYYY-MM-DD
Example: 2017-09-15

Epoch seconds
**************
Example: 1412195400
    """

    def convert(self, value, param, ctx):
        parsed_value = None

        if value is None:
            return None

        if not isinstance(value, six.string_types):
            raise click.BadParameter('Value {} is not a valid datetime. {}'.format(value, self.VALID_DATETIME_MESSAGE))

        if value.isdigit():
            try:
                parsed_value = arrow.get(value, 'X')
            except arrow.parser.ParserError:
                raise click.BadParameter('Value {} is not a value Unix time. {}'.format(value, self.VALID_DATETIME_MESSAGE))
        else:
            for datetime_format in self.VALID_DATETIME_FORMATS:
                try:
                    # Try and parse. If there is a matching format we don't have to continue
                    if datetime_format['use_timezone']:
                        parsed_value = arrow.get(value, datetime_format['format_string'], tzinfo=datetime_format['use_timezone'])
                    else:
                        parsed_value = arrow.get(value, datetime_format['format_string'])
                    break
                except arrow.parser.ParserError:
                    # This is expected if the value doesn't match the format, we'll just continue to the next format
                    continue

        if parsed_value is None:
            raise click.BadParameter('Value {} is not in a supported datetime format. {}'.format(value, self.VALID_DATETIME_MESSAGE))

        # Return a valid RFC3339 datetime string with a Z-offset. This is for consistency with how other SDKs behave, and also
        # for compatibility with services.
        #
        # Applying the UTC conversion is a no-op if the timezone is already UTC
        return '{}Z'.format(parsed_value.to('utc').format('YYYY-MM-DDTHH:mm:ss.SSS'))

    def get_matching_datetime_string_format(self, value):
        for datetime_format in self.VALID_DATETIME_FORMATS:
            try:
                # Since we only need to know the matching format, don't worry about timezone bits
                arrow.get(value, datetime_format['format_string'])
                return datetime_format['format_string']
            except arrow.parser.ParserError:
                # This is expected if the value doesn't match the format, we'll just continue to the next format
                continue

        return None

    def __repr__(self):
        return 'DATETIME'


CLI_DATETIME = CliDatetime()
