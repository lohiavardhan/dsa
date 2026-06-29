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

            
        
        max_str = ''

        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i:j + 1]) and len(s[i:j + 1]) > len(max_str):
                    max_str = s[i:j + 1]
        
        return max_str