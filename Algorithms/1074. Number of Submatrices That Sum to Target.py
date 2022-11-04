from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        2d Prefix sum and Hash and squash a matrix
        Time: O(M*M*N)
        """
        M, N = len(matrix), len(matrix[0])
        rst = 0
        for i in range(M):
            rowsum = [0] * N 
            # squash rows i to j
            for j in range(i, M):
                for k in range(N):
                    rowsum[k] += matrix[j][k]
                    
                prefixsum = 0
                dic = {0:1}
                for k in range(N):
                    prefixsum += rowsum[k]
                    need = prefixsum - target
                    rst += dic.get(need, 0)
                    dic[prefixsum] = dic.get(prefixsum, 0) + 1
        return rst
                    
                
                