#!/usr/bin/python3

import sys, re

regex = sys.argv[1]
file = sys.argv[2]


infile = open(file)
for line in infile:
    if re.search(regex, line):
        print(line, end="")
