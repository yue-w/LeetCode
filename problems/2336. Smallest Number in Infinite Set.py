
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
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)