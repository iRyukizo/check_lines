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

    def print_info(self):
        """Debug purpose only"""
        print(self._files)
        print(self._max_lines)
        print(self._options)
        print(self._ignore)
