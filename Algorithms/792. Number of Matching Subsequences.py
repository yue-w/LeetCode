from typing import List
from collections import Counter
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        #return self.method1(s, words) ## naive method
        #return self.method2(s, words) ## acceptable method
        return self.method3(s, words) ## preferred method
        
    def method1(self, s, words):
        """
        Brute force.
        Time: O((M+N)*k), where M = len(s) and N = len(words[i]), and k = len(words)
        Space: O(1)
        """
        
        def subseq(s, word):
            if len(word) > len(s):
                return False
            i = 0
            for j in range(len(s)):
                if s[j] == word[i]:
                    i += 1
                if i == len(word):
                    return True

            return False
            
        counter = Counter(words)
        
        rst = 0
        for word in counter.keys():
            if subseq(s, word):
                rst += counter[word]
         
        return rst
    
    def method2(self, s, words):
        """
        Binary search.
        Time: O((log(M) * N * k)), where M = len(s) and N = len(words[i]), and k = len(words)
        Space: O(M)
        """
        import bisect
        def bi_search(char, curindex):
            """
            Use binary search to search whether there is an index of char that is larger than curindex
            """
            
#             ####The codes below implement the binary search. We can call bisect instead
#             row_index = ord(char) - ord('a')
#             array = indextable[row_index]
#             ## return False if empty or largest index is too small
#             if not array or array[-1] <= curindex:
#                 return False, -1
#             low = 0 
#             high = len(array) - 1
#             while low < high:
#                 mid = low + (high - low) // 2
#                 if array[mid] > curindex:
#                     high = mid
#                 else:
#                     low = mid + 1
            
#             return True, array[low]

            #### The codes below call the bisect library
            row_index = ord(char) - ord('a')
            array = indextable[row_index]
            ## return False if empty or largest index is too small
            if not array or array[-1] <= curindex:
                return False, -1
            idx = bisect.bisect_right(array, curindex + 1)
            if idx == len(array):
                return False, -1
            return True, array[idx]
        
        def subseq(word):
            """
            Binary search.
            From the row corresonding to word in indextable, find the smallest 
            index that is larger than curindex
            """
            curindex = -1
            for char in word:
                found, curindex = bi_search(char, curindex)
                if not found:
                    return False
            return True


        indextable = [[] for _ in range(26)]
        for i in range(len(s)):
            indextable[ord(s[i]) - ord('a')].append(i)
        
        
        counter = Counter(words)
        
        rst = 0
        for word in counter.keys():
            if subseq(word):
                rst += counter[word]
         
        return rst
    
    def method3(self, s, words):
        """
        Reference: https://youtu.be/2eDAImbp8C4
        Time: O(n * k)
        Space: O(m)
        State machine
        """
        #### nxt_idx with dimension (len(s) * 26), nxt_idx[i][j] is at index i, look right, what
        #### is the index of letter x (x from a to z) in s 
        ## make s 1 indexed, the first index 0 is dummy index so that the first letter in
        ## s can also been seen when looked right
        m = len(s)
        s = '*' + s
        nxt_idx = [[] for _ in range(len(s))]
        nxt_idx[-1] = [-1] * 26

        #### construct the table nxt_idx (reversely)
        for i in range(m, 0, -1):
            nxt_idx[i-1] = nxt_idx[i][:]
            nxt_idx[i-1][ord(s[i]) - ord('a')] = i

        counter = Counter(words)
        
        rst = 0
        for word in counter.keys():
            idx = 0
            found = True
            for w in word:
                idx = nxt_idx[idx][ord(w) - ord('a')]
                if idx == -1:
                    found = False
                    break
            if found:
                rst += counter[word]
         
        return rst
                

if __name__ == '__main__':
    s = "abcde"
    words = ["a","bb","acd","ace"]
    rst = Solution().numMatchingSubseq(s,words)
    print(rst)
        

            