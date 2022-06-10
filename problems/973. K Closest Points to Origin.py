from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.method2(points, k)
    
    def method1(self, points, k):
        """
        Quick Select
        """
        
    def method2(self, points, k):
        """
        Binary search
        """
        #### step 1: preprocess
        dis2 = [0] * len(points)
        for i, (x, y) in enumerate(points):
            dis2[i] = x*x + y*y
        
        left = min(dis2)
        right = max(dis2)
        
        while left < right:
            mid = left + (right - left) // 2
            count = self.count_not_larger(dis2, mid)
            if count >= k:
                right = mid
            else:
                left = mid + 1
                
        rst = []
        for i in range(len(points)):
            if dis2[i] <= left:
                rst.append([points[i]])
        return rst
                
    
    def count_not_larger(self, dis2, val):
        """
        Return the count of points with dis2 value not larger than val
        """
        count = 0
        for m in dis2:
            if m <= val:
                count += 1
        
        return count 
        
"""
Thoughts:
1. KD tree?

"""

if __name__ == '__main__':
    points = [[1,3],[-2,2]]
    k = 1
    rst = Solution().kClosest(points, k)
    print(rst)
