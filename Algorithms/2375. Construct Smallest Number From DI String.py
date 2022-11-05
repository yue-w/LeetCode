
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        Search.
        DFS
        backtracking
        """
        def dfs(curr, idx):
            if len(curr) == n + 1:
                curr = [str(i) for i in curr]
                self.rst = ''.join(curr)
                return True
            
            if pattern[idx] == 'D':
                for nxt in range(curr[-1]-1, 0, -1):
                    if nxt in seen:
                        continue
                    seen.add(nxt)
                    curr.append(nxt)
                    if dfs(curr, idx+1):
                        return True
                    seen.remove(nxt)
                    curr.pop()
            else:
                for nxt in range(curr[-1]+1, 10):
                    if nxt in seen:
                        continue
                    seen.add(nxt)
                    curr.append(nxt)
                    if dfs(curr, idx+1):
                        return True
                    seen.remove(nxt)
                    curr.pop()
                
                
            return False
        n = len(pattern)
        for num in range(1, 10):   
            seen = set([num])
            if dfs([num], 0):
                return self.rst