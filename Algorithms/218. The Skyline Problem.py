
from typing import List
from sortedcontainers import SortedDict

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ## start point == -1, end point == 1
        #buildings.sort()
        sweeplines = []
        for x1, x2, h in buildings:
            """
            Pay attention here. If two points have the same x:
                (1) if they are starting point, we want to process the one with 
                larger height first.
                (2) if they are endingpoint, we want to process the one with smaller
                height first.
            We make the height of entering point negative so that they come earlier
            in ascending order.
            """
            ## start point, we want to process larger height first. So we
            ## make -h to make larger height come first. 
            sweeplines.append((x1, -h))
            ## end point, we want to preocess smaller height first
            sweeplines.append((x2, h))
        
        ## sort by x, if x1==x2, sort by h.
        sweeplines.sort()
        rst = []
        heights = SortedDict()
        for x, h in sweeplines:
            ## start point
            if h < 0:
                h = -h
                count = heights.get(h, 0)
                heights[h] = count + 1
            ## end point
            else:
                heights[h] -= 1
                if heights[h] == 0:
                    del heights[h]
            if heights:
                ## heights is sorted in ascending order, get the largest (last) element.
                height, _ = heights.peekitem(-1)
            else:
                height = 0
            
            ## add height into rst in two cases: 1 rst is empty. 2. rst is 
            ## not empty, but height is not larger.
            if not rst or height != rst[-1][1]:
                rst.append([x, height])
 
        return rst

if __name__ == '__main__':
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    expected = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]#
    rst = Solution().getSkyline(buildings)
    print(f'Test 1:')
    print(f'Computed: {rst}')
    print(f'Expected: {expected}')

    buildings = [[0,2,3],[2,5,3]]
    expected = [[0,3],[5,0]]
    rst = Solution().getSkyline(buildings)
    print(f'Test 2:')
    print(f'Computed: {rst}')
    print(f'Expected: {expected}')

    buildings = [[1,2,1],[1,2,2],[1,2,3]]
    expected = [[1,3],[2,0]]
    rst = Solution().getSkyline(buildings)
    print(f'Test 3:')
    print(f'Computed: {rst}')
    print(f'Expected: {expected}')