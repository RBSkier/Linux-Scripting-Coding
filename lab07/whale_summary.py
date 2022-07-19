#!/usr/bin/python3
import sys

for file in sys.argv[1:]:
    with open(file,'r') as infile:
        