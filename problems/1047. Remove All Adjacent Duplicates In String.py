


class Solution:
    def removeDuplicates(self, s: str) -> str:
        #return self.stack(s)
        return self.two_pointers(s)
    
    def stack(self, s):
        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])

        
        return ''.join(stack)
    
    def two_pointers(self, s):
        string = [char for char in s]
        ## element before left (exclude) will be kept, the element at left will be overwritten.
        left = 0
        ## right is the index for exploring to the right
        right = 0
        while right < len(string):
            string[left] = string[right]
            if left > 0 and string[left - 1] == string[left]:
                left -= 2
            
            left += 1
            right += 1
            
        return ''.join(string[:left])

if __name__ == "__main__":
    s = Solution()
    string = "abbaca"
    print(s.removeDuplicates(string))


