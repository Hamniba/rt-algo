class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Traversal:
    def levelOrder(self, root: TreeNode):
        if not root:
            return

        queue = []
        queue.append(root)
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.val)

            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)