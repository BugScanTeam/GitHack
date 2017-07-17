#!/usr/bin/env python
# coding:utf-8

"""
Copyright (c) 2017 BugScan (http://www.bugscan.net)
See the file 'LICENCE' for copying permission
"""

import os
from lib.data import paths
from lib.data import logger
from lib.git import clone
from lib.git import valid_git_repo
from lib.request import isdirlist
from lib.git import clone_from_list
from lib.git import clone_from_cache
from lib.git import init
from lib.git import refresh_files

def start():
    if method_a() or method_b() or method_c():
        job_success()
    else:
        job_fail()

def method_a():
    logger.info("Try to Clone straightly")
    git_dir = os.path.join(paths.GITHACK_DIST_TARGET_PATH, ".git")
    if os.path.exists(git_dir):
        logger.warning("[Skip][First Try] %s already exists." % (git_dir))
        return valid_git_repo()
    return clone()

def method_b():
    logger.info("Try to Clone with Directory Listing")
    if isdirlist():
        try:
            git_dir = os.path.join(paths.GITHACK_DIST_TARGET_PATH, ".git")
            if not os.path.exists(git_dir):
                init()
            clone_from_list("/")
            refresh_files()
            if not valid_git_repo():
                logger.warning("Clone With Directory Listing end. But missed some files.")
            return True
        except:
            return False
    logger.warning("[Skip][First Try] Target is not support Directory Listing")
    return False

def method_c():
    logger.info("Try to clone with Cache")
    git_dir = os.path.join(paths.GITHACK_DIST_TARGET_PATH, ".git")
    if not os.path.exists(git_dir):
        init()
    clone_from_cache()
    if not valid_git_repo():
        logger.warning("Clone With Cache end. But missed some files.")
    return True

def job_success():
    logger.p("", logger.GREEN)
    logger.success("Clone Success. Dist File : %s" % (paths.GITHACK_DIST_TARGET_PATH))

def job_fail():
    logger.p("", logger.GREEN)
    logger.error("Clone Fail.")
