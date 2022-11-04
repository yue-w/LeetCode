from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        nums = list(set(nums))
        if 0 in nums:
            return len(nums) - 1
        return len(nums)
                
        