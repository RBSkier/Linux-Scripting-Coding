#!/usr/bin/python3

import sys, re

input_str = sys.stdin.read()
numbers = re.findall(r"-?\d+\.?\d*|-?\.?\d+", input_str)

max = None

for number in numbers:
    if max == None or float(number) > float(max):
        max = number

if max != None:
    lines = re.split('\n', input_str)
    for line in lines:
        if re.search(max, line):
            print(line)
else:
    exit(0)