#!/usr/bin/env python3

__version__ = '0.3.1'
__modified__ = ("2020", "12", "30")
__author__ = "Hugo 'iRyukizo' MOREAU"
__maintainer__ = "Hugo 'iRyukizo' MOREAU"
__status__ = "Production"

import argparse
from . import info, precommit

def parse():
    """Parse all options and files.
    :returns: args

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--functions", dest="functions",
            action='store_true',
            help="show number of functions for desired <files>")
    parser.add_argument("-a", dest="all", action='store_true',
            help="same as -f, but will print a resume")
    parser.add_argument("files", metavar="files", type=str, nargs='+',
            help="Files to process")
    parser.add_argument("-l", "--lines", dest="lines", type=int, default=25,
            help="specify maximum number of lines for <files>")
    parser.add_argument("-r", "--remaining", dest="remaining",
            action='store_true',
            help="show number of remaining lines")
    parser.add_argument("-i", "--ignore", dest="ignore", type=str,
            default="//,/*,**,*/",
            help="specify which character should be ignored while processing")
    parser.add_argument("--install", dest="install", nargs=0,
            action=precommit.PreCommit,
            help="install pre-commit files for your repositories")
    parser.add_argument("-v", "--version", action="version",
                    version='%(prog)s {version} {date}'.
                    format(version=__version__, date="-".join(__modified__)))

    args = parser.parse_args()
    return args

def checklines_main():
    """Main function.
    """
    args = parse()
    infos = info.LinesInfos(args.files, int(args.lines),
            (args.remaining, args.functions, args.all),
            args.ignore.split(","))
    return infos.process()
