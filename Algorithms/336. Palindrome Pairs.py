from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(check):
            """
            Helper function. Whether string is a palindrome
            Time: O(len(string))
            Space: O(1)
            """
            return check == check[::-1]
        
        rst = []
        ## use a hash map to check whether a string
        ## exist with O(1) time. Record the index of each string
        ## because we need to return their indexes.
        dic = {words[i]:i for i in range(len(words))}
        
        for index, string in enumerate(words):
            n = len(string)
            for i in range(n+1):
                prefix = string[:i]
                subfix = string[i:]

                if is_palindrome(prefix):
                    back = subfix[::-1]
                    if back != string and back in dic:
                        rst.append([dic[back], index])
                
                if i != n  and is_palindrome(subfix):
                    back = prefix[::-1]
                    if back != string and back in dic:
                        rst.append([index, dic[back]])
        
        return rst

if __name__ == '__main__':
    words = ["abcd","dcba","lls","s","sssll"]
    #words = ["a",""]
    
    words = ["abc","cba"]
    rst = Solution().palindromePairs(words)
    print(rst)