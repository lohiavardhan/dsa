class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 2:
            if(s[0] == s[1]):
                return s
            else:
                return s[0]
        
        res = ''
        resLen = 0

        for i in range(len(s)):
            if len(s) % 2 == 0:
                l, r = i, i + 1
            else:
                l, r = i, i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if(r - l + 1 > resLen):
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
        return res

        