#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def reducer():
  prev = None
  total = 0
  count = 0
  for line in sys.stdin:
    weekday, sales = line.strip().split('\t')
    
    if prev and this != prev:
      print '{0}\t{1}'.format(prev, float(total)/count)
      total=0
      count=0
    total+=float(sales)
    count+=1
    prev = this

  print '{0}\t{1}'.format(prev, total/float(count))

if __name__ == '__main__':
  reducer()

