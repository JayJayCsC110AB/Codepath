from collections import deque
"""
You are grafting different varieties of apple onto the same root tree can produce many different varieties of apples! Given the following TreeNode class, create the binary tree depicted below. The text representing each node should should be used as the value.

The root, or topmost node in the tree TreeNode("Trunk") has been provided for you.

             Trunk
          /         \
      Mcintosh   Granny Smith
      /     \       /     \
    Fuji   Opal   Crab   Gala
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

root = TreeNode("Trunk")
Example Usage:

# Using print_tree() included at the top of this page
print_tree(root)
Example Output:

['Trunk', 'Mcintosh', 'Granny Smith', 'Fuji', 'Opal', 'Crab', 'Gala']

"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
        if not root:
            return []
        #define an array to store the values
        res = []
        #define a Queue to iterate through tree and store into array
        queue = deque([root])
        
        #loop through queue 
        while queue:
            #remove node from queue 
            node = queue.popleft()
            #store the popped 
            res.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")
root.right = TreeNode("Granny Smith")
root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")
root.right.right = TreeNode("Crab")
root.right.left = TreeNode("Gala")
print(print_tree(root))
