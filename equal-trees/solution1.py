def is_equal_trees(root1, root2):
  if root1 and root2:
    return root1.value == root2.value and  is_equal_trees(root1.left, root2.left) and is_equal_trees(root1.right, root2.right)
  elif not (root1 or root2):
    return True
  else:
    return False

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
root1.left.left = node3.copy()
root1.left.right = node4.copy()
root1.right.left = node5.copy()
root1.right.right = node6.copy()

root2 = BinaryTreeNode("root")
root2.left = node1.copy()
root2.right = node2.copy()
root2.left.left = node3.copy()
root2.left.right = node4.copy()
root2.right.left = node5.copy()
root2.right.right = node6.copy()

root3 = BinaryTreeNode("root")
root3.left = node2.copy()
root3.right = node1.copy()
root3.left.left = node3.copy()
root3.left.right = node4.copy()
root3.right.left = node5.copy()
root3.right.right = node6.copy()

tests = [[root1, root2, True],
         [root1, root3, False]]

for r1, r2, res in tests:
  res_ = is_equal_trees(r1, r2)
  if res_ != res:
    raise Exception("Expected %s, got %s" % (res, res_))