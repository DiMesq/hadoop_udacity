#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def reducer():
  prev = None
  the_max = 0
  for line in sys.stdin:
    this, cost = line.strip().split('\t')
    cost = float(cost)
    if prev and prev != this:
      print '{0}\t{1}'.format(prev, the_max)
      the_max = 0
    if cost > the_max:
      the_max = cost
    prev = this
  print '{0}\t{1}'.format(prev, the_max)


if __name__ == '__main__':
  reducer()

