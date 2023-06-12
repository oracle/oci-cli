# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates. All rights reserved.

import functools
import platform
import subprocess
from typing import Tuple, List
from urllib.parse import urlparse

import click

from oci.exceptions import RequestException, ServiceError
from oci.retry import RetryStrategyBuilder
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli.aliasing import CommandGroupWithAlias

from services.dts.src.oci_cli_dts.generated import dts_service_cli
from services.dts.src.oci_cli_dts.physicalappliance_cli_extended import validate_upload_user_credentials


@click.command("verify", cls=CommandGroupWithAlias, help="Verify requirements for 'Data Import - Appliance'")
@cli_util.help_option_group
def verify_group():
    pass


dts_service_cli.dts_service_group.add_command(verify_group)


@verify_group.command("prepared", help="Verify requirements after 'Preparing for Appliance Data Transfers'")
@cli_util.option("--compartment-id", required=True, help="Compartment OCID")
@cli_util.option("--job-id", required=True, help="OCID of the Transfer Job")
@cli_util.option("--bucket", required=True, help="Upload bucket name")
@click.pass_context
@cli_util.help_option
@json_skeleton_utils.get_cli_json_input_option({})
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def prepared(ctx, from_json, compartment_id, job_id, bucket):
    click.echo("Verifying requirements after 'Preparing for Appliance Data Transfers'...")

    results = [
        check_dts_connectivity(ctx, compartment_id),
        check_os_connectivity(ctx, compartment_id),
        check_iam_users_groups_policies(ctx, compartment_id),
        check_bucket_belongs_to_compartment(ctx, compartment_id, bucket),
        check_dts_entitlement(ctx, compartment_id),
        check_dts_job_and_appliance_request(ctx, compartment_id, job_id, bucket),
        check_upload_user_credentials(ctx, bucket),
    ]

    if not all(results):
        click.echo("Verification failed.")
        exit(1)
    click.echo("Verification successful.")


@verify_group.command("configured", help="Verify requirements after 'Configuring Appliance Data Imports'")
@cli_util.option("--job-id", required=True, help="OCID of the Transfer Job")
@cli_util.option("--appliance-label", required=True, help="Appliance label")
@cli_util.option("--delivery-security-tie-id", required=True, help="Physical security tag ID")
@cli_util.option("--appliance-ip", required=True, help="Configured Appliance IP address")
@click.pass_context
@cli_util.help_option
@json_skeleton_utils.get_cli_json_input_option({})
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def configured(ctx, from_json, job_id, appliance_label, delivery_security_tie_id, appliance_ip):
    click.echo("Verifying requirements after 'Configuring Appliance Data Imports'...")

    results = [
        check_delivery_security_tie(ctx, job_id, appliance_label, delivery_security_tie_id),
        check_appliance_reachability(appliance_ip),
    ]

    if not all(results):
        click.echo("Verification failed.")
        exit(1)
    click.echo("Verification successful.")


@verify_group.command("copied", help="Verify requirements after 'Copying Data to the Import Appliance'")
@cli_util.option("--job-id", required=True, help="Transfer job OCID")
@cli_util.option("--appliance-label", required=True, help="Appliance label")
@cli_util.option('--appliance-profile', required=False, default="DEFAULT", help="Transfer Appliance profile")
@click.pass_context
@cli_util.help_option
@json_skeleton_utils.get_cli_json_input_option({})
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def copied(ctx, from_json, job_id, appliance_label, appliance_profile):
    click.echo("Verifying requirements after 'Copying Data to the Import Appliance'...")

    results = [
        check_finalized_status(ctx, job_id, appliance_label)
    ]

    if not all(results):
        click.echo("Verification failed.")
        exit(1)
    click.echo("Verification successful.")


@verify_group.command("shipped", help="Verify requirements after 'Shipping the Import Appliance'")
@cli_util.option("--job-id", required=True, help="Transfer job OCID")
@cli_util.option("--appliance-label", required=True, help="Appliance label")
@cli_util.option("--return-security-tie-id", required=True, help="Physical security tag ID")
@click.pass_context
@cli_util.help_option
@json_skeleton_utils.get_cli_json_input_option({})
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def shipped(ctx, from_json, job_id, appliance_label, return_security_tie_id):
    click.echo("Verifying requirements after 'Shipping the Import Appliance'...")

    results = [
        check_return_security_tie(ctx, job_id, appliance_label, return_security_tie_id),
    ]

    if not all(results):
        click.echo("Verification failed.")
        exit(1)
    click.echo("Verification successful.")


@verify_group.command("monitored", help="Verify requirements after 'Monitoring the Import Appliance and Data Transfer'")
@cli_util.option("--job-id", required=True, help="Transfer job OCID")
@cli_util.option("--appliance-label", required=True, help="Appliance label")
@click.pass_context
@cli_util.help_option
@json_skeleton_utils.get_cli_json_input_option({})
@json_skeleton_utils.json_skeleton_generation_handler({})
@cli_util.wrap_exceptions
def monitored(ctx, from_json, job_id, appliance_label):
    click.echo("Verifying requirements after 'Monitoring the Import Appliance and Data Transfer'...")

    results = [
        check_import_appliance_status(ctx, job_id, appliance_label)
    ]

    if not all(results):
        click.echo("Verification failed.")
        exit(1)
    click.echo("Verification successful.")


def check(name, nl=False):
    """
    A decorator that checks if a certain condition is met.
    Use it to decorate a function that returns a tuple of (status:bool, messages:List[str]).
    The function is expected to return True if the condition is met, False otherwise. Function messages or raised errors
    are printed after the condition success or failure is printed.

    :param name: A string with the name of the check
    :param nl: A bool indicating whether to print a newline after 'Checking condition... '
    :return: A wrapped function
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            click.echo(click.style(f"Checking {name}... ", fg="blue"), nl=nl)
            try:
                result, messages = func(*args, **kwargs)
            except ServiceError:
                click.echo(click.style("Fail", fg="red"))
                raise

            if not result:
                click.echo(click.style("Fail", fg="red"))
                for message in messages:
                    click.echo(message)
                exit(1)
            else:
                click.echo(click.style("OK", fg="green"))
                for message in messages:
                    click.echo(message)
            return result
        return wrapper
    return decorator


@check("Data Transfer Service connectivity")
def check_dts_connectivity(ctx, compartment_id: str) -> Tuple[bool, List[str]]:
    """
    Check connectivity to the Data Transfer Service endpoint.

    :param ctx: Click context object.
    :param compartment_id: The OCID of the compartment.
    :return: A tuple of (status:bool, messages:List[str])
    """
    client = cli_util.build_client('dts', 'transfer_job', ctx)
    try:
        kwargs = {"retry_strategy": retry_strategy()}
        client.list_transfer_jobs(compartment_id=compartment_id, **kwargs)
    except RequestException:
        click.echo(f"{urlparse(client.base_client.endpoint).netloc} is not reachable.")
        click.echo("Please ensure there there are no firewall rules blocking connectivity.")
        raise
    except ServiceError:
        return True, []
    else:
        return True, []


@check("Object Storage connectivity")
def check_os_connectivity(ctx, compartment_id: str) -> Tuple[bool, List[str]]:
    """
    Check connectivity to the Object Storage endpoint.

    :param ctx: Click context object.
    :param compartment_id: The OCID of the compartment.
    :return: A tuple of (status:bool, messages:List[str])
    """
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    try:
        kwargs = {"retry_strategy": retry_strategy()}
        client.get_namespace(compartment_id=compartment_id, **kwargs)
    except RequestException:
        click.echo(f"{urlparse(client.base_client.endpoint).netloc} is not reachable.")
        click.echo("Please ensure there there are no firewall rules blocking connectivity.")
        raise
    except ServiceError:
        return True, []
    else:
        return True, []


def retry_strategy():
    return RetryStrategyBuilder() \
        .add_max_attempts(max_attempts=3) \
        .add_total_elapsed_time(total_elapsed_time_seconds=30) \
        .get_retry_strategy()


@check("Required IAM Users, Groups, and Policies")
def check_iam_users_groups_policies(ctx, compartment_id):
    """
    Verify the existence of required IAM Users, Groups, and Policies.

    :param ctx: Click context object.
    :param compartment_id: The OCID of the compartment.
    :return: A tuple of (status: bool, messages: List[str]).
    """
    os_client = cli_util.build_client('object_storage', 'object_storage', ctx)
    dts_client = cli_util.build_client('dts', 'transfer_job', ctx)
    try:
        os_client.get_namespace()
        namespace = os_client.get_namespace().data
        os_client.list_buckets(namespace_name=namespace, compartment_id=compartment_id)
        dts_client.list_transfer_jobs(compartment_id=compartment_id)
    except ServiceError as e:
        if e.target_service == "object_storage" and (e.status == 401 or e.status == 404):
            messages = [
                "Unauthorized access to Object Storage.",
                "Please ensure you have the required IAM Users, Groups, and Policies to access Object Storage.",
            ]
            return False, messages
        elif e.target_service == "transfer_job" and (e.status == 401 or e.status == 404):
            messages = [
                "Unauthorized access to Data Transfer Service.",
                "Please ensure you have the required IAM Users, Groups, and Policies to access Data Transfer Service."
            ]
            return False, messages
        else:
            raise
    return True, []


@check("Upload Bucket exists in Compartment")
def check_bucket_belongs_to_compartment(ctx, compartment_id: str, upload_bucket: str) -> Tuple[bool, List[str]]:
    """
    Check if the upload bucket exists and belongs to the specified compartment.

    :param ctx: Click context object.
    :param compartment_id: The OCID of the compartment.
    :param upload_bucket: The upload bucket name.
    :return: A tuple of (status:bool, messages:List[str])
    """
    client = cli_util.build_client('object_storage', 'object_storage', ctx)
    # An unsuccessful API call raises a Service Error. If the method call returns a response, it is safe to assume the
    # API call was successful and we can access the data in the response.
    namespace = client.get_namespace().data
    try:
        bucket_obj = client.get_bucket(namespace_name=namespace, bucket_name=upload_bucket).data
    except ServiceError as e:
        if e.status == 404:
            messages = [
                "Bucket not found.",
                f"The bucket '{upload_bucket}' does not exist in namespace '{namespace}' or you are unauthorized to "
                f"access it."
            ]
            return False, messages
        raise

    if bucket_obj.compartment_id != compartment_id:
        messages = [
            f"The bucket '{upload_bucket}' does not belong to compartment '{compartment_id}'."
        ]
        return False, messages
    else:
        return True, []


@check("Upload User credentials", nl=True)
def check_upload_user_credentials(ctx, upload_bucket: str) -> Tuple[bool, List[str]]:
    """
    Check if the Upload User is able to create, overwrite and inspect a test object in the customer's bucket and read
    the metadata from the bucket. Also check if admin user can delete the test object from the bucket.
    A Service Error is raised by the validate_upload_user_credentials method should an issue arise.

    :param ctx: Click context object.
    :param upload_bucket: The upload bucket name.
    :return: A tuple of (status:bool, messages:List[str])
    """
    validate_upload_user_credentials(ctx, upload_bucket)
    return True, []


@check("Data Transfer Appliance Entitlement")
def check_dts_entitlement(ctx, compartment_id: str) -> Tuple[bool, List[str]]:
    """
    Check for an approved Data Transfer Appliance Entitlement in compartment.

    :param ctx: Click context object.
    :param compartment_id: The OCID of the compartment.
    :return: A tuple of (status:bool, messages:List[str])
    """
    client = cli_util.build_client('dts', 'transfer_appliance_entitlement', ctx)
    entitlements = client.list_transfer_appliance_entitlement(compartment_id=compartment_id).data

    if len(entitlements) < 1:
        messages = [
            f"Unable to find Data Transfer Appliance Entitlement in Compartment '{compartment_id}'."
        ]
        return False, messages

    for entitlement in entitlements:
        if entitlement.lifecycle_state_details == "APPROVED":
            return True, []
    messages = [
        "Data Transfer Appliance Entitlement needs to be in an APPROVED lifecycle state."
    ]
    return False, messages


@check("Transfer Job and Appliance Request")
def check_dts_job_and_appliance_request(ctx, compartment_id: str, job_id: str, upload_bucket: str) -> Tuple[bool, List[str]]:
    """
    Check the appliance transfer job in the compartment has the expected bucket and a corresponding appliance request.

    :param ctx: An object containing information related to the execution context.
    :param compartment_id: The OCID of the compartment.
    :param job_id: The OCID of the Transfer Job.
    :param upload_bucket: The name of the upload bucket.
    :return: A tuple of (status:bool, messages:List[str]).
    """
    client = cli_util.build_client('dts', 'transfer_job', ctx)
    transfer_jobs = client.list_transfer_jobs(compartment_id=compartment_id).data
    valid_jobs = list(filter(lambda job: job.upload_bucket_name == upload_bucket and job.device_type == "APPLIANCE" and job.id == job_id,
                             transfer_jobs))
    if not valid_jobs:
        messages = [
            f"There is no Appliance Transfer Job '{job_id}' for Data Import into Bucket '{upload_bucket}'."
        ]
        return False, messages

    client = cli_util.build_client("dts", "transfer_appliance", ctx)
    for transfer_job in valid_jobs:
        appliances = client.list_transfer_appliances(id=transfer_job.id).data.transfer_appliance_objects
        if appliances:
            return True, []
    messages = [
        f"There is no Transfer Appliance Request for Appliance Transfer Job '{job_id}'."
    ]
    return False, messages


@check("Delivery Tamper-evident Security Tie")
def check_delivery_security_tie(ctx, job_id: str, appliance_label: str, delivery_security_tie_id: str) -> Tuple[bool, List[str]]:
    """
    Check that the delivered physical security tie ID matches the security tie ID logged by Oracle.

    :param ctx: An object containing information related to the execution context.
    :param job_id: The OCID of the Transfer Job.
    :param appliance_label: The Appliance Label.
    :param delivery_security_tie_id: The ID on the delivered physical security tie.
    :return: A tuple of (status:bool, messages:List[str]).
    """
    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    appliance = client.get_transfer_appliance(id=job_id, transfer_appliance_label=appliance_label).data
    if appliance.delivery_security_tie_id != delivery_security_tie_id:
        messages = [
            f"The provided physical security tie number '{delivery_security_tie_id}' does not match the number "
            f"'{appliance.delivery_security_tie_id}' logged by Oracle, do not plug the appliance into your network! "
            f"Immediately file a Service Request (SR)."
        ]
        return False, messages
    return True, []


@check("Appliance Reachability")
def check_appliance_reachability(appliance_ip: str) -> Tuple[bool, List[str]]:
    """
    Checks the reachability of the appliance by pinging it once.

    :param appliance_ip: IP address of the appliance.
    :return: A tuple of (status:bool, messages:List[str]).
    """
    system = platform.system()
    if system == "Windows":
        command = ["ping", "-n", "1", appliance_ip]
    else:
        command = ["ping", "-c", "1", appliance_ip]
    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        messages = [
            "Appliance is not reachable.",
            " ".join(command),
            e.output.strip(),
            "\nPlease check the following:",
            " - IP configuration of the appliance is correct",
            " - There is no issue with physical connectivity",
            " - There is no firewall rule blocking traffic to the appliance",
        ]
        return False, messages
    else:
        return True, []


@check("Finalized Status")
def check_finalized_status(ctx, job_id, appliance_label):
    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    appliance = client.get_transfer_appliance(id=job_id, transfer_appliance_label=appliance_label).data
    if appliance.lifecycle_state == "FINALIZED":
        return True, []
    messages = [
        f"Appliance needs to be in a FINALIZED lifecycle state. It is currently {appliance.lifecycle_state}."
    ]
    return False, messages


@check("Return Tamper-evident Security Tie")
def check_return_security_tie(ctx, job_id: str, appliance_label: str, return_security_tie_id: str) -> Tuple[bool, List[str]]:
    """
    Check that the return physical security tie ID matches the security tie ID logged by Oracle.

    :param ctx: Click context object.
    :param job_id: The OCID of the Transfer Job.
    :param appliance_label: The Appliance Label.
    :param return_security_tie_id: The ID on the return physical security tie.
    :return: A tuple of (status:bool, messages:List[str]).
    """
    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    appliance = client.get_transfer_appliance(id=job_id, transfer_appliance_label=appliance_label).data
    if appliance.return_security_tie_id == return_security_tie_id:
        return True, []
    messages = [
        f"The provided physical security tie number '{return_security_tie_id}' does not match the number "
        f"'{appliance.return_security_tie_id}' logged by Oracle. Please file a Service Request (SR)."
    ]
    return False, messages


@check("Import Appliance Status")
def check_import_appliance_status(ctx, job_id, appliance_label) -> Tuple[bool, List[str]]:
    """
    Check the status of the Import Appliance.

    :param ctx: Click context object.
    :param job_id: The OCID of the Transfer Job.
    :param appliance_label: The Appliance Label.
    """
    client = cli_util.build_client('dts', 'transfer_appliance', ctx)
    appliance = client.get_transfer_appliance(id=job_id, transfer_appliance_label=appliance_label).data

    if appliance.lifecycle_state == "ERROR":
        messages = [
            "Oracle encountered an unrecoverable error trying to process your import appliance. "
            "Please file a Service Request (SR)."
        ]
        return False, messages
    elif appliance.lifecycle_state == "COMPLETE":
        messages = [
            "Oracle completed your import appliance data upload. "
            "Your data is available in your designated bucket in Oracle Cloud Infrastructure Object Storage."
        ]
        return True, messages
    else:
        messages = [
            f"The Status of the Import Appliance is currently '{appliance.lifecycle_state}'."
        ]
        return True, messages
