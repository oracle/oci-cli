# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NfsExportDetails(object):
    """
    NfsExportDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NfsExportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param export_configs:
            The value to assign to the export_configs property of this NfsExportDetails.
        :type export_configs: list[NfsExportConfig]

        """
        self.swagger_types = {
            'export_configs': 'list[NfsExportConfig]'
        }

        self.attribute_map = {
            'export_configs': 'exportConfigs'
        }

        self._export_configs = None

    @property
    def export_configs(self):
        """
        Gets the export_configs of this NfsExportDetails.

        :return: The export_configs of this NfsExportDetails.
        :rtype: list[NfsExportConfig]
        """
        return self._export_configs

    @export_configs.setter
    def export_configs(self, export_configs):
        """
        Sets the export_configs of this NfsExportDetails.

        :param export_configs: The export_configs of this NfsExportDetails.
        :type: list[NfsExportConfig]
        """
        self._export_configs = export_configs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
