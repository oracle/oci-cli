# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from alloy import alloy_constants


"""The main purpose of this page is to have all the error messages which is being used in the CLI Alloy,
so updating those in the future should be easy, it is recommended not to call error messages from
outside this page, instead call get_error_message function"""

error_messages = {
    alloy_constants.INVALID_INPUT: "Incorrect input:",
    alloy_constants.NO_SERVICE_CONFIG: "Could not find service config",
    alloy_constants.NO_CLI_FOUND: "CLI installation not found",
    alloy_constants.ALLOY_NAME_TAKEN: "Alias name already in use",
    alloy_constants.PROVIDER_NAME_MISSING: "Provider name is missing in service config",
    alloy_constants.SUBSCRIBED_SERVICES_MISSING: "Subscribed services is missing in service config",
}


def get_error_message(error, extra_text=""):
    if error in error_messages:
        error_message = error_messages[error]
        if extra_text:
            error_message += " " + extra_text
        return error_message
