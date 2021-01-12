# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
import sys

import click
from oci_cli import cli_util

from services.ons.src.oci_cli_ons.ons_cli_extended import create_subscription
from services.events.src.oci_cli_events.generated.events_cli import create_rule


def setup_notifications_helper(ctx, create_topic_details, create_rule_kwargs):
    """
    Sets up notifications and prints out the commands that can be executed manually by the customer as well
    This helper populates the topicId for every action under the create_rule_kwargs actions if not provided
    :param ctx: The context object for the CLI command
    :param create_topic_details: A dictionary that contains the following keys:
        name - String, Required
        description - String, Required
        compartmentId - String, Required
    :param create_rule_kwargs: A dictionary that contains the following structure:
        display_name - String, Required
        compartment_id - String, Optional
        description - String, Required
        is_enabled - Bool, Required
        condition - String, Required
        actions - Dict, Required
            actions - List of dictionaries with the following keys, Required
                actionType - String, Required
                topicId - String, Optional
                isEnabled - Bool, Required

    :return:
    """

    # In case the user doesn't have the right credentials to do events and notifications, print the commands that
    # they can run with the right user
    click.echo('If the commands fail to run, you can use the OCI CLI to do the setup manually:')
    click.echo('oci ons topic create --compartment-id {} --name {} '
               '--description "{}"'.format(create_topic_details['compartmentId'], create_topic_details['name'],
                                           create_topic_details['description']))
    click.echo('oci ons subscription create --protocol EMAIL --compartment-id $ROOT_COMPARTMENT_OCID '
               '--topic-id $TOPIC_OCID --subscription_endpoint $EMAIL_ID')
    click.echo('oci events rule create --display-name %s --is-enabled true'
               '--compartment-id %s '
               '--actions \'{"actions":[{"actionType":"ONS","topicId":"$TOPIC_OCID","isEnabled":true}]}\' '
               '--condition \'%s\' '
               '--description "%s"'
               % (create_rule_kwargs['display_name'], create_rule_kwargs['compartment_id'],
                  create_rule_kwargs['condition'], create_rule_kwargs['description']))

    create_topic_kwargs = {
        'opc_request_id': cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    }
    ctx.endpoint = None
    ctx.obj['endpoint'] = None
    create_topic_client = get_topic_client(ctx)
    click.echo('Creating topic {}'.format(create_topic_details['name']))
    create_topic_result = create_topic_client.create_topic(
        create_topic_details=create_topic_details,
        **create_topic_kwargs
    )
    cli_util.render_response(create_topic_result, ctx)

    # Create multiple subscriptions to the topic
    emails = prompt_for_emails()
    for email in emails.split(','):
        create_subscription_kwargs = {
            'protocol': 'EMAIL',
            'compartment_id': create_topic_details['compartmentId'],
            'topic_id': get_topic_id(create_topic_result),
            'subscription_endpoint': email
        }
        click.echo('Creating subscription for {}'.format(email))
        create_subscription_helper(ctx, create_subscription_kwargs)

    for index in range(len(create_rule_kwargs['actions']['actions'])):
        if 'topicId' not in create_rule_kwargs['actions']['actions'][index] or \
                create_rule_kwargs['actions']['actions'][index]['topicId'] is None:
            create_rule_kwargs['actions']['actions'][index]['topicId'] = get_topic_id(create_topic_result)
    click.echo('Creating rule {}'.format(create_rule_kwargs['display_name']))
    ctx.endpoint = None
    ctx.obj['endpoint'] = None
    create_rule_helper(ctx, create_rule_kwargs)


# All these methods are meant solely for mock testing
def get_topic_client(ctx):
    return cli_util.build_client('ons', 'notification_control_plane', ctx)


def get_topic_id(result):
    return result.data.topic_id


def prompt_for_emails():
    return click.prompt("Enter email addresses to subscribe to as a comma separated list. "
                        "Example: joe.dan@oracle.com,july.den@xyz.com ")


def create_subscription_helper(ctx, create_subscription_kwargs):
    ctx.invoke(create_subscription, **create_subscription_kwargs)


def create_rule_helper(ctx, create_rule_kwargs):
    ctx.invoke(create_rule, **create_rule_kwargs)


def error_message_wrapper(msg):
    click.echo(click.style("Error: {}", fg="red").format(msg), err=True)
    sys.exit(1)
