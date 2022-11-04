from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Solution 1:
        Time: O(n)
        Space: O(1)
        """
        rst = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            rst[i] = prefix 
            prefix *= nums[i]
        subfix = 1
        for i in range(len(nums) - 1, -1, -1):
            rst[i] *= subfix 
            subfix *= nums[i] 
        return rst

        """
        Solution 2: 
        Time: O(n)
        Space: O(n)
        """
        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        suffix = [1] * len(nums)
        for i in range(-2, -len(nums) - 1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
            
        rst = [i*j for i, j in zip(prefix, suffix)]
        return rst