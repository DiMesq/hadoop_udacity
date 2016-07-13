#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json

def reducer():
  count_by_ip = {}
  for line in sys.stdin:
    by_ip = json.loads(line)
    for k,v in by_ip.iteritems():
      count_by_ip[k] = count_by_ip.get(k, 0) + v
  for k,v in count_by_ip.iteritems():
    print '{0}\t{1}'.format(k, v)

if __name__ == '__main__':
  reducer()
