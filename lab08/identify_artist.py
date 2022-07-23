#!/usr/bin/python3
#每个歌手的文件只打开一次，遍历所有song？.txt的log-probability，最后比较输出
import sys, os, re, math

songs = sys.argv[1:]
song_dict = {}
prob_dict = {}

for song in songs:
    prob_dict = {}
    with open(song) as songfile:
        song_content = songfile.read()
        song_words = re.findall(r'[a-zA-Z]+', song_content)

        for dirpath, dirnames, filenames in os.walk(r"lyrics/"):
            for filename in sorted(filenames):
                with open(dirpath + filename) as infile:
                    artist_content = infile.read()
                    artist_content_count = len(re.findall(r'[a-zA-Z]+', artist_content))
                    artist_name = filename.replace('.txt', '').replace('_', ' ')

                    for song_word in song_words:
                        match_count = len(re.findall(r'\b' + song_word + r'\b', artist_content, flags=re.I))
                        word_log_prob = math.log((match_count + 1) / artist_content_count)
                        if artist_name in prob_dict.keys():
                            prob_dict[artist_name] += word_log_prob
                        else:
                            prob_dict[artist_name] = word_log_prob

        song_dict[song] = prob_dict
print(song_dict)
for song, prob_dict in song_dict.items():
    max_log_prob = None
    for artist_name, log_prob in prob_dict.items():
        if max_log_prob == None or log_prob > max_log_prob:
            max_log_prob = log_prob
            max_artist_name = artist_name
    print(f"{song} most resembles the work of {max_artist_name} (log-probability={max_log_prob:.1f})")
