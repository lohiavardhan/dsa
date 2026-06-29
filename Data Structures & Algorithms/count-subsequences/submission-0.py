class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        memo = {}
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(s) and j == len(t):
                return 1
            elif i == len(s):
                return 0
            
            res = dfs(i + 1, j)
            if j < len(t) and s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)
