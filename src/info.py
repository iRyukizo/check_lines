__version__ = 0.2
__modified__ = ("2020", "12", "24")
__author__ = "Hugo 'iRyukizo' MOREAU"
__maintainer__ = "Hugo 'iRyukizo' MOREAU"
__status__ = "Production"

import os, sys
from colorama import Fore, Style
from . import functions

class LinesInfos:

    """All infos for processing."""

    def __init__(self, files, max_lines = 25, options = [False, False, False ],
            ignore = ["//", "/*", "**", "*/"]):
        """Init class linesInfos

        :files: List of files
        :max_lines: Maximum number of lines
        :options: List of boolean
        :ignore: List of characters to ignore

        """
        self._files = files
        self._max_lines = max_lines
        self._options = options
        self._ignore = ignore
        self._func = None
        self._max_len = 0
        self._dictio_func = None

    def process(self):
        """Process all files
        :returns: exit_status

        """
        self.get_func()
        if (self._options[1] or self._options[2]):
            return functions.Functions.print_funcs(1 if self._options[1] else 2,
                    self._dictio_func[0], self._dictio_func[1])
        return self.check()

    def print_info(self):
        """Debug purpose only"""
        print(self._files)
        print(self._max_lines)
        print(self._options)
        print(self._ignore)
        print(self._func)
        print(self._max_len)
        print(self._dictio_func)

    def get_func(self):
        """TODO: Docstring for process.
        :returns: TODO

        """
        command = "ctags -x --c-kinds=f --sort=no " + " ".join(self._files)
        func = os.popen(command).read().split("\n")
        func = func[:len(func) - 1]
        func = [s.strip().split() for s in func]
        maxlen, dictio = 0, [[0,0,0], {}]
        for i in range(len(func)):
            place = 0
            if maxlen < len(func[i][0]):
                maxlen = len(func[i][0])
            functions.Functions.handle_dictio(func[i], dictio)
            for ici in func[i][5:]:
                if not place and len(ici) > len(func[i][0]):
                    j = 0
                    while j < len(ici) and ici[j:len(func[i][0])+j] != func[i][0]:
                        j += 1
                    if j != len(ici):
                        place = len(func[i][4]) + j + 1
                func[i][4] += " " + ici
            func[i] = func[i][:5]
            func[i].append(place)
        self._func = func
        self._max_len = maxlen
        self._dictio_func = dictio

    def check(self):
        """TODO: Docstring for check.

        :returns: TODO

        """
        if self._options[0]:
            print("-- remaining lines --")
        res, file_ = 0, ""
        for actu in self._func:
            if (actu[1] == "function"):
                f = open(actu[3])
                if self._options[0] and file_ != actu[3]:
                    file_ = actu[3]
                    print("File:", Style.BRIGHT + Fore.CYAN + file_ + Style.RESET_ALL)
                lines = f.readlines()
                lines = [s.strip() for s in lines]
                nb_lines = self.micro_check(lines, int(actu[2]))
                if not self._options[0] and nb_lines > self._max_lines:
                    res = 1
                    self.print_err(actu, nb_lines, sys.stderr)
                if self._options[0]:
                    res |= self.remain(actu, nb_lines)
                f.close()
        return res

    def micro_check(self, lines, start_func):
        """TODO: Docstring for micro_check.

        :lines: TODO
        :start_func: TODO
        :returns: TODO

        """
        braces, nb_lines, good = 0, 0, False
        for k in lines[(start_func - 1):]:
            if len(k) == 0 or k in self._ignore:
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

    def print_err(self, actu, nb_lines, f):
        """TODO: Docstring for print_err.

        :actu: TODO
        :nb_lines: TODO
        :f: TODO
        :returns: TODO

        """
        print(Style.BRIGHT, end="", file=f)
        print(actu[3]+":"+str(actu[2])+":"+str(actu[5])+":", end=" ", file=f)
        print(Fore.RED + "warning:" + Fore.RESET, end=" ", file=f)
        print("This function is too long: " + \
                str(nb_lines) + " lines [expected " + \
                str(self._max_lines) +" lines]", file=f)
        print(Style.RESET_ALL, end="", file=f)
        LinesInfos.strange_print(actu[4], actu[5], f)

    def strange_print(proto, offset, f):
        """TODO: Docstring for strange_print.

        :proto: TODO
        :offset: TODO
        :f: TODO
        :returns: TODO

        """
        print(proto, file=f)
        print(Style.BRIGHT + Fore.GREEN, end="", file=f)
        for i in range(offset):
            print(" ", file=f, end="")
        print("^", Style.RESET_ALL, file=f)

    def remain(self, actu, nb_lines):
        """
        Will print remaining lines for each function.
        actual : list of actual function
        """
        remaining_lines, res = self._max_lines - nb_lines, 0
        print_lines = str(remaining_lines)
        if remaining_lines < 0:
            print_lines = Fore.RED + print_lines
            res = 1
        else:
            print_lines = Fore.GREEN + print_lines
        print("  {0} {1:<{5}} {2:>8}:\t{3:>15} {4}".format("Function:", \
                Fore.BLUE + actu[0] + Fore.RESET, \
                "(" + actu[2] + ":" + str(actu[5]) + ")", \
                print_lines, \
                "lines" + Fore.RESET, \
                self._max_len + 10))
        return res
