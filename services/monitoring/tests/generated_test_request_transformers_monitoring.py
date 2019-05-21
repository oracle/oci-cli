# coding: utf-8
# Copyright (c) 2019, Oracle and/or its affiliates. All rights reserved.

from tests.generated_test_request_transformers import transformer


# The input param needs to be changed as per extended command.
# --query replaced by --query-text in this case.
@transformer('monitoring', 'CreateAlarm')
def _transform_monitoring_create_alarm_request(request):
    if 'query' in request:
        request['queryText'] = request.pop('query')

    return request
