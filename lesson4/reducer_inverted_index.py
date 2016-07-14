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
      ids = list(ids)
      ids.sort()
      ids_as_str = ', '.join(ids)
      print '{0}\t{1}'.format(prev, ids_as_str, len(ids))
      ids=set()
    ids.add(the_id)
    prev=this
  ids = list(ids)
  ids.sort()
  ids_as_str = ', '.join(ids)
  print '{0}\t{1}\t{2}'.format(prev, ids_as_str, len(ids))

if __name__ == '__main__':
  reducer()