# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import pytest
import unittest
from tests import test_config_container
from tests import util

# Current setup of the test:
#     Two repos are created manually in CliTestCompartment under tenancy ociregistrydev
#     and will be kept unaltered before and after the tests
#         1. cli_test_repo:  <- this repo is created for testing.
#         2. cli_test_image_repo <- this will be pre-loaded with images for testing
#
# Limitation:
#     1.  Current testing with deleting images and remove image version(i.e. test_remove_version_container_image)
#         is done by making a dummy requests (i.e. requests with faulty arguments). Making such requests will not
#         actually delete images / tags and thus no need to re-push / re-tag images, which has to done by Docker CLI.
#         We don't have a secure location within this code repo to store credentials(username, password).

CASSETTE_LIBRARY_DIR = "services/artifacts/tests/cassettes"
TEST_REPO = "cli_test_repo"
IMAGE_REPO = "cli_test_image_repo"  # Repo to test images operations
IMAGE_TAG = "test_tag"
REPO_CREATED = "created_repo"
REPO_DELETED = "deleted_repo"
IMAGE_DISPLAY_NAME = "%s:%s" % (IMAGE_REPO, IMAGE_TAG)

COMPARTMENT_ID = "ocid1.compartment.oc1..aaaaaaaabqvhxwm6mzqiew6dmuwktihfpbqa5wt6zalpuxwkrmvvmq4j3leq"
NAMESPACE = "lrcs5a2kpcwp"
USER_ID = "ocid1.user.oc1..aaaaaaaakokzoson5qdcoagzpwhm76ff6vcszzwujpsinbe4py5hisomkfwq"
TENANT_ID = "ocid1.tenancy.oc1..aaaaaaaafjofdpueovh7fnbal77uvo2ilka5kyw26tmbw2egqzi5swmqiqgq"


@pytest.fixture(autouse=True, scope="module")
def vcr_fixture(request):
    with test_config_container.create_vcr(
            cassette_library_dir=CASSETTE_LIBRARY_DIR
    ).use_cassette("artifacts_extended.yml"):
        yield


def delete_leftover_repository():
    # list all the repos
    command = ["artifacts", "container", "repository", "list"]
    params = [
        "--compartment-id",
        COMPARTMENT_ID,
    ]
    command.extend(params)
    result = invoke_command(command)

    # Delete extra repo created during testing and keep $REPO and $IMAGE_REPO
    repo_ids = [
        repo["id"]
        for repo in result["items"]
        if (repo["display-name"] != IMAGE_REPO and repo["display-name"] != TEST_REPO)
    ]
    for id in repo_ids:
        command = ["artifacts", "container", "repository", "delete"]
        params = ["--repository-id", id, "--force"]
        command.extend(params)
        invoke_command(command, response_expected=False)


def reset_update_container_configuration():
    command = ["artifacts", "container", "configuration", "update"]
    params = [
        "--compartment-id",
        COMPARTMENT_ID,
        "--is-repository-created-on-first-push",
        "true",
    ]
    command.extend(params)
    invoke_command(command)


def find_test_repo_id():
    # get list of repo in order to get repo id
    command = ["artifacts", "container", "repository", "list"]
    params = [
        "--compartment-id",
        COMPARTMENT_ID,
    ]
    command.extend(params)
    result = invoke_command(command)
    expected_repos = [
        repo for repo in result.get("items") if repo["display-name"] == TEST_REPO
    ]
    repo_id = expected_repos[0]["id"]
    return repo_id


def reset_container_repository():
    # get list of repo in order to get repo id
    repo_id = find_test_repo_id()
    # update repo
    command = ["artifacts", "container", "repository", "update"]
    params = [
        "--repository-id",
        repo_id,
        "--force",
        "--is-public",
        "false",
    ]
    command.extend(params)
    invoke_command(command)


def get_image_id():
    command = ["artifacts", "container", "image", "list"]
    params = [
        "--compartment-id",
        COMPARTMENT_ID,
        "--display-name",
        IMAGE_DISPLAY_NAME,
    ]

    command.extend(params)
    result = invoke_command(command)
    return result["items"][0]["id"]


def invoke_command(command, response_expected=True, **kwargs):
    response = util.invoke_command(command, **kwargs)
    assert response.exit_code == 0
    data = (
        util.get_json_from_mixed_string(response.output)["data"]
        if response_expected
        else None
    )
    return data


class TestArtifactsExtended(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        delete_leftover_repository()
        reset_update_container_configuration()

    def test_get_container_configuration(self):
        command = ["artifacts", "container", "configuration", "get"]
        params = [
            "--compartment-id",
            COMPARTMENT_ID,
        ]

        command.extend(params)
        result = invoke_command(command)

        assert "is-repository-created-on-first-push" in result
        assert "namespace" in result
        assert result.get("namespace") == NAMESPACE

    def test_update_container_configuration(self):
        command = ["artifacts", "container", "configuration", "update"]
        params = [
            "--compartment-id",
            COMPARTMENT_ID,
            "--is-repository-created-on-first-push",
            "false",
        ]

        command.extend(params)
        result = invoke_command(command)

        assert "is-repository-created-on-first-push" in result
        assert "namespace" in result
        assert result.get("namespace") == NAMESPACE
        assert result.get("is-repository-created-on-first-push") is False

    def test_create_container_repository(self):
        command = ["artifacts", "container", "repository", "create"]
        params = [
            "--compartment-id",
            COMPARTMENT_ID,
            "--display-name",
            REPO_CREATED,
        ]
        command.extend(params)
        result = invoke_command(command)
        assert "compartment-id" in result
        assert "display-name" in result
        assert "created-by" in result
        assert result.get("compartment-id") == COMPARTMENT_ID
        assert result.get("created-by") == USER_ID
        assert result.get("display-name") == REPO_CREATED

    def test_list_container_repository(self):
        command = ["artifacts", "container", "repository", "list"]
        params = [
            "--compartment-id",
            COMPARTMENT_ID,
        ]
        command.extend(params)
        result = invoke_command(command)

        assert "items" in result
        assert len(result.get("items")) > 0

        expected_repos = [
            repo for repo in result.get("items") if repo["display-name"] == TEST_REPO
        ]
        assert len(expected_repos) == 1

    def test_get_container_repository(self):
        # get list of repo in order to get repo id
        repo_id = find_test_repo_id()

        # get the repo by repo id
        command = ["artifacts", "container", "repository", "get"]
        params = ["--repository-id", repo_id]
        command.extend(params)
        result = invoke_command(command)
        assert "id" in result
        assert "display-name" in result
        assert "compartment-id" in result
        assert result["id"] == repo_id
        assert result["display-name"] == TEST_REPO
        assert result["compartment-id"] == COMPARTMENT_ID

    def test_update_container_repository(self):
        # get list of repo in order to get repo id
        repo_id = find_test_repo_id()

        # update repo
        command = ["artifacts", "container", "repository", "update"]
        params = [
            "--repository-id",
            repo_id,
            "--force",
            "--is-public",
            "true",
        ]

        command.extend(params)
        result = invoke_command(command)
        assert "id" in result
        assert "display-name" in result
        assert "compartment-id" in result
        assert "is-public" in result
        assert result["id"] == repo_id
        assert result["display-name"] == TEST_REPO
        assert result["compartment-id"] == COMPARTMENT_ID
        assert result["is-public"] is True

    def test_change_compartment_container_repository(self):
        # create a repo in root compartment
        command = ["artifacts", "container", "repository", "create"]
        params = [
            "--compartment-id",
            TENANT_ID,
            "--display-name",
            REPO_CREATED,
        ]
        command.extend(params)
        result = invoke_command(command)
        repo_id = result["id"]

        # move the repository to CLITESTCOMPARTMENT
        command = ["artifacts", "container", "repository", "change-compartment"]
        params = [
            "--compartment-id",
            COMPARTMENT_ID,
            "--repository-id",
            repo_id,
        ]
        command.extend(params)
        invoke_command(command, response_expected=False)

        # find it again and make sure it is in new compartment
        command = ["artifacts", "container", "repository", "get"]
        params = ["--repository-id", repo_id]
        command.extend(params)
        result = invoke_command(command)
        assert "compartment-id" in result
        assert result["compartment-id"] == COMPARTMENT_ID

    def test_delete_container_repository(self):
        # create a repo to test deletion
        command = ["artifacts", "container", "repository", "create"]
        params = [
            "--compartment-id",
            COMPARTMENT_ID,
            "--display-name",
            REPO_DELETED,
        ]
        command.extend(params)
        result = invoke_command(command)
        repo_id = result["id"]

        # delete the repo
        command = ["artifacts", "container", "repository", "delete"]
        params = [
            "--repository-id",
            repo_id,
            "--force",
        ]
        command.extend(params)
        invoke_command(command, response_expected=False)

        # find the repo again, this time it could not be found
        command = ["artifacts", "container", "repository", "get"]
        params = ["--repository-id", repo_id]
        command.extend(params)
        response = util.invoke_command(command)
        assert "REPO_ID_UNKNOWN" in response.output
        assert response.exit_code > 0

    def test_list_container_image(self):
        command = ["artifacts", "container", "image", "list"]
        params = [
            "--compartment-id",
            COMPARTMENT_ID,
        ]
        command.extend(params)
        result = invoke_command(command)
        assert "items" in result
        assert len(result["items"]) > 0
        images = [
            image
            for image in result["items"]
            if image["display-name"] == IMAGE_DISPLAY_NAME
        ]
        assert len(images) == 1

    def test_get_container_image(self):
        image_id = get_image_id()
        command = ["artifacts", "container", "image", "get"]
        params = [
            "--image-id",
            image_id,
        ]
        command.extend(params)
        result = invoke_command(command)
        assert "compartment-id" in result
        assert "display-name" in result
        assert "repository-name" in result
        assert "version" in result
        assert result.get("compartment-id") == COMPARTMENT_ID
        assert result.get("display-name") == IMAGE_DISPLAY_NAME
        assert result.get("version") == IMAGE_TAG
        assert result.get("repository-name") == IMAGE_REPO

    def test_remove_version_container_image(self):
        result = util.invoke_command(
            [
                "artifacts",
                "container",
                "image",
                "remove-version",
                "--image-version",
                "dummy",
                "--image-id",
                "dummy",
            ]
        )
        assert "ServiceError" in result.output

    def test_restore_container_image(self):
        result = util.invoke_command(
            [
                "artifacts",
                "container",
                "image",
                "restore",
                "--image-id",
                "dummy",
            ]
        )
        assert "ServiceError" in result.output

    def delete_container_image(self):
        result = util.invoke_command(
            [
                "artifacts",
                "container",
                "image",
                "delete",
                "--image-id",
                "dummy",
                "--force",
            ]
        )
        assert "ServiceError" in result.output


if __name__ == "__main__":
    unittest.main()
