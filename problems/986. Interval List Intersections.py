
from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #return self.method1(firstList, secondList)
        return self.method2(firstList, secondList) ## preferred method
        
    def method1(self, firstList, secondList):
        """
        Sweeping line, heap
        Time: O((m+n)log(m+n))
        Space: O(m+n)
        """
        import heapq
        hq = []
        # head: -1, end: + 1. From -2 to -1, interval
        for start, end in firstList:
            hq.append((start, -1))
            hq.append((end, 1))
            
        for start, end in secondList:
            hq.append((start, -1))
            hq.append((end, 1))
            
        heapq.heapify(hq)
        counter = 0
        rst = []
        while hq:
            time, v = heapq.heappop(hq)
            ## starting point:
            if counter == -1 and counter + v == -2: 
                start = time
            elif counter == -2 and counter + v == -1:
                end = time
                rst.append([start, end])
            counter += v
            

        return rst
            
            
    def method2(self, firstList, secondList):
        """
        Two pointers
        Time: O(m + n)
        Space: O(1)
        """
        i = 0
        j = 0
        rst = []
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0]) 
            end =  min(firstList[i][1], secondList[j][1])
            if start <= end:
                rst.append([start, end])
            
            ## shift the pointer (move the smaller one)
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return rst
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        