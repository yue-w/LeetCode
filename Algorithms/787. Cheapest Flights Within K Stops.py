

import heapq
from typing import List


import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #return self.dijkstra(n, flights, src, dst, k)
        #return self.bellman_ford(n, flights, src, dst, k)
        return self.dp(n, flights, src, dst, k)
        
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
        
    def dp(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        dp[i][j]: take i flights, the cost to reach to city j from src.
        dp[i][j] = min{dp[i - 1][p] + price[p][j]} for all p if there is a flight from p to j
        """
        dp = [[float('inf') for _ in range(n)] for _ in range(k + 2)]
        
        ## if take 0 filight, the only reachable place is src itself
        dp[0][src] = 0
        
        rst = float('inf')
        for f in range(1, k + 2):
            ## for all city p and for all the cities reachable from p.
            ## this is the same of for all flights
            for tail, head, price in flights:
                dp[f][head] = min(dp[f][head], dp[f - 1][tail] + price )

        ## from all k values, get the smallest value
        rst = float('inf')
        for i in range(len(dp)):
            rst = min(rst, dp[i][dst])
        if rst == float('inf'):
            return -1
        else:
            return rst  
        
    def dijkstra(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        This implementation Time Limit Exceeded.
        Try https://www.youtube.com/watch?v=Q8oMHlThySQ&t=1300s,
        it is also dijkstra but not TLE.
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
    # n = 3
    # flights = [[0,1,100],[1,2,100],[0,2,500]]
    # src = 0
    # dst = 2
    # k = 1

    # n = 5
    # flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
    # src = 0
    # dst = 2
    # k = 2
    n = 7
    flights = [[0,3,7],[4,5,3],[6,4,8],[2,0,10],[6,5,6],[1,2,2],[2,5,9],[2,6,8],[3,6,3],[4,0,10],[4,6,8],[5,2,6],[1,4,3],[4,1,6],[0,5,10],[3,1,5],[4,3,1],[5,4,10],[0,1,6]]
    src = 2
    dst = 4
    k = 1
    rst = s.findCheapestPrice(n, flights, src, dst, k)
    print(rst)

