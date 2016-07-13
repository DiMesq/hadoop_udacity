#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def mapper():
  for line in sys.stdin:
    parsed = line.strip().split()
    if len(parsed) == 10:
      ip = parsed[0]
      print '{0}\t1'.format(ip)

if __name__ == '__main__':
  mapper()
