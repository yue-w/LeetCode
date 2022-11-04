
import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_largest = nums[:k]
        ## linear time heapify
        heapq.heapify(self.k_largest)
        for n in nums[k:]:
            if n > self.k_largest[0]:
                # heapq.heappop(self.k_largest)
                # heapq.heappush(self.k_largest, n)
                ## use heappushpop is more efficient than heappush followed by a heappop as above                
                heapq.heappushpop(self.k_largest, n)
                

    def add(self, val: int) -> int:
        if len(self.k_largest) < self.k:
            heapq.heappush(self.k_largest, val)
            return self.k_largest[0]
        else:
            if val < self.k_largest[0]:
                return self.k_largest[0]
            else:
                # heapq.heappop(self.k_largest)
                # heapq.heappush(self.k_largest, val)
                ## use heappushpop is more efficient than heappush followed by a heappop as above
                heapq.heappushpop(self.k_largest, val)
                return self.k_largest[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)