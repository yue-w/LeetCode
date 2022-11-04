
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        dp[i][j]: whether s[:i+j+1] is formed by an interleaving of s1[:i+1] 
        and s2[:j+1]      
        """
         
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n3 != (n1 + n2):
            return False
        dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        
        ## make it 1 indexed to make edge case easier
        s1 = '*' + s1
        s2 = '*' + s2
        s3 = '*' + s3
        dp[0][0] = True
        for i in range(1, n1+1):
            ## both the following lines work 
            #dp[i][0] = (dp[i-1][0] and s1[i] == s3[i])
            dp[i][0] = (s1[:i+1] == s3[:i+1])

        for j in range(1, n2+1):
            ## both the following lines work 
            #dp[0][j] = (dp[0][j-1] and s2[j] == s3[j])
            dp[0][j] = (s2[:j+1] == s3[:j+1])
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):             
                if s3[i + j] == s1[i] and dp[i-1][j] == True:
                    dp[i][j] = True  
                elif s3[i + j] == s2[j] and dp[i][j-1] == True:
                    dp[i][j] = True
 
        return dp[-1][-1]
        
    

if __name__ == '__main__':

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    rst = Solution().isInterleave(s1, s2, s3)
    print(rst)