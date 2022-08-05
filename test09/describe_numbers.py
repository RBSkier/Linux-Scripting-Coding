#!/usr/bin/python3

import sys, numpy as np, statistics, re

numbers = sys.argv[1:]
int_numbers = list(map(int, numbers))

count = len(int_numbers)
unique = len(np.unique(int_numbers))
minimum = min(int_numbers)
maximum = max(int_numbers)
mean = np.mean(int_numbers)
mean  = re.sub('\.0$','', str(mean))
median = np.median(int_numbers)
median  = re.sub('\.0$','', str(median))

mode = statistics.mode(int_numbers)
sum = sum(int_numbers)
product = np.prod(int_numbers)

print(f"count={count}")
print(f"unique={unique}")
print(f"minimum={minimum}")
print(f"maximum={maximum}")
print(f"mean={mean}")
print(f"median={median}")
print(f"mode={mode}")
print(f"sum={sum}")
print(f"product={product}")
