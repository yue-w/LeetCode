from typing import List
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
        Time: O(n^2 * log(n))
        Space: O(n^2)
        """
        ROW = len(mat)
        COL = len(mat[0])
        ## use a 2-d prefixsum to compute the sum of an area.
        ## make it 1-indexed. Coordinate in prefixsum matrix will minus 1 to transform to the coordinate
        ## in the original matrix (because prefixsum matrix is 1-indexed)
        prefixsum = [[0 for _ in range(COL + 1)] for _ in range(ROW + 1)]
        for row in range(1, ROW + 1):
            for col in range(1, COL + 1):
                prefixsum[row][col] = prefixsum[row - 1][col] + prefixsum[row][col - 1] - prefixsum[row - 1][col - 1] + mat[row-1][col-1] 
        
        left = 0
        right = min(ROW, COL)
        while left < right:
            mid = left + (right - left + 1) // 2
            
            if self.exist(mat, mid, threshold, prefixsum):
                ## try larger (inclusive)
                left = mid
                
            else:
                ## try smaller
                right = mid - 1
            
        return left
    
    def exist(self, mat, width, threshold, prefixsum):
        ## whether there is a square with width of 'width' has a summation <= threshold
        ROW = len(mat)
        COL = len(mat[0])
        ## iterate the area with right bottom corner at (row, col)
        ## the coordinates below are 1-index
        ## coordinate in the matrix will plus 1 to transform to the coordinate
        ## in the prefixsum matrix (because prefixsum matrix is 1-indexed)
        for row in range(width, ROW + 1):
            for col in range(width, COL + 1):
                sumv = prefixsum[row][col] - prefixsum[row - width][col] - prefixsum[row][col - width] + prefixsum[row - width][col - width]
                if sumv <= threshold:
                    return True
                
        return False
    
        
