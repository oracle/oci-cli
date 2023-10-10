# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates. All rights reserved.

SDK_client_map = {
    "devops.approve_deployment": "oci.devops.DevopsClient.approve_deployment",
    "devops.cancel_build_run": "oci.devops.DevopsClient.cancel_build_run",
    "devops.cancel_deployment": "oci.devops.DevopsClient.cancel_deployment",
    "devops.cancel_scheduled_cascading_project_deletion": "oci.devops.DevopsClient.cancel_scheduled_cascading_project_deletion",
    "devops.change_project_compartment": "oci.devops.DevopsClient.change_project_compartment",
    "devops.create_build_pipeline": "oci.devops.DevopsClient.create_build_pipeline",
    "devops.create_build_pipeline_stage": "oci.devops.DevopsClient.create_build_pipeline_stage",
    "devops.create_build_run": "oci.devops.DevopsClient.create_build_run",
    "devops.create_connection": "oci.devops.DevopsClient.create_connection",
    "devops.create_deploy_artifact": "oci.devops.DevopsClient.create_deploy_artifact",
    "devops.create_deploy_environment": "oci.devops.DevopsClient.create_deploy_environment",
    "devops.create_deploy_pipeline": "oci.devops.DevopsClient.create_deploy_pipeline",
    "devops.create_deploy_stage": "oci.devops.DevopsClient.create_deploy_stage",
    "devops.create_deployment": "oci.devops.DevopsClient.create_deployment",
    "devops.create_project": "oci.devops.DevopsClient.create_project",
    "devops.create_repository": "oci.devops.DevopsClient.create_repository",
    "devops.create_trigger": "oci.devops.DevopsClient.create_trigger",
    "devops.delete_build_pipeline": "oci.devops.DevopsClient.delete_build_pipeline",
    "devops.delete_build_pipeline_stage": "oci.devops.DevopsClient.delete_build_pipeline_stage",
    "devops.delete_connection": "oci.devops.DevopsClient.delete_connection",
    "devops.delete_deploy_artifact": "oci.devops.DevopsClient.delete_deploy_artifact",
    "devops.delete_deploy_environment": "oci.devops.DevopsClient.delete_deploy_environment",
    "devops.delete_deploy_pipeline": "oci.devops.DevopsClient.delete_deploy_pipeline",
    "devops.delete_deploy_stage": "oci.devops.DevopsClient.delete_deploy_stage",
    "devops.delete_project": "oci.devops.DevopsClient.delete_project",
    "devops.delete_ref": "oci.devops.DevopsClient.delete_ref",
    "devops.delete_repository": "oci.devops.DevopsClient.delete_repository",
    "devops.delete_trigger": "oci.devops.DevopsClient.delete_trigger",
    "devops.get_build_pipeline": "oci.devops.DevopsClient.get_build_pipeline",
    "devops.get_build_pipeline_stage": "oci.devops.DevopsClient.get_build_pipeline_stage",
    "devops.get_build_run": "oci.devops.DevopsClient.get_build_run",
    "devops.get_commit": "oci.devops.DevopsClient.get_commit",
    "devops.get_commit_diff": "oci.devops.DevopsClient.get_commit_diff",
    "devops.get_connection": "oci.devops.DevopsClient.get_connection",
    "devops.get_deploy_artifact": "oci.devops.DevopsClient.get_deploy_artifact",
    "devops.get_deploy_environment": "oci.devops.DevopsClient.get_deploy_environment",
    "devops.get_deploy_pipeline": "oci.devops.DevopsClient.get_deploy_pipeline",
    "devops.get_deploy_stage": "oci.devops.DevopsClient.get_deploy_stage",
    "devops.get_deployment": "oci.devops.DevopsClient.get_deployment",
    "devops.get_file_diff": "oci.devops.DevopsClient.get_file_diff",
    "devops.get_mirror_record": "oci.devops.DevopsClient.get_mirror_record",
    "devops.get_object": "oci.devops.DevopsClient.get_object",
    "devops.get_object_content": "oci.devops.DevopsClient.get_object_content",
    "devops.get_project": "oci.devops.DevopsClient.get_project",
    "devops.get_ref": "oci.devops.DevopsClient.get_ref",
    "devops.get_repo_file_diff": "oci.devops.DevopsClient.get_repo_file_diff",
    "devops.get_repo_file_lines": "oci.devops.DevopsClient.get_repo_file_lines",
    "devops.get_repository": "oci.devops.DevopsClient.get_repository",
    "devops.get_repository_archive_content": "oci.devops.DevopsClient.get_repository_archive_content",
    "devops.get_repository_file_lines": "oci.devops.DevopsClient.get_repository_file_lines",
    "devops.get_trigger": "oci.devops.DevopsClient.get_trigger",
    "devops.get_work_request": "oci.devops.DevopsClient.get_work_request",
    "devops.list_authors": "oci.devops.DevopsClient.list_authors",
    "devops.list_build_pipeline_stages": "oci.devops.DevopsClient.list_build_pipeline_stages",
    "devops.list_build_pipelines": "oci.devops.DevopsClient.list_build_pipelines",
    "devops.list_build_runs": "oci.devops.DevopsClient.list_build_runs",
    "devops.list_commit_diffs": "oci.devops.DevopsClient.list_commit_diffs",
    "devops.list_commits": "oci.devops.DevopsClient.list_commits",
    "devops.list_connections": "oci.devops.DevopsClient.list_connections",
    "devops.list_deploy_artifacts": "oci.devops.DevopsClient.list_deploy_artifacts",
    "devops.list_deploy_environments": "oci.devops.DevopsClient.list_deploy_environments",
    "devops.list_deploy_pipelines": "oci.devops.DevopsClient.list_deploy_pipelines",
    "devops.list_deploy_stages": "oci.devops.DevopsClient.list_deploy_stages",
    "devops.list_deployments": "oci.devops.DevopsClient.list_deployments",
    "devops.list_mirror_records": "oci.devops.DevopsClient.list_mirror_records",
    "devops.list_paths": "oci.devops.DevopsClient.list_paths",
    "devops.list_projects": "oci.devops.DevopsClient.list_projects",
    "devops.list_refs": "oci.devops.DevopsClient.list_refs",
    "devops.list_repositories": "oci.devops.DevopsClient.list_repositories",
    "devops.list_triggers": "oci.devops.DevopsClient.list_triggers",
    "devops.list_work_request_errors": "oci.devops.DevopsClient.list_work_request_errors",
    "devops.list_work_request_logs": "oci.devops.DevopsClient.list_work_request_logs",
    "devops.list_work_requests": "oci.devops.DevopsClient.list_work_requests",
    "devops.mirror_repository": "oci.devops.DevopsClient.mirror_repository",
    "devops.put_repository_ref": "oci.devops.DevopsClient.put_repository_ref",
    "devops.schedule_cascading_project_deletion": "oci.devops.DevopsClient.schedule_cascading_project_deletion",
    "devops.update_build_pipeline": "oci.devops.DevopsClient.update_build_pipeline",
    "devops.update_build_pipeline_stage": "oci.devops.DevopsClient.update_build_pipeline_stage",
    "devops.update_build_run": "oci.devops.DevopsClient.update_build_run",
    "devops.update_connection": "oci.devops.DevopsClient.update_connection",
    "devops.update_deploy_artifact": "oci.devops.DevopsClient.update_deploy_artifact",
    "devops.update_deploy_environment": "oci.devops.DevopsClient.update_deploy_environment",
    "devops.update_deploy_pipeline": "oci.devops.DevopsClient.update_deploy_pipeline",
    "devops.update_deploy_stage": "oci.devops.DevopsClient.update_deploy_stage",
    "devops.update_deployment": "oci.devops.DevopsClient.update_deployment",
    "devops.update_project": "oci.devops.DevopsClient.update_project",
    "devops.update_repository": "oci.devops.DevopsClient.update_repository",
    "devops.update_trigger": "oci.devops.DevopsClient.update_trigger",
    "devops.validate_connection": "oci.devops.DevopsClient.validate_connection",
}
