from typing import List
from collections import  defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most(nums, k) - self.at_most(nums, k - 1)
    
    def at_most(self, nums, k):
        """
        Return number of subarray that has at most k different integers
        """
        count = 0
        i = 0
        dic = defaultdict(int)
        for j in range(len(nums)):
            dic[nums[j]] += 1
            while len(dic) > k:
                dic[nums[i]] -= 1
                if dic[nums[i]] == 0:
                    del dic[nums[i]]
                i += 1
                
            count += j - i + 1
        return count
                
            