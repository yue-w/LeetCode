from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        n = len(nums1)
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]

        ## this step is important, if there is enough k
        ## to reduce everything to 0, do not over reduce
        if sum(diffs) <= k:
            return 0
        
        diffs.sort(reverse=True)
        
        remain = k
        i = 0
        while i < len(diffs) - 1 and remain - (i + 1) * (diffs[i] - diffs[i + 1]) > 0: 
            remain -= (i + 1) * (diffs[i] - diffs[i + 1])
            i += 1
        dh = remain // (i + 1)
        extra = remain % (i + 1)
        rst = ((diffs[i] - dh - 1) ** 2) * extra + ((diffs[i] - dh) ** 2) * (i + 1 - extra)
        
        for index in range(i+1, len(diffs)):
            rst += diffs[index] ** 2
        
        return rst

if __name__ == '__main__':
    nums1 = [1,2,3,4]
    nums2 = [2,10,20,19]
    k1 = 0
    k2 = 0
    rst = Solution().minSumSquareDiff(nums1, nums2, k1, k2)