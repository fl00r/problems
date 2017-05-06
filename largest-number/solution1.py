#!/bin/python3

def trick(n):
  return n + n[-1]

def largest_number(data):
  data_ = sorted(map(str, data), key=trick, reverse=True)
  number = int("".join(data_))
  return number

#
# TESTS
#

data = [10, 68, 75, 7, 21, 12]
res = 77568211210
res_ = largest_number(data)
if res_ != res:
  raise(Exception("Expected %s, got %s" % (res, res_)))