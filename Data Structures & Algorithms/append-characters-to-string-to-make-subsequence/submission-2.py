class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        p1 = 0
        p2 = 0

        for p1 in range(len(s)):
            if p2 < len(t) and s[p1] == t[p2]:
                p2 += 1 
        
        return len(t) - p2