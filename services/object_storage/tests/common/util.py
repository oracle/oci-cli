# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates. All rights reserved.

import os
import shutil


def remove_dir_at_path(path):
    if os.path.exists(path):
        shutil.rmtree(path)
