class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(s) and j == len(p):
                return True
            if j == len(p) - 1 and p[j] == '*':
                return True
            if i == len(s) and j != len(p):
                return False
            
            res = False
            if s[i] == p[j] or p[j] == '.':
                res = dfs(i + 1, j + 1)
            elif p[j] == '*':
                res = dfs(i + 1, j) or dfs(i + 1, j + 1)
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)