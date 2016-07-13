#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def reducer():
  prev_category = None
  total_cost = 0 
  for line in sys.stdin:
    this, cost = line.strip().split('\t')
    if prev_category and prev_category != this:
      print '{0}\t{1}'.format(prev_category, total_cost)
      total_cost = 0
    prev_category = this
    total_cost += float(cost)
  if prev_category:
    print '{0}\t{1}'.format(prev_category, total_cost)

if __name__ == '__main__':
  reducer()
