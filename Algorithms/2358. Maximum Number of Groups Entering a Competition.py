
from typing import List
from math import sqrt
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        #return self.method1(grades)
        #return self.method2(grades) ## preferred method
        return self.method3(grades)
        
    
    def method1(self, grades):
        """
        Time: O(sqrt(n))
        Space: O(1)
        """
        n = len(grades)
        rst = 0
        curr = 0
        remain = n
        while remain > curr:
            curr += 1
            rst += 1
            remain -= curr
        
        return rst
    
    def method2(self, grades):
        """
        Binary search
        Time: O(log(sqrt(n))).
        1 + 2 + ... + k = (1 + k) * k / 2
        """
        n = len(grades)
        left = 0
        right = 1000 ## because grade.length <= 1e5
        while left < right:
            mid = left + (right - left + 1) // 2
            if (mid + 1) * mid // 2 <= n:
                left = mid
            else:
                right = mid - 1
            
        return left
        
    def method3(self, grades):
        """
        Time: O(1)
        Space: O(1)
        (1+k)k/2 <= n
        (1+k)k <= 2n
        k^2 + k + 1/4 <= 2*n + 1/4
        (k+1/2)^2 <= 2*n + 1/4
        k <= sqrt(2*n+1/4) - 1/2
        """
        n = len(grades)
        k = int(sqrt(2 * n + 0.25) - 0.5)
        return k
        