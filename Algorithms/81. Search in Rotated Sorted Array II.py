
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #return self.method1(nums, target)
        return self.method2(nums, target) ## preferred method
    
    def method1(self, nums, target):
        right = len(nums) - 1
        while right > 1 and nums[0] == nums[right]:
            right -= 1
        
        #### find pivot (the first point that is larger than the point following it)
        left = 0
        
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] >= nums[left]: #and nums[mid] <= nums[right]:
                left = mid
            else:
                right = mid - 1
        
        ## left is the pivot
        pivot = left
        if nums[pivot] == target:
            return True
        if nums[0] <= target:
            return self.binary_search(nums, target, 0, pivot)
        elif pivot + 1 < len(nums):
            return self.binary_search(nums, target, pivot + 1, len(nums) - 1)
        else:
            return False
        
    def binary_search(self, nums, target, start, end):
        left = start
        right = end
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
    
    def method2(self, nums, target):
        while len(nums) > 1 and nums[0] == nums[-1]:
            nums.pop()
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            ## if on the same side
            if (target >= nums[0]) == (nums[mid] >= nums[0]):
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                ## if on different side
                if target >= nums[0]: # then nums[mid] < nums[0]
                    right = mid - 1
                else:
                    left = mid + 1
        
        if nums[left] == target:
            return True
        return False

if __name__ == '__main__':

    s = Solution()
    nums = [1,1,2,1,1,1,1,1]
    #nums = [1,0,1,1,1]
    #nums = [1, 3]
    target = 1
    rst = s.search(nums, target)
    print(rst)


"""
Corner cases:
[1], 1
[1], 0
[1,2], 1
[1, 2], 0
[2, 1], 1
[2, 1], 0
[1,2,3,3,4,5], 3
[1,2,3,3,4,5], 0
[3,4,5, 1,2,3], 3
[3,4,5, 1,2,3], 0
"""        
        

        
        
"""
Step 1: find pivot
Step 2: binary search
"""