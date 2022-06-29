from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        v = 1
        left = 0
        right = n - 1
        up = 0
        bottom = n - 1
        
        while v <= n * n:
            #### left to right
            col = left
            while col <= right:
                matrix[up][col] = v
                v += 1
                col += 1
            up += 1

            #### up to bottom
            row = up
            while row <= bottom:
                matrix[row][right] = v
                v += 1
                row += 1
            right -= 1

            #### right to left
            col = right
            while col >= left:
                matrix[bottom][col] = v
                v += 1
                col -= 1
            bottom -= 1

            #### bottom to up
            row = bottom
            while row >= up:
                matrix[row][left] = v
                v += 1
                row -= 1
            left += 1
        
        return matrix

if __name__ == '__main__':
    n = 3
    rst = Solution().generateMatrix(n)
    print(rst)