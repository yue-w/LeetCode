from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        for a number num in nums, if num-1 is not in nums, then num is the 
        lower bound of a continuous sequence, we check its upper bound.
        But if num - 1 is not in nums, then num is not a lower bound, we do
        not check it.
        """
        nums_set = set(nums)
        rst = 0
        for num in nums:
            ## if num - 1 in nums_set, ignore
            if num - 1 in nums_set:
                continue
            ## if num - 1 not in nums_set, num is the lower bound of a continuous
            ## sequence. We count how long it is, update rst.
            curr = 1
            while num + 1 in nums_set:
                curr += 1
                num += 1
            rst = max(rst, curr)
        
        return rst

if __name__ == '__main__':
    nums = [0,3,7,2,5,8,4,6,0,1]
    rst = Solution().longestConsecutive(nums)
    print(rst)