#!/usr/bin/python3
import sys, re

numbers = []

with open(sys.argv[1], 'r') as infile:
    contents = infile.read()
    numbers += re.findall(r'\d+', contents)

numbers = list(map(int,numbers))
total = sum(numbers)
print(total)