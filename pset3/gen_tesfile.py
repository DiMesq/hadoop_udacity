#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def main():
  categories = ['tech', 'food', 'suplies', 'garden', 'home']
  n = 200
  for i in range(n):
    category = random.choice(categories)
    cost = random.random() * 100
    print '0\t1\t2\t{}\t{:.2f}\t5'.format(category, cost)

if __name__ == '__main__':
  main()