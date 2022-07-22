#!/usr/bin/python3

import sys, os, re, math

phrase = sys.argv[1:]
phrase_prob = {}

for dirpath, dirnames, filenames in os.walk(r"lyrics/"):
    for filename in sorted(filenames):
        with open(dirpath + filename) as infile:
            content = infile.read()
            word_count = re.findall(r'[a-zA-Z]+', content)
            artist = filename.replace('.txt', '').replace('_', ' ')
            for word in phrase:
                match_count = re.findall(r'\b' + word + r'\b', content, flags = re.I)
                word_prob = math.log(float(format(len(match_count)/len(word_count), '.9f')))
                if artist in phrase_prob.keys():
                    phrase_prob[artist] += word_prob
                else:
                    phrase_prob[artist] = word_prob

print(phrase_prob)
                