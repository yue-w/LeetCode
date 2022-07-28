

from collections import defaultdict
from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        return self.method3(nums, k) ## method 2 and 3 are preferred. Method 2 two passes, method 3 one pass.
    
    def method1(self, nums, k):
        """
        Two pointers
        Time: O(nlogn)
        Space: O(1)
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        rst = 0
        while left < right:
            currsum = nums[left] + nums[right]
            if currsum == k:
                rst += 1
                left += 1
                right -= 1
            elif currsum < k:
                left += 1
            else:
                right -= 1
        
        return rst
    
    def method2(self, nums, k):
        """
        Hash, two passes
        Time: O(n)
        Space: O(n)
        """
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        rst = 0
        for n in nums:
            need = k - n
            if need == n:
                rst += counter[need] // 2
                counter[n] = 0
            else:
                rst += min(counter[need], counter[n])
                counter[n] = 0
            
        return rst
    
    def method3(self, nums, k):
        """
        Hash, one pass
        Time: O(n)
        Space: O(n)
        """
        counter = defaultdict(int)
        rst = 0
        
        for i in range(len(nums)):
            num = nums[i]
            need = k - num
            if counter[need] > 0:
                counter[need] -= 1
                rst += 1
            else:
                counter[num] += 1
                
        return rst 
            