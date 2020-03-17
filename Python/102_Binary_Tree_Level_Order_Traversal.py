# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return

        queue = []
        queue.append([root])
        result = []
        result.append([root.val])

        while len(queue) != 0:
            nodes = queue.pop()

            ls = []
            nums = []
            for node in nodes:    
                if node.left != None:
                    ls.append(node.left)
                    nums.append(node.left.val)
                if node.right != None:
                    ls.append(node.right)
                    nums.append(node.right.val)
                
            if len(ls) != 0:
                queue.append(ls)
                result.append(nums)

        return result


# 这道题跟普通的 traversal by level 不同的是要注意它的输出是二维数组
# 每一层在一个子数组里，注意构造这种形式
# 解题思维还是跟 traversal by level 一样