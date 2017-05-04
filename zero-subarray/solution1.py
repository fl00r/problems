#
# O(n^2) solution
#

def subarray(data):
  l = len(data)
  res = set()

  for i in range(0, l):
    sofar = 0
    for j in range(i, l):
      sofar += data[j]
      if sofar == 0:
        res.add(tuple(data[i:j+1]))
  
  return res

# 
# TESTS
# 

data = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

res = {(3, 4, -7), 
       (4, -7, 3),
       (-7, 3, 1, 3),
       (3, 1, -4),
       (3, 1, 3, 1, -4, -2, -2),
       (3, 4, -7, 3, 1, 3, 1, -4, -2, -2)}

res_ = subarray(data)
if res_ != res:
  raise(Exception("Expected %s, got %s" % (res, res_)))