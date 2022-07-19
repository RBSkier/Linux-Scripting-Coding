#!/usr/bin/python3

import sys
import collections
import re
dict = {}
files = sys.argv[1:]
for file in files:
    with open(file,"r") as infile:
        for line in infile:
            line = re.sub(r'\s+', ' ', line)
            lineInfo = line.split(" ", 2)
            if len(lineInfo) < 3:
                continue
            if lineInfo[2][0:-1].lower() in dict.keys():
                dict[lineInfo[2][0:-1].lower()][0] += 1
                dict[lineInfo[2][0:-1].lower()][1] += int(lineInfo[1])
            elif lineInfo[2][0:-2].lower() in dict.keys():
                dict[lineInfo[2][0:-2].lower()][0] += 1
                dict[lineInfo[2][0:-2].lower()][1] += int(lineInfo[1])
            else:
                if lineInfo[2][-2] == 's':
                    dict[lineInfo[2][0:-2].lower()] = [1, int(lineInfo[1])]
                else:
                    dict[lineInfo[2][0:-1].lower()] = [1, int(lineInfo[1])]
for k in sorted(dict):
    print(k + " observations:", dict[k][0], "pods,", dict[k][1], "individuals")