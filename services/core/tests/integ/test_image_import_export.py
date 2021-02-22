# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import json
from tests import util
import oci
from tests import test_config_container

CASSETTE_LIBRARY_DIR = 'services/core/tests/cassettes'


class TestImageImportExport(object):

    @util.long_running
    def test_image_import_export(self, config):
        the_vcr = test_config_container.create_vcr(cassette_library_dir=CASSETTE_LIBRARY_DIR)
        with the_vcr.use_cassette('compute_test_image_import_export.yml'):
            try:
                self.set_up_resources()
                self.subtest_image_import_export_via_tuple()
                self.subtest_image_import_export_via_uri(config)
                self.subtest_image_export_via_tuple_with_export_format_specified()
                self.subtest_image_export_via_uri_with_export_format_specified(config)
                # self.subtest_image_import_export_via_preauthenticated_url(config)
            finally:
                self.clean_up_resources()

    def subtest_image_import_export_via_tuple(self):
        self.export_via_tuple_object_name = 'export-via-tuple'

        result = self.invoke(
            ['compute', 'image', 'export', 'to-object',
             '--image-id', self.custom_image_id,
             '--namespace', self.object_storage_namespace,
             '--bucket-name', self.bucket_name,
             '--name', self.export_via_tuple_object_name])
        image_details = json.loads(result.output)
        assert self.custom_image_id == image_details['data']['id']
        assert image_details['data']['lifecycle-state'] == 'EXPORTING'

        util.wait_until(['compute', 'image', 'get', '--image-id', self.custom_image_id], 'AVAILABLE', max_wait_seconds=3600)

        result = self.invoke(
            ['compute', 'image', 'import', 'from-object',
             '--compartment-id', util.COMPARTMENT_ID,
             '--display-name', 'Imported from object storage tuple',
             '--namespace', self.object_storage_namespace,
             '--bucket-name', self.bucket_name,
             '--name', self.export_via_tuple_object_name])
        print(result.output)
        image_details = json.loads(result.output)
        self.imported_image_from_tuple_id = image_details['data']['id']
        assert self.imported_image_from_tuple_id is not None
        assert image_details['data']['lifecycle-state'] == 'IMPORTING'
        assert image_details['data']['display-name'] == 'Imported from object storage tuple'

        util.wait_until(['compute', 'image', 'get', '--image-id', self.imported_image_from_tuple_id], 'AVAILABLE', max_wait_seconds=3600)

    def subtest_image_import_export_via_uri(self, config):
        self.export_via_uri_object_name = 'export-via-uri'
        object_uri = '{}/n/{}/b/{}/o/{}'.format(
            oci.regions.endpoint_for('object_storage', config['region']),
            self.object_storage_namespace,
            self.bucket_name,
            self.export_via_uri_object_name)

        result = self.invoke(
            ['compute', 'image', 'export', 'to-object-uri',
             '--image-id', self.custom_image_id,
             '--uri', object_uri])
        image_details = json.loads(result.output)
        assert self.custom_image_id == image_details['data']['id']
        assert image_details['data']['lifecycle-state'] == 'EXPORTING'

        util.wait_until(['compute', 'image', 'get', '--image-id', self.custom_image_id], 'AVAILABLE', max_wait_seconds=3600)

        result = self.invoke(
            ['compute', 'image', 'import', 'from-object-uri',
             '--compartment-id', util.COMPARTMENT_ID,
             '--display-name', 'Imported from object storage uri',
             '--uri', object_uri])
        image_details = json.loads(result.output)
        self.imported_image_from_uri_id = image_details['data']['id']
        assert self.imported_image_from_uri_id is not None
        assert image_details['data']['lifecycle-state'] == 'IMPORTING'
        assert image_details['data']['display-name'] == 'Imported from object storage uri'

        # Create a pre-authenticated request against the object so that we can import it
        result = self.invoke(
            ['os', 'preauth-request', 'create',
             '--namespace', self.object_storage_namespace,
             '--bucket-name', self.bucket_name,
             '--object-name', self.export_via_uri_object_name,
             '--name', 'preauth-object',
             '--access-type', 'ObjectRead',
             '--time-expires', '9999-12-31T00:00:00.000+00:00'])
        par_details = json.loads(result.output)
        self.object_par_id = par_details['data']['id']

        # The access-uri in the response looks like:
        #    /p/...../n/mytenancy/b/A_CliImportExportBucket/o/test_export_1
        #
        # So we need to prepend the domain only (as the URI references the object alreadt)
        object_par_access_uri = '{}{}'.format(oci.regions.endpoint_for('object_storage', config['region']), par_details['data']['access-uri'])

        result = self.invoke(
            ['compute', 'image', 'import', 'from-object-uri',
             '--compartment-id', util.COMPARTMENT_ID,
             '--display-name', 'Imported from object storage par',
             '--uri', object_par_access_uri])
        image_details = json.loads(result.output)
        self.imported_image_from_par_id = image_details['data']['id']
        assert self.imported_image_from_par_id is not None
        assert image_details['data']['lifecycle-state'] == 'IMPORTING'
        assert image_details['data']['display-name'] == 'Imported from object storage par'

        util.wait_until(['compute', 'image', 'get', '--image-id', self.imported_image_from_uri_id], 'AVAILABLE', max_wait_seconds=3600)
        util.wait_until(['compute', 'image', 'get', '--image-id', self.imported_image_from_par_id], 'AVAILABLE', max_wait_seconds=3600)

    # This test is intended to do the lifecyle of exporting an image to a bucket pre-authenticated request (PAR) and
    # then importing it via an object PAR.
    #
    # This test is currently not used as exporting to a PAR leaves the image in the EXPORTING state for a long time
    # and so we don't execute it to keep test run times down
    #
    # def subtest_image_import_export_via_preauthenticated_url(self, config):
    #     # par == pre-authenticated request
    #     self.export_via_par_object_name = 'export-via-par'
    #
    #     # Create a pre-authenticated request against the bucket so that we can shove in objects
    #     result = self.invoke(
    #         ['os', 'preauth-request', 'create',
    #          '--namespace', self.object_storage_namespace,
    #          '--bucket-name', self.bucket_name,
    #          '--name', 'preauth-bucket',
    #          '--access-type', 'AnyObjectWrite',
    #          '--time-expires', '9999-12-31T00:00:00.000+00:00'])
    #     par_details = json.loads(result.output)
    #     self.bucket_par_id = par_details['data']['id']

    #     # The access-uri in the response looks like:
    #     #    /p/...../n/mytenancy/b/A_CliImportExportBucket/o/
    #     #
    #     # So we need to prepend the domain and append the object name in order to put something in the bucket
    #     bucket_par_access_uri = '{}{}{}'.format(
    #         oci.regions.endpoint_for('object_storage', config['region']),
    #         par_details['data']['access-uri'],
    #         self.export_via_par_object_name)

    #     result = self.invoke(
    #         ['compute', 'image', 'export', 'to-object-uri',
    #          '--image-id', self.custom_image_id,
    #          '--uri', bucket_par_access_uri])
    #     image_details = json.loads(result.output)
    #     assert self.custom_image_id == image_details['data']['id']
    #     assert image_details['data']['lifecycle-state'] == 'EXPORTING'

    #     util.wait_until(['compute', 'image', 'get', '--image-id', self.custom_image_id], 'AVAILABLE', max_wait_seconds=3600)

    #     # Create a pre-authenticated request against the object so that we can import it
    #     result = self.invoke(
    #         ['os', 'preauth-request', 'create',
    #          '--namespace', self.object_storage_namespace,
    #          '--bucket-name', self.bucket_name,
    #          '--object-name', self.export_via_par_object_name,
    #          '--name', 'preauth-object',
    #          '--access-type', 'ObjectRead',
    #          '--time-expires', '9999-12-31T00:00:00.000+00:00'])
    #     par_details = json.loads(result.output)
    #     self.object_par_id = par_details['data']['id']

    #     # The access-uri in the response looks like:
    #     #    /p/...../n/mytenancy/b/A_CliImportExportBucket/o/test_export_1
    #     #
    #     # So we need to prepend the domain only (as the URI references the object alreadt)
    #     object_par_access_uri = '{}{}'.format(oci.regions.endpoint_for('object_storage', config['region']), par_details['data']['access-uri'])

    #     result = self.invoke(
    #         ['compute', 'image', 'import', 'from-object-uri',
    #          '--compartment-id', util.COMPARTMENT_ID,
    #          '--display-name', 'Imported from object storage par',
    #          '--uri', object_par_access_uri])
    #     image_details = json.loads(result.output)
    #     self.imported_image_from_par_id = image_details['data']['id']
    #     assert self.imported_image_from_par_id is not None
    #     assert image_details['data']['lifecycle-state'] == 'IMPORTING'
    #     assert image_details['data']['display-name'] == 'Imported from object storage par'

    #     util.wait_until(['compute', 'image', 'get', '--image-id', self.imported_image_from_par_id], 'AVAILABLE', max_wait_seconds=3600)

    def subtest_image_export_via_tuple_with_export_format_specified(self):
        self.export_via_tuple_object_name_with_export_format = 'export-via-tuple-with-export-format'

        result = self.invoke(
            ['compute', 'image', 'export', 'to-object',
             '--image-id', self.custom_image_id,
             '--namespace', self.object_storage_namespace,
             '--bucket-name', self.bucket_name,
             '--name', self.export_via_tuple_object_name_with_export_format,
             '--export-format', 'vmdk'])
        image_details = json.loads(result.output)
        assert self.custom_image_id == image_details['data']['id']
        assert image_details['data']['lifecycle-state'] == 'EXPORTING'

        util.wait_until(['compute', 'image', 'get', '--image-id', self.custom_image_id], 'AVAILABLE', max_wait_seconds=3600)

    def subtest_image_export_via_uri_with_export_format_specified(self, config):
        self.export_via_uri_object_name_with_export_format = 'export-via-uri-with-export-format'
        object_uri = '{}/n/{}/b/{}/o/{}'.format(
            oci.regions.endpoint_for('object_storage', config['region']),
            self.object_storage_namespace,
            self.bucket_name,
            self.export_via_uri_object_name_with_export_format)

        result = self.invoke(
            ['compute', 'image', 'export', 'to-object-uri',
             '--image-id', self.custom_image_id,
             '--uri', object_uri,
             '--export-format', 'qcow2'])
        image_details = json.loads(result.output)
        assert self.custom_image_id == image_details['data']['id']
        assert image_details['data']['lifecycle-state'] == 'EXPORTING'

        util.wait_until(['compute', 'image', 'get', '--image-id', self.custom_image_id], 'AVAILABLE', max_wait_seconds=3600)

    def set_up_resources(self):
        # Grab the Object Storage namespace
        result = self.invoke(['os', 'ns', 'get'])
        self.object_storage_namespace = json.loads(result.output)['data']

        # Create a bucket
        print("Creating bucket")
        self.bucket_name = util.random_name('CliImageImportExport')
        result = self.invoke(
            ['os', 'bucket', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--namespace', self.object_storage_namespace,
             '--name', self.bucket_name])
        util.validate_response(result, expect_etag=True)

        # Create a VCN
        print("Creating VCN")
        vcn_name = util.random_name('cli_test_compute_vcn')
        result = self.invoke(
            ['network', 'vcn', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--display-name', vcn_name,
             '--dns-label', 'clivcn',
             '--cidr-block', '10.0.0.0/16'])
        util.validate_response(result, expect_etag=True)
        self.vcn_ocid = util.find_id_in_response(result.output)
        util.wait_until(['network', 'vcn', 'get', '--vcn-id', self.vcn_ocid], 'AVAILABLE', max_wait_seconds=300)

        # Create a subnet
        print("Creating subnet")
        subnet_name = util.random_name('cli_test_compute_subnet')
        result = self.invoke(
            ['network', 'subnet', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', subnet_name,
             '--dns-label', 'clisubnet',
             '--vcn-id', self.vcn_ocid,
             '--cidr-block', '10.0.0.0/16',
             ])
        util.validate_response(result, expect_etag=True)
        self.subnet_ocid = util.find_id_in_response(result.output)
        util.wait_until(['network', 'subnet', 'get', '--subnet-id', self.subnet_ocid], 'AVAILABLE', max_wait_seconds=300)

        # Create an instance
        image_id = util.oracle_linux_image()
        shape = 'VM.Standard1.1'
        instance_name = util.random_name('cli_test_instance')
        print("Creating instance " + instance_name)
        result = self.invoke(
            ['compute', 'instance', 'launch',
             '--compartment-id', util.COMPARTMENT_ID,
             '--availability-domain', util.availability_domain(),
             '--display-name', instance_name,
             '--subnet-id', self.subnet_ocid,
             '--image-id', image_id,
             '--shape', shape])
        util.validate_response(result, expect_etag=True)
        self.instance_id = util.find_id_in_response(result.output)
        util.wait_until(['compute', 'instance', 'get', '--instance-id', self.instance_id], 'RUNNING', max_wait_seconds=600)

        # Export an image from the instance to use in tests
        print("Exporting image")
        result = self.invoke(
            ['compute', 'image', 'create',
             '--compartment-id', util.COMPARTMENT_ID,
             '--instance-id', self.instance_id])
        util.validate_response(result, expect_etag=True)
        self.custom_image_id = util.find_id_in_response(result.output)
        util.wait_until(['compute', 'image', 'get', '--image-id', self.custom_image_id], 'AVAILABLE', max_wait_seconds=3600)

    def clean_up_resources(self):
        error_count = 0

        if hasattr(self, 'instance_id'):
            try:
                print("Deleting instance " + self.instance_id)
                result = self.invoke(['compute', 'instance', 'terminate', '--instance-id', self.instance_id, '--force'])
                util.validate_response(result)
                util.wait_until(['compute', 'instance', 'get', '--instance-id', self.instance_id], 'TERMINATED',
                                max_wait_seconds=1200, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'subnet_ocid'):
            try:
                print("Deleting subnet")
                result = self.invoke(['network', 'subnet', 'delete', '--subnet-id', self.subnet_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'subnet', 'get', '--subnet-id', self.subnet_ocid], 'TERMINATED',
                                max_wait_seconds=600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'vcn_ocid'):
            try:
                print("Deleting vcn")
                result = self.invoke(['network', 'vcn', 'delete', '--vcn-id', self.vcn_ocid, '--force'])
                util.validate_response(result)
                util.wait_until(['network', 'vcn', 'get', '--vcn-id', self.vcn_ocid], 'TERMINATED',
                                max_wait_seconds=600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'custom_image_id'):
            try:
                print("Deleting custom base image")
                result = self.invoke(
                    ['compute', 'image', 'delete',
                     '--image-id', self.custom_image_id,
                     '--force'])
                util.validate_response(result)
                util.wait_until(['compute', 'image', 'get', '--image-id', self.custom_image_id], 'DELETED',
                                max_wait_seconds=3600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'imported_image_from_tuple_id'):
            try:
                print("Deleting imported image")
                result = self.invoke(
                    ['compute', 'image', 'delete',
                     '--image-id', self.imported_image_from_tuple_id,
                     '--force'])
                util.validate_response(result)
                util.wait_until(['compute', 'image', 'get', '--image-id', self.imported_image_from_tuple_id], 'DELETED',
                                max_wait_seconds=3600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'imported_image_from_uri_id'):
            try:
                print("Deleting imported image")
                result = self.invoke(
                    ['compute', 'image', 'delete',
                     '--image-id', self.imported_image_from_uri_id,
                     '--force'])
                util.validate_response(result)
                util.wait_until(['compute', 'image', 'get', '--image-id', self.imported_image_from_uri_id], 'DELETED',
                                max_wait_seconds=3600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'imported_image_from_par_id'):
            try:
                print("Deleting imported image")
                result = self.invoke(
                    ['compute', 'image', 'delete',
                     '--image-id', self.imported_image_from_par_id,
                     '--force'])
                util.validate_response(result)
                util.wait_until(['compute', 'image', 'get', '--image-id', self.imported_image_from_par_id], 'DELETED',
                                max_wait_seconds=3600, succeed_if_not_found=True)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if (hasattr(self, 'export_via_tuple_object_name')):
            try:
                print("Deleting exported image via tuple")
                result = self.invoke(
                    ['os', 'object', 'delete',
                     '--namespace', self.object_storage_namespace,
                     '--bucket-name', self.bucket_name,
                     '--name', self.export_via_tuple_object_name,
                     '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if (hasattr(self, 'export_via_uri_object_name')):
            try:
                print("Deleting exported image via uri")
                result = self.invoke(
                    ['os', 'object', 'delete',
                     '--namespace', self.object_storage_namespace,
                     '--bucket-name', self.bucket_name,
                     '--name', self.export_via_uri_object_name,
                     '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if (hasattr(self, 'export_via_tuple_object_name_with_export_format')):
            try:
                print("Deleting exported image via tuple with export format")
                result = self.invoke(
                    ['os', 'object', 'delete',
                     '--namespace', self.object_storage_namespace,
                     '--bucket-name', self.bucket_name,
                     '--name', self.export_via_tuple_object_name_with_export_format,
                     '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if (hasattr(self, 'export_via_uri_object_name_with_export_format')):
            try:
                print("Deleting exported image via uri with export format")
                result = self.invoke(
                    ['os', 'object', 'delete',
                     '--namespace', self.object_storage_namespace,
                     '--bucket-name', self.bucket_name,
                     '--name', self.export_via_uri_object_name_with_export_format,
                     '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if (hasattr(self, 'export_via_par_object_name')):
            try:
                print("Deleting exported image via preauthenticated request")
                result = self.invoke(
                    ['os', 'object', 'delete',
                     '--namespace', self.object_storage_namespace,
                     '--bucket-name', self.bucket_name,
                     '--name', self.export_via_par_object_name,
                     '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if (hasattr(self, 'bucket_par_id')):
            try:
                print("Deleting bucket par")
                result = self.invoke(
                    ['os', 'preauth-request', 'delete',
                     '--namespace', self.object_storage_namespace,
                     '--bucket-name', self.bucket_name,
                     '--par-id', self.bucket_par_id,
                     '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if (hasattr(self, 'object_par_id')):
            try:
                print("Deleting object par")
                result = self.invoke(
                    ['os', 'preauth-request', 'delete',
                     '--namespace', self.object_storage_namespace,
                     '--bucket-name', self.bucket_name,
                     '--par-id', self.object_par_id,
                     '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if (hasattr(self, 'bucket_name')):
            try:
                print("Deleting bucket")
                result = self.invoke(
                    ['os', 'bucket', 'delete',
                     '--namespace', self.object_storage_namespace,
                     '--name', self.bucket_name,
                     '--force'])
                util.validate_response(result)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        assert error_count == 0

    def invoke(self, commands, debug=False, ** args):
        if debug is True:
            commands = ['--debug'] + commands

        return util.invoke_command(commands, ** args)
