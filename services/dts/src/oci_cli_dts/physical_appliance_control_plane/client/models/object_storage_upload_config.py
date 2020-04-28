# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectStorageUploadConfig(object):
    """
    ObjectStorageUploadConfig model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectStorageUploadConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param upload_bucket:
            The value to assign to the upload_bucket property of this ObjectStorageUploadConfig.
        :type upload_bucket: str

        :param overwrite:
            The value to assign to the overwrite property of this ObjectStorageUploadConfig.
        :type overwrite: bool

        :param object_name_prefix:
            The value to assign to the object_name_prefix property of this ObjectStorageUploadConfig.
        :type object_name_prefix: str

        :param upload_summary_object_name:
            The value to assign to the upload_summary_object_name property of this ObjectStorageUploadConfig.
        :type upload_summary_object_name: str

        :param upload_user_oci_config:
            The value to assign to the upload_user_oci_config property of this ObjectStorageUploadConfig.
        :type upload_user_oci_config: str

        :param upload_user_private_key_pem:
            The value to assign to the upload_user_private_key_pem property of this ObjectStorageUploadConfig.
        :type upload_user_private_key_pem: str

        """
        self.swagger_types = {
            'upload_bucket': 'str',
            'overwrite': 'bool',
            'object_name_prefix': 'str',
            'upload_summary_object_name': 'str',
            'upload_user_oci_config': 'str',
            'upload_user_private_key_pem': 'str'
        }

        self.attribute_map = {
            'upload_bucket': 'uploadBucket',
            'overwrite': 'overwrite',
            'object_name_prefix': 'objectNamePrefix',
            'upload_summary_object_name': 'uploadSummaryObjectName',
            'upload_user_oci_config': 'uploadUserOciConfig',
            'upload_user_private_key_pem': 'uploadUserPrivateKeyPem'
        }

        self._upload_bucket = None
        self._overwrite = None
        self._object_name_prefix = None
        self._upload_summary_object_name = None
        self._upload_user_oci_config = None
        self._upload_user_private_key_pem = None

    @property
    def upload_bucket(self):
        """
        Gets the upload_bucket of this ObjectStorageUploadConfig.

        :return: The upload_bucket of this ObjectStorageUploadConfig.
        :rtype: str
        """
        return self._upload_bucket

    @upload_bucket.setter
    def upload_bucket(self, upload_bucket):
        """
        Sets the upload_bucket of this ObjectStorageUploadConfig.

        :param upload_bucket: The upload_bucket of this ObjectStorageUploadConfig.
        :type: str
        """
        self._upload_bucket = upload_bucket

    @property
    def overwrite(self):
        """
        Gets the overwrite of this ObjectStorageUploadConfig.

        :return: The overwrite of this ObjectStorageUploadConfig.
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        """
        Sets the overwrite of this ObjectStorageUploadConfig.

        :param overwrite: The overwrite of this ObjectStorageUploadConfig.
        :type: bool
        """
        self._overwrite = overwrite

    @property
    def object_name_prefix(self):
        """
        Gets the object_name_prefix of this ObjectStorageUploadConfig.

        :return: The object_name_prefix of this ObjectStorageUploadConfig.
        :rtype: str
        """
        return self._object_name_prefix

    @object_name_prefix.setter
    def object_name_prefix(self, object_name_prefix):
        """
        Sets the object_name_prefix of this ObjectStorageUploadConfig.

        :param object_name_prefix: The object_name_prefix of this ObjectStorageUploadConfig.
        :type: str
        """
        self._object_name_prefix = object_name_prefix

    @property
    def upload_summary_object_name(self):
        """
        Gets the upload_summary_object_name of this ObjectStorageUploadConfig.

        :return: The upload_summary_object_name of this ObjectStorageUploadConfig.
        :rtype: str
        """
        return self._upload_summary_object_name

    @upload_summary_object_name.setter
    def upload_summary_object_name(self, upload_summary_object_name):
        """
        Sets the upload_summary_object_name of this ObjectStorageUploadConfig.

        :param upload_summary_object_name: The upload_summary_object_name of this ObjectStorageUploadConfig.
        :type: str
        """
        self._upload_summary_object_name = upload_summary_object_name

    @property
    def upload_user_oci_config(self):
        """
        Gets the upload_user_oci_config of this ObjectStorageUploadConfig.

        :return: The upload_user_oci_config of this ObjectStorageUploadConfig.
        :rtype: str
        """
        return self._upload_user_oci_config

    @upload_user_oci_config.setter
    def upload_user_oci_config(self, upload_user_oci_config):
        """
        Sets the upload_user_oci_config of this ObjectStorageUploadConfig.

        :param upload_user_oci_config: The upload_user_oci_config of this ObjectStorageUploadConfig.
        :type: str
        """
        self._upload_user_oci_config = upload_user_oci_config

    @property
    def upload_user_private_key_pem(self):
        """
        Gets the upload_user_private_key_pem of this ObjectStorageUploadConfig.

        :return: The upload_user_private_key_pem of this ObjectStorageUploadConfig.
        :rtype: str
        """
        return self._upload_user_private_key_pem

    @upload_user_private_key_pem.setter
    def upload_user_private_key_pem(self, upload_user_private_key_pem):
        """
        Sets the upload_user_private_key_pem of this ObjectStorageUploadConfig.

        :param upload_user_private_key_pem: The upload_user_private_key_pem of this ObjectStorageUploadConfig.
        :type: str
        """
        self._upload_user_private_key_pem = upload_user_private_key_pem

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
