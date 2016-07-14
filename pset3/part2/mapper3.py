#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re

def mapper():
  domain = re.compile(r'^http://www\.(\w|\.)+uk')
  for line in sys.stdin:
    parsed = line.strip().split()
    if len(parsed) == 10:
      filename = parsed[6]
      m = domain.search(filename)
      if m is not None:
        filename = filename[m.end():]
      print '{0}\t1'.format(filename)

if __name__ == '__main__':
  mapper()
