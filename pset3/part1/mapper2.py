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
        store = parsed[2]
        print '{0}\t{1}'.format(store, cost)

if __name__ == '__main__':
  mapper()

