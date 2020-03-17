# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minNode(self, node: TreeNode) -> TreeNode:
        while node.left != None:
            node = node.left
        
        return node
            

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if root.val == key:
            if root.left == None and root.right == None:
                root = None
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            if root.left != None and root.right != None:
                minimal = self.minNode(root.right)
                root.val = minimal.val
                root.right = self.deleteNode(root.right, minimal.val)
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root