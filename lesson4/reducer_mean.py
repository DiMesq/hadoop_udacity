#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from datetime import datetime

def reducer():
  prev = None
  total = 0
  count = 0
  for line in sys.stdin:
    date, sales = line.strip().split('\t')
    this = datetime.strptime(date, "%Y-%m-%d").weekday()
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

