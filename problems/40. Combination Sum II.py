from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        rst = []
        curr = []
        candidates.sort()
        ## the following 2 dfs method use different ideas to remove duplication
        self.dfs1(candidates, rst, curr, 0, target)
        #self.dfs2(candidates, rst, curr, 0, target)
        return rst
    
    def dfs(self, candidates, rst, curr, index, remain):
        """
        Fist method to avoid duplication.
        """
        ## bace case
        if remain == 0:
            rst.append(curr[:])
            return
        if remain < 0:
            return
        
        i = index
        while i < len(candidates):
            curr.append(candidates[i])
            self.dfs(candidates, rst, curr, i + 1, remain - candidates[i])
            ## shift pointer to avoid duplication
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            ## backing track
            curr.pop()
            i += 1
        
    def dfs2(self, candidates, rst, curr, index, remain):
        """
        Second method to avoid duplication.
        reference: 
        https://github.com/wisdompeak/LeetCode/tree/master/DFS/040.Combination-Sum-II
        https://www.youtube.com/watch?v=IEh2ATqiH_0
        """
        ## bace case
        if remain == 0:
            rst.append(curr[:])
            return
        if remain < 0:
            return
        
        for i in range(index, len(candidates)):
            ## shift pointer to avoid duplication
            ## When candidates[i] == candidates[i-1],
            ## only when i is the fist element to be considerred in this recursion can it be used. 
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            curr.append(candidates[i])
            self.dfs(candidates, rst, curr, i + 1, remain - candidates[i])
            ## backing track
            curr.pop()
            i += 1
        
if __name__ == '__main__':
    candidates = [2,5,2,1,2]
    target = 5
    rst = Solution().combinationSum2(candidates, target)
    print(rst)