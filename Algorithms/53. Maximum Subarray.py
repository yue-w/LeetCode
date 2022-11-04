from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #return self.method1(nums)
        return self.method2(nums) ## preferred method
    
    def method1(self, nums):
        """
        Kadane.
        Time: O(n)
        Space: O(n)
        """
        accsum = nums[:]
        for i in range(1, len(accsum)):
            accsum[i] = max(accsum[i]+accsum[i-1], accsum[i])
        
        return max(accsum)

    def method2(self, nums):
        """
        Kadane. (matain only relevant variables without saving the whole table)
        Time: O(n)
        Space: O(1)
        """
        cur_max = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            global_max = max(global_max, cur_max)
        return global_max
                
    

        
            

"""
Similar problem 152
"""
                