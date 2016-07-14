#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def mapper():
  for line in sys.stdin:
    
    parsed = line.strip().split(' ')
    if len(parsed) == 6:
      print '{0}\t{1}'.format(parsed[0], parsed[4])

if __name__ == '__main__':
  mapper()