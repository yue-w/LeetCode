
from typing import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Two pointers
        """
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                i += 1
            else:
                j = i
                while j < len(nums) and nums[j] == 0:
                    count += j - i + 1
                    j += 1
                i = j
                
        return count