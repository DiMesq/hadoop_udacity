#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def reducer():
  prev = None
  count = 0
  for line in sys.stdin:
    this = line.strip().split('\t')[0]
    if prev and prev != this:
      print '{0}\t{1}'.format(prev, count)
      count=0
    prev=this
    count+=1
  print '{0}\t{1}'.format(prev, count)

if __name__ == '__main__':
  reducer()
