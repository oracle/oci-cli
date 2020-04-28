# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NfsExportConfig(object):
    """
    NfsExportConfig model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NfsExportConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param read_write:
            The value to assign to the read_write property of this NfsExportConfig.
        :type read_write: bool

        :param world:
            The value to assign to the world property of this NfsExportConfig.
        :type world: bool

        :param ip_address:
            The value to assign to the ip_address property of this NfsExportConfig.
        :type ip_address: str

        :param subnet_mask_length:
            The value to assign to the subnet_mask_length property of this NfsExportConfig.
        :type subnet_mask_length: int

        :param hostname:
            The value to assign to the hostname property of this NfsExportConfig.
        :type hostname: str

        """
        self.swagger_types = {
            'read_write': 'bool',
            'world': 'bool',
            'ip_address': 'str',
            'subnet_mask_length': 'int',
            'hostname': 'str'
        }

        self.attribute_map = {
            'read_write': 'readWrite',
            'world': 'world',
            'ip_address': 'ipAddress',
            'subnet_mask_length': 'subnetMaskLength',
            'hostname': 'hostname'
        }

        self._read_write = None
        self._world = None
        self._ip_address = None
        self._subnet_mask_length = None
        self._hostname = None

    @property
    def read_write(self):
        """
        Gets the read_write of this NfsExportConfig.

        :return: The read_write of this NfsExportConfig.
        :rtype: bool
        """
        return self._read_write

    @read_write.setter
    def read_write(self, read_write):
        """
        Sets the read_write of this NfsExportConfig.

        :param read_write: The read_write of this NfsExportConfig.
        :type: bool
        """
        self._read_write = read_write

    @property
    def world(self):
        """
        Gets the world of this NfsExportConfig.

        :return: The world of this NfsExportConfig.
        :rtype: bool
        """
        return self._world

    @world.setter
    def world(self, world):
        """
        Sets the world of this NfsExportConfig.

        :param world: The world of this NfsExportConfig.
        :type: bool
        """
        self._world = world

    @property
    def ip_address(self):
        """
        Gets the ip_address of this NfsExportConfig.

        :return: The ip_address of this NfsExportConfig.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this NfsExportConfig.

        :param ip_address: The ip_address of this NfsExportConfig.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def subnet_mask_length(self):
        """
        Gets the subnet_mask_length of this NfsExportConfig.

        :return: The subnet_mask_length of this NfsExportConfig.
        :rtype: int
        """
        return self._subnet_mask_length

    @subnet_mask_length.setter
    def subnet_mask_length(self, subnet_mask_length):
        """
        Sets the subnet_mask_length of this NfsExportConfig.

        :param subnet_mask_length: The subnet_mask_length of this NfsExportConfig.
        :type: int
        """
        self._subnet_mask_length = subnet_mask_length

    @property
    def hostname(self):
        """
        Gets the hostname of this NfsExportConfig.

        :return: The hostname of this NfsExportConfig.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this NfsExportConfig.

        :param hostname: The hostname of this NfsExportConfig.
        :type: str
        """
        self._hostname = hostname

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
