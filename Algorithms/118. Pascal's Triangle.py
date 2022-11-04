from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        rst = [[1],[1,1]]
        for i in range(3, numRows + 1):
            tem = [1] * (len(rst[-1]) + 1)
            for j in range(len(rst)-1):
                tem[j+1] = rst[-1][j] + rst[-1][j+1]
            rst.append(tem[:])
        return rst
            
            