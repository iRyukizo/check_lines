import os, sys
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
        if (self._options[1] or self._options[2]):
            return functions.Functions.print_funcs(1 if self._options[1] else 2,
                    self._dictio_func[0], self._dictio_func[1])
        return 0

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
