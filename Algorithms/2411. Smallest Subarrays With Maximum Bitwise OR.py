from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        
        maxb = 0
        lst1 = [-1] * 32
        n = len(nums)
        rst = [1] * len(nums)
    
        for i in range(n-1, -1, -1):
            maxb = maxb | nums[i]
            
            
            for j in range(32):
                v = 1 << j
                if (v & nums[i]) != 0:
                    lst1[j] = i
            

            tem = nums[i]
            for j in range(32):
                if lst1[j] != -1:
                    tem = tem | (1 << j)
                    rst[i] = max(rst[i], lst1[j] - i + 1)
                if tem == maxb:
                    break
            
        return rst