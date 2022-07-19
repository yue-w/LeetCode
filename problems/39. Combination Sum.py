
from typing import List
import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time: O(2^n)
        Space: O(n)
        """
        candidates.sort()
        rst = []
        curr = []
        def dfs(index, cur_sum, curr):
            ## base case
            if cur_sum == target:
                rst.append(tuple(curr[:]))
                return
            if cur_sum > target:
                return
            
            for i in range(index, len(candidates)):
                curr.append(candidates[i])
                new_cur_sum = cur_sum + candidates[i]
                
                dfs(i, new_cur_sum, curr)
                ## backtracking
                curr.pop()
            
        dfs(0, 0, curr)
        return rst



if __name__ == '__main__':
    solution = Solution()
    candidates = [2,1]
    target = 5
    rst = solution.combinationSum(candidates, target)
    print(rst)