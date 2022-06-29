from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.method1(nums, target)
    
    def method1(self, nums, target):
        """
        DP (knapsack with hashing)
        """
        counter = {}
        counter[0] = 1
        
        for n in nums:
            counter_nxt = {}
            for c in counter:
                counter_nxt[c - n] = counter_nxt.get(c - n, 0) + counter[c]
                counter_nxt[c + n] = counter_nxt.get(c + n, 0) + counter[c]
            counter = counter_nxt
            

        return counter.get(target, 0)

if __name__ == '__main__':
    nums = [1,1,1,1,1]
    target = 3
    rst = Solution().findTargetSumWays(nums, target)
    print(rst)