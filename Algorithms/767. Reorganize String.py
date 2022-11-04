
from collections import defaultdict
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        rst = []
        
        freq = defaultdict(int)
        
        ## Because heapq prioritize min, we use negative number
        for char in s:
            freq[char] -= 1
        
        hq = []
        for char, count in freq.items():
            hq.append((count, char))
        heapq.heapify(hq)
        
        while hq:
            ## if there is only one type of character left: 
            if len(hq) == 1:
                ## if the only type of character has more than 1 count, return ''
                if hq[0][0] < -1:
                    return ''
                else:
                    rst.append(hq[0][1])
                    break
            else:           
                count1, char1 = heapq.heappop(hq)
                rst.append(char1)
                count1 += 1
                count2, char2 = heapq.heappop(hq)
                rst.append(char2)
                count2 += 1
                if count1 < 0:
                    heapq.heappush(hq, (count1, char1))
                if count2 < 0:
                    heapq.heappush(hq, (count2, char2))

        return ''.join(rst)
        