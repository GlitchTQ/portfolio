#!/usr/bin/env python3.7

import sys
import pprint
from library import mongo


def printInfo(name):
    data = mongo.getOne(name)
    if data == 'null':
        print("Unit isn't defined")
    else:
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(data)


printInfo(sys.argv[1])
