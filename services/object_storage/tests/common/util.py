# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates. All rights reserved.

import os
import shutil
from pathlib import Path


def create_empty_dir_at_path(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


def create_mixed_dir_at_path(path, n=3):
    create_empty_dir_at_path(path)
    for i in range(n):
        empty_folder = os.path.join(path, "empty_folder")
        content_folder = os.path.join(path, "content_folder")
        file_path = os.path.join(path, "file.txt")
        for j in range(3):
            if j == 0:
                Path(empty_folder).mkdir(parents=True, exist_ok=False)
            if j == 1:
                with open(file_path, 'w') as w:
                    w.write('sample_text')
            if j == 2 and i != n - 1:
                Path(content_folder).mkdir(parents=True, exist_ok=False)
                path = content_folder


def create_file_at_path(path, file_name, content=''):
    file_path = os.path.join(path, file_name)
    with open(file_path, 'w') as w:
        w.write(content)


def get_file_set_at_path(path, parent_path=None):
    if parent_path is None:
        parent_path = path
    local_files_set = set()
    for dir_name, subdir_list, file_list in os.walk(path):
        if not subdir_list and not file_list and path is not dir_name:
            empty_file_rel_path = os.path.relpath(dir_name, parent_path)
            local_files_set.add(f'{empty_file_rel_path}/'.replace(os.sep, '/'))
        for idx, file in enumerate(file_list):
            full_file_path = os.path.join(dir_name, file)
            local_files_set.add(os.path.relpath(full_file_path, parent_path).replace(os.sep, '/'))
    return local_files_set


def remove_dir_at_path(path):
    if os.path.exists(path):
        shutil.rmtree(path)


def unpack_bulk_download_result(result):
    downloaded_files = result['downloaded-objects']
    skipped_files = result['skipped-objects']
    return downloaded_files, skipped_files


def cleanup_files_from_local(file_set):
    for file in file_set:
        if os.path.exists(file):
            os.remove(file)
