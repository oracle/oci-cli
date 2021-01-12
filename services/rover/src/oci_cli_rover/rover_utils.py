# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click
import six
from oci_cli import cli_util


def get_compute_image_helper(ctx, image_id):

    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')
    ctx_endpoint = ctx.obj['endpoint']
    ctx.obj['endpoint'] = None
    kwargs_request = {
        # 'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    }
    client = cli_util.build_client('core', 'compute', ctx)
    ctx.obj['endpoint'] = ctx_endpoint
    return client.get_image(
        image_id=image_id,
        **kwargs_request
    )


def export_compute_image_helper(ctx, image_id, destinationUri):
    if isinstance(image_id, six.string_types) and len(image_id.strip()) == 0:
        raise click.UsageError('Parameter --image-id cannot be whitespace or empty string')
    export_details = {
        'destinationType': 'objectStorageUri',
        'destinationUri': destinationUri,
    }
    kwargs_request = {
        # 'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    }
    ctx_endpoint = ctx.obj['endpoint']
    ctx.obj['endpoint'] = None
    client = cli_util.build_client('core', 'compute', ctx)
    ctx.obj['endpoint'] = ctx_endpoint
    return client.export_image(
        image_id=image_id,
        export_image_details=export_details,
        **kwargs_request
    )
