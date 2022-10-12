from typing import List
import heapq
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        return self.method2(milestones) ## preferred method.
    
    def method1(self, milestones):
        """
        Heap. 
        Time:
        Space:
        TLE
        """
        ## items in hq is (-count, index)
        hq = []
        for i in range(len(milestones)):
            hq.append((-milestones[i], i))
        
        heapq.heapify(hq)
        rst = 0
        
        while hq:
            ## if only 1 project left. we can work on one more
            if len(hq) == 1:
                rst += 1
                return rst
            else: ## if more than two projects
                count1, p1 = heapq.heappop(hq)
                count2, p2 = heapq.heappop(hq)
                rst += 2
                count1 += 1
                if count1 < 0:
                    heapq.heappush(hq, (count1, p1))
                count2 += 1
                if count2 < 0:
                    heapq.heappush(hq, (count2, p2))
        return rst
    
    def method2(self, milestones):
        """
        Greedy
        Reference: https://www.youtube.com/watch?v=0ut2kGnSXLU
        """
        total = sum(milestones)
        maxv = max(milestones)
        if maxv <= total // 2:
            return total
        remain = total - maxv
        return remain * 2 + 1
        
            
        
                
        
        
        
        