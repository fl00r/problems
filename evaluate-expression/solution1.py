import operator

ops = {
  "-": operator.sub,
  "+": operator.add,
}

def parse(expr):
  left = right = op = None

  i = 0
  while i < len(expr):
    c = expr[i]
    if c in ops:
      op = ops[c]
      if left is None:
        left = 0
    elif c == "(":
      val, j = parse(expr[i+1:])
      if left is None:
        left = val
      else:
        right = val
      i += j + 1
    elif c == ")":
      return left, i
    else:
      if left is None:
        left = int(c)
      else:
        right = int(c)
    if right:
      left = op(left, right)
      right = op = None
    i += 1
  return left

#
# TESTS
#

tests = [["-2+(3-5)", -4],
         ["(-1+2)-2+(3-5)+4", 1],
         ["(1+1-2)", 0],
         ["2-(3+5)", -6]]

for (expr, res) in tests:
  res_ = parse(expr)
  if res != res_:
    raise(Exception("Expected %s, got %s" % (res, res_)))