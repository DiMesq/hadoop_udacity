#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def reducer():
  prev = None
  count = 0
  max_count = 0
  max_file = None

  for line in sys.stdin:
    this = line.strip().split('\t')[0]
    if prev != this:
      if max_count < count:
        max_count=count
        max_file=prev
      count=0
    prev=this
    count+=1
  if max_count < count:
    max_file=prev
    max_count=count
  print '{0}\t{1}'.format(max_file, max_count)

if __name__ == '__main__':
  reducer()
