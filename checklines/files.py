from colorama import Fore, Style
from . import func

class File:
    def __init__(self, location, fun):
        self._location = location
        self._size = len(fun)
        self._res = [-1] * self._size
        self._functions = []
        for elmt in fun:
            self._functions.append(func.Function(elmt))

    def __str__(self):
        res = ""
        for elmt in self._functions[:-1]:
            res += elmt.__str__() + "\n"
        res += self._functions[-1].__str__()
        return self._location + "\n" + res

    def check(self, ignore):
        f = open(self._location)
        lines = f.readlines()
        lines = [s.strip() for s in lines]
        f.close()
        for i, elmt in enumerate(self._functions):
            if elmt._type == "function":
                self._res[i] = elmt.check(lines, ignore)

    def default(self, max_lines):
        res = 0
        for elmt in self._functions:
            res |= elmt.default(max_lines)
        return res

    def remain(self, max_lines, max_len):
        res = 0
        print("File:", Style.BRIGHT + Fore.CYAN + self._location + Style.RESET_ALL)
        for elmt in self._functions:
            res |= elmt.remain(max_lines, max_len)
        return res
