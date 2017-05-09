def change(amount, denominations):
  res = []
  for i, n in enumerate(denominations):
    amount_ = amount - n
    if amount_ == 0:
      res.append([n])
    elif amount_ > 0:
      res += [[n] + x for x in change(amount_, denominations[i:])]
  return res

def change_coin(amount, denominations):
  res = change(amount, sorted(list(denominations)))
  return len(res)

#
# TESTS
#

tests = [[8, { 1, 3, 5, 7 }, 6],
         [4, { 1, 2, 3 }, 4]]

for (amount, nominations, res) in tests:
  res_ = change_coin(amount, nominations)
  if res != res_:
    raise(Exception("Expected %s got %s" % (res, res_)))