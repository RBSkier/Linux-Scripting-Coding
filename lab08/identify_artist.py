#!/usr/bin/python3

import sys, os, re, math

songs = sys.argv[1:]
song_dict = {}

#loop song?.txt file
for song in songs:
    songfile = open(song)
    song_content = songfile.read()
    songfile.close()
    song_words = re.findall(r'[a-zA-Z]+', song_content)
    #loop artist files under lyrics directory
    prob_dict = {}
    for dirpath, dirnames, filenames in os.walk(r"lyrics/"):
        for filename in sorted(filenames):
            artfile = open(dirpath + filename)
            artist_content = artfile.read()
            artfile.close()
            content_count = len(re.findall(r'[a-zA-Z]+', artist_content))
            artist = filename.replace('.txt', '').replace('_', ' ')
            #loop word in song file and count log_prob
            for song_word in song_words:
                match_count = len(re.findall(r'\b' + song_word + r'\b', artist_content, flags=re.I))
                word_log_prob = math.log((match_count + 1) / content_count)
                if artist in prob_dict.keys():
                    prob_dict[artist] += word_log_prob
                else:
                    prob_dict[artist] = word_log_prob

        song_dict[song] = prob_dict

for song, prob_dict in song_dict.items():
    max_log_prob = None
    for artist_name, log_prob in prob_dict.items():
        if max_log_prob == None or log_prob > max_log_prob:
            max_log_prob = log_prob
            max_artist_name = artist_name
    print(f"{song} most resembles the work of {max_artist_name} (log-probability={max_log_prob:.1f})")


'''
song_dict structure like this:

song_dict{
    'song0.txt': {
        'Adele': -352.37652883253605, 
        'David Bowie': -386.2860456426241, 
        'Ed Sheeran': -362.5997144585678, 
        'Justin Bieber': -357.03363107323406, 
        'Keith Urban': -368.34887863590444, 
        'Leonard Cohen': -377.1864854410847, 
        'Metallica': -384.668472176448, 
        'Rage Against The Machine': -403.11054030618243, 
        'Rihanna': -362.2956821998913, 
        'Taylor Swift': -370.2747967087364
        }, 
    'song1.txt': {
        'Adele': -269.5909311403637, 
        'David Bowie': -265.5434052074425, 
        'Ed Sheeran': -267.8372415247821, 
        'Justin Bieber': -271.14715559275436, 
        'Keith Urban': -271.63155530504974, 
        'Leonard Cohen': -268.67482284842873, 
        'Metallica': -276.44885172053074, 
        'Rage Against The Machine': -265.4101627417562, 
        'Rihanna': -254.94137263700387, 
        'Taylor Swift': -270.3287066979518
        }
    ...
    }
    
'''