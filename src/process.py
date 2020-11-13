#!/usr/bin/env python3

__author__ = "Hugo 'iRyukizo' MOREAU"
__maintainer__ = "Hugo 'iRyukizo' MOREAU"
__status__ = "Production"

"""
check_lines
2020
@author: iRyukizo
"""

import os, sys
from colorama import Fore, Style
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
from src import functions

def process(concatenate, max_lines, options, ignore):
    """
    Process all files given to check_files.
    concatenate : all given files
    max_lines : maximum number of lines (by default 25)
    ignore : ignore cases
    return : status
    """
    actual = os.popen("ctags -x --c-kinds=f --sort=no" + concatenate).read().split("\n")
    actual = actual[:len(actual) - 1]
    actual = [s.strip() for s in actual]
    actual = [s.split() for s in actual]
    maxlen, dictio = 0, [[0,0,0], {}]
    for i in range(len(actual)):
        place = 0
        if maxlen < len(actual[i][0]):
            maxlen = len(actual[i][0])
        functions.handle_dictio(actual[i], dictio)
        for ici in actual[i][5:]:
            if not place and len(ici) > len(actual[i][0]):
                j = 0
                while j < len(ici) and ici[j:len(actual[i][0])+j] != actual[i][0]:
                    j += 1
                if j != len(ici):
                    place = len(actual[i][4]) + j + 1
            actual[i][4] += " " + ici
        actual[i] = actual[i][:5]
        actual[i].append(place)

    if options[1]:
        return functions.print_funcs(options[1], dictio[0], dictio[1])
    return check(actual, max_lines, options, maxlen, ignore)

def check(actual, max_lines, options, maxlen, ignore):
    """
    Check all functions in given files.
    actual : list of all actual function
    max_lines : maximum number of lines (by default 25)
    options : list of options
    ignore : ignore cases
    return : status
    """
    if options[0]:
        print("-- remaining lines --")
    res, file_ = 0, ""
    for actu in actual:
        if (actu[1] == "function"):
            f = open(actu[3])
            if options[0] and file_ != actu[3]:
                file_ = actu[3]
                print("File:", Style.BRIGHT + Fore.CYAN + file_ + Style.RESET_ALL)
            lines = f.readlines()
            lines = [s.strip() for s in lines]
            nb_lines = micro_check(lines, int(actu[2]), ignore)
            if not options[0] and nb_lines > max_lines:
                res = 1
                print_err(actu, nb_lines, max_lines, sys.stderr)
            if options[0]:
                remain(actu, max_lines, nb_lines, maxlen)
            f.close()
    return res

def micro_check(lines, start_func, ignore):
    """
    Check current function
    lines : list of lines in file
    start_func : beginning of function
    ignore : ignore cases
    return : number of lines
    """
    braces, nb_lines, good = 0, 0, False
    for k in lines[(start_func - 1):]:
        if len(k) == 0 or \
                ignore_case(k, ignore):
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
    return nb_lines

def ignore_case(test, ignore):
    """
    Ignoring certain type of lines
    test : string
    ignore : list of tuple (len, list of string of size len)
    return : bool
    """
    for x in ignore:
        if (len(test) < x[0]):
            return False
        if (test[:x[0]] in x[1]):
            return True
    return False

def print_err(actu, nb_lines, max_lines, f):
    """
    Print error in a clang-format style
    actu : actual function
    nb_lines : number of lines in function
    max_lines : Maximum number of lines
    f : file descriptor
    """
    print(Style.BRIGHT, end="", file=f)
    print(actu[3]+":"+str(actu[2])+":"+str(actu[5])+":", end=" ", file=f)
    print(Fore.RED + "warning:" + Fore.RESET, end=" ", file=f)
    print("This function is too long: " + \
            str(nb_lines) + " lines [expected " + \
            str(max_lines) +" lines]", file=f)
    print(Style.RESET_ALL, end="", file=f)
    strange_print(actu[4], actu[5], f)


def strange_print(proto, offset, f):
    """
    Will print the name of the given function.
    proto : first line of the function prototype
    offset : real start of function
    """
    print(proto, file=f)
    print(Style.BRIGHT + Fore.GREEN, end="", file=f)
    for i in range(offset):
        print(" ", file=f, end="")
    print("^", Style.RESET_ALL, file=f)

def remain(actu, max_lines, nb_lines, maxlen):
    """
    Will print remaining lines for each function.
    actual : list of actual function
    max_lines : number of max_lines
    maxlen : used in order to format ouput
    """
    remaining_lines = max_lines - nb_lines
    print_lines = str(remaining_lines)
    if remaining_lines < 0:
        print_lines = Fore.RED + print_lines
    else:
        print_lines = Fore.GREEN + print_lines
    print("  {0} {1:<{5}} {2:>8}:\t{3:>15} {4}".format("Function:", \
            Fore.BLUE + actu[0] + Fore.RESET, \
            "(" + actu[2] + ":" + str(actu[5]) + ")", \
            print_lines, \
            "lines" + Fore.RESET, \
            maxlen + 10))
