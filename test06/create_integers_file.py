#!/usr/bin/python3

import sys

outfile = open(sys.argv[3], "w", encoding="utf-8")

for num in range(int(sys.argv[1]), int(sys.argv[2])+1):
    print(num, file=outfile)
    
outfile.close()