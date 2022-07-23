#!/usr/bin/python3

import sys, re

contents = sys.stdin.read()
match_count = len(re.findall(r'[a-zA-Z]+', contents))
print(f"{match_count} words")