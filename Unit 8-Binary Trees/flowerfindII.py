"""_summary_
        Consider the following function non_bst_find_flower() which accepts the root of a binary tree inventory and a flower name, and returns True if a flower (node) with name exists in the binary tree. Unlike the previous problem, this tree is not a binary search tree.

    Compare your solution to find_flower() in Problem 2 to the following solution. Discuss with your group: How is the code different? Why?
    What is the time complexity of non_bst_find_flower()? How does it compare to the time complexity of find_flower() in Problem 2?
    How would the time complexity of find_flower() from Problem 2 change if the tree inventory was not balanced?
    class TreeNode:
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right

    def non_bst_find_flower(root, name):
        if root is None:
            return False
        
        if root.val == name:
            return True

        return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)
    Example Usage:
    """
class TreeNode:
        def __init__(self, value, left=None, right=None):
            self.val = value
            self.left = left
            self.right = right

def non_bst_find_flower(root, name):
        if root is None:
            return False
        
        if root.val == name:
            return True

        return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

    
        
    
"""
    Understand:
     since the last one was binary tree we knew where to go, this we cant do it, and we must check everything 
     which would cause more run time
     The binary tree we dont have to go in each order so the bst would be time: o(n) space : o(H)
     The 
    """
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(non_bst_find_flower(garden, "Lilac"))  
print(non_bst_find_flower(garden, "Sunflower"))  
    