#!/usr/bin/python3

import sys, re

a = sys.stdin.read()
b = a.strip().split('\n')

for line in b:
    matches = re.findall(r'(\d+)\.(\d+)', line)
    for match in matches:
        int_num = match[0]
        little_num = match[1]
        if int(little_num[0]) < 5:
            line = re.sub(r'(\d+)\.' + little_num, r'\1', line)
        else:        
            line = re.sub(r'(\d+)\.' + little_num, r'\1', line)
            new_int_num = str(int(int_num) + 1)
            line = re.sub(int_num, new_int_num, line)
    print(line)