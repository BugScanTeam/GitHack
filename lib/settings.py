#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2017 BugScan (http://www.bugscan.net)
See the file 'LICENCE' for copying permission
"""

from lib import __version__
DEBUG = False

VERSION = __version__

BANNER = """
  ____ _ _   _   _            _
 / ___(_) |_| | | | __ _  ___| | __
| |  _| | __| |_| |/ _` |/ __| |/ /
| |_| | | |_|  _  | (_| | (__|   <
 \____|_|\__|_| |_|\__,_|\___|_|\_\\{%s}
 A '.git' folder disclosure exploit.
""" % (VERSION)

USAGE = """Usage:
  python GitHack.py http://www.target.com/.git/
"""

DEPENDS = """git was not found in $PATH"""
