# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:54:47 2022

@author: wyue
Leetcode 300
"""
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.method1(nums) ## preferred method
        #return self.method2(nums)
    
    def method1(self, nums):
        """
        Preferred method for solving Longest Increasing Subsequence (LIS) problem.
        Time: O(nlogn)
        Space: O(n)
        Reference: https://youtu.be/Q6KyDl_xiIg
        """
        ## maintain an increasing array.
        increase = []
        for x in nums:
            index = bisect_left(increase, x)
            if index == len(increase):
                increase.append(x)
            else:
                increase[index] = x
                
        return len(increase)
            
        
    
    def method2(self, nums):
        """
        DP:
        dp[i]: the LIS that end with nums[i]
        Transaction function: 
        from all j < i find the j that satisfy the following two conditions:
            (1) nums[i] > nums[j]
            (2) have largest dp[j]
        note the j found avove as j'
        then dp[i] = dp[j'] + 1 

                
        Time: O(n^2)
        Space: O(n)
        """
        N = len(nums)
        dp = [1] * N
        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
             
    
if __name__ == '__main__':
    s = Solution()
    nums = [0,1,0,3,2,3]
    rst = s.lengthOfLIS_n2(nums)
    print(rst)