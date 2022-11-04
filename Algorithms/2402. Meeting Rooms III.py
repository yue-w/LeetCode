
import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        Double heapq
        Reference: https://youtu.be/uH2hV4PlCss
        """
        meetings.sort()
        
        free = [i for i in range(n)]
        heapq.heapify(free)
        busy = [] # (free time, room number)
        counts = [0] * n
        
        for start, end in meetings:
            # if there are occupied rooms available now
            while busy and busy[0][0] <= start:
                time, room = heapq.heappop(busy)
                heapq.heappush(free, room)
                
            if free:
                room = heapq.heappop(free)
                counts[room] += 1
                heapq.heappush(busy, (end, room))
            else:
                time, room = heapq.heappop(busy)
                counts[room] += 1
                heapq.heappush(busy, (time + end - start, room))
        
        return counts.index(max(counts))
            