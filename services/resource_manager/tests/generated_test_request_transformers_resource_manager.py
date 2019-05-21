# coding: utf-8
# Copyright (c) 2019, Oracle and/or its affiliates. All rights reserved.
import base64
import os
import tempfile

from tests.generated_test_request_transformers import transformer


# The configSource param returned from oci-testing-service are base64
# encoded bytes, which is correct for SDK's. The CLI is expecting a
# path to a zipped file. This transformer function decodes the bytes
# and creates a .zip file to save the decoded data.
@transformer('resource_manager', 'CreateStack')
@transformer('resource_manager', 'UpdateStack')
def _transform_resourcemanager_create_stack_request(request):
    f = None
    if 'configSource' in request:
        source = request.pop('configSource')
        zip_file_base64_encoded = source['zipFileBase64Encoded']
        f = tempfile.NamedTemporaryFile(suffix=".zip", delete=False)
        f.close()
        print(f.name)
        with open(f.name, "wb") as fh:
            fh.write(base64.b64decode(zip_file_base64_encoded.encode()))
        request['configSource'] = f.name
    yield request

    if f is not None:
        if os.path.exists(f.name):
            os.unlink(f.name)
