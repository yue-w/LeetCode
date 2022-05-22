

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.rst = None
        self.dfs(root, p, q)
        return self.rst

    def dfs(self, node, p, q) -> int:
        """
        Return How many of p and q is the subtree with node as root.
        """
        ## Base case:
        if not node:
            return 0
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        slf = int(node.val == p.val or node.val == q.val)
        if left + right + slf == 2 and not self.rst:
            self.rst = node
        return left + right + slf



if __name__ == '__main__':

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    s = Solution()
    p = TreeNode(5)
    q = TreeNode(1)
    s.lowestCommonAncestor(root, p, q)
    print(s.rst.val)
