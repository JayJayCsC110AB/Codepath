class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    if root.val == "+":
        return root.left.val + root.right.val
    elif root.val == "-":
        return root.left.val - root.right.val
    elif root.val == "*":
        return root.left.val * root.right.val
    elif root.val == "/":
        return root.left.val / root.right.val
"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
pear_tree = TreeNode("-", TreeNode(7), TreeNode(5))

print(calculate_yield(pear_tree))