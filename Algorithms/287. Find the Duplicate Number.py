
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.method1(nums)
    
    def method1(self, nums):
        """
        cycling sort
        Time: O(n)
        Space: O(1) but change nums
        """
        n = len(nums)
        nums = [0] + nums
        i = 1
        for i in range(1, n+1):
            while nums[i] != i and nums[i] <= n and nums[nums[i]] != nums[i]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            
        print(nums)
        for i in range(1, n + 1):
            if i != nums[i]:
                return nums[i]