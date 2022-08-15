#!/usr/bin/python3

import sys, re

a = sys.stdin.read()
b = a.strip().split('\n')
for line in b:
    regex = re.search('^#(\d+)$', line)
    if regex:
        num = int(regex.group(1))
        line = b[num-1]
    print(line)