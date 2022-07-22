#!/usr/bin/python3

import sys

str_list = []

for str in sys.argv[1:]:
    if str not in str_list:
        str_list.append(str)
        
for element in str_list:
    print(element, end = ' ')

print()