class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def preorder(root):
    res = []
    if root is None:
        return res
    
    stack = [root]
    
    while stack:
        curr = stack.pop()
        res.append(curr.data)
        
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res

       
    
    
    
        
        
        
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(6)

print(preorder(root))
 


    
