from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #self.method1(nums, k)
        self.method2(nums, k) ## preferred method
    
    def method1(self, nums, k):
        """
        Time: O(n)
        Space: O(n)
        """
        copy = nums[:]
        
        for i in range(len(nums)):
            index = (i + k) % len(nums)
            nums[index] = copy[i]
            
    def method2(self, nums, k):
        """
        Time: O(n)
        Space: O(1)
        nums = [1 2 3 4 | 5 6 7], rst = [5 6 7 | 1 2 3 4]
        reverse: [7 6 5 | 4 3 2 1]
        """
        ## if k is larger than len(nums), the extra rotation is useless
        k = k % len(nums)
        
        ## reverse nums with constant extra space
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        ## swap the left and right part again for the first half
        left = 0
        right = k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        ## swap the left and right part again for the second half
        left = k
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
    