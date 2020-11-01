#!/usr/bin/env python3

__author__ = "Hugo 'iRyukizo' MOREAU"
__maintainer__ = "Hugo 'iRyukizo' MOREAU"
__status__ = "Production"

"""
check_lines
2020
@author: iRyukizo
"""

import getopt, os, sys
# A little bit tricky, but does the work for now
# Since we use a symlink for using checklines,
# We need to import from the good folder.
sys.path.append(os.path.join( \
        os.path.dirname( \
        os.path.realpath( \
        os.path.join( \
        os.path.dirname( \
        sys.argv[0] \
        ), sys.argv[0] \
        ) \
        ) \
        ), \
        'src' \
        ) \
        )
from src import usage, process

def main():
    try:
        optlist, args = getopt.getopt(sys.argv[1:], "l:rh", ['lines=', "remaining", "help"])
    except getopt.GetoptError as err:
        if (sys.argv[0][len(sys.argv[0]) - 2:] != "py"):
            print("check_lines", end="", file=sys.stderr)
        else:
            print(sys.argv[0], end="", file=sys.stderr)
        print(":", err, file=sys.stderr)
        usage.usage(2)
    max_lines, remaining = 25, False
    for opt, arg in optlist:
        if opt == '-l' or opt == '--lines=' or opt == '--lines':
            max_lines = int(arg)
        elif opt == '-r' or opt == '--remaining':
            remaining = True
        elif opt == '-h' or opt == '--help':
            usage.usage(0)
        else:
            print(sys.argv[0], ":", opt, ": unhandled option.")
            usage.usage(1)

    if (len(args) < 1):
        if (sys.argv[0][len(sys.argv[0]) - 2:] != "py"):
            print("check_lines", end="", file=sys.stderr)
        else:
            print(sys.argv[0], end="", file=sys.stderr)
        print(": no files specified", file=sys.stderr)
        usage.usage(1)
    concatenate = ""
    for elmt in args:
        concatenate += " " + elmt
    exit(process.process(concatenate, max_lines, remaining))

if __name__ == "__main__":
    main()
