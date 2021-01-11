# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


import OpenSSL
import ssl

from oci import exceptions


class ApplianceCertManager:
    def __init__(self, appliance_endpoint):
        """
        This is where all the action happens. This manager is responsible for getting the certificates from the
        appliance and validating them
        :param appliance_endpoint: The endpoint of the appliance in the form of (ip, port)
        """
        self.appliance_endpoint = appliance_endpoint

    def fetch_cert(self, cert_file):
        """
        Pull certificate from appliance (SSL server) and store in local appliance certificate file in PEM format
        :param cert_file: The String path to the cert file
        :return: None
        """
        ssl_cert = ssl.get_server_certificate(self.appliance_endpoint)
        with open(cert_file, 'w') as f:
            f.write(ssl_cert)

    @staticmethod
    def validate_cert(cert_file, expected_cert_fingerprint):
        """
        Validate whether the fingerprint of the cert file matches what the user provided
        :param cert_file: String path to the server certificate
        :param expected_cert_fingerprint: String certificate fingerprint that the user provided
        :return: None
        """
        ssl_cert = open(cert_file, 'rt').read()
        x509_cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, ssl_cert)
        server_fingerprint = x509_cert.digest("md5")
        if type(expected_cert_fingerprint) == bytes:
            expected_cert_fingerprint = expected_cert_fingerprint.decode("utf-8")
        if server_fingerprint.decode("utf-8") != expected_cert_fingerprint:
            raise exceptions.RequestException(
                "Provided cert fingerprint does not match what was returned by the appliance")
