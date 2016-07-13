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
    parsed = line.strip().split()
    if len(parsed) == 10:
      filename = parsed[6]
      print '{0}\t1'.format(filename)

if __name__ == '__main__':
  mapper()
