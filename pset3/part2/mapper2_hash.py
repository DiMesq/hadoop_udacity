#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
from collections import defaultdict

def mapper():
  count_by_ip = defaultdict(int)  
  for line in sys.stdin:
    parsed = line.strip().split()
    if len(parsed) == 10:
      ip = parsed[0].strip()
      count_by_ip[ip] += 1

  print(json.dumps(count_by_ip))
  

if __name__ == '__main__':
  mapper()
