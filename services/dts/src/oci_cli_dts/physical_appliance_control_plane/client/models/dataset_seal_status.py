# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatasetSealStatus(object):
    """
    DatasetSealStatus model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatasetSealStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param completed:
            The value to assign to the completed property of this DatasetSealStatus.
        :type completed: bool

        :param success:
            The value to assign to the success property of this DatasetSealStatus.
        :type success: bool

        :param failure_reason:
            The value to assign to the failure_reason property of this DatasetSealStatus.
        :type failure_reason: str

        :param start_time_in_ms:
            The value to assign to the start_time_in_ms property of this DatasetSealStatus.
        :type start_time_in_ms: int

        :param end_time_in_ms:
            The value to assign to the end_time_in_ms property of this DatasetSealStatus.
        :type end_time_in_ms: int

        :param num_files_to_process:
            The value to assign to the num_files_to_process property of this DatasetSealStatus.
        :type num_files_to_process: int

        :param num_files_processed:
            The value to assign to the num_files_processed property of this DatasetSealStatus.
        :type num_files_processed: int

        :param bytes_to_process:
            The value to assign to the bytes_to_process property of this DatasetSealStatus.
        :type bytes_to_process: int

        :param bytes_processed:
            The value to assign to the bytes_processed property of this DatasetSealStatus.
        :type bytes_processed: int

        """
        self.swagger_types = {
            'completed': 'bool',
            'success': 'bool',
            'failure_reason': 'str',
            'start_time_in_ms': 'int',
            'end_time_in_ms': 'int',
            'num_files_to_process': 'int',
            'num_files_processed': 'int',
            'bytes_to_process': 'int',
            'bytes_processed': 'int'
        }

        self.attribute_map = {
            'completed': 'completed',
            'success': 'success',
            'failure_reason': 'failureReason',
            'start_time_in_ms': 'startTimeInMs',
            'end_time_in_ms': 'endTimeInMs',
            'num_files_to_process': 'numFilesToProcess',
            'num_files_processed': 'numFilesProcessed',
            'bytes_to_process': 'bytesToProcess',
            'bytes_processed': 'bytesProcessed'
        }

        self._completed = None
        self._success = None
        self._failure_reason = None
        self._start_time_in_ms = None
        self._end_time_in_ms = None
        self._num_files_to_process = None
        self._num_files_processed = None
        self._bytes_to_process = None
        self._bytes_processed = None

    @property
    def completed(self):
        """
        Gets the completed of this DatasetSealStatus.

        :return: The completed of this DatasetSealStatus.
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """
        Sets the completed of this DatasetSealStatus.

        :param completed: The completed of this DatasetSealStatus.
        :type: bool
        """
        self._completed = completed

    @property
    def success(self):
        """
        Gets the success of this DatasetSealStatus.

        :return: The success of this DatasetSealStatus.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this DatasetSealStatus.

        :param success: The success of this DatasetSealStatus.
        :type: bool
        """
        self._success = success

    @property
    def failure_reason(self):
        """
        Gets the failure_reason of this DatasetSealStatus.

        :return: The failure_reason of this DatasetSealStatus.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """
        Sets the failure_reason of this DatasetSealStatus.

        :param failure_reason: The failure_reason of this DatasetSealStatus.
        :type: str
        """
        self._failure_reason = failure_reason

    @property
    def start_time_in_ms(self):
        """
        Gets the start_time_in_ms of this DatasetSealStatus.

        :return: The start_time_in_ms of this DatasetSealStatus.
        :rtype: int
        """
        return self._start_time_in_ms

    @start_time_in_ms.setter
    def start_time_in_ms(self, start_time_in_ms):
        """
        Sets the start_time_in_ms of this DatasetSealStatus.

        :param start_time_in_ms: The start_time_in_ms of this DatasetSealStatus.
        :type: int
        """
        self._start_time_in_ms = start_time_in_ms

    @property
    def end_time_in_ms(self):
        """
        Gets the end_time_in_ms of this DatasetSealStatus.

        :return: The end_time_in_ms of this DatasetSealStatus.
        :rtype: int
        """
        return self._end_time_in_ms

    @end_time_in_ms.setter
    def end_time_in_ms(self, end_time_in_ms):
        """
        Sets the end_time_in_ms of this DatasetSealStatus.

        :param end_time_in_ms: The end_time_in_ms of this DatasetSealStatus.
        :type: int
        """
        self._end_time_in_ms = end_time_in_ms

    @property
    def num_files_to_process(self):
        """
        Gets the num_files_to_process of this DatasetSealStatus.

        :return: The num_files_to_process of this DatasetSealStatus.
        :rtype: int
        """
        return self._num_files_to_process

    @num_files_to_process.setter
    def num_files_to_process(self, num_files_to_process):
        """
        Sets the num_files_to_process of this DatasetSealStatus.

        :param num_files_to_process: The num_files_to_process of this DatasetSealStatus.
        :type: int
        """
        self._num_files_to_process = num_files_to_process

    @property
    def num_files_processed(self):
        """
        Gets the num_files_processed of this DatasetSealStatus.

        :return: The num_files_processed of this DatasetSealStatus.
        :rtype: int
        """
        return self._num_files_processed

    @num_files_processed.setter
    def num_files_processed(self, num_files_processed):
        """
        Sets the num_files_processed of this DatasetSealStatus.

        :param num_files_processed: The num_files_processed of this DatasetSealStatus.
        :type: int
        """
        self._num_files_processed = num_files_processed

    @property
    def bytes_to_process(self):
        """
        Gets the bytes_to_process of this DatasetSealStatus.

        :return: The bytes_to_process of this DatasetSealStatus.
        :rtype: int
        """
        return self._bytes_to_process

    @bytes_to_process.setter
    def bytes_to_process(self, bytes_to_process):
        """
        Sets the bytes_to_process of this DatasetSealStatus.

        :param bytes_to_process: The bytes_to_process of this DatasetSealStatus.
        :type: int
        """
        self._bytes_to_process = bytes_to_process

    @property
    def bytes_processed(self):
        """
        Gets the bytes_processed of this DatasetSealStatus.

        :return: The bytes_processed of this DatasetSealStatus.
        :rtype: int
        """
        return self._bytes_processed

    @bytes_processed.setter
    def bytes_processed(self, bytes_processed):
        """
        Sets the bytes_processed of this DatasetSealStatus.

        :param bytes_processed: The bytes_processed of this DatasetSealStatus.
        :type: int
        """
        self._bytes_processed = bytes_processed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
