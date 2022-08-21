

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        rst = float('inf')
        curr = 0
        for i in range(len(blocks)):
            if blocks[i] == 'W':
                curr += 1
            
            ## remove 'W' if outside of window
            if i - k >= 0 and blocks[i - k] == 'W':
                curr -= 1
            
            ## if window is size k already
            if i - (k - 1) >= 0:
                rst = min(rst, curr)
        
        return rst
            