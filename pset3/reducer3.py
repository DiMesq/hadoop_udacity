#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def reducer():
  t_c = 0
  t_t = 0
  for line in sys.stdin:
    c, t = line.strip().split('\t')
    t_c += int(c)
    t_t += float(t)
  print '{0}\t{1}'.format(t_c, t_t)

if __name__ == '__main__':
  reducer()

