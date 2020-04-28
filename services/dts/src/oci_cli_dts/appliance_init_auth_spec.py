# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


class InitAuthSpec:

    def __init__(self, cert_fingerprint, serial_id, appliance_ip, appliance_port, appliance_profile, access_token):
        self.cert_fingerprint = cert_fingerprint
        self.serial_id = serial_id
        self.appliance_ip = appliance_ip
        self.appliance_port = appliance_port
        self.appliance_profile = appliance_profile
        self.access_token = access_token

    def get_cert_fingerprint(self):
        return self.cert_fingerprint

    def get_serial_id(self):
        return self.serial_id

    def get_appliance_profile(self):
        return self.appliance_profile

    def get_appliance_ip(self):
        return self.appliance_ip

    def get_appliance_port(self):
        return self.appliance_port

    def get_access_token(self):
        return self.access_token
