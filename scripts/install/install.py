#!/usr/bin/env python
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.
#
# This script will install the Oracle Cloud Infrastructure CLI into a directory and create an executable
# at a specified file path that is the entry point into the CLI.
#

from __future__ import print_function
import argparse
import os
import os.path
import sys
import platform
import stat
import tarfile
import tempfile
import shutil
import subprocess
import hashlib
import glob
import ssl
import traceback
try:
    # Attempt to load python 3 module
    from urllib.request import urlopen
    from urllib.error import URLError
except ImportError:
    # Import python 2 version
    from urllib2 import urlopen, URLError

try:
    # Rename raw_input to input to support Python 2
    input = raw_input
except NameError:
    # Python 3 doesn't have raw_input
    pass


def is_windows():
    return sys.platform == 'win32'


optional_feature_list = ['db (will install cx_Oracle)']

ACCEPT_ALL_DEFAULTS = False

VIRTUALENV_VERSION = '15.0.0'
VIRTUALENV_ARCHIVE = VIRTUALENV_VERSION + '.tar.gz'
VIRTUALENV_DOWNLOAD_URL = 'https://github.com/pypa/virtualenv/archive/' + VIRTUALENV_ARCHIVE
VIRTUALENV_ARCHIVE_SHA256 = 'a9759798e8bf7398084ef08c5ba98d4fb38bf2d2d9897deb01ee5412af8804b8'

DEFAULT_INSTALL_DIR = os.path.expanduser(os.path.join('~', 'lib', 'oracle-cli'))
DEFAULT_EXEC_DIR = os.path.expanduser(os.path.join('~', 'bin'))
DEFAULT_SCRIPT_DIR = os.path.expanduser(os.path.join('~', 'bin', 'oci-cli-scripts'))
OCI_EXECUTABLE_NAME = 'oci.exe' if is_windows() else 'oci'
# 'bmcs' is deprecated and is retained for backwards compatibiity, it will be removed completely in March 2018.
BMCS_EXECUTABLE_NAME = 'bmcs.exe' if is_windows() else 'bmcs'
DBAAS_SCRIPT_NAME = 'create_backup_from_onprem.exe' if is_windows() else 'create_backup_from_onprem'

USER_BASH_RC = os.path.expanduser(os.path.join('~', '.bashrc'))
USER_BASH_PROFILE = os.path.expanduser(os.path.join('~', '.bash_profile'))
SOURCE_AUTOCOMPLETE_COMMAND_TEMPLATE = '[[ -e "{completion_file_path}" ]] && source "{completion_file_path}"'
RELATIVE_PATH_TO_AUTOCOMPLETE_SCRIPT = os.path.join('oci_cli', 'bin', 'oci_autocomplete.sh')
RELATIVE_PATH_TO_POWERSHELL_AUTOCOMPLETE_SCRIPT = os.path.join('oci_cli', 'bin', 'OciTabExpansion.ps1')
DEFAULT_OPTIONAL_FEATURES = ''  # Default is to not install any optional features during OCI CLI installation


class CLIInstallError(Exception):
    pass


def print_status(msg=''):
    print('-- ' + msg)


def prompt_input(msg):
    return input('\n===> ' + msg)


def prompt_input_with_default(msg, default):
    if ACCEPT_ALL_DEFAULTS:
        return default

    if default:
        return prompt_input("{} (leave blank to use '{}'): ".format(msg, default)) or default
    else:
        return prompt_input('{}: '.format(msg))


def prompt_y_n(msg, default=None):
    if default not in [None, 'y', 'n']:
        raise ValueError("Valid values for default are 'y', 'n' or None")
    y = 'Y' if default == 'y' else 'y'
    n = 'N' if default == 'n' else 'n'

    if ACCEPT_ALL_DEFAULTS:
        return default == y.lower()

    while True:
        ans = prompt_input('{} ({}/{}): '.format(msg, y, n))
        if ans.lower() == n.lower():
            return False
        if ans.lower() == y.lower():
            return True
        if default and not ans:
            return default == y.lower()


def exec_command(command_list, cwd=None, env=None):
    print_status('Executing: ' + str(command_list))
    subprocess.check_call(command_list, cwd=cwd, env=env)


def create_tmp_dir():
    tmp_dir = tempfile.mkdtemp()
    return tmp_dir


def create_dir(dir):
    if not os.path.isdir(dir):
        print_status("Creating directory '{}'.".format(dir))
        os.makedirs(dir)


def is_valid_sha256sum(a_file, expected_sum):
    sha256 = hashlib.sha256()
    with open(a_file, 'rb') as f:
        sha256.update(f.read())
    computed_hash = sha256.hexdigest()
    return expected_sum == computed_hash


def create_virtualenv(tmp_dir, install_dir):
    if DRY_RUN:
        print_status('dry-run: Skipping virtualenv setup')
        return
    download_location = os.path.join(tmp_dir, VIRTUALENV_ARCHIVE)
    print_status('Downloading virtualenv package from {}.'.format(VIRTUALENV_DOWNLOAD_URL))

    try:
        response = urlopen(VIRTUALENV_DOWNLOAD_URL)
    except URLError as e:
        if e.reason and isinstance(e.reason, ssl.SSLError):
            traceback.print_exc()
            sys.exit('ERROR: Failed to download virtualenv package. Please check that your trusted certificates are up to date and include the certificates necessary to verify github.com')
        else:
            raise e

    with open(download_location, 'wb') as f:
        f.write(response.read())
    print_status("Downloaded virtualenv package to {}.".format(download_location))
    if is_valid_sha256sum(download_location, VIRTUALENV_ARCHIVE_SHA256):
        print_status("Checksum of {} OK.".format(download_location))
    else:
        raise CLIInstallError("The checksum of the downloaded virtualenv package does not match.")
    print_status("Extracting '{}' to '{}'.".format(download_location, tmp_dir))
    package_tar = tarfile.open(download_location)
    package_tar.extractall(path=tmp_dir)
    package_tar.close()
    virtualenv_dir_name = 'virtualenv-' + VIRTUALENV_VERSION
    working_dir = os.path.join(tmp_dir, virtualenv_dir_name)

    # due to an issue with virtualenv on windows, we need to explicitly copy some dlls into the virtual environment
    # or the python executable in the virtualenv will crash upon invocation
    # for python 3 one possible alternative is to use venv instead of virtualenv
    if is_windows():
        print_status('Copying DLLs into virtualenv.')
        dest_dir = os.path.join(install_dir, 'Scripts')
        os.makedirs(dest_dir)
        src_dir = os.path.dirname(sys.executable)
        for dll in glob.glob(os.path.join(src_dir, '*.dll')):
            print_status('Copying {} to {}'.format(dll, dest_dir))
            shutil.copy(dll, dest_dir)

    cmd = [sys.executable, 'virtualenv.py', '--python', sys.executable, install_dir]
    exec_command(cmd, cwd=working_dir)


def install_cli(install_dir, tmp_dir, version, optional_features):
    if is_windows():
        path_to_pip = os.path.join(install_dir, 'Scripts', 'pip')
    else:
        path_to_pip = os.path.join(install_dir, 'bin', 'pip')

    # known issue on python 3 where shebang for scripts install using subprocess.call will not reference python executable from venv
    # fix is to unset this environment variable
    # https://github.com/pypa/virtualenv/issues/845
    env = dict(os.environ)
    if '__PYVENV_LAUNCHER__' in os.environ:
        env.pop('__PYVENV_LAUNCHER__')

    # The python installer handles 2 cases:
    # 1) full install zip bundles -- originally for distributing preview builds
    #    --oci-cli-version can be used to pick the version of the local whl package
    # 2) installation from pypi
    #    --oci-cli-version can be used to pick the version of oci-cli from pypi

    match_wheel = "oci_cli*.whl"
    cli_package_name = 'oci_cli'
    if version:
        cli_package_name += '==' + version
        match_wheel = "oci_cli*" + version + "*.whl"
    if (optional_features):
        cli_package_name += '[' + optional_features + ']'

    # Check if we should install a local full-install bundle.
    oci_cli_whl_files = glob.glob(match_wheel)
    if os.path.exists('./cli-deps') and len(oci_cli_whl_files) > 0:
        print_status("Installing {} from local resources.".format(oci_cli_whl_files[0]))
        cmd = [path_to_pip, 'install', '--cache-dir', tmp_dir, oci_cli_whl_files[0], '--upgrade', '--find-links', 'cli-deps']
    else:
        cmd = [path_to_pip, 'install', '--cache-dir', tmp_dir, cli_package_name, '--upgrade']

    if DRY_RUN:
        print_status('dry-run: Skipping CLI install, cmd=' + str(cmd))
        return
    exec_command(cmd, env=env)


def get_install_dir():
    install_dir = None
    while not install_dir:
        prompt_message = 'In what directory would you like to place the install?'
        install_dir = prompt_input_with_default(prompt_message, DEFAULT_INSTALL_DIR)
        install_dir = os.path.realpath(os.path.expanduser(install_dir))
        if ' ' in install_dir:
            print_status("The install directory '{}' cannot contain spaces.".format(install_dir))
            install_dir = None
        else:
            create_dir(install_dir)
            if os.listdir(install_dir):
                print_status("Install directory '{}' is not empty and may contain a previous installation.".format(install_dir))
                if ACCEPT_ALL_DEFAULTS:
                    # default behavior is to NOT delete an existing directory and re-prompt for install_dir, but we can't re-prompt if ACCEPT_ALL_DEFAULTS is set
                    sys.exit("Refusing to remove existing directory {}. Please remove directory manually and re-run installation script.".format(install_dir))

                ans_yes = prompt_y_n('Remove this directory?', 'n')
                if ans_yes:
                    try:
                        shutil.rmtree(install_dir)
                    except Exception:
                        sys.exit("Failed to remove directory: {}. Please remove directory manually and re-run installation script.".format(install_dir))

                    print_status("Deleted '{}'.".format(install_dir))
                    create_dir(install_dir)
                else:
                    # User opted to not delete the directory so ask for install directory again
                    install_dir = None
    print_status("We will install at '{}'.".format(install_dir))
    return install_dir


def get_exec_dir(install_dir):
    exec_dir = None
    while not exec_dir:
        prompt_message = "In what directory would you like to place the '{}' executable?".format(OCI_EXECUTABLE_NAME)
        exec_dir = prompt_input_with_default(prompt_message, DEFAULT_EXEC_DIR)
        exec_dir = os.path.realpath(os.path.expanduser(exec_dir))
        if ' ' in exec_dir:
            print_status("The executable directory '{}' cannot contain spaces.".format(exec_dir))
            exec_dir = None

        install_dir_bin_folder = 'Scripts' if is_windows() else 'bin'
        install_bin_dir = os.path.join(install_dir, install_dir_bin_folder)
        if exec_dir == install_bin_dir:
            print_status("The executable directory cannot be the same as the {} directory of the virtualenv. Adding this directory to your PATH could interfere with your system python installation.".format(install_dir_bin_folder))
            exec_dir = None

    create_dir(exec_dir)
    print_status("The executable will be in '{}'.".format(exec_dir))
    return exec_dir


def get_script_dir(install_dir):
    script_dir = None
    while not script_dir:
        prompt_message = "In what directory would you like to place the OCI scripts?"
        script_dir = prompt_input_with_default(prompt_message, DEFAULT_SCRIPT_DIR)
        script_dir = os.path.realpath(os.path.expanduser(script_dir))
        if ' ' in script_dir:
            print_status("The script directory '{}' cannot contain spaces.".format(script_dir))
            script_dir = None

        install_dir_bin_folder = 'Scripts' if is_windows() else 'bin'
        install_bin_dir = os.path.join(install_dir, install_dir_bin_folder)
        if script_dir == install_bin_dir:
            print_status("The script directory cannot be the same as the {} directory of the virtualenv. Adding this directory to your PATH could interfere with your system python installation.".format(install_dir_bin_folder))
            script_dir = None

    create_dir(script_dir)
    print_status("The scripts will be in '{}'.".format(script_dir))
    return script_dir


def get_optional_features():
    prompt_message = "Currently supported optional packages are: {}\n" \
                     "What optional CLI packages would you like to be installed (comma separated names; press enter if " \
                     "you don't need any optional packages)?".format(optional_feature_list)
    optional_features = prompt_input_with_default(prompt_message, DEFAULT_OPTIONAL_FEATURES)

    print_status("The optional packages installed will be '{}'.".format(optional_features))
    return optional_features


def _backup_rc(rc_file):
    try:
        shutil.copyfile(rc_file, rc_file + '.backup')
        print_status("Backed up '{}' to '{}'".format(rc_file, rc_file + '.backup'))
    except (OSError, IOError):
        pass


def _get_default_rc_file():
    bashrc_exists = os.path.isfile(USER_BASH_RC)
    bash_profile_exists = os.path.isfile(USER_BASH_PROFILE)
    if not bashrc_exists and bash_profile_exists:
        return USER_BASH_PROFILE
    if bashrc_exists and bash_profile_exists and platform.system().lower() == 'darwin':
        return USER_BASH_PROFILE
    return USER_BASH_RC if bashrc_exists else None


def _default_rc_file_creation_step():
    rcfile = USER_BASH_PROFILE if platform.system().lower() == 'darwin' else USER_BASH_RC
    ans_yes = prompt_y_n('Could not automatically find a suitable file to use. Create {} now?'.format(rcfile), default='y')
    if ans_yes:
        open(rcfile, 'a').close()
        return rcfile
    return None


def _find_line_in_file(file_path, search_pattern):
    try:
        with open(file_path, 'r') as search_file:
            for line in search_file:
                if search_pattern in line:
                    return True
    except (OSError, IOError):
        pass
    return False


def _modify_rc(rc_file_path, line_to_add):
    if not _find_line_in_file(rc_file_path, line_to_add):
        with open(rc_file_path, 'a') as rc_file:
            rc_file.write('\n' + line_to_add + '\n')


def get_rc_file_path():
    rc_file = None
    default_rc_file = _get_default_rc_file()
    if not default_rc_file:
        rc_file = _default_rc_file_creation_step()
    rc_file = rc_file or prompt_input_with_default('Enter a path to an rc file to update', default_rc_file)
    if rc_file:
        rc_file_path = os.path.realpath(os.path.expanduser(rc_file))
        if os.path.isfile(rc_file_path):
            return rc_file_path
        print_status("The file '{}' could not be found.".format(rc_file_path))
    return None


def warn_other_oci_or_bmcs_on_path(exec_dir, exec_filepath):
    env_path = os.environ.get('PATH')
    conflicting_paths = []
    if env_path:
        for p in env_path.split(':'):
            p_to_oci = os.path.join(p, OCI_EXECUTABLE_NAME)
            p_to_bmcs = os.path.join(p, BMCS_EXECUTABLE_NAME)
            if p != exec_dir:
                if os.path.isfile(p_to_oci):
                    conflicting_paths.append(p_to_oci)
                if os.path.isfile(p_to_bmcs):
                    conflicting_paths.append(p_to_bmcs)
    if conflicting_paths:
        print_status()
        print_status("** WARNING: Other '{}' or '{}' executables are on your $PATH. **".format(OCI_EXECUTABLE_NAME, BMCS_EXECUTABLE_NAME))
        print_status("Conflicting paths: {}".format(', '.join(conflicting_paths)))
        print_status("You can run this installation of the CLI with '{}'.".format(exec_filepath))


def handle_path_and_tab_completion(completion_file_path, exec_filepath, exec_dir, update_path_and_enable_tab_completion,
                                   rc_file_path):
    if DRY_RUN:
        print_status("dry-run: Skipping handle_path_and_tab_completion")
        print_status("dry-run: update_path_and_enable_tab_completion=" + str(update_path_and_enable_tab_completion))
        print_status("dry-run: rc_file_path=" + str(rc_file_path))
        return
    if is_windows():
        if update_path_and_enable_tab_completion:
            ans_yes = True
        else:
            ans_yes = prompt_y_n('Modify PATH to include the CLI and enable tab completion in PowerShell now?', 'y')
        if ans_yes:
            # Add autocomplete to the user's profile. Assume that powershell is on the path
            profile_file_path = subprocess.check_output(['powershell', '-NoProfile', 'echo $profile']).decode(sys.stdout.encoding).strip()
            if not os.path.exists(profile_file_path):
                if not os.path.exists(os.path.dirname(profile_file_path)):
                    os.makedirs(os.path.dirname(profile_file_path))

                with open(profile_file_path, 'w') as f:
                    f.write('. {}'.format(completion_file_path))
            else:
                with open(profile_file_path, 'a+') as f:
                    current_file_contents = f.read()

                    if current_file_contents.find(completion_file_path) >= 0:
                        # They have the tab completion script in the place we thought already. No action needed
                        pass
                    elif current_file_contents.find('OciTabExpansion.ps1') >= 0:
                        # They have the tab completion script, but not in the place we thought. Print out a warning
                        # but otherwise take no action on the profile
                        print_status()

                        format_str = "It looks like tab completion for oci is already configured in {profile_file_path}. If you wish to replace this with the tab completion script included in this version of the CLI, please remove any lines containing 'OciTabExpansion.ps1' from {profile_file_path} and then run 'oci setup autocomplete'"
                        print_status(format_str.format(profile_file_path=profile_file_path))
                    else:
                        # They don't have the tab completion script in their profile. Add it
                        f.write('\n. {}\n'.format(completion_file_path))

            # powershell one-liner to append the exec_dir to the USER path permanently
            # makes the assumption that powershell is on the PATH already
            command = "powershell -Command \"[Environment]::SetEnvironmentVariable(\\\"PATH\\\", \\\"{};\\\" + (Get-ItemProperty -Path 'Registry::HKEY_CURRENT_USER\Environment' -Name PATH).Path, \\\"User\\\")".format(exec_dir)  # noqa: W605
            subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
            print_status()
            print_status('** Close and re-open PowerShell to reload changes to your PATH **')
            print_status('In order to run the autocomplete script, you may also need to set your PowerShell execution policy to allow for running local scripts (as an Administrator run Set-ExecutionPolicy RemoteSigned in a PowerShell prompt)')
            print_status()
        else:
            print_status("If you change your mind, dot source {} in your PowerShell profile and restart your shell to enable tab completion.".format(completion_file_path))
            print_status("You can run the CLI with '{}'.".format(exec_filepath))
    else:
        if update_path_and_enable_tab_completion:
            ans_yes = True
        else:
            ans_yes = prompt_y_n('Modify profile to update your $PATH and enable shell/tab completion now?', 'y')
        if ans_yes:
            if rc_file_path is None:
                rc_file_path = get_rc_file_path()
            if not rc_file_path:
                raise CLIInstallError('No suitable profile file found.')
            _backup_rc(rc_file_path)
            line_to_add = "export PATH={}:$PATH".format(exec_dir)
            _modify_rc(rc_file_path, line_to_add)
            line_to_add = SOURCE_AUTOCOMPLETE_COMMAND_TEMPLATE.format(completion_file_path=completion_file_path)
            _modify_rc(rc_file_path, line_to_add)
            print_status('Tab completion set up complete.')
            print_status("If tab completion is not activated, verify that '{}' is sourced by your shell.".format(rc_file_path))
            warn_other_oci_or_bmcs_on_path(exec_dir, exec_filepath)
            print_status()
            print_status('** Run `exec -l $SHELL` to restart your shell. **')
            print_status()
        else:
            print_status("If you change your mind, add 'source {}' to your rc file and restart your shell to enable tab completion.".format(completion_file_path))
            print_status("You can run the CLI with '{}'.".format(exec_filepath))


def verify_python_version():
    print_status('Verifying Python version.')
    v = sys.version_info
    valid_version = v >= (2, 7, 5) if v.major == 2 else v >= (3, 5, 0)
    if not valid_version:
        raise CLIInstallError('The CLI does not support Python 2 versions less than 2.7.5 or Python 3 versions less than 3.5.0.')
    if 'conda' in sys.version:
        raise CLIInstallError("This script does not support the Python Anaconda environment. "
                              "Create an Anaconda virtual environment and install with 'pip'")
    print_status('Python version {}.{}.{} okay.'.format(v.major, v.minor, v.micro))


# This code is being deprecated.  See verify_native_dependencies() below.
def _native_dependencies_for_dist(verify_cmd_args, update_cmd_args, install_cmd_args, dep_list):
    try:
        print_status("Executing: '{} {}'".format(' '.join(verify_cmd_args), ' '.join(dep_list)))
        subprocess.check_output(verify_cmd_args + dep_list, stderr=subprocess.STDOUT)
        print_status('Native dependencies okay.')
    except subprocess.CalledProcessError:
        err_msg = 'One or more of the following native dependencies are not currently installed and may be required.\n'
        err_msg += '"{}"'.format(' '.join(install_cmd_args + dep_list))
        print_status(err_msg)

        prompt = 'Missing native dependencies. Continue and install the following dependencies: {}?'.format(', '.join(dep_list))
        ans_yes = prompt_y_n(prompt, 'y')
        if not ans_yes:
            raise CLIInstallError('Please install the native dependencies and try again.')

        # run command to update packages for this OS (e.g. apt-get update)
        subprocess.call(update_cmd_args)

        # run command to install packages using native package manager (e.g. apt-get install {deps})
        subprocess.call(install_cmd_args + dep_list)


# This code is being deprecated.
# Also the name is a little goofy as it does more than just verify your system, it actually can modify your system.
# Installing native dependencies on ubuntu 18, may cause the system to restart which is disruptive to this installer.
# By removing this code we are removing the dependency for needing elevated sudo privs to run this script.
# We also no longer need to compile the crypto python package, so it will also speed things up.
#
# We already have OS specific front end scripts, install.sh and install.ps1.
# Any OS native dependencies should be done in one of those front end scripts.
# They will already require elevated sudo privs in order to install python, if it is not present.
#
# This will give flexibility to organizations to have sysadmins install system requirements whereas this
# python CLI installer can be run by average users without elevated sudo permissions.
def verify_native_dependencies():
    distname, version, _ = platform.linux_distribution()
    if not distname:
        # There's no distribution name so can't determine native dependencies required / or they may not be needed like on OS X
        return
    print_status('Verifying native dependencies.')
    is_python3 = sys.version_info[0] == 3
    distname = distname.lower().strip()
    verify_cmd_args = None
    install_cmd_args = None
    dep_list = None
    if any(x in distname for x in ['ubuntu', 'debian']):
        verify_cmd_args = ['dpkg', '-s']
        update_cmd_args = ['sudo', 'apt-get', 'update']
        install_cmd_args = ['sudo', 'apt-get', 'install', '-y']
        python_dep = 'python3-dev' if is_python3 else 'python-dev'
        if distname == 'ubuntu' and version in ['12.04', '14.04'] or distname == 'debian' and version.startswith('7'):
            dep_list = ['libssl-dev', 'libffi-dev', python_dep]
        elif distname == 'ubuntu' and version in ['15.10', '16.04', '18.04'] or distname == 'debian' and (version.startswith('8') or version.startswith('10')):
            dep_list = ['libssl-dev', 'libffi-dev', python_dep, 'build-essential']
    elif any(x in distname for x in ['centos', 'rhel', 'red hat']):
        verify_cmd_args = ['rpm', '-q']
        update_cmd_args = ['sudo', 'yum', 'check-update']
        install_cmd_args = ['sudo', 'yum', 'install', '-y']
        # python3-devel not available on yum but python3Xu-devel versions available.
        python_dep = 'python3{}u-devel'.format(sys.version_info[1]) if is_python3 else 'python-devel'
        dep_list = ['gcc', 'libffi-devel', python_dep, 'openssl-devel']
    if verify_cmd_args and install_cmd_args and dep_list:
        if DRY_RUN:
            print_status("dry-run: Skipping native_dependencies execution.")
            print_status("dry-run: verify_cmd_args=" + str(verify_cmd_args))
            print_status("dry-run: update_cmd_args=" + str(update_cmd_args))
            print_status("dry-run: install_cmd_args=" + str(install_cmd_args))
            print_status("dry-run: dep_list=" + str(dep_list))
        _native_dependencies_for_dist(verify_cmd_args, update_cmd_args, install_cmd_args, dep_list)
    else:
        print_status("Unable to verify native dependencies. dist={}, version={}. Continuing...".format(distname, version))


def verify_install_dir_exec_path_conflict(install_dir, exec_path):
    if install_dir == exec_path:
        raise CLIInstallError("The executable file '{}' would clash with the install directory of '{}'. Choose either a different install directory or directory to place the executable.".format(exec_path, install_dir))


def main():
    parser = argparse.ArgumentParser(description='Install Oracle Cloud Infrastructure CLI.')
    parser.add_argument('--accept-all-defaults', action='store_true',
                        help='If this flag is specified, no user prompts will be displayed and all default prompt '
                             'responses will be used. This flag can be used in combination with other input '
                             'parameters/flags. When used with other parameters/flags, other parameter values '
                             'mentioned on command line take precedence over default values.')
    parser.add_argument('--optional-features', help="""This input param is used to specify any optional
                         features that need to be installed as part of OCI CLI install .e.g. to run dbaas script
                         'create_backup_from_onprem', users need to install optional "db" feature which will install
                         dependent cxOracle package. Use this optional input param as follows:
                         --optional-features feature1,feature2""")
    parser.add_argument('--install-dir', help='This input parameter allows the user to specify the directory where '
                                              'CLI installation is done.')
    parser.add_argument('--exec-dir', help='This input parameter allows the user to specify the directory where CLI '
                                           'executable is stored.')
    parser.add_argument('--update-path-and-enable-tab-completion', action='store_true',
                        help='If this flag is specified, the PATH environment variable is updated to include CLI '
                             'executable and tab auto completion of CLI commands is enabled. It does require rc '
                             'file path in *NIX systems which can be either given interactively or using the '
                             '--rc-file-path option')
    parser.add_argument('--rc-file-path', help='This input param is used in *NIX systems to update the corresponding '
                                               'shell rc file with command auto completion and modification to '
                                               'PATH environment variable with CLI executable path. It requires '
                                               'shell\'s rc file path. e.g. ~/.bashrc. Ideally, should be used with '
                                               'the --update-path-and-enable-tab-completion option')
    parser.add_argument('--oci-cli-version', help='The pip version of CLI to install.')
    parser.add_argument('--dry-run', action='store_true', help='Do not install virtualenv or CLI but go through the motions.')
    parser.add_argument('--verify-native-dependencies', action='store_true',
                        help='Check whether linux native dependencies are available to compile modules like cryptography.')
    args = parser.parse_args()
    global ACCEPT_ALL_DEFAULTS
    ACCEPT_ALL_DEFAULTS = args.accept_all_defaults
    global DRY_RUN
    DRY_RUN = args.dry_run
    OPTIONAL_FEATURES = args.optional_features
    install_dir = args.install_dir
    exec_dir = args.exec_dir

    verify_python_version()
    if args.verify_native_dependencies:
        verify_native_dependencies()
    tmp_dir = create_tmp_dir()
    if install_dir is None:
        install_dir = get_install_dir()
    else:
        # Create the install directory provided by the user if it does not exist
        create_dir(install_dir)
    if exec_dir is None:
        exec_dir = get_exec_dir(install_dir)
    else:
        # Create the executable directory provided by the user if it does not exist
        create_dir(exec_dir)
    script_dir = get_script_dir(install_dir)
    if OPTIONAL_FEATURES is None:
        OPTIONAL_FEATURES = get_optional_features()

    oci_exec_path = os.path.join(exec_dir, OCI_EXECUTABLE_NAME)
    bmcs_exec_path = os.path.join(exec_dir, BMCS_EXECUTABLE_NAME)
    dbaas_exec_path = os.path.join(script_dir, DBAAS_SCRIPT_NAME)
    verify_install_dir_exec_path_conflict(install_dir, oci_exec_path)
    verify_install_dir_exec_path_conflict(install_dir, bmcs_exec_path)
    create_virtualenv(tmp_dir, install_dir)
    install_cli(install_dir, tmp_dir, args.oci_cli_version, OPTIONAL_FEATURES)

    if DRY_RUN:
        print_status("dry-run: Skipping copying files to Scripts/bin directories.")
        print_status("dry-run: exec_dir=" + exec_dir)
        completion_file_path = None
    elif is_windows():
        venv_python_executable = os.path.join(install_dir, 'Scripts', 'python')
        venv_site_packages_directory = subprocess.check_output([venv_python_executable, '-c', 'from distutils.sysconfig import get_python_lib; print(get_python_lib())']).strip()
        completion_file_path = os.path.join(venv_site_packages_directory.decode(sys.stdout.encoding), RELATIVE_PATH_TO_POWERSHELL_AUTOCOMPLETE_SCRIPT)

        # copy the executable created from the pip install to the bin directory specified by the user
        shutil.copyfile(os.path.join(install_dir, 'Scripts', OCI_EXECUTABLE_NAME), oci_exec_path)
        shutil.copyfile(os.path.join(install_dir, 'Scripts', BMCS_EXECUTABLE_NAME), bmcs_exec_path)
        shutil.copyfile(os.path.join(install_dir, 'Scripts', DBAAS_SCRIPT_NAME), dbaas_exec_path)
    else:
        # copy the executable created from the pip install to the bin directory specified by the user
        shutil.copyfile(os.path.join(install_dir, 'bin', OCI_EXECUTABLE_NAME), oci_exec_path)
        shutil.copyfile(os.path.join(install_dir, 'bin', BMCS_EXECUTABLE_NAME), bmcs_exec_path)
        shutil.copyfile(os.path.join(install_dir, 'bin', DBAAS_SCRIPT_NAME), dbaas_exec_path)

        oci_exec_cur_stat = os.stat(oci_exec_path)
        bmcs_exec_cur_stat = os.stat(bmcs_exec_path)
        dbaas_exec_cur_stat = os.stat(dbaas_exec_path)
        os.chmod(oci_exec_path, oci_exec_cur_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        os.chmod(bmcs_exec_path, bmcs_exec_cur_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        os.chmod(dbaas_exec_path, dbaas_exec_cur_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

        # find the site-packages directory in the virtual environment where we installed oci
        # and use the autocomplete script contained in the bin/ directory
        venv_python_executable = os.path.join(install_dir, 'bin', 'python')
        venv_site_packages_directory = subprocess.check_output([venv_python_executable, '-c', 'from distutils.sysconfig import get_python_lib; print(get_python_lib())']).strip()
        completion_file_path = os.path.join(venv_site_packages_directory.decode(sys.stdout.encoding), RELATIVE_PATH_TO_AUTOCOMPLETE_SCRIPT)

    try:
        # this function prints out the executable location so we only want to point users to 'oci'
        handle_path_and_tab_completion(completion_file_path, oci_exec_path, exec_dir,
                                       args.update_path_and_enable_tab_completion, args.rc_file_path)
    except Exception as e:
        print_status("Unable to set up tab completion. ERROR: {}".format(str(e)))

    shutil.rmtree(tmp_dir)
    print_status("Installation successful.")
    print_status("Run the CLI with {} --help".format(oci_exec_path))


if __name__ == '__main__':
    try:
        main()
    except CLIInstallError as cie:
        print('ERROR: ' + str(cie), file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print('\n\nExiting...')
        sys.exit(1)
