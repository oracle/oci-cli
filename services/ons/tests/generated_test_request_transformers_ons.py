# coding: utf-8
# Copyright (c) 2019, Oracle and/or its affiliates. All rights reserved.

from tests.generated_test_request_transformers import transformer


# The input param needs to be changed as per extended command.
# --endpoint replaced by --subscription-endpoint in this case.
@transformer('ons', 'CreateSubscription')
def _transform_ons_create_subscription_request(request):
    if 'endpoint' in request:
        request['subscriptionEndpoint'] = request.pop('endpoint')

    return request
