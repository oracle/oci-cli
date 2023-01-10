# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import sys
import json
import datetime

from . import cli_constants
from .version import __version__


class RequiredValueNotInDefaultOrUserInputError(Exception):
    """A required value was not in the specified defaults file, nor was it provided as part of user input."""


class RequiredValueNotAvailableInternallyOrUserInputError(Exception):
    """A required value was not available internally (via SDK API call) nor was it provided as part of user input."""


class ClientException(Exception):
    """Custom Client Exception class that accepts kwargs as input and returns formatted JSON"""

    def __init__(self, exception_class, *args, **kwargs):
        exception_dict = kwargs
        exception_dict['logging_tips'] = "Please run the OCI CLI command using --debug flag to find more debug information."
        troubleshooting_tips = f"See [{cli_constants.TROUBLESHOOTING_DOCUMENTATION}] for more information about resolving this error. If you are unable to resolve this issue, run this CLI command with --debug option and contact Oracle support and provide them the full error message."

        if 'troubleshooting_tips' in exception_dict:
            exception_dict['troubleshooting_tips'] += " " + troubleshooting_tips
        else:
            exception_dict['troubleshooting_tips'] = troubleshooting_tips
        exception_dict['client_version'] = f'Oracle-PythonCLI/{__version__}'
        exception_dict['target_service'] = 'CLI'
        exception_dict['timestamp'] = datetime.datetime.utcnow().isoformat()
        self.exception_dict = exception_dict
        self.exception_class = exception_class

    def __str__(self):
        exception_resp = self.exception_dict
        details = json.dumps(exception_resp, indent=4, sort_keys=True)
        tpl = "{exc}:\n{details}"
        sys.exit(tpl.format(exc=self.exception_class, details=details))


class ServiceException(Exception):
    """Custom Service Exception class that accepts kwargs as input and returns formatted JSON"""

    def __init__(self, exception_dict, exception_class, *args, **kwargs):
        exception_dict.update(kwargs)
        self.exception_dict = exception_dict
        self.exception_class = exception_class
        exception_dict['logging_tips'] = "Please run the OCI CLI command using --debug flag to find more debug information."
        exception_dict['troubleshooting_tips'] = f"See [{cli_constants.SERVICE_ERROR_DOCUMENTATION}] for more information about resolving this error. If you are unable to resolve this issue, run this CLI command with --debug option and contact Oracle support and provide them the full error message."
        if 'client_version' in exception_dict:
            exception_dict['client_version'] += ', Oracle-PythonCLI/{}'.format(__version__)
        else:
            exception_dict['client_version'] = 'Oracle-PythonCLI/{}'.format(__version__)

    def __str__(self):
        exception_resp = self.exception_dict
        details = json.dumps(exception_resp, indent=4, sort_keys=True)
        tpl = "{exc}:\n{details}"
        sys.exit(tpl.format(exc=self.exception_class, details=details))
