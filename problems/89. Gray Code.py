from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        rst = [0]
        if n == 0:
            return rst
        
        for i in range(n):
            for j in range(len(rst)-1, -1, -1):
                rst.append(rst[j] | (1 << i))
        return rst

"""
Reference:
https://www.youtube.com/watch?v=K3_IvifT0pI
Steps to generate n-digit gray code from n - 1 digit gray code:
1. mirror the n - 1 digit gray code.
2. for the first half of the mirrored gray code, add 0 to the left.
3. for the second half the mirrored gray code, add 1 to the left. 
Example:
1 digit: 
    0
    1
2 digits:
                                   0                       00
mirror gray code of 1 digit -->    1  --> add 0 and 1  --> 01      
                                   1                       11
                                   0                       10
"""