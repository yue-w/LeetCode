

class Solution(object):
    def canChange(self, start, target):
        """
        Use two pointers to check relative positions.
        """
        
        ## the count of L and R should be the same
        if start.count('L') != target.count('L'):
            return False
        if start.count('R') != target.count('R'):
            return False
        
        """
        The relative position of L and R should be the same, no interwine,
        i.e., the index of L and R in start and target should follow the following rules
        index of 'L' in start should be larger than the index of 'L' in target
        index of 'R' in start should be smaller than the index of 'R' in target
        """
        ## i point to start, j point to target.
        j = 0
        for i in range(len(start)):
            if start[i] == '_':
                continue
            
            while j < len(target) and start[i] != target[j]:
                j += 1
            
            ## if find violation, return False
            if start[i] == 'L' and i < j:
                return False
            
            if start[i] == 'R' and i > j:
                return False
            j += 1
            
        return True
        

                
            
if __name__ == '__main__':
    # start = "_L__R__RL"
    # target = "L_____RLR"
    # start = "_L__R__R_"
    # target = "L______RR"
    # start = "R_L_"
    # target = "__LR"
    start = "_R"
    target = "R_"
    rst = Solution().canChange(start, target)
    print(rst)