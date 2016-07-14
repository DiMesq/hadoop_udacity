#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from datetime import datetime

def mapper():
  for line in sys.stdin:
    parsed = line.strip().split('\t')
    if len(parsed) == 6:
      weekday = datetime.strptime(parsed[0], "%Y-%m-%d").weekday()
      print '{0}\t{1}'.format(weekday, parsed[4])

if __name__ == '__main__':
  mapper()