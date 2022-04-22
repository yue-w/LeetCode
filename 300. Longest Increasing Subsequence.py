# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:54:47 2022

@author: wyue
Leetcode 300
"""
from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return s.lengthOfLIS_nlogn(nums)
    
    ## O(nlogn)
    def lengthOfLIS_nlogn(self, nums: List[int]) -> int:
         dp = []
         for x in nums:
             """
             Return the index of the smallest number in array that is larger than val
             array is sorted from smallest to largest, use binary search.
             if not found, return len(array)
             """
             index = bisect_left(dp, x)
             if index == len(dp):
                 dp.append(x)
             else:
                dp[index] = x
         return len(dp)
        

    
    ## O(n^2)   
    def lengthOfLIS_n2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        cache = [1] * n
        
        for i in range(n-1, -1, -1):
            max_v = 0
            j = i + 1
            while j <= n - 1:
                if nums[i] < nums[j]:
                    max_v = max(max_v, cache[j])
                    j += 1 
                else:
                    j += 1
            cache[i] = max_v + 1
                        
        return max(cache)
    
if __name__ == '__main__':
    s = Solution()
    nums = [0,1,0,3,2,3]
    rst = s.lengthOfLIS_n2(nums)
    print(rst)