from typing import List
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        return self.method1(jobs, k)
    
    def method1(self, jobs, k):
        """
        Trim branch.
        """
        left = 0
        right = sum(jobs) * 2
        jobs.sort(reverse=True)
        while left < right:
            people = [0] * k
            mid = left + (right - left) // 2
            ## if it is possible to get a result this small, try even smaller
            if self.dfs(jobs, k, 0, people, mid):
                right = mid
            ## if it is not possible to get a result that small, try larger
            else:
                left = mid + 1
            
        return left
        
    def dfs(self, jobs, k, workindex, people, maxwork):
        ## base case
        if workindex == len(jobs):
            return True
        
        ## set up a flag to trim branches.
        ## if a some workers has not been assigned work yet, they are all equal (symmetrical),
        ## we only need to test one brunch. If this branch is not successful, all other branches 
        ## will not be successful.
        no_work_tried = False
        for i in range(k):
            if people[i] + jobs[workindex] <= maxwork:
                if people[i] == 0:
                    if no_work_tried:
                        continue
                    else:
                        no_work_tried = True
                        
                people[i] += jobs[workindex]
                if self.dfs(jobs, k, workindex + 1, people, maxwork):
                    return True
                ## backingtrack
                people[i] -= jobs[workindex]
        ## if non of the above dfs returned True, return False
        return False
    
    def method2(self, jobs, k):
        """
        State compress. Todo.
        reference: https://www.youtube.com/watch?v=vT1nhRyFfNo&t=2s
        """
        ## TODO