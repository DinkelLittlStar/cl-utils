#! /usr/bin/python

import sys

i = 0
mean = 0
meansum = 0
sumdif = 0
array = []
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

sttdev = (sumdif / (i - 2))**0.5

uncertainty = sttdev / (mean**0.5)
print uncertainty

