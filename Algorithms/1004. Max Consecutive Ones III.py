
from typing import List 

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        rst = 0
        left = 0
        remain = k
        for right in range(len(nums)):
            if nums[right]:
                rst = max(rst, right - left + 1)
            else:
                remain -= 1
                while remain < 0:
                    if nums[left] == 0:
                        remain += 1
                    left += 1
                rst = max(rst, right - left + 1)
        return rst

if __name__ == '__main__':
    s = Solution()
    nums = [1, 0, 1]
    k = 0
    rst = s.longestOnes(nums, k)
    print(rst)
        
        
        