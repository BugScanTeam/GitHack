#!/usr/bin/env python
# coding:utf-8

"""
Copyright (c) 2017 BugScan (http://www.bugscan.net)
See the file 'LICENCE' for copying permission
"""

import sys
import os
import urlparse
from lib.data import logger
from lib.data import paths
from lib.data import target
from lib.data import agents
from lib.settings import USAGE
from lib.settings import BANNER
import subprocess
from lib.settings import DEPENDS
from lib.settings import DEBUG


def checkdepends():
    logger.info("Check Depends")
    process = subprocess.Popen("git --version", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        logger.error(DEPENDS)
        sys.exit(1)
    logger.success("Check depends end")


def check(boolean, message):
    if not boolean:
        logger.error(message)
        sys.exit(1)


def usage():
    logger.p(USAGE, logger.GREEN)


def banner():
    logger.p(BANNER, logger.GREEN)


def setPaths(url):
    logger.info("Set Paths")
    target.TARGET_GIT_URL = url if (url[-1] == "/") else url + "/"
    target.TARGET_DIST = urlparse.urlparse(target.TARGET_GIT_URL).netloc.replace(':', '_')
    logger.info("Target Url: %s" % (target.TARGET_GIT_URL))
    paths.GITHACK_DIST_ROOT_PATH = os.path.join(paths.GITHACK_ROOT_PATH, "dist")
    paths.GITHACK_DATA_PATH = os.path.join(paths.GITHACK_ROOT_PATH, "data")
    paths.USER_AGENTS = os.path.join(paths.GITHACK_DATA_PATH, "user-agents.txt")
    paths.GITHACK_DIST_TARGET_PATH = os.path.join(paths.GITHACK_DIST_ROOT_PATH, target.TARGET_DIST)
    paths.GITHACK_DIST_TARGET_GIT_PATH = os.path.join(paths.GITHACK_DIST_TARGET_PATH, ".git")


def mkdir_p(path):
    if not os.path.exists(path):
        os.makedirs(path)
        # logger.info("Create Directory: %s" % (path))
    # else:
        # logger.info("Directory Exists: %s " % (path))


def initDirs():
    logger.info("Initialize Target")
    mkdir_p(paths.GITHACK_DIST_ROOT_PATH)
    mkdir_p(paths.GITHACK_DIST_TARGET_PATH)


def initAgents():
    data = readFile(paths.USER_AGENTS).splitlines()
    data = [t.strip() for t in data if t.strip() != '']
    agents.extend(data)


def readFile(filename):
    # fileObject = open(filename)
    try:
        with open(filename, "rb") as f:
            retVal = f.read()
    except IOError, ex:
        errMsg = "something went wrong while trying to read "
        errMsg += "the input file ('%s')" % ex
        # raise IOError(errMsg)
    return retVal


def writeFile(filename, data):
    try:
        with open(filename, "wb") as f:
            f.write(data)
    except IOError, ex:
        errMsg = "something went wrong while trying to write "
        errMsg += "to the output file ('%s')" % ex
        # raise IOError(errMsg)
