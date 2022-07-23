#!/usr/bin/python3

import sys

with open(sys.argv[1]) as infile:
    content_list = list(infile)
    content_list.sort(key = lambda x: (len(x), x))
    for item in content_list:
        print(item, end = "")