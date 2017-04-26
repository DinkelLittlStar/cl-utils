#! /usr/bin/python

import fileinput

sum = 0
i = 0  
for line in fileinput.input():
  line = line.strip()
  num = float(line)
  sum += num
  i += 1
avg = sum/i
print avg
