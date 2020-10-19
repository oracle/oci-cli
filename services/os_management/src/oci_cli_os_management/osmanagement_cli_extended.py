# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import click

from services.os_management.src.oci_cli_os_management.generated import osmanagement_cli
from oci_cli import cli_util
from oci_cli import json_skeleton_utils

# Managed Instance - rename commands
managed_instance_group = osmanagement_cli.managed_instance_group
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.install_all_package_updates_on_managed_instance, "install-all-updates")
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.install_package_on_managed_instance, "install-package")
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.install_package_update_on_managed_instance, "install-update")
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.list_available_packages_for_managed_instance, "list-available-packages")
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.list_available_updates_for_managed_instance, "list-available-updates")
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.list_available_software_sources_for_managed_instance, "list-available-software-sources")
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.list_packages_installed_on_managed_instance, "list-installed-packages")
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.remove_package_from_managed_instance, "remove-package")

cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.install_all_windows_updates_on_managed_instance, "install-all-windows-updates")
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.install_windows_update_on_managed_instance, "install-windows-update")
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.list_available_windows_updates_for_managed_instance, "list-available-windows-updates")
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.list_windows_updates_installed_on_managed_instance, "list-installed-windows-updates")


# rename the parameter software-package-name to just be package-name
@cli_util.copy_params_from_generated_command(osmanagement_cli.remove_package_from_managed_instance, params_to_exclude=['software_package_name'])
@cli_util.option('--package-name', required=True, help="""Name of package to be removed. This should be the full package name including version and architecture""")
@osmanagement_cli.managed_instance_group.command(name='remove-package', help=osmanagement_cli.remove_package_from_managed_instance.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def remove_package_from_managed_instance(ctx, **kwargs):
    if 'package_name' in kwargs:
        kwargs['software_package_name'] = kwargs['package_name']
        kwargs.pop('package_name')

    ctx.invoke(osmanagement_cli.remove_package_from_managed_instance, **kwargs)


# rename the parameter software-package-name to just be package-name
@cli_util.copy_params_from_generated_command(osmanagement_cli.install_package_on_managed_instance, params_to_exclude=['software_package_name'])
@cli_util.option('--package-name', required=True, help="""Name of package to be installed. This should be the full package name including version and architecture""")
@osmanagement_cli.managed_instance_group.command(name='install-package', help=osmanagement_cli.install_package_on_managed_instance.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def install_package_on_managed_instance(ctx, **kwargs):
    if 'package_name' in kwargs:
        kwargs['software_package_name'] = kwargs['package_name']
        kwargs.pop('package_name')

    ctx.invoke(osmanagement_cli.install_package_on_managed_instance, **kwargs)


# rename the parameter software-package-name to just be package-name
@cli_util.copy_params_from_generated_command(osmanagement_cli.install_package_update_on_managed_instance, params_to_exclude=['software_package_name'])
@cli_util.option('--package-name', required=True, help="""Name of update to be installed. This should be the full package name including version and architecture""")
@osmanagement_cli.managed_instance_group.command(name='install-update', help=osmanagement_cli.install_package_update_on_managed_instance.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def install_package_update_on_managed_instance(ctx, **kwargs):
    if 'package_name' in kwargs:
        kwargs['software_package_name'] = kwargs['package_name']
        kwargs.pop('package_name')

    ctx.invoke(osmanagement_cli.install_package_update_on_managed_instance, **kwargs)


# changing name of remove to be remove-package to be consistent with install-package
cli_util.rename_command(osmanagement_cli, managed_instance_group, remove_package_from_managed_instance, "remove-package")


# The generated commands for attach/detach software source dropped the parent/child part and mapped both the parent and child
# operations to the same command.
# rename commands for attach-parent, detach-parent and attach-child, detach-child
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.attach_child_software_source_to_managed_instance, 'attach-child')
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.attach_parent_software_source_to_managed_instance, 'attach-parent')
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.detach_child_software_source_from_managed_instance, 'detach-child')
cli_util.rename_command(osmanagement_cli, managed_instance_group, osmanagement_cli.detach_parent_software_source_from_managed_instance, 'detach-parent')

#
# Scheduled Job commands
#

# rename commands
scheduled_job_group = osmanagement_cli.scheduled_job_group
cli_util.rename_command(osmanagement_cli, scheduled_job_group, osmanagement_cli.skip_next_scheduled_job_execution, "skip-next-execution")
cli_util.rename_command(osmanagement_cli, scheduled_job_group, osmanagement_cli.run_scheduled_job_now, "run-now")

#
# Software Source commands
#

# rename commands
software_source_group = osmanagement_cli.software_source_group
cli_util.rename_command(osmanagement_cli, software_source_group, osmanagement_cli.get_software_package, "get-package")
cli_util.rename_command(osmanagement_cli, software_source_group, osmanagement_cli.list_software_source_packages, "list-packages")
cli_util.rename_command(osmanagement_cli, software_source_group, osmanagement_cli.search_software_packages, "search-packages")
cli_util.rename_command(osmanagement_cli, software_source_group, osmanagement_cli.add_packages_to_software_source, "add-packages")
cli_util.rename_command(osmanagement_cli, software_source_group, osmanagement_cli.remove_packages_from_software_source, "remove-packages")


# rename the parameter software-package-name to just be package-name
@cli_util.copy_params_from_generated_command(osmanagement_cli.get_software_package, params_to_exclude=['software_package_name'])
@cli_util.option('--package-name', required=True, help="""Name of package to retrieve. This should be the full package name including version and architecture""")
@osmanagement_cli.software_source_group.command(name='get-package', help=osmanagement_cli.get_software_package.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_software_package(ctx, **kwargs):
    if 'package_name' in kwargs:
        kwargs['software_package_name'] = kwargs['package_name']
        kwargs.pop('package_name')

    ctx.invoke(osmanagement_cli.get_software_package, **kwargs)


# rename the parameter software-package-name to just be package-name
@cli_util.copy_params_from_generated_command(osmanagement_cli.search_software_packages, params_to_exclude=['software_package_name'])
@cli_util.option('--package-name', help="""Name of package for which to search. This should be the full package name including version and architecture""")
@osmanagement_cli.software_source_group.command(name='search-packages', help=osmanagement_cli.search_software_packages.help)
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def search_software_packages(ctx, **kwargs):
    if 'package_name' in kwargs:
        kwargs['software_package_name'] = kwargs['package_name']
        kwargs.pop('package_name')

    ctx.invoke(osmanagement_cli.search_software_packages, **kwargs)


#
# Work Request commands
#

# rename commands
work_request_group = osmanagement_cli.work_request_group
cli_util.rename_command(osmanagement_cli, work_request_group, osmanagement_cli.list_work_request_errors, "list-errors")
cli_util.rename_command(osmanagement_cli, work_request_group, osmanagement_cli.list_work_request_logs, "list-logs")

#
# Work Request Summary
#

# rename command to be list instead of list-work-requests
work_request_summary_group = osmanagement_cli.work_request_summary_group
cli_util.rename_command(osmanagement_cli, work_request_summary_group, osmanagement_cli.list_work_requests, "list")

# move command from work request summary group and add it to work request group
work_request_summary_group.commands.pop(osmanagement_cli.list_work_requests.name)
work_request_group.add_command(osmanagement_cli.list_work_requests)

# remove the work request summary command from the top-level
osmanagement_cli.os_management_root_group.commands.pop(work_request_summary_group.name)
