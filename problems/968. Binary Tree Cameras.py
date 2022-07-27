
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        """
        DFS
        Case 1: two children are coverred, do NOT cover this node
        Case 2: eigher one or none children is coverred, cover this node (only if it have two children)
        Do NOT cover leaf (unless it is also root)
        """
        if not root.left and not root.right:
            return 1
        
        
        def dfs(node):
            """
            Return state:
            0: this node is not covered
            1: this node is covered with a camera install at it.
            2: this node is covered (by camera from a child) without a camera being installed.
            """
            ## base case None:
            if not node:
                return 2
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            ## if both children are covered but neither has a camera
            if left == 2 and right == 2:
                return 0
            
            ## if one or two children are not covrered
            if left == 0 or right == 0:
                self.rst += 1
                return 1
            
            return 2
            

        self.rst = 0
        
        ## all node are taken care by their parent node. 
        ## So we need to take care of the root as well.
        rt = dfs(root)
        if rt == 0:
            self.rst += 1
        return self.rst
            
"""
[0,0,null,null,0,0,null,null,0,0]
[0,0,null,0,0]
[0,0,null,0,null,0,null,null,0]      
[0,null,0,null,0,null,0]
"""
        
            
                
            