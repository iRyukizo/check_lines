from . import func

class File:

    """Docstring for File. """

    def __init__(self, location, fun):
        """TODO: to be defined.

        :func: TODO

        """

        self._location = location
        self._functions = []
        for elmt in fun:
            self._functions.append(func.Function(elmt))

    def __str__(self):
        res = ""
        for elmt in self._functions[:-1]:
            res += elmt.__str__() + "\n"
        res += self._functions[-1].__str__()
        return self._location + "\n" + res
