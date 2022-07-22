#!/usr/bin/python3

import sys, os, re

pattern = sys.argv[1]

for dirpath, dirnames, filenames in os.walk(r"lyrics/"):
    for filename in sorted(filenames):
        with open(dirpath + filename) as infile:
            content = infile.read()
            word_list = re.findall(r'[a-zA-Z]+', content)
            match_list = re.findall(r'\b' + pattern + r'\b', content, flags = re.I)
            artist = filename.replace('.txt', '').replace('_', ' ')
            print(f"{len(match_list):4}/{len(word_list):6} = {len(match_list)/len(word_list):.9f} {artist}")