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
            """
            flatten the tree, and return the last node of the list
            """
            # base case: leaf node:
            if not node.left and not node.right:
                return node
            
            if node.left:
                left = node.left
                node.left = None
                lst_node_lft = dfs(left)
                right = node.right
                node.right = left
                lst_node_lft.left = None
                lst_node_lft.right = right
                if right:
                    return dfs(right)
                else:
                    return lst_node_lft
            else:
                return dfs(node.right)
                     
        if not root:
            return 
        dfs(root)
        
            
    def method2(self, root):
        """
        Iteration.
        Time: O(n)
        Space: O(1)
        Reference: https://leetcode.com/problems/flatten-binary-tree-to-linked-list
        /discuss/1208004/Extremely-Intuitive-O(1)-Space-solution-with-Simple-explanation-Python
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
        
        
            