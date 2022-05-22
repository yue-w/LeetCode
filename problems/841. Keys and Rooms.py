from typing  import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:


        #return self.dfs(rooms)
        return self.bfs(rooms)

    def bfs(self, rooms):
        N = len(rooms)
        seen = [False] * N

        dq = deque()
        dq.append(0)

        while dq:
            for _ in range(len(dq)):
                room = dq.popleft()
                seen[room] = True
                keys = rooms[room]
                for key in keys:
                    if not seen[key]:
                        dq.append(key) 
        return sum(seen) == N



    def dfs(self, rooms):
        N = len(rooms)
        seen = [False] * N
        
        self.dfs_recursion(0, rooms, seen)
        
        
        return sum(seen) == N
    
    def dfs_recursion(self, room, rooms, seen):
        ## Base case
        if seen[room]:
            return
        
        seen[room] = True
        keys = rooms[room]
        for key in keys:
            self.dfs_recursion(key, rooms, seen)
        

if __name__ == '__main__':

    s = Solution()
    rooms = [[1],[2],[3],[]]
    rst = s.canVisitAllRooms(rooms)
    print(rst)