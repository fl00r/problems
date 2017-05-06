#!/bin/python3

def find_pair(data, sum):
  numbers = {}
  
  for n in data:
    n_ = numbers.get(n, 0)
    numbers[n] = n_ + 1

  for n in data:
    m = sum - n
    m_ = numbers.get(m)

    if m_ and m == n and m_ > 1:
      return (n, m)
    elif m_ and m != n and m_ > 0:
      return (n, m)

# 
# TESTS
# 

data = [5, 8, 1, 5, 6, 3, 4]

test_suit = [[10, (5, 5)],
             [11, (5, 6)],
             [100, None]]

for (sum, res) in test_suit:
  res_ = find_pair(data, sum)
  if res_ != res:
    raise(Exception("Expected %s, got %s" % (res, res_)))