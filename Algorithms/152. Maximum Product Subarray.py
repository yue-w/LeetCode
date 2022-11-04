
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return self.method1(nums)
    
    def method1(self, nums):
        """
        Modified Kadane's algorithm
        Time: O(n)
        Space: O(1) (matain only relevant variables without save the whole table)
        """
        cur_max = nums[0]
        cur_min = nums[0]
        global_max = nums[0]
        
        for i in range(1, len(nums)):
            ## back_up cur_max[i - 1] and cur_min[i - 1]
            cur_max_backup = cur_max
            cur_min_backup = cur_min
            cur_max = max(cur_max_backup * nums[i], cur_min_backup * nums[i], nums[i])
            cur_min = min(cur_max_backup * nums[i], cur_min_backup * nums[i], nums[i])
            global_max = max(cur_max, cur_min, global_max)
        
        return global_max
        
    def method2(self, nums):
        """
        Modified Kadane's algorithm
        Time: O(n)
        Space: O(n)
        """
        submax = [0] * len(nums)
        submin = [0] * len(nums)
        submax[0] = nums[0]
        submin[0] = nums[0]
        maxv = nums[0]
        for i in range(1, len(nums)):
            submax[i] = max(submax[i - 1] * nums[i], submin[i - 1] * nums[i], nums[i])
            submin[i] = min(submax[i - 1] * nums[i], submin[i - 1] * nums[i], nums[i])
            maxv = max(submax[i], submin[i], maxv)
        
        return maxv