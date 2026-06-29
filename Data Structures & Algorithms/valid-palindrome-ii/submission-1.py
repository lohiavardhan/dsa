class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        used = 0
        l = 0 
        r = len(s) - 1

        def isPalindrome(x, y):
            while x <= y:
                if s[x] != s[y]:
                    return False
                
            return True

        while l <= r:
            print(s[l], s[r], l, r, used)
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            
            if used == 1:
                return False
            
            return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)

        return True
                
            
            