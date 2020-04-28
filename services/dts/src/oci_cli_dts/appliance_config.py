# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


class ApplianceConfig:
    def __init__(self, appliance_url, access_token, serial_id):
        self.appliance_url = appliance_url
        self.access_token = access_token
        self.serial_id = serial_id

    def get_appliance_url(self):
        return self.appliance_url

    def get_access_token(self):
        return self.access_token

    def get_appliance_serial_id(self):
        return self.serial_id

    def __str__(self):
        return "ApplianceConfig{applianceUrl=%s, accessToken='%s', xaSerialId='%s'}" \
               % (self.appliance_url, self.access_token, self.serial_id)

    def __eq__(self, other):
        if self is other:
            return True
        if other is None or self.__class__.__name__ != other.__class__.__name__:
            return False
        return self.appliance_url == other.appliance_url and self.access_token == other.access_token and \
            self.serial_id == other.serial_id

    def __hash__(self):
        return hash(self.appliance_url + self.access_token + self.serial_id)
