
from typing import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Two pointers
        """
        count = 0
        j = 0
        while j < len(nums):
            i = j
            while j < len(nums) and nums[j] == 0:
                count += j - i + 1
                j += 1
            j += 1
        return count