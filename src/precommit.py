#!/usr/bin/env python3

__author__ = "Hugo 'iRyukizo' MOREAU"
__maintainer__ = "Hugo 'iRyukizo' MOREAU"
__status__ = "Production"

"""
check_lines
2020
@author: iRyukizo
"""

import os, shutil, sys
from os import path as p

def get_project_path():
    current_path = p.join(p.dirname(sys.argv[0]), sys.argv[0])
    return p.dirname(p.realpath(current_path))

def install():
    pwd, project = os.getcwd(), get_project_path()
    clang, precommit = p.join(project, "pre-commit/.clang-format"), p.join(project, "pre-commit/.pre-commit-config.yaml")
    gitignore = p.join(project, "pre-commit/.gitignore")
    print("Copying " + clang + " into " + pwd)
    shutil.copy(clang, pwd)
    print("Copying " + precommit + " into " + pwd)
    shutil.copy(precommit, pwd)
    print("Copying " + gitignore + " into " + pwd)
    shutil.copy(gitignore, pwd)
    try:
        inst = os.popen("pre-commit install")
    except:
        return 1
    print(inst.read(), end="")
    return 0
