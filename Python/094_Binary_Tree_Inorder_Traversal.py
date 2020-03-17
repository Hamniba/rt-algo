# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        
        result = []
        stack = []
        while root != None or len(stack) != 0:
            while root != None:
                stack.append(root)
                root = root.left
                
            if len(stack) != 0:
                node = stack.pop()
                result.append(node.val)
                root = node.right
                
        return result      
        
        