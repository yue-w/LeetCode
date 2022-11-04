
from typing import List
from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Time: O(M*M*N*log(N))
        """

        M = len(matrix)
        N = len(matrix[0])
        
        
        ## if M > N we can transpose the matrix to reduce runing time (this section is optional)
        if M > N:
            matrix2 = list(map(list, zip(*matrix)))
            # matrix2 = [[0 for _ in range(M)] for _ in range(N)]
            # for i in range(M):
            #     for j in range(N):
            #         matrix2[j][i] = matrix[i][j]
            return self.maxSumSubmatrix(matrix2, k)
            
        
        rst = float('-inf')
        for i in range(M):
            rowsum = [0] * N 
            for j in range(i, M):
                for t in range(N):
                    rowsum[t] += matrix[j][t]
                presum = 0
                stlist = SortedList([0])
                for t in range(N):
                    presum += rowsum[t]
                    index = stlist.bisect_left(presum-k)
                    if index < len(stlist):
                        rst = max(rst, presum-stlist[index])
                    stlist.add(presum)
                    
        return rst
                