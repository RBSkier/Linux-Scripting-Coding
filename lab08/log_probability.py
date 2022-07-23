#!/usr/bin/python3

import sys, os, re, math

phrase = sys.argv[1:]
prob_dict = {}

for dirpath, dirnames, filenames in os.walk(r"lyrics/"):
    for filename in sorted(filenames):
        with open(dirpath + filename) as infile:
            content = infile.read()
            all_word_num = len(re.findall(r'[a-zA-Z]+', content))
            artist = filename.replace('.txt', '').replace('_', ' ')
            for word in phrase:
                match_count = len(re.findall(r'\b' + word + r'\b', content, flags=re.I))
                word_log_prob = math.log((match_count + 1)/all_word_num)
                if artist in prob_dict.keys():
                    prob_dict[artist] += word_log_prob
                else:
                    prob_dict[artist] = word_log_prob
#output
for artist, log_prob in prob_dict.items():
    print(f"{log_prob:10.5f} {artist}")