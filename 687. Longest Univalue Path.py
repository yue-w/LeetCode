##Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = 0
        self.helper(root)
        return self.max
    
    def helper(self, node):
        if not node:
            return 0
        
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        leftV = 0
        if node.left and node.val == node.left.val:
            leftV = 1 + left

        rightV = 0 
        if node.right and node.val == node.right.val:
            rightV = 1 + right
            
        self.max = max(rightV+leftV, self.max)
        
        return max(leftV, rightV)


node = TreeNode(5)
node.left = TreeNode(4)
node.right = TreeNode(5)
node.left.left  = TreeNode(1)
node.left.right  = TreeNode(1)
node.right.right = TreeNode(5)
print(Solution().longestUnivaluePath(node))