from typing import List

class Solution:
    """
    Two pointers. Bit.
    Reference: https://youtu.be/stXRx71prEE
    """
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        j = 0
        rst = 0
        state = 0
        n = len(nums)
        for i in range(n):
            while j < n and ((state & nums[j] == 0)):
                state += nums[j]
                j += 1
            rst = max(rst, j - i)
            state -= nums[i]
        return rst

        
        