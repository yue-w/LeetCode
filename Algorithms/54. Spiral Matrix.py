from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rst = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        size = len(matrix) * len(matrix[0])
        
        while len(rst) < size:
            ## left to right
            row = top
            col = left
            while col <= right and len(rst) < size:
                rst.append(matrix[row][col])
                col += 1
            top += 1
            
            ## up to bottom
            col = right
            row += 1
            while row <= bottom and len(rst) < size:
                rst.append(matrix[row][col])
                row += 1
            right -= 1
            
            ## right to left
            row = bottom
            col -= 1
            while col >= left and len(rst) < size:
                rst.append(matrix[row][col])
                col -= 1
            bottom -= 1    
                
            ## bottom to up
            col = left
            row -= 1
            while row >= top and len(rst) < size:
                rst.append(matrix[row][col])
                row -= 1
            left += 1
            
        return rst

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]] #[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    rst = s.spiralOrder(matrix)
    print(rst) #[1,2,3,4,8,12,11,10,9,5,6,7]