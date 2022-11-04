from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #return self.method1(candidates, target) # acceptable method to avoid duplicate
        return self.method2(candidates, target) # preferred method to avoid duplicate
    
    def method1(self, candidates, target):
        """
        Use a local set in dfs to avoid duplicate
        """
        def dfs(idx, curr, cursum):
            # base case
            if cursum == target:
                rst.append(curr[:])
                return
            if cursum > target:
                return
            visited = set()

            for i in range(idx, n):
                # if the previous occurance is not selected, this occurance will not be selected
                if candidates[i] in visited:
                    continue
                visited.add(candidates[i])
                curr.append(candidates[i])
                cursum += candidates[i]
                dfs(i + 1, curr, cursum)
                # backtracking
                curr.pop()
                cursum -= candidates[i]
                
            
        candidates.sort(reverse=True)
        rst = []
        n = len(candidates)
        dfs(0, [], 0)
        return rst
    
    def method2(self, candidates, target):
        """
        Avoid duplicate.
        Reference: https://github.com/wisdompeak/LeetCode/tree/master/DFS/040.Combination-Sum-II
        """
        def dfs(idx, curr, cursum):
            # base case
            if cursum == target:
                rst.append(curr[:])
                return
            if cursum > target:
                return

            for i in range(idx, n):
                # if the previous occurance is not selected, this occurance will not be selected
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                cursum += candidates[i]
                dfs(i + 1, curr, cursum)
                # backtracking
                curr.pop()
                cursum -= candidates[i]
                
            
        candidates.sort(reverse=True)
        rst = []
        n = len(candidates)
        dfs(0, [], 0)
        return rst
        
if __name__ == '__main__':
    candidates = [2,5,2,1,2]
    target = 5
    rst = Solution().combinationSum2(candidates, target)
    print(rst)