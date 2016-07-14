#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
import csv

def read(delim=','):
  reader = csv.reader(sys.stdin, delimiter=delim)
  for line in reader:
    yield line

def is_int(s):
  try:
    n = int(s)
    return True
  except ValueError:
    return False

def mapper():
  split_by = re.compile(r'\W+')
  for l in read(delim='\t'):
    if len(l) == 19 and is_int(l[0]):
      words = split_by.split(l[4])
      for word in words:
        print '{0}\t{1}'.format(word.lower(), l[0]) 

def create_test(file, delim='\t'):
  with open(file, 'wb') as csvf:
    writer = csv.writer(csvf, delimiter=delim, quotechar='"', quoting=csv.QUOTE_ALL)
    n=10
    for i in range(10):
      writer.writerow([i, 1, 1, 1, (i+1)*10] + [1]*14)
if __name__ == '__main__':
  #create_test('testfile')
  mapper()
