# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click  # noqa: F401
import json  # noqa: F401
from services.globally_distributed_database.src.oci_cli_sharded_database_service.generated import shardeddatabaseservice_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401


# Remove create from oci globally-distributed-database sharded-database
shardeddatabaseservice_cli.sharded_database_group.commands.pop(shardeddatabaseservice_cli.create_sharded_database.name)


# Remove fetch-shardable-cloud-autonomous-vm-clusters from oci globally-distributed-database sharded-database
shardeddatabaseservice_cli.sharded_database_group.commands.pop(shardeddatabaseservice_cli.fetch_shardable_cloud_autonomous_vm_clusters.name)


# Remove prevalidate from oci globally-distributed-database sharded-database
shardeddatabaseservice_cli.sharded_database_group.commands.pop(shardeddatabaseservice_cli.prevalidate_sharded_database.name)


# Remove prevalidate-sharded-database-prevalidate-create-payload from oci globally-distributed-database sharded-database
shardeddatabaseservice_cli.sharded_database_group.commands.pop(shardeddatabaseservice_cli.prevalidate_sharded_database_prevalidate_create_payload.name)


# Remove prevalidate-sharded-database-prevalidate-patch-payload from oci globally-distributed-database sharded-database
shardeddatabaseservice_cli.sharded_database_group.commands.pop(shardeddatabaseservice_cli.prevalidate_sharded_database_prevalidate_patch_payload.name)


# Remove validate-network from oci globally-distributed-database sharded-database
shardeddatabaseservice_cli.sharded_database_group.commands.pop(shardeddatabaseservice_cli.validate_network.name)


@cli_util.copy_params_from_generated_command(shardeddatabaseservice_cli.upload_signed_certificate_and_generate_wallet, params_to_exclude=['ca_signed_certificate'])
@shardeddatabaseservice_cli.sharded_database_group.command(name=cli_util.override('gdd.upload_signed_certificate_and_generate_wallet.command_name', 'upload-signed-certificate-and-generate-wallet'), help=u"""Upload the CA signed certificate to the GSM instances and generate wallets for GSM instances of the sharded database. Customer shall provide the CA signed certificate key details by adding the certificate in request body. \n[Command Reference](uploadSignedCertificateAndGenerateWallet)""")
@cli_util.option('--ca-signed-certificate-file', required=True, type=click.File('r'), help=u"""A file containing CA signed certificate.""")
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def upload_signed_certificate_and_generate_wallet_extended(ctx, **kwargs):

    # Set "--ca-signed-certificate" to the content of file "--ca-signed-certificate-file"
    if 'ca_signed_certificate_file' in kwargs and kwargs['ca_signed_certificate_file']:
        kwargs['ca_signed_certificate'] = kwargs.get('ca_signed_certificate_file').read()

    # Remove the extram parameters not expected on base method "upload_signed_certificate_and_generate_wallet".
    del kwargs['ca_signed_certificate_file']

    # Invoke base method "upload_signed_certificate_and_generate_wallet"
    ctx.invoke(shardeddatabaseservice_cli.upload_signed_certificate_and_generate_wallet, **kwargs)
