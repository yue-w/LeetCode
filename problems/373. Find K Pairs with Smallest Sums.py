

import heapq
from typing import List



class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #return self.method1(nums1, nums2, k) ## binary search
        return self.method2(nums1, nums2, k) ## heap.
    
    def method1(self, nums1, nums2, k):
        """
        Binary search
        Time: O(logC) * O(n1 + n2) = O(n1 + n2)
        Reference: https://youtu.be/TsOzIxkzh1E
        """
        def less_or_equal(nums1, nums2, mid):
            """
            Two pointers
            Return the number of pairs have a sum less than or equal to mid
            """
            count = 0
            j = len(nums2) - 1
            for i in range(len(nums1)):
                while j >= 0 and nums1[i] + nums2[j] > mid:
                    j -= 1
                count += j + 1
 
            return count
            
        ## k may be larger than all possible pairs, so we modify kk if necessary   
        kk = min(len(nums1) * len(nums2), k)
        rst = []
        backup = []
        
        low = nums1[0] + nums2[0]
        high = nums1[-1] + nums2[-1]
        
        while low < high:
            mid = low + (high - low) // 2
            if less_or_equal(nums1, nums2, mid) < kk:
                low = mid + 1
            else:
                high = mid
                
        ## at this point, low is the threshold
        for i in range(len(nums1)):
            j = 0
            while j < len(nums2):
                if len(rst) == kk:
                    return rst
                if nums1[i] + nums2[j] < low:
                    rst.append([nums1[i], nums2[j]])
                    j += 1
                elif nums1[i] + nums2[j] == low:
                    backup.append([nums1[i], nums2[j]])
                    j += 1
                else:
                    break
        i = 0
        while len(rst) < kk:
            rst.append(backup[i])
            i += 1
        
        return rst

    def method2(self, nums1, nums2, k):
        """
        Heap.
        Time: O(klogk)
        Reference: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
        discuss/84551/simple-Java-O(KlogK)-solution-with-explanation
        """
        hq = []
        ## k may be larger than all possible pairs, so we modify kk if necessary   
        kk = min(len(nums1) * len(nums2), k)
        i = 0
        ## initialize the heapq, put at most kk elements into it
        while i <= kk and i < len(nums1):
            heapq.heappush(hq, (nums1[i] + nums2[0], i, 0))
            i += 1
        
        rst = []
        while len(rst) < kk:
            sum2, idx1, idx2 = heapq.heappop(hq)
            rst.append([nums1[idx1], nums2[idx2]])
            if idx2 + 1< len(nums2):
                heapq.heappush(hq, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
            
        return rst
                

if __name__ == '__main__':
    s = Solution()
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    rst = s.kSmallestPairs(nums1, nums2, k)
    print(rst)
        
        
        
                
        
                