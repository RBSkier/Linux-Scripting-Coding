#!/usr/bin/python3
import sys

count = 0
for file in sys.argv[1:]:
    with open(file, "r") as infile:
        for line in infile:
            if "Orca" in line:
                data = line.split()
                count += int(data[1])
print(count, "Orcas reported")