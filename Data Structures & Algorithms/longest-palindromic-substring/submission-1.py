class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resL = 0
        resI = 0
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] =True
                    if (j-i+1 > resL):
                        resI = i
                        resL = j-i+1
        return s[resI:resI+resL]


