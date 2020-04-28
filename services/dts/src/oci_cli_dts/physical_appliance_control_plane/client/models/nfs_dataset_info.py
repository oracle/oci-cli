# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NfsDatasetInfo(object):
    """
    NfsDatasetInfo model.
    """

    #: A constant which can be used with the state property of a NfsDatasetInfo.
    #: This constant has a value of "INITIALIZED"
    STATE_INITIALIZED = "INITIALIZED"

    #: A constant which can be used with the state property of a NfsDatasetInfo.
    #: This constant has a value of "ACTIVE"
    STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the state property of a NfsDatasetInfo.
    #: This constant has a value of "INACTIVE"
    STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the state property of a NfsDatasetInfo.
    #: This constant has a value of "SEALING"
    STATE_SEALING = "SEALING"

    #: A constant which can be used with the state property of a NfsDatasetInfo.
    #: This constant has a value of "SEALED"
    STATE_SEALED = "SEALED"

    #: A constant which can be used with the state property of a NfsDatasetInfo.
    #: This constant has a value of "DELETED"
    STATE_DELETED = "DELETED"

    #: A constant which can be used with the dataset_type property of a NfsDatasetInfo.
    #: This constant has a value of "NFS"
    DATASET_TYPE_NFS = "NFS"

    def __init__(self, **kwargs):
        """
        Initializes a new NfsDatasetInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this NfsDatasetInfo.
        :type name: str

        :param state:
            The value to assign to the state property of this NfsDatasetInfo.
            Allowed values for this property are: "INITIALIZED", "ACTIVE", "INACTIVE", "SEALING", "SEALED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type state: str

        :param dataset_type:
            The value to assign to the dataset_type property of this NfsDatasetInfo.
            Allowed values for this property are: "NFS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type dataset_type: str

        :param nfs_export_details:
            The value to assign to the nfs_export_details property of this NfsDatasetInfo.
        :type nfs_export_details: NfsExportDetails

        """
        self.swagger_types = {
            'name': 'str',
            'state': 'str',
            'dataset_type': 'str',
            'nfs_export_details': 'NfsExportDetails'
        }

        self.attribute_map = {
            'name': 'name',
            'state': 'state',
            'dataset_type': 'datasetType',
            'nfs_export_details': 'nfsExportDetails'
        }

        self._name = None
        self._state = None
        self._dataset_type = None
        self._nfs_export_details = None

    @property
    def name(self):
        """
        Gets the name of this NfsDatasetInfo.

        :return: The name of this NfsDatasetInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NfsDatasetInfo.

        :param name: The name of this NfsDatasetInfo.
        :type: str
        """
        self._name = name

    @property
    def state(self):
        """
        Gets the state of this NfsDatasetInfo.
        Allowed values for this property are: "INITIALIZED", "ACTIVE", "INACTIVE", "SEALING", "SEALED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The state of this NfsDatasetInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this NfsDatasetInfo.

        :param state: The state of this NfsDatasetInfo.
        :type: str
        """
        allowed_values = ["INITIALIZED", "ACTIVE", "INACTIVE", "SEALING", "SEALED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            state = 'UNKNOWN_ENUM_VALUE'
        self._state = state

    @property
    def dataset_type(self):
        """
        Gets the dataset_type of this NfsDatasetInfo.
        Allowed values for this property are: "NFS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The dataset_type of this NfsDatasetInfo.
        :rtype: str
        """
        return self._dataset_type

    @dataset_type.setter
    def dataset_type(self, dataset_type):
        """
        Sets the dataset_type of this NfsDatasetInfo.

        :param dataset_type: The dataset_type of this NfsDatasetInfo.
        :type: str
        """
        allowed_values = ["NFS"]
        if not value_allowed_none_or_none_sentinel(dataset_type, allowed_values):
            dataset_type = 'UNKNOWN_ENUM_VALUE'
        self._dataset_type = dataset_type

    @property
    def nfs_export_details(self):
        """
        Gets the nfs_export_details of this NfsDatasetInfo.

        :return: The nfs_export_details of this NfsDatasetInfo.
        :rtype: NfsExportDetails
        """
        return self._nfs_export_details

    @nfs_export_details.setter
    def nfs_export_details(self, nfs_export_details):
        """
        Sets the nfs_export_details of this NfsDatasetInfo.

        :param nfs_export_details: The nfs_export_details of this NfsDatasetInfo.
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
