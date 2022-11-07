# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
from oci_cli import cli_setup
from oci_cli import cli_util

from oci_cli.cli_setup import DEFAULT_KEY_NAME, PUBLIC_KEY_FILENAME_SUFFIX, PRIVATE_KEY_FILENAME_SUFFIX

import base64
import click
import errno
import oci._vendor.jwt as jwt
import oci
import oci.regions as regions
import os
import sys
import uuid
import webbrowser
from oci import identity

from urllib.parse import urlparse, parse_qs, urlencode
from http.server import BaseHTTPRequestHandler, HTTPServer

BOOTSTRAP_SERVICE_PORT = 8181
BOOTSTRAP_PROCESS_CANCELED_MESSAGE = 'Bootstrap process canceled.'
CONSOLE_AUTH_URL_FORMAT = "https://login.{region}.{realm}/v1/oauth2/authorize"


@cli_setup.setup_group.command('bootstrap', help="""
Provides an interactive process to create a CLI config file using username / password based login through a browser.
Also handles generating API keys and uploading them to your Oracle Cloud Infrastructure account.

Note that port {port} must be available in order for this command to complete properly.""".format(port=BOOTSTRAP_SERVICE_PORT))
@click.option('--profile-name', help='Name of the profile you are creating')
@click.option('--config-location', help='Path to the config for the new profile')
@cli_util.help_option
@click.pass_context
@cli_util.wrap_exceptions
def bootstrap_oci_cli(ctx, profile_name, config_location):
    region_param = ctx.obj['region'] if ctx.obj['region'] else ''
    user_session = create_user_session(region=region_param)

    public_key = user_session.public_key
    private_key = user_session.private_key
    region = user_session.region
    token = user_session.token
    tenancy_ocid = user_session.tenancy_ocid
    user_ocid = user_session.user_ocid
    fingerprint = user_session.fingerprint

    # create initial SDK client which targets region that user specified
    signer = oci.auth.signers.SecurityTokenSigner(token, private_key)
    client = identity.IdentityClient({'region': region}, signer=signer)

    # find home region and create new client targeting home region to use for subsequent identity requests
    result = client.list_region_subscriptions(tenancy_ocid)
    for r in result.data:
        if r.is_home_region:
            home_region = r.region_name
            break

    client = identity.IdentityClient({'region': home_region}, signer=signer)

    create_api_key_details = identity.models.CreateApiKeyDetails()
    create_api_key_details.key = cli_util.serialize_key(public_key=public_key).decode('UTF-8')

    try:
        result = client.upload_api_key(user_ocid, create_api_key_details)
    except oci.exceptions.ServiceError as e:
        if e.status == 409 and e.code == 'ApiKeyLimitExceeded':
            # User cannot upload any more API keys, so ask if they'd like to delete one
            result = client.list_api_keys(user_ocid)
            click.echo('ApiKey limit has been reached for this user account.')
            click.echo('The following API keys are currently enabled for this account:')
            count = 1
            for result in result.data:
                click.echo('\tKey [{index}]: Fingerprint: {fingerprint}, Time Created: {time_created}'.format(
                    index=count,
                    fingerprint=result.fingerprint,
                    time_created=result.time_created
                ), sys.stderr)
                count += 1

            delete_thumbprint = click.prompt(text='Enter the fingerprint of the API key to delete to make space for the new key (leave empty to skip deletion and exit command)', confirmation_prompt=True)
            if not delete_thumbprint:
                click.echo(BOOTSTRAP_PROCESS_CANCELED_MESSAGE)
                sys.exit(0)

            client.delete_api_key(user_ocid, delete_thumbprint)
            click.echo('Deleted Api key with fingerprint: {}'.format(delete_thumbprint))
            client.upload_api_key(user_ocid, create_api_key_details)
        else:
            raise e

    click.echo('Uploaded new API key with fingerprint: {}'.format(fingerprint))

    # write credentials to filesystem
    config_loc = os.path.expanduser(config_location) if config_location else None
    profile_name, config_location = persist_user_session(user_session, profile_name=profile_name, config=config_loc, persist_token=False, bootstrap=True)

    click.echo('Config written to: {}'.format(config_location))

    click.echo("""
    Try out your newly registered credentials with the following example command:

    oci iam region list --config-file {config_file} --profile {profile}
""".format(config_file=config_location, profile=profile_name))


def create_user_session(region='', tenancy_name=None):
    if region == '':
        region = cli_setup.prompt_for_region()

    # try to set up http server so we can fail early if the required port is in use
    try:
        server_address = ('', BOOTSTRAP_SERVICE_PORT)
        httpd = StoppableHttpServer(server_address, StoppableHttpRequestHandler)
    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            click.echo("Could not complete bootstrap process because port {port} is already in use.".format(
                port=BOOTSTRAP_SERVICE_PORT)
            )

            sys.exit(1)

        raise e

    # create new key pair
    # this key pair is used to get the initial token and also uploaded as a new API key for the user
    private_key = cli_util.generate_key()
    public_key = private_key.public_key()

    fingerprint = cli_setup.public_key_to_fingerprint(public_key)
    key = cli_util.to_jwk(public_key)
    jwk_content = key

    bytes_jwk_content = jwk_content.encode('UTF-8')
    b64_jwk_content = base64.urlsafe_b64encode(bytes_jwk_content).decode('UTF-8')
    public_key_jwk = b64_jwk_content

    query = {
        'action': 'login',
        'client_id': 'iaas_console',
        'response_type': 'token id_token',
        'nonce': uuid.uuid4(),
        'scope': 'openid',
        'public_key': public_key_jwk,
        'redirect_uri': 'http://localhost:{}'.format(BOOTSTRAP_SERVICE_PORT)
    }

    if tenancy_name:
        query['tenant'] = tenancy_name

    if region in regions.REGIONS_SHORT_NAMES:
        region = regions.REGIONS_SHORT_NAMES[region]

    if regions.is_region(region):
        console_url = CONSOLE_AUTH_URL_FORMAT.format(region=region,
                                                     realm=regions.REALMS[regions.REGION_REALMS[region]])
    else:
        click.echo('Error: {} is not a valid region. Valid regions are \n{}'.format(region, regions.REGIONS))
        sys.exit(1)

    query_string = urlencode(query)
    url = "{console_auth_url}?{query_string}".format(
        console_auth_url=console_url,
        query_string=query_string
    )

    # attempt to open browser to console log in page
    try:
        if webbrowser.open_new(url):
            click.echo('    Please switch to newly opened browser window to log in!')
            click.echo('    You can also open the following URL in a web browser window to continue:')
            click.echo('%s' % url)
        else:
            click.echo('    Open the following URL in a web browser window to continue:')
            click.echo('%s' % url)
    except webbrowser.Error as e:
        click.echo('Could not launch web browser to complete login process, exiting bootstrap command. Error: {exc_info}.'.format(
            exc_info=str(e)
        ))
        sys.exit(1)

    # start up http server which will handle capturing auth redirect from console
    token = httpd.serve_forever()

    click.echo('    Completed browser authentication process!')

    # get user / tenant info out of token
    token_data = jwt.decode(token, verify=False)
    user_ocid = token_data['sub']
    tenancy_ocid = token_data['tenant']

    return UserSession(user_ocid, tenancy_ocid, region, token, public_key, private_key, fingerprint)


def persist_user_session(user_session, profile_name=None, config=None, use_passphrase=False, persist_token=False, bootstrap=False, session_auth=False):
    if not profile_name:
        # prompt for location of user config
        config_location, profile_name = cli_setup.prompt_session_for_profile()
    if config:
        config_location = config
    else:
        config_location = cli_setup.DEFAULT_CONFIG_LOCATION

    if not config_location:
        click.echo(BOOTSTRAP_PROCESS_CANCELED_MESSAGE)
        sys.exit(0)

    # prompt for directory to place keys
    session_auth_location = os.path.abspath(os.path.join(cli_setup.DEFAULT_TOKEN_DIRECTORY, profile_name))
    if not os.path.exists(session_auth_location):
        cli_util.create_directory(session_auth_location)

    public_key_file_path = os.path.join(session_auth_location, DEFAULT_KEY_NAME + PUBLIC_KEY_FILENAME_SUFFIX)
    private_key_file_path = os.path.join(session_auth_location, DEFAULT_KEY_NAME + PRIVATE_KEY_FILENAME_SUFFIX)
    if not cli_setup.write_public_key_to_file(public_key_file_path, user_session.public_key, True, True):
        click.echo(BOOTSTRAP_PROCESS_CANCELED_MESSAGE)
        sys.exit(0)

    key_passphrase = ''
    if bootstrap or (session_auth and use_passphrase):
        key_passphrase = click.prompt(text='Enter a passphrase for your private key (empty for no passphrase)',
                                      default='', hide_input=True, show_default=False, confirmation_prompt=True)

    if not cli_setup.write_private_key_to_file(private_key_file_path, user_session.private_key, key_passphrase, True, True):
        click.echo(BOOTSTRAP_PROCESS_CANCELED_MESSAGE)
        sys.exit(0)

    # write token to a file so we can refresh it without having to read / write the entire config
    if persist_token:
        token_location = os.path.join(session_auth_location, 'token')
        with open(token_location, 'w') as security_token_file:
            security_token_file.write(user_session.token)
        cli_util.apply_user_only_access_permissions(token_location)

    # remove conflicting profile entry if exists
    cli_setup.remove_profile_from_config(config_location, profile_name)

    userId = None
    if bootstrap:
        userId = user_session.user_ocid

    if session_auth and key_passphrase and not click.confirm('Do you want to write your passphrase to the config file? (If not, you will need to enter it when prompted each time you run an oci command)', default=False):
        key_passphrase = None

    cli_setup.write_config(
        filename=config_location,
        user_id=userId,
        fingerprint=user_session.fingerprint,
        key_file=os.path.abspath(private_key_file_path),
        tenancy=user_session.tenancy_ocid,
        region=user_session.region,
        pass_phrase=key_passphrase,
        profile_name=profile_name,
        security_token_file=token_location if persist_token else None
    )

    return profile_name, config_location


class StoppableHttpRequestHandler (BaseHTTPRequestHandler):
    """http request handler with abilitiy to stop the server"""

    def log_message(self, format, *args):
        return

    def do_GET(self):
        """send 200 OK response, and set server.stop to True"""

        self.send_response(200)
        self.end_headers()

        if self.path == '/':
            javascript = """
            <script type='text/javascript'>
                hash = window.location.hash

                // remove leading '#' so that python can detect it
                if (hash[0] === '#') {
                    hash = hash.substr(1)
                }

                console.log(hash)

                function reqListener () {
                    console.log(this.responseText);
                    document.write('Authorization completed! Please close this window and return to your terminal to finish the bootstrap process.')
                }

                var oReq = new XMLHttpRequest();
                oReq.addEventListener("load", reqListener);
                oReq.open("GET", "/token?" + hash);
                oReq.send();
            </script>
            """
            try:
                self.wfile.write(javascript)
            except TypeError:
                self.wfile.write(bytes(javascript, 'UTF-8'))
        else:
            query_components = parse_qs(urlparse(self.path).query)
            if 'security_token' in query_components:
                security_token = query_components['security_token'][0]
                self.server.ret_value = security_token
                self.server.stop = True


class StoppableHttpServer (HTTPServer):
    """http server that reacts to self.stop flag"""

    def serve_forever(self):
        """Handle one request at a time until stopped."""

        self.stop = False
        self.ret_value = None

        while not self.stop:
            self.handle_request()

        self.server_close()

        return self.ret_value


class UserSession(object):
    def __init__(self, user_ocid, tenancy_ocid, region, token, public_key, private_key, fingerprint):
        self.user_ocid = user_ocid
        self.tenancy_ocid = tenancy_ocid
        self.region = region
        self.token = token
        self.public_key = public_key
        self.private_key = private_key
        self.fingerprint = fingerprint


def process_security_tokenname(filename):
    filename_expanded = os.path.expanduser(filename)
    if os.path.isdir(filename_expanded):
        raise click.BadParameter("Token file location must be a filename not a directory")

    if os.path.exists(filename_expanded):
        raise click.BadParameter("Token file location cannot already exist")

    return filename_expanded
