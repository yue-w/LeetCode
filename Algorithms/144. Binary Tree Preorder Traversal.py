# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.method1(root)
    def method1(self, root):
        """
        Recursion
        """
        
        def dfs(node):
            ## base case
            if not node:
                return
            rst.append(node.val)
            dfs(node.left)
            dfs(node.right)
  
            
        rst = []
        dfs(root)
        return rst
    
    def method2(self, root):
        """
        Iteration
        """
        if not root:
            return []
        stack = []
        rst = []
        
        stack.append(root)
        
        while stack:
            node = stack.pop()
            rst.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return rst