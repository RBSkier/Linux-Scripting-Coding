#!/usr/bin/python3

import sys, re

content_list = []
input_count = 0
type_count = 0

while True:
    try:
        content = input().strip().lower()
        content = re.sub(r'\s+', ' ', content)
        input_count += 1
    except EOFError:
        print(f"End of input reached after {input_count} lines read - {sys.argv[1]} different lines not seen.")
        exit(0)

    if content not in content_list:
        content_list.append(content)
    if len(content_list) == int(sys.argv[1]):
        print(f"{sys.argv[1]} distinct lines seen after {input_count} lines read.")
        exit(0)