import heapq
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        heapq
        """
        if startFuel >= target:
            return 0
        
        hq = []
        cur_fuel = startFuel
        cur_dis = 0
        i = 0
        count = 0
        
        stations.append([target, 0])
        
        n = len(stations)
        while i < n:
            ## if can reach station i without adding gas at station i - 1
            if cur_fuel >= stations[i][0]:
                heapq.heappush(hq, -stations[i][1])
                i += 1
            else:
                ## while cannot reach station i, virtually add gas from past stations that have not been added gas yet
                ## from most gas to fewest gas.
                while hq and cur_fuel < stations[i][0]:
                    count += 1
                    cur_fuel -= hq[0]
                    heapq.heappop(hq)
                    
                if not hq and cur_fuel < stations[i][0]:
                    return -1
            
        return count
                
if __name__ == '__main__':
    target = 100
    startFuel = 10
    stations = [[10,60],[20,30],[30,30],[60,40]]
    rst = Solution().minRefuelStops(target, startFuel, stations)
    print(rst)