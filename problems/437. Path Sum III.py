

from collections import defaultdict
from typing import Optional

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.prefixsum = defaultdict(int)
        ## add 0 into the prefixsum, which is a common edge case for prefix sum
        self.prefixsum[0] = 1
        curr_sum = 0
        return self.dfs(root, targetSum, curr_sum)
        
    def dfs(self, node, targetSum, curr_sum):
        ## Base case
        if not node:
            return 0
        
        """
        on the path from root to the current node, use the  prefixsum to
        find the number of sums equal the targetSum
        """
        curr_sum += node.val
        need = curr_sum - targetSum
        count = self.prefixsum[need]
        
        ## add the current prefix sum into the prefixsum hash
        self.prefixsum[curr_sum] += 1
        
        ## recursion on left tree
        count += self.dfs(node.left, targetSum, curr_sum)
        count += self.dfs(node.right, targetSum, curr_sum)
        
        ## Remove the current prefix sum from the prefixsum hash
        self.prefixsum[curr_sum] -= 1
        
        return count
        
        
        
        
        
    
        
#         self.count = 0
#         # self.prefixsum = {}
        
#         self.dfs(root, targetSum)
        
#         return self.count

#     def dfs(self, node, targetSum):
#         ## base case: leaf node. (node cannot be None)
#         if not node.left and not node.right:
#             if node.val == targetSum:
#                 self.count += 1
#             return [set([0, node.val])]
        
#         if node.left:
#             left_pre_fix_sum = self.dfs(node.left, targetSum)
#             # need = targetSum - node.val
#             # if need in left_pre_fix_sum:
#             #     self.count += 1
#         else:
#             left_pre_fix_sum = [set()]
                
#         if node.right:
#             right_pre_fix_sum = self.dfs(node.right, targetSum)
#             # need = targetSum - node.val
#             # if need in right_pre_fix_sum:
#             #     self.count += 1
#         else:
#             right_pre_fix_sum = [set()]
                
#         ## Combine two list
#         pre_fix_sum = left_pre_fix_sum + right_pre_fix_sum
            
#         ## add node val to the prefix sum
#         for aset in pre_fix_sum:
#             for v in aset:
#                 aset.pop(v)
#                 aset.add(v + node.val)
                
        
#         need = 
        
        
#         return pre_fix_sum
            
        
        
        
"""
Hash 
DFS
Prefixsum
"""
        