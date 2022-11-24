from typing import List
from collections import Counter

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        Sliding window and hashing
        Time: O(n)
        Space: O(k)
        """
        n = len(nums)
        curr = 0
        rst = 0
        counter = Counter()
        # j is right bound, i is left bound (both inclusive) of the sliding window 
        for j in range(n):
            curr += nums[j]
            counter[nums[j]] += 1
            i = j - k + 1
            if i - 1 >= 0:
                counter[nums[i - 1]] -= 1
                curr -= nums[i - 1]
                if counter[nums[i - 1]] == 0:
                    del counter[nums[i - 1]]
            if len(counter) == k:
                rst = max(rst, curr)
        return rst