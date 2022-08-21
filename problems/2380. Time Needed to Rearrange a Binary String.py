


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        satisfied = False
        rst = 0
        string = [char for char in s]
        n = len(s)
        while not satisfied:
            satisfied = True
            rst += 1
            i = 0
            while i < n:
                if i + 1 < n and string[i] == '0' and string[i+1] == '1':
                    satisfied = False
                    string[i] = '1'
                    string[i + 1] = '0'
                    i += 2
                else:
                    i += 1
                
        return rst - 1