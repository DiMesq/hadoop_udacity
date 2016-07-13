#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys

def main():
  t = sys.argv[1]
  print t
  n = 200

  if t == '1':
    categories = ['tech', 'food', 'suplies', 'garden', 'home']
    for i in range(n):
      category = random.choice(categories)
      cost = random.random() * 100
      print '0\t1\t2\t{0}\t{1:.2f}\t5'.format(category, cost)

  elif t == '2':
    categories = ['LA', 'NY', 'Seattle', 'SF', 'Boston']
    for i in range(n):
      category = random.choice(categories)
      cost = random.random() * 100
      print '0\t1\t{0}\t3\t{1:.2f}\t5'.format(category, cost)


if __name__ == '__main__':
  main()
  