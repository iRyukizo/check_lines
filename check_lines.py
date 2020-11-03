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
        optlist, args = getopt.getopt( \
                sys.argv[1:], \
                "fi:l:rh", \
                ["function", 'lines=', "remaining", 'ignore=', "help"])
    except getopt.GetoptError as err:
        usage.print_name(sys.stderr, ": " + str(err))
        usage.usage(1)
    max_lines, options, ignore = 25, [False, False] , [";", "//", "/*", "**", "*/"]
    for opt, arg in optlist:
        if opt == '-l' or opt == '--lines=' or opt == '--lines':
            max_lines = int(arg)
        elif opt == '-r' or opt == '--remaining':
            options[0] = True
        elif opt == '-i' or opt == '--ignore' or opt == '--ignore=':
            ignore = arg.split(',')
        elif opt == '-f' or opt == '--function':
            options[1] = True
        elif opt == '-h' or opt == '--help':
            usage.usage(0)
        else:
            usage.print_name(sys.stderr, ":" + opt + ": unhandled option.")
            usage.usage(1)

    sep = [ (x, []) for x in range(len(max(ignore, key=len)) + 1)]
    for x in ignore:
        sep[len(x)][1].append(x)
    if (len(args) < 1):
        usage.print_name(sys.stderr, ": no files specified")
        usage.usage(1)
    concatenate = ""
    for elmt in args:
        concatenate += " " + elmt
    exit(process.process(concatenate, max_lines, options, sep))

if __name__ == "__main__":
    main()
