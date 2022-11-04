
class Solution:
    def largestPalindromic(self, num: str) -> str:
        from collections import Counter, deque
        counter = Counter(num)
        if counter['0'] == len(num):
            return '0'
        dq = deque()
        maxv = -1
        for i in range(10):
            if counter[str(i)] % 2 == 1:
                maxv = i
        
        ## the middle value
        if maxv > -1:
            dq.append(str(maxv))
            counter[maxv] -= 1
        
        ## add 0s, check whether we can add 0 (avoid leading 0)
        cando = False
        for i in range(1, 10):
            if counter[str(i)] >= 2:
                cando = True
                break
        
        if cando:
            if maxv == -1:
                dq = ['0'] * counter['0']
                dq = deque(dq) 
            elif counter['0'] >= 2 :
                v = counter['0'] // 2
                dq.extendleft(['0'] * v)
                dq.extend(['0'] * v)

            
        for i in range(1, 10):
            v = counter[str(i)] // 2
            for _ in range(v):
                dq.append(str(i))
                dq.appendleft(str(i))
        #print(counter)
        return ''.join(dq)