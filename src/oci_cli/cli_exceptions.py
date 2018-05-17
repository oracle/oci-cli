# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


class RequiredValueNotInDefaultOrUserInputError(Exception):
    """A required value was not in the specified defaults file, nor was it provided as part of user input."""


class RequiredValueNotAvailableInternallyOrUserInputError(Exception):
    """A required value was not available internally (via SDK API call) nor was it provided as part of user input."""
