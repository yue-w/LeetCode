import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.hq = [i for i in range(1, 1002)]
        #print(self.hq)
        self.set = set(self.hq)
        heapq.heapify(self.hq)


    def popSmallest(self) -> int:
        v = heapq.heappop(self.hq)
        self.set.remove(v)
        return v
        
        

    def addBack(self, num: int) -> None:
        if num in self.set:
            return
        self.set.add(num)
        heapq.heappush(self.hq, num)
        
        
"""
Method 2: use sortedcontainers

from sortedcontainers import SortedSet 
class SmallestInfiniteSet:

    def __init__(self):
        self.ss = SortedSet([i for i in range(1, 1002)])

    def popSmallest(self) -> int:
        v = self.ss[0]
        del self.ss[0]
        return v

    def addBack(self, num: int) -> None:
        self.ss.add(num)
"""

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)