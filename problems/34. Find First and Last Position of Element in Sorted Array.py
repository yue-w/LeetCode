from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #return self.method1(nums, target)
        return self.method2(nums, target) # preferred method

    def method1(self, nums, target):
        """
        Implement binary search
        """
        rst = [-1, -1]
        if not nums:
            return rst
        
        low = 0
        up = len(nums) - 1
        
        ## find start: find the first element that is not smaller than target.
        while low < up:
            mid = low + (up - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                up = mid
            
        if nums[low] == target:  
            rst[0] = low
        
        ## find end: find the last element that is not larger than target.
        low = 0
        up = len(nums) - 1
        while low < up:
            mid = low + (up - low + 1) // 2
            if nums[mid] > target:
                up = mid - 1
            else:
                low = mid   
            
        if nums[low] == target:  
            rst[1] = low
        
        return rst
    
    def method2(self, nums, target):
        """
        call bisect functions
        """
        if not nums:
            return [-1, -1]
        left = bisect.bisect_left(nums, target)
        if left == len(nums):
            return [-1, -1]
        elif nums[left] != target:
            return [-1, -1]
        
        right = bisect.bisect_right(nums, target) - 1

        return [left, right]