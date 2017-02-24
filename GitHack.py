#!/usr/bin/env python
# coding:utf-8
"""
Copyright (c) 2017 BugScan (http://www.bugscan.net)
See the file 'LICENCE' for copying permission
"""

import os
import sys
from lib.data import paths
from lib.common import banner
from lib.common import usage
from lib.common import setPaths
from lib.common import initAgents
from lib.common import initDirs
from lib.common import checkdepends
from lib.controler import start


def main():
    init()


def init():
    try:
        paths.GITHACK_ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
        banner()
        if len(sys.argv) < 2:
            usage()
            sys.exit(1)
        checkdepends()
        setPaths(sys.argv[-1])
        initAgents()
        initDirs()
        start()
    except:
        raise

if __name__ == '__main__':
    main()
