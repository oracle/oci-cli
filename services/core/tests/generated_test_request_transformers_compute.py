# coding: utf-8
# Copyright (c) 2019, Oracle and/or its affiliates. All rights reserved.

from tests.generated_test_request_transformers import transformer


# This is a workaround for some logic in the testing service which is supplying
# sourceDetails AND imageId in the same request which is disallowed in the CLI
@transformer('core', 'LaunchInstance')
def _transform_launch_instance_request(request):
    if 'sourceDetails' in request and 'imageId' in request:
        request.pop('imageId')

    return request
