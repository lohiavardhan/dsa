class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        used = 0
        l = 0 
        r = len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            
            if used == 1:
                return False
            
            if s[l + 1] == s[r]:
                l += 1
                used = 1
                continue
            elif s[r - 1] == s[l]:
                r -= 1
                used = 1
                continue
            else:
                return False
        
        return True
                
            
            