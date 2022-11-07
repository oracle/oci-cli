# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import io
import os
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
    'oci==2.88.0',
    'arrow>=1.0.0',
    'certifi',
    'click==7.1.2',
    'cryptography>=3.2.1,<=37.0.2',
    'jmespath==0.10.0',
    'python-dateutil>=2.5.3,<3.0.0',
    'pytz>=2016.10',
    'six>=1.15.0',
    'terminaltables==3.1.0',
    'pyOpenSSL>=17.5.0,<=22.0.0',
    'PyYAML>=5.4,<6',
    'prompt-toolkit==3.0.29'
]

extras = {
    'db': ['cx_Oracle==8.3']
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
package_dirs[ALL_SERVICES_DIR] = os.path.join('.', ALL_SERVICES_DIR)
all_packages.extend([ALL_SERVICES_DIR])

# Populating package_dirs and all_packages from directories under services
packages = find_packages(where=".")
service_packages = []
for package in packages:
    if package.startswith("services"):
        service_packages.append(package)
        package_path = "."
        for pkg in package.split("."):
            package_dirs[package] = os.path.join(package_path, pkg)
            package_path = os.path.join(package_path, pkg)
all_packages.extend(service_packages)

setup(
    name='oci-cli',
    url='https://docs.cloud.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm',
    version=version,
    author='Oracle',
    author_email='joe.levy@oracle.com',
    description='Oracle Cloud Infrastructure CLI',
    long_description=readme,
    entry_points={
        'console_scripts': ["oci=oci_cli.cli:cli",
                            "create_backup_from_onprem=oci_cli.scripts.database.dbaas:create_backup_from_onprem"]
    },
    install_requires=requires,
    extras_require=extras,
    packages=all_packages,
    package_dir=package_dirs,
    include_package_data=True,
    python_requires='>=3.6',
    license="Universal Permissive License 1.0 or Apache License 2.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "License :: OSI Approved :: Universal Permissive License (UPL)",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ]
)
