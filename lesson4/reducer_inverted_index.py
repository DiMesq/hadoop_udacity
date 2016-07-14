#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

def reducer():
  ids=set()
  prev=None
  for line in sys.stdin:
    this, the_id = line.split('\t')
    the_id = the_id.strip()
    if prev and this != prev:
      ids_as_str = ', '.join(ids)
      print '{0}\t{1}'.format(prev, ids_as_str)
      ids=set()
    ids.add(the_id)
    prev=this
  ids_as_str = ', '.join(ids)
  print '{0}\t{1}'.format(prev, ids_as_str)

if __name__ == '__main__':
  reducer()