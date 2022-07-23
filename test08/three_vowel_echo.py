#!/usr/bin/python3
import sys, re

words = sys.argv[1:]
output_list = []

for word in words:
    match_list = re.findall(r'[aeiouAEIOU]{3}', word)
    if len(match_list) != 0:
        output_list.append(word)
        
print(*output_list)