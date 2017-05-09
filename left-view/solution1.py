def left_view(root):
  res = []
  stack = [(root, 0, 0)]
  for s in stack:
    node, x, y = s
    if len(res) <= y:
      res.append(node.value)
    if node.left:
      stack.append((node.left, x * 2, y + 1))
    if node.right:
      stack.append((node.right, x * 2 + 1, y + 1))

  return res

#
# TESTS
#

class BinaryTreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
  def set_left(self, left):
    self.left = left

  def set_right(self, right):
    self.right = right

  def copy(self):
    new = BinaryTreeNode(self.value)
    new.left = self.left
    new.right = self.right
    return new


node1 = BinaryTreeNode(1)
node2 = BinaryTreeNode(2)
node3 = BinaryTreeNode(3)
node4 = BinaryTreeNode(4)
node5 = BinaryTreeNode(5)
node6 = BinaryTreeNode(6)

root1 = BinaryTreeNode("root")
root1.left = node1.copy()
root1.right = node2.copy()
root1.left.right = node3.copy()
root1.right.left = node4.copy()
root1.right.right = node5.copy()
root1.right.right.right = node6.copy()

res = ["root", 1, 3, 6]
res_ = left_view(root1)
if res != res_:
  raise Exception("Expected %s got %s" % (res, res_))

