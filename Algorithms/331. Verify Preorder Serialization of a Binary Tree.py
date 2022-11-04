


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        #return self.method1(preorder) ## stack
        return self.method2(preorder) ## preferred method. Trick to memorize.
        
        
    def method1(self, preorder):
        stack = []
        preorder = preorder.split(',')
        for t in preorder:
            stack.append(t)
            while len(stack) > 2 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
            
        return stack == ['#']
    
    def method2(self, preorder):
        """
        Use the following properties of a binary tree:
        normal nodes (including root) occupy 1 spot then provide 2 spots (thus increase spots by 1).
        leaves take 1 spot and provide 0 new spot (thus decrease spots by 1).
        During this process, spot cannot be less than 1
        In the end, spot is 0.
        """
        ## one slot for the root.
        spot = 1
        for t in preorder.split(','):
            if spot < 1:
                return False
            if t == '#':
                spot -= 1
            else:
                spot += 1
            
        
        return spot == 0
        
        
if __name__ == '__main__':
    preorder = "9,#,92,#,#"
    rst = Solution().isValidSerialization(preorder)
    print(rst)