from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        This problem requires no extra memory, so we implement our own quick_sort without 
        calling the built in sort() function. 
        """
        ## corner case
        if len(nums) <= 1:
            return 
        ## right to left, find the first index that decreases
        i = len(nums) - 1
        while i >= 1 and nums[i - 1] >= nums[i]:
            i -= 1
        
        ## at this point, i = 0 or nums[i - 1] < nums[i]
        if i == 0:
            self.quick_sort(nums, 0, len(nums) - 1)
        else:
            i -= 1
            ## from riht to left find first number that is larger than nums[i]
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            ## swap
            nums[i], nums[j] = nums[j], nums[i]
            self.quick_sort(nums, i + 1, len(nums) - 1)
            
    def quick_sort(self, nums, start, end):
        """
        Sort array nums from start to end (inclusive) inplace.
        S S S S S E E E E E U U U U U U U U U L L L L
                  |         |               |
                 left       cur           right
        """
        ## base case
        if start >= end:
            return
        pivot = nums[start]
        left = start
        cur = start
        right = end
        while cur <= right:
            if nums[cur] == pivot:
                cur += 1
            elif nums[cur] > pivot:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            else: # nums[cur] < pivot
                nums[left], nums[cur] = nums[cur], nums[left]
                cur += 1
                left += 1
        ## recursion
        self.quick_sort(nums, start, left - 1)
        self.quick_sort(nums, right + 1, end)
                

            
if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1]
    s.nextPermutation(nums)
    print(nums)
        
        
        