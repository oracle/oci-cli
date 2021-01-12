# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click


COMPLEX_TYPE_HELP = """
This is a complex type whose value must be valid JSON. The value can be provided as a string on the command line or passed in as a file using
the file://path/to/file syntax.

The --generate-param-json-input option can be used to generate an example of the JSON which must be provided. We recommend storing this example
in a file, modifying it as needed and then passing it back in via the file:// syntax.
"""


# A thin wrapper around click's String/Text type so that we can flag parameters which actually
# need to be provided as JSON. These still come across as strings on the command line (e.g. as
# a literal JSON string or as a file:// path), so the type here is currently more a convenience
# to easily flag/denote these as different than a "normal" string
class CliComplexType(click.types.StringParamType):
    name = 'complex type'

    def __repr__(self):
        return 'COMPLEX_TYPE'


CLI_COMPLEX_TYPE = CliComplexType()
