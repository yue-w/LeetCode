
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Sliding window
        max possible bitwise AND is max(nums)
        """
        maxv = max(nums)
        maxlen = 1
        n = len(nums)
        curr = 1
        #for i in range(n):
        i = 0
        while i < n:
            j = i + 1
            curr = nums[i]
            while (j < n) and ((curr & nums[j]) == maxv):
                j += 1
            maxlen = max(maxlen, j - i)
            i = j
        
        return maxlen