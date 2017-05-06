def find_duplicate(data):
  n = len(data) - 1
  n_sum = n * (n + 1) / 2
  data_sum = sum(data)
  
  return data_sum - n_sum

# 
# TESTS
# 

test = [[[1, 2, 3, 4, 4], 4],
        [[1, 2, 3, 4, 2], 2]]

for (data, res) in test:
  res_ = find_duplicate(data)
  if res_ != res:
    raise(Exception("Expected %s, got %s" % (res, res_)))