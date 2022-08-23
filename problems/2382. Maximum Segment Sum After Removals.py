
from typing import List
from sortedcontainers import SortedList
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        """
        Sorted List
        Reference:
        https://youtu.be/sB-WTpNpOwE
        """
        n = len(nums)
        
        prefixsum = [0] * n
        prefixsum[0] = nums[0]
        for i in range(1, n):
            prefixsum[i] = prefixsum[i-1] + nums[i]
        
        ## Sorted List, first element is start of a segment, second element is end of a segment 
        segments = SortedList()
        segments.add((0, n-1))
        
        ## sorted List, stores sums of segments, when a segments is splited, remove and
        ## updates its corresponding segsum
        segsums = SortedList()
        segsums.add(prefixsum[n-1])
        
        rst = []
        for r in removeQueries:
            ## from all the sorted segments, find the last one that is smaller than or equal to r     
            idx = segments.bisect_right((r, n)) - 1 
        
            ## get the segment and get its subsum
            start, end =  segments[idx]
            segments.remove((start, end))


            ## split the segment if the segment can be splitted
            if start == 0:
                orisum = prefixsum[end]
            else:
                orisum = prefixsum[end] - prefixsum[start - 1] 
            ## remove and update segmentsum
            segsums.remove(orisum)

            ## if can split more
            if start <= r - 1:
                segments.add((start, r - 1))
                if start == 0:
                    leftsum = prefixsum[r - 1]
                else:
                    leftsum = prefixsum[r - 1] - prefixsum[start - 1]
                segsums.add(leftsum) 
            
            ## if can split more
            if r + 1 <= end:
                segments.add((r+1, end))
                rightsum = prefixsum[end] - prefixsum[r]
                segsums.add(rightsum)

            if segsums:
                maxsum = segsums[-1]
            else:
                maxsum = 0
            rst.append(maxsum)
            
 
        return rst

if __name__ == '__main__':
    # nums = [1,2,5,6,1]
    # removeQueries = [0,3,2,4,1]

    nums = [3,2,11,1]
    removeQueries = [3,2,1,0]
    rst = Solution().maximumSegmentSum(nums, removeQueries)
    print(rst)