#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Description"""

# Import Statements
# Import built-ins first, then 3rd party, then local source, then changes to path and own modules

# Built-in/Generic Imports

import os
import sys
import argparse
import importlib
import logging
from lxml import html
import requests
import random
import datetime
import re
import locale

# Libs

# Own modules

# Global Variables

LOG_FILE = '.log'
LOG_FILE_SMTP_HOST = 'localhost'
LOG_FILE_TO = ''
LOG_FILE_FROM = ''
LOG_FILE_SUBJECT = ''

logging.basicConfig(filename='.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# Status is Prototype, Development, Test, Production

# Script

class SomeClass:
    __var1 = ''
    __var2 = ''

    def __init__(self, a, b):
        self.__var1 = a
        self.__var2 = b

def check_requirements():
    if sys.platform == 'linux' or sys.platform == 'linux2':
        pass
    else:
        return False
    return True

def make_timestamp():
    now = datetime.datetime.now()
    tstamp = re.sub('[-:]', '', now.isoformat('_'))
    return tstamp[:15]

def main(arguments):
    if not check_requirements():
        print('System does not meet minimum requirements.')
        exit()

    # Parse arguments
    parser = argparse.ArgumentParser()
    # parser.add_argument("-t", "--clipboard_TTL", type=int,
    #                     help="Set clipboard TTL (in seconds, default: 15)", nargs='?', const=15)
    # args = parser.parse_args()
    # print(args)
    # print args.erase_fault

    print(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
