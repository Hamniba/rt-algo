# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        if s.val != t.val:
            return False

        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t: 
            return True
        if not s:
            return False
        if self.isSameTree(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        

# isSameTree 判断两棵树是否相等
# isSubtree 里面，如果 s 和 t 不相等，就分别比较 s 的左子树和右子树是否与 t 相等