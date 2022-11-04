
from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        DP
        length[i]: length of longest increasing subsequence ending with nums[i]
        count[i]: count of longest increasing subsequence ending with nums[i]
        Time: O(n^2)
        Space: O(n)
        
        """
        N = len(nums)
        length = [1] * N
        count = [1] * N
        
        for i in range(N):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]
        maxlen = 1
        maxcount = 0
        for i in range(N):
            if maxlen < length[i]:
                maxlen = length[i]
                maxcount = count[i]
            elif maxlen == length[i]:
                maxcount += count[i]
            
        return maxcount
                    
if __name__ == '__main__':
    s = Solution()
    nums = [2,2,2,2,2]
    rst = s.findNumberOfLIS(nums)
    print(rst)