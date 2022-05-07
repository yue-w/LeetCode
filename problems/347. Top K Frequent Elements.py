from collections import defaultdict
from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        """
        Method 1:
        Bucket sort.
        """

        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
            
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for key, count in counter.items():
            bucket[count].append(key)
        
        rst  = []
        for i in range(len(nums) , 0, -1):
            rst += bucket[i]
            if len(rst) == k:
                return rst
        
#         """
#         Method 2:
#         Heap.
#         Use default dictionary and heap.
#         Run: O(nlogn) when k = n
#         Space: O(n)
#         """
#         rst = []
#         counter = defaultdict(int)
#         for n in nums:
#             counter[n] += 1
        
#         heap = []
#         for key, count in counter.items():
#             ## min heap, so add a minus sign
#             heapq.heappush(heap, (-count, key))
        
#         while k > 0 and heap:
#             count, key = heapq.heappop(heap)
#             rst.append(key)
#             k -= 1

            
        
#         return rst