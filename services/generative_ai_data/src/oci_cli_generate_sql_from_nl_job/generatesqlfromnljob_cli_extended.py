import click  # noqa: F401
import json  # noqa: F401
from services.generative_ai_data.src.oci_cli_generate_sql_from_nl_job.generated import generatesqlfromnljob_cli
from oci_cli import cli_util  # noqa: F401
from oci_cli import custom_types  # noqa: F401
from oci_cli import json_skeleton_utils  # noqa: F401
# Remove redundant subcommand
generatesqlfromnljob_cli.generate_sql_from_nl_job_group.commands.pop(generatesqlfromnljob_cli.generate_sql_from_nl.name)
generatesqlfromnljob_cli.generate_sql_from_nl_job_root_group.add_command(generatesqlfromnljob_cli.generate_sql_from_nl)
generatesqlfromnljob_cli.generate_sql_from_nl_job_root_group.commands.pop(generatesqlfromnljob_cli.generate_sql_from_nl_job_group.name)