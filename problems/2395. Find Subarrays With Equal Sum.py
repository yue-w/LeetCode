from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        for i in range(n - 1):
            tem = nums[i] + nums[i + 1]
            if tem in seen:
                return True
            seen.add(tem)
            
            
        return False