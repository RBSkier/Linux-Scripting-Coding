#!/usr/bin/python3

import sys, re

pattern = sys.argv[1]
contents = sys.stdin.read()

match_count = len(re.findall(r'\b' + pattern + r'\b', contents, flags = re.I))
print(f"{pattern} occurred {match_count} times")