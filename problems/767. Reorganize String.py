
from collections import defaultdict
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(int)
        for i in range(len(s)):
            counter[s[i]] += 1
        
        heap = [(-freq, key) for key, freq in counter.items()]
        heapq.heapify(heap)
        
        rst = []
        while heap:
            freq1, chr1 = heapq.heappop(heap)
            freq1 += 1
            rst.append(chr1)
            if not heap:
                if freq1 < 0:
                    return ''
                else:
                    break
            else:
                freq2, chr2 = heapq.heappop(heap)
                if chr2 == chr1:
                    return ''
                rst.append(chr2)
                freq2 += 1
            
            if freq1 < 0:
                heapq.heappush(heap, (freq1, chr1))
            
            if freq2 < 0:
                heapq.heappush(heap, (freq2, chr2))
                
        return ''.join(rst)
        
        
        