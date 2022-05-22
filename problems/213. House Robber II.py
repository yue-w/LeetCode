
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        DP bottom up
        """
        if len(nums) == 1:
            return nums[0]
        memo = {}
        
        rst1 = self.recursion(nums, 0, len(nums) - 2, memo)
        rst2 = self.recursion(nums, 1, len(nums) - 1, memo)
        return max(rst1, rst2)

        
    def recursion(self, nums, i, j, memo):    
        ## Base case
        if i > j:
            return 0
        if i == j:
            memo[(i, j)] = nums[i]
            return nums[i]
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        ## rob first house
        num1 = nums[i] + self.recursion(nums, i + 2, j, memo)
        ## do not rob first house
        num2  = self.recursion(nums, i + 1, j, memo)
        memo[(i, j)] = max(num1, num2)
        return max(num1, num2)
        
        
