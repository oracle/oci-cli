# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


"""The main purpose of this page is to have all the error messages which is being used in the Interactive CLI,
so updating those in the future should be easy, it is recommended not to call those of those error messages from
outside this page, instead call get_error_message funstion"""

error_messages = {
    "invalid_input": "Incorrect input:",
    "missing_required_params": "Error: Missing required parameters",
    "resource_search_failed": "Error: Resource search failed, please check you are correctly authorized to view resources",
    "no_items_found": "No items found",
}


def get_error_message(error, extra_text=""):
    if error in error_messages:
        error_message = error_messages[error]
        if extra_text:
            error_message += " " + extra_text
        return error_message
