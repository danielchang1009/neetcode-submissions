class Solution:    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        for i in range(len(s)):
            l, r  =i-1, i+1 
            while l >= 0 and r < n and s[r] == s[l]:
                l -= 1
                r += 1
            temp = s[l+1:r]
            if len(temp) > len(res):
                res = temp 


            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            temp = s[l+1:r]
            if len(temp) > len(res):
                res = temp 
        return res



        