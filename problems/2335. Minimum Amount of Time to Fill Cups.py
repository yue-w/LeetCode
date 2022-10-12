from typing import List
import heapq

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        #return self.method1(amount) ## use heap
        return self.method2(amount) ## preferred method: arrangement
        
    def method1(self, amount):
        """
        heap
        """

        rst =  0
        
        hq = []
        for a in amount:
            if a == 0:
                continue
            heapq.heappush(hq,-a)
        
        while hq:
            c1 = heapq.heappop(hq)
            c1 += 1
            rst += 1
            if hq:
                c2 = heapq.heappop(hq)
                c2 += 1
                if c2 < 0:
                    heapq.heappush(hq, c2)
            if c1 < 0:
                heapq.heappush(hq, c1)


        return rst
    
    def method2(self, amount):
        """
        Arrangement. 
        Reference: https://youtu.be/cuZBEzojuOw
        """
        total = sum(amount)
        maxv = max(amount)
        if maxv >= (total + 1) // 2:
            return maxv
        else:
            return (total + 1) // 2