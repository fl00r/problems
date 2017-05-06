#!/bin/python3

#
# O(n) solution
#

def sort_binary(data):
  res = [1] * len(data)
  i = 0
  for num in data:
    if num == 0:
      res[i] = num
      i += 1
  return res

# 
# TESTS
# 

data = [1, 0, 1, 0, 1, 0, 0, 1]

res = [0, 0, 0, 0, 1, 1, 1, 1]

res_ = sort_binary(data)

if res_ != res:
  raise(Exception("Expected %s, got %s" % (res, res_)))