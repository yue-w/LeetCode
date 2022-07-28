from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.method2(root) ## preferred method
        
    def method1(self, root):
        """
        recursion:
        Time: O(n)
        Space: O(1) if not considering recursion
        """
        def dfs(node):
            if not node:
                return
            
            if not node.left:
                dfs(node.right)
                return
            
            nleft = node.left
            nright = node.right
            
            dfs(nleft)
            dfs(nright)
            
            node.left = None
            node.right = nleft
            
            while nleft.right:
                nleft = nleft.right
            nleft.right = nright
            
        dfs(root)
            
    def method2(self, root):
        """
        Iteration.
        Time: O(n)
        Space: O(1)
        Reference: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/1208004/Extremely-Intuitive-O(1)-Space-solution-with-Simple-explanation-Python
        """
        cur = root
        while cur:
            if cur.left:
                left = cur.left
                while left.right:
                    left = left.right
                left.right = cur.right
                cur.right = cur.left
                cur.left = None
                
            cur = cur.right
        
        
            