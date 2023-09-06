# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from oci import exceptions
from oci.config import from_file
from oci_cli.service_mapping import service_mapping

from alloy import alloy_constants
from alloy.error_messages import get_error_message

import json
import os.path


def _get_dot_oci_path(ctx=None):
    """
    Returns the path where the oci config is located. If no context were provided, returns None.

    Args:
        ctx (click.Context): A click.Context should include information such as the path to oci config.

    Returns:
        str: A path to the directory that the oci config is located [~/.oci], or None if the config is not found.
    """
    if ctx:
        # Confirm if this is a valid config file path
        path = os.path.expanduser(ctx.obj['config_file'])
        from_file(path, ctx.obj['profile'])
        return os.path.split(path)[0]


def get_service_config_path(ctx=None):
    """
    Assumes that the service config file is named "alloy-config.json."
    Finds and returns the path to the service config if it exists in the same directory as the config file; otherwise, None.

    Args:
        ctx (click.Context): A click.Context should include information such as the path to oci config.

    Returns:
        str: A valid path to the service config file, or None if the service config is not found.
    """
    # Find path
    try:
        path = os.path.join(_get_dot_oci_path(ctx), alloy_constants.DEFAULT_ALLOY_CONFIG_NAME) if ctx \
            else os.path.expanduser(alloy_constants.ALLOY_CONFIG_DEFAULT_LOCATION)
    except Exception:
        # Handles oci help case when config file not is present
        return None

    # TODO: distinguish if this is an oci user or an Alloy user
    # check for file path only if this is
    if os.path.isfile(path):
        return path


def get_service_config(ctx=None):
    """
    Finds the service config file from the same directory as the oci config file. Returns the content of the service config as a dict.

    Args:
        ctx (click.Context): A click.Context should include information such as the path to oci config.

    Raises:
        exceptions.ConfigFileNotFound: alloy-config.json isn't found in the same directory as the oci config file.
        e: _description_

    Returns:
        dict: The content of the alloy-config.json.
    """
    path = get_service_config_path(ctx)
    if not path:
        raise exceptions.ConfigFileNotFound(get_error_message(alloy_constants.NO_SERVICE_CONFIG))

    try:
        # Load Json Alloy
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        # TODO: customize error message
        raise e


def get_provider_name(ctx=None):
    """
    Finds and returns the name of the provider as specified in the service config file.

    Args:
        ctx (click.Context): A click.Context should include information such as the path to oci config.

    Raises:
        exceptions.InvalidConfig: Provider name is not specified in the service config file as `provider`.

    Returns:
        str: Name of the provider.
    """
    # TODO: distinguish if this is an oci user or a Alloy user
    # check for file path only if this is
    config = get_service_config(ctx)

    if config.get('alloyProvider'):
        return config['alloyProvider']

    raise exceptions.InvalidConfig(get_error_message(alloy_constants.PROVIDER_NAME_MISSING))


def get_subscribed_services(ctx):
    """
    Finds and returns the list of subscribed services as specified in the service config file.

    Args:
        ctx (click.Context): A click.Context should include information such as the path to oci config.

    Raises:
        exceptions.InvalidConfig: Subscribed services is not specified in the service config file as `services`.

    Returns:
        [str]: A list of subscribed services.
    """
    # TODO: distinguish if this is an oci user or an Alloy user
    # check for file path only if this is
    config = get_service_config(ctx)

    if config.get('services'):
        return config['services']

    raise exceptions.InvalidConfig(get_error_message(alloy_constants.SUBSCRIBED_SERVICES_MISSING))


def get_service_mapping_path(ctx):
    """
    Finds service_mapping.json from the same directory as the config file and returns the path.
    If no context were provided, returns the default path [~/.oci/service_mapping.json].

    Args:
        ctx (click.Context): A click.Context should include information such as the path to oci config.

    Returns:
        str: A path to service_mapping.json.
    """
    if ctx:
        return os.path.join(_get_dot_oci_path(ctx), alloy_constants.DEFAULT_SUBSCRIBED_SERVICE_MAPPING)
    return alloy_constants.DEFAULT_SUBSCRIBED_SERVICE_MAPPING_LOCATION


def write_subscribed_services(ctx):
    """
    Creates a service_mapping.json file with content similar to service_mapping.py, except it only contains information of the subscribed
    services according to alloy-config.json.

    Args:
        ctx (click.Context): A click.Context should include information such as the path to oci config.

    Returns:
        {str: str}: A dictionary of subscribed services.
    """
    subscribed_services = get_subscribed_services(ctx)

    services = {}
    for k, v in service_mapping.items():
        if v[0] in subscribed_services:
            services[k] = v

    with open(get_service_mapping_path(ctx), 'w+') as f:
        json.dump(services, f)

    return services


def read_subscribed_services(ctx=None):
    """
    Returns a service_mapping-equivalent (dict[str, str]) of the subscribed services.

    Only attempts to write service_mapping.json in the same directory as oci config if context were given.
    Otherwise, raises json errors if service_mapping.json was not found or is corrupted.

    Args:
        ctx (click.Context): A click.Context should include information such as the path to oci config.

    Raises:
        FileNotFoundError: service_mapping.json is not found and ctx was not provided.
        JSONDecodeError: service_mapping.json is corrupted and ctx was not provided.

    Returns:
        {str: str}: A dictionary of subscribed services.
    """
    try:
        with open(get_service_mapping_path(ctx), 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        if ctx:
            return write_subscribed_services(ctx)
        raise e


def get_subscribed_services_list(ctx):
    """
    Finds and returns a list of subscribed services in alloy config file.

    Args:
        ctx (click.Context): A click.Context should include information such as the path to oci config.

    Raises:
        FileNotFoundError: service_mapping.json is not found and ctx was not provided.
        JSONDecodeError: service_mapping.json is corrupted and ctx was not provided.

    Returns:
        [str]: A list of subscribed services.
    """
    service_mapping = read_subscribed_services(ctx)
    return list(service_mapping.keys())
