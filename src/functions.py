__version__ = 0.2
__modified__ = ("2020", "12", "24")
__author__ = "Hugo 'iRyukizo' MOREAU"
__maintainer__ = "Hugo 'iRyukizo' MOREAU"
__status__ = "Production"

import sys
from colorama import Fore, Style

class Functions():

    """Docstring for Function. """

    def handle_dictio(actu, dictio):
        """Add or initiate current filename in dictionary.

        :actu: actual functions
        :dictio: dictionary used to handle number of functions

        """
        if actu[3] not in dictio[1]:
            dictio[1][actu[3]] = [0, 0, 0]
        dictio[1][actu[3]][0] += 1
        dictio[1][actu[3]][1 if actu[4][:6] == "static" else 2] += 1
        dictio[0][0] += 1
        dictio[0][1 if actu[4][:6] == "static" else 2] += 1

    def print_funcs(what, total, dictio):
        """Check number of static and non-static functions.

        :total: Total number of functions
        :dictio: dictionary used to handle number of functions

        :return: bool
        """
        res1, res2, res3 = 0, 0, 0
        for item in dictio:
            res1 = dictio[item][0] > 10 or res1
            res2 = dictio[item][1] > ((10 - dictio[item][2]) if dictio[item][2] <= 5 else 5) or res2
            res3 = dictio[item][2] > 5 or res3
        print("-- functions counter --")
        if (len(dictio) > 1  or what == 2):
            print_func("Total of all   ", total[0], len(dictio) * 10 if not res1 else 0)
            print_func("Total of static", total[1], len(dictio) * 10 if not res2 else 0)
            print_func("Total of normal", total[2], len(dictio) * 5 if not res3 else 0)
        if what == 1:
            for item in dictio:
                print("File:", Style.BRIGHT + Fore.CYAN + item + Style.RESET_ALL)
                print_func("Total ", dictio[item][0], 10)
                print_func("Static", dictio[item][1], ((10 - dictio[item][2]) if dictio[item][2] <= 5 else 5))
                print_func("Normal", dictio[item][2], 5)
        elif (res1 or res2 or res3):
            print(Style.BRIGHT, end="", file=sys.stderr)
            for item in dictio:
                if dictio[item][1] > ((10 - dictio[item][2]) if dictio[item][2] <= 5 else 5):
                    print(item + ": " + Fore.RED + "warning:" + Fore.RESET, \
                            "too much static functions (" + str(dictio[item][1]) + " functions) ", \
                            "[expected " + \
                            str((10 - dictio[item][2]) if dictio[item][2] <= 5 else 5) + \
                            " functions]", file=sys.stderr)
                if dictio[item][2] > 5:
                    print(item + ": " + Fore.RED + "warning:" + Fore.RESET, \
                            "too much exported functions (" + str(dictio[item][2]) + " functions) " \
                            "[expected 5 functions]", file=sys.stderr)
            print(Style.RESET_ALL, end="", file=sys.stderr)
        return res1 or res2 or res3

def print_func(name, nb, max_nb):
    """Print in a good format number of functions.

    :name: current category name of functions
    :nb: actual number of functions
    :max_nb: maximum number of functions

    """
    print("  " + Fore.BLUE + name + Fore.RESET + "  functions:\t", func_prompt(nb, max_nb))
    return nb > max_nb

def func_prompt(nb, max_nb):
    """Returns good color

    """
    return (Fore.RED if nb > max_nb else Fore.GREEN) + Style.BRIGHT + str(nb) + Style.RESET_ALL
