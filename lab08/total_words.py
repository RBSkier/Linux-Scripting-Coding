#!/usr/bin/python3

import sys, re

contents = sys.stdin.read()
match_list = re.findall(r'[a-zA-Z]+', contents)
print(f"{len(match_list)} words")