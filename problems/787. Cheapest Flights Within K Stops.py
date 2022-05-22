

import heapq
from typing import List


import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #return self.dijkstra(n, flights, src, dst, k)
        return self.bellman_ford(n, flights, src, dst, k)
        
    def bellman_ford(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            tem = prices[:]
            for s, d, p in flights:
                if tem[s] < float('inf'):
                    tem[d] = min(tem[d], prices[s] + p)
            prices = tem
        if prices[dst] == float('inf'):
            return -1
        else:
            return prices[dst]
        
        
        
    def dijkstra(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Time Limit Exceeded
        """
        self.build_graph(n, flights)
        hq = [(0, src, -1)]
        heapq.heapify(hq)
        
        while hq:
            price, city, stops = heapq.heappop(hq)
            if city == dst:
                return price

            if stops >= k:
                continue
            #prices[city] = price

            for des, prc in self.adlist[city]:
                #if price + prc < prices[des]:
                
                heapq.heappush(hq, (price + prc, des, stops + 1))
            
        return -1
    
    def build_graph(self, n, flights):
        """
        build an adjacent list self.adlist. A list of list.
        """
        self.adlist = [[] for _ in range(n)]
        for flight in flights:
            frm, to, price = flight
            self.adlist[frm].append((to, price))
            

if __name__ == '__main__':
    s = Solution()
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    rst = s.findCheapestPrice(n, flights, src, dst, k)
    print(rst)

