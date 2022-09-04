from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # two pointers
        rst = 1
        i = 0
        j = 1
        curr = nums[0]
        while j < len(nums):
            while j < len(nums) and curr & nums[j] == 0:
                curr = (curr | nums[j]) 
                j += 1
                rst = max(rst, j - i)
            curr = self.subtract(curr, nums[i])
            i += 1
        
        return rst
        
        
    def subtract(self, curr, pre):
        rst = curr
        ptr = 1
        while curr and pre:

            cu = curr % 2
            pr = pre % 2
            curr = curr//2
            pre = pre//2
            if pr == 1 and cu == 1:
                rst -= ptr
            ptr = ptr << 1

        return rst

        
        