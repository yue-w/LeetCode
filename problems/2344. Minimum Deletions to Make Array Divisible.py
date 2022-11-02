from typing import List

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        numsDivide = set(numsDivide)
        rst = 0
        while rst < len(nums):
            i = 0
            for s in numsDivide:
                if s % nums[rst] == 0:
                    i += 1
                else:
                    rst += 1
                    break

            if i == len(numsDivide):
                return rst
        
        return -1