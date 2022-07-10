

class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        if start.count('L') != target.count('L'):
            return False
        if start.count('R') != target.count('R'):
            return False
        
        n = len(start)
        index = 0
        j = 0
        for index in range(n):
            if target[index] != 'L':
                continue
            else:
                j = max(j, index)
            
            while j <= n:
                if j == n:
                    return False
                if start[j] == 'R':
                    return False
                if start[j] == '_':
                    j += 1
                else:
                    j += 1
                    break  
                    
        ## find R
        j = n - 1
        for index in range(n - 1, -1, -1):
            if target[index] != 'R':
                continue
            else:
                j = min(j, index)
            
            while j >= -1:
                if j == -1:
                    return False
                if start[j] == 'L':
                    return False
                if start[j] == '_':
                    j -= 1
                else:
                    j -= 1
                    break    
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