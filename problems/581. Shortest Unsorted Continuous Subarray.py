from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        return self.method1(nums)
        #return self.method2(nums)
    
    def method1(self, nums):
        """
        Two pointers
        Time: O(n)
        Space: O(1)
        """
        ## Iterate from start, find the right most number that is smaller
        ## than the largest number to its left. Update largest number so far in the 
        ## iteration
        maxv = float('-inf')
        right = 0
        for i in range(0, len(nums)):
            maxv = max(maxv, nums[i])
            if nums[i] < maxv:
                right = i
        
        ## iterate from end to start, fin the index of the left most number that is 
        ## larget than the smallest number to its right
        minv = float('inf')
        left = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            minv = min(minv, nums[i])
            if nums[i] > minv:
                left = i
                
        if right < left:
            return 0
        return right - left + 1
    
    def method2(self, nums):
        """
        Monotonic stack
        Time: O(n)
        Space:O(n)
        """
        
        ## monotonic stack left to right
        n = len(nums)
        stack = []
        left = n
        stack.append((nums[0], 0))
        for i in range(1, n):
            if not stack or nums[i] > stack[-1][0]:
                stack.append((nums[i], i))
            else:
                while stack and nums[i] < stack[-1][0]:
                    val, index = stack.pop()
                    left = min(left, index)
  
        ## monotonic stack right to left
        right = 0
        stack = []

        stack.append((nums[-1], n - 1))
        for i in range(n - 2, -1, -1):
            if not stack or nums[i] < stack[-1][0]:
                stack.append((nums[i], i))
            else:
                while stack and nums[i] > stack[-1][0]:
                    val, index = stack.pop()
                    right = max(right, index)

        if left > right:
            return 0
        return right - left + 1
        
        
