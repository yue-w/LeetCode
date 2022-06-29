from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        rst = 0
        for n in nums:
            rst ^= n
            
        return rst