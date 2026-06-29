class Solution:
    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(string):
            l = 0
            r = len(string) - 1

            while(l < r):
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        if len(s) == 1:
            return s
        if len(s) == 2:
            if isPalindrome(s):
                return s
            else:
                return s[0] 
            
        
        max_str = ''

        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i:j]) and len(s[i:j]) > len(max_str):
                    max_str = s[i:j]
        
        return max_str