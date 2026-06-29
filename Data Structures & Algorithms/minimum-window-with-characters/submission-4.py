class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        
        l = 0

        need = defaultdict(int)
        have = defaultdict(int)
        res_l = 0
        res_r = float('inf')

        for char in t:
            need[char] += 1
        
        for r in range(len(s)):
            have[s[r]] += 1

            
            while all(have[i] >= need[i] for i in need.keys()):
                if (res_r - res_l + 1) > len(s[l:r + 1]):
                    res_r = r
                    res_l = l
                have[s[l]] -= 1
                l += 1
        
        if res_r == float('inf'):
            return ""
        return s[res_l : res_r + 1]