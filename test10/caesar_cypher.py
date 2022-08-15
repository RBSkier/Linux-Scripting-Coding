#!/usr/bin/python3

import sys

key = int(sys.argv[1])

while True:
    try:
        a = input()
    except EOFError:
        exit(0)

    for character in a:
        if character.isalpha():
            ascii = ord(character) + key
            if character.isupper():
                if ascii > ord('Z'):
                    ascii = ord('A') + (ascii-90)%26 - 1
                if ascii < ord('A'):
                    ascii = ord('Z') - (65-ascii)%26 + 1
            elif character.islower():
                if ascii > 122:
                    ascii = ord('a') + (ascii-122)%26 - 1
                if ascii < 97:
                    if (97 - ascii)% 26 == 0:
                        ascii = 97
                    else:
                        ascii = ord('z') - (97 - ascii) % 26 + 1
            new_character = chr(ascii)
            print(new_character, end='')
        else:
            print(character, end = '')
    if key >100:
        exit(0)
    else:
        print()

import sys

offset = int(sys.argv[1])

for text in sys.stdin.readlines():
  cipherText = ""
  for i in range(len(text)):
    x = text[i]
    if x >= 'a' and x <= 'z':
      cipherText += chr( ord('a') + (ord(x) - ord('a') + offset) % 26)
    elif x >= 'A' and x <= 'Z':
      cipherText += chr( ord('A') + (ord(x) - ord('A') + offset) % 26)
    else:
      cipherText += text[i]
  print(cipherText , end = "")
