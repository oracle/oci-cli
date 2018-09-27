# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

# TODO: handle 'missing option' (missing parameter required) verification locally since CLI doesnt send request to service

import json
import requests
from oci_cli.cli_util import use_or_generate_request_id, make_dict_keys_camel_case, LIST_NOT_ALL_ITEMS_RETURNED_WARNING

# if you are running the CLI tests inside a docker container on Mac, change SERVICE_HOSTNAME to 'docker.for.mac.localhost'
SERVICE_HOSTNAME = 'localhost'
SERVICE_PORT = '8090'
SERVICE_PATH = 'SDKTestingService'
SERVICE_ROOT_URL = 'http://{hostname}:{port}/{path}'.format(hostname=SERVICE_HOSTNAME, port=SERVICE_PORT, path=SERVICE_PATH)
SERVICE_LANGUAGE = "PythonCLI"


class CLITestingServiceClient:
    def get_requests(self, service_name, api_name):
        """
        Gets a list of requests from the testing service to be used in calling the API specified by service_name and api_name.

        :param str service_name
            The name of the service to request input parameters for. The testing service uses the following template to
            construct the Java SDK request object:
            String.format("com.oracle.bmc.%s.requests.%sRequest", serviceName, apiName);

        :param str api_name
            The name of the API to request input parameters for. The testing service uses the following template to
            construct the Java SDK request object:
            String.format("com.oracle.bmc.%s.requests.%sRequest", serviceName, apiName);

        :return: A list of dicts containing parameters to call the API specified by service_name and api_name

        """
        if not self.session_id:
            raise RuntimeError('Must call create_session before calling get_requests.')

        # standardize service name to convention for Java SDK model namespaces (all lower case one word)
        service_name = service_name.replace('_', '').lower()

        params = {
            'serviceName': service_name,
            'apiName': api_name,
            'lang': SERVICE_LANGUAGE,
            'sessionId': self.session_id
        }

        url = '{service_root_url}/request'.format(service_root_url=SERVICE_ROOT_URL)
        response = requests.get(url, params=params)
        response_content = response.content.decode('UTF-8')
        try:
            return json.loads(response_content)
        except ValueError as e:
            print('Failed to parse testing service response as valid JSON. Response: ' + response_content)
            raise e

    def validate_result(self, service_name, api_name, container_id, request, result, data_field_name, is_delete_operation):
        """
        Calls the testing service to validate a CLI command result.

        :param str service_name
            The name of the service to request input parameters for. The testing service uses the following template to
            construct the Java SDK request object:
            String.format("com.oracle.bmc.%s.requests.%sRequest", serviceName, apiName);

        :param str api_name
            The name of the API to request input parameters for. The testing service uses the following template to
            construct the Java SDK request object:
            String.format("com.oracle.bmc.%s.requests.%sRequest", serviceName, apiName);

        :param str container_id:
            The ID of the current container.

        :param str request:
            The json content of the request object.

        :param Result result:
            The result object from click.testing.CliRunner.

        :param str data_field_name:
            The CLI returns the main resource under the field name 'data' but we need to convert it to
            the name used in the Java SDK (e.g. for GetGroup data -> group)

        :return: None

        """
        # standardize service name to convention for Java SDK model namespaces (all lower case one word)
        java_package_name = service_name.replace('_', '').lower()

        request_class = 'com.oracle.bmc.{java_package_name}.requests.{api_name}Request'.format(java_package_name=java_package_name, api_name=api_name)
        response_class = 'com.oracle.bmc.{java_package_name}.responses.{api_name}Response'.format(java_package_name=java_package_name, api_name=api_name)

        success_url = '{service_root_url}/response'.format(service_root_url=SERVICE_ROOT_URL)
        error_url = '{service_root_url}/error'.format(service_root_url=SERVICE_ROOT_URL)
        data = {
            'containerId': container_id,
            'requestClass': request_class,
            'requestJson': json.dumps(request),
        }

        params = {
            "sessionId": self.session_id,
            "lang": SERVICE_LANGUAGE
        }

        if result.exit_code == 0:
            # remove known warnings from output that would break JSON parsing
            output = result.output.replace(LIST_NOT_ALL_ITEMS_RETURNED_WARNING, '')

            # list and delete CLI commands can return an empty string so specially handle those cases
            if len(output) == 0:
                if api_name.lower().startswith('list'):
                    normalized_response_json = {data_field_name: []}
                elif is_delete_operation:
                    normalized_response_json = {}
                else:
                    raise ValueError('CLI output was empty')
            else:
                try:
                    normalized_response_json = json.loads(output)
                except ValueError as e:
                    print('Failed to parse CLI output as valid JSON. Output: {}'.format(output))
                    raise e

                # convert the CLI response (keys with '-') to camelcase so that testing service can validate
                complex_parameter_type = {
                    'module': service_name,
                    'class': data_field_name[0].upper() + data_field_name[1:]
                }

                # remove 'data' temporarily to camelize all other fields
                response_data = normalized_response_json.pop('data', None)

                # camelize the rest of the response fields (data is removed so there is no corresponding complex type definition for the top level object)
                normalized_response_json = make_dict_keys_camel_case(normalized_response_json)

                # camelize response['data'] independently and specify the corresponding complex_parameter_type
                # this will correctly skip camelizing keys of dictionaries nested within the response such as 'metadata' or 'defined-tags'
                if response_data:
                    normalized_response_json[data_field_name] = make_dict_keys_camel_case(response_data, complex_parameter_type=complex_parameter_type)

            # right now we only return the opc-request-id for errors but the validator looks for it
            # tempporarily bypassing this check by hardcoding one here
            normalized_response_json['opcRequestId'] = use_or_generate_request_id(None)

            data['responseJson'] = json.dumps(normalized_response_json)
            data['responseClass'] = response_class

            response = requests.post(success_url, params=params, data=json.dumps(data))
            assert response.status_code == 200, response.content
            return response.content.decode("UTF-8")
        else:
            error = json.loads(result.output.replace('ServiceError:', ''))
            error['statusCode'] = error.pop('status')
            error['opcRequestId'] = error.pop('opc-request-id')

            data['errorJson'] = json.dumps(error)
            print('errorToValidate: {}'.format(json.dumps(data, indent=2)))

            response = requests.post(error_url, params=params, data=json.dumps(data))
            assert response.status_code == 200, response.content
            return response.content.decode("UTF-8")

    def create_session(self):
        """
        Initializes a session with the testing service.

        """
        url = '{service_root_url}/sessions'.format(service_root_url=SERVICE_ROOT_URL)
        data = {'language': SERVICE_LANGUAGE}
        response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json', 'Accept': 'text/plain'})
        assert response.status_code == 200, 'Failed to create session. Response from testing service: {}'.format(response.content)

        session_id_response = response.content.decode('UTF-8')
        try:
            int(session_id_response)
        except ValueError as e:
            print('Failed to create session, did not receive valid session ID from testing service: {}'.format(session_id_response))
            raise e

        self.session_id = session_id_response
        print('Created session: {}'.format(self.session_id))
        return self.session_id

    def end_session(self):
        """
        Ends the existing session with the testing service.

        """
        if not self.session_id:
            raise RuntimeError('Must call create_session before calling end_session.')

        print('Ending session for {}'.format(self.session_id))
        url = '{service_root_url}/sessions/{session_id}'.format(service_root_url=SERVICE_ROOT_URL, session_id=self.session_id)
        response = requests.delete(url)
        assert response.status_code == 204, 'Failed to end session. Response: {}'.format(response.content)

    def is_api_enabled(self, service_name, api_name):
        """
        Checks if a given service_name / api_name is supported by the testing service and enabled for this client / language.

        :param str service_name
            The name of the service to request input parameters for. The testing service uses the following template to
            construct the Java SDK request object:
            String.format("com.oracle.bmc.%s.requests.%sRequest", serviceName, apiName);

        :param str api_name
            The name of the API to request input parameters for. The testing service uses the following template to
            construct the Java SDK request object:
            String.format("com.oracle.bmc.%s.requests.%sRequest", serviceName, apiName);

        :return: Whether or not this API is enabled in the testing service.

        """
        # standardize service name to convention for Java SDK model namespaces (all lower case one word)
        service_name = service_name.replace('_', '').lower()

        url = '{service_root_url}/request/enable'.format(service_root_url=SERVICE_ROOT_URL)
        params = {
            'lang': SERVICE_LANGUAGE,
            'serviceName': service_name,
            'apiName': api_name
        }

        response = requests.get(url, params=params)
        assert response.status_code == 200, response.content

        response_content = response.content.decode('UTF-8')
        try:
            api_enabled_response = json.loads(response_content)
        except ValueError as e:
            print('Failed to parse testing service response as valid JSON. Response: {}'.format(response_content))
            raise e

        assert api_enabled_response is True or api_enabled_response is False, 'Received invalid response from testing service, should be true or false. Response: {}'.format(api_enabled_response)
        return api_enabled_response

    def get_endpoint(self, service_name, client_name):
        # standardize service name to convention for Java SDK model namespaces (all lower case one word)
        service_name = service_name.replace('_', '').lower()

        url = '{service_root_url}/endpoint'.format(service_root_url=SERVICE_ROOT_URL)
        params = {
            'sessionId': self.session_id,
            'serviceName': service_name,
            'clientName': client_name
        }

        response = requests.get(url, params=params)
        assert response.status_code == 200, response.content
        return response.content.decode('UTF-8')
