# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 20:13:00 2022

@author: wyue
"""
from collections import defaultdict
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.two_pointers(nums)
    
    def two_pointers(self, nums: List[int]) -> List[List[int]]:
        
        """
        runtime O(n^2)
        space O(1)
        """
        if len(nums) < 3:
            return []
        rst = []
        ## sort nums
        nums.sort()
        for i in range(len(nums)-2):
            ## Avoid duplication
            if i and nums[i] == nums[i-1]:
                continue 
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < - nums[i]:
                    j += 1
                elif nums[j] + nums[k] > - nums[i]:
                    k -= 1
                else:
                    ## add rst
                    rst.append([nums[i], nums[j], nums[k]])
                    ## Avoid duplicate
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while k > j and nums[k] == nums[k-1]:
                        k -= 1
                    ## update j and k
                    j += 1
                    k -= 1
        return rst
                

    def hash(self, nums: List[int])-> List[List[int]]:
        """
        runtime O(n^2)
        space: O(n)
        """
        if len(nums) < 3:
            return []
        ## Sort nums to make removing duplication easier
        nums.sort()
        rst = []
        counts = defaultdict(int)
        ## Count each number in nums
        for num in nums:
            counts[num] += 1
        ## Iterate
        for i in range(len(nums)-1):
            ## Only count the first occurance to avoid duplication
            if i and nums[i] == nums[i-1]:
                continue 
            for j in range(i+1, len(nums)):
                ## Only count the first occurance to avoid duplication
                if i != j - 1 and nums[j] == nums[j-1]:
                    continue 
                diff = 0 - nums[i] - nums[j]
                ## nums is sorted, if diff < nums[j] continue
                if diff < nums[j]:
                    continue
                ## if diff is not in nums, continue
                if not counts[diff]:
                    continue
                if counts[diff] >= 1 + (diff == nums[i]) + (diff == nums[j]):
                    rst.append([nums[i], nums[j], diff])
                

        return rst

if __name__ == '__main__':
    s = Solution()
    nums = [1,-1,-1,0]
    rst = s.threeSum(nums)
    print(rst)