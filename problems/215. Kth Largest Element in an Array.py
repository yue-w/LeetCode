# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:12:08 2020

@author: wyue
"""

import heapq
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ## Method 1: sort the array and return the kth element
        ## Time complexity: n logn
        # nums.sort()
        # return nums[-k]
        
        ## Method 2: Use heap. complexity N log k
        ## Keep the largest k element. Use pythn nlargest function
        # return heapq.nlargest(k, nums)[-1]    
        
        # ## Method 3: Similar to method 2, implement by hand
        # klargest = []
        # heapq.heapify(klargest)
        # for i in range(k):
        #     heapq.heappush(klargest, nums[i])
        
        # for i in range(k, len(nums)):
        #     if nums[i] > klargest[0]:
        #         heapq.heapreplace(klargest, nums[i])
        
        # return klargest[0] ## The smallest element is always the root, heap[0].
    
        ## Method 4: Quick Select:
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)

nums = [3,2,1,5,6,4]
k = 2

print(Solution().findKthLargest(nums,k))