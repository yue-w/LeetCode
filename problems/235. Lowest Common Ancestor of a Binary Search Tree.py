
##Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.iteration(root, p, q)
        return self.recursion(root, p, q)
    def iteration(self, root, p, q):
        node = root
        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
                
            else:
                return node


    def recursion(self, root, p, q):
        ## Base case:
        if (root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val):
            return root
        if p.val <= root.val and q.val <=root.val:
            return self.recursion(root.left, p, q)
        else:
            return self.recursion(root.right, p, q)
                