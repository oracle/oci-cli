# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import sys
import click
from oci_cli import cli_util, cli_root
import tempfile
from subprocess import Popen, PIPE  # to spawn processes
import time  # to sleep before retrying
import os  # to get access to os environment
import re  # for regular expressions
from oci._vendor import requests  # to make non-standard oci http calls
from oci._vendor.requests.auth import HTTPBasicAuth  # for swift authorizarion
import math  # to ceil dataSize and redoSize
import shutil  # to delete a directory
from oci.util import Sentinel
import tarfile

try:
    import cx_Oracle  # to query oracle instance
except ImportError:
    click.echo("cx_Oracle module could not be imported. This most likely means you have installed OCI CLI without "
               "optional feature 'db'. To use this script, please re-install CLI with 'db' optional feature.\n"
               "Below are the relevant commands to do it:\n"
               "In *NIX systems:\n"
               "    curl -L -O https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh\n"
               "    ./install.sh --optional-features db\n"
               "In Windows systems using powershell:\n"
               "    ((New-Object System.Net.WebClient).DownloadFile('https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.ps1', ""$pwd\\install.ps1""))\n"
               "    .\\install.ps1 -OptionalFeatures db\n"
               "If just using pip:\n"
               "    pip install 'oci-cli[db]'")
    exit(1)


DEFAULT_LOCATION = os.path.join('~', '.oci', 'config')
DEFAULT_PROFILE = "DEFAULT"


@click.command(name='create-from-onprem', help="""Create a backup of on-premise database on OCI """,
               context_settings=dict(allow_interspersed_args=True, ignore_unknown_options=True))
@click.option('--config-file',
              default=DEFAULT_LOCATION, show_default=True,
              help='The path to the config file.')
@click.option('--profile',
              default=Sentinel(DEFAULT_PROFILE), show_default=False,
              help='The profile in the config file to load. This profile will also be used to locate any default parameter values which have been specified in the OCI CLI-specific configuration file.  [default: DEFAULT]')
@click.option('--compartment-id', required=True, help="""Compartment_id to store backup""")
@click.option('--display-name', required=True, help="""The user-friendly name for the backup. It does not have to be unique.""")
@click.option('--availability-domain', required=True, help="""The Availability Domain where the DB System is located.""")
@click.option('--edition', required=True, help="""Database edition on to which the backup will be restored to""")
@click.option('--opc-installer-dir', required=True, help="""Directory containing opc_installer.jar file""")
@click.option('--additional-opc-args', required=False, help="""Optional additional arguments for opc installer""")
@click.option('--tmp-dir', required=False, help="""Optional Directory for temporary files""")
@click.option('--rman-password', required=False, help="""RMAN password to use (required) if TDE is not enabled""")
@click.option('--rman-channels', required=False, default='5', help="""RMAN Channels (default: 5)""")
@click.pass_context
def create_backup_from_onprem(ctx, config_file, profile, **kwargs):

    if os.name == 'nt':
        exit("This script is not supported on Windows operating systems.")

    if profile == Sentinel(DEFAULT_PROFILE):
        profile = DEFAULT_PROFILE

    initial_dict = {
        'config_file': config_file,
        'default_values_from_file': {},
        'profile': profile,
        'cert_bundle': None,
        'endpoint': None,
        'request_id': None,
        'no_retry': None,
        'debug': False,
        'proxy': None,
        'settings': {'proxy': None},
        'parameter_aliases': {},
        'region': None,
    }

    ctx.obj = initial_dict
    cli_root.load_default_values(ctx, config_file, profile)
    cli_util.populate_dict_key_with_default_value(ctx, 'region', click.STRING)

    availability_domain = kwargs['availability_domain']
    opcinstallerdir = kwargs['opc_installer_dir']
    rmanchannels = int(kwargs['rman_channels'])
    if 'rman_password' in kwargs:
        rmanpassword = kwargs['rman_password']
    if 'additional_opc_args' in kwargs:
        additionalopcargs = kwargs['additional_opc_args']

    # default tmpDir if it is not supplied
    tmpdir = os.path.join(tempfile.gettempdir(), "onprem_upload")
    if 'tmp_dir' in kwargs and kwargs['tmp_dir']:
        tmpdir = os.path.abspath(kwargs['tmp_dir'])

    # Make as many checks as possible before taking a backup.

    # Make sure opcInstaller exists and is readable
    opcinstaller = os.path.join(opcinstallerdir, "opc_install.jar")
    if not os.path.isfile(opcinstaller) and os.access(opcinstaller, os.R_OK):
        sys.exit("Could not access " + opcinstaller)

    # create tmpDir if it doesn't exist
    os.makedirs(tmpdir, 0o700)
    # make sure it is a directory and is empty
    if not os.path.isdir(tmpdir):
        sys.exit(tmpdir + " is not a directory")
    if os.listdir(tmpdir):
        sys.exit(tmpdir + " is not empty")

    # Verify ORACLE_HOME and ORACLE_SID are set and rman is good
    if 'ORACLE_HOME' not in os.environ or 'ORACLE_SID' not in os.environ:
        sys.exit("ORACLE_HOME and ORACLE_SID should be set")

    rman = os.path.join(os.environ['ORACLE_HOME'], "bin", "rman")
    if not (os.path.isfile(rman) and os.access(rman, os.X_OK)):
        sys.exit("Could not find a usable rman in this environment")

    click.echo("Connecting to Oracle database")
    db = cx_Oracle.connect("/", mode=cx_Oracle.SYSDBA)

    cursor = db.cursor()

    cursor.execute('select version from v$instance')
    for row in cursor:
        dbversion = row[0]
    if '18.' in dbversion:
        cursor.execute('select version_full from v$instance')
        for row in cursor:
            dbversion = row[0]
    click.echo("Oracle version is:%s" % dbversion)

    omf = None
    cursor.execute("select value from v$parameter where name ='db_create_file_dest'")
    for row in cursor:
        omf = row[0]
    if omf is None:
        sys.exit("OMF is required for the script to work.")

    click.echo("Checking the archive log mode of the database")
    cursor.execute('select log_mode from v$database')
    for row in cursor:
        if row[0] != "ARCHIVELOG":
            sys.exit("Database should be in archivelog mode")

    # Make sure that the database instance is open. It is possible to backup the database even if it is
    # mounted. But, it will have to be consistently dismounted. The script doesn't handle that case now
    click.echo("Checking if the database is open")
    cursor.execute('select status from v$instance')
    for row in cursor:
        if row[0] != 'OPEN':
            sys.exit("Database is not open")

    # Make sure spfile is in play
    cursor.execute("select count(*) from v$parameter where name = 'spfile' and value is not null")
    for row in cursor:
        if row[0] != 1:
            sys.exit("script requires the instance to be started with spfile")

    dbId = None
    dbName = None
    dbUniqueName = None
    # Get the name of the database
    click.echo("Getting database name and database unique name")
    cursor.execute('select dbid, name, db_unique_name from v$database')
    for row in cursor:
        dbId = row[0]
        dbName = row[1]
        dbUniqueName = row[2]
        click.echo("Database Id:%d Name:%s UniqueName:%s" % (dbId, dbName, dbUniqueName))

    charSet = None
    click.echo("Fetching character set")
    cursor.execute("select value$ from sys.props$ where name='NLS_CHARACTERSET'")
    for row in cursor:
        charSet = row[0]
        click.echo("Character Set:%s" % charSet)

    nCharSet = None
    click.echo("Fetching national character set")
    cursor.execute("select value$ from sys.props$ where name='NLS_NCHAR_CHARACTERSET'")
    for row in cursor:
        nCharSet = row[0]
        click.echo("National Character Set:%s" % nCharSet)

    racMode = 'FALSE'
    click.echo("Fetching rac mode")
    cursor.execute("select value from v$parameter where name='cluster_database'")
    for row in cursor:
        racMode = row[0]
        click.echo("Rac mode:%s" % racMode)

    pdbname = None
    cdbmode = None
    tdeenabled = False
    walletLoc = None

    # check if tde is enabled
    cursor.execute('select BITAND(flags, 8) from x$kcbdbk')
    for row in cursor:
        if row[0] == 8:
            tdeenabled = True

    if not tdeenabled:
        if not rmanpassword:
            sys.exit("TDE is not active in the instance. RMAN password is required")
    else:
        # TDE Enabled
        if rmanpassword:
            sys.exit("TDE is active in the instance. RMAN password should not be specified")
        cursor.execute('select upper(wrl_type), wrl_parameter, upper(status) from v$encryption_wallet where rownum < 2')
        for row in cursor:
            if (row[0] != 'FILE') or (row[2] != 'OPEN'):
                sys.exit("This operation requires the wallet to be in file and for it to be open")
            if row[1] is not None:
                walletLoc = os.path.expandvars(row[1])
            if row[1] is None or not os.path.isdir(walletLoc):
                sys.exit("Could not query the wallet file.\nPlease ensure that any environment variables referenced in sqlnet.ora file are set")

        versions = dbversion.split(".")
        if int(versions[0]) >= 12:
            cursor.execute('select upper(wallet_type) from v$encryption_wallet')
            for row in cursor:
                if row[0] != 'AUTOLOGIN' and row[0] != 'UNKNOWN':
                    sys.exit("Unsupported wallet type:" + row[0])

            cursor.execute('select cdb from v$database')
            for row in cursor:
                cdbmode = row[0]

            if cdbmode == "YES":
                pdbs = []
                cursor.execute("select name from v$containers where name <> 'CDB$ROOT' and open_mode like 'READ%'")
                for row in cursor:
                    pdbs.append(row[0])
                for pdb in pdbs:
                    cursor.execute('alter session set container = "' + pdb + '"')
                    cursor.execute(
                        'select upper(wrl_type), upper(status), upper(wallet_type), wrl_parameter from v$encryption_wallet')
                    for row in cursor:
                        if row[0] != 'FILE' or row[1] != 'OPEN' or (row[2] != 'AUTOLOGIN' and row[2] != 'UNKNOWN'):
                            sys.exit("PDB:" + pdb + " cannot be backed up")

    # Get the datasize and redosize
    dataSize = 0
    redoSize = 0
    cursor.execute('select sum(bytes)/1024/1024 from ( select sum(bytes) bytes from v$datafile union select sum(bytes) bytes from v$tempfile)')
    for row in cursor:
        dataSize = math.ceil(row[0])
    cursor.execute("select sum(bytes)/1024/1024 from (select sum(bytes*members) bytes from v$log where group# in " +  # noqa: W504
                   "(select group# from v$logfile where type='ONLINE') union select (BLOCK_SIZE*FILE_SIZE_BLKS) bytes from v$controlfile)")
    for row in cursor:
        redoSize = math.ceil(row[0])
    if dataSize == 0 or redoSize == 0:
        sys.exit("Failed to determine data size and/or redo size")

    # dump all initialization parameters. The most likely reason why restore will fail is
    # due to references to local system in initialization parameters
    cursor.execute("select name, value from v$parameter where isdefault = 'FALSE'")
    with open(os.path.join(tmpdir, "parameter.log"), 'w') as pf:
        for row in cursor:
            pf.write(row[0] + ":\t\t" + row[1] if row[1] else "<None>")
            pf.write("\n")

    cursor.close()
    db.close()

    # run rman once to make sure that it is running
    p = Popen([rman, "target", "/"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate(b'show all;')
    if err or not out or (p.returncode != 0):
        sys.exit("Error while test running rman")
    out = out.splitlines()
    if out[-1] != b'Recovery Manager complete.':
        sys.exit("Failed to successfully execute rman")

    client = cli_util.build_client('database', 'database', ctx)

    # Create Backup resource
    details = {}
    details['availabilityDomain'] = availability_domain
    if charSet:
        details['characterSet'] = charSet
    if nCharSet:
        details['ncharacterSet'] = nCharSet
    if 'edition' in kwargs and kwargs['edition']:
        details['databaseEdition'] = kwargs['edition']
    if dbName:
        details['dbName'] = dbName
    if 'display_name' in kwargs and kwargs['display_name']:
        details['displayName'] = kwargs['display_name']
    if dbUniqueName:
        details['dbUniqueName'] = dbUniqueName
    if dbId:
        details['externalDatabaseIdentifier'] = dbId
    details['databaseMode'] = 'SI' if racMode == 'FALSE' else 'RAC'
    details['dbVersion'] = dbversion
    details['pdbName'] = pdbname
    details['compartmentId'] = kwargs['compartment_id']

    click.echo("Creating external backup job resource...")
    backupId = None
    try:
        kwargs = {}
        result = client.create_external_backup_job(
            create_external_backup_job_details=details,
            **kwargs
        )
        backupId = result.data.backup_id
        click.echo("Created external backup job resource with id: " + backupId)

        # Check until the backup is ready
        while True:
            kwargs = {}
            result = client.get_external_backup_job(
                backup_id=backupId,
                **kwargs
            )

            if backupId != result.data.backup_id:
                sys.exit("Internal error, backupId mismatch. Please contact Oracle support")
            if result.data.provisioning:
                time.sleep(10)
                click.echo("Creating external backup job resource...")
                continue

            swiftPath = result.data.swift_path
            bucketName = result.data.bucket_name
            rmanTag = result.data.tag
            userName = result.data.user_name
            passWord = result.data.swift_password
            if swiftPath is None or \
                    bucketName is None or \
                    rmanTag is None or \
                    userName is None or \
                    passWord is None:
                sys.exit("Backup no longer exists")
            break

        # wait for object store credential to be available
        click.echo("Waiting for completion of external backup job...")
        time.sleep(300)

        if tdeenabled:
            # push the wallet to object store
            tdeWalletFile = os.path.join(tmpdir, 'tdeWallet.tar.gz')
            tdeWalletPath = swiftPath + '/' + bucketName + '/tdeWallet.tar.gz'
            click.echo("Compressing the wallet")
            with tarfile.open(tdeWalletFile, 'w:gz') as tar:
                tar.add(walletLoc, arcname=os.path.basename(walletLoc))
            click.echo("Uploading wallet")
            with open(tdeWalletFile, 'rb') as payload:
                response = requests.put(tdeWalletPath,
                                        auth=HTTPBasicAuth(userName, passWord),
                                        headers={'Content-Length': str(os.path.getsize(tdeWalletFile))},
                                        data=payload)
                response.raise_for_status()
        else:
            tdeWalletPath = None

        # push the parameter logs
        click.echo("Uploading parameter logs")
        with open(os.path.join(tmpdir, "parameter.log"), 'rb') as pf:
            response = requests.put(swiftPath + "/" + bucketName + "/" + "parameter.log",
                                    auth=HTTPBasicAuth(userName, passWord),
                                    headers={'Content-Length': str(os.path.getsize(os.path.join(tmpdir, "parameter.log")))},
                                    data=pf)
            response.raise_for_status()

        # Run opcInstaller
        cmd = "java -jar " + opcinstaller + " -host " + swiftPath + " -opcId '" + userName + "' -opcPass '" + passWord + \
              "' -walletDir " + tmpdir + " -libDir " + tmpdir + " -configFile " + \
              os.path.join(tmpdir, "opc" + os.environ['ORACLE_SID'] + ".ora") + " -container " + bucketName

        if additionalopcargs:
            cmd = cmd + " " + additionalopcargs

        click.echo("Setting up opc installer")

        cmd_redacted = "java -jar " + opcinstaller + " -host " + swiftPath + " -opcId '" + userName + "' -opcPass " + \
            "<redacted_password>" + " -walletDir " + tmpdir + " -libDir " + tmpdir + " -configFile " + \
            os.path.join(tmpdir, "opc" + os.environ['ORACLE_SID'] + ".ora") + " -container " + bucketName

        click.echo("Executing command: %s" % cmd_redacted)
        p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        if err or (p.returncode != 0):
            sys.exit("Failed to run opcInstaller cmd:" + cmd)
            print(out)
            print(err)

        # Make sure that config file, wallet and the library exists
        libfile = "libopc.so" if os.name != 'nt' else "libopc.dll"
        if not os.path.exists(os.path.join(tmpdir, "opc" + os.environ['ORACLE_SID'] + ".ora")) or \
                not os.path.exists(os.path.join(tmpdir, "cwallet.sso")) or \
                not os.path.exists(os.path.join(tmpdir, libfile)):
            sys.exit("Unexpected status from opcInstaller. Please contact Oracle support")

        # Create RMAN script
        script = open(os.path.join(tmpdir, "rman.sql"), "w")
        script.write("set echo on\n")
        if not tdeenabled:
            script.write("set encryption on identified by '" + rmanpassword + "' only;\n")
        else:
            script.write("set encryption on;\n")

        script.write("run {\n")
        for channel in range(rmanchannels):
            script.write("allocate channel odbms" + str(channel) + " type sbt " +            # noqa: W504
                         "PARMS='SBT_LIBRARY=" + tmpdir + os.path.sep + libfile + "," +      # noqa: W504
                         "SBT_PARMS=(OPC_PFILE=" + tmpdir + os.path.sep + "opc" + os.environ['ORACLE_SID'] + ".ora)';\n")
        script.write("backup as compressed backupset database tag '" + rmanTag + "' " +      # noqa: W504
                     "format '" + rmanTag + "__%d_%I_%U_%T_%t' " +                           # noqa: W504
                     "keep until time 'sysdate+29000' restore point '" + rmanTag + "';\n" +  # noqa: W504
                     "}\n")
        script.close()

        # Execute RMAN
        click.echo("Executing RMAN. It will take a few minutes to complete..")
        p = Popen([rman, "target", "/", "log", os.path.join(tmpdir, "rman.log"), "@" + os.path.join(tmpdir, "rman.sql")], stdin=PIPE,
                  stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        if err or (not out) or (p.returncode != 0):
            sys.exit("Error while running rman commands")
            print(out)
            print(err)

        with open(os.path.join(tmpdir, "rman.log"), 'rb') as rl:
            response = requests.put(swiftPath + "/" + bucketName + "/" + "rman.log",
                                    auth=HTTPBasicAuth(userName, passWord),
                                    headers={'Content-Length': str(os.path.getsize(os.path.join(tmpdir, "rman.log")))},
                                    data=rl)
            response.raise_for_status()

        # fetch the spfile and controlfile handles
        spfHandle = None
        cfHandle = None
        with open(os.path.join(tmpdir + os.sep + "rman.log")) as f:
            lines = f.readlines()
            lines = [x.strip() for x in lines]
            i = 0
            while i < len(lines):
                spf = (lines[i] == "including current SPFILE in backup set")
                if spf:
                    spfHandle = None if spf else 0
                    i = i + 3
                    if i < len(lines):
                        m = re.search('^piece handle=(.+?) tag=', lines[i])
                        if m:
                            spfHandle = m.group(1) if spf else 0
                cf = (lines[i] == "including current control file in backup set")
                if cf:
                    cfHandle = None if cf else 0
                    i = i + 3
                    if i < len(lines):
                        m = re.search('^piece handle=(.+?) tag=', lines[i])
                        if m:
                            cfHandle = m.group(1) if cf else 0
                else:
                    i = i + 1

        if spfHandle is None or cfHandle is None:
            sys.exit("Could not find spfile/controlfile Handle")

        click.echo("Completing the external backup job..")
        details = {}
        details['cfBackupHandle'] = cfHandle
        details['dataSize'] = dataSize
        details['redoSize'] = redoSize
        details['spfBackupHandle'] = spfHandle
        details['sqlPatches'] = []
        details['tdeWalletPath'] = tdeWalletPath
        result = client.complete_external_backup_job(
            backup_id=backupId,
            complete_external_backup_job_details=details,
            **kwargs
        )
        # print(details)
        click.echo("Response:%s" % result.status)
        click.echo("External Backup created.")
        backupId = None

    finally:
        if backupId is not None:
            click.echo("Deleting incomplete backup")
            kwargs = {}
            client.delete_backup(
                backup_id=backupId,
                **kwargs
            )
        shutil.rmtree(tmpdir)


if __name__ == '__main__':
    create_backup_from_onprem()
