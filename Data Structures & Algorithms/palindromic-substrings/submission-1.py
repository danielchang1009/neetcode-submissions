class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0 
        sheet = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if (s[i] == s[j] and (j-i <=2 or sheet[i+1][j-1] == True)):
                    sheet[i][j] = True
                    res +=1
        return res 
        