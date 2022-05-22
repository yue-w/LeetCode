
from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        DFS, Hash
        """
        ans = []
        
        self.adlist = defaultdict(list)
        ### build adjancent list
        for ticket in tickets:
            fr, to = ticket
            self.adlist[fr].append(to)
        
        ## sort destiny?
        for key in self.adlist.keys():
            self.adlist[key].sort(reverse=True)
        
        #fr = self.adlist['JFK'][0]
        #ans.append('JFK')
        self.dfs('JFK', ans)
        ans.reverse()
        return ans
    
    def dfs(self, fr, ans): 
        ## Base case: no more trip
        if not self.adlist[fr]:
            ans.append(fr)
            return
        while self.adlist[fr]:
            nxt_fr = self.adlist[fr].pop()
            self.dfs(nxt_fr, ans)
        ans.append(fr)
        
if __name__ == '__main__':
    s = Solution()
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    ans = s.findItinerary(tickets)
    print(ans)
            