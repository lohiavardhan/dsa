class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        
        l = 0

        orig_s = s

        s = s.upper()
        t = t.upper()

        need = [0] * 26
        have = [0] * 26
        res_l = 0
        res_r = float('inf')

        for char in t:
            need[ord(char) - ord('A')] += 1
        
        for r in range(len(s)):
            have[ord(s[r]) - ord('A')] += 1

            
            while all(have[i] >= need[i] for i in range(26)):
                if (res_r - res_l + 1) > len(s[l:r + 1]):
                    res_r = r
                    res_l = l
                have[ord(s[l]) - ord('A')] -= 1
                l += 1
        
        return orig_s[res_l : res_r + 1]