# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.queue = []
        if not root:
            return False

        self.preOrder(root)
        unique = set(self.queue)
        if len(unique) > 1:
            return False
        else:
            return True
        
    def preOrder(self, root: TreeNode):
        if not root:
            return
        
        self.queue.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

        