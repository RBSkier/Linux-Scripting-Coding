#!/usr/bin/python3

import sys

file = sys.argv[1]

with open(file) as infile:
    content = infile.readlines()
    if len(content) == 0:
        exit(0)
    elif len(content)%2 == 1:
        middle_line_num = int(len(content)/2)
        print(content[middle_line_num], end = '')
    else:
        middle_line_num = int(len(content)/2)
        print(content[middle_line_num - 1], end = '')
        print(content[middle_line_num], end = '')