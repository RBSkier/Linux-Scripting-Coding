#!/usr/bin/python3

import sys

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

content_list = input_file.readlines()
contentall = [x.strip() for x in content_list]
contentall_new = contentall[::-1]
for x in contentall_new:
    output_file.write(x +"\n")

input_file.close()
output_file.close()