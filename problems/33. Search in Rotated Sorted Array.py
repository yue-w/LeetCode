# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:29:30 2022

@author: wyue
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        
        if nums[0] > target:
            return self.bisearch(nums, target, pivot, len(nums)) 
        else:
            return self.bisearch(nums, target, 0, pivot+1)
        
        
    def find_pivot(self,nums):
        # [left, right)
        ## Base case
        left = 0
        right = len(nums)
        ## if there is only one element
        if len(nums) == 1:
            return 0
        ## if there is no pivot point
        if nums[left] < nums[right - 1]:
            return right - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid + 1 < len(nums):
                if nums[mid] > nums[mid + 1]:
                    return mid
            else:
                return mid - 1
            if nums[left] < nums[mid]: 
                left = mid + 1
            else:
                right = mid
        
    
    def bisearch(self, nums, target, left, right):
        """
        Use binary search to find target
        return -1 if not found
        [Left, right)
        """
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid 
            else:
                left = mid + 1
        return -1
    
if __name__ == '__main__':
    s = Solution()
    nums = [1, 3]
    target = 1
    rst = s.search(nums, target)
    print(rst)
    
