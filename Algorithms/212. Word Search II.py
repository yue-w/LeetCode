
from typing import List

class TrieNode:
    def __init__(self):
        self.nxt = [None] * 26
        self.isword = False
        ## How many word pass through this node. Used for deleting node
        self.count = 0
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(curr, row, col, cur_node):
            ## base case
            if not cur_node.nxt[ord(board[row][col]) - ord('a')]:
                return
            if cur_node.nxt[ord(board[row][col]) - ord('a')].count == 0:
                return
            
            cur_node = cur_node.nxt[ord(board[row][col]) - ord('a')]
            
            curr.append(board[row][col])
            
            ## base case
            if cur_node.isword:
                rst.add(''.join(curr))
                cur_node.isword = False
                del_node(curr)
            
            for dr, dc in dirs:
                if row + dr < 0 or row + dr >= M or col + dc < 0 or col + dc >= N:
                    continue
                char = board[row+dr][col+dc]
                if visited[row+dr][col+dc]:
                    continue
                visited[row+dr][col+dc] = 1
                dfs(curr, row+dr, col+dc, cur_node)
                visited[row+dr][col+dc] = 0
            
            curr.pop()
            
            
        def del_node(curr):
            curr_node = root
            for char in curr:
                curr_node = curr_node.nxt[ord(char) - ord('a')]
                curr_node.count -= 1
            
            
            
        ## step 1: build trie
        root = TrieNode()
        for word in words:
            curr_node = root
            for w in word:
                idx = ord(w) - ord('a')
                if not curr_node.nxt[idx]:
                    curr_node.nxt[idx] = TrieNode()
                curr_node = curr_node.nxt[idx]
                curr_node.count += 1
            curr_node.isword = True
            
        
        ## step 2: DFS
        M = len(board)
        N = len(board[0])
        
        visited = [[0 for _ in range(N)] for _ in range(M)]
        rst = set()
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for row in range(M):
            for col in range(N):
                cur_node = root
                curr = [] #[board[row][col]]
                visited[row][col] = 1
                dfs(curr, row, col, cur_node)
                visited[row][col] = 0  
                
        
        return list(rst)
        

if __name__ == '__main__':

    board = [["a","a"]]
    words = ["aaa"]
    rst = Solution().findWords(board, words)
    print(rst)

    """
    [["o","a","b","n"],
    ["o","t","a","e"],
    ["a","h","k","r"],
    ["a","f","l","v"]]


    ["oa","oaa"]



    """