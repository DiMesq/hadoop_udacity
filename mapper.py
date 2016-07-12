#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def is_float(s):
  try:
    n = float(s)
    return True
  except Exception:
    return False

def mapper():
  for line in sys.stdin:
    parsed = line.strip().split(' ')
    if len(parsed) == 3:
      store, product, cost = parsed
      if is_float(cost):
        print '{}\t{}'.format(store, cost)

if __name__ == '__main__':
  mapper()  