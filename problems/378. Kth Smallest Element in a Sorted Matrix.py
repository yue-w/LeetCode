
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix) 
        low = matrix[0][0] 
        up = matrix[n-1][n-1] 
        while low < up:
            mid = low + (up - low) // 2
            count = self.count_not_larger(matrix, mid)
            if count < k:
                low = mid + 1
            else:
                up = mid
        return low
        
    def count_not_larger(self, matrix, val):
        n = len(matrix)
        count = 0
        i = n - 1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= val:
                count += i + 1
                j += 1
            else:
                i -= 1
        return count