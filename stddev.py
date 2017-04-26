#! /usr/bin/python

import sys
i = 0
array = []
meansum = 0
sumdif = 0
for line in sys.stdin:
  line = line.strip()
  num = float(line)
  array.append(num)
  meansum += num
  i += 1

mean = meansum / i
  
for a in array:
  d = a - mean
  dif = d**2
  sumdif += dif

stddev = (sumdif / (i - 1))**0.5

print stddev

