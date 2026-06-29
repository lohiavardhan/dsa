class Solution:
    def numDecodings(self, s: str) -> int:
        l = 0
        r = 0
        count = 0

        while l < len(s):
            if s[l] == '0':
                return 0
            
            if 1 <= int(s[l:r + 1]) <= 26 and r < len(s):
                count += 1
                r += 1
            else:
                l += 1
        
        return count


