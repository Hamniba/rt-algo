# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        level = [root]
        while len(level) != 0:
            ls = []
            for node in level:
                if node.left != None:
                    ls.append(node.left)
                if node.right != None:
                    ls.append(node.right)

            if len(ls) != 0:
                level = ls
            else:
                break

        result = 0
        for node in level:
            result += node.val

        return result



# traversal by level, and return sum of the last level items.