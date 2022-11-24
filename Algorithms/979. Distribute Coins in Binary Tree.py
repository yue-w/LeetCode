
from collections import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        """
        Reference:
        https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221939/C%2B%2B-with-picture-post-order-traversal
        We traverse childs first (post-order traversal), and return the ballance
         of coins. For example, if we get '+3' from the left child, that means 
         that the left subtree has 3 extra coins to move out. If we get '-1' 
         from the right child, we need to move 1 coin in. So, we increase the 
         number of moves by 4 (3 moves out left + 1 moves in right). We then 
         return the final ballance: 
         r->val (coins in the root) + 3 (left) + (-1) (right) - 1 (keep one coin for the root).
        """
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.rst += abs(left) + abs(right) + node.val - 1
            return node.val + left + right - 1
        
        self.rst = 0
        dfs(root)
        
        return self.rst