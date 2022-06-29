from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #return self.method1(words, order)
        return self.method2(words, order) ## preferred method
    def method1(self, words, order):
        """
        Use a dictionary as hash
        """
        dic = {}
        for i, char in enumerate(order):
            dic[char] = i
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            j1 = 0
            j2 = 0
            while j1 < len(word1) and j2 < len(word2):
                if dic[word1[j1]] < dic[word2[j2]]:
                    break
                elif dic[word1[j1]] == dic[word2[j2]]:
                    j1 += 1
                    j2 += 1
                else:
                    return False
            if j2 == len(word2) and j1 < len(word1):
                return False
                
        
        return True
        
    def method2(self, words, order):
        """
        Use a lookup taboe as hash.
        Preferred method
        """
        table = [0] * len(order)
        for i, char in enumerate(order):
            index = ord(char) - ord('a')
            table[index] = i
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            j1 = 0
            j2 = 0
            while j1 < len(word1) and j2 < len(word2):
                if table[ord(word1[j1]) - ord('a')] < table[ord(word2[j2]) - ord('a')]:
                    break
                elif table[ord(word1[j1]) - ord('a')] == table[ord(word2[j2]) - ord('a')]:
                    j1 += 1
                    j2 += 1
                else:
                    return False
            if j2 == len(word2) and j1 < len(word1):
                return False
                
        
        return True

if __name__ == '__main__':
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    rst = Solution().isAlienSorted(words, order)
    print(rst)