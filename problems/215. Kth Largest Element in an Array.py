# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:12:08 2020

@author: wyue
"""

# import heapq
# import random
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         ## Method 1: sort the array and return the kth element
#         ## Time complexity: n logn
#         # nums.sort()
#         # return nums[-k]
        
#         ## Method 2: Use heap. complexity N log k
#         ## Keep the largest k element. Use pythn nlargest function
#         # return heapq.nlargest(k, nums)[-1]    
        
#         # ## Method 3: Similar to method 2, implement by hand
#         # klargest = []
#         # heapq.heapify(klargest)
#         # for i in range(k):
#         #     heapq.heappush(klargest, nums[i])
        
#         # for i in range(k, len(nums)):
#         #     if nums[i] > klargest[0]:
#         #         heapq.heapreplace(klargest, nums[i])
        
#         # return klargest[0] ## The smallest element is always the root, heap[0].
    
#         ## Method 4: Quick Select:
#         def partition(left, right, pivot_index):
#             pivot = nums[pivot_index]
#             # 1. move pivot to end
#             nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
#             # 2. move all smaller elements to the left
#             store_index = left
#             for i in range(left, right):
#                 if nums[i] < pivot:
#                     nums[store_index], nums[i] = nums[i], nums[store_index]
#                     store_index += 1

#             # 3. move pivot to its final place
#             nums[right], nums[store_index] = nums[store_index], nums[right]  
            
#             return store_index
        
#         def select(left, right, k_smallest):
#             """
#             Returns the k-th smallest element of list within left..right
#             """
#             if left == right:       # If the list contains only one element,
#                 return nums[left]   # return that element
            
#             # select a random pivot_index between 
#             pivot_index = random.randint(left, right)     
                            
#             # find the pivot position in a sorted list   
#             pivot_index = partition(left, right, pivot_index)
            
#             # the pivot is in its final sorted position
#             if k_smallest == pivot_index:
#                  return nums[k_smallest]
#             # go left
#             elif k_smallest < pivot_index:
#                 return select(left, pivot_index - 1, k_smallest)
#             # go right
#             else:
#                 return select(pivot_index + 1, right, k_smallest)

#         # kth largest is (n - k)th smallest 
#         return select(0, len(nums) - 1, len(nums) - k)

# nums = [3,2,1,5,6,4]
# k = 2

# print(Solution().findKthLargest(nums,k))

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
        Three pointers
        time: O(n) on average
        Space: O(1)
        """
        return self.recursion(nums, 0, len(nums)-1, k)
    
    def recursion(self, nums, start, end, k):
        ## base case
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