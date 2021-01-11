# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NfsDatasetSpec(object):
    """
    NfsDatasetSpec model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NfsDatasetSpec object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this NfsDatasetSpec.
        :type name: str

        :param nfs_export_details:
            The value to assign to the nfs_export_details property of this NfsDatasetSpec.
        :type nfs_export_details: NfsExportDetails

        """
        self.swagger_types = {
            'name': 'str',
            'nfs_export_details': 'NfsExportDetails'
        }

        self.attribute_map = {
            'name': 'name',
            'nfs_export_details': 'nfsExportDetails'
        }

        self._name = None
        self._nfs_export_details = None

    @property
    def name(self):
        """
        Gets the name of this NfsDatasetSpec.

        :return: The name of this NfsDatasetSpec.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NfsDatasetSpec.

        :param name: The name of this NfsDatasetSpec.
        :type: str
        """
        self._name = name

    @property
    def nfs_export_details(self):
        """
        Gets the nfs_export_details of this NfsDatasetSpec.

        :return: The nfs_export_details of this NfsDatasetSpec.
        :rtype: NfsExportDetails
        """
        return self._nfs_export_details

    @nfs_export_details.setter
    def nfs_export_details(self, nfs_export_details):
        """
        Sets the nfs_export_details of this NfsDatasetSpec.

        :param nfs_export_details: The nfs_export_details of this NfsDatasetSpec.
        :type: NfsExportDetails
        """
        self._nfs_export_details = nfs_export_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
