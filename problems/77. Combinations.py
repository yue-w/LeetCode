
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        rst = []
        curr = []
        self.recursion(rst, curr, 1, n, k)
        return rst
    def recursion(self, rst, curr, index, n, k):
        if len(curr) == k:
            rst.append(curr[:])
            return 
        
        for i in range(index, n + 1):
            curr.append(i)
            self.recursion(rst, curr, i + 1, n, k)
            curr.pop()

if __name__ == '__main__':
    s = Solution()
    n = 4
    k = 2
    rst = s.combine(n, k)
    print(rst)