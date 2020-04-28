# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import arrow
import click
import re
import six


class CliDatetime(click.ParamType):
    name = 'datetime'

    # Each entry in this list is a dict with the following keys:
    #
    #   - format_string: The format string arrow will use to parse the date
    #   - regex_pattern: The regular expression we'll apply to check if the input should be parsed using the format_string in this
    #     entry. We need this because arrow tends to be a bit loose on accepted formats and tries its best to match, so if we want a
    #     hard match we have to gate with something else
    #   - use_timezone: If the datetime is effectively naive (i.e. the format string does not parse out a timezone), what timezone we
    #     should assume the datetime is in. For naive datetimes, this should be UTC unless there is a very good reason to be otherwise.
    #     For formats that do have an explicit timezone, the value of this key should be None
    VALID_DATETIME_FORMATS = [
        ######################################
        # Datetimes with a literal Z at the end (for UTC)
        ######################################
        {
            # Literal Z at the end for UTC with milliseconds
            'format_string': 'YYYY-MM-DDTHH:mm:ss.SSS[Z]',
            'regex_pattern': re.compile(r"^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{1,3})[Zz]$"),
            'use_timezone': None,
        },
        {
            # Literal Z at the end for UTC without milliseconds
            'format_string': 'YYYY-MM-DDTHH:mm:ss[Z]',
            'regex_pattern': re.compile(r"^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)[Zz]$"),
            'use_timezone': None
        },
        {
            # Literal Z at the end for UTC with to-the-minute precision
            'format_string': 'YYYY-MM-DDTHH:mm[Z]',
            'regex_pattern': re.compile(r"^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]([01][0-9]|2[0-3]):([0-5][0-9])[Zz]$"),
            'use_timezone': None
        },

        ######################################
        # Datetimes with a numeric timezone offset that is colon separated (e.g. 08:00)
        ######################################
        {
            # Full RFC 3339 date with milliseconds and a colon in the timezone component, e.g. 2018-06-08T10:11:51.456+02:00
            'format_string': 'YYYY-MM-DDTHH:mm:ss.SSSZZ',
            'regex_pattern': re.compile(r"^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{1,3})([\+|\-]([01][0-9]|2[0-3]):[0-5][0-9])$"),
            'use_timezone': None
        },
        {
            # RFC 3339 date without the milliseconds and a colon in the timezone component, e.g. 2018-03-07T10:11:51+08:00
            'format_string': 'YYYY-MM-DDTHH:mm:ssZZ',
            'regex_pattern': re.compile(r"^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)([\+|\-]([01][0-9]|2[0-3]):[0-5][0-9])$"),
            'use_timezone': None
        },
        {
            # ISO8601 date with minute precision and a colon in the timezone component, e.g. 2018-03-07T10:17+08:00
            'format_string': 'YYYY-MM-DDTHH:mmZZ',
            'regex_pattern': re.compile(r"^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]([01][0-9]|2[0-3]):([0-5][0-9])([\+|\-]([01][0-9]|2[0-3]):[0-5][0-9])$"),
            'use_timezone': None
        },

        ######################################
        # Datetimes with a numeric timezone offset that is not colon separated (e.g. 0800)
        ######################################
        {
            # Full ISO8601 date with milliseconds and no colon in the timezone component, e.g. 2018-06-08T10:11:51.456+0200
            'format_string': 'YYYY-MM-DDTHH:mm:ss.SSSZ',
            'regex_pattern': re.compile(r"^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{1,3})([\+|\-]([01][0-9]|2[0-3])[0-5][0-9])$"),
            'use_timezone': None
        },
        {
            # ISO8601 date without the milliseconds and no colon in the timezone component, e.g. 2018-03-07T10:11:51+0800
            'format_string': 'YYYY-MM-DDTHH:mm:ssZ',
            'regex_pattern': re.compile(r"^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)([\+|\-]([01][0-9]|2[0-3])[0-5][0-9])$"),
            'use_timezone': None
        },
        {
            # ISO8601 date with minute precision and no colon in the timezone component, e.g. 2018-03-07T10:17+0800
            'format_string': 'YYYY-MM-DDTHH:mmZ',
            'regex_pattern': re.compile(r"^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]([01][0-9]|2[0-3]):([0-5][0-9])([\+|\-]([01][0-9]|2[0-3])[0-5][0-9])$"),
            'use_timezone': None
        },

        ######################################
        # Short datetimes we interpret as UTC
        ######################################
        {
            'format_string': 'YYYY-MM-DDTHH:mm',
            'regex_pattern': re.compile(r"^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]([01][0-9]|2[0-3]):([0-5][0-9])$"),
            'use_timezone': 'utc'
        },
        {
            'format_string': 'YYYY-MM-DD',
            'regex_pattern': re.compile(r"^\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$"),
            'use_timezone': 'utc'
        }
    ]

    VALID_DATETIME_EXCEPTION_MESSAGE = """The following datetime formats are supported:

    YYYY-MM-DDTHH:mm:ss.sssTZD (UTC) with milliseconds, e.g. 2017-09-15T20:30:00.123Z
    YYYY-MM-DDTHH:mm:ssTZD (UTC) without milliseconds, e.g. 2017-09-15T20:30:00Z
    YYYY-MM-DDTHH:mmTZD (UTC) with minute precision, e.g. 2017-09-15T20:30Z
    YYYY-MM-DDTHH:mm:ssTZD (timzone with offset) with milliseconds, e.g. 2017-09-15T12:30:00.456-08:00, 2017-09-15T12:30:00.456-0800
    YYYY-MM-DDTHH:mm:ssTZD (timezone with offset) without milliseconds, e.g. 2017-09-15T12:30:00-08:00, 2017-09-15T12:30:00-0800
    YYYY-MM-DDTHH:mmTZD (timezone with offset) with minute precision, e.g. 2017-09-15T12:35-08:00, 2017-09-15T12:35-0800
    YYYY-MM-DD HH:mm, e.g. 2017-09-15 17:25. The timezone for this date will be taken as UTC. (Needs to be surrounded by single or double quotes)
    YYYY-MM-DD, e.g. 2017-09-15. This date will be taken as midnight UTC of that day
    Unix time in seconds, e.g. 1412195400
    """

    VALID_DATETIME_CLI_HELP_MESSAGE = """
\b
The following datetime formats are supported:
\b
UTC with milliseconds
***********************
Format: YYYY-MM-DDTHH:mm:ss.sssTZD
Example: 2017-09-15T20:30:00.123Z
\b
UTC without milliseconds
**************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example: 2017-09-15T20:30:00Z
\b
UTC with minute precision
**************************
Format: YYYY-MM-DDTHH:mmTZD
Example: 2017-09-15T20:30Z
\b
Timezone with milliseconds
***************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00.456-08:00,
2017-09-15T12:30:00.456-0800
\b
Timezone without milliseconds
*******************************
Format: YYYY-MM-DDTHH:mm:ssTZD
Example:
2017-09-15T12:30:00-08:00,
2017-09-15T12:30:00-0800
\b
Timezone with minute precision
*******************************
Format: YYYY-MM-DDTHH:mmTZD
Example:
2017-09-15T12:30-08:00,
2017-09-15T12:30-0800
\b
Short date and time
********************
The timezone for this date and time will be taken as UTC (Needs to be surrounded by single or double quotes)
Format: 'YYYY-MM-DD HH:mm' or "YYYY-MM-DD HH:mm"
Example: '2017-09-15 17:25'
\b
Date Only
*********
This date will be taken as midnight UTC of that day
Format: YYYY-MM-DD
Example: 2017-09-15
\b
Epoch seconds
**************
Example: 1412195400
    """

    VALID_DATETIME_CLI_HELP_MESSAGE_RST = """

The following datetime formats are supported:

UTC with milliseconds
***********************
.. code::

    Format: YYYY-MM-DDTHH:mm:ss.sssTZD
    Example: 2017-09-15T20:30:00.123Z

UTC without milliseconds
**************************
.. code::

    Format: YYYY-MM-DDTHH:mm:ssTZD
    Example: 2017-09-15T20:30:00Z

UTC with minute precision
**************************
.. code::

    Format: YYYY-MM-DDTHH:mmTZD
    Example: 2017-09-15T20:30Z

Timezone with milliseconds
***************************
.. code::

    Format: YYYY-MM-DDTHH:mm:ssTZD
    Example: 2017-09-15T12:30:00.456-08:00, 2017-09-15T12:30:00.456-0800

Timezone without milliseconds
*******************************
.. code::

    Format: YYYY-MM-DDTHH:mm:ssTZD
    Example: 2017-09-15T12:30:00-08:00, 2017-09-15T12:30:00-0800

Timezone with minute precision
*******************************
.. code::

    Format: YYYY-MM-DDTHH:mmTZD
    Example: 2017-09-15T12:30-08:00, 2017-09-15T12:30-0800

Short date and time
********************
The timezone for this date and time will be taken as UTC (Needs to be surrounded by single or double quotes)

.. code::

    Format: 'YYYY-MM-DD HH:mm' or "YYYY-MM-DD HH:mm"
    Example: '2017-09-15 17:25'

Date Only
**********
This date will be taken as midnight UTC of that day

.. code::

    Format: YYYY-MM-DD
    Example: 2017-09-15

Epoch seconds
**************
.. code::

    Example: 1412195400
    """

    def __init__(self, apply_rounding=None):
        # Currently only the audit operations need rounding to the nearest minute
        if apply_rounding is not None and apply_rounding != 'minute':
            raise ValueError("The only current valid value for apply_rounding is 'minute'")

        self.apply_rounding = apply_rounding

    def convert(self, value, param, ctx):
        parsed_value = None

        if value is None:
            return None

        if not isinstance(value, six.string_types):
            raise click.BadParameter('Value {} is not a valid datetime. {}'.format(value, self.VALID_DATETIME_EXCEPTION_MESSAGE))

        if value.isdigit():
            try:
                parsed_value = arrow.get(value, 'X')
            except arrow.parser.ParserError:
                raise click.BadParameter('Value {} is not a value Unix time. {}'.format(value, self.VALID_DATETIME_EXCEPTION_MESSAGE))
        else:
            value_to_parse = value.strip().replace(' ', 'T')
            matching_format = self.get_matching_datetime_string_format(value_to_parse)

            if matching_format:
                if matching_format[1]:
                    parsed_value = arrow.get(value_to_parse, matching_format[0], tzinfo=matching_format[1])
                else:
                    parsed_value = arrow.get(value_to_parse, matching_format[0])

        if parsed_value is None:
            raise click.BadParameter('Value {} is not in a supported datetime format. {}'.format(value, self.VALID_DATETIME_EXCEPTION_MESSAGE))

        # Return a valid RFC3339 datetime string with a Z-offset. This is for consistency with how other SDKs behave, and also
        # for compatibility with services.
        #
        # Applying the UTC conversion is a no-op if the timezone is already UTC
        return '{}Z'.format(self.perform_rounding(parsed_value.to('utc')).format('YYYY-MM-DDTHH:mm:ss.SSS'))

    def get_matching_datetime_string_format(self, value):
        # This handles when someone passes us a valid ISO-8601 date, e.g. 2018-03-07 16:03:00+00:00 as the "T" separator
        # is optional (by consent)
        value_to_parse = value.strip().replace(' ', 'T')

        for datetime_format in self.VALID_DATETIME_FORMATS:
            if datetime_format['regex_pattern'].match(value_to_parse):
                return (datetime_format['format_string'], datetime_format['use_timezone'])

        return None

    # Round to the nearest minute (currently only minutes are supported), according to:
    #
    #   * < 30 seconds rounds down to the previous minute
    #   * >= 30 seconds rounds up to the next minute
    #
    # If this object has no rounding definition (i.e. apply_rounding is None) then this function
    # is a no-op and we just return the object which was passed in
    #
    # Note that milliseconds aren't taken into account when rounding - we truncate them rather than using the milliseconds
    # to round the seconds and then the seconds to round the minutes. As an example, in the case where the number of milliseconds
    # would cause the seconds to be rounded up to 30 we would still round the overall datetime down
    def perform_rounding(self, datetime_obj):
        if self.apply_rounding is None:
            return datetime_obj

        if self.apply_rounding != 'minute':
            raise ValueError("The only current valid value for apply_rounding is 'minute'")

        second = datetime_obj.second

        if second < 30:
            # Current minute
            return datetime_obj.replace(second=0, microsecond=0)
        else:
            # Round up to the next minute
            return datetime_obj.shift(minutes=1).replace(second=0, microsecond=0)

    def __repr__(self):
        return 'DATETIME'


CLI_DATETIME = CliDatetime()
CLI_DATETIME_ROUNDED_MINUTE = CliDatetime(apply_rounding='minute')
