from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #return self.method1(nums)
        return self.method2(nums)
        
    def method1(self, nums):
        """
        Quicksort
        
        S S S S S S S E E E E E E U U U U U U U U L L L L L L L
                      |           |             |
                     left        curr          right

        S S S S S S S E E E E E E E E E E E E E E L L L L L L L
                      |                         |
                     left                      right
        """
        
        def quick_sort(nums, start, end):
            ## base case:
            if start >= end:
                return 
            ## select pivot and swap. Choose mid for now
            mid = start + (end - start) // 2
            nums[start], nums[mid] = nums[mid], nums[start]
            pivot = nums[start]
            left = curr = start
            right = end
            while curr <= right:
                if nums[curr] == pivot:
                    curr += 1
                elif nums[curr] < pivot:
                    nums[left], nums[curr] = nums[curr], nums[left]
                    curr += 1
                    left += 1
                else:
                    nums[curr], nums[right] = nums[right], nums[curr]
                    right -= 1
                
            ## sort left part
            quick_sort(nums, start, left - 1)
            ## sort right part
            quick_sort(nums, right + 1, end)
            
        quick_sort(nums, 0, len(nums)-1)
        return nums
    
    def method2(self, nums):
        """
        Merge sort
        """
        
        def merge_sort(array):
            ## base case 1: 
            if len(array) == 1:
                return array
            
            ## base case 2:
            if len(array) == 2:
                minv = min(array[0], array[1])
                maxv = max(array[0], array[1])
                return [minv, maxv]
            n = len(array)
            mid = (n  - 1) // 2
            array1 =  merge_sort(array[:mid+1])
            array2 = merge_sort(array[mid+1:])

            sorted_array = combine(array1, array2)
            return sorted_array
        
        def combine(array1, array2):
            """
            combine array1 and array2 in sorted order.
            both array1 and array2 are in sorted order 
            """
            array = [0 for _ in range(len(array1) + len(array2))]
            i = j = k = 0
            while i < len(array1) and j < len(array2):
                if array1[i] <= array2[j]:
                    array[k] = array1[i]
                    i += 1
                else:
                    array[k] = array2[j]
                    j += 1
                k += 1
            
            while i < len(array1):
                array[k] = array1[i]
                i += 1
                k += 1
            while j < len(array2):
                array[k] = array2[j]
                j += 1
                k += 1
            
            return array
        
        return merge_sort(nums)