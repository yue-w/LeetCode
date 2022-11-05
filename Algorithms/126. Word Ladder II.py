
from collections import deque, defaultdict
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        dictionary = set(wordList)
        dictionary.add(beginWord)
        if not endWord in dictionary:
            return []
        
        
        ## adjacent word (word reachable by flipping one letter)
        adjwords = defaultdict(list)
        
        for word in dictionary:
            for i in range(len(word)):
                for j in range(26):
                    newchar = chr(ord('a') + j)
                    newword = word[:i] + newchar + word[i+1:]
                    if newword == word:
                        continue
                    if newword in dictionary:
                        adjwords[word].append(newword)
        
        prevword = defaultdict(set) 
        
        dq = deque()
        dq.append(beginWord)
        visited = set()
        
        found = False
        while dq:
            visiting = set()
            for _ in range(len(dq)):
                word = dq.popleft()
                for newword in adjwords[word]:
                    if newword == endWord:
                        found = True
                    if newword in visited:
                        continue
                    prevword[newword].add(word)
                    visiting.add(newword)               

            for nv in visiting:
                visited.add(nv)  
                dq.append(nv)
            if found:
                break
        
        if not found:
            return []
        
        self.rst = []
        path = [endWord]
        ## from the end word, trace back to find the all the words that led to the end word.
        self.dfs(path, prevword, endWord, beginWord)
        return self.rst

    def dfs(self, path, prevword, curword, beginWord):
        """
        Use dfs to trace back from endword to the beginword.
        """
        if curword == beginWord:
            pathcp = path[:]
            pathcp.reverse()
            self.rst.append(pathcp[:])
            return

        for pre in prevword[curword]:
            path.append(pre)
            self.dfs(path, prevword, pre, beginWord)
            path.pop()



        
if __name__ == '__main__':
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot","dot","dog","lot","log","cog"]
    # rst = Solution().findLadders(beginWord, endWord, wordList)
    # print(rst)

    beginWord = "red"
    endWord = "tax"
    wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
    
    rst = Solution().findLadders(beginWord, endWord, wordList)
    expected = [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]
    print(f"Result:{rst}")
    print(f'Expected:{expected}')