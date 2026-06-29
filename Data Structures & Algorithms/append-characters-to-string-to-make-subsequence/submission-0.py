class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        max_common = 0
        l = 0

        for r in range(len(s)):
            size = r - l + 1
            if s[l:r + 1] == t[0: size]:
                max_common = max(max_common, size)
            else:
                l = r
        
        return len(t) - max_common