
import heapq
from typing import List
class KthLargest:

    """
    Solution if delete elements smaller than kth largest
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_largest = nums[:k]
        ## linear time heapify
        heapq.heapify(self.k_largest)
        for n in nums[k:]:
            if n > self.k_largest[0]:
                heapq.heappop(self.k_largest)
                heapq.heappush(self.k_largest, n)

    def add(self, val: int) -> int:
        if len(self.k_largest) < self.k:
            heapq.heappush(self.k_largest, val)
            return self.k_largest[0]
        else:
            if val < self.k_largest[0]:
                return self.k_largest[0]
            else:
                heapq.heappop(self.k_largest)
                heapq.heappush(self.k_largest, val)
                return self.klargest[0]
        

    """
    Solution if need to keep all added element
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.smaller = []
        if not nums:
            self.klargest = []
        else:
            if len(nums) < k:
                self.klargest = nums[:]
            else:
                self.klargest = nums[0:k]
            heapq.heapify(self.klargest)
        for ele in nums[k:]:
            if ele <= self.klargest[0]:
                self.smaller.append(ele)
            else:
                tem = heapq.heappop(self.klargest)
                heapq.heappush(self.klargest, ele)
                self.smaller.append(tem)


    def add(self, val: int) -> int:
        if len(self.klargest) < self.k:
            heapq.heappush(self.klargest, val)
            return self.klargest[0]
        if val <= self.klargest[0]:
            self.smaller.append(val)
            return self.klargest[0]
        else:
            tem = heapq.heappop(self.klargest)
            heapq.heappush(self.klargest, val)
            self.smaller.append(tem)
            return self.klargest[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)