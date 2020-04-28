# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PassphraseDetails(object):
    """
    PassphraseDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PassphraseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param passphrase:
            The value to assign to the passphrase property of this PassphraseDetails.
        :type passphrase: str

        """
        self.swagger_types = {
            'passphrase': 'str'
        }

        self.attribute_map = {
            'passphrase': 'passphrase'
        }

        self._passphrase = None

    @property
    def passphrase(self):
        """
        Gets the passphrase of this PassphraseDetails.

        :return: The passphrase of this PassphraseDetails.
        :rtype: str
        """
        return self._passphrase

    @passphrase.setter
    def passphrase(self, passphrase):
        """
        Sets the passphrase of this PassphraseDetails.

        :param passphrase: The passphrase of this PassphraseDetails.
        :type: str
        """
        self._passphrase = passphrase

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
