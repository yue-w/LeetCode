from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0
        seen = {}# key: nums[i], value: i
        rst = 0
        cur_sum = 0
        for i, n in enumerate(nums):
            if n in seen: # remove the numbers before i
                idx = seen[n]
                seen = {}
                cur_sum = 0
                for j in range(idx+1, i + 1):
                    seen[nums[j]] = j
                    cur_sum += nums[j]

            else:
                seen[n] = i
                cur_sum += n
                if len(seen) == k:
                    rst = max(rst, cur_sum)
                elif len(seen) > k:
                    cur_sum -= nums[i - k]
                    rst = max(rst, cur_sum)
                    del seen[nums[i - k]]
                #print(i, rst)

        return rst