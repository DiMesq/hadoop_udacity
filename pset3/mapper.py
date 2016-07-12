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
  for line in sys.stdin:
    parsed = line.strip().split('\t')
    if len(parsed) == 6:
      cost = parsed[4]
      if is_float(cost):
        category = parsed[3]
        print '{}\t{}'.format(category, cost)

if __name__ == '__main__':
  mapper()
