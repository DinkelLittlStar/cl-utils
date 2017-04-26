#! /usr/bin/python

import sys

sum = 0
i = 0  
for line in sys.stdin:
  line = line.strip()
  num = float(line)
  sum += num
  i += 1
avg = sum/i
print avg
