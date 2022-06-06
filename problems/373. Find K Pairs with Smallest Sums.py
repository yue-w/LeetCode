

import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return self.method1(nums1, nums2, k)
        
    def method1(self, nums1, nums2, k):
        """
        Binary search
        Time: O(log(n1 * n2)) + O(n1 + n2) = o(log(n1 * n2))
        """
        left = nums1[0] + nums2[0]
        right = nums1[-1] + nums2[-1]
        
        while left < right:
            mid = left + (right - left) // 2
            ct_not_larger = self.count_not_larger(nums1, nums2, mid)
            if ct_not_larger < k:
                left = mid + 1
            else:
                right = mid
        
        sum_up_bnd = left
        
        """
        the k's smallest sum equals to sum_up_bnd, iterate all possible sums, if
        the sum is less than sum_up_bnd, put it in rst1, else, put it in rst2.
        We may need to add some elements to rst1 from rst2.
        """
        rst1 = []
        rst2 = []
        for i in range(len(nums1)):
            j = 0
            while j < len(nums2) and nums1[i] + nums2[j] <= sum_up_bnd:
                if nums1[i] + nums2[j]  < sum_up_bnd:
                    rst1.append([nums1[i], nums2[j] ])
                else:
                    rst2.append([nums1[i], nums2[j] ])
                j += 1
        idx = 0
        while idx < len(rst2) and len(rst1) < k:
            rst1.append(rst2[idx])
            idx += 1
        return rst1
    
    def count_not_larger(self, nums1, nums2, mid):
        j = len(nums2) - 1
        count = 0
        for i in range(len(nums1)):
            while j >= 0 and nums1[i] + nums2[j] > mid:
                j -= 1
            count += j + 1
                
        return count


if __name__ == '__main__':
    s = Solution()
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    rst = s.kSmallestPairs(nums1, nums2, k)
    print(rst)
        
        
        
                
        
                