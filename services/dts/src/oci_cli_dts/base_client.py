# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

try:
    from oci._vendor.requests.packages.urllib2.poolmanager import PoolManager
except Exception as e:
    from oci._vendor.requests.packages.urllib3.poolmanager import PoolManager

import six

from oci import exceptions
from oci.response import Response
from oci.request import Request

import json
import logging


class BaseClient(object):
    def __init__(self, service, config, signer, type_mapping, **kwargs):
        self._config = config
        self._signer = signer

        self._base_path = kwargs.get('base_path')

        if kwargs.get('service_endpoint'):
            self._endpoint = kwargs.get('service_endpoint')
        else:
            raise Exception("The service_endpoint has to be provided")

        self.service = service
        self.complex_type_mappings = type_mapping
        self.pool_manager = PoolManager(ca_certs=kwargs.get('self_signed_cert'), assert_hostname=False)
        self.timeout = kwargs.get('timeout')

        self.logger = logging.getLogger("{}.{}".format(__name__, id(self)))
        self.logger.addHandler(logging.NullHandler())

        self.skip_deserialization = kwargs.get('skip_deserialization')

    def call_api(self, resource_path, method,
                 path_params=None, query_params=None, header_params=None,
                 body=None, response_type=None, enforce_content_headers=True):
        """
        Makes the HTTP request and return the deserialized data.

        :param resource_path: Path to the resource (e.g. /instance)
        :param method: HTTP method
        :param path_params: (optional) Path parameters in the url.
        :param query_params: (optional) Query parameters in the url.
        :param header_params: (optional) Request header params.
        :param body: (optional) Request body.
        :param response_type: (optional) Response data type.
        :param enforce_content_headers: (optional) Whether content headers should be added for
            PUT and POST requests when not present.  Defaults to True.
        :return: A Response object, or throw in the case of an error.

        """

        if path_params is not None:
            for k, v in path_params.items():
                replacement = six.moves.urllib.parse.quote(v)
                resource_path = resource_path.\
                    replace('{' + k + '}', replacement)

        response = self.pool_manager.request(method,
                                             '{}{}{}'.format(self._endpoint, self._base_path, resource_path),
                                             body=json.dumps(body),
                                             headers=header_params)

        request = Request(
            method=method,
            url=self._endpoint + self._base_path + resource_path,
            query_params=query_params,
            header_params=header_params,
            body=body,
            response_type=response_type,
            enforce_content_headers=enforce_content_headers
        )
        if not 200 <= response.status <= 299:
            raise exceptions.ServiceError(
                response.status,
                None,
                response.headers,
                str(response.data),
                original_request=request)

        data = response.data
        try:
            data = json.loads(response.data.decode("utf-8"))
        except Exception as e:
            pass
        return Response(response.status, dict(response.getheaders()), data, request)
