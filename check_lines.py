#!/usr/bin/env python3

import re, os, sys
from colorama import Fore

def usage():
    print("Usage:")
    print(sys.argv[0] + " [files]")

def main():
    if (len(sys.argv) < 2):
        usage()
        exit(1)
    concatenate = ""
    for i in range(1, len(sys.argv)):
        concatenate += " " + sys.argv[i]
    actual = os.popen("ctags -x --c-kinds=fp" + concatenate).read().split("\n")
    actual = actual[:len(actual) - 1]
    actual = [s.strip() for s in actual]
    actual = [s.split() for s in actual]
    for i in range(len(actual)):
        place = 0
        for ici in actual[i][5:]:
            if len(ici) > len(actual[i][0]) and ici[:len(actual[i][0])] == actual[i][0]:
                place = len(actual[i][4]) + 1
            actual[i][4] += " " + ici
        actual[i] = actual[i][:5]
        actual[i].append(place)

    exit(check(actual))

def check(actual):
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
            if nb_lines > 25:
                res = 1
                print(actu[3]+":"+str(actu[2])+":"+str(actu[5])+":", \
                        Fore.RED + "warning: This function is too long: " + \
                        str(nb_lines) + " lines [expected 25 lines]." + \
                        Fore.RESET)
                strange_print(actu[4], actu[5])
            f.close()
    return res

def strange_print(actu, offset):
    print(actu)
    for i in range(offset):
        print(" ", end="")
    print("^")

if __name__ == "__main__":
    main()
