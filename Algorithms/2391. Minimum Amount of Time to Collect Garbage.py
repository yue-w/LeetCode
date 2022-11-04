
from typing import List
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        rst = 0
        G = -1
        M = -1
        P = -1
        for i, gar in enumerate(garbage):
            rst += len(gar)
            for g in gar:
                if g == 'G':
                    G = i
                elif g == 'M':
                    M = i
                else:
                    P = i
                    
        for i in range(G):
            rst += travel[i]

        for i in range(M):
            rst += travel[i]

        for i in range(P):
            rst += travel[i]
        
        return rst