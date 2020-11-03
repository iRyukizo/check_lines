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
    """
    Print on stdout or stderr help page.
    out : exit value
    """
    f = correct_std(out)
    print("Usage: ", end="", file=f)
    print_name(f, " [OPTION]... [FILE]...")
    print("Options:", file=f)
    print("\t-f, --functions\tShow number of functions for each file.", file=f)
    print("\t\t\t(This option will override others)", file=f)
    print("\t-a,         \tSame as -f, except will only print once.", file=f)
    print("\t-i, --ignore\tSpecify which case should be ignored when processing.", file=f)
    print("\t-l, --lines\tSpecify number of maximum lines for each functions.", file=f)
    print("\t-h, --help\tDisplay this message.", file=f)
    print("\t-r, --remaining\tShow number of remaining lines.", file=f)
    print("\nFull documentation <https://github.com/iRyukizo/check_lines>", file=f)
    exit(out)

def print_name(f, message):
    """
    Print on stdout or stderr an err message.
    f : file descriptor
    message : message to be displayed
    """
    if (sys.argv[0][len(sys.argv[0]) - 2:] != "py"):
        print("check_lines", end="", file=f)
    else:
        print(sys.argv[0], end="", file=f)
    print(message, file=f)

def correct_std(out):
    """
    out : value
    return : file descriptor of out
    """
    if out:
        return sys.stderr
    return sys.stdout
