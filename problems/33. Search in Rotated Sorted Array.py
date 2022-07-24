# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:29:30 2022

@author: wyue
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #return self.method1(nums, target)
        return self.method2(nums, target) ## preferred method
        
    def method1(self, nums, target):
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
        if len(nums) == 1:
            return 0
        if nums[left] < nums[right - 1]:
            return right - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid + 1 < len(nums):
                if nums[mid] > nums[mid + 1]:
                    return mid
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
    
    def method2(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            ## If on the same side
            if (nums[mid] >= nums[0]) == (target >= nums[0]):
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            ## on different side
            else:
                if target >= nums[0]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        if (left == right) and (nums[left] == target):
            return left
        return -1
    
if __name__ == '__main__':
    s = Solution()
    nums = [4,5,6,7,8,9,0,1,2]
    target = 1
    rst = s.search(nums, target)
    print(rst)
    
