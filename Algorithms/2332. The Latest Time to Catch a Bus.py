from typing import List
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        """
        Two pointers
        """
        buses.sort()
        passengers.sort()
        rst = 0
        
        p = 0
        for b in range(len(buses)):
            cap = capacity
            ## for every passenger that can go into a bus, check whether we can board
            ## before this person
            while p < len(passengers) and cap > 0 and passengers[p] <= buses[b]:
                ## if there is a spot before passengers[p], take it
                if p == 0 or (p >= 1 and passengers[p] - 1 != passengers[p - 1]):
                    rst = max(rst, passengers[p] - 1)
                cap -= 1
                p += 1
            
            ## if the bus is not full and there is no person arrives at the leaving time, update
            if p == 0 or (cap > 0 and p >=1 and passengers[p-1] != buses[b]):
                rst = max(rst, buses[b])
        
        return rst
        