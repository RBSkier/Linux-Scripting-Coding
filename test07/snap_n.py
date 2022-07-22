#!/usr/bin/python3

import sys

times = int(sys.argv[1])
str_dict = {}

for line in sys.stdin:
    if line not in str_dict.key():
        str_dict[line] = 1
    else:
        str_dict[line] += 1
        if str_dict[line] == times:
            print("Snap: " + line, end = '')
            exit(0)