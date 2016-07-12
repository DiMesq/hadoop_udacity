#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def reducer():
  prev_store = None
  total_sum = 0
  for line in sys.stdin:
    this, cost = line.strip().split('\t')

    if prev_store and this != prev_store:
      print '{}\t{}'.format(prev_store, total_sum)
      total_sum = 0

    prev_store = this
    total_sum += float(cost)

  print '{}\t{}'.format(prev_store, total_sum)

if __name__ == '__main__':
  reducer()

