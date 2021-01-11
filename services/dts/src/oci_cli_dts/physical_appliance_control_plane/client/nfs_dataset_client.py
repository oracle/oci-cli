# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry  # noqa: F401
from services.dts.src.oci_cli_dts.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel
from .models import client_type_mapping
missing = Sentinel("Missing")


class NfsDatasetClient(object):
    """
    A description of the XACP API
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default is that the client never times out. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.cloud.oracle.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
            by passing an instance of :py:class:`~oci.auth.signers.InstancePrincipalsSecurityTokenSigner` as the value for this keyword argument
        :type signer: :py:class:`~oci.signer.AbstractBaseSigner`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to all calls made by this service client (i.e. at the client level). There is no retry strategy applied by default.
            Retry strategies can also be applied at the operation level by passing a ``retry_strategy`` keyword argument as part of calling the operation.
            Any value provided at the operation level will override whatever is specified at the client level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.
        """
        validate_config(config, signer=kwargs.get('signer'))
        if 'signer' in kwargs:
            signer = kwargs['signer']
        else:
            signer = Signer(
                tenancy=config["tenancy"],
                user=config["user"],
                fingerprint=config["fingerprint"],
                private_key_file_location=config.get("key_file"),
                pass_phrase=get_config_value_or_default(config, "pass_phrase"),
                private_key_content=config.get("key_content")
            )

        base_client_init_kwargs = {
            'regional_client': True,
            'service_endpoint': kwargs.get('service_endpoint'),
            'timeout': kwargs.get('timeout'),
            'base_path': '/20180301',
            'skip_deserialization': kwargs.get('skip_deserialization', False),
            'self_signed_cert': kwargs.get('self_signed_cert')
        }
        self.base_client = BaseClient("nfs_dataset", config, signer, client_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def activate_nfs_dataset(self, dataset_name, **kwargs):
        """
        Activates the NFS dataset
        Activates the NFS dataset


        :param str dataset_name: (required)

        :param Details details: (optional)

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dataset/nfs/{datasetName}/activate"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "details",
            "auth_value",
            "serial_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "activate_nfs_dataset got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "datasetName": dataset_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "xa-auth": kwargs.get('auth_value'),
            "xa-serial-id": kwargs.get('serial_id')
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=kwargs.get('details'))
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=kwargs.get('details'))

    def create_nfs_dataset(self, details, **kwargs):
        """
        Creates a NFS dataset
        Creates a NFS dataset


        :param NfsDatasetSpec details: (required)

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.client.models.NfsDatasetInfo`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dataset/nfs"
        method = "POST"

        expected_kwargs = [
            "retry_strategy",
            "auth_value",
            "serial_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_nfs_dataset got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "xa-auth": kwargs.get('auth_value'),
            "xa-serial-id": kwargs.get('serial_id')
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=details,
                response_type="NfsDatasetInfo")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=details,
                response_type="NfsDatasetInfo")

    def deactivate_nfs_dataset(self, dataset_name, **kwargs):
        """
        Deactivates the NFS dataset
        Deactivates the NFS dataset


        :param str dataset_name: (required)

        :param Details details: (optional)

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dataset/nfs/{datasetName}/deactivate"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "details",
            "auth_value",
            "serial_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "deactivate_nfs_dataset got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "datasetName": dataset_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "xa-auth": kwargs.get('auth_value'),
            "xa-serial-id": kwargs.get('serial_id')
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=kwargs.get('details'))
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=kwargs.get('details'))

    def delete_nfs_dataset(self, dataset_name, **kwargs):
        """
        Deletes the NFS dataset
        Deletes the NFS dataset


        :param str dataset_name: (required)

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dataset/nfs/{datasetName}"
        method = "DELETE"

        expected_kwargs = [
            "retry_strategy",
            "auth_value",
            "serial_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_nfs_dataset got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "datasetName": dataset_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "xa-auth": kwargs.get('auth_value'),
            "xa-serial-id": kwargs.get('serial_id')
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def get_nfs_dataset(self, dataset_name, **kwargs):
        """
        Gets the NFS dataset details
        Gets the NFS dataset details


        :param str dataset_name: (required)

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.client.models.NfsDatasetInfo`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dataset/nfs/{datasetName}"
        method = "GET"

        expected_kwargs = [
            "retry_strategy",
            "auth_value",
            "serial_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_nfs_dataset got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "datasetName": dataset_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "xa-auth": kwargs.get('auth_value'),
            "xa-serial-id": kwargs.get('serial_id')
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="NfsDatasetInfo")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="NfsDatasetInfo")

    def get_nfs_dataset_seal_manifest(self, dataset_name, **kwargs):
        """
        Streams the manifest file for the sealed NFS dataset
        Streams the manifest file for the sealed NFS dataset


        :param str dataset_name: (required)

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type stream
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dataset/nfs/{datasetName}/sealManifest"
        method = "GET"

        expected_kwargs = [
            "retry_strategy",
            "auth_value",
            "serial_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_nfs_dataset_seal_manifest got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "datasetName": dataset_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "text/plain; charset=utf-8",
            "content-type": "application/json",
            "xa-auth": kwargs.get('auth_value'),
            "xa-serial-id": kwargs.get('serial_id')
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="stream")

    def get_nfs_dataset_seal_status(self, dataset_name, **kwargs):
        """
        Returns the seal status for the NFS dataset
        Returns the seal status for the NFS dataset


        :param str dataset_name: (required)

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.client.models.DatasetSealStatus`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dataset/nfs/{datasetName}/sealStatus"
        method = "GET"

        expected_kwargs = [
            "retry_strategy",
            "auth_value",
            "serial_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_nfs_dataset_seal_status got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "datasetName": dataset_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "xa-auth": kwargs.get('auth_value'),
            "xa-serial-id": kwargs.get('serial_id')
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DatasetSealStatus")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DatasetSealStatus")

    def initiate_seal_on_nfs_dataset(self, dataset_name, **kwargs):
        """
        Initiates seal on the NFS dataset
        Initiates seal on the NFS dataset


        :param str dataset_name: (required)

        :param Details details: (optional)

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dataset/nfs/{datasetName}/initiateSeal"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "details",
            "auth_value",
            "serial_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "initiate_seal_on_nfs_dataset got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "datasetName": dataset_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "xa-auth": kwargs.get('auth_value'),
            "xa-serial-id": kwargs.get('serial_id')
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=kwargs.get('details'))
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=kwargs.get('details'))

    def list_nfs_datasets(self, **kwargs):
        """
        Lists NFS datasets
        Lists NFS datasets


        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.client.models.NfsDatasetInfo`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dataset/nfs"
        method = "GET"

        expected_kwargs = [
            "retry_strategy",
            "auth_value",
            "serial_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_nfs_datasets got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "xa-auth": kwargs.get('auth_value'),
            "xa-serial-id": kwargs.get('serial_id')
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                response_type="list[NfsDatasetInfo]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                response_type="list[NfsDatasetInfo]")

    def reopen_nfs_dataset(self, dataset_name, **kwargs):
        """
        Reopens the sealed NFS dataset
        Reopens the sealed NFS dataset


        :param str dataset_name: (required)

        :param Details details: (optional)

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dataset/nfs/{datasetName}/reopen"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "details",
            "auth_value",
            "serial_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "reopen_nfs_dataset got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "datasetName": dataset_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "xa-auth": kwargs.get('auth_value'),
            "xa-serial-id": kwargs.get('serial_id')
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=kwargs.get('details'))
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=kwargs.get('details'))

    def update_nfs_dataset(self, dataset_name, body, **kwargs):
        """
        Updates the NFS dataset
        Updates the NFS dataset


        :param str dataset_name: (required)

        :param NfsDatasetSpec body: (required)

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.client.models.NfsDatasetInfo`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dataset/nfs/{datasetName}"
        method = "PUT"

        expected_kwargs = [
            "retry_strategy",
            "auth_value",
            "serial_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_nfs_dataset got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "datasetName": dataset_name
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "xa-auth": kwargs.get('auth_value'),
            "xa-serial-id": kwargs.get('serial_id')
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=body,
                response_type="NfsDatasetInfo")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=body,
                response_type="NfsDatasetInfo")
