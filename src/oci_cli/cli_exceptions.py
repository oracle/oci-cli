# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


class RequiredValueNotInDefaultOrUserInputError(Exception):
    """A required value was not in the specified defaults file, nor was it provided as part of user input."""


class RequiredValueNotAvailableInternallyOrUserInputError(Exception):
    """A required value was not available internally (via SDK API call) nor was it provided as part of user input."""
