#!/usr/bin/python3

import sys
import linecache

line = sys.argv[1]
filename = sys.argv[2]
content = linecache.getline(filename, int(line))
print(content,end="")