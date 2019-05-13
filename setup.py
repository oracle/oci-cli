# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import io
import os
import sys
import re
from setuptools import setup, find_packages


def open_relative(*path):
    """
    Opens files in read-only with a fixed utf-8 encoding.

    All locations are relative to this setup.py file.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(here, *path)
    return io.open(filename, mode="r", encoding="utf-8")

with open_relative("src", "oci_cli", "version.py") as fd:
    version = re.search(
        r"^__version__\s*=\s*['\"]([^'\"]*)['\"]",
        fd.read(), re.MULTILINE).group(1)
    if not version:
        raise RuntimeError("Cannot find version information")

with open_relative("README.rst") as f:
    readme = f.read()

requires = [
    'oci==2.2.9',
    'arrow==0.10.0',
    'certifi',
    'click==6.7',
    'configparser==3.5.0',
    'cryptography==2.4.2',
    'httpsig_cffi==15.0.0',
    'jmespath==0.9.3',
    'python-dateutil==2.7.3',
    'pytz==2016.10',
    'retrying==1.3.3',
    'six==1.11.0',
    'terminaltables==3.1.0',
    'idna>=2.5,<2.7',
    'pyOpenSSL==18.0.0',
    'PyYAML==3.13'
]

extras = {
    'db': ['cx_Oracle==7.0']
}

fips_libcrypto_file = os.getenv("OCI_CLI_FIPS_LIBCRYPTO_FILE")
if fips_libcrypto_file:
    from setuptools.command.easy_install import ScriptWriter
    with open('src/oci_cli/oci_template.py', 'r') as template_file:
        template = template_file.read()
        ScriptWriter.template = template

ALL_SERVICES_DIR = "services"
package_dirs = {"": "src"}
all_packages = find_packages(where="src")
# Populating package_dirs and all_packages from directories outside of src/oci_cli
python_cli_root_dir = "."  # absolute paths are not allowed in setup
for spec_dir_name in os.listdir(python_cli_root_dir + '/' + ALL_SERVICES_DIR):
    if os.path.isdir(os.path.join(python_cli_root_dir, ALL_SERVICES_DIR, spec_dir_name)):
        spec_dir_src = os.path.join(python_cli_root_dir, ALL_SERVICES_DIR, spec_dir_name, "src")
        packages = find_packages(where=spec_dir_src)
        for package in packages:
            package_path = os.path.join(ALL_SERVICES_DIR, spec_dir_name, "src")
            for pkg in package.split("."):
                package_dirs[package] = os.path.join(package_path, pkg)
                package_path = os.path.join(package_path, pkg)
        all_packages.extend(packages)

setup(
    name='oci-cli',
    url='https://docs.cloud.oracle.com/Content/API/SDKDocs/cli.htm',
    version=version,
    author='Oracle',
    author_email='joe.levy@oracle.com',
    description='Oracle Cloud Infrastructure CLI',
    long_description=readme,
    entry_points={
        'console_scripts': ["bmcs=oci_cli.cli:cli", "oci=oci_cli.cli:cli",
                            "create_backup_from_onprem=oci_cli.scripts.database.dbaas:create_backup_from_onprem"]
    },
    install_requires=requires,
    extras_require=extras,
    packages=all_packages,
    package_dir=package_dirs,
    include_package_data=True,
    license="Universal Permissive License 1.0 or Apache License 2.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "License :: OSI Approved :: Universal Permissive License (UPL)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)
