#!/bin/python3

#
# O(A(r,n)) ~= O(n!)
#

def permutations(data, r):
  for i, d in enumerate(data):
    if r > 1:
      data_ = data[:i] + data[i+1:]
      for p in permutations(data_, r - 1):
        yield [d] + p
    else:
      yield [d]

def tricky_combinations(n):
  res = []
  data = list(range(2*n))
  for permutation in permutations(data, n):
    inter = [None] * 2 * n
    for i, m in enumerate(permutation):
      m_ = m + i + 2
      if m_ >= 2 * n or inter[m_] or inter[m]:
        inter = None
        break
      inter[m] = i + 1
      inter[m_] = i + 1
    if inter:
      res.append(inter)
  return res

#
# TESTS
#

data = [[3, [[3, 1, 2, 1, 3, 2], [2, 3, 1, 2, 1, 3]]],
        [4, [[4, 1, 3, 1, 2, 4, 3, 2], [2, 3, 4, 2, 1, 3, 1, 4]]],
        [5, []]]
for (n, res) in data:
  res_ = tricky_combinations(n)
  if res_ != res:
    raise(Exception("Expected %s, got %s" % (res, res_)))