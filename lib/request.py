#!/usr/bin/env python
# coding:utf-8

"""
Copyright (c) 2017 BugScan (http://www.bugscan.net)
See the file 'LICENCE' for copying permission
"""

import os
import urllib2
import random
from lib.common import writeFile
from lib.data import paths
from lib.data import target
from lib.data import agents
from lib.data import logger
from lib.settings import DEBUG


def randomAgent():
    return random.choice(agents)


def request_data(url):
    for i in range(3):
        data = None
        try:
            request = urllib2.Request(url, None, {'User-Agent': randomAgent()})
            data = urllib2.urlopen(request).read()
            if data:
                return data
        except Exception, e:
            if DEBUG:
                logger.warning("Request Exception: %s" % str(e))
    return None


def wget(filepath):
    url = "%s%s" % (target.TARGET_GIT_URL, filepath)
    filename = os.path.join(paths.GITHACK_DIST_TARGET_GIT_PATH, filepath)
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    data = request_data(url)
    if data:
        writeFile(filename, data)
        if DEBUG:
            logger.success("Get %s => %s" % (url, filepath))


def isdirlist():
    keywords = [
        "To Parent Directory",
        "Index of /",
        "Directory Listing For /",
        "[转到父目录]",
        "objects/",
    ]
    data = request_data(target.TARGET_GIT_URL)
    if data:
        for key in keywords:
            if key in data:
                logger.info("%s is support Directory Listing" % target.TARGET_GIT_URL)
                return True
    logger.info("%s is not support Directory Listing" % target.TARGET_GIT_URL)
    return False
