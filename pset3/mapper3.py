#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def is_float(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def mapper():
  c=0
  total_sales = 0
  for line in sys.stdin:
    parsed = line.strip().split('\t')
    if len(parsed) == 6:
      cost = parsed[4]
      if is_float(cost):
        total_sales += float(cost)
        c+=1
  print '{0}\t{1}'.format(c, total_sales)

if __name__ == '__main__':
  mapper()

