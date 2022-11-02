from typing import List
from collections import Counter
from bisect import bisect_right
import math
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        Time: O(n^1.5 * logn)
        """
        arr.sort()
        counter = Counter(arr)
        
        ## binary_search
        for i in range(1, len(arr)):
            idx = bisect_right(arr, math.sqrt(arr[i]))
            for j in range(idx):
                need = arr[i] / arr[j]

                if need in counter:
                    acc = counter[arr[j]] * counter[need]
                    if need != arr[j]:
                        acc *= 2 
                    counter[arr[i]] += acc

        rst = 0
        for c in counter.values():
            rst += c
        
        M = 10**9+7
        return rst % M
    
    
    
if __name__ == '__main__':
    arr = [18,3,6,2] #[2,4,5,10] #[18,3,6,2]
    rst = Solution().numFactoredBinaryTrees(arr)
    print(rst)

