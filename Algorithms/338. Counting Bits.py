from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        DP
        Time: O(n)
        Space: O(n)
        """
        rst = [0] * (n + 1)
        offset = 1
        
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
        
            rst[i] = 1 + rst[i - offset]
            
        return rst

"""
0:  0000
1:  0001
-
2:  0010 ## the following 2**1=1 numbers repeat the previouse 2 with a 1 added at a new bit
3:  0011
--
4:  0100 ## the following 2**2=4 numbers repeat the previouse 4 with a 1 added at a new bit
5:  0101
6:  0110
7:  0111
---
8:  1000 ## the following 2**3=8 numbers repeat the previouse 4 with a 1 added at a new bit

"""