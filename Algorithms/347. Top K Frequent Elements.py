from collections import defaultdict
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.method1(nums, k) ## preferred method. QuickSelect.
    
    def method1(self, nums, k):
        """
        Quick select (three pointers).
        Time: O(n)
        Space: O(1)
        S: Smaller, E: Equal, U: Unknown, L: larger
        S S S S E E E E E U U U U U U U L L L L L L L
                |         |           |
               left      curr       right
        when returned from the recursion, the final state
        S S S S E E E E E E E E E E E E L L L L L L L
                |                     |
               left                 right (curr)
        """
        def quick_select(array, k, low, high):
            ## Return the kth largest elements in array (recursivly)
            ## Base case. Only one number left, it is the answer
            if low == high:
                return array[low]
            
            ## pivot. Here, we use the middle point as the pivot.
            pivot = array[low + (high - low) // 2]
            left = low
            curr = low
            right = high
            while curr <= right:
                if array[curr] < pivot:
                    array[left], array[curr] = array[curr], array[left]
                    left += 1
                    curr += 1
                elif array[curr] == pivot:
                    curr += 1
                else: ## array[curr] > pivot:
                    array[curr], array[right] = array[right], array[curr]
                    right -= 1
            ## now curr = right
            count_larger = high - right 
            if count_larger >= k:
                return quick_select(array, k, right + 1, high)
             
            else:
                count_not_smaller = high - left + 1
                if count_not_smaller >= k:
                    return pivot
                else: 
                    remain = k - count_not_smaller
                    return quick_select(array, remain, low, left - 1)
  
            
        from collections import defaultdict
        ## get the frequency of each word
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        freq_lst = []
        for key, val in freq.items():
            freq_lst.append(val)
        
        rst = []
        ## the threshold of frequency
        thre = quick_select(freq_lst, k, 0, len(freq_lst)-1)
        ## we need to find all values that occured not less than thre times,
        ## so we need to iteratate the dictionary again to find them all.
        for key, val in freq.items():
            if val >= thre:
                rst.append(key)
        
        return rst
        
    def method2(self, nums, k):
        """
        Binary search
        Time: O(nlogC)
        Space: O(1)
        """
        
    def method3(self, nums, k):
        """
        Heap.
        Time: O(nlogk)
        Space: O(k)
        """
        
    def method4(self, nums, k):
        """
        Bucket sort.
        Time: O(n)
        Space: O(n)
        """
        ## worst case of storate is when every element is different.
        ## each elements of the array is the count of
        ## occurance of the frequency.
        ## e.g. if nums = [1,1,1,2,2,3] then freq = [[3], [2], [1],[], [], []]
        ## one number (3) occurred once, two numbers (2) occurred twice,
        ## and one number (1) occurred 3 times. Zero number of numbers occurred more
        ## than 3 times.
        bucket = [[] for _ in range(len(nums) + 1)]
        
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        for v, count in freq.items():
            bucket[count].append(v)
        rst = []
        for vs in bucket[::-1]:
            if not vs:
                continue
            for v in vs:
                rst.append(v)
            if len(rst) == k:
                return rst

if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
    k = 10
    rst = Solution().topKFrequent(nums, k)
    print(rst)

