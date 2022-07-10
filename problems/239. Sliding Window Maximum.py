
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Time: O(n)
        Space: O(k)
        """
        dq = deque() ## monotonic decreasing q (stores index in nums)
        rst = []
        for i in range(len(nums)):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            
            ## if more than k elements, pop the leftmost one
            left = dq[0]
            right = i
            if right - left >= k:
                dq.popleft()
            
            ## add the number to rst starting from index k - 1
            if i >= k - 1:
                rst.append(nums[dq[0]])
        
        return rst

if __name__ == '__main__':
    nums = [9,10,9,-7,-4,-8,2,-6]
    k = 5
    rst = Solution().maxSlidingWindow(nums, k)
    print(rst)