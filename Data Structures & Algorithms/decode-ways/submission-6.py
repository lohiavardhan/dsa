class Solution:
    def numDecodings(self, s: str) -> int:
        

        def dfs(l, r):
            
            if r >= len(s) or l > r:
                return 0
            if int(s[l: r + 1]) > 26:
                return 0
            if '0' in s[l: r + 1]:
                return 0

            if int(s[l: r + 1]) == 1 or int(s[l: r + 1]) == 2:
                return 1 + dfs(l, r + 1)
            else:
                return 1 + dfs(l + 1, r + 1)
        
        return dfs(0, 0)
