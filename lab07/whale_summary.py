#!/usr/bin/python3
import sys
import re

species_data={}

for file in sys.argv[1:]:
    with open(file, 'r') as infile:
        for line in infile:
            line = line.strip().lower()
            line = re.sub("\s+", ' ', line)
            line = re.sub("([^'s])s($| )", r"\1", line)
            data = re.split(' ', line, 2)
            if data[2].lower() in species_data.keys():
                species_data[data[2]][0] += 1
                species_data[data[2]][1] += int(data[1])
            else:
                species_data[data[2]] = [1, int(data[1])]

for species_name, amount in sorted(species_data.items()):
    print(species_name + " observations: " + 
        str(amount[0]) + " pods, " + 
        str(amount[1]) + " individuals")