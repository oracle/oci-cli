# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PhysicalTransferAppliance(object):
    """
    PhysicalTransferAppliance model.
    """

    #: A constant which can be used with the lock_status property of a PhysicalTransferAppliance.
    #: This constant has a value of "LOCKED"
    LOCK_STATUS_LOCKED = "LOCKED"

    #: A constant which can be used with the lock_status property of a PhysicalTransferAppliance.
    #: This constant has a value of "NOT_LOCKED"
    LOCK_STATUS_NOT_LOCKED = "NOT_LOCKED"

    #: A constant which can be used with the lock_status property of a PhysicalTransferAppliance.
    #: This constant has a value of "NA"
    LOCK_STATUS_NA = "NA"

    #: A constant which can be used with the finalize_status property of a PhysicalTransferAppliance.
    #: This constant has a value of "FINALIZED"
    FINALIZE_STATUS_FINALIZED = "FINALIZED"

    #: A constant which can be used with the finalize_status property of a PhysicalTransferAppliance.
    #: This constant has a value of "NOT_FINALIZED"
    FINALIZE_STATUS_NOT_FINALIZED = "NOT_FINALIZED"

    #: A constant which can be used with the finalize_status property of a PhysicalTransferAppliance.
    #: This constant has a value of "NA"
    FINALIZE_STATUS_NA = "NA"

    def __init__(self, **kwargs):
        """
        Initializes a new PhysicalTransferAppliance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param encryption_configured:
            The value to assign to the encryption_configured property of this PhysicalTransferAppliance.
        :type encryption_configured: bool

        :param lock_status:
            The value to assign to the lock_status property of this PhysicalTransferAppliance.
            Allowed values for this property are: "LOCKED", "NOT_LOCKED", "NA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lock_status: str

        :param finalize_status:
            The value to assign to the finalize_status property of this PhysicalTransferAppliance.
            Allowed values for this property are: "FINALIZED", "NOT_FINALIZED", "NA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type finalize_status: str

        :param total_space_in_bytes:
            The value to assign to the total_space_in_bytes property of this PhysicalTransferAppliance.
        :type total_space_in_bytes: int

        :param available_space_in_bytes:
            The value to assign to the available_space_in_bytes property of this PhysicalTransferAppliance.
        :type available_space_in_bytes: int

        """
        self.swagger_types = {
            'encryption_configured': 'bool',
            'lock_status': 'str',
            'finalize_status': 'str',
            'total_space_in_bytes': 'int',
            'available_space_in_bytes': 'int'
        }

        self.attribute_map = {
            'encryption_configured': 'encryptionConfigured',
            'lock_status': 'lockStatus',
            'finalize_status': 'finalizeStatus',
            'total_space_in_bytes': 'totalSpaceInBytes',
            'available_space_in_bytes': 'availableSpaceInBytes'
        }

        self._encryption_configured = None
        self._lock_status = None
        self._finalize_status = None
        self._total_space_in_bytes = None
        self._available_space_in_bytes = None

    @property
    def encryption_configured(self):
        """
        Gets the encryption_configured of this PhysicalTransferAppliance.

        :return: The encryption_configured of this PhysicalTransferAppliance.
        :rtype: bool
        """
        return self._encryption_configured

    @encryption_configured.setter
    def encryption_configured(self, encryption_configured):
        """
        Sets the encryption_configured of this PhysicalTransferAppliance.

        :param encryption_configured: The encryption_configured of this PhysicalTransferAppliance.
        :type: bool
        """
        self._encryption_configured = encryption_configured

    @property
    def lock_status(self):
        """
        Gets the lock_status of this PhysicalTransferAppliance.
        Allowed values for this property are: "LOCKED", "NOT_LOCKED", "NA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lock_status of this PhysicalTransferAppliance.
        :rtype: str
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        """
        Sets the lock_status of this PhysicalTransferAppliance.

        :param lock_status: The lock_status of this PhysicalTransferAppliance.
        :type: str
        """
        allowed_values = ["LOCKED", "NOT_LOCKED", "NA"]
        if not value_allowed_none_or_none_sentinel(lock_status, allowed_values):
            lock_status = 'UNKNOWN_ENUM_VALUE'
        self._lock_status = lock_status

    @property
    def finalize_status(self):
        """
        Gets the finalize_status of this PhysicalTransferAppliance.
        Allowed values for this property are: "FINALIZED", "NOT_FINALIZED", "NA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The finalize_status of this PhysicalTransferAppliance.
        :rtype: str
        """
        return self._finalize_status

    @finalize_status.setter
    def finalize_status(self, finalize_status):
        """
        Sets the finalize_status of this PhysicalTransferAppliance.

        :param finalize_status: The finalize_status of this PhysicalTransferAppliance.
        :type: str
        """
        allowed_values = ["FINALIZED", "NOT_FINALIZED", "NA"]
        if not value_allowed_none_or_none_sentinel(finalize_status, allowed_values):
            finalize_status = 'UNKNOWN_ENUM_VALUE'
        self._finalize_status = finalize_status

    @property
    def total_space_in_bytes(self):
        """
        Gets the total_space_in_bytes of this PhysicalTransferAppliance.

        :return: The total_space_in_bytes of this PhysicalTransferAppliance.
        :rtype: int
        """
        return self._total_space_in_bytes

    @total_space_in_bytes.setter
    def total_space_in_bytes(self, total_space_in_bytes):
        """
        Sets the total_space_in_bytes of this PhysicalTransferAppliance.

        :param total_space_in_bytes: The total_space_in_bytes of this PhysicalTransferAppliance.
        :type: int
        """
        self._total_space_in_bytes = total_space_in_bytes

    @property
    def available_space_in_bytes(self):
        """
        Gets the available_space_in_bytes of this PhysicalTransferAppliance.

        :return: The available_space_in_bytes of this PhysicalTransferAppliance.
        :rtype: int
        """
        return self._available_space_in_bytes

    @available_space_in_bytes.setter
    def available_space_in_bytes(self, available_space_in_bytes):
        """
        Sets the available_space_in_bytes of this PhysicalTransferAppliance.

        :param available_space_in_bytes: The available_space_in_bytes of this PhysicalTransferAppliance.
        :type: int
        """
        self._available_space_in_bytes = available_space_in_bytes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
