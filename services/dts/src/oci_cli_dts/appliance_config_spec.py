# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


class ApplianceConfigSpec:
    def __init__(self, profile, endpoint, access_token, serial_id):
        self.profile = profile
        self.endpoint = endpoint
        self.access_token = access_token
        self.serial_id = serial_id

    def get_endpoint(self):
        return self.endpoint

    def get_profile(self):
        return self.profile

    def get_access_token(self):
        return self.access_token

    def get_serial_id(self):
        return self.serial_id

    def __str__(self):
        return "ApplianceConfigSpec{profile=%s, endpoint=%s, accessToken='%s', xaSerialId='%s'}" \
               % (self.profile, self.endpoint, self.access_token, self.serial_id)

    def __eq__(self, other):
        if self == other:
            return True
        if other is None or self.__class__.__name__ != other.__class__.__name__:
            return False
        return self.profile == other.profile and self.endpoint == other.endpoint and \
            self.access_token == other.access_token and self.serial_id == other.serial_id

    def __hash__(self):
        return hash(self.profile + self.endpoint + self.access_token + self.serial_id)
