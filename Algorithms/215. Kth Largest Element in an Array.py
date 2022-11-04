# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:12:08 2020

@author: wyue
"""

import heapq
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return self.method1(nums, k)
        return self.method2(nums, k) 
        #return self.method3(nums, k) 
        
    def method1(self, nums, k):
        """
        Heap.
        time: O(nlogk)
        space: O(k)
        """
        hq = []
        for i in range(k):
            hq.append(nums[i])
        heapq.heapify(hq)
        for i in range(k, len(nums)):
            if nums[i] > hq[0]:
                heapq.heappop(hq)
                heapq.heappush(hq, nums[i])
        return hq[0]
    
    def method2(self, nums, k):
        """
        Three pointers (quick select)
        time: O(n) on average
        Space: O(1)
        """
        return self.recursion(nums, 0, len(nums)-1, k)
    
    def recursion(self, nums, start, end, k):
        ## base case
        """
        S S S S E E X X X X L L L L
                ^   ^     ^          
              left mid   right

        S is element smaller than pivot, L is element larger than pivot. X are element not explored yet.

        left, mid start from 0
        right start from n - 1
        increase mid until mid > right

        the final state is:
        S S S S E E E E E E L L L L
                ^         ^          
              left       right
        [0, left - 1] are smaller than pivot
        [left, right] are equal to the pivot
        [right + 1, end] are larger than the pivot.
        """
        if start == end:
            return nums[start]
        left = start
        mid = start
        right = end
        pivot = nums[left]
        while mid <= right:
            if nums[mid] == pivot:
                mid += 1
            elif nums[mid] < pivot:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            else:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
        
        if end - (right + 1) + 1 >= k:
            return self.recursion(nums, right + 1, end, k)
        elif end - left + 1 >= k:
            return nums[left]
        else:
            remain = k - (end - left + 1)
            return self.recursion(nums, start, left - 1, remain)
        
        
    def method3(self, nums, k):
        """
        Binary search.
        Time: O(n)*log(C)
        Space: O(1)
        """
        left = min(nums) # float('-inf')
        right = max(nums) # float('inf')
        
        while left < right:
            mid = left + (right - left + 1) // 2
            count = self.count_not_less_than(nums, mid)
            if count >= k:
                left = mid
            else:
                right = mid - 1
        
        return left
        
    def count_not_less_than(self, nums, v):
        count = 0
        for n in nums:
            count += n >= v
        
        return count

if __name__ == '__main__':
    s = Solution()

    nums = [3,2,1, 5, 6, 4]
    k = 2
    rst = s.findKthLargest(nums, k)
    print(rst)