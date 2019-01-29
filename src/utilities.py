#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Utilities for analyzing Enron email data"""

import sys
import logging


__author__ = "Pujaa Rajan"
__email__ = "pujaa.rajan@gmail.com"


def logger():
    """
    Create and format logger that logs to file and console
    @return None:
    """
    logger = logging.getLogger('Enron_email_analysis')
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler('Enron_email_analysis.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with the same log level
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.info('Finished creating logger')


def takeInput():
    cond = False
    # take input
    while (cond == False):
        sen = input('Enter the string\n')
        # ? We may need to remove puncuation from the input
        before_and_after_blank = sen.split("_")
        before_blank_tokens = before_and_after_blank[0].split()[-3:]
        after_blank_tokens = before_and_after_blank[1].split()[:3]
        print("EXTRACTED TEXT FROM INPUT")
        if len(before_blank_tokens) < 3 or len(after_blank_tokens) < 3:
            print("Please enter at least 3 words before and after the blank!")
        return before_blank_tokens, after_blank_tokens
