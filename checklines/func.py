import sys
from colorama import Fore, Style

class Function:
    def __init__(self, desc):
        self._name = desc[0]
        self._type = desc[1]
        self._line = int(desc[2])
        self._location = desc[3]
        self._proto = desc[4]
        self._name_offset = desc[5]
        self._nb_lines = -1

    def __str__(self):
        return self._name + " "\
                + self._type + " "\
                + str(self._line) + " "\
                + self._location + " "\
                + self._proto + " "\
                + str(self._name_offset)

    def check(self, lines, ignore):
        self._nb_lines, braces, good = 0, 0, False
        for k in lines[(self._line - 1):]:
            if len(k) == 0 or Function.ignore_case(k, ignore):
                continue
            if k == "{":
                braces += 1
                good = True
                continue
            if k == "}":
                braces -= 1
                continue
            if good and braces <= 0:
                break
            if good:
                self._nb_lines += 1
        return self._nb_lines


    def ignore_case(test, ignore):
        for x in ignore:
            if (test[:len(x)] == x):
                return True
        return False

    def default(self, max_lines):
        if self._nb_lines > max_lines:
            self.error(max_lines)
            return 1
        return 0

    def error(self, max_lines):
        f = sys.stderr
        print(Style.BRIGHT, end="", file=f)
        print(self._location+":"+str(self._line)+":"+str(self._name_offset)\
                +":", end=" ", file=f)
        print(Fore.RED + "warning:" + Fore.RESET, end=" ", file=f)
        print("This function is too long: " + \
                str(self._nb_lines) + " lines [expected " + \
                str(max_lines) +" lines]", file=f)
        print(Style.RESET_ALL, end="", file=f)
        self.offset_print(f)

    def offset_print(self, f):
        print(self._proto, file=f)
        print(Style.BRIGHT + Fore.GREEN, end="", file=f)
        for i in range(self._name_offset):
            print(" ", file=f, end="")
        print("^", Style.RESET_ALL, file=f)

    def remain(self, max_lines, max_len):
        remaining_lines, res = max_lines - self._nb_lines, 0
        print_lines = str(remaining_lines)
        if remaining_lines < 0:
            print_lines = Fore.RED + print_lines
            res = 1
        else:
            print_lines = Fore.GREEN + print_lines
        print("  {0} {1:<{5}} {2:>8}:\t{3:>15} {4}".format("Function:", \
                Fore.BLUE + self._name + Fore.RESET, \
                "(" + str(self._line) + ":" + str(self._name_offset) + ")", \
                print_lines, \
                "lines" + Fore.RESET, \
                max_len + 10))
        return res
