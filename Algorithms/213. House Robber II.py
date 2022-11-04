
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        #return self.method1(nums)
        return self.method2(nums)
        
    def method1(self, nums):
        """
        DP recursion
        """
        if len(nums) == 1:
            return nums[0]
        memo = {}
        
        rst1 = self.recursion(nums, 0, len(nums) - 2, memo)
        rst2 = self.recursion(nums, 1, len(nums) - 1, memo)
        return max(rst1, rst2)

    def method2(self, nums):
        """
        DP table. Preferred method.
        State of dp:
        dp_rob[i]: max amount if rob house i. dp_rob[i]
                  dp_rob[i] = max(dp_not[i-1] + nums[i])
        dp_notrob[i]: max amount if not rob house i. dp_notrob[i]. 
                  dp_notrob[i] = max(dp_rob[i-1], dp_notrob[i-1])
        consider two cases: 
            1. if rob house 1, house n cannot be robbed.
            2. if not rob house 1, house n may be robbed. 
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        rob = nums[0]
        notrob = 0
        ## case 1, rob first house, then the last house must not be robbed
        for i in range(1, len(nums) - 1):
            notrobtmp = notrob
            notrob = max(rob, notrob)
            rob = notrobtmp + nums[i]
        case1 = max(rob, notrob)
            
        ## case 2, do not rob the first house, the last house mau be robbed
        rob = nums[1]
        notrob = 0
        for i in range(2, len(nums)):
            notrobtmp = notrob
            notrob = max(rob, notrob)
            rob = notrobtmp + nums[i]
        case2 = max(rob, notrob)
        return max(case1, case2)
        
        
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
        
        
