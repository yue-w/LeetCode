from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        max(O(logm), O(logn))
        O(1)
        """
        m, n = len(matrix), len(matrix[0])
        """
        1: for the first column, find the largest element that is not larger than target, get the row number
        """
        low, high = 0, m - 1
        while low < high:
            mid = low + (high - low + 1) // 2
            if matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid 
            
        """
        2. for the row find in step 1, do binary search
        """
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[low][mid] == target:
                return True
            if matrix[low][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
        

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    rst =s.searchMatrix(matrix, target)
    print(rst)
            
        