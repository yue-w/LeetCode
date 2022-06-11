from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #return self.kadane(nums)
    
        return self.kadane2(nums)

    def kadane(self, nums):
        """
        Time: O(n)
        Space: O(n)
        """
        cur_max = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            global_max = max(global_max, cur_max)
        return global_max
                
    
    def kadane2(self, nums):
        """
        optimized Kadane, update a virable instead an array.
        Runtime: O(n),
        Space: O(1)
        """
        ans = nums[0]
        cumsum = nums[0]
        for i in range(1, len(nums)):
            cumsum = max(nums[i] + cumsum, nums[i]) 
            ans = max(ans, cumsum)
        return ans

"""
Similar problem 152
"""
                