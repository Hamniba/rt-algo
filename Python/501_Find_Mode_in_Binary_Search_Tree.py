# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.nodes = []
        self.max_frequency = 0
        self.inorderTraversal(root)

        dic = {}
        for val in self.nodes:
            if val in dic:
                dic[val] += 1
            else:
                dic[val] = 1

        res = []
        for k,v in dic.items():
            if v > self.max_frequency:
                self.max_frequency = v
                res.clear()
                res.append(k)
            elif v == self.max_frequency:
                res.append(k)

        return res
        
    def inorderTraversal(self, root: TreeNode):
        if root == None:
            return
        
        self.inorderTraversal(root.left)
        self.nodes.append(root.val)
        self.inorderTraversal(root.right)
        
        
