#!/usr/bin/python3

import re
import sys
import os
file = sys.argv[1]
digitals = re.compile(r'\d+', re.I)
fp = open(os.path.join(file),'r')
data = fp.readlines()
sum = 0
digits = []
l = []
for i in data:
    digital = re.findall(digitals, i)
    digits.append([int(i) for i in digital])
file_digits = [i for i in digits if i != []]
del digits
for i in range(0, len(file_digits)):
    for j in file_digits[i]:
        l.append(j)
for i in l:
    sum = sum + i
print(sum)
