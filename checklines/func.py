class Function:

    """Docstring for Function. """

    def __init__(self, desc):
        """TODO: to be defined. """

        self._name = desc[0]
        self._type = desc[1]
        self._line = desc[2]
        self._location = desc[3]
        self._proto = desc[4]
        self._name_offset = desc[5]
        self._nb_lines = -1

    def __str__(self):
        return self._name + " "\
                + self._type + " "\
                + self._location + " "\
                + self._proto + " "\
                + str(self._name_offset)
