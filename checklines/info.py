__version__ = '0.3.2'
__modified__ = ("2021", "02", "01")
__author__ = "Hugo 'iRyukizo' MOREAU"
__maintainer__ = "Hugo 'iRyukizo' MOREAU"
__status__ = "Production"

import os, sys
from . import functions, files, func

def operator(s):
    if s[0] == "operator" and s[1] != "function":
        s[0] += s[1]
        for i in range(1, len(s) - 1):
            s[i] = s[i + 1]
        s.pop()
    return s

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
        self._files_cont = []
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
        self.check()
        if (self._options[0]):
            return self.remain()
        return self.default()

    def print(self):
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
        command = "ctags -x --c-kinds=f --sort=no -R --languages=c,c++ " + " ".join(self._files)
        func = os.popen(command).read().split("\n")
        func = func[:len(func) - 1]
        func = [s.strip().split() for s in func]
        func = [operator(s) for s in func]
        visited, newfunc = [], []
        maxlen, dictio = 0, [[0,0,0], {}]
        for i in range(len(func)):
            if func[i][0] == '_':
                continue
            if func[i] in visited:
                continue
            else:
                visited.append(func[i].copy())
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
            newfunc.append(func[i])
        self._func = newfunc
        if self._func == None:
            return 0
        location, beg, end = self._func[0][3], 0, len(self._func)
        for i in range(1, end):
            if (location != self._func[i][3]):
                self._files_cont.append(files.File(location, self._func[beg:i]))
                location, beg = self._func[i][3], i
        self._files_cont.append(files.File(location, self._func[beg:end]))
        self._max_len = maxlen
        self._dictio_func = dictio

    def check(self):
        for elmt in self._files_cont:
            elmt.check(self._ignore)

    def default(self):
        res = 0
        for elmt in self._files_cont:
            res |= elmt.default(self._max_lines)
        return res

    def remain(self):
        res = 0
        for elmt in self._files_cont:
            res |= elmt.remain(self._max_lines, self._max_len)
        return res
