from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32
        
        for n in nums:
            for i in range(len(bits)):
                bits[i] += (n >> i) & 1
        
        rst = 0
        for i in range(len(bits)):
            rst += (bits[i] % 3) << i
        
        """
        overflow cases in python: maximum value for int32 is 2^31 - 1, 
        so if we get number larger than this value we have negative answer in fact.
        """
        if rst < (1<<31):
            return rst
        else: 
            return rst - (1<<32)   