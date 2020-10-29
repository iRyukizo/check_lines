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
from colorama import Fore, Style

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
    print("\nFull documentation <https://github.com/iRyukizo/check_lines>")
    exit(out)

def main():
    try:
        optlist, args = getopt.getopt(sys.argv[1:], "l:h", ['lines=', "help"])
    except getopt.GetoptErr as err:
        print(err)
        exit(2)
    max_lines = 25
    for opt, arg in optlist:
        if opt == '-l' or opt == '--lines=' or opt == '--lines':
            max_lines = int(arg)
        elif opt == '-h' or opt == '--help':
            usage(0)
        else:
            print(sys.argv[0], ":", opt, ": unhandled option.")
            assert False, "undhandled option"

    if (len(args) < 1):
        usage(1)
    concatenate = ""
    for elmt in args:
        concatenate += " " + elmt
    exit(process(concatenate, max_lines))

def process(concatenate, max_lines):
    """
    Process all files given to check_files.
    concatenate : all given files
    max_lines : maximum number of lines (by default 25)
    return : status
    """
    actual = os.popen("ctags -x --c-kinds=fp --sort=no" + concatenate).read().split("\n")
    actual = actual[:len(actual) - 1]
    actual = [s.strip() for s in actual]
    actual = [s.split() for s in actual]
    for i in range(len(actual)):
        place = 0
        for ici in actual[i][5:]:
            if len(ici) > len(actual[i][0]) and \
                    (ici[:len(actual[i][0])] == actual[i][0] or \
                     ici[1:len(actual[i][0])+1] == actual[i][0] ):
                place = len(actual[i][4]) + 1 + (ici[1:len(actual[i][0])+1] == actual[i][0])
            actual[i][4] += " " + ici
        actual[i] = actual[i][:5]
        actual[i].append(place)

    return check(actual, max_lines)

def check(actual, max_lines):
    """
    Check all functions in given files.
    actual : list of all actual function
    max_lines : maximum number of lines (by default 25)
    return : status
    """
    res = 0
    for actu in actual:
        if (actu[1] == "function"):
            f = open(actu[3])
            start_func = int(actu[2])
            braces, nb_lines = 0, 0
            lines = f.readlines()
            lines = [s.strip() for s in lines]
            good = False
            for k in lines[(start_func - 1):]:
                if len(k) == 0 or \
                        k[0] == ';' or \
                        k[:2] == '//' or \
                        k[:2] == "/*" or k[:2] == "**" or k[:2] == "*/":
                    continue
                if k == "{":
                    braces+=1
                    good = True
                    continue
                if k == "}":
                    braces -= 1
                    continue
                if good and braces <= 0:
                    break
                if good:
                    nb_lines += 1
            if nb_lines > max_lines:
                res = 1
                print(Style.BRIGHT, end="", file=sys.stderr)
                print(actu[3]+":"+str(actu[2])+":"+str(actu[5])+":", \
                        Fore.RED + "warning: " + Fore.RESET + \
                        "This function is too long: " + \
                        str(nb_lines) + " lines [expected " + \
                        str(max_lines) +" lines]", file=sys.stderr)
                print(Style.RESET_ALL, end="", file=sys.stderr)
                strange_print(actu[4], actu[5], sys.stderr)
            f.close()
    return res

def strange_print(actu, offset, where):
    """
    Will print the name of the given function.
    actu : first line of the function prototype
    offset : real start of function
    """
    print(actu, file=where)
    print(Style.BRIGHT + Fore.GREEN, end="", file=where)
    for i in range(offset):
        print(" ", file=where, end="")
    print("^", Style.RESET_ALL, file=where)

if __name__ == "__main__":
    main()
