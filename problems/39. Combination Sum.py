
from typing import List
import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rst = []
        curr = []
        self.dfs(candidates, target, 0, rst, curr)
        return rst

    def dfs(self, candidates, remain, i, rst, curr):
        ## Base case
        if remain == 0:
            rst.append(curr[:])
            return
        if i == len(candidates) or remain < 0:
            return
        ## Include candidates[i]
        curr.append(candidates[i])
        self.dfs(candidates, remain-candidates[i], i, rst, curr)
        ## does not include candidates[i]
        curr.pop()
        self.dfs(candidates, remain, i + 1, rst, curr)



if __name__ == '__main__':
    solution = Solution()
    candidates = [2,1]
    target = 5
    rst = solution.combinationSum(candidates, target)
    print(rst)