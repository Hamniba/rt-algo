# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ls = []
        if not root:
            return None

        self.inOrder(root)
        return self.ls[k - 1]

    def inOrder(self, root: TreeNode):
        if not root:
            return

        self.inOrder(root.left)
        self.ls.append(root.val)
        self.inOrder(root.right)
        