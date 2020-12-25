__version__ = 0.2
__modified__ = ("2020", "12", "24")
__author__ = "Hugo 'iRyukizo' MOREAU"
__maintainer__ = "Hugo 'iRyukizo' MOREAU"
__status__ = "Production"

import argparse, os, shutil, sys
from os import path as p

class PreCommit(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        try:
            os.popen("curl -fsLo .clang-format https://raw.githubusercontent.com/iRyukizo/check_lines/main/pre-commit/.clang-format")
            os.popen("curl -fsLo .gitignore https://raw.githubusercontent.com/iRyukizo/check_lines/main/pre-commit/.gitignore")
            os.popen("curl -fsLo .pre-commit-config.yaml https://raw.githubusercontent.com/iRyukizo/check_lines/main/pre-commit/.pre-commit-config.yaml")
            inst = os.popen("pre-commit install")
        except:
            return 1
        print(inst.read(), end="")
        parser.exit()

