# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def checkBST(self, root: TreeNode, lower: TreeNode, upper: TreeNode) -> bool:
        if root == None: return True

        # left subtree
        if lower != None and root.val <= lower.val:
            return False
        
        # right subtree
        if upper != None and root.val >= upper.val:
            return False
    
        return self.checkBST(root.left, lower, root) and self.checkBST(root.right, root, upper)

    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkBST(root, None, None)