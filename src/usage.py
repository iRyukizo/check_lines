#!/usr/bin/env python3

__author__ = "Hugo 'iRyukizo' MOREAU"
__maintainer__ = "Hugo 'iRyukizo' MOREAU"
__status__ = "Production"

"""
check_lines
2020
@author: iRyukizo
"""

import sys

def usage(out):
    print("Usage: ", end="")
    if (sys.argv[0][len(sys.argv[0]) - 2:] != "py"):
        print("check_lines", end="")
    else:
        print(sys.argv[0], end="")
    print(" [OPTION]... [FILE]...")
    print("Options:")
    print("\t-l, --lines\tSpecify number of maximum lines for each functions.")
    print("\t-h, --help\tDisplay this message.")
    print("\t-r, --remaing\tShow number of remaining lines.")
    print("\nFull documentation <https://github.com/iRyukizo/check_lines>")
    exit(out)
